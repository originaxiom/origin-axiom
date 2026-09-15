#!/usr/bin/env python3
"""MEMO-106 CELL (repofeq verification of B1195/B1196 + one bench
cross-link): THE ONE POLYNOMIAL — cc's item-4 law (the relational
bit's classification is governed by kappa, with kappa - 2 = omega^2)
and cc's item-7 claim (epsilon is CONJUGATION-INVARIANT: the
relational bit is selector-free) verified independently on this
bench; and a cross-link cc's report does not name, found and proved
here: cc's item-1 SADDLE EQUATION u^2 + u + 1 = 0 has as its roots
EXACTLY kappa - 2 and its conjugate — items 1 and 4 are one invariant
— and the SAME polynomial Phi_3 is the boundary lattice's
complex-structure equation (memo 104's M^2 + M + I = 0).  One
polynomial, three faces: the partition function's saddle, the
relational bit's obstruction, the boundary's Eisenstein structure.

PREREGISTERED CHECKS (each two-outcome: holds exactly / banks a
discrepancy against the relay):
  K1: kappa - 2 = omega^2 in the lane's exact pair arithmetic
      (omega^2 = omega - 1; kappa = 1 + omega).
  K2: Phi_3(kappa - 2) = 0 exactly — the saddle equation's roots are
      {kappa - 2, conj(kappa - 2)} (both roots verified).
  K3: memo 104's M = Coxeter^4 satisfies the same Phi_3 (rebuilt from
      scratch, one assert).
  E1: THE TRANSPORT THEOREM (epsilon selector-free): for ANY
      G in GL2(Z), Y realizes the simultaneous mirror of (P, Q) iff
      G Y G^-1 realizes it for (G P G^-1, G Q G^-1), with det
      preserved — so the realizer det SET is conjugation-invariant.
      Verified symbolically on the banked crown pair (A, M1) for five
      explicit conjugators of both determinant signs, PLUS independent
      brute-force realizer searches on the conjugated pairs
      (single-signed {-1} every time), PLUS the control (A, A)
      keeping both signs under conjugation.
Gate 5 untouched (exact algebra only).
"""
from fractions import Fraction as Fr
import sympy as sp

# ---- K1/K2: pair arithmetic over Q(omega), omega^2 = omega - 1
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
ONE = (Fr(1), Fr(0)); W = (Fr(0), Fr(1))
kappa = padd(ONE, W)                        # kappa = 1 + omega
w2 = pmul(W, W)                             # omega^2
km2 = padd(kappa, (Fr(-2), Fr(0)))          # kappa - 2
assert km2 == w2 == (Fr(-1), Fr(1))         # both equal omega - 1
print("K1: kappa - 2 = omega^2 = omega - 1 EXACTLY (cc's item-4 law, re-derived).")

phi3 = padd(padd(pmul(km2, km2), km2), ONE)  # (kappa-2)^2 + (kappa-2) + 1
assert phi3 == (Fr(0), Fr(0))
# the conjugate root: conj(omega^2) = conj(omega) - 1 = (1 - omega) - 1 = -omega
conj = (Fr(0), Fr(-1))
assert padd(padd(pmul(conj, conj), conj), ONE) == (Fr(0), Fr(0))
print("K2: Phi_3(kappa - 2) = 0 AND Phi_3(conj) = 0 — cc's SADDLE EQUATION")
print("    u^2 + u + 1 = 0 has roots EXACTLY {kappa - 2, its conjugate}:")
print("    the partition function's saddle IS the relational obstruction —")
print("    items 1 and 4 of the disposition are ONE invariant (bench cross-link).")

# ---- K3: memo 104's M satisfies the same Phi_3 (rebuilt)
G = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0], [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0], [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1], [ 0,  0,  0,  0, -1,  2]])
c = sp.eye(6)
for i in range(6):
    S = sp.eye(6)
    for j in range(6):
        S[i, j] -= G[i, j]
    c = c * S
M = c**4
assert (M**2 + M + sp.eye(6)) == sp.zeros(6, 6)
print("K3: memo 104's boundary complex structure M = Coxeter^4 satisfies the SAME")
print("    Phi_3 (M^2 + M + I = 0, rebuilt from scratch) — one polynomial, three")
print("    faces: saddle / relational obstruction / boundary Eisenstein structure.")

# ---- E1: epsilon is selector-free (conjugation-invariant)
A = sp.Matrix([[2, 1], [1, 1]])
M1 = sp.Matrix([[2, 3], [1, 2]])
X0 = sp.Matrix([[2, -3], [1, -2]])
assert X0*A*X0.inv() == A.inv() and X0*M1*X0.inv() == M1.inv() and X0.det() == -1

