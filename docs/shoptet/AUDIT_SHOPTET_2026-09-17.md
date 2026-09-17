# Polarita.eu — první audit Shoptetu a vzorové popisy

> Následná realizace: Duše e-shopu byla aktivována, devět produktů upraveno a titulek úvodní stránky opraven. Aktuální stav a otevřené technické otázky uvádí [záznam provedených úprav](PROVEDENE_UPRAVY_2026-09-17.md). Níže je zachován původní audit před změnami.

Datum kontroly: 17. 9. 2026. Rozsah: aktuální tarif, Duše e-shopu, veřejné kategorie a devět reprezentativních produktů. Jde o obsahový audit, nikoliv revizi elektrických zařízení či potvrzení parametrů výrobcem. Návrhy nebyly publikovány.

## 1. Ověřená administrace

- Tarif **Basic**. Zdroj: https://www.polarita.eu/admin/tarif-platba-a-doklady/
- **Duše e-shopu je dostupná, vypnutá a všech šest polí je prázdných** (0/500 znaků). Zdroj: https://www.polarita.eu/admin/duse-eshopu/
- Viditelné ovládání: uložit, vyplnit z obchodu, ruční vyplnění, odvození z dat a AI návrhy. Nic z toho nebylo spuštěno ani uloženo.
- Oficiální článek Shoptetu omezuje MCP a vlastní produktové prompty na Premium. Basic tedy není tarif s těmito funkcemi. Zdroj: https://www.polarita.eu/admin/univerzita-clanek/?id=734
- Po obnovení přihlášení ověřeno přímo v administraci:

| Funkce | Výsledek kontroly |
|---|---|
| AI úprava popisů | U produktu 227 jsou tlačítka „Vylepšit pomocí AI“ u krátkého i podrobného popisu. |
| Generování obrázků | Fotogalerie produktu nabízí „Vygenerovat z obrázků“. |
| AI copywriter | Stránka `/admin/ai-copywriter/` je přístupná; nabízí nový text, blog, newsletter a příspěvek na sociální sítě. Zobrazuje výzvu k vytvoření prvního textu. |
| SEO generování | `/admin/zakladni-seo/` obsahuje tlačítka „Vygenerovat pomocí AI“ například u titulku a popisu úvodní stránky. |
| Sklad | Přístupné obrazovky Sklad a Zásoby; skladový výpis obsahuje 33 položek včetně variant. AI naskladnění na těchto obrazovkách nebylo nalezeno; jeho dostupnost není potvrzena. |
| AI související produkty | Dostupnost nepotvrzena: otevření záložky přes nabídku dalších záložek nezobrazilo její obsah. |

Ověřena je přítomnost ovládání, nikoliv úspěšné generování, limity či případná spotřeba kreditů. Žádné generování ani ukládání změn nebylo spuštěno.

Další konkrétní zjištění v SEO: titulek úvodní stránky je `Polarita.eu--Nabijeci-stanice--Wallbox`, produktová šablona meta description je `#PRODUCT_NAME#. #SHORT_DESCRIPTION#`. Chybějící krátké popisy tedy omezují i obsah této šablony. Doporučený návrh titulku úvodní stránky: **Nabíječky pro elektromobily a wallboxy | Polarita.eu**. Před změnou ověřit výsledný titulek a popis na veřejné stránce; šablona sama nedokazuje výsledné HTML.

## 2. Sortiment a priority

Veřejná kategorie Nabíječky zobrazila 12 produktových položek, Elektro 9. Následně administrace Přehled potvrdila 21 produktů; skladový výpis ukázal 33 položek včetně variant. Zastoupené typy: přenosné nabíječky, wallboxy, nabíjecí kabely, napájecí adaptéry, tašky, proudové chrániče a jističe.

### P1 — opravit faktické rozpory před další propagací

