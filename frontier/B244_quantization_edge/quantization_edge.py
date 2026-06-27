"""B244 (pyenv part) -- the (1)<->(2) quantization edge of the three-SU(3) trichotomy (B242): how the quantum
SU(3)_k WRT relates to the classical SL(3,C) character variety (B71). Firewall-clean; nothing to CLAIMS.md.

THE QUESTION (thread 2): does the level-rank SU(3)_2 invariant "see" the 3 components of the SL(3,C) character
variety (B71: V0 geometric=Sym^2, W1/W2 Dehn-filling)?

THE HONEST ANSWER: NO at level 2 -- the SU(3)_2 fundamental invariant is a SINGLE number (-2/phi, B242); it does
not individually resolve the 3 components. The components are the CLASSICAL SL(3,C) flat-connection SADDLES that
the WRT/colored invariant quantizes; they appear only in the k->infty asymptotic expansion (sum over flat
connections, Witten/Gukov), dominated by the geometric component. Two computed facts pin this down:

  (A) [Ptolemy, sl3_volumes.py] the 3 components carry DISTINCT complex volumes: the geometric V0 has
      Vol = 8.11953285 = 4 * Vol(SL(2)) = (n^3-n)/6 * Vol at n=3 (the Sym^2 factor, confirming B71's V0=Sym^2
      identification via the volume); W1/W2 (Dehn-filling) have Vol = 0. So the saddles are geometrically distinct.
  (B) the FUNDAMENTAL invariant cannot see them: P_fig8(a=q^3, z=q-q^{-1}) -> 1 as q -> 1 (k->infty), i.e. NO
      exponential volume growth -- seeing the volume needs the LARGE-COLOR limit (color ~ k; the SL(3) volume
      conjecture), not the fixed fundamental rep at growing level.

So the (1)<->(2) edge is QUANTIZATION (classical char variety <-> quantum WRT); the components are the classical
data (computed here), resolved by the WRT only asymptotically, NOT at the small level k=2.

Run: python quantization_edge.py (pyenv).
"""
import cmath

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
VOL_SL2 = 2.02988321281931            # Vol(4_1), SnapPy
VOL_SL3_GEO = 8.119532851277231       # geometric SL(3) component, SnapPy Ptolemy (sl3_volumes.py)
SL3_COMPONENT_VOLS = (8.119532851277231, 0.0, 0.0)   # V0 (geometric), W1, W2 -- distinct saddles (B71's 3 comps)


def sym_volume_factor(n):
    """(n^3 - n)/6: the factor by which the Sym^{n-1} (principal) rep scales the hyperbolic volume."""
    return (n ** 3 - n) // 6


def P_fig8(a, z):
    return a ** 2 - z ** 2 + a ** -2 - 1          # 4_1 HOMFLY = fundamental SU(N)_k invariant at a=q^N


def su32_fundamental():
    """the SU(3)_2 fundamental invariant of 4_1 (a=q^3, q=e^{i pi/5}) -- a SINGLE number (B242)."""
    q = cmath.exp(1j * np.pi / 5)
    return P_fig8(q ** 3, q - 1 / q)


def fundamental_limit(N, k):
    """P_fig8(a=q^N) at q=e^{i pi/(k+N)} -- for fixed rep, -> 1 as k -> infty (no volume growth)."""
    q = cmath.exp(1j * np.pi / (k + N))
    return P_fig8(q ** N, q - 1 / q)


if __name__ == "__main__":
    print("=== (A) the classical saddles: 3 SL(3,C) components with distinct complex volumes ===")
    print(f"  geometric V0 (=Sym^2 of the SL(2) rep): Vol = {VOL_SL3_GEO}")
    print(f"  = (n^3-n)/6 * Vol(SL(2)) = {sym_volume_factor(3)} * {VOL_SL2} = {sym_volume_factor(3) * VOL_SL2}")
    assert abs(VOL_SL3_GEO - sym_volume_factor(3) * VOL_SL2) < 1e-9
    print(f"  W1, W2 (Dehn-filling): Vol = 0   -> the 3 components are geometrically distinct saddles (B71).")

    print("\n=== (B) SU(3)_2 at level 2 is ONE number; the fundamental rep cannot see the volume ===")
    print(f"  SU(3)_2 fundamental(4_1) = {su32_fundamental():+.6f} = -2/phi  (a single number; resolves nothing)")
    assert abs(su32_fundamental() - (-2 / PHI)) < 1e-9
    for k in (5, 20, 100, 500):
        print(f"  fundamental at k={k:4d}: {fundamental_limit(3, k):+.6f}  -> 1 (no exp. volume growth)")
    assert abs(fundamental_limit(3, 2000) - 1) < 1e-3

    print("\n=== verdict ===")
    print("  SU(3)_2 does NOT resolve the 3 components at level 2; they are the classical SL(3,C) saddles")
    print("  (volumes {4*Vol, 0, 0}) that the WRT quantizes -- resolved only in the k->infty asymptotics")
    print("  (large color, geometric saddle dominant), NOT at level 2. The (1)<->(2) edge is quantization.")
    print("ALL CHECKS PASS")
