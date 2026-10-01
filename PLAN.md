# Čitelnější logo Polarita.eu — 2026-09-29

## Oddělení hlavních činností na homepage 1. 10. 2026

Goal: školení a přezkoušení je samostatná hlavní činnost. Vyjmout kartu z revizí, vytvořit vlastní hlavní sekci, uvést ji v hero a přehledu činností. Zachovat revize jako hlavní nabídku a e-shop jako důležitou cestu. Non-goals: ostatní stránky a oddělené sekce, právní rozšíření nabídky, instalace nových pluginů, změny formuláře/příjemce, rozesílání, push/PR, SynthBit.

Baseline 0b14103cb8c426e37d70efed072179d82682e8de, čistý index/worktree. Windows/Python, přihlášený WordPress539. Plugin-management prověřen; Sites list neobsahuje připojený web, neprovádět migraci. Existující komerční WordPress plugin nadále poskytuje šablonu. Vlastněný rozsah: PLAN.md, web/src/pages/polarita.html, web/check_home_service_layout.py a docs/skoleni/07-homepage.md. Kontrolní skript ověřuje skutečnou strukturu i původní chybné zařazení jako negativní fixture; existující kontroly neměnit/oslabovat.

Impact: hero CTA a přehled hlavních činností, samostatná sekce #skoleni před #revize, šest čistě revizních karet. Bez nových tvrzení o kvalifikaci/ceně/termínu. Před změnou přesná shoda zdroje a editoru a ignored záloha. Souběžnou změnu nepřepsat. Oponent AGY read-only vyžádán majitelem.

Acceptance: žádný školící odkaz ani karta uvnitř #revize; samostatný #skoleni se svým H2, účelem §4/6/7, CTA a telefonem; hero zvýrazňuje obě činnosti. Jeden H1, funkční navigace/kontakt/formulář/e-shop; desktop a 320/390px bez přetečení. Commands: python web/check_home_service_layout.py; python web/check_training_update.py; python -m py_compile web/check_home_service_layout.py; git diff --check; git diff --cached --check. Žádný skutečný formulářový submit.

Recovery: .artifacts/skoleni-20261001/home-layout-before.html obsahuje přesný zdroj. Případný návrat pouze vlastní změny po kontrole mezitímních editací. Nejvýše tři cílené opravy s důkazy; lokální commit po ověření, bez vzdálených zápisů. Kompletní platformový audit se netvrdí.

Outcome: homepage539 má samostatné hlavní školení před revizemi, hero pro obě činnosti a šest čistě revizních karet. Po vizuální kontrole doplněna mobilní pevná cesta k přezkoušení a opraveno její zalomení při320px; všechny tři cíle44px a bez přetečení. §4poučení odlišeno od §6/7zkoušek, E2A vysvětleno podle existujícího detailu; připomínky AGY zapracovány. Veřejný strukturálnícheckPASS (před nasazením baselineFAIL), původnícheck11URLPASS, desktop1280/320/390 vizuálně ověřeny, viewportreset. Záloha a screenshotyignored, formulář neodeslán. Report07-homepage.md. Lokální commit po závěrečných kontrolách, bez push/PR.

## Upřesnění pořadatele a platnosti 1. 10. 2026

Goal: pokračování webu a školení výslovně potvrzené majitelem; sjednotit aktuální podklady a doplnit veřejně pořadatele Polarita s.r.o. Non-goals: instalace SynthBit, další služby, změny pluginů, rozesílání, skutečný kurz, veřejné osobní skeny a remote Git zápisy.

Baseline: 455df133274b4a664e3d759d10b1c64403be4095; čistý index i pracovní strom, Windows/Python, přihlášený editor WP 1462. Vlastnictví změn: tento běh pouze PLAN.md, docs/skoleni/01-overeni.md, 02-organizace.md, 04-zaznamy.md, 05-pilot-a-komunikace.md, 06-report.md, README.md a web/src/pages/skoleni-a-zkousky-elektro.html. Složky bez symlinků ověřit před zápisem. Pravidla dodaná v chatu jsou načtená; immutable souborový manifest jejich původních bajtů ani harness nejsou vytvořené a nejsou zde prohlašované za ověřené.

