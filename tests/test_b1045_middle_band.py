"""B1045 locks — B485 is B1040's law in another vocabulary; the middle band is a MAP."""
import json
import pathlib
import re
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts" / "checks"))
import law_siblings as ls  # noqa: E402

_R = json.loads((_ROOT / "frontier" / "B1045_middle_band_mapped" / "results.json")
                .read_text(encoding="utf-8"))


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_alexander_law_is_the_char_poly_of_the_squared_monodromy():
    m, a = sp.symbols("m a")
    M = sp.Matrix([[m, 1], [1, 0]])
    assert sp.expand((M * M).charpoly(a).as_expr() - (a**2 - (m**2 + 2) * a + 1)) == 0
    lam = (m + sp.sqrt(m**2 + 4)) / 2
    assert sp.simplify(sp.expand((a**2 - (m**2 + 2) * a + 1).subs(a, lam**2))) == 0


def test_the_widened_fingerprint_reaches_B485_and_the_old_one_did_not():
    c = json.loads(list(_ROOT.glob("frontier/B485_*/arc_verdict.json"))[0]
                   .read_text(encoding="utf-8"))["claim_one_line"]
    old = r"isomonodrom|Painlev|Schlesinger|Vieta|Jimbo|Fricke cubic"
    assert not re.search(old, c, re.I)                                   # the miss
    assert re.search(ls.FINGERPRINTS["isomonodromy (B1040)"], c, re.I)   # the fix


def test_the_limitation_is_stated_not_hidden():
    reg = re.sub(r"\s+", " ", (_ROOT / "docs" / "consolidation" / "LAW_SIBLINGS.md")
                 .read_text(encoding="utf-8"))
    assert "TRANSLATION between vocabularies escapes it" in reg
    assert "not fixable by adding terms" in reg


def test_the_band_is_labelled_a_map_and_carries_its_error_rate():
    led = (_ROOT / "docs" / "consolidation" / "DEBT_LEDGER.md").read_text(encoding="utf-8")
    assert "MAPPED, not dispositioned" in led
    assert "5 of 58" in led
    assert "unverified" in led          # the other 53 are hypotheses, and say so


def test_the_two_denials_are_real_and_the_third_was_withdrawn():
    """B345 and B316 deny their assigned cluster; B346 only contrasts. The first draft said three."""
    def claim(b):
        return json.loads(list(_ROOT.glob(f"frontier/{b}_*/arc_verdict.json"))[0]
                          .read_text(encoding="utf-8"))["claim_one_line"]
    assert "independent of the E6-exponent grading" in claim("B345")
    assert "not a metallic-ladder member" in claim("B316").lower()
    c = _R["checks"]["and_TWO_of_the_five_are_arcs_whose_claim_line_DENIES_the_cluster"]
    assert c["pass"] and sorted(c["denying"]) == ["B316", "B345"]
