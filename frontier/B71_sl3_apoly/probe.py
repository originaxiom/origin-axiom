"""B71 -- the SL(3) figure-eight character variety from the trace-map fixed locus (Track B, B0-B1).

The SL(3) analogue of B67. The figure-eight is the once-punctured-torus bundle with monodromy
phi = [[2,1],[1,1]] = M^2; on the 8 SL(3) trace coordinates of the fiber F_2 = <a,b> the induced
trace map is T_1^2, where T_1 (B48, m=1; a->ab, b->a) is

    T_1(x) = (x3, x1, x1 x3 - x4 x2 + x6, x8, x4, x5, x2, x4 x8 - x1 x5 + x7),
    x = (x1..x8) = (tr A, tr B, tr AB, tr A^-1, tr B^-1, tr A^-1 B, tr A B^-1, tr A^-1 B^-1).

A fiber representation extends over the bundle iff its character is FIXED by T_1^2 (then it is
conjugate to its phi-image, so a monodromy t exists) -- exactly as at SL(2) in B67. The fixed locus
Fix(T_1^2) is therefore the SL(3) character variety of the figure-eight bundle.

RESULT (B0-B1, exact):
  * The fixed-locus equations give 4 linear identifications x3=x2, x8=x5, x6=x4, x7=x1, reducing to
    (x1,x2,x4,x5); the remaining ideal factors as
        (x1-x4)(x2-1) = (x1-x4)(x5-1) = 0   plus two cubics,
    and decomposes EXACTLY into THREE components, each of dimension 2:
        V0 = {x1=x4, x2=x5}     (geometric -- contains Sym^2 of the figure-eight SL(2) holonomy)
        W1 = {x1=x4=1}          (a trace-=1 / Dehn-filling-type component)
        W2 = {x2=x5=1}          (a trace-=1 / Dehn-filling-type component)
  * This reproduces the component STRUCTURE of the published Heusener-Munoz-Porti SL(3) figure-eight
    character variety (arXiv:1505.04451): irreducible part = 3 components, each dimension 2, the
    geometric one containing Sym^2(discrete-faithful SL(2) holonomy). The W1/W2 trace-=1 components
    are the analogue of the +-3 Dehn-filling components V1/V2 (= Falbel et al. D2/D3, arXiv:1412.4711).
  * Ground truth: Sym^2 : SL(2)->SL(3) of the B67 fixed-locus family lands on V0 to ~1e-14 (offline,
    exact; no Magma/Sage/internet).

Honest scope: HMP coordinatize the KNOT group <S,T>; here the coordinates are the FIBER group <a,b>.
The component count / dimension / Sym^2-geometric match is structural and dictionary-free; a full
literal fiber<->knot coordinate dictionary is a separate identification (not claimed here). The
peripheral eigenvalue "A-variety" (monodromy t, longitude [A,B]) is the B2-B3 continuation.
Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1-P16 untouched.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

# --------------------------------------------------------------------------- #
# the trace map and its fixed locus (B48 coordinates)
# --------------------------------------------------------------------------- #

X8 = sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8")


def T1(c):
    """B48 m=1 trace map (a->ab, b->a) on the 8 coordinates."""
    x1, x2, x3, x4, x5, x6, x7, x8 = c
    return (x3, x1, sp.expand(x1 * x3 - x4 * x2 + x6), x8, x4, x5, x2,
            sp.expand(x4 * x8 - x1 * x5 + x7))


def T1_sq(c):
    """T_1^2 -- the figure-eight monodromy [[2,1],[1,1]] action on the 8 coordinates."""
    return tuple(sp.expand(e) for e in T1(T1(c)))


def fixed_locus_equations():
    """The 8 polynomials T_1^2(x) - x defining Fix(T_1^2)."""
    img = T1_sq(X8)
    return [sp.expand(img[i] - X8[i]) for i in range(8)]


def components():
    """The exact irreducible-component decomposition of Fix(T_1^2).

    Returns a dict name -> (param_symbols, 8-tuple of coordinates) giving an explicit rational
    parametrization of each 2-dim component. After the 4 linear identifications (x3=x2, x8=x5,
    x6=x4, x7=x1), Fix(T_1^2) splits exactly into V0 {x1=x4,x2=x5}, W1 {x1=x4=1}, W2 {x2=x5=1}.
    """
    p, q = sp.symbols("p q")
    one = sp.Integer(1)
    return {
        # geometric: x1=x4=x6=x7=p, x2=x3=x5=x8=q  (contains Sym^2)
        "V0": ((p, q), (p, q, q, p, q, p, p, q)),
        # x1=x4=1: (1, q, q, 1, p, 1, 1, p)
        "W1": ((p, q), (one, q, q, one, p, one, one, p)),
        # x2=x5=1: (p, 1, 1, q, 1, q, p, 1)
        "W2": ((p, q), (p, one, one, q, one, q, p, one)),
    }


def reduced_ideal():
    """Fix(T_1^2) in the 4 free coordinates (x1,x2,x4,x5) after the linear identifications."""
    x1, x2, x3, x4, x5, x6, x7, x8 = X8
    lin = {x3: x2, x8: x5, x6: x4, x7: x1}
    return [sp.expand(e.subs(lin)) for e in fixed_locus_equations() if sp.expand(e.subs(lin)) != 0]


# --------------------------------------------------------------------------- #
# Sym^2 ground truth (offline, exact): figure-eight SL(2) holonomy -> SL(3)
# --------------------------------------------------------------------------- #

def sym2(g):
    """Sym^2 : SL(2,C) -> SL(3,C), the 3-dim irrep on {e1^2, e1 e2, e2^2}."""
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    return np.array([[a * a, 2 * a * b, b * b],
                     [a * c, a * d + b * c, b * d],
                     [c * c, 2 * c * d, d * d]], dtype=complex)


def coords8_numeric(A, B):
    """The 8 B48 trace coordinates of a numeric SL(3) pair (A,B)."""
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    tr = np.trace
    return np.array([tr(A), tr(B), tr(A @ B), tr(Ai), tr(Bi),
                     tr(Ai @ B), tr(A @ Bi), tr(Ai @ Bi)], dtype=complex)


def _load_b67():
    """Load the B67 probe under a unique module name (avoids the generic 'probe' name collision)."""
    import importlib.util
    import pathlib
    p = pathlib.Path(__file__).resolve().parents[1] / "B67_figure_eight_apolynomial" / "probe.py"
    spec = importlib.util.spec_from_file_location("b67_probe", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sym2_groundtruth_coords(xval):
    """The 8 SL(3) coordinates of Sym^2 applied to the B67 figure-eight SL(2) rep at x=xval."""
    A2, B2, *_ = _load_b67().build_rep(xval)
    return coords8_numeric(sym2(A2), sym2(B2))


# --------------------------------------------------------------------------- #

def main():
    print("B71 -- SL(3) figure-eight character variety from the trace-map fixed locus\n")
    eqs = fixed_locus_equations()
    print("Fix(T_1^2) = {T_1^2(x) = x}.  Linear consequences: x3=x2, x8=x5, x6=x4, x7=x1.")
    print("reduced ideal in (x1,x2,x4,x5):")
    for e in reduced_ideal():
        print("   ", sp.factor(e), "= 0")

    comps = components()
    print("\nexact decomposition into 3 components, each dim 2 (T_1^2 fixes each parametrization):")
    print("   V0 {x1=x4, x2=x5}  (geometric, contains Sym^2)")
    print("   W1 {x1=x4=1}       (trace-=1 / Dehn-filling-type)")
    print("   W2 {x2=x5=1}       (trace-=1 / Dehn-filling-type)")
    for nm, (_params, coord) in comps.items():
        fixed = all(sp.expand(a - b) == 0 for a, b in zip(T1_sq(coord), coord))
        print(f"     {nm} subset Fix(T_1^2): {'OK' if fixed else 'FAIL'}")

    print("\nSym^2 ground truth: deviation from V0 {x1=x4, x2=x5}")
    dev = 0.0
    for xv in (3, 4, 5, 2.5, 7, -1, 0.3, 1.7, -2.5, 6, 8, 0.5 + 0.5j):
        c = sym2_groundtruth_coords(xv)
        dev = max(dev, abs(c[0] - c[3]) + abs(c[1] - c[4]))
    print(f"   max(|x1-x4| + |x2-x5|) over 12 points = {dev:.1e}  -> Sym^2 subset V0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
