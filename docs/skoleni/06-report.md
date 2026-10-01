# Výsledky přípravy školení dne 1. 10. 2026

Celkový stav INCOMPLETE. Organizační podklady a úzká webová změna jsou připravené a ověřené v uvedeném rozsahu. Pořadatel je majitelem určen; skutečný kurz, finální odborný test a nezávislé ověření podnikatelského pokrytí externího zkoušení nejsou dokončené.

## BEFORE

Nová stránka nebyla v allowlistu existujícího komerčního pluginu: bez vlastního meta/OG popisu, s druhým skrytým H1 staré šablony a starším logem. Chyběla ucelená organizační sada. Původní doklad § 7 obsahoval rozpor v platnosti; zastaralé pracovní texty uváděly čtyři roky do 2030 a nevyjasněného pořadatele. Předchozí potvrzení podmínek majitelem není nezávislé ověření.

## CHANGES

Vznikly pracovní listy pořadatele, zákazníka, účastníka a komise, osnovy, pravidla hodnocení, záznamy/evidence, pilot a návrhy neodeslané komunikace. Oponent AGY ověřil aktuální e-Sbírku a podklady. Po jeho připomínkách doplněny věk/svéprávnost, přesná praxe § 7 E2A a odlišení organizačních otázek od skutečného zkušebního testu.

Do existujícího pluginu Polarita Commercial Pages1.3.6 přidán pouze záznam1462. Titulek, popis, OG, breadcrumb a šablona nyní fungují stejně jako u ostatních komerčních stránek. Prázdný Service typ zatím nepřidává tvrzení o ověřeném poskytovateli zkoušek. Nové logo se načítá, stránka má jediný H1 a skip link, dialog cookies je česky. Profil Václava Šercla doplněn o osobní osvědčení E2A a dvě profesní kvalifikace z dříve vizuálně ověřených podkladů; bez čísel, osobních identifikátorů a skenů.

Záloha přesného pluginu v ignored .artifacts/skoleni-20261001/plugin-before.php; sha256a22c8af46fa2eb544f63e6c8ad8f5c9aec589a7cd3bb0b948352232df6599d54. Kandidát po jediném přidaném řádku má 9276 znaků, sha256 74a56ca0f05630d5564f6302c2b24252d4ea36b5ce688059696893f2ac0ed6ec. Před uložením přesná shoda kandidáta v editoru ověřena kopírováním jeho obsahu; WordPress oznámil úspěšnou změnu a uložený textarea obsah se shoduje. Přesný obsah stránky před doplněním profilu zálohován jako training-before.html a porovnán s verzovaným HTML, shoda úplná. Nejde o plnou databázovou zálohu.

## NOT CHANGED

Jiné komerční služby, hlavní důraz homepage na revize, e-shop, formulářová pole/příjemce, globální nastavení SEO a pluginové aktualizace. Žádný nový plugin ani účet. Soubor šablony a existující jiné položky pluginu nebyly změněny. Nebyl proveden vzdálený Git zápis ani PR.

## NEEDS OWNER INPUT

Majitel určil Polaritu jako pořadatele a opravil platnost na tři roky do roku 2029; tyto otázky se znovu nevyžadují. Vydavatel musí potvrdit datum vydání a opravit původní překlep. Při vydání 24. 6. 2026 vychází konec platnosti na 24. 6. 2029. Podnikatelské pokrytí externího zkoušení podle § 19 odst. 4 zůstává nezávisle neuzavřené. Zákon přímo nejmenuje obor č. 72; jeho výslovnou nutnost netvrdit. Dřívější ARES/RŽP výsledek se starým datem aktualizace 2022-02-01 není konečným právním posouzením. Soukromě doložit identitu/kvalifikaci již zajištěných členů komise, schválit konkrétní odborné testy, aktuální technické zdroje, délku školení a praktický nácvik, zákazníka, termín a cenu pilotu.

## TESTS