1. Proudový chránič AR874103--: název a tabulka uvádějí **typ B**, odrážka **typ A, certifikace VDE**. Typ a certifikaci ověřit podle dokumentace přesného modelu, nikoliv většinovým výskytem v textu.
2. Přenosná nabíječka 11 kW: název a text slibují aplikaci obecně, ale konfigurace ji nabízejí jako samostatnou příplatkovou výbavu. Dvě sekce obsahu balení se rozcházejí v přítomnosti tašky.
3. Přenosná nabíječka 3,5 kW: popis uvádí 5 m, nejlevnější varianta 3,5 m. Aplikace je v názvu, ale jen jedna varianta ji výslovně obsahuje.
4. Zásuvkový wallbox F-OBZ30-AC-3P32: nabídka míchá Type1/Type2/GB/T/TS-NACS bez jasného rozlišení dodávaného provedení. Není doloženo, že jedna nabízená položka obslouží všechny standardy.
5. Adaptér DEP2-216: název „z 400 V na 230 V“ může mást směr použití. Popis uvádí CEE samici a EU zástrčku, tedy připojení odpovídající nabíječky k zásuvce 230 V. Před přejmenováním ověřit skutečné koncovky a určené použití.

### P2 — zlepšit rozhodování zákazníka

- Omezit absolutní sliby („absolutní bezpečí“, „v jakýchkoliv podmínkách“), nedoložená srovnání a nepodmíněné úspory.
- U 11kW nabíječky nedoloženě nepřebírat označení „proudový chránič typu B“ jen ze zápisu AC 30 mA + DC 6 mA; ověřit dokumentaci ochranné funkce. Toto je požadavek na ověření, nikoliv určení skutečného zapojení zařízení.
- Oddělit společné vlastnosti produktu od obsahu konkrétní varianty.
- U samostatného kabelu doplnit délku, přesné koncovky a proud. Neodvozovat chybějící parametry pouze z SKU.
- U wallboxu s DLB doložit, jak funguje vazba s ADL400, jaké příslušenství je součástí a co je nutné nastavit. Samotný nadpis DLB tyto otázky neřeší.
- Zpřehlednit názvy, jednotky, češtinu a vysvětlit zkratky. Odstranit viditelné bloky „Klíčová slova“ a německé zbytky u elektro sortimentu.
- U více kontrolovaných stránek byly v doplňkových parametrech jen kategorie a záruka, případně hmotnost. Technické hodnoty přitom zůstávají pouze v textu. Zda jsou vyplněné neveřejné parametry v administraci, nebylo ověřeno.

### P3 — struktura a údržba

- Dlouhé produktové URL obsahující celou dodavatelskou adresu navrhnout zkrátit až s mapou původní → nová adresa a přesměrováním. Nyní neměnit.
- Názvy obrázků jako „ezgif.com webp to jpg converter“ nahradit smysluplnými alternativními texty po vizuální kontrole snímků.
- U jističe B16/3P jsou jako související uvedené i odlišné proudy a počet pólů. Označit je jako jiné varianty, nikoliv automaticky zaměnitelné náhrady.
- Dvě kategorie samy o sobě neposkytují důvod pro drahou automatizaci. Nejprve sjednotit data a vzory, pak rozhodnout o případném doplňku.

## 3. Kontrola devíti produktů

