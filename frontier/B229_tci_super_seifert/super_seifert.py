"""B229 -- the explicit super-Seifert dual of the tricritical Ising, and the 3-manifold form of B228:
ONE CFT (the TCI/golden), TWO distinct bulk 3-manifolds. Nothing to CLAIMS.md.

B228 showed (at the coset level) that the TCI is the unique metallic chain realized BOTH as an ordinary AND
as an N=1 super minimal model (the ordinary and super GKO cosets coincide uniquely at SU(2)_3). This computes
the explicit 3-manifold (Seifert) realizations and finds they are DIFFERENT 3-manifolds.

The two 3d-3d recipes (Gang-Kang-Kim arXiv:2405.16377 ordinary; Baek-Kang arXiv:2511.04524 super) have the SAME
Seifert form S^2((P,P-R),(Q,S),(3,1)) but DIFFERENT determinant -- the SU(2) level used in the GKO coset:
    ORDINARY  M(P,Q):  PS - QR = 1   (SU(2)_1)
    SUPER     SM(P,Q): PS - QR = 2   (SU(2)_2)

The tricritical Ising:
    ordinary label M(4,5) (|P-Q|=1, c=1-6/(4*5)=7/10) -> S^2((5,4),(4,1),(3,1)),  cone orders (5,4,3),  |H_1|=83.
    super label    SM(3,5) (|P-Q|=2, c=3/2(1-2*4/(3*5))=7/10) -> S^2((5,4),(3,1),(3,1)), cone orders (5,3,3), |H_1|=66.

So the TCI has TWO distinct 3d-3d bulk realizations: the ordinary one on the Seifert space over the orbifold
S^2(3,4,5) (|H_1|=83), and the super one on the Seifert space over S^2(3,3,5) (|H_1|=66). The coset coincidence
(B228, same boundary CFT) does NOT lift to a 3-manifold coincidence: ONE CFT, TWO bulk 3-manifolds, distinguished
by the SU(2)_1-vs-SU(2)_2 (determinant 1-vs-2) structure.

Only golden/TCI has a super realization at all (the metallic ordinary models M(m^2+3,m^2+4) have |P-Q|=1, never
the |P-Q|=2 of the unitary super series SM(p,p+2); the unique overlap is the TCI = M(4,5) = SM(3,5)).

VERIFICATION (verify-don't-trust, honest): the ordinary recipe is fully verified (B227 reproduces the published
TCI Seifert). The super recipe PS-QR=2 + the Seifert form is a VERIFIED VERBATIM abstract quote (arXiv:2511.04524);
TCI=SM(3,5) is verified via the central-charge formula c=3/2(1-2(p'-p)^2/pp') (arXiv:2405.05746). The cone orders
(P,Q,3) follow from the recipe form. NOT independently anchored against a published super WORKED example (the
paper's html was unavailable) -- flagged. Firewall: Seifert/H_1 bookkeeping + cited recipes = firewall-clean;
the 3d-3d reading firewalled in S040; nothing to CLAIMS.md. Run: python super_seifert.py (pyenv).
"""
from fractions import Fraction as Fr


def c_ordinary(P, Q):
    """ordinary minimal model M(P,Q): c = 1 - 6(P-Q)^2/(P*Q)."""
    return Fr(1) - Fr(6 * (P - Q) ** 2, P * Q)


def c_super(P, Q):
    """N=1 super minimal model SM(P,Q): c = 3/2 (1 - 2(P-Q)^2/(P*Q))  (arXiv:2405.05746 eq.3)."""
    return Fr(3, 2) * (Fr(1) - Fr(2 * (P - Q) ** 2, P * Q))


def find_RS(P, Q, det):
    """smallest (R,S) with P*S - Q*R = det (det=1 ordinary, det=2 super)."""
    for S in range(0, 4 * (P + Q)):
        for R in range(0, 4 * (P + Q)):
            if P * S - Q * R == det:
                return R, S
    raise ValueError("no (R,S)")


def seifert(P, Q, det):
    """Seifert S^2((P,P-R),(Q,S),(3,1)) with P*S-Q*R=det; returns (fibers, cone_orders)."""
    R, S = find_RS(P, Q, det)
    fibers = [(P, P - R), (Q, S), (3, 1)]
    return fibers, (P, Q, 3)


def h1_order(fibers):
    (a1, b1), (a2, b2), (a3, b3) = fibers
    det = -(b1 * a2 * a3 + a1 * b2 * a3 + a1 * a2 * b3)   # background b=0
    return abs(det)


if __name__ == "__main__":
    print("the SU(2) level in the GKO coset = the determinant of the 3d-3d recipe:")
    print("  ORDINARY M(P,Q): PS-QR=1 (SU(2)_1);   SUPER SM(P,Q): PS-QR=2 (SU(2)_2)\n")

    print("tricritical Ising, two labels / two bulk realizations:")
    # ordinary M(4,5): use P=5,Q=4 (P>Q)
    fib_o, cone_o = seifert(5, 4, 1)
    print(f"  ORDINARY M(4,5): c={c_ordinary(5,4)}  Seifert {fib_o}  cone orders {cone_o}  base S^2{tuple(sorted(cone_o))}  |H_1|={h1_order(fib_o)}")
    # super SM(3,5): use P=5,Q=3
    fib_s, cone_s = seifert(5, 3, 2)
    print(f"  SUPER    SM(3,5): c={c_super(5,3)}  Seifert {fib_s}  cone orders {cone_s}  base S^2{tuple(sorted(cone_s))}  |H_1|={h1_order(fib_s)}")

    same_cft = c_ordinary(5, 4) == c_super(5, 3) == Fr(7, 10)
    diff_manifold = (tuple(sorted(cone_o)) != tuple(sorted(cone_s))) and (h1_order(fib_o) != h1_order(fib_s))
    print(f"\n  same boundary CFT (c=7/10): {same_cft}")
    print(f"  DIFFERENT bulk 3-manifold (base orbifold AND |H_1| differ): {diff_manifold}")
    print("  => ONE CFT (golden/TCI), TWO distinct bulk 3-manifolds: S^2(3,4,5) |H_1|=83 (ordinary) vs")
    print("     S^2(3,3,5) |H_1|=66 (super). The coset coincidence (B228) does NOT lift to the bulk.")

    print("\n  only golden is BOTH: the metallic ordinary models M(m^2+3,m^2+4) have |P-Q|=1; the unitary super")
    print("  series SM(p,p+2) has |P-Q|=2; the unique overlap is the TCI = M(4,5) = SM(3,5).")
    assert same_cft and diff_manifold
    print("ALL CHECKS PASS")
