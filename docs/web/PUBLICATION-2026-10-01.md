# Publikace a dokončení bodů 1–5 — 1. 10. 2026

Stav: PASS_WITH_LIMITATIONS. Živé změny a kontroly jsou oddělené od podkladů. Výchozí revize: 469a4c07647bdb591f666505dfe1a24aea2db670. Žádná změna aplikačního kódu, DNS, závislostí ani placené propagace.

## BEFORE

- Hosting měl WWW redirect aktivní, SSL redirect neaktivní; HTTP bez www procházelo dvěma přesměrováními.
- Konverze generate_lead neměla po posledním nasazení nový doložený test doručení.
- Sociální texty byly v repozitáři vedeny jako připravené.

## CHANGES

1. Ve Forpsi aktivován SSL redirect pouze pro hosting polarita.cz. WWW redirect zachován. Ze všech tří nekanonických variant jedna 301 přímo na https://www.polarita.cz/, následně 200; zachována cesta školení i query. AGY nezávisle otestoval šest kombinací a potvrdil PASS. Návrat v případě regrese: deaktivovat pouze nově zapnutý SSL redirect.
2. Jedna výslovně schválená testovací poptávka 20:34 SELČ, jasně označená TEST, bez obchodní objednávky. Web zobrazil nové potvrzení, GA4 přijal generate_lead 1 jako klíčovou událost. Ověřen odpovídající e-mail v doručené poště a předání přes adresu Polarity. Test proveden v přihlášeném WordPress prohlížeči; nejde o nový test anonymního antispamu.
3. [PageSpeed mobil](https://pagespeed.web.dev/analysis/https-www-polarita-cz/bb8vtymccr?form_factor=mobile), 20:37 SELČ: výkon 97, přístupnost 100, doporučené postupy 100, SEO 100, procházení agenty 2/2. FCP 1,8 s, LCP 2,3 s, TBT 0 ms, CLS 0. [Desktop](https://pagespeed.web.dev/analysis/https-www-polarita-cz/bb8vtymccr?form_factor=desktop): všechny čtyři kategorie 100; LCP 0,5 s, TBT 0 ms, CLS 0. Jde o laboratorní výsledky Lighthouse 13.5.0; CrUX nemá dostatek dat a nelze tvrdit splnění field CWV ani dokonalou přístupnost či SEO.
4. Google Search Console: sitemap úspěšně načtena 1. 10.; stránka školení indexována, HTTPS a jedna platná navigační struktura. Bing sitemap Success bez chyb/varování; stránka školení Indexed successfully. Starší indexovaná kopie Bingu hlásí chybějící description/alt a dva H1, aktuální veřejná metadata prošla samostatným checkem. Úplná indexace všech komerčních URL nebyla doložena touto kontrolou.

Bing Live URL test 20:41 SELČ navíc výslovně potvrzuje „No SEO/GEO issues found“, „URL can be indexed by Bing“ a dva typy markup. Staré chyby v indexu nejsou chybami této aktuální kopie. Požádáno o aktualizaci této jediné stránky; její následné přeindexování není okamžitě garantováno.
5. Publikovány a ověřeny čtyři příspěvky: Facebook revize a samostatné školení pod stránkou Polarita; [X](https://x.com/VaclavSercl/status/2105727092486787264); [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7511493444788183040/) pod osobním profilem Václava Šercla. LinkedIn použil otevřený externí Chrome. Neproběhla žádná placená propagace. Google publikace výslovně blokována hláškou „Abyste mohli zveřejňovat novinky, musíte ověřit svůj zápis“.

## NOT CHANGED

DNS, poštovní nastavení, runtime, pluginy a aplikační zdroje. Fotografie a reference odloženy podle pokynu majitele. YouTube má pouze scénář; video nebylo vyrobeno ani zveřejněno.

## NEEDS OWNER INPUT

Google vyžaduje dokončení ověření zápisu vlastníkem, záložka ponechána k předání. Následně lze publikovat připravenou aktualitu. Pro video potřebujeme skutečný záznam a souhlas s použitím podkladů.

## TESTS

- Veřejný HTTP GET: tři doménové varianty a školení s query, jedna 301 a 200; AGY nezávislá kontrola šesti kombinací. Bez testu všech cest, POST a všech síťových lokalit.
- Jeden skutečný submit, nový success, odpovídající doručený e-mail a GA4 generate_lead 1; žádný další opakovaný submit.
- PageSpeed aktuální mobil/desktop, GSC skutečný index a sitemap, Bing index/sitemap.
- python -X utf8 web/check_seo.py: exit 0; 11 komerčních stránek a 200 komerčních odkazů/anchorů, sitemap a robot pravidla.
- Vizuální potvrzení příspěvků, autora a obsahu; privátní důkazy pouze v ignored .artifacts/publication-20261001. Mailové hlavičky ani přístupové tokeny nepatří do Git.
- Kontrola dokumentačního diffu a whitespace před lokálním commitem. Nejde o implementaci nebo plný gate SynthBit harnessu.

## REMAINING ISSUES

- Google firemní aktualita čeká na ověření identity.
- Ve veřejném Google výsledku i Facebook podrobnostech zůstává stará adresa Zázvorkova; jde o rozpor se sídlem Na Folimance na webu. Předchozí schválení údajů v administračním pohledu není důkazem jejich současného veřejného zobrazení. Nutné dořešit správný zápis a ověření.
- Facebook náhled homepage použil starý cachovaný SEO titulek; X ukazuje aktuální a Facebook školení správný. Doplnit obnovu náhledu Meta, nepovažovat starou kartu za změnu aktuálních webových metadata.
- Zpracování novější kopie ve vyhledávačích a reálné CWV nemají garantovaný okamžitý výsledek. Zbývají drobné příležitosti cache, obrázků a blokujícího CSS podle PageSpeed; žádné riskantní změny kvůli skóre nebyly provedeny.
- Nový GitHub push ani PR nebyly v tomto pokračování provedeny. Předchozí konkrétní souhlas s 469a4c0 neopravňuje publikaci nového dokumentačního commitu.