| Produkt | Co je použitelné | Hlavní nedostatek | Další krok |
|---|---|---|---|
| FR-OJ2D-3P16A2, kabel 11 kW | Identifikace, výkon v názvu, základní odolnost | Text jej nazývá nabíječkou; chybí délka a přehled elektrických parametrů | Doplnit dokumentaci a popsat správný druh výrobku |
| 191, přenosná 11 kW | Podrobná tabulka, čtyři varianty | Aplikace, taška a ochrany nejsou spolehlivě rozlišené | Variantová matice a kontrola ochranných funkcí |
| 221, přenosná 3,5 kW | Proudové stupně, Schuko, varianty délky | Rozpor 3,5/5 m a aplikace v názvu | Přepsat společný popis a oddělit výbavu |
| F-OBZ1-AC-3P32, wallbox DLB | 22 kW, 3 fáze, 5 m, konkrétní obsah balení | Nevysvětlené DLB, neurčitý rozsah proudu a ochrany | Doložit technické podmínky DLB |
| F-OBZ30-AC-3P32, zásuvkový wallbox | Rozměry, nastavení 8–32 A, obsah balení | Smíchané konektorové standardy a fáze | Určit přesné prodávané provedení |
| DEP2-216, adaptér | Délka 46 cm, limit 16 A, vyloučení 11kW varianty | Směr použití nejasný z názvu | Ověřit koncovky, upravit název a použití |
| TASKA-FEYREE | Rozměry 36 × 36 × 9 cm, účel | Obecný název, neověřená kompatibilita konkrétních sad | Zpřesnit název a vyzkoušet balení |
| AR874103--, chránič | Rozsáhlá tabulka včetně typu B a 40 A/30 mA | Přímý rozpor typ A/B | Nejvyšší priorita ověření dokumentace |
| AM618316--, jistič | 16 A, 3P, B, 6 kA a výrobce | Pouhá tabulka, duplicity klíčových slov, nejasné množství v balení | Doplnit krátké vysvětlení a prodejní jednotku |

## 4. Návrh Duše e-shopu

Každé pole je návrh do limitu 500 znaků. Nebyl vložen ani aktivován. Pole odlišení neobsahuje neověřené sliby servisu nebo montáže.

**Co prodáváte**

Prodáváme nabíjecí techniku pro elektromobily: přenosné nabíječky, wallboxy, nabíjecí kabely a příslušenství Feyree. Sortiment doplňují instalační jističe a proudové chrániče Schrack AMPARO. U nabíjecí techniky rozlišujeme výkon, připojení a konkrétní výbavu variant.

**Co u vás platí vždy**

Cenu, dostupnost a termín dodání přebírej pouze z aktuálních údajů konkrétní varianty. Obsah balení a technické parametry uváděj jen podle ověřených podkladů daného modelu. Vlastnosti příplatkové výbavy nepřisuzuj základní variantě. Chybějící informace označ k doplnění v pracovním návrhu.

**Komu prodáváte**

Domácnostem, firmám a elektrikářům, kteří vybírají nabíjení elektromobilu nebo součásti elektroinstalace. Laikům vysvětluj zkratky a rozdíly mezi variantami. Odborným zákazníkům předkládej přesné parametry a identifikaci modelu. Nepředpokládej stejné možnosti připojení u všech zákazníků.

**Jak mluvíte se zákazníky**

Piš česky, věcně, srozumitelně a zákazníkům vykej. Používej krátké odstavce, přehledné tabulky a jednotné zápisy jednotek, například 11 kW a 16 A. Vysvětluj praktický význam doložených funkcí. Vynechávej přehnané superlativy, opakování, výkřiky a dlouhé názvy plné svislítek.

**Čím se odlišujete**

Spojujeme nabídku nabíjecí techniky a součástí elektroinstalace. V komunikaci zdůrazňuj konkrétní výbavu, parametry a rozdíly mezi výrobky. Další výhody, například montáž, servis nebo odborné poradenství, uváděj pouze tehdy, jsou-li pro danou nabídku výslovně potvrzené.

**Co AI nesmí nikdy tvrdit**

Neslibuj absolutní bezpečnost, univerzální kompatibilitu ani zaručenou úsporu. Nevymýšlej certifikace, ochrany, výkon, krytí ani obsah balení. Neoznačuj ochranu AC 30 mA + DC 6 mA automaticky za proudový chránič typu B. Netvrď, že zákazník nepotřebuje posouzení elektroinstalace. Nepřisuzuj příplatkovou aplikaci všem variantám. Neřeš rozpory v podkladech odhadem.

## 5. Vzorové popisy

Následují redakční návrhy založené na současném katalogu. Údaje opsané z e-shopu nejsou nezávisle ověřené u výrobce. Seznamy „Před publikací“ jsou interní úkoly a nepatří do veřejného popisu. Ceny a skladové termíny mají zůstat v dynamických polích Shoptetu.

