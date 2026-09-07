#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Vytvoreni stranek na polarita.cz pres WP REST API (cookies+nonce)."""
import json, subprocess, os, sys

TEMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')
COOKIES = os.path.join(TEMP, 'wp_cookies.txt')
NONCE = open(os.path.join(TEMP, 'wp_nonce.txt')).read().strip()

PAGES = [
  {
    "title": "Elektroinstalace",
    "slug": "elektroinstalace",
    "status": "draft",  # najdriv koncept ke kontrole
    "content": """<h2>Kompletní elektroinstalace v Praze a okolí — kvalitně, na míru, se zárukou</h2>
<p><strong>Polarita s.r.o.</strong> se zabývá kompletní elektroinstalací pro novostavby, rekonstrukce a komerční prostory.</p>
<h3>Co pro vás uděláme</h3>
<ul>
<li><strong>Kompletní rozvaděče na klíč</strong> — návrh, montáž, zapojení, dokumentace</li>
<li><strong>Elektroinstalace novostaveb</strong> — rodinné domy, byty, pronájmy</li>
<li><strong>Rekonstrukce elektroinstalace</strong> — výměna rozvodů, zásuvek, osvětlení</li>
<li><strong>Přípojky pro wallboxy a nabíjecí stanice</strong> — příprava i montáž</li>
<li><strong>Osvětlení</strong> — interiérové i venkovní, chytré ovládání</li>
</ul>
<h3>Proč nás</h3>
<ul>
<li>Rychlá a spolehlivá práce, čisté provedení</li>
<li>Individuální přístup k zakázce</li>
<li>Férové ceny bez skrytých položek</li>
</ul>
<h3>Kontaktujte nás</h3>
<p>Telefon: <a href="tel:+420792779534">+420 792 779 534</a> | E-mail: <a href="mailto:vaclav.sercl@polarita.cz">vaclav.sercl@polarita.cz</a></p>"""
  },
  {
    "title": "Wallboxy a nabíjení",
    "slug": "wallboxy",
    "status": "draft",
    "content": """<h2>Wallboxy a nabíjecí stanice pro elektromobily — prodej i instalace</h2>
<p>Nabízíme <strong>kompletní řešení nabíjení elektromobilů</strong>: od výběru vhodné nabíjecí stanice, přes elektroinstalaci a zapojení, až po zprovoznění.</p>
<h3>Co nabízíme</h3>
<ul>
<li><strong>Nabíjecí stanice (wallboxy)</strong> — 11 kW i 22 kW, AC i DC</li>
<li><strong>Nabíjecí kabely</strong> Typ 2 a adaptéry</li>
<li><strong>Instalace na klíč</strong> — revize přípojky, montáž, zprovoznění</li>
<li><strong>Poradenství</strong> — jakou stanici zvolit pro váš domov či firmu</li>
</ul>
<h3>E-shop</h3>
<p>Kompletní sortiment nabíjecích stanic a kabelů najdete v našem e-shopu: <a href="https://www.polarita.eu">www.polarita.eu</a></p>
<h3>Chcete wallbox doma nebo ve firmě?</h3>
<p>Zavolejte: <a href="tel:+420792779534">+420 792 779 534</a> — poradíme zdarma.</p>"""
  },
]

def wp_api(method, endpoint, payload):
    cmd = ['curl', '-s', '-X', method,
           '-b', COOKIES,
           '-H', f'X-WP-Nonce: {NONCE}',
           '-H', 'Content-Type: application/json; charset=utf-8',
           '-d', json.dumps(payload),
           f'https://www.polarita.cz/wp-json/wp/v2/{endpoint}']
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout

for p in PAGES:
    result = wp_api('POST', 'pages', p)
    try:
        d = json.loads(result)
        if 'id' in d:
            print(f"VYTVORENO: {p['title']} (id={d['id']}, slug={d.get('slug')}, status={d.get('status')})")
            print(f"  odkaz konceptu: {d.get('link')}")
        else:
            print(f"CHYBA u {p['title']}: {result[:300]}")
    except Exception:
        print(f"CHYBA parse u {p['title']}: {result[:300]}")
