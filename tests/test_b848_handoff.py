"""Locks B848 -- the independent verification of the incoming handoff bundle.

What these locks are FOR: the bundle's headline (the arrow census) is a claim the sending seat
got wrong four times, and its own record says every wrong version looked cleaner than the truth.
These lock the RECOMPUTED verdicts, the instrument's self-test, and -- the point of the arc --
the refutation of a stated mechanism whose conclusion happens to be correct.
"""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b848", _ROOT / "frontier" / "B848_handoff_verification" / "verify_handoff.py")
b8 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b8)


# --------------------------------------------------------------------------------------
# The instrument, before it is trusted on our data
# --------------------------------------------------------------------------------------
def test_reduction_cycle_reproduces_known_forms():
    """x^2-2y^2 and x^2-5y^2 represent both +-1; x^2-3y^2 and x^2-7y^2 never represent -1."""
    for a, b, c, both in [(1, 0, -2, True), (1, 0, -5, True),
                          (1, 0, -3, False), (1, 0, -7, False)]:
        p1, m1, _lead, _D = b8.represents_pm1(a, b, c)
        assert p1, f"({a},{b},{c}) must represent +1"
        assert m1 is both, f"({a},{b},{c}): -1 representable should be {both}"


def test_cycle_rejects_a_definite_or_square_discriminant():
    """A form the statistic is not defined for must raise, not return a plausible number.

    Written with pytest.raises rather than try/except: the vacuity gate flagged the
    try/except form as unconditionally-passing, and it was right to -- a bare `continue`
    on the exception path carries no assertion the gate can see.
    """
    for bad in [(1, 0, 1), (1, 2, 1), (1, 0, -4)]:      # neg disc, disc 0, disc 16 = 4^2
        with pytest.raises(ValueError):
            b8.cycle_leads(*bad)
    # and the positive control: a form it IS defined for must come back with a cycle
    lead, D = b8.cycle_leads(1, 0, -2)
    assert D == 8 and lead


def test_conjugator_lattice_basis_actually_conjugates():
    """The derivation tr(P)=0 is verified by substitution, not assumed (an assumed criterion
    is how the first of the sending seat's four wrong attempts died)."""
    for w in b8.CLAIMED:
        A = b8.wm(w)
        Ai = A.inv()
        for M in b8.conjugator_lattice(A):
            assert M * A == Ai * M
            assert M != sp.zeros(2, 2)


# --------------------------------------------------------------------------------------
# The census -- the headline
# --------------------------------------------------------------------------------------
CENSUS = {                     # word: (trace, disc, amphichiral, arrow)
    "LR":     (3,  5,   True,  False),
    "LLRR":   (6,  8,   True,  False),
    "LRR":    (4,  12,  False, False),
    "LLRLR":  (10, 96,  False, False),
    "LLRLRR": (15, 221, True,  True),
    "LLRRLR": (15, 221, True,  True),
}


def test_arrow_census_reproduces_the_handoff_table():
    for w, (tr, disc, amphi, arrow) in CENSUS.items():
        A = b8.wm(w)
        a, ar, _lead, D = b8.verdict(A)
        assert int(A.trace()) == tr, w
        assert D == disc, w
        assert a is amphi, w
        assert ar is arrow, w


def test_box_search_independently_exhibits_every_conjugator_the_cycle_permits():
    """Second method, no shared code path with the lattice route."""
    for w, (_tr, _d, amphi, arrow) in CENSUS.items():
        found = b8.box_search(b8.wm(w))
        for det in found:                       # nothing found may be forbidden by the cycle
            assert (det == 1 and amphi) or (det == -1 and not arrow), w
        if amphi:
            assert 1 in found, f"{w}: cycle says +1 exists; the search must exhibit it"
        if not arrow:
            assert -1 in found, f"{w}: cycle says -1 exists; the search must exhibit it"


def test_arithmetic_bundles_are_exactly_the_both_signs_cases():
    """The trade-off headline: arithmetic => no arrow AND amphichiral."""
    for w in ["LR", "LLRR"]:
        amphi, arrow, _l, _D = b8.verdict(b8.wm(w))
        assert amphi and not arrow


def test_the_arrow_is_real_at_trace_15():
    amphi, arrow, lead, D = b8.verdict(b8.wm("LLRLRR"))
    assert arrow and D == 221 and -1 not in lead


# --------------------------------------------------------------------------------------
# The defect: a true identity that proves the wrong half
# --------------------------------------------------------------------------------------
def test_symmetric_identity_is_true_and_has_det_plus_one():
    """S A S^-1 = adj(A) for ANY symmetric A -- and det S = +1, which is amphichirality."""
    a, b_, d = sp.symbols("a b d")
    A = sp.Matrix([[a, b_], [b_, d]])
    S = sp.Matrix([[0, -1], [1, 0]])
    assert sp.simplify(S * A * S.inv() - A.adjugate()) == sp.zeros(2, 2)
    assert S.det() == 1


