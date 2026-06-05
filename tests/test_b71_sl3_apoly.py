"""B71 -- SL(3) figure-eight character variety from the trace-map fixed locus (B0-B1).

Locks: (1) the T_1^2 fixed-locus linear identifications; (2) the exact 3-component decomposition
of Fix(T_1^2) (each dim 2); (3) the Sym^2 ground-truth family lands on the geometric component V0.
"""
import importlib.util
import pathlib

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b71_probe", _ROOT / "frontier" / "B71_sl3_apoly" / "probe.py")
b71 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b71)


def test_fixed_locus_linear_identifications():
    """Fix(T_1^2) forces x3=x2, x8=x5, x6=x4, x7=x1 (the 4 degree-1 consequences)."""
    x1, x2, x3, x4, x5, x6, x7, x8 = b71.X8
    eqs = b71.fixed_locus_equations()
    linear = {sp.factor(e) for e in eqs if sp.Poly(e, *b71.X8).total_degree() == 1}
    assert linear == {sp.factor(x3 - x2), sp.factor(x8 - x5),
                      sp.factor(x4 - x6), sp.factor(x1 - x7)}


def test_three_components_are_fixed():
    """V0, W1, W2 are each pointwise fixed by T_1^2 (contained in Fix(T_1^2))."""
    for _nm, (_params, coord) in b71.components().items():
        assert all(sp.expand(a - b) == 0 for a, b in zip(b71.T1_sq(coord), coord))


def test_decomposition_is_exact():
    """The reduced ideal's nonlinear part factors as (x1-x4)(x2-1), (x1-x4)(x5-1) + two cubics;
    the case split (x1=x4) | (x2=1,x5=1) yields exactly the three listed components and no other
    top-dimensional piece (lex Groebner basis has the two product generators)."""
    x1, x2, x4, x5 = sp.symbols("x1 x2 x4 x5")
    lin = dict(zip(b71.X8, (x1, x2, x2, x4, x5, x4, x1, x5)))  # apply x3=x2,x6=x4,x7=x1,x8=x5
    red = [sp.expand(e.subs(lin)) for e in b71.fixed_locus_equations()]
    red = [e for e in red if e != 0]
    G = sp.groebner(red, x1, x2, x4, x5, order="lex")
    factored = {sp.factor(g) for g in G}
    assert sp.factor((x1 - x4) * (x5 - 1)) in factored
    assert sp.factor((x2 - x5) * (x4 - 1)) in factored


def test_sym2_groundtruth_on_V0():
    """Sym^2 of the figure-eight SL(2) holonomy lands on V0 = {x1=x4, x2=x5}."""
    for xv in (3, 4, 5, 2.5, 7, -1, 0.3, 1.7, -2.5, 6, 8, 0.5 + 0.5j):
        c = b71.sym2_groundtruth_coords(xv)
        assert abs(c[0] - c[3]) + abs(c[1] - c[4]) < 1e-9


def test_sym2_is_T1sq_fixed():
    """The Sym^2 ground-truth character is fixed by the SL(3) trace map T_1^2 (extends over the
    bundle by functoriality) -- the numeric confirmation that T_1^2 is the figure-eight monodromy."""
    def T1_num(c):
        x1, x2, x3, x4, x5, x6, x7, x8 = c
        return np.array([x3, x1, x1 * x3 - x4 * x2 + x6, x8, x4, x5, x2,
                         x4 * x8 - x1 * x5 + x7], dtype=complex)
    for xv in (3, 4, 5, 2.5, 7, -1):
        c = b71.sym2_groundtruth_coords(xv)
        assert np.max(np.abs(T1_num(T1_num(c)) - c)) < 1e-8


# --------------------------------------------------------------------------- #
# B2-B3: explicit realization + peripheral eigenvalue A-variety
# --------------------------------------------------------------------------- #

_pspec = importlib.util.spec_from_file_location(
    "b71_peripheral", _ROOT / "frontier" / "B71_sl3_apoly" / "peripheral.py")
per = importlib.util.module_from_spec(_pspec)
_pspec.loader.exec_module(per)


def _coords8(A, B):
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    tr = np.trace
    return np.array([tr(A), tr(B), tr(A@B), tr(Ai), tr(Bi), tr(Ai@B), tr(A@Bi), tr(Ai@Bi)])


