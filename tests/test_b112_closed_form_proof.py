"""B112 -- locking tests for the PROOF of the opposition-involution closed form (the sign half of rho_n).
The root-system reversal lemma (theta=-w0 on the height-h roots of A_{n-1}) gives (+1,-1) dims
(ceil((n-h)/2), floor((n-h)/2)) for all n<=12, all h; with B64's parity assignment this proves the closed form
mult char(M^h)=ceil((n-h)/2), char(-M^h)=floor((n-h)/2) for ALL n. NO physics; P1-P16 untouched."""
import importlib.util
import math
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b112", _ROOT / "frontier" / "B112_closed_form_proof" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_theta_acts_as_reversal_involution():
    for n in range(2, 13):
        for h in range(1, n):
            assert B.is_reversal_involution(n, h)        # theta = the reversal i -> (n-h+1)-i, P^2=I


def test_lemma_eigenspace_split_equals_ceil_floor_all_n():
    r = B.lemma_holds(12)
    assert r["all_match"] is True                        # (+1,-1) dims = (ceil, floor) for all n<=12, all h
    assert r["mismatches"] == []


def test_closed_form_matches_b62_and_b111_low_n():
    # height-2 splits (1,0),(1,1),(2,1) at n=3,4,5 (B62); the n=4 all-heights profile (B111)
    assert B.eigenspace_split(3, 2) == (1, 0)
    assert B.eigenspace_split(4, 2) == (1, 1)
    assert B.eigenspace_split(5, 2) == (2, 1)
    assert [B.eigenspace_split(4, h) for h in (1, 2, 3)] == [(2, 1), (1, 1), (1, 0)]


def test_global_invariants():
    for n in range(2, 13):
        assert B.excess(n)["matches"]                    # (+)-excess = floor(n/2)
        assert B.total_char_factors(n)["matches"]        # sum of dims = #positive roots = n(n-1)/2
