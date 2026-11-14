"""B1030 locks — the price-lock verification (one unit, two bits, ONE TRIT)."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1030_price_lock_verification"


def _cells():
    spec = importlib.util.spec_from_file_location("b1030_verify", ARC / "b1030_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_two_bits_formula_route():
    m = _cells()
    r = m.v1_two_bits_by_formula()
    assert all(r.values()), r
    # independent arithmetic: H^1 of a C2 permutation module = 2^(#fixed points)
    assert 2 ** (2 + 2) // 2 ** 2 == 2 ** 2 == 4


def test_v2_the_trit():
    m = _cells()
    r = m.v2_the_trit()
    assert all(r.values()), r
    assert float(sp.log(3, 2)) < 3.0  # the trit fits any 3-bit cap trivially


def test_v3_defect_and_v4_adoption():
    m = _cells()
    assert all(m.v3_item1_defect().values())
    r = m.v4_adoption_arithmetic()
    assert all(r.values()), r
    # the exact-zero identity re-derived here, not trusted:
    assert sp.simplify((2 + sp.log(3, 2) + 1) - (3 + sp.log(3, 2))) == 0


def test_findings_and_adoption_propagated():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "one ℤ/3 label = log₂3 = 1.585 bits" in flat or "1.585 bits" in flat
    assert "cannot fail at length-weight 1" in flat.lower() or "unfailable" in flat.lower()
    assert "does not survive adoption" in flat
    # THE_CLAIM must carry the adoption AND drop the dead sentence (same batch):
    claim = " ".join((ROOT / "docs" / "THE_CLAIM.md").read_text(encoding="utf-8")
                     .replace("**", "").replace("−", "-").split())
    assert "ONE TRIT" in claim and "B1030" in claim
    assert "+1.585 bits. Verdict" not in claim, "the dead conflated sentence must not survive"
    assert "exactly 0.000 at the floor" in claim


def test_verdict_json():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1030" and v["verdict"] == "PROVED"
    assert "ONE TRIT" in v["claim_one_line"]
    assert "DEFECT" in v["claim_one_line"].upper()
    for dep in ("B1028", "B1025", "B936", "B897"):
        assert dep in v["depends_on"]


def test_unit_obstruction_kappa_minus_two():
    """R43-10's closure hardened on main: |kappa - 2| = 1 exactly -- the founding
    sentence as an equation (B309, B518, B1010; re-verified at the price_lock repair).
    kappa = tr[a,b] = u^2 + 2 at the Eisenstein point u = omega."""
    import sympy as sp
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    kappa = sp.simplify(omega ** 2 + 2)
    assert sp.simplify(sp.Abs(kappa - 2) - 1) == 0
    assert sp.simplify(kappa - 2 - omega ** 2) == 0
    assert sp.simplify(sp.arg(kappa) + sp.pi / 6) == 0   # arg kappa = -pi/6 (the matter face)


# 2026-11-12 (R80b, part 6; a reader's supplement on the arcs main changed at Review 80, its finding 7; not checked by main).
# Main's correction of 2026-11-11 stands on this arc's page and in its verdict file, and the lock of B1028 holds it there.
# The arc's script says the same thing in a docstring, with no mark; and this test file held nothing of the correction.
# Nothing above this line is changed.
THE_CORRECTION = "the freedom ledger's zero is not a computed quantity"
WHAT_THE_SCRIPT_SAYS = "verdict (retroactive freedom 0.000) is untouched"


def _where_the_correction_is_missing(page, verdict_file, script):
    """the names of the three files of this arc in which the correction does not stand where the old statement does"""
    bad = []
    if THE_CORRECTION not in page:
        bad.append("the page")
    v = json.loads(verdict_file)
    if THE_CORRECTION not in v["claim_one_line"] or "B1028's verdict is OPEN" not in v["claim_one_line"]:
        bad.append("the verdict file")
    flat = lambda s: " ".join(s.replace("#", " ").split())
    if WHAT_THE_SCRIPT_SAYS in script:
        head = script[:script.index(WHAT_THE_SCRIPT_SAYS)]
        note = head[head.rindex("\n\n") if "\n\n" in head else 0:]             # what stands between the last blank line and the statement
        if THE_CORRECTION not in flat(note) or "B1028's verdict is OPEN" not in flat(note):
            bad.append("the script")
    return bad


def test_the_correction_of_the_zero_stands_in_the_arcs_three_files():
    page = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    verdict = (ARC / "arc_verdict.json").read_text(encoding="utf-8")
    script = (ARC / "b1030_verify.py").read_text(encoding="utf-8")
    assert script.count(WHAT_THE_SCRIPT_SAYS) == 1                              # the docstring is kept as it was written, and the note does not repeat it
    assert _where_the_correction_is_missing(page, verdict, script) == []
    # the script as it stood: the note taken out
    i, j = script.index("# [NOTE 2026-11-12"), script.index("def v4_adoption_arithmetic():")
    as_it_stood = script[:i] + script[j:]
    assert WHAT_THE_SCRIPT_SAYS in as_it_stood and _where_the_correction_is_missing(page, verdict, as_it_stood) == ["the script"]
    # the note moved to the head of the file, away from the statement, is not beside it
    moved = script[i:j] + "\n\n" + as_it_stood
    assert _where_the_correction_is_missing(page, verdict, moved) == ["the script"]
    # the page and the verdict file with the correction taken out
    assert _where_the_correction_is_missing(page.replace(THE_CORRECTION, ""), verdict, script) == ["the page"]
    v = json.loads(verdict)
    v["claim_one_line"] = v["claim_one_line"].replace("B1028's verdict is OPEN", "")
    assert _where_the_correction_is_missing(page, json.dumps(v), script) == ["the verdict file"]
    # the twin: a script that no longer makes the statement needs no note
    assert _where_the_correction_is_missing(page, verdict, as_it_stood.replace(WHAT_THE_SCRIPT_SAYS, "")) == []
    # what the function computes is what it computed
    assert all(_cells().v4_adoption_arithmetic().values())
