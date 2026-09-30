"""Read-only, bounded check of the published training update. Never submits forms."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

BASE = "https://www.polarita.cz/"
SERVICE = "skoleni-a-zkousky-elektro/"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.canonical = []
        self.options = []
        self.option = False
        self.required = 0
        self.robots = []

    def handle_starttag(self, tag, attributes):
        data = dict(attributes)
        if tag == "a":
            self.links.append(data.get("href", ""))
        if tag == "link" and data.get("rel") == "canonical":
            self.canonical.append(data.get("href"))
        if tag == "option":
            self.option = True
        if tag in ("input", "select", "textarea") and "required" in data:
            self.required += 1
        if tag == "meta" and data.get("name") == "robots":
            self.robots.append(data.get("content", ""))

    def handle_endtag(self, tag):
        if tag == "option":
            self.option = False

    def handle_data(self, data):
        if self.option:
            self.options.append(data)


def fetch(url):
    request = Request(url, headers={"User-Agent": "Polarita-training-verification/1.0"})
    with urlopen(request, timeout=25) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}: {url}")
        content = response.read(2_000_001)
        if len(content) > 2_000_000:
            raise RuntimeError(f"Page exceeds check bound: {url}")
        return content.decode("utf-8"), response.url


def main():
    targets = set()
    manifest = json.loads((Path(__file__).parent / "src/pages/manifest.json").read_text(encoding="utf-8"))
    commercial_paths = {urlsplit(item["url"]).path for item in manifest}
    for path in ("", SERVICE):
        url = urljoin(BASE, path)
        text, final = fetch(url)
        page = Page()
        page.feed(text)
        assert final == url, (url, final)
        assert page.canonical == [url], (url, page.canonical)
        assert not any("noindex" in x for x in page.robots), url
        assert "tel:+420792779534" in page.links, url
        assert any(x.startswith("mailto:vaclav.sercl@polarita.cz") for x in page.links), url
        assert "https://www.polarita.eu/" in page.links, url
        if not path:
            assert any("Školení a zkoušky elektro" in x for x in page.options)
            assert page.required == 5, page.required
            assert "/" + SERVICE in page.links
        else:
            assert "Přijímáme nezávazné poptávky připravované služby." in text
            assert "tříčlenné komise" in text
            assert "/#poptavka" in page.links
        for link in page.links:
            absolute = urlsplit(urljoin(BASE, link))
            if absolute.scheme != "https" or absolute.netloc != "www.polarita.cz":
                continue
            if absolute.path not in commercial_paths:
                continue
            targets.add(absolute._replace(fragment="", query="").geturl())
        print(f"PASS {url}: canonical, indexability, contact and training content")
    with ThreadPoolExecutor(max_workers=4) as pool:
        for url, result in zip(sorted(targets), pool.map(fetch, sorted(targets))):
            print(f"PASS link {url} -> {result[1]}")
    print(f"PASS: {len(targets)} commercial internal targets; form not submitted")


if __name__ == "__main__":
    main()
