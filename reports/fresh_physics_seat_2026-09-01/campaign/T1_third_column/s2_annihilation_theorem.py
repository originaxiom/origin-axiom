"""T1 step 2 -- the EXACT annihilation<->invariance equivalence over Q(zeta_12), sympy.

Object: the selected down block T[i,j,k], i = Q family (3), j = d^c family (3),
k in B_0 = C(3 conn) + lift-of-T(1 tail)  -- the (3,4,1) sequence of s1.

Splitting convention (matches B1232/verify_quotient_lemma.py): a section s_t: T -> V
sends the tail generator to  h(t) = bhat_2 + t_1 c_1 + t_2 c_2 + t_3 c_3,  t in K^3.
The observable at splitting t is the 3x3 family matrix  Y[i,j](t) = T[i,j, h(t)].

THEOREM (proved symbolically below, valid over any field, hence over Q(zeta_12)):
  Y[i,j](t) - Y[i,j](0) = sum_k t_k T[i,j,conn_k]  identically, therefore
  (spread over ALL splittings == 0)  <=>  (all 27 Higgs-connecting entries == 0)
                                     <=>  (Y annihilates C and factors uniquely through T).
Both directions are exhibited: the zero branch exactly on a genuine Q(zeta_12) instance,
the nonzero branch by a single-entry perturbation (MB12 bite at the exact level).
"""
import sympy as sp

# ---------- symbolic generic tensor: 3 x 3 x 4, entries free symbols ----------
T = [[[sp.Symbol(f"T_{i}{j}{k}") for k in range(4)] for j in range(3)] for i in range(3)]
t = sp.symbols("t1 t2 t3")   # the splitting coordinates (the P^3 = affine chart coordinates)

def Y(i, j, tv):
    # Higgs leg h(t) = e_tail + sum t_k e_conn_k ; conn indices k=0,1,2 ; tail index k=3
    return T[i][j][3] + sum(tv[m] * T[i][j][m] for m in range(3))

# (1) the exact linearity identity: Y(t) - Y(0) = sum t_k T[i,j,k_conn]
for i in range(3):
    for j in range(3):
        diff = sp.expand(Y(i, j, t) - Y(i, j, (0, 0, 0)) - sum(t[m] * T[i][j][m] for m in range(3)))
        assert diff == 0
print("[1] EXACT IDENTITY: Y[i,j](t) - Y[i,j](0) = sum_k t_k T[i,j,conn_k]  (all 9 family entries)")

# (2) => equivalence: t-independence for ALL t  <=>  the 27 conn entries vanish.
#     forward: if all T[i,j,conn_k]=0 then Y(t)=Y(0) identically (constant, exact);
#     backward: if some T[i0,j0,conn_k0] != 0 then d/dt_k0 Y[i0,j0] = T[i0,j0,conn_k0] != 0.
grad_nonzero = sp.diff(Y(0, 0, t), t[0])
assert grad_nonzero == T[0][0][0] != 0   # a free symbol is not the zero polynomial
print("[2] EQUIVALENCE: spread==0 over the splitting family  <=>  27 Higgs-connecting entries all 0;")
print("    a SINGLE nonzero conn entry already makes the observable depend on t (derivative = that entry).")

# (3) uniqueness of the factorisation through T when Y annihilates C:
#     Ybar[i,j] := T[i,j,tail] satisfies Y = Ybar o proj_T, and any factorisation agrees on
#     proj_T's image, which is all of T (proj_T surjective) => unique.
print("[3] UNIQUENESS: Ybar[i,j] = T[i,j,tail]; proj_T surjective => the factorisation is unique.")

# ---------- (4) the zero branch EXACTLY over Q(zeta_12) ----------
z = sp.Symbol("z")                      # z = zeta_12, minimal polynomial z^4 - z^2 + 1
MIN = sp.Poly(z**4 - z**2 + 1, z)
def red(e):                             # reduce a polynomial expression mod the minimal polynomial
    return sp.rem(sp.Poly(sp.expand(e), z), MIN).as_expr()

# a genuine annihilating instance: conn entries 0, tail entries nontrivial Q(zeta_12) numbers
tail_vals = [[1 + z, z**3 - 2, sp.Rational(3, 7) * z**2],
             [z - z**3, 5, 1 - z**2],
             [z**2 + z, -z, sp.Rational(1, 2)]]
subs_ann = {T[i][j][3]: tail_vals[i][j] for i in range(3) for j in range(3)}
subs_ann.update({T[i][j][m]: 0 for i in range(3) for j in range(3) for m in range(3)})

# 25 exact rational splitting points, including large and negative coordinates
pts = [(sp.Rational(p, q), sp.Rational(-q, p + 1), sp.Rational(p * q, 3)) for p in range(1, 6) for q in range(1, 6)]
max_dev = 0
for i in range(3):
    for j in range(3):
        base = red(Y(i, j, (0, 0, 0)).subs(subs_ann))
        for pt in pts:
            dev = red(Y(i, j, pt).subs(subs_ann) - base)
            assert dev == 0, f"nonzero deviation at {pt}"
print(f"[4] ZERO BRANCH (exact, Q(zeta_12)): 9 family entries x {len(pts)} exact splittings ->")
print("    deviation from the t=0 value is IDENTICALLY 0 after reduction mod z^4 - z^2 + 1. Spread = 0 exactly.")

# ---------- (5) MB12 bite at the exact level: one conn entry = z (a unit) ----------
subs_bite = dict(subs_ann); subs_bite[T[0][0][0]] = z
dev = red(Y(0, 0, (1, 0, 0)).subs(subs_bite) - Y(0, 0, (0, 0, 0)).subs(subs_bite))
assert dev == z != 0
print("[5] BITE (exact): setting the single conn entry T[0,0,conn_1] = zeta_12 makes the deviation")
print(f"    at splitting t=(1,0,0) equal zeta_12 itself (nonzero unit). The criterion FAILS both ways.")

print("\nS2 VERDICT: over Q(zeta_12), P^3-invisibility of the down observable is EXACTLY equivalent")
print("            to the vanishing of the 27 typed Higgs-connecting entries -- proved, with bite.")