def test_symmetry_does_NOT_imply_absence_of_arrow():
    """The refutation, from inside the handoff's own table: LLRLRR is symmetric and has an
    arrow. Symmetry supplies det=+1 (amphichiral); 'no arrow' needs det=-1."""
    A = b8.wm("LLRLRR")
    assert A.T == A, "LLRLRR must be symmetric for this to be a counterexample"
    assert A.tolist() == [[2, 5], [5, 13]]
    amphi, arrow, _l, _D = b8.verdict(A)
    assert amphi is True and arrow is True


def test_metallic_conclusion_holds_and_the_real_mechanism_is_norm_minus_one():
    """No arrow for m=1..12 -- because disc = m^2+4 and the metallic mean is a unit of norm -1,
    not because the monodromy is symmetric (LLRLRR is symmetric and has an arrow)."""
    for row in b8.metallic_census(12):
        assert row["arrow"] is False, row
        assert row["disc"] == row["m"] ** 2 + 4, row
        assert row["symmetric"] is True, row
        # the mechanism, stated as arithmetic: N((m + sqrt(m^2+4))/2) = -1
        m = row["m"]
        assert (m * m - (m * m + 4)) // 4 == -1


# --------------------------------------------------------------------------------------
# Base rates -- new, and they sharpen the trade-off
# --------------------------------------------------------------------------------------
def test_base_rates_first_arrow_at_length_six_and_generic_by_ten():
    rows = {r["length"]: r for r in b8.base_rates(10)}
    assert all(rows[n]["arrow"] == 0 for n in range(2, 6)), "no arrow below length 6"
    assert rows[6]["arrow"] == 2 and rows[6]["classes"] == 12
    assert rows[10]["arrow"] == 60 and rows[10]["classes"] == 106
    assert rows[10]["arrow"] / rows[10]["classes"] > 0.5, "the arrow is GENERIC, not rare"


def test_amphichirality_never_occurs_at_odd_length_on_the_tested_range():
    rows = {r["length"]: r for r in b8.base_rates(9)}
    for n in (3, 5, 7, 9):
        assert rows[n]["non_amphichiral"] == rows[n]["classes"], n


# --------------------------------------------------------------------------------------
# The rest of the bundle
# --------------------------------------------------------------------------------------
def test_riley_polynomial_is_the_corrected_form():
    """Decided from the raw relation BOTH documents quote, not from either simplified form."""
    r = b8.riley()
    assert r["u_coeff_equals_const"], "=> u^2 + k(u+1): the correction, not the E6 probe's form"
    assert r["both_collapse_at_x2"], "why the parabolic check passed on the wrong polynomial"
    assert r["both_degree_2"], "so Gate C's deg>=2 residue mechanism survives the error"
    assert r["trefoil_degree"] == 1


def test_gky_power_sums_all_hold():
    for k, v in b8.gky().items():
        assert v["holds"], f"power sum k={k} failed at {v['max_abs_err']}"


def test_lambda_k_residues_and_that_the_two_routes_are_one():
    r = b8.lambda_k()
    assert r["res_LambdaK_is_one_sixth"]
    assert r["res_phi_matches_handoff"]
    assert r["vol_equals_12sqrt3_LK2"]
    # the withdrawal was correct: the "3.6e-20 agreement" is algebra, not corroboration
    assert r["two_routes_are_algebraically_identical"]


def test_e6_exponent_arithmetic():
    e = b8.e6()
    assert e["dim_is_78"] and e["block_dims"] == [3, 9, 11, 15, 17, 23]
    assert e["sum_exponents"] == 36 and e["cartan_det"] == 3 and e["coxeter"] == 12
    assert e["h1_equals_rank"]


def test_the_L_R_convention_gap_is_real():
    """C = [[1,0],[-1,-1]] works only under the swapped convention, which the bundle omits."""
    C = sp.Matrix([[1, 0], [-1, -1]])
    std = b8.wm("LR")
    swp = b8.wm("LR", b8.R, b8.L)
    assert C * std * C.inv() != std.inv()
    assert C * swp * C.inv() == swp.inv()
    assert C.det() == -1


def test_main_carries_seventeen_eigenvalues_not_fortythree():
    """Four of the six handoff documents say 43. Measured in main: 17."""
    import json
    p = _ROOT / "frontier" / "B797_maass_spectrum_harvest" / "eigenvalues_final.json"
    assert len(json.loads(p.read_text(encoding="utf-8"))["eigenvalues"]) == 17
