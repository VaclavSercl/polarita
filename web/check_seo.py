"""Read-only SEO regression check for explicitly selected commercial pages."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

BASE = "https://www.polarita.cz/"
COMPANY_PROFILES = {"https://www.facebook.com/polarita.cz/", "https://www.youtube.com/@polarita2983"}
PERSON_PROFILES = {"https://x.com/VaclavSercl", "https://www.linkedin.com/in/vaclav-sercl/"}


class SEOPage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles, self.descriptions, self.canonicals, self.robots = [], [], [], []
        self.og, self.links, self.ids, self.graph = {}, [], set(), []
        self.h1 = 0
        self.lang = None
        self.capture = None
        self.buffer = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "title" or (tag == "script" and a.get("type") == "application/ld+json"):
            self.capture, self.buffer = tag, ""
        if tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href"))
        if tag == "meta":
            if a.get("name") == "description":
                self.descriptions.append(a.get("content", ""))
            if a.get("name") == "robots":
                self.robots.append(a.get("content", ""))
            if a.get("property", "").startswith("og:"):
                self.og.setdefault(a["property"], []).append(a.get("content", ""))

    def handle_data(self, data):
        if self.capture:
            self.buffer += data

    def handle_endtag(self, tag):
        if tag == self.capture:
            if tag == "title":
                self.titles.append(self.buffer.strip())
            else:
                data = json.loads(self.buffer)
                self.graph.extend(data.get("@graph", [data]))
            self.capture = None


def validate(page, url):
    assert page.lang == "cs", (url, "language")
    assert page.h1 == 1, (url, "H1", page.h1)
    assert len(page.titles) == 1 and page.titles[0], (url, "title")
    assert len(page.descriptions) == 1 and page.descriptions[0], (url, "description")
    assert page.canonicals == [url], (url, "canonical")
    assert not any("noindex" in x.lower() for x in page.robots), (url, "noindex")
    assert page.og.get("og:title") == page.titles, (url, "OG title")
    assert page.og.get("og:description") == page.descriptions, (url, "OG description")
    assert page.og.get("og:url") == [url], (url, "OG URL")
    by_type = {x.get("@type"): x for x in page.graph if isinstance(x.get("@type"), str)}
    assert {"Organization", "Person", "WebPage", "WebSite", "BreadcrumbList"} <= set(by_type)
    assert set(by_type["Organization"].get("sameAs", [])) == COMPANY_PROFILES
    person = by_type["Person"]
    assert person["@id"] == BASE + "#vaclav-sercl"
    assert person["name"] == "Václav Šercl"
    assert person["url"] == BASE + "kontakt/#vaclav-sercl"
    assert person["worksFor"] == {"@id": BASE + "#organization"}
    assert set(person.get("sameAs", [])) == PERSON_PROFILES
    web = by_type["WebPage"]
    assert web["name"] == page.titles[0] and web["description"] == page.descriptions[0]
    assert web["url"] == url
    datetime.fromisoformat(web["dateModified"])
    assert "tel:+420792779534" in page.links
    assert any(x.startswith("mailto:vaclav.sercl@polarita.cz") for x in page.links)
    assert "https://www.polarita.eu/" in page.links
    if url == BASE:
        assert "přezkoušení" in page.titles[0] and "přezkoušením" in page.descriptions[0]
    if url == BASE + "kontakt/":
        assert "vaclav-sercl" in page.ids
        assert COMPANY_PROFILES | PERSON_PROFILES <= set(page.links)



def validate_assets(page):
    obsolete = {"twentyfifteen-style-css", "twentyfifteen-block-style-css", "twentyfifteen-jetpack-css", "sharedaddy-css", "social-logos-css"}
    assert not obsolete & page.ids, ("Obsolete render-blocking CSS", obsolete & page.ids)
    assert {"cookieadmin-style-css", "cookieadmin_js-js"} <= page.ids, "Consent assets missing"
    if "g539-druhsluby" in page.ids:
        assert {"grunion.css-css", "jp-forms-view-js-module", "akismet-frontend-js"} <= page.ids, "Form/antispam assets missing"


def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": "Polarita-SEO-verification/1.0"}), timeout=30) as r:
        assert r.status == 200 and r.url == url, (url, r.status, r.url)
        assert "noindex" not in r.headers.get("X-Robots-Tag", "").lower()
        data = r.read(2_000_001)
        assert len(data) <= 2_000_000, "Bound exceeded"
        return data.decode("utf8")


def main():
    manifest = json.loads((Path(__file__).parent / "src/pages/manifest.json").read_text(encoding="utf8"))
    urls = [x["url"] for x in manifest]
    with ThreadPoolExecutor(max_workers=4) as pool:
        texts = list(pool.map(fetch, urls))
    pages = {}
    for url, text in zip(urls, texts):
        p = SEOPage()
        p.feed(text)
        validate(p, url)
        validate_assets(p)
        pages[url] = p
        print("PASS metadata/entity:", url)
    assert len({p.titles[0] for p in pages.values()}) == len(urls), "Duplicate titles"
    assert len({p.descriptions[0] for p in pages.values()}) == len(urls), "Duplicate descriptions"
    count = 0
    for source, p in pages.items():
        for link in p.links:
            a = urlsplit(urljoin(source, link))
            target = a._replace(fragment="", query="").geturl()
            if target in pages:
                if a.fragment:
                    assert unquote(a.fragment) in pages[target].ids, (source, link, "Missing anchor")
                count += 1
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap = ET.fromstring(fetch(BASE + "sitemap-1.xml"))
    listed = {x.text for x in sitemap.findall("s:url/s:loc", ns)}
    assert set(urls) <= listed, "Commercial sitemap entries missing"
    news = ET.fromstring(fetch(BASE + "news-sitemap.xml"))
    assert BASE + "skoleni-a-zkousky-elektro/" not in {x.text for x in news.findall("s:url/s:loc", ns)}
    robots = RobotFileParser()
    robots.parse(fetch(BASE + "robots.txt").splitlines())
    for bot in ("Googlebot", "Bingbot", "OAI-SearchBot"):
        assert all(robots.can_fetch(bot, u) for u in urls), bot
    print(f"PASS {len(urls)} commercial pages, {count} commercial links/anchors, sitemap, news and robot rules")
    print("Outside this automated check: actual indexation, genuine crawler IP access, mail delivery, analytics, field CWV")


if __name__ == "__main__":
    main()
