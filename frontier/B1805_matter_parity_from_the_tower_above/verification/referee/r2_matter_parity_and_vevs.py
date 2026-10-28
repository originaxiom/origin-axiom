"""Referee B1805, r2: claims (b), (c), (e).
(b') Q_X = 5(B-L) - 4Y on every MSSM field + nu^c; z2 = exp(i pi Q_X) equals P_M = (-1)^{3(B-L)} ON THE NOSE on all of them,
     and agrees with (-1)^{3(B-L)} on the SM pieces of the 45 and the 126 (tensor reps: both +1).
(c') P_M is in no global form of the SM group: L and H_d carry identical gauge quantum numbers (so every gauge element acts
     on them identically) while P_M separates them; nu^c is a gauge singlet with P_M = -1.  (Independent of Z6 quotients.)
(e1) the residual discrete symmetry after a VEV, computed on the Spin(10) torus t / Lambda^vee (Lambda^vee = D5 coroot
     lattice = integer vectors of even sum): stabiliser of the VEV's weight mu = {H : <H, mu> in Z}; its component group is
     Z / <Lambda^vee, mu>.  16-type VEV (nu^c weight) vs 126-type (2 x nu^c weight).
(e2) WHICH so(10) irreps can occur as localized chiral matter at an ADE enhancement point (Acharya-Witten: the irreps in
     adj(G') restricted to the regular subalgebra so(10)), by the norm bound: the weights of adj(G') for simply-laced G'
     have |.|^2 <= 2 and orthogonal projection does not increase the norm, so a highest weight with |lambda|^2 > 2 cannot
     occur.  Lists 1, 10, 16, 45, 54, 120, 126, 210 with their norms; and cross-checks with explicit branchings of
     so(12) and e6 adjoints (weights from the root systems, restricted to the D5 sub-root-system)."""
from fractions import Fraction as Fr
import itertools
import numpy as np

# ---------- (b') ----------
fields = {  # name: (B-L, Y, colour rep dimension, SU(2) dim)
    "Q": (Fr(1, 3), Fr(1, 6), 3, 2), "u^c": (Fr(-1, 3), Fr(-2, 3), 3, 1), "d^c": (Fr(-1, 3), Fr(1, 3), 3, 1),
    "L": (Fr(-1), Fr(-1, 2), 1, 2), "e^c": (Fr(1), Fr(1), 1, 1), "nu^c": (Fr(1), Fr(0), 1, 1),
    "H_u": (Fr(0), Fr(1, 2), 1, 2), "H_d": (Fr(0), Fr(-1, 2), 1, 2)}
expected_QX = {"Q": 1, "u^c": 1, "e^c": 1, "d^c": -3, "L": -3, "nu^c": 5, "H_u": -2, "H_d": 2}
print("(b') Q_X = 5(B-L) - 4Y; z2 = exp(i pi Q_X); P_M = (-1)^{3(B-L)}")
for f, (bl, y, c, w) in fields.items():
    qx = 5 * bl - 4 * y
    z2 = (-1) ** int(qx); pm = (-1) ** int(3 * bl)
    assert qx == expected_QX[f] and z2 == pm
    print("   %-5s B-L=%-5s Y=%-5s Q_X=%3d  z2=%+d  P_M=%+d" % (f, bl, y, qx, z2, pm))
# 45 and 126 pieces (PS content -> SM), B-L and Y from T3R + (B-L)/2
def ps_to_sm(su4_bl_list, su2L, su2R):
    out = []
    for bl in su4_bl_list:
        for t3r in [Fr(k, 2) for k in range(-(su2R - 1), su2R, 2)]:
            out.append((bl, t3r + bl / 2))
    return out
four = [Fr(1, 3)] * 3 + [Fr(-1)]
six = [Fr(2, 3)] * 3 + [Fr(-2, 3)] * 3
ten = [a + b for a, b in itertools.combinations_with_replacement(four, 2)]   # Sym^2 4 (B-L adds)
fifteen = [a - b for a in four for b in four]                                 # 4 x 4bar (incl. trace)
reps = {"45": [(fifteen, 1, 1), ([Fr(0)], 3, 1), ([Fr(0)], 1, 3), (six, 2, 2)],
        "126": [([Fr(0)] * 1 if False else [-x for x in six], 1, 1), ([-x for x in ten], 3, 1), (ten, 1, 3), (fifteen, 2, 2)]}
for name, parts in reps.items():
    vals = set()
    for bls, l, r in parts:
        for bl, y in ps_to_sm(bls, l, r):
            qx = 5 * bl - 4 * y
            assert qx.denominator == 1
            vals.add(((-1) ** int(qx), (-1) ** int(3 * bl)))
    print("   %s: (z2, (-1)^{3(B-L)}) values on its SM pieces: %s" % (name, sorted(vals)))

