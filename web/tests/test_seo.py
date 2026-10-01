"""Offline negative fixtures for public SEO check; no providers or site writes."""
from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_seo import BASE, COMPANY_PROFILES, PERSON_PROFILES, SEOPage, validate, validate_assets


def valid_page():
    p = SEOPage()
    p.lang, p.h1 = "cs", 1
    p.titles = ["Revize a přezkoušení"]
    p.descriptions = ["Revize se školením a přezkoušením"]
    p.canonicals = [BASE]
    p.og = {"og:title": p.titles[:], "og:description": p.descriptions[:], "og:url": [BASE]}
    p.links = ["tel:+420792779534", "mailto:vaclav.sercl@polarita.cz", "https://www.polarita.eu/"]
    p.graph = [
        {"@type": "Organization", "sameAs": sorted(COMPANY_PROFILES)},
        {"@type": "Person", "@id": BASE+"#vaclav-sercl", "name": "Václav Šercl", "url": BASE+"kontakt/#vaclav-sercl", "worksFor": {"@id": BASE+"#organization"}, "sameAs": sorted(PERSON_PROFILES)},
        {"@type": "WebPage", "name": p.titles[0], "description": p.descriptions[0], "url": BASE, "dateModified": datetime.now(timezone.utc).isoformat()},
        {"@type": "WebSite"}, {"@type": "BreadcrumbList"}]
    return p


class SEOTests(unittest.TestCase):
    def test_asset_regressions(self):
        p = SEOPage()
        p.ids = {"cookieadmin-style-css", "cookieadmin_js-js", "g539-druhsluby", "grunion.css-css", "jp-forms-view-js-module", "akismet-frontend-js"}
        validate_assets(p)
        p.ids.add("sharedaddy-css")
        with self.assertRaises(AssertionError):
            validate_assets(p)
        p.ids.remove("sharedaddy-css")
        p.ids.remove("akismet-frontend-js")
        with self.assertRaises(AssertionError):
            validate_assets(p)

    def test_valid(self):
        validate(valid_page(), BASE)

    def test_rejects_old_home_metadata(self):
        p = valid_page()
        p.titles = ["Revize elektro"]
        p.og["og:title"] = p.titles[:]
        p.graph[2]["name"] = p.titles[0]
        with self.assertRaises(AssertionError):
            validate(p, BASE)

    def test_rejects_noindex_duplicate_and_wrong_canonical(self):
        for attr, value in (("robots", ["noindex"]), ("titles", ["a", "b"]), ("canonicals", [BASE+"other/"]), ("h1", 2)):
            p = valid_page()
            setattr(p, attr, value)
            with self.assertRaises(AssertionError):
                validate(p, BASE)

    def test_rejects_profile_misclassification(self):
        p = valid_page()
        p.graph[0]["sameAs"] = sorted(PERSON_PROFILES)
        with self.assertRaises(AssertionError):
            validate(p, BASE)

    def test_parser_accumulates_script_chunks(self):
        p = SEOPage()
        p.feed('<html lang="cs"><title>Revize ')
        p.feed('a školení</title><script type="application/ld+json">{"@graph":[')
        p.feed('{"@type":"Person"}]}</script></html>')
        self.assertEqual(p.titles, ["Revize a školení"])
        self.assertEqual(p.graph, [{"@type": "Person"}])


if __name__ == "__main__":
    unittest.main()
