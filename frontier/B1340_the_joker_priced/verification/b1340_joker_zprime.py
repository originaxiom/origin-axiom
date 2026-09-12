"""B1340 -- THE JOKER PRICED: grant C3 (three CHIRAL generations) as a declared input and compute
what it costs, and what it buys.

THE CLAIM UNDER TEST -- the paper, section 8 (papers/P3_THE_PAPER/main.tex:775):
    "The tree-level vacuum of the ninth leaves one abelian factor beyond the Standard Model,
     a family-non-universal Z', ANOMALY-FREE BY THE CONJUGATE GENERATIONS ..."
with the 19624 vacua coming "all in mirror pairs, VECTOR-LIKE" (main.tex:772-774), and B1303's
verified check (h): "cubic anomaly -20250 from the 27s and +20250 from the 27bars, total 0".
The record's Z' is P9 in docs/FALSIFIER_REGISTER.md -- the register's ONE entry whose regime the
object's own vacuum names.

CHIRALITY IS EXACTLY THE DELETION OF THE MIRRORS. So the joker's question is one line: delete them.

TWO NAIVE FALSIFIERS, BOTH VACUOUS -- recorded so they are not re-proposed (this bench proposed
both before checking, and owns that):
  (i)  anomalies over a full 27 cannot fail -- E6 is anomaly-safe (T-ANOMALY-REALIZED, B864(1));
  (ii) SM anomalies over N chiral generations cannot fail -- they are LINEAR in N, and one
       generation already cancels (B864(3)).  3 x 0 = 0.
The coefficient that CAN fail is the CUBIC of a FAMILY-NON-UNIVERSAL direction: it carries
sum_i f_i^3, cubic and not linear in the family charges, so multiplicity does NOT divide out.

PRE-REGISTERED (DESIGN B1340): Q1 the from-scratch branching reproduces B1303's -20250 (positive
control); Q2 the record's Z' FAILS on chiral content (failability: if it passed, the joker costs
nothing); Q3 on the VECTOR-LIKE content every anomaly polynomial is IDENTICALLY zero in all six
parameters, i.e. the record's anomaly check carries zero bits (vacuity control); Q4 on chiral
content the family part is FORCED to the shape (0, t, -t) up to permutation, on both readings of
"three chiral generations" (3 x 27 and 3 x 16); Q5 the record's (-10, 5, 5) is NOT of that shape.
PASS iff all five hold.
"""
import json
import sympy as sp
from sympy import Rational as R

# ---- the 27 of E6 in Standard-Model irreps, built from the branching, NOT imported ----------
# E6 > SO(10) x U(1)_psi > SU(5) x U(1)_chi x U(1)_psi:  27 = 16_(psi=1) + 10_(psi=-2) + 1_(psi=4)
#   16 = 10_(chi=-1) + 5bar_(chi=3) + 1_(chi=-5);        10 = 5_(chi=2) + 5bar_(chi=-2)
# columns: name, states, |colour|, su(2) dim, Y, chi, psi, in the 16?
F = [("Q",    6, 3, 2, R(1, 6),  -1,  1, True),
     ("uc",   3, 3, 1, R(-2, 3), -1,  1, True),
     ("ec",   1, 1, 1, R(1),     -1,  1, True),
     ("dc",   3, 3, 1, R(1, 3),   3,  1, True),
     ("L",    2, 1, 2, R(-1, 2),  3,  1, True),
     ("nuc",  1, 1, 1, R(0),     -5,  1, True),
     ("Hu",   2, 1, 2, R(1, 2),   2, -2, False),
     ("D",    3, 3, 1, R(-1, 3),  2, -2, False),
     ("Hd",   2, 1, 2, R(-1, 2), -2, -2, False),
     ("Dbar", 3, 3, 1, R(1, 3),  -2, -2, False),
     ("N",    1, 1, 1, R(0),      0,  4, False)]
assert sum(f[1] for f in F) == 27 and sum(f[1] for f in F if f[7]) == 16
for k, nm in ((4, "Y"), (5, "chi"), (6, "psi")):
    assert sum(f[1] * f[k] for f in F) == 0, nm      # every E6 Cartan direction is traceless on the 27

