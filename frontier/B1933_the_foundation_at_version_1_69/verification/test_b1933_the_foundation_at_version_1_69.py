"""B1933's lock: the foundation at version 1.69, its m000 row and its list "Computed nowhere yet" (card C21)."""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("write_version_1_69", HERE / "write_version_1_69.py")
W = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(W)


def _problems(page):
    bad = []
    if W.HEADER_IS not in page:
        bad.append("not at 1.69")
    for name, line in (("the m000 row", W.ROW_IS), ("the list's m000 entry", W.LIST_IS), ("the list's first entry", W.FIRST_IS)):
        if page.count(line) != 1:
            bad.append(name)
    if W.ROW_WAS in page:
        bad.append("the old m000 row")
    return bad


def _taken_back(page):
    """the page with version 1.69 taken back: the three lines as they were, the entry and the version's line"""
    t = page.replace(W.ROW_IS, W.ROW_WAS).replace(W.LIST_IS, W.LIST_WAS).replace(W.FIRST_IS, W.FIRST_WAS)
    return t.replace(W.ENTRY, "").replace(W.HEADER_IS, W.HEADER_WAS)


def test_the_page_is_at_1_69_and_the_script_gives_it_again():
    page = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert _problems(page) == []
    assert page.index("- **v1.69 ") < page.index("- **v1.68 ")
    assert W.version_1_69(_taken_back(page)) == page


def test_each_cell_says_what_its_source_says():
    b1926 = next(ROOT.glob("frontier/B1926_*"))
    page = (b1926 / "FINDINGS.md").read_text(encoding="utf-8")
    claim = json.loads((b1926 / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "every level n = 1 to 8 has b₁ = 1 and cusp rank 1" in page
    assert "the twisted classes are the double cover's matter seen from below" in page and "three codes" in page
    assert "is a stated choice" in claim
    ledger = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    rows = {l.split("|")[1].strip(): l for l in ledger.split("\n") if l.startswith("| 17")}
    assert "B1926" in rows["1755"] and "B1926" in rows["1768"]
    assert "X-NEVER" in rows["1797"] and "eight chiral word states outside m004's levels" in rows["1797"]


def test_the_lock_refuses_the_old_row_and_the_mark_taken_off():
    page = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "the m000 row" in _problems(page.replace(W.ROW_IS, W.ROW_WAS))
    assert "the list's first entry" in _problems(page.replace(W.FIRST_IS, W.FIRST_WAS))