### A. Nabíjecí kabel — FR-OJ2D-3P16A2

**Název:** Nabíjecí kabel Feyree Typ 2, až 11 kW

**Krátký popis:** Nabíjecí kabel Feyree Typ 2 s uváděným maximálním výkonem 11 kW. Při výběru zkontrolujte provedení obou koncovek a potřebnou délku. Model FR-OJ2D-3P16A2.

**Dlouhý popis:**

Samostatný nabíjecí kabel je určen k propojení kompatibilního vozidla a nabíjecího bodu. Tento výrobek je kabel, nikoliv přenosná nabíjecí jednotka do domácí zásuvky.

| Parametr | Údaj z katalogu |
|---|---|
| Značka | Feyree |
| Model | FR-OJ2D-3P16A2 |
| Označení připojení | Typ 2 |
| Maximální výkon uvedený v nabídce | 11 kW |

Před objednáním porovnejte připojení na straně vozidla i nabíjecího bodu. Maximální výkon kabelu sám o sobě nezaručuje stejný výkon při každém nabíjení.

**Před publikací:** doložit délku, oba konektory, jmenovitý proud a počet fází; ověřit působnost IP66, monitorování teploty a dokumentaci tvrzení CE. U neúplné specifikace zatím pouze koncept.

### B. Přenosná nabíječka — 11 kW, produkt 191

**Název:** Přenosná nabíječka Feyree 11 kW, Typ 2 — výběr výbavy

**Krátký popis:** Přenosná nabíječka s konektorem Typ 2, přívodem CEE 16 A a nabíjecím kabelem 5 m. Nabídka obsahuje základní provedení i varianty s adaptérem nebo mobilní aplikací. Výbavu zkontrolujte u vybrané varianty.

**Dlouhý popis:**

Feyree 11 kW je přenosná nabíjecí jednotka pro kompatibilní elektromobily. Katalog uvádí třífázové připojení přes červenou pětikolíkovou zástrčku CEE 16 A a konektor Typ 2 na straně vozidla.

| Parametr | Údaj z katalogu |
|---|---|
| Maximální výkon | 11 kW |
| Nastavení proudu | 8 / 10 / 13 / 16 A |
| Síťové připojení | CEE 16 A, 3P+N+PE |
| Připojení vozidla | Typ 2 |
| Délka kabelu | 5 m |

**Vyberte výbavu:**

- Základ: varianta 191/- Z.
- S adaptérem 400/230 V: varianta 191/- A.
- S aplikací pro mobil: varianta 191/- A2.
- S adaptérem a aplikací: varianta 191/- A3.

Mobilní funkce se vztahují k variantám, které je výslovně obsahují. Skutečný nabíjecí výkon závisí také na vozidle a podmínkách připojení.

**Před publikací:** ověřit model F-OBM22-AC-3P16 pro všechny varianty, délku, obsah balení včetně tašky a držáku, rozsah funkcí aplikace a dokumentaci ochran. Nevracet do textu „absolutní bezpečí“, „60 km za hodinu“ bez podmínek ani automatické označení ochrany jako typ B.

### C. Wallbox — F-OBZ1-AC-3P32

**Název:** Wallbox Feyree 22 kW, Typ 2, Wi-Fi a RFID, s elektroměrem ADL400

**Krátký popis:** Nástěnná nabíjecí stanice s výkonem až 22 kW, kabelem Typ 2 o délce 5 m a ovládáním přes Wi-Fi aplikaci. Nabídka zahrnuje elektroměr ADL400 a RFID funkci. Model F-OBZ1-AC-3P32.

**Dlouhý popis:**

Wallbox Feyree je určen k nástěnné instalaci a nabíjení kompatibilních vozidel přes konektor Typ 2. Katalog uvádí třífázové provedení, nastavitelný proud a ovládání přes aplikaci.

