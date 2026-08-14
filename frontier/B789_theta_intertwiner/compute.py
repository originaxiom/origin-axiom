"""B789 — the explicit theta-intertwiner: harvest of a cc3 (audit-seat) deliverable,
independently re-derived here and STRENGTHENED by the descent check.

Provenance: the matrix Q originates with the cc3 audit seat (its e4ce8ee1). cc3 never merges;
this arc re-derives every claim from scratch under a new number, per the standing rule.

What is banked: the repo's theta-triviality was a TRACE statement (tr g = tr g^R = tr g^-1 in
SL(2)). This upgrades it to an explicit MATRIX intertwiner for the figure-eight geometric rep,
with three scoping facts that keep it honest.
"""
import random

import sympy as sp

u = sp.Symbol("u")
Z2, Z3 = sp.zeros(2, 2), sp.zeros(3, 3)
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
line = "=" * 74


def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, 2*a*b, b**2],
                      [a*c, a*d + b*c, b*d],
                      [c**2, 2*c*d, d**2]])


def ev(word, g):
    M = sp.eye(g[1].shape[0])
    for l in word:
        M = M * g[l]
    return sp.simplify(M)


def head(t):
    print(f"\n{line}\n{t}\n{line}")


# ---- the rep -----------------------------------------------------------------
A = sp.Matrix([[1, 1], [0, 1]])
B_u = sp.Matrix([[1, 0], [-u, 1]])
B = B_u.subs(u, omega)
W = [1, -2, -1, 2]                 # w = a b^-1 a^-1 b   (found by search, see V1)
REL_L, REL_R = W + [1], [2] + W    # the relator  w a = b w

head("V1 - the relator, DERIVED not cited: w a = b w with w = a b^-1 a^-1 b")
Gu = {1: A, -1: A.inv(), 2: B_u, -2: B_u.inv()}
R = sp.simplify(ev(REL_L, Gu) - ev(REL_R, Gu))
print("  residual W*A - B*W over Z[u]:")
for i in range(2):
    print("   ", [sp.factor(sp.simplify(R[i, j])) for j in range(2)])
print(f"  every entry divisible by u^2+u+1?  "
      f"{all(sp.simplify(sp.rem(sp.Poly(sp.numer(sp.together(sp.simplify(R[i,j]))), u), sp.Poly(u**2+u+1, u)).as_expr()) == 0 for i in range(2) for j in range(2))}")
G = {1: A, -1: A.inv(), 2: B, -2: B.inv()}
print(f"  relator holds exactly at u = omega?  {sp.simplify(ev(REL_L, G) - ev(REL_R, G)).equals(Z2)}")

sA, sB = sym2(A), sym2(B)
S = {1: sA, -1: sA.inv(), 2: sB, -2: sB.inv()}
print(f"  and on Sym^2 (the geometric rep rho_1)? "
      f"{sp.simplify(ev(REL_L, S) - ev(REL_R, S)).equals(Z3)}")

# ---- the automorphism --------------------------------------------------------
head("V2 - rho_2 := transpose o reversal DESCENDS to pi_1(4_1)   [THE STRENGTHENING]")
print("  Transpose is an ANTI-homomorphism and word-reversal is order-reversing, so the")
print("  composite rho_2(w) := rho_1(w^R)^T IS a homomorphism of the free group. Whether it")
print("  descends to the KNOT group is a separate fact and is checked here, not assumed:")


def rho2(word):
    return ev(list(reversed(word)), S).T


desc = sp.simplify(rho2(REL_L) - rho2(REL_R)).equals(Z3)
print(f"    rho_2(w a) == rho_2(b w) ?   {desc}")
print("  => rho_2 is a genuine representation of pi_1(S^3 - 4_1), not merely of F_2.")
print("     (Consistent with 4_1 being invertible; verified at the rep, not cited.)")