a, b, c = sp.symbols('a b c')                        # the SM-commuting E6 Cartan: Y, chi, psi
FAM = sp.symbols('f1 f2 f3')                         # the family torus -- NOT inside E6
PARAMS = [a, b, c] + list(FAM)
# the record's Z' (FALSIFIER_REGISTER P9): E6 part (5 psi - 3 chi)/2, family part (-10, 5, 5)
ZP = {a: 0, b: R(-3, 2), c: R(5, 2), FAM[0]: -10, FAM[1]: 5, FAM[2]: 5}

def content(kind, mirrors):
    """(states, |col|, su2dim, Y, charge) over three generations; `mirrors` adds the conjugates"""
    out = []
    for fi in FAM:
        for nm, n, col, s2, Y, chi, psi, in16 in F:
            if kind == "16" and not in16: continue
            q = a * Y + b * chi + c * psi + fi
            out.append((n, col, s2, Y, q))
            if mirrors: out.append((n, col, s2, -Y, -q))   # a 27bar: opposite Y and opposite Z'
    return out

def anomalies(C):
    return dict(
        grav =sp.expand(sum(n * q for n, _, _, _, q in C)),
        su3sq=sp.expand(sum(R(s2, 2) * q for n, col, s2, _, q in C if col == 3)),   # T(3)=1/2 per su2 component
        su2sq=sp.expand(sum(R(col, 2) * q for n, col, s2, _, q in C if s2 == 2)),   # T(2)=1/2 per colour component
        YYZ  =sp.expand(sum(n * Y ** 2 * q for n, _, _, Y, q in C)),
        YZZ  =sp.expand(sum(n * Y * q ** 2 for n, _, _, Y, q in C)),
        cubic=sp.expand(sum(n * q ** 3 for n, _, _, _, q in C)))

