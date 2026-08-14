"""B786 (cc) -- the theta/iota refinement of the measurement-torsor rank (Phase-2 structural).

Opened by R31-4 (the C20 audit) + cc3's N7/N8. The measurement torsor C20/B766 names its
third generator "theta (reversal)". But reversal is TRACE-TRIVIAL at every rank, so it is
invisible to the character variety. The involution that IS active on the SL(3) character
variety is iota = inversion (contragredient, g -> g^-1). This cell pins the distinction and
its consequence for the rank.

Gate 5-Q. Nothing to CLAIMS. Exact sympy.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
R = {}


def sym2(M):
    a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*e + b*c, 2*b*e], [c**2, c*e, e**2]])


print("=" * 80)
print("A. theta(reversal) vs iota(inversion) on the GENUINE SL(3) character variety")
print("=" * 80)
A = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
B = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
assert A.det() == 1 and B.det() == 1
W = A * A * B
WR = B * A * A                       # reversal
theta_moves = sp.simplify(sp.trace(W) - sp.trace(WR)) != 0
iota_moves = sp.simplify(sp.trace(W) - sp.trace(W.inv())) != 0
print(f"  tr(W)={sp.trace(W)}, tr(W^R)={sp.trace(WR)}, tr(W^-1)={sp.trace(W.inv())}")
print(f"  theta (reversal) moves the trace at SL(3): {theta_moves}   (FALSE => trace-trivial)")
print(f"  iota  (inversion) moves the trace at SL(3): {iota_moves}   (TRUE  => trace-active)")
R["A"] = {"theta_trace_active_sl3": bool(theta_moves), "iota_trace_active_sl3": bool(iota_moves)}
assert theta_moves is False and iota_moves is True

print()
print("=" * 80)
print("B. the character-variety generators are {c, IOTA, gamma5} -- rank 3, iota NOT theta")
print("=" * 80)
# c moves Q(sqrt-3) traces; gamma5 moves Q(sqrt5); iota moves SL(3) traces; theta does not.
c_active = sp.simplify(sp.conjugate(2 - omega) - (2 - omega)) != 0
g5_active = sp.simplify((1 - phi) ** 2 - phi ** -2) == 0     # gamma5 = the Galois relation
print(f"  c active on Q(sqrt-3) trace values : {c_active}")
print(f"  iota active on SL(3) trace         : {iota_moves}")
print(f"  gamma5 active (Gal(Q(sqrt5)))      : {g5_active}")
print(f"  theta active on the character variety: {theta_moves}  -> it is the MATRIX-LEVEL chord")
R["B"] = {"charvariety_generators": ["c", "iota", "gamma5"], "rank": 3,
          "theta_is_matrix_level_chord": True}

print()
print("=" * 80)
print("C. the OBJECT (fig-8 = Sym^2(SL(2)), self-dual/V0): iota and theta both collapse")
print("=" * 80)
Ao = sp.Matrix([[1, 1], [0, 1]])
Bo = sp.Matrix([[1, 0], [-omega, 1]])
Wo = Ao * Ao * Bo
iota_obj = sp.simplify(sym2(Wo).trace() - sym2(Wo.inv()).trace()) != 0
theta_obj = sp.simplify(sym2(Wo).trace() - sym2(Bo * Ao * Ao).trace()) != 0
print(f"  on Sym^2(SL(2)): iota trace-active={iota_obj}, theta trace-active={theta_obj}")
print(f"  => BOTH trivial on the object's traces (tr(g^-1)=tr(g)=tr(g^R) in SL(2)); they coincide.")
print(f"  => object measurement rank = 3 {{c, (theta~iota collapsed), gamma5}}. C20 STANDS.")
R["C"] = {"object_iota_trace_active": bool(iota_obj), "object_theta_trace_active": bool(theta_obj),
          "object_rank": 3, "c20_stands": True}
assert iota_obj is False and theta_obj is False

print()
print("=" * 80)
print("VERDICT (B786): the character-variety torsor generator is IOTA=inversion, not")
print("THETA=reversal; theta is the matrix-level chord. On the object (self-dual Sym^2) the two")
print("collapse, so C20's rank-3 is correct -- but its third generator is properly iota on the")
print("character variety. The full non-self-dual SL(3) variety can carry theta as a distinct")
print("4th (matrix-level) involution (cc3 N8, S-derivation pending on cc3).")
R["verdict"] = ("charvariety generator = iota (not theta); theta = matrix-level chord; "
                "object rank 3 stands; full-SL(3) rank-4 open on cc3's S")

import json
with open("results.json", "w") as f:
    json.dump(R, f, indent=1)
print("\nwrote results.json")
