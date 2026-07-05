"""Locks for B441 (C5) — the WRT tool validations + the field-content verdict."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B441_child_wrt")
sys.path.insert(0, HERE)
import wrt as W
import field_content as FC


def test_wrt_tool_validated():
    ok_s3, ok_amphi = W.validate(dps=40)
    assert ok_s3      # tau_r(S^3) = 1 via +1 surgery on the unknot
    assert ok_amphi   # amphichirality: tau_r(4_1(5,1)) = conj tau_r(4_1(-5,1))


def test_field_method_validated():
    assert FC.method_ok()   # tau_r(S^3) reads as rational (Galois-twist method sound)


def test_child_wrt_field_is_surgery_forced():
    # C5 verdict: Field(tau_r(child)) == Field(tau_r(L(5,1) skeleton)) for all r -> Bin 3
    assert FC.child_field_is_forced()


def test_r15_forced_quadratics_present_in_skeleton_too():
    # sqrt5/sqrt-3/sqrt-15 appear in the child at r=15 -- but they are FORCED (in L(5,1) too)
    ch = FC.field_report(FC.cj_fig8, 5, 15)
    sk = FC.field_report(FC.cj_unknot, 5, 15)
    assert ch["has_sqrt5"] and ch["has_sqrtm3"] and ch["has_sqrtm15"]
    assert (ch["has_sqrt5"], ch["has_sqrtm3"], ch["has_sqrtm15"]) == \
           (sk["has_sqrt5"], sk["has_sqrtm3"], sk["has_sqrtm15"])