| Parametr | Údaj z katalogu |
|---|---|
| Model | F-OBZ1-AC-3P32 |
| Maximální výkon | 22 kW |
| Počet fází | 3 |
| Délka nabíjecího kabelu | 5 m |
| Funkce | Wi-Fi aplikace, RFID |
| Dodávaný elektroměr | ADL400 |

**Obsah balení podle nabídky:** nabíjecí stanice, nástěnný držák, elektroměr ADL400, deset šroubů, deset hmoždinek a manuál.

Před výběrem je potřeba ověřit podmínky připojení a požadované řízení nabíjení. Návrh zapojení musí vycházet z návodu konkrétního modelu.

**Před publikací:** ověřit Bluetooth, rozsah nastavení proudu, ochrany, přesné napájení a DLB včetně zapojení ADL400. DLB záměrně není v navrženém názvu, dokud nebude doloženo. Počet RFID čipů není v současném obsahu balení uveden.

### D. Adaptér — DEP2-216

**Pracovní název po ověření koncovek:** Adaptér Feyree pro CEE 32 A nabíječku do zásuvky 230 V

**Krátký popis:** Adaptér pro odpovídající přenosnou nabíječku s konektorem CEE 32 A. Katalog uvádí CEE samici, EU zástrčku, délku 46 cm a maximální proud 16 A. Není určen pro menší CEE konektor 11kW varianty uvedené v nabídce.

**Dlouhý popis:**

Adaptér DEP2-216 umožňuje podle současného popisu připojit odpovídající přenosnou 22kW nabíječku k napájení 230 V. Při tomto způsobu použití nabídka uvádí jednofázové nabíjení do 16 A a výkon do 3,5 kW; nejde o zachování třífázového výkonu 22 kW.

| Parametr | Údaj z katalogu |
|---|---|
| Model | DEP2-216 |
| Provedení | CEE samice / EU zástrčka |
| Maximální proud | 16 A |
| Délka | 46 cm |
| Obsah balení | Jeden adaptér |

Před objednáním porovnejte přesné konektory i seznam kompatibilních nabíječek. Označení 22 kW popisuje určenou nabíječku, nikoliv výkon při napájení přes tento adaptér.

**Před publikací:** potvrdit orientaci a typ koncovek, kompatibilní modely, podmínky proudového omezení a návod výrobce. Název je pracovní, nikoliv potvrzení zapojení.

### E. Taška — TASKA-FEYREE

**Název:** Taška Feyree na nabíječku a kabely, 36 × 36 × 9 cm

**Krátký popis:** Taška pro uložení přenosné nabíječky, kabelu nebo příslušenství. Katalogové rozměry jsou 36 × 36 × 9 cm. Před výběrem porovnejte velikost své nabíjecí sestavy.

**Dlouhý popis:**

Taška Feyree pomůže uspořádat nabíjecí vybavení na jednom místě. Je určena pro přenosné nabíjecí stanice, kabely a další příslušenství odpovídající velikosti.

- Kód: TASKA-FEYREE.
- Uváděné rozměry: 36 × 36 × 9 cm.
- Uváděná hmotnost: 0,5 kg.

Nabíječka a kabely nejsou tímto textem deklarovány jako součást dodávky tašky. Vhodnost pro konkrétní sestavu je potřeba posoudit podle její velikosti.

**Před publikací:** potvrdit, zda jde o vnější nebo vnitřní rozměry, materiál, hmotnost a obsah dodávky. Netvrdit vodotěsnost, polstrování ani vhodnost pro všechny nabíječky.

### F. Proudový chránič — AR874103--

**Stav: pracovní koncept, pozastavit publikaci do vyřešení typu A/B.**

**Pracovní název podle tabulky:** Proudový chránič Schrack AMPARO, typ B, 40 A, 4P, 30 mA

**Krátký popis:** Proudový chránič Schrack řady AMPARO, model AR874103--. Tabulka současné nabídky uvádí čtyřpólové provedení, jmenovitý proud 40 A a reziduální proud 30 mA. Před zveřejněním je nutné potvrdit typ chrániče podle dokumentace výrobce.

