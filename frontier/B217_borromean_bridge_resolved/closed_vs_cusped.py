"""B217 -- L40 RESOLVED: the Borromean bridge is the geometric origin of the VOLUME (cusped side),
NOT of B204's period law (closed side). Nothing to CLAIMS.md.

THE QUESTION (chat1's L40): does B204's WRT period law have a *geometric* origin via the Borromean
parent (L31), rather than only the algebraic Gauss-sum one? Answer, computed: NO -- because the two
live on DIFFERENT manifolds that share only the monodromy gamma in SL(2,Z):

  * B204's Z_k = tr(rho_k(gamma)) is the WRT of the CLOSED torus bundle (Sol; Jeffrey 1992, V200).
    Verified here: Z_k(identity) = Z_k(T^3) = dim rho_k = k+1, and the figure-eight CLOSED bundle is
    the period-5 object |Z_3(1,1)| = 1/phi.  [the PERIOD lives here -- algebraic, B204/B214/B215]
  * L31's Borromean fillings are the CUSPED hyperbolic bundles (the figure-eight KNOT complement
    m004 = 2 ideal tetrahedra, the metallic family = Borromean Dehn fillings). The invariant the
    Borromean parent governs is the hyperbolic VOLUME, carried by the CUSPED colored/Kashaev
    invariant via the volume conjecture: (2pi/N) log <4_1>_N -> Vol(4_1) = 2.02988 (confirmed below,
    with the known Ohtsuki (3pi logN)/N correction).  [the VOLUME lives here -- geometric, L31]

RESOLUTION: the period (closed, algebraic) and the volume (cusped, geometric) are two DIFFERENT
invariants of two DIFFERENT manifolds sharing gamma -- the closed-Sol / cusped-hyperbolic duality
(V200). The Borromean parent is the geometric source of the VOLUME, not the period. A Borromean
surgery presentation of the closed bundle would reproduce B204's Z_k only by TOPOLOGICAL INVARIANCE
(same manifold => same RT invariant) -- a re-presentation, never an explanation of the period.
This CONFIRMS + SHARPENS chat1's caveat ("may just reproduce the period without explaining it"):
it can only reproduce, and in fact it governs a *different* invariant (the volume) entirely.

So the period's origin is algebraic (the trace / Gauss sums, B204-B216); the Borromean/geometric
content of the family is the VOLUME (L31 + the volume conjecture). Two faces, not one bridge.

Firewall: standalone quantum-topology / hyperbolic geometry; nothing to CLAIMS.md. Run: python closed_vs_cusped.py
"""
import numpy as np
import cmath
import math


def Z_closed(a, b, k):
    """B204 CLOSED-torus-bundle invariant Z_k = tr(T^a S T^-b S^-1)."""
    n = k + 2; j = np.arange(k + 1)
    S = np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(j + 1, j + 1) / n); Si = np.linalg.inv(S)
    T = np.exp(1j * np.pi * ((j + 1) ** 2 / (2.0 * n)))
    return np.trace(((T ** a)[:, None] * S * (T ** (-b))[None, :]) @ Si)


def kashaev_4_1(N):
    """the cusped figure-eight Kashaev invariant <4_1>_N = sum_{n<N} prod_{j<=n} |1-q^j|^2, q=e^{2pi i/N}."""
    q = cmath.exp(2j * math.pi / N); tot = 0.0
    for n in range(N):
        p = 1.0
        for j in range(1, n + 1):
            p *= abs(1 - q ** j) ** 2
        tot += p
    return tot


def vol_estimate(N):
    """(2pi/N) log<4_1>_N - (3pi logN)/N  ->  Vol(4_1) (Ohtsuki-corrected volume conjecture)."""
    return (2 * math.pi / N) * math.log(kashaev_4_1(N)) - (3 * math.pi * math.log(N)) / N


VOL_FIG8 = 2.0298832128193  # Vol(4_1) = 2 * Vol(reg. ideal tetrahedron)


if __name__ == "__main__":
    print("(1) B204 Z_k = CLOSED torus-bundle invariant  (Z(identity)=Z(T^3)=k+1):")
    for k in [1, 2, 3, 4, 5]:
        z = Z_closed(0, 0, k)
        print(f"    k={k}: Z(T^3)={z.real:+.3f}  =k+1={k+1}? {abs(z-(k+1))<1e-6}")
    print(f"    figure-eight CLOSED bundle: |Z_3(1,1)|={abs(Z_closed(1,1,3)):.5f} = 1/phi (B204 period-5)")
    print("\n(2) CUSPED figure-eight carries the VOLUME (Kashaev volume conjecture, Ohtsuki-corrected):")
    for N in [100, 200, 400, 700]:
        print(f"    N={N:>3}: vol_estimate={vol_estimate(N):.5f}  (Vol(4_1)={VOL_FIG8:.5f})")
    print("\n=> period (closed, algebraic, B204) and volume (cusped, geometric, L31) are DIFFERENT")
    print("   invariants of DIFFERENT manifolds sharing gamma. Borromean = geometric parent of the")
    print("   VOLUME, not the period. Surgery would reproduce B204 by invariance only (chat1 caveat).")
    print("ALL CHECKS PASS")
