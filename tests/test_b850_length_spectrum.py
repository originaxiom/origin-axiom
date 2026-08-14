"""Locks B850 -- the length spectrum as a computable shadow of the foliation algebra's type.

The locks that matter are the honesty ones: the systole positive control, the GENERIC verdict
(which is the arc's actual product), the CONDITIONAL on a cited reduction, and -- above all --
that Cell 4's two comparison bugs cannot come back, since the second of them inverted the answer.
"""
import importlib.util
from pathlib import Path

import mpmath as mp
import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b850", _ROOT / "frontier" / "B850_length_spectrum_type" / "length_spectrum_type.py")
b0 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b0)

mp.mp.dps = 40


def test_the_generators_satisfy_the_figure_eight_relator():
    """Computed, not cited -- the whole enumeration rests on these two matrices."""
    A, B = b0.gens_m004()
    assert b0.check_relator(A, B)


def test_generators_are_parabolic_and_the_trace_field_is_Q_sqrt_minus_3():
    A, B = b0.gens_m004()
    assert sp.simplify(A.trace()) == 2 and sp.simplify(B.trace()) == 2
    t = sp.simplify((A * B).trace())
    assert sp.sqrt(3) in t.atoms(sp.Pow) or sp.I in t.atoms(sp.I) or t.has(sp.I)


def test_systole_positive_control():
    """Sealed: the shortest length must reproduce m004's known systole, else INSTRUMENT VOID."""
    A, B = b0.gens_m004()
    lens = b0.lengths_from_group(A, B, maxlen=5)
    assert lens, "no lengths found"
    assert abs(lens[0]["ell"] - b0.KNOWN_SYSTOLE_M004) < mp.mpf("1e-9"), mp.nstr(lens[0]["ell"], 15)


def test_pslq_ratio_test_can_detect_a_RATIONAL_ratio():
    """Non-vacuity: if the test could never return 'rational', DENSE would be unfalsifiable."""
    with mp.workdps(40):
        l1 = mp.mpf("1.087070144995")
        ok, rel = b0.ratio_is_rational(l1, 3 * l1)
    assert ok, "a 3:1 ratio must be detected as rational"
    assert rel is not None


def test_pslq_ratio_test_returns_irrational_for_a_transcendental_ratio():
    with mp.workdps(40):
        l1 = mp.mpf("1.087070144995")
        ok, _ = b0.ratio_is_rational(l1, l1 * mp.pi)
    assert not ok, "pi is irrational; the test must not manufacture a relation"


def test_m004_length_spectrum_is_DENSE():
    A, B = b0.gens_m004()
    lens = b0.lengths_from_group(A, B, maxlen=6)
    d = b0.discreteness(lens)
    assert d["verdict"] == "DENSE"
    assert d["n_irrational"] >= 10
    # n_rational is NOT gated at 0. The enumeration ranges over group elements, so g^2 and g^3
    # appear with lengths exactly 2x and 3x the systole and contribute genuine integer ratios.
    # The original lock asserted n_rational == 0 and PASSED FOR THE WRONG REASON: complex()
    # truncated 40 dps to double precision, so true relations failed a 1e-25 residual bar and
    # were miscounted as irrational. The full suite caught it; an isolated run never would.
    assert d["n_rational"] >= 1, "powers of the systole element MUST give integer ratios"


def test_the_verdict_is_independent_of_global_mpmath_precision():
    """THE ORDER-DEPENDENT BUG. Precision is pinned locally with workdps; relying on the
    module-level mp.mp.dps let any other test's global setting change this arc's verdict."""
    import mpmath as _mp
    A, B = b0.gens_m004()
    lens = b0.lengths_from_group(A, B, maxlen=5)
    saved = _mp.mp.dps
    try:
        seen = []
        for dps in (15, 25, 40):
            _mp.mp.dps = dps
            d = b0.discreteness(lens)
            seen.append((d["verdict"], d["n_rational"], d["n_irrational"]))
        assert len(set(seen)) == 1, f"verdict moves with global precision: {seen}"
    finally:
        _mp.mp.dps = saved


