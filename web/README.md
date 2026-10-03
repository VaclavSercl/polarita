# Polarita.cz — revize elektro a e-shop

Redesign zveřejněný 17. 9. 2026. Hlavní nabídka: revize elektroinstalací, hromosvodů, spotřebičů, nabíjecích stanic a FVE po celé ČR. E-shop Polarita.eu má výraznou vlastní sekci, skutečné produktové fotografie a přímé odkazy. Obsah dovolených se nemění.

## Soubory a obnova

- `src/pages/`: aktuální obsah jedenácti obchodních stránek; `manifest.json` mapuje soubory na WordPress ID a URL.
- `backups/before-redesign/`: veřejné obsahové snímky původních čtyř existujících obchodních stránek před tímto redesignem. Již zahrnují předchozí úpravy nabídky a formuláře; nejde o původní web před celou spoluprací.
- `snapshot.py`: čte veřejné REST API bez přihlašování. Z vykresleného obsahu odstraní formulářové tokeny a nahradí formulář autorským Jetpack shortcode. HTML je normalizované, nejde o úplnou zálohu databáze ani přesný export struktury původních bloků.
- `check_site.py`: kontroluje živé stránky, odkazy, kotvy, formulář a izolaci dovolených. Nic neodesílá.

Nasazení: ve WordPressu otevřít stránku podle ID v manifestu, přepnout do HTML editoru, nahradit obsah odpovídajícím souborem a uložit. Nejprve aktualizovat detailní stránky, úvod nakonec. Poté ověřit veřejnou stránku i formulář. Přihlašování probíhá v prohlížeči; repozitář neobsahuje relace, hesla ani nonce.

Obnova jednotlivé stránky: použít Starší verze ve WordPressu, případně obsah souboru v `backups/before-redesign`. Zálohy jsou pouze obsahové; před větším zásahem do šablony, pluginů či databáze je nutná standardní záloha hostingu. Nové detaily služeb nemají starší obsah v této záloze.

**Starší skripty `monitoring/wp_update_home.py` a `monitoring/wp_create_pages.py` nepoužívat pro tento redesign:** obsahují jinou verzi obsahu a mohly by přepsat aktuální stránky.

## Lokální kontrola

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r web/requirements-dev.txt
.\.venv\Scripts\python.exe web/snapshot.py
.\.venv\Scripts\python.exe web/check_site.py
```

Export standardně vybírá pouze stránky označené `.polarita-business`. Volba `--ids` slouží k cílené obsahové záloze. Před commitem vždy zkontrolovat diff.

## Design a obsah

Kompaktní horní navigace, vlastní logo, námořnická modrá a petrolejová pro služby, oranžová pro e-shop. Výrazná typografie, jednoduchá mřížka, žádné nové JS animační knihovny nebo externí fonty. Obrázky produktů se načítají odloženě z existujícího CDN e-shopu.

Společné CSS je vložené v každé obchodní stránce, aby změny nezasahovaly dovolené. Selektor `body:has(.polarita-business)` upravuje rozvržení šablony Twenty Fifteen pouze na těchto stránkách. Vyžaduje současný prohlížeč s podporou `:has()`. Při větším rozvoji je vhodné přesunout sdílený design do samostatné WordPress šablony; aktuální řešení zachovává ostatní obsah webu.

Formulář používá stávající Jetpack: pět povinných údajů, telefon a termín volitelné. Příjemce `vaclav.sercl@polarita.cz`. Test při redesignu 17. 9. byl zaznamenán ve WordPress Forms; tehdy nebylo doručení e-mailu ověřeno. Nový samostatně schválený test 1. 10. byl doručen do připojené schránky a majitel jej potvrdil; podrobnosti uvádí nový SEO report. Přesun do nového vzhledu zachovává shortcode.

Faktické údaje od uživatele: celá ČR a označení „revizní technik elektro“. Neuvádíme vymyšlená čísla oprávnění, reference, počty zakázek, pevné termíny ani ceny. Fotografie technika a ověřitelné realizace čekají na dodání. Revizní intervaly se bez znalosti zařízení a podmínek neuvádějí paušálně.

## Podklady pro rozhodnutí

- [Tuch et al., 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/): první estetické hodnocení ovlivňuje vizuální složitost a typičnost rozvržení; nejde o důkaz růstu poptávek.
- [Seckler et al., CHI 2014](https://edoc.unibas.ch/entities/publication/6d0819d7-ce1d-4216-9c27-ee8a2bbc300a): studie s 65 účastníky podporuje soubor doporučení pro použitelnost formulářů. Nelze z ní odvodit účinek jediného pole na našem webu.
- [Jongmans et al., 2022](https://doi.org/10.1080/0267257X.2022.2085315): použitelnost a vizuální prožitek; použit dostupný abstrakt, nikoli plný text.
- [Webflow: trendy 2026](https://webflow.com/blog/web-design-trends-2026): oborová inspirace pro vlastní značku, typografii a stručnost; není vědeckým důkazem.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): čitelnost, focus a ovládání. Tlačítka navržena s výškou alespoň 48 px. Nejde o certifikaci shody celého webu.
- [Core Web Vitals](https://web.dev/articles/vitals): cíle LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 na 75. percentilu. Data reálných návštěvníků ani úplný výkonnostní audit nebyly změřeny; netvrdíme splnění těchto cílů.

## Ověření

Vizuálně ověřen desktop a mobilní šířka 390 px: úvod, produktové karty a poptávka. Fotografie tří produktů se úspěšně načetly. Mobilní úvod nemá vodorovné přetékání. Pět povinných polí a volitelné telefon/termín byly ověřeny ve vykresleném formuláři.

Automatický read-only smoke test viz `check_site.py`. Dostupnost stránek není totéž co uživatelský test, audit přístupnosti či měření konverzí. Tvrzení o „dokonalém“ designu nelze technickým testem doložit.

## SEO a dohledatelnost aktualizované 1. října 2026

Viz `docs/web/SEO-GEO-2026-10-01.md` pro změny, aktuální indexaci, předchozí a nové měření i otevřené kroky. `check_seo.py` používá standardní knihovnu Pythonu a prochází pouze obchodní URL v manifestu; negativní fixtures jsou v `tests/`. Spustit `python web/check_seo.py` a `python -m unittest discover -s web/tests`.

`wp-plugin/polarita-commercial.php` je verzovaný hlavní soubor existujícího pluginu, nikoli celý instalační balíček. Před editací získat přesnou kopii aktuálního serverového souboru, prověřit souběžné změny a zachovat ostatní komponenty. Metadata i odstranění starých stylů mají stránkový allowlist. Existující Jetpack a cookie komponenty zůstávají.

**`snapshot.py` nyní nepoužívat pro obnovu formuláře:** jeho starší rekonstrukce neobsahuje všechny aktuální volby. Obnova přes přesný editorový export nebo WordPress revize; žádný plošný přepis novějšího živého obsahu podle starého exportu.
