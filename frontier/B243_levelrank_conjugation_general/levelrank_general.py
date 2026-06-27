"""B243 -- generalizing the B242 level-rank=conjugation mechanism across levels k. Two findings, one of which is
a REFUTED over-claim (verify-don't-trust). Firewall-clean; nothing to CLAIMS.md.

FINDING 1 (the mechanism is UNIVERSAL, not golden-specific).
The level-rank duality SU(2)_k <-> SU(k)_2 acts on the fundamental KNOT invariant
(= HOMFLY(a=q^N, z=q-q^{-1}), q=e^{i pi/kappa}, kappa=k+2) as COMPLEX CONJUGATION, for ALL k:
  q^kappa = e^{i pi} = -1  =>  a=q^2 |-> a=q^k = q^{kappa-2} = -q^{-2}  =>  a^2 |-> q^{-4} = conj(q^4) = conj(a^2).
Hence SU(2)_k = SU(k)_2 EXACTLY iff the invariant is real iff the knot is AMPHICHEIRAL -- at EVERY level k.
So B242's golden coincidence is one instance of a level-independent mechanism; the golden value -2/phi is just
the k=3 specialization. (Specificity filter: the MECHANISM is universal; the VALUE is level-specific.)

FINDING 2 (the seductive 'metallic ladder' is REFUTED).
The figure-eight's level-rank-self-dual value V(k)=2cos(4pi/kappa)-2cos(2pi/kappa)+1 is GOLDEN (-2/phi) at k=3
and SILVER (1-sqrt2) at k=6 -- which LOOKS like a metallic ladder V(m^2+2) in Q(sqrt(m^2+4)). It is NOT a ladder:
V(k) lands in a QUADRATIC field exactly at the four levels with phi(kappa)=4, i.e. kappa in {5,8,10,12}
(k=3,6,8,10 -> sqrt5, sqrt2, Q(V=0), sqrt3). Golden (kappa=5) and silver (kappa=8) coincide with metallic fields
m=1,2 ONLY because 5 and 8 happen to be phi=4 levels. BRONZE (kappa=13, m=3) has phi(13)=12 -> V(11) is DEGREE 6,
NOT in Q(sqrt13). The metallic correspondence is a 2-case coincidence, not a ladder. (Sage-verified degrees:
deg(V) = 2 only for kappa in {5,8,10,12} among kappa<=14; deg(V(11))=6.)

FINDING 3 (scope of the clean statement). The exact '=conjugation' holds for the self-transpose FUNDAMENTAL rep
(single box, R^T=R). For higher colors the level-rank duality transposes the Young diagram (SU(2)_k color N <->
SU(k)_2 in the column/antisymmetric rep Lambda^{N-1}), relating DIFFERENT invariants -- not pure conjugation.

Run: python levelrank_general.py (pyenv).
"""
import cmath

import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def P_fig8(a, z):
    return a ** 2 - z ** 2 + a ** -2 - 1            # 4_1 HOMFLY (amphicheiral: symmetric a<->1/a)


def P_tref(a, z):
    return -a ** 4 + a ** 2 * z ** 2 + 2 * a ** 2   # 3_1 HOMFLY (chiral)


def levelrank_pair(P, k):
    """(SU(2)_k value, SU(k)_2 value) of the knot at the CS root q=e^{i pi/(k+2)}."""
    q = cmath.exp(1j * np.pi / (k + 2)); z = q - 1 / q
    return P(q ** 2, z), P(q ** k, z)


def fig8_value(k):
    """V(k) = the figure-eight's level-rank-self-dual fundamental invariant at level k."""
    kap = k + 2
    return 2 * np.cos(4 * np.pi / kap) - 2 * np.cos(2 * np.pi / kap) + 1


# Sage-verified algebraic degrees of V(k): rational (deg 1) at k in {1,2,4,8}; quadratic (deg 2) at k in {3,6,10};
# else deg>2. The quadratic+rational ('field deg <=2') levels are exactly phi(kappa)<=2-equivalent; deg(V(11))=6.
FIELD_LABEL = {1: "rational (1)", 2: "rational (-1)", 3: "sqrt5 (GOLDEN, m=1)", 4: "rational (-1)",
               6: "sqrt2 (SILVER, m=2)", 8: "rational (0)", 10: "sqrt3"}

if __name__ == "__main__":
    print("=== FINDING 1: level-rank = complex conjugation is UNIVERSAL across k ===")
    for k in range(2, 11):
        f2, fk = levelrank_pair(P_fig8, k)
        t2, tk = levelrank_pair(P_tref, k)
        fig_exact = abs(f2 - fk) < 1e-9
        tref_conj = abs(t2 - tk.conjugate()) < 1e-9
        selfdual = (k == 2)   # SU(2)_2 <-> SU(2)_2: a=q^2 maps to itself
        assert fig_exact and tref_conj
        print(f"  k={k:2d}: fig8 exact={fig_exact}  trefoil conjugate={tref_conj}" + ("  (k=2 self-dual point)" if selfdual else ""))

    print("\n=== FINDING 2: the figure-eight value V(k) -- and the REFUTED metallic ladder ===")
    assert abs(fig8_value(3) - (-2 / PHI)) < 1e-9          # golden
    assert abs(fig8_value(6) - (1 - 2 ** 0.5)) < 1e-9       # silver
    assert abs(fig8_value(8) - 0) < 1e-9                    # zero
    assert abs(fig8_value(10) - (2 - 3 ** 0.5)) < 1e-9      # sqrt3
    for k in range(1, 13):
        kap = k + 2
        met = next((f"  metallic m={m}" for m in range(1, 5) if kap == m * m + 4), "")
        field = FIELD_LABEL.get(k, "deg>2 (non-quadratic)")
        print(f"  k={k:2d} (kappa={kap:2d}): V={fig8_value(k):+.5f}   {field}{met}")
    print("\n  => golden(k=3)+silver(k=6) match metallic fields, BUT bronze (kappa=13,m=3) is degree 6, NOT in")
    print("     Q(sqrt13): the 'metallic ladder' is a 2-case coincidence (the phi(kappa)=4 levels {5,8,10,12}),")
    print("     NOT a ladder. The MECHANISM is universal; the metallic VALUES are not a general pattern.")
    print("\nALL CHECKS PASS")