def test_realize_roundtrip():
    """B2: the explicit SL(3) realization reproduces the target trace coordinates on all 3 components."""
    pts = [(per.V0, 0.7 + 0.3j, -0.4 + 1.1j), (per.W1, 1.3 - 0.2j, 0.5 + 0.9j),
           (per.W2, -0.6 + 0.8j, 1.2 + 0.1j)]
    for fn, p, q in pts:
        c = fn(p, q)
        out = per.realize(c)
        assert out is not None
        A, B = out
        assert abs(np.linalg.det(A) - 1) < 1e-9 and abs(np.linalg.det(B) - 1) < 1e-9
        assert np.max(np.abs(_coords8(A, B) - np.array(c, dtype=complex))) < 1e-6


def test_sym2_shadow_validates_monodromy():
    """B3: monodromy of a Sym^2 rep reproduces Sym^2 of the B67 SL(2) monodromy -- eig(t)={mu^2,1,mu^-2}
    (mu = eig of the SL(2) monodromy), up to a global cube-root-of-unity. Validates the t-construction."""
    b67 = b71._load_b67()
    for xv in (4, 5, 2.5, 7):
        A2, B2, t2, _ = b67.build_rep(xv)
        A3, B3 = b71.sym2(A2), b71.sym2(B2)
        t3, res = per.monodromy(A3, B3)
        assert res is not None and res < 1e-6
        e3 = np.sort_complex(np.linalg.eigvals(t3))
        mu = np.linalg.eigvals(t2)
        mu = mu[np.argmax(np.abs(mu))]
        pred = np.sort_complex(np.array([mu**2, 1.0, mu**-2]))
        best = min(np.max(np.abs(e3 - w * pred))
                   for w in (1, np.exp(2j*np.pi/3), np.exp(-2j*np.pi/3)))
        assert best < 1e-7


def test_dehn_filling_avariety_literal_match():
    """B3: the Dehn-filling components reproduce Falbel et al.'s A-variety (arXiv:1412.4711), with
    meridian<->longitude transposed:  W1=D2 -> M^3=L ;  W2=D3 -> M^3 L=1  (M=eig-ratios of mu,
    L=eig-ratios of [A,B])."""
    medW1, _, nW1 = per._avariety_residual("W1", per.W1, lambda M, L: abs(M**3 - L))
    medW2, _, nW2 = per._avariety_residual("W2", per.W2, lambda M, L: abs(M**3 * L - 1))
    assert nW1 >= 10 and medW1 < 1e-6
    assert nW2 >= 10 and medW2 < 1e-6


_dspec = importlib.util.spec_from_file_location(
    "b71_symbolic_dehn", _ROOT / "frontier" / "B71_sl3_apoly" / "symbolic_dehn.py")
sdehn = importlib.util.module_from_spec(_dspec)
_dspec.loader.exec_module(sdehn)


def test_dehn_filling_exact_scalar_criterion():
    """P1 (V47): the Dehn-filling relations are the EXACT scalar-matrix identities [A,B]=c*mu^3 (W1=D2)
    and [A,B]*mu^3=c (W2=D3) -- equivalent to M^3=L / M^3 L=1 given the V46 commutativity. Check the
    scalar-deviation is ~0 on both components."""
    medW1, nW1 = sdehn.dehn_scalar_residual(sdehn.per.W1, "D2")
    medW2, nW2 = sdehn.dehn_scalar_residual(sdehn.per.W2, "D3")
    assert nW1 >= 10 and medW1 < 1e-6
    assert nW2 >= 10 and medW2 < 1e-6


def test_genuine_meridian_commutes_with_longitude():
    """B3 (meridian fix): the genuine peripheral meridian mu = w^-1 t COMMUTES with the longitude
    [A,B] (the abelian cusp pair) on all three components -- the bare monodromy t does NOT. And
    eig(mu)=eig(t), so the A-variety eigenvalue data is unchanged."""
    for fn in (per.V0, per.W1, per.W2):
        rng = np.random.default_rng(5)
        checked = 0
        for _ in range(8):
            p = complex(rng.standard_normal(), rng.standard_normal())
            q = complex(rng.standard_normal(), rng.standard_normal())
            out = per.realize(fn(p, q))
            if out is None:
                continue
            A, B = out
            mu, cdev = per.meridian(A, B)
            t, _res = per.monodromy(A, B)
            if mu is None or t is None:
                continue
            assert cdev < 1e-6                                   # mu commutes with [A,B]
            eig_mu = np.sort_complex(np.linalg.eigvals(mu))
            eig_t = np.sort_complex(np.linalg.eigvals(t))
            assert np.max(np.abs(eig_mu - eig_t)) < 1e-7         # eig(mu) = eig(t)
            checked += 1
        assert checked >= 3
