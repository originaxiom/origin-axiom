"""B481 — det(T) = zeta5 is FLOAT (the eighth kill): exact recompute + verdict lock.

Recompute tier: reading 2 in full (wrt_tmatrix.py — the SU(2)_k modular T-matrix
determinant as an exact rational phase, k = 3 and 13; zeta5 appears as the twist
EIGENVALUE theta_2 = zeta5^2, never as det), the reading-1 determinants that are
recomputable exactly without the F_p harness (det Par = -1 by permutation parity,
det D = zeta3 via the exponent C(15,3) = 5 mod 15, det F_15 = -i), and the
group-theoretic core of the kill (dets generate 12th roots of unity; 5 does not
divide 12, so zeta5 is FORBIDDEN in the det image, not merely unfound).

Doc-integrity tier (not a recompute): the F_p four-prime Weil table rows — their
reproducer det_kill.py is referenced by FINDINGS.md but not present in the bulletin
dir, so those rows are locked as documentation only — and the verdict line.
"""
import pathlib
from fractions import Fraction as Fr
from math import comb, gcd

import numpy as np

FINDINGS = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
            / "B481_det_zeta5_kill" / "FINDINGS.md").read_text(encoding="utf-8")

N = 15


def _tdet(k, framing=True):
    """Exact det phase of the SU(2)_k T-matrix (wrt_tmatrix.py)."""
    r = k + 2
    hs = [Fr(a * (a + 2), 4 * r) for a in range(k + 1)]
    c = Fr(3 * k, r)
    ph = sum(hs) - (Fr(k + 1) * c / 24 if framing else 0)
    return ph % 1


def test_wrt_tmatrix_dets_exact_and_never_zeta5():
    """k=3: det T = 1 (framed), zeta10^3 (theta-only); k=13 (r=15): zeta6 / zeta60^41.
    No phase is a primitive fifth root (denominator 5)."""
    vals = {(3, True): Fr(0), (3, False): Fr(3, 10),
            (13, True): Fr(1, 6), (13, False): Fr(41, 60)}
    for (k, fr), want in vals.items():
        got = _tdet(k, fr)
        assert got == want, (k, fr, got)
        assert got not in (Fr(1, 5), Fr(2, 5), Fr(3, 5), Fr(4, 5)), (k, fr)


def test_zeta5_survives_as_twist_eigenvalue_not_det():
    """At k=3 the spin-1 anyon has h_2 = 2/5 exactly, so theta_2 = zeta5^2 — a
    T-matrix EIGENVALUE of order 5; the det never carries 5-torsion."""
    h2 = Fr(2 * (2 + 2), 4 * (3 + 2))
    assert h2 == Fr(2, 5) and h2.denominator == 5
    # order of the twist e^{2 pi i h2} is exactly 5
    assert h2.denominator // gcd(h2.numerator, h2.denominator) == 5


def test_weil_dets_recomputed_exactly():
    """Reading-1 rows recomputable without the F_p harness: det Par = -1
    (j -> -j mod 15 is 7 transpositions), det D = zeta3 (exponent sum
    C(15,3) = 455 = 5 mod 15, so det D = zeta15^5 = zeta3; = zeta3^{cm} in general),
    det F_15 = -i = zeta4^3 (DFT kernel e^{-2 pi i jk/15}/sqrt(15))."""
    # Par: fixed point j=0, transpositions (j, 15-j) for j=1..7 -> sign (-1)^7
    n_transpositions = (N - 1) // 2
    assert (-1) ** n_transpositions == -1
    Par = np.zeros((N, N))
    for j in range(N):
        Par[(-j) % N, j] = 1
    assert abs(np.linalg.det(Par) - (-1)) < 1e-12
    # D = diag(zeta^{j(j-1)/2}): exponent sum = C(15,3) = 455 = 5 (mod 15)
    assert comb(N, 3) % N == 5
    z = np.exp(2j * np.pi / N)
    D = np.diag([z ** ((j * (j - 1) // 2) % N) for j in range(N)])
    assert abs(np.linalg.det(D) - np.exp(2j * np.pi / 3)) < 1e-12   # zeta3
    # F (unitary DFT, e^- convention): det = -i for N = 15
    F = np.exp(-2j * np.pi * np.outer(np.arange(N), np.arange(N)) / N) / np.sqrt(N)
    assert abs(np.linalg.det(F) - (-1j)) < 1e-9


def test_det_image_is_12_torsion_so_zeta5_is_forbidden():
    """The structural kill: the recorded dets {1, -1, zeta3, zeta3^2, -i} generate
    the group of 12th roots of unity (lcm of orders 1,2,3,4 = 12); since 5 does not
    divide 12 there is NO element of order 5 — zeta5 is forbidden, not unfound."""
    from math import lcm
    orders = (1, 2, 3, 4)   # 1, Par, D, F dets
    assert lcm(*orders) == 12
    assert 12 % 5 != 0
    # a cyclic group of order 12 has an element of order d iff d | 12
    assert all(12 % d == 0 for d in orders) and 5 not in [d for d in range(1, 13) if 12 % d == 0]


def test_findings_eighth_kill_verdict_locked():
    """Documentation-integrity lock (not a recompute): the F_p four-prime table rows
    (det_kill.py is not in the bulletin dir) and the banked verdict."""
    assert "| W₁, W₂, W₁W₂, [W₁,W₂] | **1** |" in FINDINGS
    assert "| Par, Par·W₁, Par·W₂, Par·W₁W₂ | **−1** |" in FINDINGS
    assert "lands in ⟨ζ₃, ζ₄, −1⟩ = the **12th roots of unity**" in FINDINGS
    assert "ζ₅ is NOT in the image" in FINDINGS
    assert "det(T) = ζ₅ is FLOAT — the eighth kill." in FINDINGS
