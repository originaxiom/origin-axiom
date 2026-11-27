"""B2018's lock: the plant list committed here is the one sealed before reading (its sha256); it holds eight plants in three
folders, three, three and two; and the review's page mends are present on the pages they mend."""
import hashlib
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def test_plants_sealed():
    b = (HERE / "plants.txt").read_bytes()
    assert hashlib.sha256(b).hexdigest() == "440211cdfc9192435a6665c482d4e2ecf74bdd872e6150c1b2d94b68f3d9f54c"
    ids = re.findall(r"^([ABC][1-9]) ", b.decode(), re.M)
    assert ids == ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]


def test_the_probes_found_every_serious_code_finding_real():
    run = (HERE / "probe_run.txt").read_text()
    lines = [l for l in run.splitlines() if l.strip()]
    assert len(lines) == 17 and all("HOLDS" in l for l in lines), lines


def test_page_mends_present():
    page = lambda rel: (ROOT / rel).read_text(encoding="utf-8")
    assert "fails on the sealed commit,\n  exiting 1 with no traceback" in page("docs/CLAIM_CARD.md")
    assert "the card is its own expectation" in page("docs/roles/PRODUCER.md")
    assert "Commit the card before you run the decisive script" not in page("docs/roles/PRODUCER.md").split("*[CHANGED")[0]
    assert "the author's three below it" in page("docs/roles/PRODUCER.md")
    assert "No sealed look, and no comparison with data" in page("docs/roles/PRODUCER.md")
    rules = page("docs/roles/THE_RULES_SORTED.md")
    assert "(owed in the thin path)" not in rules and "the record check's `waits_on` (T6, landed)" in rules
    assert "within a day" not in rules
    bank = page("docs/roles/BANKING.md")
    assert "A card is VERIFIED only when both ACCEPT it." in bank
    assert "a card you cannot reproduce or re-derive\n  is RETURNED" in bank
    assert "VERIFIED is both banking seats' ACCEPT." in page("docs/seats/README.md")
    assert "*[RETIRED 2026-11-27 (Review 88; P-885): work cards are retired" in page("docs/seats/README.md")


def test_the_live_code_is_not_the_planted_copy():
    q = lambda name: (ROOT / "scripts" / "queue" / name).read_text(encoding="utf-8")
    assert 'CARD_PATH = re.compile(r"relays/claims/CLAIM_[A-Za-z0-9._-]+\\.md")' in q("queue_schema.py")
    assert '"requests"' not in q("card_form.py")
    assert '"%.12g"' in q("rerun.py")
    assert 'seen["at"] > rec["history"][0]["at"]' in q("custody.py")
    assert "sealed look" in q("record_check.py")
