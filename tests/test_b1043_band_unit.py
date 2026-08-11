"""B1043 locks — the band is the wrong unit; B564 closes what B1039 restored as open."""
import glob
import json
import pathlib
import re

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_R = json.loads((_ROOT / "frontier" / "B1043_the_band_is_the_wrong_unit" / "results.json")
                .read_text(encoding="utf-8"))


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_B564_closes_the_conjecture_and_says_so_itself():
    v = json.loads(pathlib.Path(glob.glob(str(_ROOT / "frontier/B564_*/arc_verdict.json"))[0])
                   .read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and not v.get("instrument")
    assert "contains no irreducible representation" in v["claim_one_line"]
    f = pathlib.Path(glob.glob(str(_ROOT / "frontier/B564_*/FINDINGS.md"))[0]).read_text(
        encoding="utf-8")
    assert "confirms the B141 Item-4 conjecture" in re.sub(r"\s+", " ", f)


def test_the_in_band_bodies_carry_no_forward_pointer():
    """The reason step 1 could not catch it: a body cannot cite its own future."""
    for pat in ("frontier/B141_*/FINDINGS.md", "frontier/B142_*/FINDINGS.md"):
        assert "B564" not in pathlib.Path(glob.glob(str(_ROOT / pat))[0]).read_text(
            encoding="utf-8")


def test_B1039_now_records_that_item_4_is_closed():
    assert "B564 CLOSED it" in (_ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "settled four hundred arcs later" in (
        _ROOT / "frontier" / "B1039_phi_fixed_and_metallic_exponent" / "FINDINGS.md"
    ).read_text(encoding="utf-8")


def test_B232_is_B1038s_law_differentiated():
    x, y, t = sp.symbols("x y t")

    def h(d, vs):
        if d < 0:
            return sp.Integer(0)
        gf = sp.prod([1 / (1 - v * t) for v in vs])
        return sp.expand(sp.series(gf, t, 0, d + 1).removeO().coeff(t, d))

    V, W = (x, y), (x, y, 1)

    def band(n):
        return sp.expand(h(n, W) + h(n - 3, W) - h(1, W))

    for n in range(3, 11):
        assert sp.simplify(band(n) - band(n - 1) - h(n, V) - h(n - 3, V)) == 0, n
        assert sp.simplify(band(n).subs({x: 1, y: 1}) - (n * n - 1)) == 0, n


def test_the_siblings_are_named_so_the_next_pass_starts_from_evidence():
    c = _R["checks"]["every_restored_law_but_one_has_siblings_STILL_IN_DEBT_in_other_bands"]
    sib = c["siblings"]
    assert "B564" in sib["phi-fixed reducibility (B1039)"]
    assert "B232" in sib["the tower (B1038)"]
    assert sib["isomonodromy (B1040)"] == []          # the control: a law CAN be band-local
    leads = (_ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "L164" in leads
    for b in ("B33", "B232", "B522", "B564", "B75", "B77", "B106", "B257"):
        assert b in leads, b
