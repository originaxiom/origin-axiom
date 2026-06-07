"""B120 -- locking test: the trivial-point tower is determined by (n; trace, det).
Banks Chat-2 Q2/Q3 + Supplement S1-S5 with three verify-don't-trust corrections (S1 formula, S5 closed form +
heights-to-n, the theta/Sym units error). The tower (Sym two-sequence, B117/B103) is fixed by two inputs --
unfolding depth n and the abelianization seed (trace,det). NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b120", _ROOT / "frontier" / "B120_tower_determination" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_q3_tower_determined_by_trace_det():
    q = B.tower_determined_by_trace_det()
    assert q["same_invariants"] is True and q["distinct_matrices"] is True
    assert q["all_identical"] is True            # distinct same-(tr,det) matrices -> identical towers (n=3,4,5)


def test_s2_m_universality_of_sym_content():
    s = B.m_universality_of_sym_content()
    assert s["m_universal"] is True              # Sym content identical for m=1,2,3 (n=4 tower)
    # honest scope: a reduction/reframing, not a closure
    assert "not a closure" in s["scope"] or "reduction" in s["scope"]


def test_s1_doubling_range_forced_corrected():
    s = B.doubling_range_forced(10)
    assert s["doubling_equals_deficit"] is True   # doubling-sum == (n-4)(n+1)/2
    assert s["handoff_formula_off_by"] == {2}     # the handoff's (n^2-3n)/2 is off by exactly 2
    assert s["handoff_formula_wrong"] is True


def test_s3_s5_height_count_closed_form_corrected():
    s = B.height_count_closed_form(8)
    assert s["count0_is_n_minus_1"] is True       # S3
    assert s["closed_form_matches"] is True        # S5: the corrected closed form (heights 0..n)
    assert s["sums_to_n2_minus_1"] is True          # the total lock
    assert s["handoff_guess_fails"] is True         # 2*max(1,n-h-1) is wrong


def test_q2_degree_rank_split():
    q = B.degree_rank_split(8)
    assert q["spectral_all_n"] is True            # (I) spectral: mu_n=1 for all n
    assert q["geometric_order"] == {3: 4, 4: 3, 5: 2, 6: None}   # (II) geometric: order {4,3,2,inf}
    assert q["geometric_n_in_3_4"] is True


def test_s4_b116_factor_level_confirm():
    s = B.b116_factor_level_confirm()
    assert s["agree_through_n5"] is True and s["diverges_at_n6"] is True   # B116 stands (factor-level)
