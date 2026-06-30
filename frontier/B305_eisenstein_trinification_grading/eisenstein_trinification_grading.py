"""B305 -- the Eisenstein trinification grading: E6 -> SU(3)^3 at omega (verified); the saddle gives SU(2)^3 NOT SU(3)
(Chat-1 re-refuted). Run with sage-python (E6 root system); verdict.py records the Sage-verified facts (pyenv).

Chat-1 proposed a forced breaking cascade E6 -> SU(3)^3 trinification -> SU(3), parametrized by the deformation u
along the character variety, at the Eisenstein values u=2pi i/3 and u=i pi/3. Assessed verify-don't-trust (after
B304 already refuted the same "saddle SU(3)" once). The condition for a root alpha to survive exp(u h) (h = principal
grading element, alpha(h) = height) is u*height(alpha) in 2pi i Z:
   u = 2pi i/3  ->  height == 0 mod 3
   u = i pi/3   ->  height == 0 mod 6

VERIFIED (E6 root system, Sage):
  * u = 2pi i/3 (the EISENSTEIN point): 9 surviving positive roots (heights 3,6,9 -> 5+3+1), in 3 mutually-orthogonal
    components of 3 each = A2 x A2 x A2 = SU(3)^3 = TRINIFICATION. This is the standard Z3 grading of E6; its grading
    eigenvalue is omega = e^{2pi i/3} in Q(sqrt-3) -- the SAME Eisenstein root that gives 2T (B266) and +-pi/6 (B285).
    So the figure-eight's arithmetic omega IS the trinification grading. And the orbifold (theta,phi) (B299) is the
    triality permuting these three SU(3)'s -- gauge breaking and the (theta,phi) structure are the same object.

REFUTED (2nd time -- a clean verify-don't-trust catch):
  * u = i pi/3 (the saddle): 3 surviving positive roots, all MUTUALLY ORTHOGONAL -> A1 x A1 x A1 = SU(2)^3, NOT
    A2 = SU(3). A2 is impossible (needs a height-12 root; E6 max height 11). So the cascade is
    E6 -> SU(3)^3 -> SU(2)^3 x U(1)^3, NOT -> SU(3). Chat-1's "SU(3) color at the saddle" is WRONG (again).

NOT FORCED / firewalled [LEAP]: which SU(3) is color (the trinification triality permutes them -- external, B299/B301);
"u = the energy scale, the character variety = RG trajectories, the topology = the Higgs mechanism" (the deformation-
as-RG reading is unverified physics). The trinification grading itself (height==0 mod 3 = A2^3) is STANDARD E6 rep
theory; the OBJECT connection is the grading eigenvalue omega = the figure-eight's Eisenstein root.

FIREWALLED. Nothing to CLAIMS.
"""
from sage.all import RootSystem, matrix, ZZ
from collections import Counter


def _setup():
    RS = RootSystem('E6'); Q = RS.root_lattice(); C = RS.cartan_matrix()
    pos = list(Q.positive_roots())
    def ht(r): return int(sum(r.coefficients()))
    def vec(r):
        d = r.monomial_coefficients(); return [int(d.get(i + 1, 0)) for i in range(6)]
    def form(r1, r2):
        v1, v2 = vec(r1), vec(r2)
        return sum(v1[i] * C[i, j] * v2[j] for i in range(6) for j in range(6))
    return pos, ht, form


def surviving_components(mod):
    """Positive roots with height == 0 mod `mod`, grouped into non-orthogonal components (the simple factors)."""
    pos, ht, form = _setup()
    surv = [r for r in pos if ht(r) % mod == 0]
    n = len(surv)
    import networkx as nx
    G = nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if form(surv[i], surv[j]) != 0:
                G.add_edge(i, j)
    comps = sorted(len(c) for c in nx.connected_components(G))
    return n, comps


if __name__ == "__main__":
    n3, c3 = surviving_components(3)
    print(f"u=2pi i/3 (Eisenstein omega): {n3} positive roots, components {c3}")
    print(f"   -> A2^3 = SU(3)^3 trinification: {c3 == [3, 3, 3]}  (grading eigenvalue omega in Q(sqrt-3) = B266/B285)")
    n6, c6 = surviving_components(6)
    print(f"u=i pi/3 (saddle): {n6} positive roots, components {c6}")
    print(f"   -> A1^3 = SU(2)^3 (NOT A2=SU(3)): {c6 == [1, 1, 1]}  (Chat-1 'SU(3)' REFUTED, 2nd time)")
    print("\nVERDICT: E6 -> SU(3)^3 (trinification) at the Eisenstein omega is REAL (ties B266/B285/B299);")
    print("the saddle gives SU(2)^3, not SU(3). 'which SU(3) is color' + the RG/Higgs reading stay external/firewalled.")
    assert c3 == [3, 3, 3] and c6 == [1, 1, 1]
