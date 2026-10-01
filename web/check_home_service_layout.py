"""Check homepage service separation locally and anonymously. Never submits a form."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen

TRAINING = "/skoleni-a-zkousky-elektro/"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Layout(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.sections = []
        self.links = {"revize": [], "skoleni": [], "hero": []}
        self.training_h2 = 0
        self.inspection_cards = 0
        self.h1 = 0
        self.nested_training = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        current = [x[1] for x in self.stack]
        if tag == "section" and data.get("id"):
            self.sections.append(data["id"])
        if data.get("id") == "skoleni" and "revize" in current:
            self.nested_training = True
        if tag == "h1":
            self.h1 += 1
        if tag == "h2" and "skoleni" in current:
            self.training_h2 += 1
        if tag == "article" and "revize" in current:
            self.inspection_cards += 1
        if tag == "a":
            for scope in self.links:
                if scope in current:
                    self.links[scope].append(data.get("href", ""))
        scope = data.get("id", "")
        if "pk-hero" in data.get("class", "").split():
            scope = "hero"
        if tag not in VOID:
            self.stack.append((tag, scope))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break


def check(text):
    page = Layout()
    page.feed(text)
    assert page.sections.count("skoleni") == 1, "Missing or duplicate independent training section"
    assert not page.nested_training, "Training nested in inspection section"
    assert page.sections.index("skoleni") < page.sections.index("revize"), "Training is buried after inspections"
    assert TRAINING not in page.links["revize"], "Training is still classified as an inspection"
    assert page.inspection_cards == 6, page.inspection_cards
    assert page.training_h2 == 1, "Training needs its own heading"
    assert TRAINING in page.links["skoleni"], "Training has no path to its landing page"
    assert "tel:+420792779534" in page.links["skoleni"]
    assert "#skoleni" in page.links["hero"], "Training is absent from hero actions"
    assert "#poptavka" in page.links["hero"], "Inspection action was removed"
    assert page.h1 == 1, page.h1


def self_test():
    cards = "<article></article>" * 6
    good = ('<section class="pk-hero"><h1>Services</h1><a href="#skoleni">Training</a>'
            '<a href="#poptavka">Inspection</a></section><section id="skoleni"><h2>Training</h2>'
            f'<a href="{TRAINING}">Details</a><a href="tel:+420792779534">Call</a></section>'
            f'<section id="revize">{cards}</section>')
    check(good)
    bad = [good.replace('<section id="revize">', f'<section id="revize"><a href="{TRAINING}">Training</a>'),
           good.replace('id="skoleni"', 'id="other"'),
           good.replace('href="#skoleni"', 'href="#other"')]
    for fixture in bad:
        try:
            check(fixture)
        except AssertionError:
            continue
        raise AssertionError("A layout regression was accepted")
    print("PASS: valid layout accepted; mixed services and missing training actions rejected")


if __name__ == "__main__":
    self_test()
    check((Path(__file__).parent / "src/pages/polarita.html").read_text(encoding="utf-8"))
    print("PASS: local homepage layout")
    with urlopen("https://www.polarita.cz/", timeout=25) as response:
        assert response.status == 200
        data = response.read(2_000_001)
        assert len(data) <= 2_000_000, "Response exceeds read bound"
        check(data.decode("utf-8"))
    print("PASS: anonymous published homepage layout")