- Read-only ARES/RŽP API; AGY přímé čtení zákona250/2021 § 19 a NV194/2022 § 4,6–9 v oficiální e-Sbírce.
- python web/check_training_update.py: před změnou i po změně veřejné HTTP bez přihlášení, homepage/školení,11 komerčních cílů HTTP200, tel/mailto/shop, canonical/indexovatelnost, formulářová volba a5povinných polí. Nové kontroly metadata/OG, jediného H1, syntakticky platného JSON-LD a očekávaného graphu, skip linku a nepřítomnosti skutečného sharing widgetu. Jedna oprava samotného kontrolního skriptu: hledání slova sharedaddy zachycovalo CSS/skript; opraveno na přítomnost elementu s touto třídou, žádné jiné kontroly odstraněny.
- Prohlížeč po úpravě: title/popisek, načtené nové logo128px, jediný H1; nastavení cookies otevřeno, české kategorie bez placeholderů, odmítnutí volitelných funguje;320px bez horizontálního přetečení, oba mobilní kontakty vysoké68px; FAQ platnosti otevřeno a obsahuje 3 roky.
- Windows/PowerShell/Python; samostatné PHP CLI chybí, WSL nezobrazuje dostupnou distribuci. Nativní WordPress editor změnu přijal, anonymní veřejné výsledky ověřeny. Nepředstírat lokální PHP lint ani kompletní testy celé šablony.
- Po doplnění profilu další kontrola390px: bez horizontálního přetečení, nové logo načtené, profesní údaje skutečně viditelné, zachycené chyby konzole žádné. Výsledný screenshot uložen lokálně v ignored .artifacts/skoleni-20261001/training-after.png. AGY nezávisle spustil veřejný skript: exit0,11komerčních URL. Přidány pozitivní kontroly obou profesních kvalifikací a osobního E2A.
- git diff --check a konečné kontroly dle PLAN.md; nejedná se o SynthBit integrated gate.

## REMAINING ISSUES

Finální odborný test pro skutečné zařízení chybí: organizační otázky nejsou zkušební test. Úřední vzory příloh2/3/4 musí pořadatel převzít a vyplnit pro konkrétní průběh; checklisty je nenahrazují. Kurz ani video nejsou uskutečněné. Žádné emaily, příspěvky ani testovací formulář nebyly odeslány; doručení do schránky zůstává neověřené. Není provedeno úplné posouzení GDPR, cookies před souhlasem, performance ani shody WCAG. WordPress ukazuje7dostupných aktualizací a vypnuté cachování; tato zjištění jsou mimo úzké nasazení, nezměněna.

Oponent AGY hodnotil předchozí přípravu PASS_WITH_LIMITATIONS; toto není potvrzení připravenosti pořádat konkrétní kurz. Další krok: dokončit opravu původního dokladu, vyjasnit pokrytí externího zkoušení současným předmětem podnikání a s předsedou sestavit skutečný technický test. Doručovací test připraven v05, vyžaduje konkrétní autorizaci odeslání majitelem.

## Navazující upřesnění majitele

Podklady byly sjednoceny na pořadatele Polarita s.r.o., IČO 14180324, a tříletou platnost do roku 2029. Jde o potvrzení majitele; přijetí podkladů úřadem ani uskutečněný kurz se tím netvrdí. Objednávkový a protokolový pracovní list i neodeslané návrhy komunikace obsahují stejného pořadatele. Příliš kategorická formulace o oboru č. 72 je nahrazena skutečným požadavkem § 19 odst. 4. Původní PDF zůstala beze změny.

Na stránce školení publikována pouze věta „Pořadatel školení: Polarita s.r.o., IČO 14180324.“ v kontaktní kartě. Před zápisem přesná shoda celého editoru s verzovaným zdrojem a záloha training-organizer-before.html v ignored .artifacts/skoleni-20261001. WordPress potvrdil aktualizaci, veřejná kontaktní karta obsahuje větu a anonymní HTTP kontrola potvrzuje 200 i přesný text. Screenshot training-organizer-after.png zachycuje zveřejněnou kartu. Kontrola při 320 px: žádné horizontální přetečení, karta široká 265 px; po kontrole viewport resetován. Zachycené chyby konzole žádné. python web/check_training_update.py po publikaci: exit 0, 11 komerčních URL. Kontrolní skript se neměnil, formulář nebyl odeslán. AGY úzký diff hodnotil PASS_WITH_LIMITATIONS; obě jeho drobné připomínky k formulaci a primárnímu zdroji zapracovány.
