# Výsledky přípravy školení dne 1. 10. 2026

Celkový stav INCOMPLETE. Organizační podklady a úzká webová změna jsou připravené a ověřené v uvedeném rozsahu. Skutečný kurz, finální odborný test a ověření pořadatele nejsou dokončené.

## BEFORE

Nová stránka nebyla v allowlistu existujícího komerčního pluginu: bez vlastního meta/OG popisu, s druhým skrytým H1 staré šablony a starším logem. Chyběla ucelená organizační sada. Rozpor platnosti dokladu § 7 přetrvával; majitel nyní uvádí překlep a čtyři roky do 2030, což odporuje § 19 zákona. Předchozí potvrzení podmínek majitelem není nezávislé ověření.

## CHANGES

Vznikly pracovní listy pořadatele, zákazníka, účastníka a komise, osnovy, pravidla hodnocení, záznamy/evidence, pilot a návrhy neodeslané komunikace. Oponent AGY ověřil aktuální e-Sbírku a podklady. Po jeho připomínkách doplněny věk/svéprávnost, přesná praxe § 7 E2A a odlišení organizačních otázek od skutečného zkušebního testu.

Do existujícího pluginu Polarita Commercial Pages1.3.6 přidán pouze záznam1462. Titulek, popis, OG, breadcrumb a šablona nyní fungují stejně jako u ostatních komerčních stránek. Prázdný Service typ zatím nepřidává tvrzení o ověřeném poskytovateli zkoušek. Nové logo se načítá, stránka má jediný H1 a skip link, dialog cookies je česky. Profil Václava Šercla doplněn o osobní osvědčení E2A a dvě profesní kvalifikace z dříve vizuálně ověřených podkladů; bez čísel, osobních identifikátorů a skenů.

Záloha přesného pluginu v ignored .artifacts/skoleni-20261001/plugin-before.php; sha256a22c8af46fa2eb544f63e6c8ad8f5c9aec589a7cd3bb0b948352232df6599d54. Kandidát po jediném přidaném řádku má 9276 znaků, sha256 74a56ca0f05630d5564f6302c2b24252d4ea36b5ce688059696893f2ac0ed6ec. Před uložením přesná shoda kandidáta v editoru ověřena kopírováním jeho obsahu; WordPress oznámil úspěšnou změnu a uložený textarea obsah se shoduje. Přesný obsah stránky před doplněním profilu zálohován jako training-before.html a porovnán s verzovaným HTML, shoda úplná. Nejde o plnou databázovou zálohu.

## NOT CHANGED

Jiné komerční služby, hlavní důraz homepage na revize, e-shop, formulářová pole/příjemce, globální nastavení SEO a pluginové aktualizace. Žádný nový plugin ani účet. Soubor šablony a existující jiné položky pluginu nebyly změněny. Nebyl proveden vzdálený Git zápis ani PR.

## NEEDS OWNER INPUT

Vydavatel musí vyjasnit datum vydání a opravit platnost § 7; zákon stanovuje 3 roky, ne4. Doložit aktuálního pořadatele a jeho podnikatelský rozsah. ARES/RŽP API proIČ14180324 dne1. 10. 2026 vrací 4 aktivní živnosti a 18 oborů bez oboru školení; záznam má datum aktualizace2022-02-01. Výpis se mohl změnit později, proto výsledek není definitivní závěr o neexistenci oprávnění. Soukromě zajistit identitu/kvalifikaci členů komise, schválit konkrétní odborné testy, aktuální technické zdroje, délku školení a praktický nácvik, zákazníka, termín a cenu pilotu.

## TESTS

- Read-only ARES/RŽP API; AGY přímé čtení zákona250/2021 § 19 a NV194/2022 § 4,6–9 v oficiální e-Sbírce.
- python web/check_training_update.py: před změnou i po změně veřejné HTTP bez přihlášení, homepage/školení,11 komerčních cílů HTTP200, tel/mailto/shop, canonical/indexovatelnost, formulářová volba a5povinných polí. Nové kontroly metadata/OG, jediného H1, syntakticky platného JSON-LD a očekávaného graphu, skip linku a nepřítomnosti skutečného sharing widgetu. Jedna oprava samotného kontrolního skriptu: hledání slova sharedaddy zachycovalo CSS/skript; opraveno na přítomnost elementu s touto třídou, žádné jiné kontroly odstraněny.
- Prohlížeč po úpravě: title/popisek, načtené nové logo128px, jediný H1; nastavení cookies otevřeno, české kategorie bez placeholderů, odmítnutí volitelných funguje;320px bez horizontálního přetečení, oba mobilní kontakty vysoké68px; FAQ platnosti otevřeno a obsahuje 3 roky.
- Windows/PowerShell/Python; samostatné PHP CLI chybí, WSL nezobrazuje dostupnou distribuci. Nativní WordPress editor změnu přijal, anonymní veřejné výsledky ověřeny. Nepředstírat lokální PHP lint ani kompletní testy celé šablony.
- Po doplnění profilu další kontrola390px: bez horizontálního přetečení, nové logo načtené, profesní údaje skutečně viditelné, zachycené chyby konzole žádné. Výsledný screenshot uložen lokálně v ignored .artifacts/skoleni-20261001/training-after.png. AGY nezávisle spustil veřejný skript: exit0,11komerčních URL. Přidány pozitivní kontroly obou profesních kvalifikací a osobního E2A.
- git diff --check a konečné kontroly dle PLAN.md; nejedná se o SynthBit integrated gate.

## REMAINING ISSUES

Finální odborný test pro skutečné zařízení chybí: organizační otázky nejsou zkušební test. Úřední vzory příloh2/3/4 musí pořadatel převzít a vyplnit pro konkrétní průběh; checklisty je nenahrazují. Kurz ani video nejsou uskutečněné. Žádné emaily, příspěvky ani testovací formulář nebyly odeslány; doručení do schránky zůstává neověřené. Není provedeno úplné posouzení GDPR, cookies před souhlasem, performance ani shody WCAG. WordPress ukazuje7dostupných aktualizací a vypnuté cachování; tato zjištění jsou mimo úzké nasazení, nezměněna.

Oponent AGY hodnotí přípravu PASS_WITH_LIMITATIONS; toto není potvrzení připravenosti pořádat konkrétní kurz. Další krok: získat opravu dokladu/aktuální výpis a s předsedou sestavit skutečný technický test. Doručovací test připraven v05, vyžaduje konkrétní autorizaci odeslání majitelem.
