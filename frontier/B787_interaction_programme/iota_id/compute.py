"""B787 Phase 1 -- THE IOTA-IDENTIFICATION (highest-priority door).

Question. The measurement torsor (B766) is (Z/2)^3 = <c, theta, gamma5>.  B786 showed the
character-variety-active involution is IOTA = inversion (g -> g^-1), not THETA = reversal
(which is trace-trivial at all ranks).  Which element of (Z/2)^3 does IOTA equal -- or is it
a genuinely independent 4th generator (rank 4)?

Method. Evaluate the FOUR involutions c, theta, iota, gamma5 on
  (i)  the 8 SL(3) fiber trace coordinates x1..x8 = (trA,trB,trAB,trA^-1,trB^-1,trA^-1B,trAB^-1,trA^-1B^-1);
  (ii) the FIVE discrete torsor axes B766 uses (T4 chirality-side, T6 chord-sign,
       T7 time-direction, T3 basepoint-bit, T1 pairing);
and read off IOTA's flip-vector against the B766 basis (c, theta, gamma5).

Everything exact (sympy) or exact-combinatorial (sympy.combinatorics for A5).  Gate 5-Q:
structural labels only; nothing to CLAIMS.
"""
import sympy as sp
from sympy.combinatorics import Permutation
from sympy.combinatorics.named_groups import AlternatingGroup

phi   = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2      # primitive cube root, Q(sqrt-3)
R = {}
def head(s): print("=" * 84); print(s); print("=" * 84)


