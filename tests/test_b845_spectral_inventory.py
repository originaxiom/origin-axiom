"""B845 — locks the spectral inventory and the JSON/table discrepancy."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HARVEST = ROOT / "frontier" / "B797_maass_spectrum_harvest"


def test_no_spectral_paper_exists():
    """The phantom the register carried for five reviews."""
    hits = [p for p in (ROOT / "papers").rglob("*.md")
            if re.search(r"maass|spectrum|eigenvalue", p.name, re.I)]
    assert not hits, f"a spectral paper now exists in papers/: {hits} -- update B845"


def test_the_certified_spectrum_is_in_the_frontier():
    for slug in ("B794_congruence_level4", "B795_eigenvalue_verification",
                 "B797_maass_spectrum_harvest"):
        assert (ROOT / "frontier" / slug / "FINDINGS.md").is_file(), slug


def test_b792_is_NOT_in_main():
    """It is cc3's arc; cc3 never merges. Citing it as if it were here is the phantom's class."""
    assert not list((ROOT / "frontier").glob("B792_*")), "B792 appeared in main -- was it harvested?"


def test_the_json_now_MATCHES_its_own_table():
    """B845 found 6 in the JSON vs 17 in the table; B846 completed it. This now guards the fix.

    The table is a TWO-COLUMN layout: 9 rows carrying n and n+9, so 17 eigenvalues (the last row
    has one). Count the r values, not the rows -- and tolerate markdown emphasis, since one entry
    is bolded (`| 6 | **7.072004187** |`) and a stricter pattern silently lost that row.
    """
    e = json.loads((HARVEST / "eigenvalues_final.json").read_text(encoding="utf-8"))["eigenvalues"]
    text = (HARVEST / "FINDINGS.md").read_text(encoding="utf-8")
    certified = len(re.findall(r"\|\s*\*{0,2}\d\.\d{9}\*{0,2}\s*\|", text))
    assert certified >= 17, f"the certified spectrum shrank to {certified} eigenvalues"
    assert len(e) == certified, (
        f"the JSON carries {len(e)} of {certified} certified eigenvalues -- it must serialize the "
        f"whole table, or a reader silently gets a truncated spectrum (B845/B846)")


def test_the_added_entries_do_NOT_fabricate_diagnostics():
    """The 11 table-sourced entries carry r/lambda/mult only; cc3's per-eigenvalue diagnostics
    were not harvested and must be marked ABSENT rather than invented."""
    e = json.loads((HARVEST / "eigenvalues_final.json").read_text(encoding="utf-8"))["eigenvalues"]
    added = [x for x in e if str(x.get("source", "")).startswith("FINDINGS")]
    assert len(added) == 11, f"expected 11 table-sourced entries, got {len(added)}"
    for x in added:
        assert "sv_tail" not in x and "S_invariance_dev" not in x, (
            f"n={x.get('n')} carries diagnostics it cannot have -- they were never harvested")
        assert "NOT IN MAIN" in x.get("diagnostics", ""), f"n={x.get('n')} must mark them absent"
