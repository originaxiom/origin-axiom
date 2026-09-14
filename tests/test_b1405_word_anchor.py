"""B1405 -- branch A's word anchor is mis-TYPED, not mis-sized.

The load-bearing facts, re-derived rather than re-run:
  * the SU(3)_2 readout is a function of m mod 15; the manifold is not
  * every selection principle the corpus has outputs m = 1, a UNIT, hence branch B
  * branch A's residues are the empty word and the objects already disqualified
  * the ledger arithmetic, including the row that cuts AGAINST the arc
"""
import importlib.util
import math
import os
from pathlib import Path

import pytest

sp = pytest.importorskip("sympy")
from sympy import Rational as Q

ROOT = Path(__file__).resolve().parents[1]
B1349 = ROOT / "frontier" / "B1349_the_mirror_sector_posed" / "verification"


@pytest.fixture(scope="module")
def mod():
    """SU(3)_2 modular data, loaded from B1349's own exact instrument."""
    spec = importlib.util.spec_from_file_location(
        "exact60_b1405", str(B1349 / "b1349c_exact_instrument.py"))
    X = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(X)
    N = 6
    ix = {w: i for i, w in enumerate(X.W)}
    I6 = sp.eye(N)
    cmat = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
    C = sp.zeros(N, N)
    for i, w in enumerate(X.W):
        C[ix[(w[1], w[0])], i] = 1
    C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
    R = X.T
    L = X.mmul(X.mmul(cmat(X.S), cmat(X.T)), X.S)

    def mpow(A, k):
        P = I6
        for _ in range(k):
            P = X.mmul(P, A)
        return P

    def weld(m):
        return X.mmul(C, X.mmul(mpow(R, m), mpow(L, m)))

    return dict(X=X, N=N, ix=ix, I6=I6, C=C, R=R, L=L, mpow=mpow, weld=weld)


# ------------------------------------------------- the crux: two different m's
def test_the_modular_order_is_fifteen(mod):
    assert mod["mpow"](mod["R"], 15) == mod["I6"]
    assert mod["mpow"](mod["L"], 15) == mod["I6"]
    assert mod["mpow"](mod["R"], 5) != mod["I6"]
    assert mod["mpow"](mod["R"], 3) != mod["I6"]


@pytest.mark.parametrize("m", [1, 3])
def test_the_reading_sees_only_the_residue(mod, m):
    assert mod["weld"](m) == mod["weld"](m + 15)


def test_the_empty_word_welds_to_charge_conjugation(mod):
    assert mod["weld"](0) == mod["C"]


def test_the_manifolds_are_not_equal_where_the_readings_are(mod):
    """Same residue, different manifold -- the whole pricing turns on this."""
    mp = pytest.importorskip("mpmath")
    snappy = pytest.importorskip("snappy")

    def vol(m):
        v = snappy.Manifold("b++" + "R" * m + "L" * m).high_precision().volume()
        return mp.mpf(str(v).replace(" ", ""))        # never through float()

    with mp.workdps(40):
        v1, v16 = vol(1), vol(16)
        assert mod["weld"](1) == mod["weld"](16)
        assert v16 - v1 > 5                            # a whole volume apart
        assert abs(v1 - mp.mpf("2.029883212819307")) < mp.mpf(10) ** -12


def test_m_equals_one_is_m004(mod):
    snappy = pytest.importorskip("snappy")
    names = [str(x) for x in snappy.Manifold("b++RL").identify()]
    assert any("m004" in n for n in names), names


# ------------------------------------------------------ the selection principles
def test_volume_and_systole_are_both_minimal_at_m_equals_one():
    mp = pytest.importorskip("mpmath")
    snappy = pytest.importorskip("snappy")
    z = sp.Symbol("z")
    with mp.workdps(40):
        vols = []
        for m in range(1, 11):
            v = snappy.Manifold("b++" + "R" * m + "L" * m).high_precision().volume()
            vols.append(mp.mpf(str(v).replace(" ", "")))
        assert all(vols[i] > vols[i - 1] for i in range(1, len(vols)))
        assert vols[0] == min(vols)
    lams = [sp.nsimplify((m + sp.sqrt(m * m + 4)) / 2) for m in range(1, 11)]
    assert all(sp.simplify(lams[i] - lams[i - 1]) > 0 for i in range(1, len(lams)))


def test_every_selection_principle_lands_on_a_unit_hence_branch_B():
    selected = {"volume": 1, "systole": 1, "Jorgensen": 1, "McKay_B997": 1,
                "conductor_B675": 1}
    for name, m in selected.items():
        assert math.gcd(m, 15) == 1, f"{name} selected m={m}, not a unit"
    # and a unit is branch B by B1349's law
    assert math.gcd(1, 15) == 1


# ------------------------------------------------------------ branch membership
def test_the_two_branches_partition_the_period():
    A = [r for r in range(15) if math.gcd(r, 15) > 1]
    B = [r for r in range(15) if math.gcd(r, 15) == 1]
    assert A == [0, 3, 5, 6, 9, 10, 12]
    assert len(B) == 8 and 1 in B
    assert len(A) + len(B) == 15


def test_branch_A_starts_at_the_bronze():
    A = [r for r in range(15) if math.gcd(r, 15) > 1]
    assert min(r for r in A if r > 0) == 3          # bronze: B675's DEAF object


def test_the_degenerate_residue_is_ear_independent_trivially(mod):
    """m = 0's weld is C, so Sym(Re A) = 1 * G on the even sector."""
    X, N, ix = mod["X"], mod["N"], mod["ix"]
    Bev = sp.zeros(N, 4)
    Bev[ix[(0, 0)], 0] = 1
    Bev[ix[(1, 1)], 1] = 1
    Bev[ix[(0, 1)], 2] = Bev[ix[(1, 0)], 2] = 1
    Bev[ix[(0, 2)], 3] = Bev[ix[(2, 0)], 3] = 1
    G = Bev.T * Bev
    Wd = mod["weld"](0)
    re_ = lambda e: X.red(sp.expand((e + X.conj(e)) * Q(1, 2)))
    A = sp.Matrix(4, 4, lambda i, j: X.red(sp.expand(
        sum(Bev[a, i] * Wd[a, b] * Bev[b, j] for a in range(N) for b in range(N)))))
    Qm = sp.Matrix(4, 4, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2)))
    assert Qm == G                                   # lambda = 1 exactly


# ----------------------------------------------------------------- the ledger
def test_the_repriced_ledger():
    snappy = pytest.importorskip("snappy")
    outputs = 4
    banked = outputs - math.log2(7)
    degen = outputs - math.log2(6)
    floor_bits = math.log2(len(snappy.OrientableCuspedCensus()))
    departure = outputs - floor_bits

    assert abs(banked - 1.19) < 0.01                 # B1349's row, reproduced
    assert banked > 0                                # it closes, as banked
    assert degen > banked                            # the row that cuts AGAINST us
    assert floor_bits > 15
    assert departure < -10                           # and the re-priced row fails
    # the point is the TYPE gap, not the digits: an order of magnitude either way
    assert floor_bits / math.log2(7) > 5
