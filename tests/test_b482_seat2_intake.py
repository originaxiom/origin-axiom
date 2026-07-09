"""B482 — seat-2 twisted-Markov intake: recompute the verified math + lock verdicts.

Recompute tier: B3 (the unified symmetric-pair commutator identity, symbolic), A6
(the indefinite-Hurwitz solution (1, d, d^2+1) of z^2 - x^2 - y^2 = d*xyz, symbolic
— note verify_seat2.py's printed A6 expression drops the x*y factor of xyz and is
nonzero; the FINDINGS claim, locked here, is the actual equation), and the A2
two-teeth negative-Pell spot-check (golden D=5 solvable, silver via the content-2
reduced discriminant 8, Markov m = 5, 13, 29 fail).

Doc-integrity tier (not a recompute): the intake verdict lines — A2's novelty is
UNVERIFIED pending lit-gate (W0 result: essentially KNOWN), and seat-2's B1 "banked
error" claim is a DISCREPANCY (their 2.1775291199 is not the repo's banked
1.57705744122666946), NOT applied.
"""
import math
import pathlib

import sympy as sp

_DIR = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B482_seat2_twisted_markov_intake"
FINDINGS = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
W0 = (_DIR / "W0_LITGATE_RESULTS.md").read_text(encoding="utf-8")


def test_b3_unified_symmetric_pair_commutator():
    """tr[A,B] = 2 - gap^2/(det A det B) for symmetric A, B of ANY determinant
    (gap = M12 - M21, M = AB) — the generalization of P4 Lemma 2.2, symbolically."""
    a, b, c, e, f, g = sp.symbols("a b c e f g")
    A = sp.Matrix([[a, b], [b, c]])
    B = sp.Matrix([[e, f], [f, g]])
    M = A * B
    gap = M[0, 1] - M[1, 0]
    lhs = sp.trace(A * B * A.inv() * B.inv())
    assert sp.simplify(lhs - (2 - gap**2 / (A.det() * B.det()))) == 0


def test_a6_indefinite_hurwitz_identity():
    """(1, d, d^2+1) solves z^2 - x^2 - y^2 = d*xyz for every d (exact). This is the
    FINDINGS statement; the probe's own A6 print line omitted the x*y = d factor."""
    d = sp.symbols("d")
    x, y, z = sp.Integer(1), d, d**2 + 1
    assert sp.expand(z**2 - x**2 - y**2 - d * x * y * z) == 0


def _negpell_minus4(D, tmax=2000):
    """Smallest (v, t) with v^2 - D t^2 = -4, or None within the bound (the probe's
    filter)."""
    for t in range(1, tmax):
        v2 = D * t * t - 4
        if v2 >= 0 and math.isqrt(v2) ** 2 == v2:
            return (math.isqrt(v2), t)
    return None


def test_a2_two_teeth_negative_pell_filter():
    """The spot-verify: D_m = 9m^2-4. Golden m=1 (D=5) passes: (1,1). Silver m=2
    passes on the content-2 branch (reduced discriminant 32/4 = 8: (2,1), the 2*sqrt2
    tooth); the naive D=32 filter fails as the probe records. Markov m = 5, 13, 29
    give no -4 solution (unit norm +1) — only the golden and silver teeth below 3."""
    assert _negpell_minus4(9 * 1 - 4) == (1, 1)          # m=1, D=5
    assert _negpell_minus4(9 * 4 - 4) is None            # m=2 naive D=32: no
    assert _negpell_minus4(8) == (2, 1)                  # content-2 branch: disc 8
    for m in (5, 13, 29):
        assert _negpell_minus4(9 * m * m - 4) is None, m


def test_intake_verdicts_locked():
    """Documentation-integrity lock (not a recompute): the load-bearing verdict
    lines of the intake — verified-but-novelty-blocked A2, and the B1 flag."""
    assert "Markov spectrum ∩ (0,3) = {√5, 2√2}" in FINDINGS
    assert "Novelty UNVERIFIED — lit-gate" in FINDINGS
    assert "DISCREPANCY, not applied" in FINDINGS
    assert "2.1775291199" in FINDINGS                      # seat-2's number
    assert "1.57705744122666946" in FINDINGS               # the repo's banked number
    assert "do NOT overwrite the banked value" in FINDINGS


def test_w0_litgate_verdict_locked():
    """Documentation-integrity lock: the W0 gate outcome that blocks novelty."""
    assert "the twisted-Markov spinoff is essentially KNOWN" in W0
    assert "A2 (Two-Teeth) — PARTIALLY-KNOWN" in W0
