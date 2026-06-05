"""B94 §1b -- locking test (computer-assisted, n=2): the ACTUAL SL(2) trace-map Jacobian of a genuine
non-square monodromy [[3,2],[1,1]] (and the metallic/square controls) factors as char(Sym^2 N), with the
parity marker (s - det N) -- confirming catalog appearance at the actual-Jacobian level for a non-square."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b94_sl2", _ROOT / "frontier" / "B94_tower_universality" / "sl2_nonsquare_check.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_sl2_jacobian_equals_sym2_for_all_cases():
    """For metallic, square, and the genuine NON-square [[3,2],[1,1]]: charpoly_at_triv(T) == char(Sym^2 N)."""
    for name, (T, N) in B.CASES.items():
        assert sp.simplify(B.charpoly_at_triv(T) - B.sym2(N)) == 0, name


def test_parity_marker_is_s_minus_det():
    """The parity marker (s - det N): (s+1) iff det N = -1 (metallic), (s-1) iff det N = +1 (square /
    non-square)."""
    s = B.s
    metallic = B.charpoly_at_triv(B.CASES["metallic [[1,1],[1,0]] det -1"][0])
    nonsquare = B.charpoly_at_triv(B.CASES["NONsquare[[3,2],[1,1]] det +1"][0])
    assert sp.rem(sp.Poly(metallic, s), sp.Poly(s + 1, s)).as_expr() == 0          # det=-1 -> (s+1)
    assert sp.rem(sp.Poly(nonsquare, s), sp.Poly(s + 1, s)).as_expr() != 0         # det=+1 -> no (s+1)
    assert sp.rem(sp.Poly(nonsquare, s), sp.Poly(s - 1, s)).as_expr() == 0         # det=+1 -> (s-1)