**Dlouhý popis po potvrzení typu:**

Proudový chránič Schrack AMPARO je součástí nabídky ochranných přístrojů pro elektroinstalace. Při jeho výběru je rozhodující přesný typ, jmenovitý proud, reziduální proud a provedení odpovídající projektu instalace.

| Parametr | Údaj k ověření proti výrobci |
|---|---|
| Model | AR874103-- |
| Řada | AMPARO |
| Typ | B podle názvu a tabulky; odrážka uvádí A |
| Jmenovitý proud | 40 A |
| Jmenovitý reziduální proud | 30 mA |
| Počet pólů | N+3 |
| Konstrukce | Bez zpoždění |

**Před publikací:** odstranit rozpor A/B podle datasheetu přesného SKU, doložit případnou certifikaci VDE, význam a podmínky údaje 10 kA a prodejní jednotku. Tabulka s rozporem je interní pracovní pomůcka, nikoliv hotový veřejný obsah.

### G. Instalační jistič — AM618316--

**Název:** Instalační jistič Schrack AMPARO B16, 3P, 6 kA

**Krátký popis:** Třípólový instalační jistič Schrack AMPARO s charakteristikou B, jmenovitým proudem 16 A a katalogovou spínací schopností 6 kA. Model AM618316--.

**Dlouhý popis:**

Jistič Schrack AMPARO AM618316-- nabízí třípólové provedení s jmenovitým proudem 16 A. Při výběru porovnejte všechny parametry s požadavky konkrétního obvodu; jiné proudové hodnoty ani jednopólová provedení nejsou automaticky zaměnitelné.

| Parametr | Údaj z katalogu |
|---|---|
| Výrobce | Schrack |
| Řada / typ | AMPARO / AM6 |
| Charakteristika | B |
| Jmenovitý proud | 16 A |
| Počet pólů | 3 |
| Spínací schopnost | 6 kA |
| Varianta | AC jistič |

Detailní rozměry a podmínky použití ověřte v dokumentaci výrobce pro uvedený kód.

**Před publikací:** doplnit odkaz na datasheet a jednoznačně určit množství prodávané za cenu za kus. Výpis „1 ks, 4 ks, 60 ks“ nyní nerozlišuje prodejní a logistické balení.

## 6. Doporučené rozhodnutí

Nejprve opravit rozpory a variantovou výbavu, potom doplnit Duši a sjednotit popisy. Na základě nalezených problémů není potřeba přecházet na Premium kvůli první sadě oprav. Přes prohlížeč je možné provádět jednotlivé úpravy po připravení podkladů; pro větší objem lze samostatně posoudit export/import. MCP má smysl znovu hodnotit při opakované automatizaci, nikoliv jako řešení nekvalitních vstupních dat.

## Zdroje produktového auditu

1. https://www.polarita.eu/feyree-nabijeci-kabel-az-11-kw-typ-2-ce/
2. https://www.polarita.eu/https-www-feyree-com-products-feyree-ev-portable-charger-type-2-portable-electric-car-charger-11kw-16a-3-phase-app-control/
3. https://www.polarita.eu/feyree-3-5-kw-prenosna-levna-nabijecka-pro-elektromobily-typ-2-230v-3-5kw--16a/
4. https://www.polarita.eu/feyree-wallbox-type-2--32a22kw-w-wifi-rfid-dlb-elektromer/
5. https://www.polarita.eu/feyree-wallbox-type1-type2/
6. https://www.polarita.eu/feyree-eu-adapter-z-400v-32a-na-230v-16a/
7. https://www.polarita.eu/feyree-taska-na-produkty/
8. https://www.polarita.eu/proudovy-chranic-amparo-10-ka--40-a--4p--30-ma--b/
9. https://www.polarita.eu/instalacni-jistic-amparo-6ka--b-16a--3p/