fails, out = [], {}
def check(label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok: fails.append(label)

A_vec = anomalies(content("27", mirrors=True))     # the record's vacuum: 3 x 27 + 3 x 27bar
A_27  = anomalies(content("27", mirrors=False))    # C3 granted, full 27s
A_16  = anomalies(content("16", mirrors=False))    # C3 granted, exotics paired off

print("STEP 0 -- the Z' charges rebuilt from the branching (compare FALSIFIER_REGISTER P9's list)")
z = {nm: R(-3, 2) * chi + R(5, 2) * psi for nm, n, col, s2, Y, chi, psi, _ in F}
print("   ", z)
check("Q0 the branching reproduces P9's charges: 4 on Q,uc,ec; -2 on dc,L; 10 on nuc,N; -8 on Hu,D; -2 on Hd,Dbar",
      [z[k] for k in ("Q","uc","ec")] == [4,4,4] and [z[k] for k in ("dc","L","Hd","Dbar")] == [-2]*4
      and [z[k] for k in ("nuc","N")] == [10,10] and [z[k] for k in ("Hu","D")] == [-8,-8])

print("\nSTEP 1 (Q1, positive control) -- the 27s ALONE, on the record's Z'")
v27 = {k: sp.simplify(v.subs(ZP)) for k, v in A_27.items()}
print("   ", v27)
check("Q1 B1303's check (h) reproduced from an independent branching: cubic on the 27s = -20250", v27['cubic'] == -20250)
check("Q1' and it is the family torus's alone: 27 * sum f^3 = -20250, every other coefficient 0 on the 27s",
      27 * sum(x ** 3 for x in (-10, 5, 5)) == -20250 and all(v27[k] == 0 for k in ('grav','su3sq','su2sq','YYZ','YZZ')))

print("\nSTEP 2 (Q2, FAILABILITY) -- does the record's Z' survive chirality?")
v16 = {k: sp.simplify(v.subs(ZP)) for k, v in A_16.items()}
vv  = {k: sp.simplify(v.subs(ZP)) for k, v in A_vec.items()}
print("   3 x 27 + 3 x 27bar (the record's vacuum):", vv)
print("   3 x 27, chiral                         :", v27)
print("   3 x 16, chiral                         :", v16)
check("Q2a the Z' IS anomaly-free on the record's vector-like content", all(v == 0 for v in vv.values()))
check("Q2b the Z' is NOT anomaly-free on 3 chiral 27s (the cubic obstructs)", v27['cubic'] != 0)
check("Q2c the Z' is NOT anomaly-free on 3 chiral 16s (five of six coefficients obstruct)",
      sum(1 for v in v16.values() if v != 0) >= 5)

print("\nSTEP 3 (Q3, VACUITY CONTROL) -- how many bits does the record's anomaly check carry?")
ident = all(sp.simplify(v) == 0 for v in A_vec.values())
print("   every anomaly polynomial on 3 x 27 + 3 x 27bar, as a polynomial in", PARAMS, ":",
      {k: sp.simplify(v) for k, v in A_vec.items()})
check("Q3 on a VECTOR-LIKE spectrum all six coefficients vanish IDENTICALLY -- every SM-commuting "
      "direction is anomaly-free, so the check on the record's vacuum cannot fail and carries ZERO bits", ident)

print("\nSTEP 4 (Q4) -- what IS anomaly-free once the mirrors are gone? solve the six conditions")
def shape(sol):
    """the family charges of a solution, and whether they are (0, t, -t) up to permutation.
    On the 16 psi is constant, so the EFFECTIVE family charge is g_i = f_i + c*psi|_16 = f_i + c."""
    return [sp.simplify(sol.get(x, x)) for x in FAM]
res = {}
for label, A, shift in (("3 x 27, chiral", A_27, 0), ("3 x 16, chiral", A_16, 1)):
    sols = sp.solve(list(A.values()), PARAMS, dict=True)
    print(f"   {label}: {len(sols)} solution branches")
    allshape = True
    for s in sols:
        g = shape(s)
        if shift: g = [sp.simplify(x + s.get(c, c)) for x in g]   # effective charge on the 16
        zeros = [i for i, x in enumerate(g) if sp.simplify(x) == 0]
        pairs = any(sp.simplify(g[i] + g[j]) == 0 for i in range(3) for j in range(3) if i != j)
        ok = bool(zeros) and pairs and sp.simplify(sum(g)) == 0
        print(f"      {s}\n         effective family charges {g}  -> shape (0,t,-t): {ok}")
        allshape &= ok
    res[label] = [str(s) for s in sols]
    check(f"Q4 on {label} EVERY anomaly-free branch has family shape (0, t, -t) up to permutation "
          f"-- one generation exactly neutral, the other two exactly OPPOSITE", allshape and len(sols) > 0)

print("\n   the theorem behind it, checked as an identity (no solver):")
S1 = sp.simplify(sum(FAM)); S3 = sp.simplify(sum(x ** 3 for x in FAM))
check("Q4' sum f = 0  =>  sum f^3 = 3 f1 f2 f3, so grav=0 and cubic=0 force some f_i = 0",
      sp.simplify((S3 - 3 * FAM[0] * FAM[1] * FAM[2]).subs({FAM[2]: -FAM[0] - FAM[1]})) == 0)

print("\nSTEP 5 (Q5) -- is the record's family part of that shape?")
f = (-10, 5, 5)
check(f"Q5 the record's family part {f} has sum {sum(f)} = 0 but product {f[0]*f[1]*f[2]} != 0, "
      f"so it is NOT of the forced shape -- the paper's Z' is the one thing chirality forbids",
      sum(f) == 0 and f[0] * f[1] * f[2] != 0)
print("   NOTE: P9 says the distinguished generation is neutral and 'the other two generations EQUAL'.")
print("   Chirality forces the other two to be OPPOSITE. That is a falsifiable difference, not a rescaling.")

json.dump({"zprime_charges": {k: str(v) for k, v in z.items()},
           "vector_like": {k: str(sp.simplify(v.subs(ZP))) for k, v in A_vec.items()},
           "chiral_27": {k: str(v) for k, v in v27.items()},
           "chiral_16": {k: str(v) for k, v in v16.items()},
           "identically_zero_on_vector_like": bool(ident),
           "solutions": res, "fails": fails}, open("b1340_joker_zprime.json", "w"), indent=1)
print("\nB1340:", "PASS" if not fails else f"FAIL ({len(fails)}): {fails}")
raise SystemExit(0 if not fails else 1)
