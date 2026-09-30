# Čitelnější logo Polarita.eu — 2026-09-29

## Nová nabídka školení a zkoušek — 2026-09-30
Goal: analyzovat majitelem dodaný odkaz a doplnit přesně vymezenou nabídku na Polarita.cz. Non-goals: instalace harnessu, změna infrastruktury, změny jiných sekcí a e-shopu, push/PR. Výchozí HEAD eea57a79aeda2aeb5836bc054abf6a8b1b14890d, čistý pracovní strom; Windows/PowerShell, přihlášený WordPress. Vlastněný rozsah: tento plán, nový obsah školení, jeho odborný report a případně úzké doplnění aktuální homepage. Neobnovovat staré zdrojové HTML přes novější živý obsah.

Discovery: sdílenou konverzaci nelze načíst přes odkaz; majitel následně vložil její celé vysvětlení. Uvedl externí školení firem a živnostníků v rozsahu E2A pro § 4/6/7. NV 194/2022 Sb. v e-Sbírce zobrazuje aktuální znění od 1. 7. 2024. Ověřeny § 4, 6–9 a § 19 zákona 250/2021 Sb.: komise pro § 6/7, zkoušky, dokumentace, vstupní předpoklady i předmět podnikání externího pořadatele. Číslo a platnost dokladů, předmět podnikání a zajištění dalších členů komise zatím nejsou doloženy. Web proto výslovně označí připravovanou službu a nezávazné poptávky; konkrétní provedení až po ověření podmínek. Nezveřejní tvrzení o hotové komisi či doloženém oprávnění školitele.

File checklist: PLAN.md; web/src/pages/skoleni-a-zkousky-elektro.html; docs/web/SKOLENI_2026-09-30.md; aktuální web/src/pages/polarita.html a nový záznam manifestu; web/check_training_update.py pro nezávislé úzké veřejné ověření. Obnova: přesná lokální kopie aktuálního HTML editoru v ignored .artifacts a WordPress revize; návrat pouze vlastní změny. Před publikací ověřit shodu zálohy s editorem. Rizika: záměna s osvědčením TIČR nebo profesní kvalifikací, nedoložená komise, neaktuální zdroj v Git, kolize jiných editorů.

Outcome: publikována stránka WP 1462 a úzké propojení homepage WP 539. Nabídka je výslovně připravovaná, skutečné provedení podmíněno ověřením podkladů a komise. Veřejný check exit 0 (11 komerčních URL), FAQ a volba formuláře ověřeny, mobil 320/390 px bez přetečení. Limity: neověřené doručení emailu, chybějící samostatné SEO popisy nové stránky a skrytý H1 šablony; provozní doklady pořadatele čekají na majitele. Lokální kontrola / commit, bez push/PR. Viz výsledný report.

Acceptance: pravdivý rozsah potvrzen majitelem, nezměněná hlavní nabídka revizí a e-shop, funkční poptávka a kontakt, jediný H1, správný odkaz a mobilní čitelnost; žádné vymyšlené ceny, termíny či oprávnění. Exact verification: `git diff --check`; kontrola konkrétních nových URL přes veřejné HTTP a prohlížeč, H1/CTA/formulář, šířky 320/390px; nepoužívat zastaralé web/check_site.py jako doklad úspěchu. Bez skutečného nasazení reportovat připraveno, nikoli hotovo. Lokální commit jen vlastněných souborů; vzdálené zápisy neautorizovány.

## Cíl a rozsah
Zvětšit stávající logo pouze v hlavičce Shoptetu a zachovat funkčnost mobilního menu, hledání a košíku. Jde o úzkou úpravu vzhledu na pokyn majitele, nikoli instalaci SynthBit harnessu nebo změnu WordPressu. Bez změn oprávnění doplňků, produktů a ostatního obsahu.

## Prostředí a výchozí stav
Repozitář: polarita, výchozí commit 6b4d62fb3f88208af70c299948ec7da9ce4bbd13. Pracovní strom před úpravou čistý. Windows / PowerShell, živá administrace přihlášena. Záhlaví, zápatí i další textová pole HTML editoru byla prázdná. Aktuální logo /user/logos/polarita_logo_800.png. Desktop: max-height 60px; mobil: vykreslený box 50 × 60px při šířce viewportu 390px. Přímý ovladač velikosti loga nenalezen v Editoru ani Dalším nastavení.

## Dopad a soubory
- PLAN.md: plán a stav této úpravy.
- docs/shoptet/logo-header.html: samostatný označený blok CSS pro pole Záhlaví.
- docs/shoptet/LOGO_2026-09-29.md: výsledky ověření a návrat změny.
Zásah omezit na #header .site-name. Původní obrázek zůstane zachován. Nepřepisovat cizí kód, pokud se pole mezitím změní.

## Přijetí a ověření
Vložený blok musí být menší než 8192 znaků. Ověřit úspěšné uložení a veřejné vykreslení při běžné desktopové šířce a mobilních šířkách 390 a 320px: zachované proporce, logo načtené, bez překryvu s ovládáním a bez vodorovného přetečení. Zkontrolovat menu a hledání bez objednávky. Provést `git diff --check`, přesně vybrat vlastní soubory pro místní commit. Nejde o ověření neexistujícího integrovaného harnessu.

## Rizika a obnova
Šablona může mít odlišné mobilní limity; po změně ověřit skutečný layout a nejvýše třikrát cíleně opravit. Při chybě odstranit pouze označený blok CSS (výchozí záhlaví prázdné). Nezasahovat do oprávnění doplňků. Ztráta relace blokuje pouze nasazení.

## Autorizace a stav
Uživatel autorizoval pokračování úpravy loga v e-shopu. Změny Git zůstanou místní; push ani PR nejsou součástí tohoto kroku. Stav: nasazeno a živě ověřeno. Desktopový obrázek 120 × 120px, mobilní 72 × 72px v odkazu 72 × 50px s ořezem okolních bílých okrajů. Kontroly 390px a 320px bez vodorovného přetečení nebo kolize s ovládáním. Mobilní menu otevřeno a zavřeno, vyhledávací pole otevřeno a zavřeno. Uložený obsah záhlaví se přesně shoduje s vloženým blokem; ostatní textová pole zůstala prázdná. Nebyly potřeba opravné cykly po nasazení.
