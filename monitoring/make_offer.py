#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Univerzální generátor nabídek pro Polarita s.r.o.
Použití: python make_offer.py <cesta_ke_slozce_klienta> [--markup 22] [--labor 4500]

Očekává: <slozka>/cart.csv (Schrack export, středník, UTF-8-sig)
Vytvoří: <slozka>/Nabidka_<klient>_<téma>.xlsx
"""
import csv, re, sys, os, argparse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def main():
    parser = argparse.ArgumentParser(description="Generátor nabídek Polarita s.r.o.")
    parser.add_argument("folder", help="Cesta ke složce klienta (obsahuje cart.csv)")
    parser.add_argument("--markup", type=float, default=22, help="Marže na materiálu v %% (výchozí: 22)")
    parser.add_argument("--labor", type=float, default=4500, help="Cena práce za kus (výchozí: 4500)")
    parser.add_argument("--client", help="Jméno klienta (jinak z názvu složky)")
    parser.add_argument("--topic", help="Téma nabídky (jinak z cart.csv nebo 'Elektroinstalace')")
    args = parser.parse_args()

    folder = args.folder.rstrip("\\/")
    cart_path = os.path.join(folder, "cart.csv")
    if not os.path.exists(cart_path):
        print(f"CHYBA: {cart_path} neexistuje")
        sys.exit(1)

    # Metadata
    client_name = args.client or os.path.basename(folder)
    topic = args.topic or "Elektroinstalace"
    markup = args.markup / 100.0
    labor_per_ks = args.labor

    # Parsuj cart.csv
    rows = []
    with open(cart_path, encoding="utf-8-sig") as f:
        for r in csv.reader(f, delimiter=";"):
            if not r or r[0].strip().startswith("Číslo") or r[0].strip() == "":
                continue
            num = r[0].strip('" ')
            try:
                qty = int(r[1])
            except (ValueError, IndexError):
                continue
            unit = r[2] if len(r) > 2 else "ks"
            name = r[3].strip('" ') if len(r) > 3 else ""
            # cena: "CZK 853,05" — bereme sloupec 5 (Cena), ne 7 (Součet)
            cena_str = r[5] if len(r) > 5 else "CZK 0"
            m = re.search(r"([\d.,]+)", cena_str.replace(" ", ""))
            if not m:
                continue
            cena_raw = float(m.group(1).replace(".", "").replace(",", "."))
            cena = round(cena_raw * (1 + markup), 2)
            rows.append((num, qty, unit, name, cena))

    if not rows:
        print("CHYBA: cart.csv neobsahuje žádné platné řádky")
        sys.exit(1)

    # Vytvoř xlsx
    wb = Workbook()
    ws = wb.active
    ws.title = "Nabídka"

    thin = Side(style="thin", color="999999")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    bold = Font(bold=True)
    fill_h = PatternFill("solid", fgColor="1F4E78")
    font_h = Font(bold=True, color="FFFFFF")

    # Header
    ws["A1"] = "POLARITA s.r.o."
    ws["A1"].font = Font(bold=True, size=16)
    ws["E1"] = f"NABÍDKA"
    ws["E1"].font = Font(bold=True, size=14)
    ws["A2"] = "IČ: 14180324 | DIČ: CZ14180324"
    ws["A3"] = f"Datum vystavení: {__import__('datetime').date.today().strftime('%d. %m. %Y')}"
    ws["E3"] = "Platnost nabídky: 30 dní"
    ws["A5"] = "Odběratel:"
    ws["A5"].font = bold
    ws["A6"] = client_name
    ws["E5"] = "Předmět:"
    ws["E5"].font = bold
    ws["E6"] = topic

    # Table header
    hdr_row = 8
    headers = ["#", "Objednací číslo", "Název položky", "Množství", "Jedn.", f"Cena/ks (Kč) +{args.markup:.0f}%", "Celkem (Kč)"]
    for c, h in enumerate(headers, 1):
        cell = ws.cell(hdr_row, c, h)
        cell.font = font_h
        cell.fill = fill_h
        cell.border = border
        cell.alignment = Alignment(horizontal="center")

    r = hdr_row + 1
    for i, (num, qty, unit, name, cena) in enumerate(rows, 1):
        ws.cell(r, 1, i).border = border
        ws.cell(r, 2, num).border = border
        ws.cell(r, 3, name).border = border
        ws.cell(r, 4, qty).border = border
        ws.cell(r, 5, unit).border = border
        ws.cell(r, 6, cena).border = border
        ws.cell(r, 6).number_format = "#,##0.00"
        ws.cell(r, 7, f"=D{r}*F{r}").border = border
        ws.cell(r, 7).number_format = "#,##0.00"
        r += 1

    mat_last = r - 1

    # Práce
    unique_qty = sum(qty for _, qty, _, _, _ in rows)
    ws.cell(r, 3, f"Montážní práce: demontáž, montáž a zapojení, přepojení obvodů, označení").border = border
    ws.cell(r, 4, unique_qty).border = border
    ws.cell(r, 5, "ks").border = border
    ws.cell(r, 6, labor_per_ks).border = border
    ws.cell(r, 6).number_format = "#,##0.00"
    ws.cell(r, 7, f"=D{r}*F{r}").border = border
    ws.cell(r, 7).number_format = "#,##0.00"
    work_row = r
    r += 1

    # Totals
    ws.cell(r, 3, "Materiál celkem").font = bold
    ws.cell(r, 3).alignment = Alignment(horizontal="right")
    ws.cell(r, 7, f"=SUM(G{hdr_row+1}:G{mat_last})").font = bold
    ws.cell(r, 7).number_format = "#,##0.00"
    mat_row = r
    r += 1

    ws.cell(r, 3, "Práce celkem").font = bold
    ws.cell(r, 3).alignment = Alignment(horizontal="right")
    ws.cell(r, 7, f"=G{work_row}").font = bold
    ws.cell(r, 7).number_format = "#,##0.00"
    r += 1

    ws.cell(r, 3, "Cena celkem bez DPH").font = Font(bold=True, size=12)
    ws.cell(r, 3).alignment = Alignment(horizontal="right")
    ws.cell(r, 7, f"=G{mat_row}+G{work_row}").font = Font(bold=True, size=12)
    ws.cell(r, 7).number_format = "#,##0.00"
    bez_dph_row = r
    r += 1

    ws.cell(r, 3, "DPH 21 %").alignment = Alignment(horizontal="right")
    ws.cell(r, 7, f"=G{bez_dph_row}*0.21").number_format = "#,##0.00"
    r += 1

    ws.cell(r, 3, "Cena celkem vč. DPH").font = Font(bold=True, size=12)
    ws.cell(r, 3).alignment = Alignment(horizontal="right")
    ws.cell(r, 7, f"=G{bez_dph_row}*1.21").font = Font(bold=True, size=12)
    ws.cell(r, 7).number_format = "#,##0.00"

    # Notes
    r += 2
    notes = [
        "Poznámky:",
        f"• Ceny materiálu dle ceníku Schrack Technik s marží {args.markup:.0f} %.",
        "• Cenou není zahrnuta revize po montáži ani stavební práce.",
        "• Platba fakturou po provedení práce, splatnost 14 dní.",
        "• Polarita s.r.o., Na Folimance 2155/15, 120 00 Praha 2",
    ]
    for n in notes:
        ws.cell(r, 1, n).font = Font(italic=True) if n != "Poznámky:" else bold
        r += 1

    # Column widths
    widths = [4, 16, 62, 10, 6, 14, 12]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    wb.calculation.fullCalcOnLoad = True

    # Ulož
    out_name = f"Nabidka_{client_name.replace(' ', '_')}_{topic.replace(' ', '_')}.xlsx"
    out_path = os.path.join(folder, out_name)
    wb.save(out_path)

    mat_total = sum(q * c for _, q, _, _, c in rows)
    print(f"OK: {out_path}")
    print(f"  Materiálů: {len(rows)} položek, {unique_qty} ks")
    print(f"  Materiál celkem: {mat_total:,.2f} Kč bez DPH")
    print(f"  Práce: {unique_qty} ks × {labor_per_ks} Kč = {unique_qty * labor_per_ks:,.2f} Kč")
    print(f"  Celkem bez DPH: {mat_total + unique_qty * labor_per_ks:,.2f} Kč")

if __name__ == "__main__":
    main()
