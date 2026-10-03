"""Read-only smoke checks of published business pages. Does not submit forms."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urldefrag
from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
BASE = 'https://www.polarita.cz/'

def fetch(url):
    with urlopen(Request(url, headers={'User-Agent': 'Polarita-site-check/1.0'}), timeout=30) as r:
        assert r.status == 200, (url, r.status)
        return url, BeautifulSoup(r.read(), 'html.parser')

def main():
    manifest = json.loads((ROOT / 'src/pages/manifest.json').read_text(encoding='utf-8'))
    with ThreadPoolExecutor(max_workers=4) as pool:
        pages = dict(pool.map(fetch, [p['url'] for p in manifest]))
    links = set()
    for url, soup in pages.items():
        body = soup.select_one('.polarita-business')
        assert body, f'Missing design: {url}'
        assert len(body.select('h1')) == 1, f'H1: {url}'
        assert soup.select_one('link[rel="canonical"]'), f'Canonical: {url}'
        assert body.select_one('a[href="tel:+420792779534"]'), f'Phone: {url}'
        assert body.select_one('a[href="https://www.polarita.eu/"]'), f'Shop: {url}'
        for a in body.select('a[href]'):
            target = urljoin(url, a['href'])
            if urlsplit(target).scheme in ('http', 'https'):
                links.add(target)
    targets = {urldefrag(u)[0] for u in links} - set(pages)
    with ThreadPoolExecutor(max_workers=4) as pool:
        pages.update(pool.map(fetch, targets))
    for link in links:
        url, anchor = urldefrag(link)
        if anchor and urlsplit(url).hostname == 'www.polarita.cz':
            assert pages[url].find(id=anchor), f'Broken anchor: {link}'
    home = pages[BASE].select_one('.polarita-business')
    expected = 'Revize elektro pro domácnosti, firmy, družstva, společenství vlastníků a podobně.'
    assert home.h1.get_text() == expected
    form = home.find('form')
    assert form and len(form.select('[required]')) == 5, 'Required form fields'
    assert form.select_one('input[type="email"][required]'), 'Email validation'
    assert form.find('button', string='Odeslat poptávku') or form.select_one('button[type="submit"]')
    assert not pages[BASE + 'dovolena/'].select_one('.polarita-business'), 'Holiday design isolation'
    for file in (ROOT / 'src/pages').glob('*.html'):
        content = file.read_text(encoding='utf-8')
        assert 'jetpack_form_token' not in content and 'name="_wpnonce"' not in content
        assert '<script' not in content
    print(f'PASS: {len(manifest)} business pages, {len(links)} distinct links including anchors; form, headline, canonical, holiday isolation, no transient form tokens.')

if __name__ == '__main__':
    main()