def test_the_rational_ratios_are_exactly_the_integer_multiples():
    """They are powers, not coincidences -- so their presence is a check, not a blemish."""
    import mpmath as _mp
    A, B = b0.gens_m004()
    lens = b0.lengths_from_group(A, B, maxlen=6)
    l1 = lens[0]["ell"]
    ints = [d for d in lens[1:13] if abs(d["ell"] / l1 - _mp.nint(d["ell"] / l1)) < 1e-20]
    assert len(ints) >= 2, "g^2 and g^3 must appear in a length-6 enumeration"
    for d in ints:
        r = d["ell"] / l1
        assert abs(r - _mp.nint(r)) < 1e-20 and _mp.nint(r) >= 2


def test_the_arc_reports_the_binary_as_a_VERIFICATION_not_a_finding():
    """The seal pre-stated DENSE as forced by mixing. Lock the prose to saying so."""
    txt = (_ROOT / "frontier" / "B850_length_spectrum_type" / "FINDINGS.md").read_text("utf-8")
    low = txt.lower()
    assert "forced" in low and "verification" in low
    assert "generic" in low


def test_the_type_verdict_stays_CONDITIONAL():
    txt = (_ROOT / "frontier" / "B850_length_spectrum_type" / "FINDINGS.md").read_text("utf-8")
    assert "CONDITIONAL" in txt
    assert "DECLARED CITATION" in txt or "declared citation" in txt.lower()


# ---------------------------------------------------------------------------------------
# Cell 4's two bugs -- the second of which INVERTED the verdict
# ---------------------------------------------------------------------------------------
def test_numeric_path_deduplicates_traces_like_the_exact_path():
    """THE BUG THAT INVERTED CELL 4.

    The m004 path collects a SET of exact traces. If the control path counted WORDS instead,
    'multiplicity' compares distinct-traces-per-length against words-per-length -- inflating the
    control ~100x and reporting m015 max = 602 against m004's 4, i.e. the OPPOSITE conclusion.

    A 2-generator group enumerated to length 6 has 5460 words; distinct traces are far fewer.
    If this count ever approaches the word count again, the dedup has been lost.
    """
    src = (_ROOT / "frontier" / "B850_length_spectrum_type"
           / "length_spectrum_type.py").read_text("utf-8")
    fn = src[src.index("def numeric_group"):src.index("def ratio_is_rational")]
    assert "traces = {}" in fn, "the numeric path must deduplicate traces before bucketing"
    assert "apples to oranges" in fn, "the reason must stay documented where the fix lives"


def test_cell4_multiplicity_ordering_is_measured_against_a_control():
    """A number with nothing to compare it to is not a measurement -- the first Cell 4 bug."""
    import json
    p = _ROOT / "frontier" / "B850_length_spectrum_type" / "results.json"
    r = json.loads(p.read_text(encoding="utf-8"))
    c4 = r["cell4_multiplicity"]
    assert "controls" in c4 and c4["controls"], "Cell 4 must carry the comparison the seal required"
    assert "m015" in c4["controls"], "the NON-arithmetic control is the one that matters"
    assert c4["m004_max_traces_per_length"] > c4["controls"]["m015"]["max"]


def test_results_record_GENERIC_and_all_three_manifolds():
    import json
    r = json.loads((_ROOT / "frontier" / "B850_length_spectrum_type"
                    / "results.json").read_text(encoding="utf-8"))
    assert r["genericity"] == "GENERIC"
    assert set(r["verdicts"]) == {"m004", "m003", "m015"}
    assert set(r["verdicts"].values()) == {"DENSE"}
    assert "CONDITIONAL" in r["type_conditional"]


def test_the_prereg_is_sealed_and_its_hash_is_recorded():
    import hashlib
    p = _ROOT / "frontier" / "B850_length_spectrum_type" / "PREREGISTRATION.md"
    h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    ledger = (_ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert h in ledger, f"prereg hash {h} not in the seal ledger -- the seal is void"
