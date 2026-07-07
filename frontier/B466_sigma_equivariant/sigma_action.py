#!/usr/bin/env python3
"""B466 — the sigma-equivariant locus (Chat-1's proposal, adjudicated + computed).

sigma = the substitution a->ab, b->a = B71's T1; sigma^2 = the fig-8 monodromy.
sigma_ab = [[1,1],[1,0]], det = -1: sigma is ORIENTATION-REVERSING; its mapping torus
is the Gieseking manifold, and the fig-8 complement is its orientation double cover
(standard; lit-gate). The sigma-action on the bundle's character variety is the deck
action of that 2-cover; sigma-fixed characters = those descending to Gieseking.

Computed exactly here (sympy, on B71's banked component parametrizations):
  T1(V0(p,q)) = V0(q,p)   -- the geometric component is preserved, with involution
  T1(W1(p,q)) = W2(q,p)   -- the Dehn-filling pair EXCHANGES (Chat-1's central question)
  sigma-fixed locus = the line {p = q} in V0, through the all-ones triple point
                      (V0 cap W1 cap W2 = the all-ones character).
At SL(2): the geometric fiber characters are x = (3 +- sqrt(-3))/2 on the B67 curve
(kappa = -2 restricts to x^2(x^2-3x+3) = 0), and sigma (x -> x/(x-1)) SWAPS them —
the banked B448 period-2 Q(sqrt-3) orbit IS the sigma-orbit of the geometric structure.
The only sigma-fixed characters on the curve are the degenerate x in {0, 2}.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B71_sl3_apoly"))
from probe import T1, components

p, q = sp.symbols("p q")
x = sp.Symbol("x")


def sigma_component_map():
    """returns {source: (target, 'swapped-params')} for the T1 action on B71's components."""
    comps = components()
    out = {}
    for name, (params, coords) in comps.items():
        img = tuple(sp.expand(e) for e in T1(coords))
        for name2, (params2, coords2) in comps.items():
            swapped = tuple(sp.expand(c.subs({params2[0]: q, params2[1]: p}, simultaneous=True))
                            for c in coords2)
            if img == swapped:
                out[name] = name2
    return out


def sigma_fixed_locus():
    comps = components()
    V0 = comps["V0"][1]
    on_v0 = sorted({sp.expand(a - b) for a, b in zip(T1(V0), V0)} - {0}, key=str)
    W1 = comps["W1"][1]
    on_w1 = sp.solve([sp.Eq(a, b) for a, b in zip(T1(W1), W1)], [p, q], dict=True)
    allones = all(tuple(c.subs({p: 1, q: 1}) for c in comps[n][1]) == tuple([1] * 8)
                  for n in comps)
    return on_v0, on_w1, allones


def sl2_geometric_orbit():
    """the geometric fiber characters and the sigma swap on the B67 curve."""
    y = x / (x - 1)
    kap_plus_2 = sp.factor(sp.numer(sp.together(x**2 + 2 * y**2 - x * y**2)))
    roots = sp.solve(x**2 - 3 * x + 3, x)
    inv = lambda t: sp.simplify(t / (t - 1))
    swap = sp.simplify(inv(roots[0]) - roots[1]) == 0 and sp.simplify(inv(roots[1]) - roots[0]) == 0
    fixed = sp.solve(sp.Eq(inv(x), x), x)
    return kap_plus_2, roots, swap, fixed


if __name__ == "__main__":
    ok = True
    m = sigma_component_map()
    print("sigma on components:", m)
    ok &= m == {"V0": "V0", "W1": "W2", "W2": "W1"}
    on_v0, on_w1, allones = sigma_fixed_locus()
    print("fixed on V0 iff:", on_v0, "| fixed on W1:", on_w1, "| all-ones triple point:", allones)
    ok &= set(map(str, on_v0)) == {"-p + q", "p - q"} and on_w1 == [{p: 1, q: 1}] and allones
    kap, roots, swap, fixed = sl2_geometric_orbit()
    print("kappa+2 numerator on B67 curve:", kap)
    print("geometric characters:", roots, "| sigma swaps them:", swap, "| sigma-fixed on curve:", fixed)
    ok &= swap and set(fixed) == {0, 2}
    A = sp.Matrix([[1, 1], [1, 0]])
    ok &= A.det() == -1 and (A * A) == sp.Matrix([[2, 1], [1, 1]])
    print("sigma_ab det -1, sigma^2 = monodromy: verified")
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)
