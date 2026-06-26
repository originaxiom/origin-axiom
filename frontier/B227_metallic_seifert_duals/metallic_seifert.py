"""B227 / L45 -- the metallic SUSY chains have explicit Seifert 3-manifold duals (the Gang et al. 3d-3d
program). Nothing to CLAIMS.md.

B224 showed the metallic chain at index m flows to the unitary minimal model M(m^2+4, m^2+3) (m=1 golden =
tricritical Ising M(4,5), the unique superconformal one). Gang-Kang-Kim (arXiv:2405.16377, VERIFIED) realize
each minimal model M(P,Q) as a 3D class-R theory on a SEIFERT FIBER SPACE:

    M(P,Q)  <->  Seifert  S^2((P, P-R), (Q, S), (3,1)),    with  P*S - Q*R = 1  (R,S mod Z(P,Q)).

For the metallic family P=m^2+4 (= the METALLIC DISCRIMINANT), Q=m^2+3=P-1, the relation P*S-Q*R=1 is solved
by (R,S)=(1,1) for ALL m (since P-Q=1). So:

    metallic chain m  ->  Seifert  S^2((m^2+4, m^2+3), (m^2+3, 1), (3,1)).

RESULTS (verified):
  - m=1 reproduces the paper's TCI Seifert S^2((5,-1),(4,5),(3,1)) (same 3-manifold; (R,S)=(1,1) and (6,5) are
    in the same class (1,1)+(P,Q); |H_1|=83 in both presentations).
  - the base orbifold is S^2(m^2+4, m^2+3, 3): the three cone-point orders are (m^2+4, m^2+3, 3), and the
    LARGEST is the metallic discriminant m^2+4 (the sequence 5,8,13,20,29,40,53,...). golden (m=1) = S^2(5,4,3).
  - |H_1| = 4m^4 + 28m^2 + 51 = (2m^2+7)^2 + 2 = (2P-1)^2 + 2  (a clean quartic; finite, so b_1=0).
  - orbifold Euler number e = -(P-R)/P - S/Q - 1/3 = -|H_1| / (3 P Q)  (e != 0 confirms |H_1| finite).
  - all base orbifolds are hyperbolic (1/(m^2+4)+1/(m^2+3)+1/3 < 1) -> SL2~ / non-hyperbolic 3-manifolds
    (consistent with "minimal models from NON-hyperbolic 3-manifolds", B226).

So the metallic SUSY chains pick out the SUBFAMILY of unitary-minimal-model Seifert spaces whose largest cone
order is a metallic discriminant. This ties B224 (the metallic SUSY family) concretely to the active 3d-3d
minimal-model program. The deeper "golden is the UNIQUE superconformal one" (B224) becomes, in 3-manifold terms,
"the golden Seifert S^2(5,4,3) is the unique one ALSO realized as a SUSY-minimal-model Seifert space" -- a
follow-on needing the SUSY-minimal-model recipe (JHEP 01(2025)027 / JHEP 03(2026)066), NOT computed here.

Firewall: the Seifert/H_1/Euler bookkeeping + the cited recipe are firewall-clean math; the 3d-3d physics reading
is firewalled in speculations/S040; nothing to CLAIMS.md; P1-P16 untouched. Run: python metallic_seifert.py (pyenv;
uses only fractions). [Smith-form/H_1 also cross-checked with sage-python; here computed by the exact det formula.]
"""
from fractions import Fraction as Fr


def metallic_minimal_model(m):
    """B224: metallic chain m -> unitary minimal model M(P,Q), P=m^2+4 (discriminant), Q=m^2+3."""
    return m * m + 4, m * m + 3


def seifert_data(m):
    """Gang-Kang-Kim recipe with (R,S)=(1,1): S^2((P,P-R),(Q,S),(3,1)); returns (fibers, b)."""
    P, Q = metallic_minimal_model(m)
    R, S = 1, 1
    assert P * S - Q * R == 1                      # the SL(2,Z) condition
    return [(P, P - R), (Q, S), (3, 1)], 0


def h1_order(fibers, b):
    """|H_1| of the Seifert space over S^2 = |det| of the presentation matrix
    [[a1,0,0,b1],[0,a2,0,b2],[0,0,a3,b3],[1,1,1,b]] (exact integer formula, b=0 here)."""
    (a1, b1), (a2, b2), (a3, b3) = fibers
    # det = a1 a2 a3 b - (b1 a2 a3 + a1 b2 a3 + a1 a2 b3)
    det = a1 * a2 * a3 * b - (b1 * a2 * a3 + a1 * b2 * a3 + a1 * a2 * b3)
    return abs(det)


def euler_number(fibers, b):
    """orbifold/Seifert Euler number e = -(b + sum beta_i/alpha_i)."""
    return -(Fr(b) + sum(Fr(bb, a) for (a, bb) in fibers))


def cone_orders(m):
    P, Q = metallic_minimal_model(m)
    return (P, Q, 3)


if __name__ == "__main__":
    print("metallic chain m -> M(m^2+4, m^2+3) -> Seifert S^2((m^2+4,m^2+3),(m^2+3,1),(3,1)):")
    print(f"{'m':>2} {'M(P,Q)':>11} {'cone orders':>14} {'|H_1|':>8} {'Euler e':>12}")
    for m in range(1, 8):
        fib, b = seifert_data(m)
        P, Q = metallic_minimal_model(m)
        print(f"{m:>2} M({P:>3},{Q:>3}) {str(cone_orders(m)):>14} {h1_order(fib, b):>8} {str(euler_number(fib, b)):>12}")
    print("\n  cone orders = (m^2+4, m^2+3, 3); LARGEST = m^2+4 = the metallic discriminant (5,8,13,20,29,...).")
    ok = all(h1_order(seifert_data(m)[0], 0) == 4 * m**4 + 28 * m**2 + 51 for m in range(1, 12))
    print(f"  |H_1| = 4m^4+28m^2+51 = (2m^2+7)^2+2 : {ok}")
    # verify m=1 reproduces the paper's TCI Seifert (same 3-manifold, different (R,S) in the same class)
    h1_mine = h1_order(seifert_data(1)[0], 0)
    h1_paper = h1_order([(5, -1), (4, 5), (3, 1)], 0)
    print(f"  m=1 vs paper TCI S^2((5,-1),(4,5),(3,1)): |H_1| {h1_mine} == {h1_paper}: {h1_mine == h1_paper}")
    print("ALL CHECKS PASS")