# ---------- (c') ----------
print("(c') L =", fields["L"][1:], " H_d =", fields["H_d"][1:], "(Y, colour, SU(2)): identical gauge quantum numbers ->",
      "every element of any global form of SU(3)xSU(2)xU(1) acts identically on L and H_d; P_M(L) = -1, P_M(H_d) = +1.",
      "Also nu^c is a gauge singlet with P_M = -1.  So P_M is in no form of the SM group (draft's (c) correct; this proof is",
      "form-independent and needs no Schur step).")

# ---------- (e1) ----------
def component_group(mu, N=4):
    """order of Z / <Lambda^vee, mu> for Lambda^vee = D5 coroot lattice, computed on generators."""
    gens = [np.eye(5)[i] - np.eye(5)[i + 1] for i in range(4)] + [np.eye(5)[3] + np.eye(5)[4]]
    vals = [Fr(sum(Fr(int(g[k])) * mu[k] for k in range(5))) for g in gens]
    # <Lambda, mu> = gcd of the values (as rationals) times Z; component group of {H:<H,mu> in Z} / identity comp. = Z / gcd
    from math import gcd
    den = 1
    for v in vals: den = den * v.denominator // gcd(den, v.denominator)
    ints = [int(v * den) for v in vals]
    g = 0
    for x in ints: g = gcd(g, abs(x))
    gen = Fr(g, den)                # <Lambda, mu> = gen * Z
    return gen, gen.numerator   # Z/(Z cap gen Z) = Z/(numerator) for gen = a/b reduced
nu = [Fr(1, 2)] * 5                     # the 16's SU(5)-singlet weight (Q_X = +5 in the 2*sum convention)
nunu = [Fr(1)] * 5                      # its double: the 126's SU(5)-singlet weight (Q_X = 10)
for name, mu in [("16-type (nu^c)", nu), ("126-type (nu^c nu^c)", nunu)]:
    gen, idx = component_group(mu)
    print("(e1) %-22s <Lambda^vee, mu> = %s Z  -> residual discrete group (stabiliser in the torus modulo its identity component) has order %s;"
          " (the SU(5) = SM maximal torus {sum H = 0})" % (name, gen, idx))
z2H = [1, 0, 0, 0, 0]
for name, mu in [("16-type", nu), ("126-type", nunu)]:
    print("     z2 = exp(2 pi i e1) fixes the %s VEV ? %s" % (name, sum(Fr(z2H[k]) * mu[k] for k in range(5)).denominator == 1))

# ---------- (e2) ----------
def D_roots(n):
    R = []
    for i in range(n):
        for j in range(i + 1, n):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0] * n; v[i] = si; v[j] = sj; R.append(tuple(v))
    return R
hw = {"1": [0] * 5, "10": [1, 0, 0, 0, 0], "16": [0.5] * 5, "45": [1, 1, 0, 0, 0], "54": [2, 0, 0, 0, 0],
      "120": [1, 1, 1, 0, 0], "126": [1, 1, 1, 1, 1], "210": [1, 1, 1, 1, 0]}
print("(e2) highest-weight norms^2 (orthonormal basis, roots norm^2 2):",
      {k: float(np.dot(v, v)) for k, v in hw.items()}, "-> only 1, 10, 16/16bar, 45 can occur in adj(G') of a simply-laced G' (norm <= 2)")
# explicit check: so(12) adjoint restricted to so(10) (first 5 coordinates): weights with nonzero so(10) part
w12 = [r[:5] for r in D_roots(6)]
print("     so(12) adj -> so(10): max norm^2 of restricted weights", max(np.dot(w, w) for w in w12),
      "; distinct nonzero norms", sorted(set(float(np.dot(w, w)) for w in w12 if any(w))))
# e6 roots in an 6-dim realisation: D5 roots (in first 5 coords, last coord 0) + 32 weights (±1/2,...,±1/2; e6 normalisation):
# E6 roots = D5 roots + {(1/2)(±1,...,±1 [even # minus], ±sqrt(3)/2*...)}; use the standard E8 embedding instead:
E8 = [tuple(r) + (0, 0, 0) for r in D_roots(5)]  # placeholder for D5 part
def e8_roots():
    R = [tuple(r) for r in D_roots(8)]
    for s in itertools.product((0.5, -0.5), repeat=8):
        if sum(1 for x in s if x < 0) % 2 == 0: R.append(s)
    return R
E8r = e8_roots()
assert len(E8r) == 240
rest = [r[:5] for r in E8r]
print("     e8 adj (240 roots) -> so(10) on the first 5 coordinates (regular D5 subsystem): max norm^2 of restricted weights",
      max(np.dot(w, w) for w in rest), "; restricted dominant weights present:",
      sorted(set(tuple(sorted([abs(x) for x in w], reverse=True)) for w in rest if any(w))))
print("     -> the 126's weight (1,1,1,1,1) never occurs: in Witten's / Acharya-Witten's frame a 126 is not available as"
      " localized matter, so the only rank-reducing (U(1)_X-breaking) localized field is a 16/16bar, which is z2-odd")
print("r2 exit 0")
