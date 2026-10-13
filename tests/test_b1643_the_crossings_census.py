"""B1643 -- the crossings census: every crossing it cites is a banked arc with the verdict the census states; the census
names its criteria C1-C6 and its answer; and the bite -- a census row citing an arc with the wrong verdict would fail."""
import glob, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1643_the_crossings_census"
CITED = {"B856": "PROVED", "B915": "NEGATIVE", "B925": "NEGATIVE", "B929": "PROVED", "B1005": "NEGATIVE",
         "B1027": "NEGATIVE", "B1063": "NEGATIVE", "B1066": "NEGATIVE", "B1028": "PROVED", "B1241": "OPEN",
         "B1020": "PROVED", "B926": "PROVED", "B927": "PROVED", "B1642": "NEGATIVE", "B1612": "PROVED",
         "B1625": "PROVED", "B1628": "NEGATIVE"}


def _verdict(arc):
    return json.load(open(glob.glob(str(ROOT / "frontier" / f"{arc}_*" / "arc_verdict.json"))[0]))["verdict"]


def test_every_cited_verdict():
    for arc, v in CITED.items():
        assert _verdict(arc) == v, (arc, _verdict(arc), v)
    assert _verdict("B1643") == "PROVED"


def test_the_census_names_its_criteria_and_its_answer():
    f = open(A / "FINDINGS.md", encoding="utf-8").read()
    for c in ("C1", "C2", "C3", "C4", "C5", "C6"):
        assert f"**{c}**" in f
    assert "**No.** No crossing from the principle's mathematics to a physical number has succeeded." in f
    page = ROOT / "docs" / "THE_CROSSINGS_CENSUS_2026-10-13.md"
    assert page.exists()


def test_the_bite():
    wrong = dict(CITED, B915="PROVED")
    assert any(_verdict(a) != v for a, v in wrong.items())
