"""Export public WordPress page content without transient form tokens.

No authentication is used. Never save rendered form inputs/nonces to Git.
The form is restored as the authored Jetpack shortcode instead.
"""
from pathlib import Path
import argparse
import json
import urllib.request
from bs4 import BeautifulSoup

BASE = 'https://www.polarita.cz'
ROOT = Path(__file__).resolve().parent
FORM = '''[contact-form to="vaclav.sercl@polarita.cz" subject="Polarita.cz – poptávka revize elektro" submit_button_text="Odeslat poptávku"]
[contact-field label="Druh revize" type="select" required="true" options="Elektroinstalace,Hromosvod,Elektrické spotřebiče,Nabíjecí stanice,FVE – fotovoltaická elektrárna,Jiné / více druhů revizí" /]
[contact-field label="Místo realizace (obec)" type="text" required="true" /]
[contact-field label="Stručný popis požadavku" type="textarea" required="true" /]
[contact-field label="Jméno" type="name" required="true" /]
[contact-field label="E-mail" type="email" required="true" /]
[contact-field label="Telefon (volitelně)" type="text" /]
[contact-field label="Požadovaný termín (volitelně)" type="text" /]
[/contact-form]'''

def read_json(path):
    req = urllib.request.Request(BASE + path, headers={'User-Agent': 'Polarita-site-versioning/1.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def clean_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    for form in list(soup.find_all('form')):
        if form.find_parent() is None:
            continue
        wrapper = form.find_parent(id=lambda x: bool(x and (x.startswith('contact-form-') or x.startswith('jp-form-'))))
        (wrapper or form).replace_with(FORM)
    for el in list(soup.select('script, .sharedaddy, .jetpack-likes-widget-wrapper')):
        el.decompose()
    for el in soup.select('input[type="hidden"]'):
        el.decompose()
    for el in soup.find_all(True):
        for attr in list(el.attrs):
            if attr.startswith('data-wp-') or attr.startswith('on'):
                del el.attrs[attr]
    result = str(soup)
    if 'jetpack_form_token' in result or 'name="_wpnonce"' in result:
        raise ValueError('Unexpected transient form token in snapshot')
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='src/pages')
    parser.add_argument('--ids', nargs='*', type=int)
    args = parser.parse_args()
    out = ROOT / args.output
    out.mkdir(parents=True, exist_ok=True)
    pages = [read_json('/wp-json/wp/v2/pages/' + str(i)) for i in args.ids] if args.ids else read_json('/wp-json/wp/v2/pages?per_page=100')
    manifest = []
    for page in pages:
        html = page['content']['rendered']
        if not args.ids and 'polarita-business' not in html:
            continue
        slug = page['slug']
        content = clean_content(html)
        filename = slug + '.html'
        (out / filename).write_text('<!-- wp:html -->\n' + content + '\n<!-- /wp:html -->\n', encoding='utf-8')
        manifest.append({'id': page['id'], 'slug': slug, 'url': page['link'], 'title': BeautifulSoup(page['title']['rendered'], 'html.parser').get_text(), 'file': filename})
        print(f'Exported {slug}: page {page["id"]}')
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
