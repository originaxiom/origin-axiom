"""B94 (Paper 0, Phase G1) -- the tower's universality: catalog universal, parity det=-1-specific.

THE QUESTION (handoff G1): does the metallic trace-map tower char(J) = prod char(+-M^k) survive when we
leave the metallic slice -- i.e. for a NON-metallic monodromy (det=+1, CF period >= 2)?

THE METHOD (rigorous -- reuses the PROVED metallic Jacobian, no new substitution needed). The trace map
of phi^2 is the composition T o T, so at a fixed point its Jacobian is J(phi^2) = J(phi)^2. The square of
the metallic substitution phi_m has abelianization M_m^2, which has det = +1 -- a non-metallic monodromy.
So J^2 IS the fixed-line Jacobian of a det=+1 monodromy, obtained exactly by squaring the proved metallic
J. Factoring char(J^2) and comparing to the catalog char(N^k), N = M_m^2, is the decisive G1 test.

THE RESULT (computer-assisted, exact at SL(3) and SL(4), m=1 baseline N=[[2,1],[1,1]]):
  * SL(3): char(J)   = (t-1)(t+1) char(M^-1) char(M^2) char(M^3)        [metallic, det=-1: WITH parity]
           char(J^2) = (t-1)^2 char(N^1) char(N^2) char(N^3)            [N=M^2, det=+1: catalog only]
  * SL(4): char(J^2) = (t-1)^3 char(N^1) char(N^2) char(N^3)^2 char(N^4) [det=+1: catalog only]
In every case char(J^2) factors EXACTLY over the catalog char(N^k) (N's characteristic polynomials), with
det(N)^k = +1, and EVERY sign sector char(-N^k) AND the (t+1) factor are ABSENT.

THE CONCLUSION -- "universal catalog, det=-1 parity":
  * The Dickson CATALOG prod char(N^k) is UNIVERSAL across GL(2,Z): char(N^k) is just the characteristic
    polynomial of N^k (Cayley-Hamilton), defined for any monodromy; the trace-map Jacobian factors over it.
  * The PARITY / sign sectors char(-N^k) (and the (t+1) Cartan-parity factor) are det = -1-SPECIFIC: they
    are the negative-small-eigenvalue (-1/lambda) sectors (B93/MyCalc-1), and squaring to det=+1 removes
    every one of them. So the tower's two-sheeted (CPT) structure is a metallic (det=-1) phenomenon, not a
    general GL(2,Z) one. This makes the foundational det=-1 condition (B92) STRUCTURALLY DISTINGUISHED.

G3 note (degree=rank diverges from the tower on det-sign). The figure-eight bundle of B73/B89 has
monodromy [[2,1],[1,1]] (det = +1), and degree=rank M^n=L is PROVED there (B89/V72). So degree=rank is
det-AGNOSTIC -- a peripheral/cusp property (B77/V75) -- UNLIKE the tower's parity, which is det=-1-specific.
The tower and degree=rank give DIFFERENT answers to "universal?", confirming they are two problems.

Standalone trace-map / Lie theory; no physics, no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]
t, m = sp.symbols("t m")


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def char_Nk(N, k, sign=1):
    """char(sign*N^k) = t^2 - sign*tr(N^k) t + det(N)^k -- the catalog for ANY 2x2 N."""
    N = sp.Matrix(N)
    Nk = N**k if k >= 0 else N.inv() ** (-k)
    return sp.expand(t**2 - sign * sp.trace(Nk) * t + sp.det(N) ** k)


def _sl3_jacobian_m1():
    b54 = _load("b54", "frontier/B54_general_c_exchange_structure/probe.py")
    return b54.symbolic_jacobian(1, 3)            # SL(3), metallic m=1, fixed line c=3


def _sl4_jacobian_m1():
    b65 = _load("b65", "frontier/B65_sl4_symbolic_jacobian/probe.py")
    return b65.symbolic_jacobian().subs(m, 1)     # SL(4), metallic m=1


def universality(J, ks):
    """Factor char(J) (metallic, det=-1) and char(J^2) (N=M^2, det=+1); report which catalog factors
    divide char(J^2), and whether any sign sector char(-N^k) survives. Returns dict."""
    charJ = sp.factor(J.charpoly(t).as_expr())
    J2 = sp.expand(J * J)
    charJ2 = sp.factor(J2.charpoly(t).as_expr())
    N = [[2, 1], [1, 1]]                           # M_1^2, det = +1
    catalog = [k for k in ks if sp.div(sp.Poly(charJ2, t), sp.Poly(char_Nk(N, k), t))[1].as_expr() == 0]
    sign_sectors = [k for k in ks if sp.div(sp.Poly(charJ2, t), sp.Poly(char_Nk(N, k, -1), t))[1].as_expr() == 0]
    tplus1 = sp.div(sp.Poly(charJ2, t), sp.Poly(t + 1, t))[1].as_expr() == 0
    return {"charJ": charJ, "charJ2": charJ2, "catalog_k": catalog,
            "sign_sectors_k": sign_sectors, "tplus1_present": tplus1}


def degree_rank_is_det_agnostic():
    """The figure-eight bundle (B73/B89) has monodromy [[2,1],[1,1]] (det=+1) and M^n=L holds (B89).
    So degree=rank is det-agnostic. Returns (figure_eight_monodromy, det)."""
    N = sp.Matrix([[2, 1], [1, 1]])               # the figure-eight once-punctured-torus monodromy
    return N.tolist(), int(N.det())


def main():
    print("B94 (Paper 0, G1) -- tower universality: catalog universal, parity det=-1-specific\n")
    for rank, J in (("SL(3)", _sl3_jacobian_m1()), ("SL(4)", _sl4_jacobian_m1())):
        r = universality(J, ks=(1, 2, 3, 4))
        print(f"{rank}:")
        print(f"  metallic (det=-1)  char(J)   = {r['charJ']}")
        print(f"  squared  (det=+1)  char(J^2) = {r['charJ2']}")
        print(f"     catalog char(N^k) dividing char(J^2): k={r['catalog_k']}  (universal)")
        print(f"     sign sectors char(-N^k) present: k={r['sign_sectors_k'] or 'NONE'};  "
              f"(t+1) present: {r['tplus1_present']}   (parity det=-1-specific -> gone)")
    fe, det = degree_rank_is_det_agnostic()
    print(f"\nG3 note: the figure-eight bundle monodromy is {fe} (det={det:+d}); M^n=L PROVED there (B89).")
    print("  => degree=rank is det-AGNOSTIC (peripheral), UNLIKE the tower's det=-1-specific parity.")
    print("     The tower and degree=rank answer 'universal?' differently -> two problems, not one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
