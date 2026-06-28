"""B263 locks -- Rung 1b: the CS structure of T[4_1] from the Neumann-Zagier symplectic frame. The NZ data is a
valid Lagrangian (A B^T symmetric) and the CS quadratic form A^{-1}B = [[0,-1],[-1,0]] (U(1) bare level 0 + unit BF
coupling to the meridian flavor). FIREWALLED (3d-3d, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B263_t41_cs_levels" / "t41_cs_levels.py"
_spec = importlib.util.spec_from_file_location("b263", _PATH)
b263 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b263)


def test_rect_to_nz_change_of_basis():
    # A = a+b, B = b, nu = (c + sum b) mod 2
    assert b263.EDGE == ([1, 1], [-1, -1], 1)
    assert b263.MERIDIAN == ([1, 0], [0, -1], 0)
    assert b263.LONGITUDE == ([0, 2], [0, -2], 1)


def test_nz_symplectic_property():
    assert b263.nz_symplectic_ok()                      # A B^T symmetric -> valid Lagrangian


def test_cs_quadratic_form():
    CS = b263.cs_quadratic_form()
    assert CS == CS.T                                   # CS matrix must be symmetric
    assert CS == sp.Matrix([[0, -1], [-1, 0]])          # k_uu=0, k_um=-1 (unit BF), k_mm=0
