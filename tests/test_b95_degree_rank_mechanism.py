"""B95 (Task M) -- locking tests: the principal degree=rank spectrum is forced (n=3,4,5 explicit; n>=6
impossible), and the n=5 forced spectrum {1,1,1,-1,-1} degenerates (A^2=I -> dihedral -> reducible)."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b95", _ROOT / "frontier" / "B95_degree_rank_mechanism" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_forced_principal_spectrum():
    """tr A = tr A^-1 = 1 with eigenvalue 1 at mult n-2 forces the two extra eigenvalues: n=3 {1,i,-i},
    n=4 {1,1,w,w2}, n=5 {1,1,1,-1,-1}; n>=6 is impossible (a root-of-unity 2cos=3-n needs |cos|<=1)."""
    spec3, rou3, s3 = B.forced_principal_spectrum(3)
    assert rou3 and s3 == 0 and len(spec3) == 3
    spec5, rou5, s5 = B.forced_principal_spectrum(5)
    assert rou5 and s5 == -2 and len(spec5) == 5
    assert sorted([sp.simplify(x) for x in spec5], key=str) == sorted(
        [sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(-1), sp.Integer(-1)], key=str)
    spec6, rou6, s6 = B.forced_principal_spectrum(6)
    assert spec6 is None and rou6 is False         # n=6: 2cos = -3, impossible


def test_n5_principal_degenerates_to_reducible():
    """At n=5 the forced spectrum has A^2=I, forcing B=tAt^-1 (involution); <A,B> dihedral -> reducible
    (algebra-span rank << 25). So no irreducible principal Dehn-filling rep at SL(5)."""
    a2, ranks = B.n5_principal_is_reducible()
    assert a2 is True                              # A^2 = I
    assert all(r < 25 for r in ranks)              # reducible (dihedral): span never reaches 25
    assert all(r <= 12 for r in ranks)             # in fact ~8, far below irreducible
