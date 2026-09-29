# Čitelnější logo Polarita.eu — 2026-09-29

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
