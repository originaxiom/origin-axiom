"""B1409 -- the tower's parameter budget: dim H^1 = k(n-1), and all of it is boundary.

Recomputed, not re-read. Covers are selected BY PROPERTY, never by list index (E75).
Exact over Q(zeta_12) via B1333's engine; no tolerance anywhere.
"""
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
B1333 = ROOT / "frontier" / "B1333_the_index_on_several_cusps" / "verification"

snappy = pytest.importorskip("snappy")
sys.path.insert(0, str(B1333))
exact_rho = pytest.importorskip("recogmc").exact_rho
_fi = pytest.importorskip("fi_lib")
sym, blockdiag = _fi.sym, _fi.blockdiag
analyse_exact = pytest.importorskip("mcexact").analyse_exact
mp = pytest.importorskip("mpmath")

# E75 #6-#8, live: mp.pslq does `tol = to_fixed(tol, prec)` and asserts it non-zero, so a
# low AMBIENT precision silently turns a 1e-35 tolerance into 0 and the recognition dies
# inside mpmath. B1333's modules set mp.dps at import time and depend on the order they are
# imported in; under pytest that order differs. Global numeric state is not a contract --
# set it explicitly here and re-assert it before every recognition.
DPS = 60
mp.mp.dps = DPS


def _chiral_multicusped(degree=10):
    """Select by PROPERTY: multi-cusped and not amphichiral. Never by index."""
    out = {}
    for i, C in enumerate(snappy.Manifold("m004").covers(degree)):
        k = C.num_cusps()
        if k < 2:
            continue
        try:
            if C.symmetry_group().is_amphicheiral():
                continue
        except Exception:
            continue
        out.setdefault(k, []).append((i, C))
    return out


def _dims(C):
    """(a0, dim H^1(sl2), dim H^1(sl3), r1, n) exactly, or None if PSLQ halts."""
    mp.mp.dps = DPS                      # re-assert: another import may have lowered it
    got = exact_rho(C)
    if got is None:
        return None
    _, _, gens, rels, per, rho = got
    A2 = analyse_exact(gens, rels, per, {g: sym(rho[g], 2) for g in gens}, 3)
    V8 = {g: blockdiag([sym(rho[g], 2), sym(rho[g], 4)]) for g in gens}
    A8 = analyse_exact(gens, rels, per, V8, 8)
    return A2["a0"], A2["a1"], A8["a1"], A8["r1"], A8["n"]


@pytest.fixture(scope="module")
def tower():
    return _chiral_multicusped(10)


def test_guard_the_recognition_survives_a_lowered_ambient_precision():
    """The failure this file actually hit, locked as a PROPERTY not a value.

    mp.pslq does `tol = to_fixed(tol, prec)` and asserts it non-zero, so a low ambient
    mp.mp.dps kills the recognition inside mpmath rather than in any mathematics. The first
    version of this guard asserted `mp.mp.dps >= 50` -- i.e. it asserted the ambient VALUE
    -- and failed, because another test had already lowered it. That is the lesson twice
    over: global numeric state is not a contract, so the guard must test that `_dims`
    RE-ASSERTS the precision, not that someone else left it alone. E75 #6-#8.
    """
    mp.mp.dps = 15                                  # deliberately too low for the pslq call
    d = _dims(snappy.Manifold("m004"))
    assert d is not None, "the recognition did not survive a lowered ambient precision"
    assert (d[0], d[1], d[2], d[4]) == (0, 1, 2, 0)
    assert mp.mp.dps == DPS                         # _dims restored it


def test_the_positive_control_m004_returns_k_equals_one():
    """If this fails the instrument is wrong and every dimension below is void."""
    d = _dims(snappy.Manifold("m004"))
    assert d is not None, "PSLQ halted on m004 -- no float fallback permitted"
    a0, sl2, sl3, r1, n = d
    assert a0 == 0
    assert sl2 == 1            # k = 1, Thurston
    assert sl3 == 2            # k(n-1) = 2
    assert n == 0


def test_the_ceiling_is_five_cusps_and_two_chiral_covers_reach_it(tower):
    assert max(tower) == 5
    assert len(tower[5]) == 2


def test_the_two_five_cusped_chiral_covers_are_the_same_manifold(tower):
    (_, A), (_, B) = tower[5]
    assert bool(A.is_isometric_to(B))
    assert A.num_cusps() == B.num_cusps() == 5
    assert A.num_tetrahedra() == 20


@pytest.mark.parametrize("k", [2, 3, 4, 5])
def test_dim_H1_tracks_k_in_both_parameters(tower, k):
    """The control that matters: the thing that can break (k) is the thing that varies."""
    for _, C in tower[k][:2]:
        d = _dims(C)
        assert d is not None
        a0, sl2, sl3, r1, n = d
        assert a0 == 0                 # irreducible
        assert sl2 == k                # Thurston
        assert sl3 == 2 * k            # Menal-Ferrer-Porti, k(n-1)
        assert r1 == sl3               # image is all of H^1
        assert n == 0                  # restriction to the boundary is INJECTIVE


def test_every_parameter_is_boundary_data(tower):
    """n = a1 - r1 = 0 everywhere: zero interior moduli anywhere in the tower."""
    for k in sorted(tower):
        for _, C in tower[k][:1]:
            d = _dims(C)
            assert d is not None
            assert d[4] == 0, f"k={k}: a nonzero interior modulus appeared"


def test_the_amphichiral_five_cusped_control_gives_the_same_numbers():
    """The dimension is chirality-blind -- the fence stated in the sealed prereg."""
    amph = [C for C in snappy.Manifold("m004").covers(10)
            if C.num_cusps() == 5 and C.symmetry_group().is_amphicheiral()]
    assert len(amph) == 1
    d = _dims(amph[0])
    assert d is not None
    a0, sl2, sl3, r1, n = d
    assert (a0, sl2, sl3, n) == (0, 5, 10, 0)


def test_half_lives_half_dies(tower):
    """dim H^1(dM) = 2 dim H^1(M): the image is Lagrangian, so the map loses nothing."""
    for _, C in tower[5][:1]:
        mp.mp.dps = DPS
        got = exact_rho(C)
        assert got is not None
        _, _, gens, rels, per, rho = got
        for m in (2, 4):
            A = analyse_exact(gens, rels, per, {g: sym(rho[g], m) for g in gens}, m + 1)
            assert A["t1"] == 2 * A["a1"]
            assert A["r1"] == A["a1"]
