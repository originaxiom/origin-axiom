"""B306 -- the principal-grading cascade of E6: the forced pseudo-Levi chain, the left-right SM-containing group at
N=5, and the saddle re-refuted (Chat-1, 3rd time). Run with sage-python (E6 root system); verdict.py records (pyenv).

Chat-1 claimed the full SM gauge group appears as a transient "window" SU(3)xSU(2)xU(1)^3 (dim 14) at u=2pi i/3+eps,
between trinification and a saddle "SU(3)xU(1)^4". Assessed verify-don't-trust. The principal-grading centralizers
(roots with height == 0 mod N, i.e. survivors of exp((2pi i/N) h)) form a FORCED cascade:

  N=1: E6 (78) ; N=2: SU(6)xSU(2) (38) ; N=3: SU(3)^3 trinification (24) ; N=4: SU(3)^2xSU(2) (20) ;
  N=5: SU(3)xSU(2)xSU(2)xU(1)^2 (16) ; N=6: SU(2)^3 (12) ; ...

FINDINGS:
  * The SM-shaped point is N=5, NOT Chat-1's "2pi i/3+eps". At N=5 the centralizer is the LEFT-RIGHT gauge group
    SU(3)_c x SU(2)_L x SU(2)_R x U(1)^2 -- which CONTAINS the SM; the SM is reached by breaking SU(2)_R (the standard
    left-right -> SM step), an EXTERNAL choice (which SU(2) survives, which U(1) is hypercharge).
  * Chat-1's "dim-14 SU(3)xSU(2)xU(1)^3" matches NO clean centralizer (N=4 dim 20, N=5 dim 16). The perturbative
    "window" is not a forced grading point.
  * The saddle N=6 is SU(2)^3, NOT SU(3)xU(1)^4 -- Chat-1 refuted a THIRD time (after B304, B305).
  * N=5 = k+2 is the figure-eight's WRT level (k=3); the N=3,6 (Eisenstein) points are the hyperbolic/Q(sqrt-3) end
    (B305), N=5 the golden/zeta_5 end (B261) -- so the level connection is a [LEAP] (mixes the two ends), flagged.

What's forced: the cascade (standard E6 Borel-de Siebenthal, GENERIC E6). Object connection: N=3,6 at the Eisenstein
omega (B305). NOT forced / firewalled: the SM as the exact endpoint (needs SU(2)_R breaking + U(1) projection = the
external value choice); the deformation-as-RG reading; the N=5<->level coincidence. Nothing to CLAIMS.
"""
from sage.all import RootSystem
import networkx as nx

_NAMES = {1: 'A1', 3: 'A2', 6: 'A3', 10: 'A4', 15: 'A5', 36: 'E6'}


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


def cascade():
    pos, ht, form = _setup()
    out = {}
    for N in range(1, 7):
        surv = [r for r in pos if ht(r) % N == 0]
        n = len(surv)
        G = nx.Graph(); G.add_nodes_from(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if form(surv[i], surv[j]) != 0:
                    G.add_edge(i, j)
        comps = sorted(len(c) for c in nx.connected_components(G))
        dim = 2 * n + 6                                  # roots + Cartan(6)
        out[N] = (comps, dim)
    return out


if __name__ == "__main__":
    c = cascade()
    label = {1: 'E6', 2: 'SU(6)xSU(2)', 3: 'SU(3)^3 (trinification)', 4: 'SU(3)^2xSU(2)',
             5: 'SU(3)xSU(2)xSU(2)xU(1)^2 (LEFT-RIGHT, contains SM)', 6: 'SU(2)^3 (saddle)'}
    print("principal-grading cascade (height==0 mod N):")
    for N in range(1, 7):
        comps, dim = c[N]
        print(f"  N={N}: components {comps}, dim {dim}  = {label[N]}")
    print("\nSM-shaped point = N=5 (left-right SU(3)xSU(2)_LxSU(2)_RxU(1)^2 ⊃ SM; break SU(2)_R -> SM).")
    print("Chat-1 dim-14 'window' matches no clean centralizer; saddle N=6 = SU(2)^3 (NOT SU(3)xU(1)^4) -- refuted 3rd.")
    assert c[3][0] == [3, 3, 3] and c[5][0] == [1, 1, 3] and c[6][0] == [1, 1, 1]
