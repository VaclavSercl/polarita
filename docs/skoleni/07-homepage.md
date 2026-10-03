# Samostatné přezkoušení na úvodní stránce

Datum: 1. 10. 2026. Rozvržení nasazeno a ověřeno v popsaném rozsahu. Školení a přezkoušení je hlavní činnost s vlastní sekcí, nikoli druh revize.

## BEFORE

Karta školení byla mezi sedmi kartami pod nadpisem „Jakou revizi potřebujete?“. Hlavní nadpis a přehled činností školení nezmiňovaly. Mobilní pevná lišta nabízela pouze telefon a revizi.

## CHANGES

- Hero uvádí revize i přezkoušení elektrikářů a má samostatná tlačítka pro oba směry.
- Nový samostatný blok #skoleni před revizemi má vlastní nadpis, vysvětlení služby, rozsah E2A, rozlišení poučení § 4 a přezkoušení § 6/7 a odkaz na detail služby.
- Přehled hlavních činností zahrnuje školení. Revizní část obsahuje šest čistě revizních karet.
- Mobilní lišta nabízí telefon, revize a přezkoušení; při 320 px má každý prvek výšku 44 px a text se vejde na řádek.
- Přidán strukturální regresní check včetně negativních fixtures; původní kontrolní skript zůstal beze změny.

## NOT CHANGED

Poptávkový formulář a příjemce, navigace, detail školení, ostatní komerční stránky, produktové odkazy a e-shop. Žádný nový WordPress plugin. Existující komerční plugin dál poskytuje šablonu; Sites prověřen read-only, seznam připojených webů prázdný. Bez migrace webu a bez změn pluginového nastavení.

## TESTS

- Přesná shoda celého původního editoru s Git zdrojem před zápisem; záloha v ignored .artifacts/skoleni-20261001/home-layout-before.html. Před každým navazujícím uložením kontrola shody s posledním vlastním kandidátem. WordPress potvrdil uložení; veřejný výsledek ověřen samostatně.
- python web/check_home_service_layout.py: místní a anonymní veřejný PASS; samostatné sekce, pořadí, šest revizních karet, žádné školení uvnitř revizí, vlastní H2, jediný H1, kontaktní cesty. Negativní fixtures odmítají smíchání služeb i chybějící hlavní cestu. Před nasazením veřejný check správně selhal na chybějící sekci.
- python web/check_training_update.py: PASS, 11 komerčních URL, canonical/indexovatelnost, telefon, e-mail, e-shop a dosavadní kontroly formuláře/metadat. Žádný formulářový submit.
- python -m py_compile web/check_home_service_layout.py a git diff --check.
- Prohlížeč: desktop 1280 px, mobil 320 a 390 px bez horizontálního přetečení. Hero tlačítko a mobilní tlačítko vedou do #skoleni. Při 320 px opraveno zalomení mobilního textu; označení paragrafů v panelu zůstává na jednom řádku. Zachycené chyby konzole žádné. Dočasný viewport resetován.
- Screenshoty home-training-desktop.png a home-layout-mobile320.png v ignored .artifacts/skoleni-20261001, skutečně vizuálně kontrolovány.
- Oponent AGY read-only přezkoumal kandidáta, kontrolní skript i výsledné snímky a nezávisle spustil oba veřejné checky: PASS_WITH_LIMITATIONS, žádný další blokující nález. Jeho připomínky k odlišení § 4 a vysvětlení E2A zapracovány.
- Poptávkový shortcode, celý navigační blok a celá e-shopová sekce porovnány se základním Git zdrojem: přesná shoda obsahu.

## REMAINING ISSUES

Tento zásah neověřuje doručení formuláře, celkovou shodu WCAG ani Core Web Vitals. Odborné podklady školení a původní doklad se řeší odděleně. Žádné zprávy ani formulář nebyly odeslány. Git změny zůstávají místní, bez push a PR.