Impact: vlastník opravil tvrzení na tři roky do 2029 a určil pořadatele Polarita. Neoznačovat obor 72 za výslovnou jedinou zákonnou podmínku; současně nezamlčet požadavek § 19 odst. 4 zákona 250/2021 na předmět podnikání externího pořadatele. Právní pokrytí aktuálního zápisu zatím nezávisle neuzavřeno. Původní dokument nenahrazovat vlastní úpravou.

Acceptance: konzistentní aktuální stav v podkladech, předvyplněný pořadatel v pracovních listech, veřejná věta o pořadateli bez tvrzení o schválení úřadem; zachovat ostatní obsah. Commands: python web/check_training_update.py; git diff --check; git diff --cached --check; kontrola úzkého diffu a AGY read-only oponentura. Žádná instalace závislostí. Kontrolní skript se nemění.

Recovery: uložit přesný současný HTML obsah do ignored .artifacts, ověřit shodu s Git zdrojem před publikací a vracet jen vlastní větu. Souběžná změna blokuje přepis. Nejvýše tři doložené opravné cykly. Doručení formuláře nelze potvrdit bez odeslání; dřívější otázka na autorizaci zůstává nevyřešená, tento běh nic neodesílá. Lokální commit po ověření, žádný push/PR.

Outcome: dokumentace sjednocena na potvrzeného pořadatele a tříletou platnost do2029; požadavek předmětu podnikání zachován bez kategorické povinnosti konkrétního oboru72. Veřejně uložena pouze jedna věta pořadatele, přesná záloha/shoda zdroje před změnou; potvrzení WordPress a anonymní HTTP200 s přesným textem. Screenshot kontaktní karty, 320px bez přetečení; konzole bez zachycených chyb, viewport reset. AGY read-only PASS_WITH_LIMITATIONS, připomínky zapracovány. Kontrolní skript beze změny, po nasazení exit0 pro11komerčníchURL. Finální odborný test, původní opravený doklad, právní pokrytí předmětu podnikání a doručení poptávky se tím nepovažují za uzavřené. Žádný email, sociální příspěvek, push aniPR. Harness neinstalován.

## Dokončení školení body 1 až 4 dne 1. 10. 2026

Goal: ověřit podmínky nabídky, připravit provozní dokumentaci, bezpečné technické úpravy webu a pilot/komunikaci. Non-goals: jiné sekce, instalace harnessu/závislostí/pluginů, vzdálené Git zápisy, odesílání emailů/příspěvků, smyšlené termíny/ceny, skutečný kurz bez zákazníka.

Baseline: 16b97cd085fafa0bafbeeaa8c34de55ad91fbe15; čistý index/worktree, Windows PowerShell. Repozitář nemá AGENTS.md ani SynthBit. Pravidla vlastníka dodaná v chatu platí jako provozní omezení, nikoli příkaz instalovat harness v tomto webovém úkolu. Oponent AGY je výslovně vyžádán a má read-only úlohu. Rozsah: PLAN.md, docs/skoleni/, report, případně úzká úprava nové stránky/SEO po aktuálním čtení editoru. Osobní skeny a secrets nepatří do Gitu.

Discovery: tvrzení o čtyřleté platnosti §7 do2030 odporuje zákonné tříleté platnosti. Neopravovat originál ani potvrdit2030; připravit žádost vydavateli. Pořadatel a aktuální předmět podnikání čekají na doložení. Starší výpis OSVČ nedokládá aktuální stav firmy. Nabídka byla publikována na potvrzení majitele, rozdíl proti ověření zachovat.

Acceptance: vyplnitelné podklady, oddělený §4 a §6/7, skutečná účast komise, žádné fiktivní údaje, právní zdroje/omezení; veřejné komerční URL, metadata/CTA/mobile podle dostupnosti; AGY zapracován. Commands: python web/check_training_update.py; git diff --check; git diff --cached --check. Registr/web read-only. Odeslání emailu/formuláře/příspěvku vyžaduje výslovnou autorizaci; připravit konkrétní text/test.