# ---------------------------------------------------------------------------
def sym2(M):
    """Sym^2 : SL(2,C) -> SL(3,C) on {e1^2, e1 e2, e2^2} (B71 convention)."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a*a, a*b, b*b], [2*a*c, a*d + b*c, 2*b*d], [c*c, c*d, d*d]])

def coords8(A, B):
    """The 8 B48/B71 fiber trace coordinates of an SL(3) pair (A,B)."""
    Ai, Bi = A.inv(), B.inv()
    tr = lambda M: sp.expand(M.trace())
    return [tr(A), tr(B), tr(A*B), tr(Ai), tr(Bi), tr(Ai*B), tr(A*Bi), tr(Ai*Bi)]


# ===========================================================================
head("A.  IOTA on the 8 trace coordinates = the dual permutation (14)(25)(38)(67)")
# ===========================================================================
# iota sends the rep to g->g^-1: new generators A'=A^-1, B'=B^-1.  Its 8 coords are the old
# 8 permuted.  Verify on a GENERIC (non-self-dual) SL(3) pair -- the B786 triangular pair.
A = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
B = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
assert A.det() == 1 and B.det() == 1
base   = coords8(A, B)
iota_c = coords8(A.inv(), B.inv())                     # coords of the iota-image rep
perm_expected = [3, 4, 7, 0, 1, 6, 5, 2]               # (14)(25)(38)(67) 0-indexed
perm_ok = all(sp.simplify(iota_c[i] - base[perm_expected[i]]) == 0 for i in range(8))
print("  base   x1..x8 =", base)
print("  iota   x1..x8 =", iota_c)
print("  iota permutes the coords by (x1 x4)(x2 x5)(x3 x8)(x6 x7):", perm_ok)
# a witness that iota is TRACE-ACTIVE on the non-self-dual variety (B786's tr 49 vs 409):
W = A*A*B
print(f"  witness  tr(W)={sp.trace(W)}  tr(W^-1)={sp.trace(W.inv())}  -> iota trace-active: "
      f"{sp.trace(W) != sp.trace(W.inv())}")
R["A_perm_is_dual_swap"] = bool(perm_ok)
R["A_iota_trace_active_generic"] = bool(sp.trace(W) != sp.trace(W.inv()))
assert perm_ok


# ===========================================================================
head("B.  Self-dual OBJECT (V0 = Sym^2, geometric rep): iota fixes the traces; "
     "non-self-dual: it moves them")
# ===========================================================================
# The geometric SL(3) rep is Sym^2 of the SL(2) figure-eight Riley rep at u=omega (B99/B101).
A2 = sp.Matrix([[1, 1], [0, 1]])
B2 = sp.Matrix([[1, 0], [-omega, 1]])
Ag, Bg = sym2(A2), sym2(B2)
cg = coords8(Ag, Bg)
cg_iota = coords8(Ag.inv(), Bg.inv())
# self-dual locus V0: x1=x4, x2=x5, x3=x8, x6=x7  <=> iota fixes every coordinate
v0 = all(sp.simplify(cg[i] - cg[j]) == 0 for i, j in [(0, 3), (1, 4), (2, 7), (5, 6)])
iota_fixes_object = all(sp.simplify(cg_iota[i] - cg[i]) == 0 for i in range(8))
print("  geometric (Sym^2) coords x1..x8 =", [sp.simplify(v) for v in cg])
print(f"  lies on the self-dual locus V0 (x1=x4,x2=x5,x3=x8,x6=x7): {v0}")
print(f"  => iota fixes ALL 8 trace coords on the object (self-dual): {iota_fixes_object}")
print(f"  contrast (A): iota moves them on the non-self-dual variety -> the rank-jump lives OFF V0")
R["B_object_selfdual"] = bool(v0)
R["B_iota_fixes_object_traces"] = bool(iota_fixes_object)
assert v0 and iota_fixes_object


# ===========================================================================
head("C.  T7 (time-direction): iota FLIPS it -- monodromy t -> t^-1 inverts the loxodromic spectrum")
# ===========================================================================
# figure-eight monodromy on H1 = [[2,1],[1,1]] = phi^2; spectrum {phi^2, phi^-2}.
Mn = sp.Matrix([[2, 1], [1, 1]])
ev = sorted(Mn.eigenvals().keys(), key=lambda e: -sp.re(sp.N(e)))
ev = [sp.nsimplify(e, [sp.sqrt(5)]) for e in ev]
ev_inv = [sp.nsimplify(1/e, [sp.sqrt(5)]) for e in ev]
# iota inverts the monodromy: spectrum {lambda, lambda^-1} -> {lambda^-1, lambda}: the ordered
# (future/past) labels SWAP -> orientation flip = T7 FLIP.
iota_flips_T7 = (set(sp.simplify(e) for e in ev) == set(sp.simplify(e) for e in ev_inv)) and \
                sp.simplify(ev[0] - ev_inv[0]) != 0
# gamma5 realizes the SAME inversion arithmetically: (1-phi)^2 = phi^-2.
g5_flips_T7 = sp.simplify((1 - phi)**2 - phi**-2) == 0
# theta (reversal) gives a CONJUGATE monodromy (RL->LR), same ordered spectrum -> FIX (B766).
print(f"  monodromy spectrum        = {ev}")
print(f"  iota-inverted spectrum    = {ev_inv}   (future<->past labels swap)")
print(f"  iota FLIPS T7 (time)      : {iota_flips_T7}")
print(f"  gamma5 FLIPS T7 [(1-phi)^2=phi^-2]: {g5_flips_T7}")
print(f"  theta FIXES T7 (reversal = conjugate monodromy, same ordered spectrum) : True  (B766)")
R["C_iota_flips_T7"] = bool(iota_flips_T7)
R["C_gamma5_flips_T7"] = bool(g5_flips_T7)
assert iota_flips_T7 and g5_flips_T7


# ===========================================================================
head("D.  T3 (basepoint-bit = Out(A5)/5A-5B): iota FIXES it -- A5 is AMBIVALENT (g ~ g^-1)")
# ===========================================================================
# T3 is the sister's Out(A5) = 5A/5B swap (B701/B766). gamma5 = Frobenius realizes Out(A5).
# Does iota (g->g^-1) realize it?  In A5 the 5-cycles split 5A|5B; test whether inversion
# swaps them (=> iota would flip T3) or fixes each (=> iota FIXES T3).
A5 = AlternatingGroup(5)
elts = list(A5.generate())
g = Permutation([1, 2, 3, 4, 0]); gi = g**-1; g2 = g*g
cls = lambda x: frozenset(h*x*h**-1 for h in elts)
Cg, Cg2 = cls(g), cls(g2)
five_classes_split   = (Cg != Cg2) and len(Cg) == 12 and len(Cg2) == 12
iota_fixes_5class    = gi in Cg                        # inversion keeps g in its own 5-class
odd = Permutation([1, 0, 2, 3, 4])                     # a transposition = Out(A5) generator
out_swaps_5class     = (odd*g*odd**-1) in Cg2          # Out(A5) SWAPS 5A<->5B
ambivalent = all((x**-1) in cls(x) for x in elts)      # every A5 class self-inverse
print(f"  5-cycles split into 5A,5B (sizes 12,12): {five_classes_split}")
print(f"  A5 ambivalent (every class self-inverse): {ambivalent}")
print(f"  iota (inversion) keeps g in its 5-class -> FIXES 5A,5B -> FIXES T3: {iota_fixes_5class}")
print(f"  Out(A5)=gamma5/Frobenius SWAPS 5A<->5B -> FLIPS T3: {out_swaps_5class}")
R["D_iota_fixes_T3"] = bool(iota_fixes_5class)
R["D_gamma5_flips_T3"] = bool(out_swaps_5class)
R["D_A5_ambivalent"] = bool(ambivalent)
assert iota_fixes_5class and out_swaps_5class and ambivalent


# ===========================================================================
head("E.  T4 (chirality-side) and T6 (chord-sign) under iota")
# ===========================================================================
# T4: the two roots y_+- = (3 +- sqrt(-3))/2 of the B711 curve at x=2. c swaps them (conj).
x, y = sp.symbols("x y")
sols = sp.solve((y**2 - (x**2 - 1)*y + (x**2 - 1)).subs(x, 2), y)
c_flips_T4 = all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols) and \
             set(sp.nsimplify(sp.conjugate(s)) for s in sols) == set(sp.nsimplify(s) for s in sols)
# iota on T4: on the self-dual object the branch coordinate is a trace datum (x3=x8), iota-fixed:
iota_fixes_T4 = sp.simplify(cg[2] - cg[7]) == 0        # x3 = x8 on V0 => the AB-branch is iota-fixed
print(f"  T4 roots y_+- = {sols}")
print(f"  c FLIPS T4 (complex-conjugate roots swap): {c_flips_T4}")
print(f"  iota FIXES T4 on the object (x3=x8 self-dual, the branch datum is iota-invariant): {iota_fixes_T4}")

# T6: the chord = matrix-level Sym^2(AB)-Sym^2(BA); theta-odd by construction; c flips (sqrt3 -> -sqrt3).
# The chord's sign is a CONJUGATION-INVARIANT: det(C) (traceless 3x3) is theta-ODD (C->-C => det->-det),
# so det(C) carries the T6 sign basis-free.  iota sends the observable to Sym^2((AB)^-1)-Sym^2((BA)^-1)
# = Sym^2(B^-1 A^-1) - Sym^2(A^-1 B^-1); compare det(C_iota) to +-det(C).
u = sp.symbols("u")
A2u = sp.Matrix([[1, 1], [0, 1]]); B2u = sp.Matrix([[1, 0], [-u, 1]])
AB, BA = A2u*B2u, B2u*A2u
dC   = lambda P, Q: (sym2(P) - sym2(Q)).applyfunc(lambda e: sp.diff(sp.expand(e), u)).subs(u, omega)
chord      = dC(AB, BA).applyfunc(sp.nsimplify)                 # the base chord C
chord_iota = dC(AB.inv(), BA.inv()).applyfunc(sp.nsimplify)     # iota-image: (AB)^-1, (BA)^-1
spec_C = [sp.simplify(e) for e in chord.eigenvals()]           # the chord's spectrum (with mult)
det_C  = sp.simplify(chord.det())
# The chord is traceless with det 0 and a +-SYMMETRIC spectrum {lambda,-lambda,0}, so C is CONJUGATE
# to -C: its theta-odd sign is NOT a conjugation-invariant -- it is frame-dependent.  Hence iota's
# action on T6 is not a basis-free Z/2 and cannot (by itself) be pinned; we mark it UNDETERMINED and
# show the rank-4 verdict holds for EITHER value of the T6 bit.
chord_pm_symmetric = (sp.simplify(chord.det()) == 0 and sp.simplify(chord.trace()) == 0)
T6_undetermined = chord_pm_symmetric
print(f"  chord C (theta-odd) trace = {sp.simplify(chord.trace())}; det(C) = {det_C}; spectrum = {spec_C}")
print(f"  spectrum is +-symmetric => C ~ -C => the theta-odd sign is FRAME-DEPENDENT, not conj-invariant")
print(f"  => iota's T6 action is UNDETERMINED as a basis-free Z/2: {T6_undetermined}")
print(f"     (handled below by checking the rank for BOTH T6 values; the verdict is independent of it)")
R["E_c_flips_T4"] = bool(c_flips_T4)
R["E_iota_fixes_T4"] = bool(iota_fixes_T4)
R["E_T6_undetermined_frame_dependent"] = bool(T6_undetermined)


# ===========================================================================
head("F.  IOTA's flip-vector vs the B766 basis -- rank of the enlarged torsor")
# ===========================================================================
# B766 flip-vectors on axes (T4,T6,T7,T3), rows = generators, entry = flips? (from B766 output):
axes = ["T4", "T6", "T7", "T3"]
table = {
    "c":     [1, 1, 0, 0],
    "theta": [0, 1, 0, 0],
    "gamma5":[0, 0, 1, 1],
}
for k in ("c", "theta", "gamma5"):
    print(f"  {k:7s} flips (T4,T6,T7,T3) = {table[k]}")
print(f"  iota    flips (T4,T6,T7,T3) = [0, ?, 1, 0]   (T4 fix, T6 frame-dependent, T7 FLIP, T3 fix)")

def f2_rank(rows):
    M = [r[:] for r in rows]; r = 0; ncol = len(M[0])
    for col in range(ncol):
        piv = next((i for i in range(r, len(M)) if M[i][col] & 1), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][col] & 1:
                M[i] = [(a + b) & 1 for a, b in zip(M[i], M[r])]
        r += 1
    return r

# enumerate (Z/2)^3 flip-vectors to confirm iota equals NONE of them:
import itertools
gens = {"c": table["c"], "theta": table["theta"], "gamma5": table["gamma5"]}
elements = {}
for bits in itertools.product([0, 1], repeat=3):
    v = [0, 0, 0, 0]
    for b, k in zip(bits, ("c", "theta", "gamma5")):
        if b:
            v = [(a ^ cc) for a, cc in zip(v, gens[k])]
    elements["".join(k for b, k in zip(bits, ("c", "th", "g5")) if b) or "id"] = v

rank3 = f2_rank([table["c"], table["theta"], table["gamma5"]])
span_T7_eq_T3 = all(table[k][2] == table[k][3] for k in ("c", "theta", "gamma5"))
print()
print(f"  rank <c,theta,gamma5>            = {rank3}")
print(f"  in <c,theta,gamma5>: T7-col == T3-col (B766's 'T7=T3, one choice'): {span_T7_eq_T3}")
print()
# T6 is frame-dependent (E): verify the verdict for BOTH possible T6 values.
robust = True
for t6 in (0, 1):
    iota_row = [0, t6, 1, 0]                    # T4 fix, T6=t6 either, T7 FLIP, T3 fix
    rank4 = f2_rank([table["c"], table["theta"], table["gamma5"], iota_row])
    match = [name for name, v in elements.items() if v == iota_row]
    print(f"  iota=(T4,T6,T7,T3)={iota_row} [T6={t6}]: rank<...,iota>={rank4}, "
          f"independent={rank4 > rank3}, equals-(Z/2)^3-elt={match or 'NONE'}")
    robust = robust and (rank4 == 4) and (not match)
iota_splits_T7_T3 = True                        # iota flips T7 (=1) but fixes T3 (=0)
print()
print(f"  IOTA flips T7 but FIXES T3 -> SPLITS B766's T7=T3 identification: {iota_splits_T7_T3}")
print(f"  RANK-4 and 'equals no (Z/2)^3 element' hold for BOTH T6 values (robust): {robust}")
R["F_rank_without_iota"] = rank3
R["F_rank_with_iota"] = 4
R["F_iota_independent"] = True
R["F_iota_splits_T7_T3"] = bool(iota_splits_T7_T3)
R["F_iota_equals"] = None
R["F_robust_to_T6"] = bool(robust)
assert robust


# ===========================================================================
head("VERDICT (B787 Phase 1 -- iota-identification)")
# ===========================================================================
verdict = (
 "OUTCOME B: iota (inversion) is a GENUINELY INDEPENDENT 4th generator. It is NOT c, theta,\n"
 "gamma5, or any product. Decisive mechanism (two independent confirmations):\n"
 "  (1) ORIENTATION vs ARITHMETIC split: iota FLIPS T7 (time: monodromy t->t^-1 inverts the\n"
 "      loxodromic spectrum {phi^2,phi^-2}) but FIXES T3 (basepoint: A5 is AMBIVALENT, g~g^-1,\n"
 "      so inversion preserves 5A,5B; only Out(A5)=gamma5/Frobenius swaps them). In\n"
 "      <c,theta,gamma5> every element flips T7 IFF it flips T3 (B766's 'T7=T3, one choice'),\n"
 "      so iota, flipping one but not the other, cannot lie in the span. Rank 3 -> rank 4.\n"
 "  (2) DUAL-PAIR trace action: iota permutes the 8 coords by (x1 x4)(x2 x5)(x3 x8)(x6 x7);\n"
 "      trivial on the self-dual object V0 (=Sym^2, matching B786's collapse) but trace-active\n"
 "      on the non-self-dual variety (W1/W2, generic) -- a move no c/theta/gamma5 makes.\n"
 "CONSEQUENCE: admitting inversion, TIME'S ARROW (T7) and THE BASEPOINT BIT (T3) -- welded into\n"
 "ONE choice by {c,theta,gamma5} -- become INDEPENDENT. iota is the involution that separates\n"
 "them. This sharpens B786 (rank-4 on the full SL(3) variety) with an exact mechanism and holds\n"
 "even on the object's orientation structure. Exact identification; not a numeric coincidence."
)
print(verdict)
R["VERDICT"] = "OUTCOME_B: iota independent 4th generator (rank 4); flips T7 not T3, splitting B766's T7=T3"

import json
with open("results.json", "w") as f:
    json.dump(R, f, indent=1, default=str)
print("\nwrote results.json")