def realizer_dets(P, Q, B):
    """fast integer box search for Y with Y P Y^-1 = P^-1, Y Q Y^-1 = Q^-1,
    det Y = +-1 (as Y P = P^-1 Y etc.)."""
    Pi, Qi = P.inv(), Q.inv()
    Pt = [[int(P[i, j]) for j in range(2)] for i in range(2)]
    Pit = [[int(Pi[i, j]) for j in range(2)] for i in range(2)]
    Qt = [[int(Q[i, j]) for j in range(2)] for i in range(2)]
    Qit = [[int(Qi[i, j]) for j in range(2)] for i in range(2)]
    def mm(X, Y2):
        return [[X[0][0]*Y2[0][0] + X[0][1]*Y2[1][0], X[0][0]*Y2[0][1] + X[0][1]*Y2[1][1]],
                [X[1][0]*Y2[0][0] + X[1][1]*Y2[1][0], X[1][0]*Y2[0][1] + X[1][1]*Y2[1][1]]]
    dets = set()
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            for c2 in range(-B, B + 1):
                for d in range(-B, B + 1):
                    det = a*d - b*c2
                    if det not in (1, -1):
                        continue
                    Y = [[a, b], [c2, d]]
                    if mm(Y, Pt) == mm(Pit, Y) and mm(Y, Qt) == mm(Qit, Y):
                        dets.add(det)
    return dets

CONJ = [sp.Matrix(m) for m in ([[1, 1], [0, 1]], [[0, 1], [1, 0]],
                               [[2, 1], [1, 1]], [[1, 0], [3, 1]],
                               [[1, 0], [0, -1]])]
for Gm in CONJ:
    assert Gm.det() in (1, -1)
    P, Q = Gm*A*Gm.inv(), Gm*M1*Gm.inv()
    Y = Gm*X0*Gm.inv()
    # transport: Y realizes the conjugated pair, same det, stays integral
    assert Y*P*Y.inv() == P.inv() and Y*Q*Y.inv() == Q.inv() and Y.det() == -1
    assert all(x == int(x) for x in Y)
    # the complete argument, transported: [P, Q] != 0 and P has irrational
    # eigenvalues (charpoly x^2-3x+1 preserved by conjugation) => joint
    # centralizer {+-I} => realizer set is EXACTLY {+-Y}: single-signed -1.
    assert P*Q - Q*P != sp.zeros(2, 2)
    assert sp.expand(P.charpoly(sp.symbols('x')).as_expr()
                     - (sp.symbols('x')**2 - 3*sp.symbols('x') + 1)) == 0
    # belt-and-braces: independent box search wherever the transported
    # realizer fits a tractable box (search radius = |Y|_max + 2, capped 12)
    Bneed = max(abs(int(x)) for x in Y) + 2
    if Bneed <= 12:
        d = realizer_dets(P, Q, Bneed)
        assert d == {-1}, (Gm, d)
        note = f"box search (B={Bneed}) returns {{-1}}"
    else:
        note = f"realizer entries reach {Bneed-2}: search skipped, exact argument stands"
    dAA = realizer_dets(Gm*A*Gm.inv(), Gm*A*Gm.inv(), 6)
    assert dAA == {1, -1}
    print(f"    conjugator {Gm.tolist()} (det {int(Gm.det())}): transported realizer "
          f"det -1 verified; {note}; (A,A) control keeps both signs")
print("E1: SELECTOR-FREE CONFIRMED — for five conjugators of both det signs:")
print("    G X0 G^-1 realizes the conjugated pair with det -1, and the complete")
print("    argument transports (centralizer {+-I} via [P,Q] != 0 + irrational")
print("    spectrum => realizer set EXACTLY {+-G X0 G^-1}); independent box")
print("    searches, where tractable, return single-signed {-1}.  epsilon(A, M1)")
print("    = -1 is a property of the PAIR'S ORBIT, not of any chosen frame —")
print("    cc's item-7 claim independently verified: the observer's one bit")
print("    needs no selection act.")

print("""
VERDICT: B1195's kappa law and B1196's selector-freedom both REPRODUCE
exactly on this bench, and the bench adds one cross-link the relay did
not name: the saddle equation, the relational obstruction, and the
boundary lattice's complex structure are ONE polynomial (Phi_3), whose
roots are kappa - 2 and its conjugate.  The founding Fricke invariant
governs all three.  Gate 5 untouched.""")
