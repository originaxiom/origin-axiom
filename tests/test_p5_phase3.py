"""P5 Phase 3 — locks the verdict and the two vacuity repairs.

The draft is WITHDRAWN: its core is Baake-Grimm-Joseph 1993. These locks guard (a) that the
verdict stays recorded, and (b) that the two artifacts which certified nothing now compute.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P5 = ROOT / "papers" / "P5_monoid"


def _hopf():
    spec = importlib.util.spec_from_file_location("hopf", P5 / "hopf_separation.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_verdict_records_the_prior_art_with_its_source():
    t = " ".join((P5 / "PHASE3_VERDICT.md").read_text(encoding="utf-8").split())
    assert "Baake, Grimm & Joseph" in t and "1993" in t
    assert "Peyri" in t and "Kol" in t
    assert "invertible if and only if P_ϱ ≡ 1" in t or "invertible iff P_ϱ ≡ 1" in t
    assert "does not stand" in t or "is not a paper" in t


def test_the_recheck_records_BOTH_directions():
    """A prior-art call that only checks the death half is half a check."""
    t = " ".join((P5 / "PHASE3_VERDICT.md").read_text(encoding="utf-8").split())
    assert "RE-CHECK" in t
    assert "overstated" in t, "the reviewer's 'verbatim' claim must be corrected, not repeated"
    assert "confirmed by absence, measured" in t
    assert "Verdict unchanged" in t


def test_the_reproducer_DERIVES_its_matrices_from_words():
    """The vacuity: both matrices were previously built from the SAME literal argument."""
    m = _hopf()
    src = (P5 / "hopf_separation.py").read_text(encoding="utf-8")
    assert "abelianization_of(TM_A, TM_B)" in src, "matrices must come from the image WORDS"
    assert m.exponent_sums("aaabAB") == (2, 0), "exponent sums must be computed by free reduction"
    assert m.substitute("aB", "ab", "ab") == "", "the kernel must be found by substitution"
    assert m.substitute("aB", "ab", "ba") != "", "and TM must NOT kill it"


def test_the_reproducer_CAN_FAIL():
    """A negative control must exist, or `same` is true by construction as before."""
    m = _hopf()
    assert m.TM == m.S4
    assert m.TM != m.CTRL, "the control pair must NOT share an abelianization"


def test_the_scope_is_confined_to_det_zero():
    """det != 0 => injective, so the forgetting cannot happen off the singular fibre."""
    m = _hopf()
    assert all(M.det() == 0 for M in (m.TM, m.S4, m.PSI1, m.PSI2))
    t = " ".join((P5 / "PHASE3_VERDICT.md").read_text(encoding="utf-8").split())
    assert "det ≠ 0 ⟹ injective" in t


def test_the_banked_kernel_check_is_no_longer_a_tautology():
    """verify_monoid.py's s4_kernel was x*x^-1 = 1 -- true for every element of every group."""
    src = (ROOT / "frontier" / "B497_endomorphism_monoid"
           / "verify_monoid.py").read_text(encoding="utf-8")
    assert "not _src.is_identity" in src, "the source word must be checked nontrivial"
    assert "TRUE FOR EVERY ELEMENT OF EVERY GROUP" in src, "the defect must stay documented"
