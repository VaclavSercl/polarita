#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update homepage (id 539) — novy obsah Kdo jsme + odkazy na nove stranky.
Puvodni bloky 'Potulny revizák' + 'Eshop' zachovany, jen doplnene a prolinkovane.
"""
import json, subprocess, os

TEMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')
COOKIES = os.path.join(TEMP, 'wp_cookies.txt')
NONCE = open(os.path.join(TEMP, 'wp_nonce.txt')).read().strip()

CONTENT = """<!-- wp:heading -->
<h2>Kdo jsme</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Polarita s.r.o.</strong> — vaše elektro firma v Praze. Elektroinstalace, wallboxy a nabíjecí stanice pro elektromobily. Pracujeme pro domácnosti, firmy i developery.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>🔌 Rychle · 🛠️ Spolehlivě · 📋 S dokumentací</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Naše služby</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="/elektroinstalace/"><strong>Elektroinstalace</strong></a> — kompletní rozvaděče na klíč, novostavby, rekonstrukce, osvětlení.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/wallboxy/"><strong>Wallboxy a nabíjení</strong></a> — prodej a instalace nabíjecích stanic pro elektromobily.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Potulný revizák</strong><br>Revize elektrických zařízení.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Eshop</strong><br>Elektronický obchod nabíjecí stanice pro elektromobily, nabíjecí kabely, Wallboxy<br><a href="https://www.polarita.eu">www.polarita.eu</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Kontakt</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>📞 <a href="tel:+420792779534">+420 792 779 534</a> · ✉️ <a href="mailto:vaclav.sercl@polarita.cz">vaclav.sercl@polarita.cz</a></p>
<!-- /wp:paragraph -->"""

payload = {"content": CONTENT}

cmd = ['curl', '-s', '-X', 'POST',
       '-b', COOKIES,
       '-H', f'X-WP-Nonce: {NONCE}',
       '-H', 'Content-Type: application/json; charset=utf-8',
       '-d', json.dumps(payload),
       'https://www.polarita.cz/wp-json/wp/v2/pages/539']
r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
d = json.loads(r.stdout)
if 'id' in d:
    print(f"HOMEPAGE UPDATOVANA (id={d['id']}, modifikace: {d.get('modified','?')})")
else:
    print('CHYBA:', r.stdout[:400])
