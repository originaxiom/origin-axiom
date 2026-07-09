"""Locks for B489 (the self-interaction tower = cyclic cover tower of 4_1).

Recomputes the verified arithmetic: torsion law |H1 tor| = |det(A1^n - I)| = |2 - L(2n)|
(exact 2x2 integer identity + Lucas), the odd/even split L(2n) = L(n)^2 - 2(-1)^n, and —
SnapPy-guarded — the tower table (volume = n*vol(4_1), homology torsion, DGG rank 2n-1,
rectangular cusps, n=2 = m206 = THE degree-2 cover) and the 4c refutation
(m206(3,1) is closed with vol 2.568971 = m160(1,2), not the cusped 5_2 at 2.828122).
The firewall/no-bank verdicts are locked as FINDINGS lines.
"""
import pathlib

import pytest

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B489_self_interaction_tower" / "FINDINGS.md").read_text(encoding="utf-8")


def _matpow(M, n):
    R = ((1, 0), (0, 1))
    for _ in range(n):
        R = tuple(tuple(sum(R[i][k] * M[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return R


def _lucas(k):
    a, b = 2, 1          # L0, L1
    for _ in range(k):
        a, b = b, a + b
    return a


A1 = ((2, 1), (1, 1))


def test_torsion_law_exact():
    # |det(A1^n - I)| = |2 - tr(A1^n)| (det=1 identity) and tr(A1^n) = L(2n)
    for n in range(1, 11):
        P = _matpow(A1, n)
        tr = P[0][0] + P[1][1]
        det_minus_I = (P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0]
        assert det_minus_I == 2 - tr, n
        assert tr == _lucas(2 * n), n
    # the banked table rows
    assert {n: _matpow(A1, n)[0][0] + _matpow(A1, n)[1][1] for n in (1, 2, 3, 4, 5, 8)} == \
        {1: 3, 2: 7, 3: 18, 4: 47, 5: 123, 8: 2207}
    assert {n: abs(2 - _lucas(2 * n)) for n in (1, 2, 3, 4, 5, 8)} == \
        {1: 1, 2: 5, 3: 16, 4: 45, 5: 121, 8: 2205}


def test_odd_even_split():
    for n in range(1, 11):
        assert _lucas(2 * n) == _lucas(n)**2 - 2 * (-1)**n, n
        tor = abs(2 - _lucas(2 * n))
        if n % 2 == 1:
            assert tor == _lucas(n)**2, n                       # 1, 16, 121, 841, ...
        else:
            assert tor == (_lucas(n) - 2) * (_lucas(n) + 2), n  # 5, 45, 320, 2205, ...
            assert tor % 5 == 0, n                              # always divisible by 5


def _torsion_order(M):
    prod = 1
    for part in str(M.homology()).split(" + "):
        if part.startswith("Z/"):
            prod *= int(part[2:])
    return prod


def test_tower_table_snappy():
    snappy = pytest.importorskip("snappy")
    v4 = float(snappy.Manifold('4_1').volume())
    for n in range(1, 6):
        M = snappy.Manifold('b++' + 'RL' * n)
        assert abs(float(M.volume()) - n * v4) < 1e-9, n            # vol = n * vol(4_1)
        assert M.num_tetrahedra() - M.num_cusps() == 2 * n - 1      # DGG abelian U(1)^{2n-1}
        assert _torsion_order(M) == abs(2 - _lucas(2 * n)), n       # Fox-Weber live
        assert abs(complex(M.cusp_info(0).modulus).real) < 1e-9     # rectangular, whole tower
    assert str(snappy.Manifold('b++RLRL').homology()) == "Z/5 + Z"
    assert str(snappy.Manifold('b++RLRLRL').homology()) == "Z/4 + Z/4 + Z"
    assert str(snappy.Manifold('b++RLRLRLRL').homology()) == "Z/3 + Z/15 + Z"


def test_n2_is_the_unique_degree2_cover_snappy():
    snappy = pytest.importorskip("snappy")
    covers = snappy.Manifold('4_1').covers(2)
    assert len(covers) == 1
    m206 = snappy.Manifold('m206')
    assert covers[0].is_isometric_to(m206)
    assert snappy.Manifold('b++RLRL').is_isometric_to(m206)


def test_4c_refutation_snappy():
    # m206(3,1) is CLOSED with vol 2.568971 (= m160(1,2)); 5_2 is CUSPED with vol 2.828122
    snappy = pytest.importorskip("snappy")
    F = snappy.Manifold('m206')
    F.dehn_fill((3, 1))
    v = float(F.volume())
    assert abs(v - 2.568971) < 1e-5
    G = snappy.Manifold('m160')
    G.dehn_fill((1, 2))
    assert abs(v - float(G.volume())) < 1e-9
    assert abs(v - float(snappy.Manifold('5_2').volume())) > 0.25   # not the 5_2 complement


def test_verdict_lines():
    assert "**4c REFUTED (wrong volume):**" in _FIND
    assert "**DGG is abelian at every level.**" in _FIND
    assert "LARGELY NUMEROLOGY" in _FIND                # the section 3 adjudication
    norm = " ".join(_FIND.split())
    assert "Nothing to CLAIMS.md." in norm
    assert "banked as **mathematics**" in norm