# ---- the intertwiner ---------------------------------------------------------
head("V3 - the explicit intertwiner Q, and its derivation Q = S_iota * S_sd^-1")
Q = sp.Matrix([[0, 0, 1], [0, sp.Rational(1, 2), 0], [1, 0, 0]])
S_iota = sp.diag(1, -1, 1)
S_sd = sp.Matrix([[0, 0, 1], [0, -2, 0], [1, 0, 0]])
print(f"  S_iota * S_sd^-1 == Q ?                     {sp.simplify(S_iota*S_sd.inv() - Q).equals(Z3)}")
print(f"  generators:  Q rho_1(a)^T Q^-1 == rho_1(a) ? {sp.simplify(Q*sA.T*Q.inv() - sA).equals(Z3)}")
print(f"               Q rho_1(b)^T Q^-1 == rho_1(b) ? {sp.simplify(Q*sB.T*Q.inv() - sB).equals(Z3)}")
rng = random.Random(11)
allok = True
words = []
for _ in range(10):
    w = [rng.choice([1, -1, 2, -2]) for _ in range(rng.randint(3, 7))]
    ok = sp.simplify(Q * rho2(w) * Q.inv() - ev(w, S)).equals(Z3)
    words.append((w, ok))
    allok &= ok
print(f"  Q rho_2(w) Q^-1 == rho_1(w) on 10 random words?  {allok}")
print("  => rho_2 is conjugate to rho_1 by a SINGLE fixed Q. The banked theta-triviality")
print("     (a trace identity) is now realised by an explicit matrix.")

# ---- the three scoping facts -------------------------------------------------
head("V4 - SCOPE 1: Q implements transpose-WITH-REVERSAL, not transpose (abelian obstruction)")
prod = sp.simplify(sA * sB)
print(f"  Q Sym2(ab)^T Q^-1 == Sym2(ab) ?  {sp.simplify(Q*prod.T*Q.inv() - prod).equals(Z3)}")
print(f"  Q Sym2(ab)^T Q^-1 == Sym2(ba) ?  {sp.simplify(Q*prod.T*Q.inv() - sp.simplify(sB*sA)).equals(Z3)}")
print("  Proof that the group-level version CANNOT hold: if Q M^T Q^-1 = M for all M in a")
print("  group, then M N = Q (MN)^T Q^-1 = Q N^T M^T Q^-1 = N M, forcing the group abelian.")
print("  The figure-eight geometric rep is irreducible, hence non-abelian. So 'theta_T is")
print("  inner on Sym^2(SL(2))' is FALSE; 'rho o (transpose o reversal) ~ rho' is TRUE.")

head("V5 - SCOPE 2: Q is REP-DEPENDENT, not one universal intertwiner")
A2, B2 = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[1, 0], [3, 1]])
oka = sp.simplify(Q*sym2(A2).T*Q.inv() - sym2(A2)).equals(Z3)
okb = sp.simplify(Q*sym2(B2).T*Q.inv() - sym2(B2)).equals(Z3)
print(f"  same Q on a NON-Riley pair:  a:{oka}   b:{okb}")
print("  => Q is adapted to the normalised Riley family (A upper-unipotent, B lower).")
print("     Each rep is conjugate to its transpose-reversal by its OWN intertwiner.")

head("V6 - SCOPE 3: basis reconciliation of the self-duality form")
D = sp.diag(1, 2, 1)
S_cc = sp.Matrix([[0, 0, 2], [0, -1, 0], [2, 0, 0]])
print(f"  2 * D^-T S_sd D^-1 == disc-form [[0,0,2],[0,-1,0],[2,0,0]] ?  "
      f"{sp.simplify(2*(D.inv().T*S_sd*D.inv()) - S_cc).equals(Z3)}")
print("  The {x^2,xy,y^2} and {x^2,2xy,y^2} conventions differ by D=diag(1,2,1) and a scalar.")
print("  Same object; the earlier disagreement was a basis convention, not mathematics.")

head("CONSEQUENCE FOR RANK (the reason this does not disturb B766/B787)")
print("  rho_2 ~ rho_1 is exactly the banked theta-triviality on the character variety.")
print("  A trivial action contributes NO independent generator there. So this result")
print("  SHARPENS the mechanism and leaves both rank statements untouched:")
print("    B766 closing-axis rank 3  -- unaffected (different object: measurement choices)")
print("    B787 iota-driven rank 4   -- unaffected (iota is inversion, and its independence")
print("                                 was established on the closing axes, not here)")