Recovery: aktuální obsah před změnou do ignored .artifacts; nepřepsat souběžné změny. Nejvýše tři doložené opravy. Nedostupný admin/SEO mechanismus uvést jako blokaci. Lokální commit jen vlastněných souborů po kontrolách a AGY; bez push/PR. Podklady k odbornému schválení nejsou uskutečněný kurz.

Discovery update: existující vlastní plugin Polarita Commercial Pages1.3.6 řídí metadata a šablonu explicitním allowlistem10stránek, nové1462 chybí. Rank Math čeká na globální průvodce, nepoužít jej v úzkém rozsahu. Bez změny funkcí přidat pouze1462 do existujícího seznamu, Service ponechat prázdné do ověření pořadatele. Dosavadní template.php zkontrolován; odstraňuje skrytý H1 a poskytuje skip link i nastavení cookies. Přesný plugin9030znaků zálohován, sha256a22c8af46fa2eb544f63e6c8ad8f5c9aec589a7cd3bb0b948352232df6599d54 shodný s aktuálním editorem. Neměnit jiné ID ani globální funkce. Patch popsat v docs/skoleni; před uložením opakovat shodu a vyžádat read-only oponenturu. PHP CLI zatím chybí; použít pouze při dostupné nativní kontrole WordPressu a ověřit veřejný výsledek. Nejde o kompletní platformový gate.

Outcome: přidán pouze entry1462 v aktuálním pluginu po záloze/AGY/shodě editoru, WordPress potvrdil uložení. Metadata/OG a jediný H1 veřejně ověřeny, logo/cookies/320px a390px/FAQ v prohlížeči. Úzké doplnění doložených profesních údajů na1462 publikováno po přesné shodě zdroje se zálohou. Žádné jiné stránkové obsahy změněny. docs/skoleni pracovní podklady; AGY nezávisle ověřil právní zdroje a veřejný checkexit0. Finální odborný test, aktuální pořadatel, oprava dokladu, pilot a doručení emailu zůstávají otevřené; čeká otázka na konkrétní autorizaci jednoho testu. Žádný push/PR, harness neinstalován. Celkový stav INCOMPLETE, webový zásah ověřen v úzkém rozsahu.

## Potvrzená dostupnost školení — pokračování 2026-09-30

Výsledek pokračování: na obou stránkách publikována dostupná nabídka; veřejný check exit 0. Dodaných šest PDF přečteno vizuálně (11 stran), mimo Git a bez veřejného uploadu. Nové zjištění: doklad § 7 má rozpor data platnosti, živnostenský výpis je pro OSVČ z roku 2021 bez oboru školení. Majitel požádán o vysvětlení; do veřejného obsahu nepřenášet tvrzení o nezávisle ověřené platnosti § 7 ani čísla/oprávnění pořadatele. Rozsah nabídky E2A osobní osvědčení RT dokládá, platnost do 14. 9. 2031. Neřešit opravu originálních PDF ani přepisovat osobní údaje. Výsledný report obsahuje omezení a rozlišení potvrzení majitele od doložených faktů.
Majitel výslovně potvrdil zajištěný předmět podnikání, platné osobní osvědčení RT E2A, doklad § 7 i další dva odborně způsobilé členy komise. Na jeho pokyn změnit označení připravované služby na dostupnou nabídku; další podmínky a obsah zachovat. Výchozí HEAD e19ae1d0ae2b78bd571ff15b0de17a3b1101cd1d, čistý pracovní strom. Soubory: tento plán, dvě HTML stránky (WP 1462 a 539), report a kontrolní skript. Před úpravou získat přesné aktuální HTML editorů a zálohovat do ignored .artifacts; při odchylce od zdrojů nepřepisovat cizí změny. Měnit pouze konkrétní texty o připravované službě. Akceptace: žádné označení připravované nabídky, zachované § 4/6/7, komise, vstupní předpoklady, kontakty, e-shop a formulář. Kontroly: python web/check_training_update.py, veřejný prohlížeč, git diff --check. Opravy nejvýše tři; návrat přes přesné zálohy a WP revize. Aktualizace kontrolního skriptu se týká schváleného očekávaného obsahu, nesmí odstranit ostatní kontroly. Lokální commit, žádný push/PR. Potvrzení majitele je podklad pro publikaci nabídky, nikoli nezávislý audit jeho dokladů.

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
