"""B156 -- the Ω strict-full cone (V149). Fast deterministic locks.

Re-derives the cheap core facts of the four independently-verified Ω claims:
- core R/G algebra (det R=1, palindromic charpoly, R^T G R=G, det G=-delta/(m+1),
  shear actions, signature (1,3)/(1,2,1)/(2,2));
- TC-2 (a strict-full matrix has a reciprocal charpoly; a non-reciprocal control
  admits no nondegenerate invariant form);
- the Fibonacci block-count (transfer matrix [[1,1],[1,0]] -> F_{n+1});
- the strict-full L4 seed count = 96 (and every seed reciprocal -> TC-2 spot check).

The heavy reproducers (full signature sweep, entropy to n=8000, the L5-L10 counts)
live in frontier/B156_omega_strict_full_cone/ and are not re-run here.
"""
import importlib.util
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
B156 = ROOT / "frontier" / "B156_omega_strict_full_cone"

a, m, x = sp.symbols("a m x")

# explicit family (transcribed from the verified omega_independent_verify.py)
R = sp.Matrix([
    [a - 3, a - 2, 1, a - 4],
    [0, 1, 1, 0],
    [m + 1, m + 1, 1, m + 1],
    [1, 1, 0, 1],
])
G = sp.Matrix([
    [-1, 0, (a - 4) / (m + 1), 0],
    [0, -(2 * a - m - 9) / (m + 1), 0, 2],
    [(a - 4) / (m + 1), 0, -(a ** 2 - 8 * a + 2 * m + 18) / (m + 1) ** 2, 1],
    [0, 2, 1, 0],
])
delta = 2 * a - 1 - m


def test_core_algebra_symbolic():
    assert sp.simplify(R.det()) == 1
    cp = sp.expand((x * sp.eye(4) - R).det())
    assert sp.simplify(cp - (x**4 - a * x**3 + (2 * a - 2 * m - 4) * x**2 - a * x + 1)) == 0
    coeffs = sp.Poly(cp, x).all_coeffs()
    assert all(sp.simplify(coeffs[i] - coeffs[-1 - i]) == 0 for i in range(len(coeffs)))  # palindromic
    assert sp.simplify(R.T * G * R - G) == sp.zeros(4)
    assert sp.simplify(G - G.T) == sp.zeros(4)
    assert sp.simplify(G.det() - (-delta / (m + 1))) == 0


def test_shear_actions():
    S03 = sp.eye(4); S03[0, 3] = 1
    S23 = sp.eye(4); S23[2, 3] = 1
    assert sp.simplify(S03 * R - R.subs(a, a + 1)) == sp.zeros(4)  # delta -> delta+2
    assert sp.simplify(S23 * R - R.subs(m, m + 1)) == sp.zeros(4)  # delta -> delta-1


def _sig(av, mv):
    Gn = np.array(G.subs({a: av, m: mv}).evalf(), dtype=float)
    ev = np.linalg.eigvalsh(Gn)
    return int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((np.abs(ev) <= 1e-9).sum())


def test_signature_cone_wall_below():
    assert _sig(8, 0) == (1, 3, 0)        # live cone delta>=1
    assert _sig(8, 2 * 8 - 1) == (1, 2, 1)  # wall delta=0
    assert _sig(8, 20) == (2, 2, 0)       # delta<0


def test_tc2_reciprocal_and_control():
    # a strict-full matrix R_{a,m} (a=8,m=0) is reciprocal
    Rn = sp.Matrix(R.subs({a: 8, m: 0}))
    cp = sp.Poly((x * sp.eye(4) - Rn).det(), x).all_coeffs()
    assert all(cp[i] == cp[-1 - i] for i in range(len(cp)))
    # control: a det-1 NON-reciprocal charpoly admits no NONdegenerate invariant form
    # companion of x^4 - 3x^3 + 2x^2 - x + 1 (non-palindromic)
    C = sp.Matrix([[0, 0, 0, -1], [1, 0, 0, 1], [0, 1, 0, -2], [0, 0, 1, 3]])
    g = sp.symbols("g0:16")
    Gv = sp.Matrix(4, 4, lambda i, j: g[4 * i + j])
    cons = [Gv[i, j] - Gv[j, i] for i in range(4) for j in range(i + 1, 4)]
    cons += list(C.T * Gv * C - Gv)
    sol = sp.solve(cons, list(g), dict=True)[0]
    free = sorted({s for v in sol.values() for s in v.free_symbols}, key=str)
    Gg = Gv.subs(sol)
    # generic member is identically singular -> no nondegenerate invariant form
    assert sp.expand(Gg.det()) == 0 or len(free) == 0


def test_fibonacci_block_count():
    T = sp.Matrix([[1, 1], [1, 0]])  # transfer matrix; compositions into {1,2}
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    # N_n = compositions of n into parts {1,2} = F_{n+1}
    def comps(n, memo={0: 1, 1: 1}):
        if n in memo:
            return memo[n]
        memo[n] = comps(n - 1) + comps(n - 2)
        return memo[n]
    assert [comps(n) for n in range(13)] == fib
    assert sorted(T.eigenvals().keys(), key=lambda e: float(e)) == \
        sorted([(1 - sp.sqrt(5)) / 2, (1 + sp.sqrt(5)) / 2], key=lambda e: float(e))


def test_strict_full_L4_seed_is_96_and_reciprocal():
    spec = importlib.util.spec_from_file_location("ir", B156 / "independent_recount.py")
    ir = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ir)
    cache = {}
    seed = ir.initial_seed_counter(cache)
    assert sum(seed.values()) == 96
    assert len(seed) == 36
    # every seed endpoint has the golden×phase charpoly (4,5,4) -> reciprocal (a==c)
    for M in seed:
        abc = ir.charpoly_abc(M)
        assert abc == (4, 5, 4) and abc[0] == abc[2]
