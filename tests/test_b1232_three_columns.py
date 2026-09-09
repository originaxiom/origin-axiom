"""B1232 -- codex R031A/R031B verified here; three retractions; the third column.

These locks pin the RETRACTIONS. If a later seat restores "sigma in Q is a reduction" or
"no receiver for k therefore k=1", the suite reds -- both were load-bearing and both were wrong.
"""
import json, pathlib
import numpy as np
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1232_codex_r031_verified_and_three_columns"


def test_Q_is_dense_so_rationality_reduces_nothing():
    """The retraction, as arithmetic: between ANY two reals there is a rational, so 'sigma is
    rational' excludes no interval. This is why B1229's 'robust core' was empty."""
    from fractions import Fraction as F
    for lo, hi in [(0.0, 1.0), (0.999, 1.001), (1/3 - 1e-9, 1/3 + 1e-9)]:
        mid = F((lo + hi) / 2).limit_denominator(10**12)
        assert lo < float(mid) < hi, (lo, hi, mid)


def test_the_quotient_lemma_and_its_bite():
    """dim (C,V,T) = (3,4,1). Y annihilating C => the observable is constant across the whole
    splitting family; a generic Y => it is not. Both directions, or the lemma says nothing."""
    rng = np.random.default_rng(20260901)
    dC, dV, dT = 3, 4, 1
    assert dC + dT == dV

    def obs(Y, t):
        s = np.zeros((dV, dT)); s[dC, 0] = 1.0; s[:dC, 0] = t
        return float((Y @ s).ravel()[0])

    Y_ann = np.zeros((1, dV)); Y_ann[0, dC] = 0.7
    vals = [obs(Y_ann, rng.normal(size=dC)) for _ in range(500)]
    assert max(vals) - min(vals) < 1e-12, "annihilating Y must give a CONSTANT observable"

    Y_gen = rng.normal(size=(1, dV))
    vals2 = [obs(Y_gen, rng.normal(size=dC)) for _ in range(500)]
    assert max(vals2) - min(vals2) > 1e-6, "generic Y must SEE the choice -- else no bite"


def test_trace_field_galois_is_order_two_not_three():
    """I-7's factual error: Q(sqrt-3) = Q(zeta_3) is QUADRATIC -- Gal has order 2, not 3."""
    import sympy as sp
    x = sp.symbols("x")
    assert sp.degree(sp.minimal_polynomial(sp.sqrt(-3), x), x) == 2
    assert sp.degree(sp.minimal_polynomial(sp.Rational(-1, 2) + sp.sqrt(-3)/2, x), x) == 2


def test_the_retractions_are_recorded_not_softened():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    c = v["claim_one_line"]
    assert "RETRACTION 1" in c and "Q IS DENSE IN R" in c
    assert "RETRACTION 2" in c and "DEFAULT-VALUE INFERENCE FROM ABSENCE" in c
    assert "RETRACTION 3" in c
    assert "NOT VERIFIED HERE" in c          # the fence on codex's running computation


def test_codex_certs_were_rerun_not_cited():
    out = (ARC / "codex_certs_rerun.txt").read_text(encoding="utf-8")
    assert "R031A B_0 character/base-field retrieval: PASS" in out
    assert "R031B RCFT consistency-scope controls: PASS" in out
    assert "K-rank: 4, not 1" in out          # the result that refuted my Outcome B
