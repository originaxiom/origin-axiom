#!/usr/bin/env python3
"""
R04 BLIND RECOMPUTATION -- B863 (termination) + B994 (rule variation), over B861's menus.

Written BEFORE opening frontier/B861_fused_cascade/fused_cascade.py,
frontier/B863_termination/termination.py, any results.json / arc_verdict.json,
or tests/test_b861_*.py / tests/test_b863_*.py.
Only the three FINDINGS.md files were read (claim statement + menu content).

Everything here is exact (integer rep arithmetic); no floats, no measured SM values.

Conventions (mine, stated up front):
  * A "rep" of a candidate subalgebra is a tuple of factor-labels, one per
    NON-ABELIAN simple factor; all u(1) charges are stripped ("dial-stripped").
  * Conjugation acts factorwise; real and pseudoreal factor-reps are
    self-conjugate; complex ones swap with their bar.
  * The GENERATION at a given level = the branching of E6's 27 down the chain
    (B861's uniform object).  For B863's step-4 table the arc's stated multiset
    {3:2, 3bar:2, 1:3} is the 15-state SM generation (the chiral content of a
    family); I test BOTH the full-27 content and the 15-state SM generation and
    report both, since the verdict (chiral yes/no) is what is banked.
  * chiral(M)  :=  M != conj(M) as multisets.
"""

from collections import Counter
from itertools import product

# ---------------------------------------------------------------------------
# rep atoms: (group, label) with dimension and conjugate
# ---------------------------------------------------------------------------
# label table: name -> (dim, conjugate_name).  Self-conjugate <=> conj == name.
ATOMS = {
    # su(2)
    "su2.1": (1, "su2.1"), "su2.2": (2, "su2.2"), "su2.3": (3, "su2.3"),
    # su(3)
    "su3.1": (1, "su3.1"), "su3.3": (3, "su3.3b"), "su3.3b": (3, "su3.3"),
    # su(4)
    "su4.1": (1, "su4.1"), "su4.4": (4, "su4.4b"), "su4.4b": (4, "su4.4"),
    "su4.6": (6, "su4.6"),          # Lambda^2 4, self-conjugate (real)
    # su(5)
    "su5.1": (1, "su5.1"), "su5.5": (5, "su5.5b"), "su5.5b": (5, "su5.5"),
    "su5.10": (10, "su5.10b"), "su5.10b": (10, "su5.10"),
    # su(6)
    "su6.6": (6, "su6.6b"), "su6.6b": (6, "su6.6"),
    "su6.15": (15, "su6.15b"), "su6.15b": (15, "su6.15"),   # Lambda^2 6, complex
    # so(10)
    "so10.1": (1, "so10.1"), "so10.10": (10, "so10.10"),
    "so10.16": (16, "so10.16b"), "so10.16b": (16, "so10.16"),
    # sp(8) = C4
    "sp8.27": (27, "sp8.27"),       # traceless Lambda^2 8, self-dual
    # trivial placeholder for "no non-abelian factor left"
    "triv": (1, "triv"),
}

def dim_atom(a): return ATOMS[a][0]
def conj_atom(a): return ATOMS[a][1]

def dim_rep(r):  # r = tuple of atoms
    d = 1
    for a in r: d *= dim_atom(a)
    return d

def conj_rep(r): return tuple(conj_atom(a) for a in r)

def dim_content(M):  # M = Counter of reps
    return sum(dim_rep(r) * n for r, n in M.items())

def conj_content(M):
    return Counter({conj_rep(r): n for r, n in M.items()})

def chiral(M):
    """Registerability core: multiset stays chiral <=> M != conj(M)."""
    return M != conj_content(M)

def C(*reps):  # content builder
    return Counter(reps)

def mul(n, M):
    return Counter({r: n * c for r, c in M.items()})

# ---------------------------------------------------------------------------
# Step 1: 27 of E6 under the four maximal-subalgebra options (B861 menu)
# ---------------------------------------------------------------------------
# dims of the OPTION algebras (u(1)s counted, as in the banked tables)
OPT_DIMS = {
    "SO(10)xU(1)": 45 + 1,           # 46
    "SU(6)xSU(2)": 35 + 3,           # 38
    "Sp(8)":       36,               # 36
    "SU(3)^3":     8 * 3,            # 24
    "SU(5)xU(1)":  24 + 1,           # 25
    "Pati-Salam":  15 + 3 + 3,       # 21  (su(4)+su(2)+su(2))
    "SU(4)xU(1)":  15 + 1,           # 16
    "SM":          8 + 3 + 1,        # 12  (su(3)+su(2)+u(1))
}

step1 = {
    # 27 -> 16(+1) + 10(-2) + 1(+4); u(1) stripped
    "SO(10)xU(1)": C(("so10.16",), ("so10.10",), ("so10.1",)),
    # 27 -> (15bar,1) + (6,2)
    "SU(6)xSU(2)": C(("su6.15b", "su2.1"), ("su6.6", "su2.2")),
    # 27 -> 27 (traceless Lambda^2 of the 8), self-dual
    "Sp(8)": C(("sp8.27",)),
    # trinification: 27 -> (3,3b,1) + (1,3,3b) + (3b,1,3)
    "SU(3)^3": C(("su3.3", "su3.3b", "su3.1"),
                 ("su3.1", "su3.3", "su3.3b"),
                 ("su3.3b", "su3.1", "su3.3")),
}

# ---------------------------------------------------------------------------
# Step 2: content {16,10,1} of so(10) under the two options (B861 menu)
# ---------------------------------------------------------------------------
step2 = {
    # 16 -> 10 + 5b + 1 ; 10 -> 5 + 5b ; 1 -> 1     (u(1) stripped)
    "SU(5)xU(1)": C(("su5.10",), ("su5.5b",), ("su5.1",),
                    ("su5.5",), ("su5.5b",), ("su5.1",)),
    # 16 -> (4,2,1) + (4b,1,2) ; 10 -> (6,1,1) + (1,2,2) ; 1 -> (1,1,1)
    "Pati-Salam": C(("su4.4", "su2.2", "su2.1"), ("su4.4b", "su2.1", "su2.2"),
                    ("su4.6", "su2.1", "su2.1"), ("su4.1", "su2.2", "su2.2"),
                    ("su4.1", "su2.1", "su2.1")),
}

# ---------------------------------------------------------------------------
# Step 3: 27-content at su(5) level = {10, 5, 5b x2, 1 x2}; two options
# ---------------------------------------------------------------------------
# branchings inside su(5):  5 -> 4 + 1 ; 10 = L^2 5 -> 6 + 4    (to su(4)+u(1))
#                           5 -> (3,1) + (1,2) ; 10 -> (3,2) + (3b,1) + (1,1)
step3 = {
    "SU(4)xU(1)": (
        C(("su4.6",), ("su4.4",))            # from 10
        + C(("su4.4",), ("su4.1",))          # from 5
        + C(("su4.4b",), ("su4.1",)) + C(("su4.4b",), ("su4.1",))  # 5b x2
        + C(("su4.1",)) + C(("su4.1",))      # 1 x2
    ),
    "SM": (
        C(("su3.3", "su2.2"), ("su3.3b", "su2.1"), ("su3.1", "su2.1"))  # 10
        + C(("su3.3", "su2.1"), ("su3.1", "su2.2"))                     # 5
        + mul(2, C(("su3.3b", "su2.1"), ("su3.1", "su2.2")))           # 5b x2
        + mul(2, C(("su3.1", "su2.1")))                                  # 1 x2
    ),
}

# ---------------------------------------------------------------------------
# B863 step 4: proper descents of the SM
# ---------------------------------------------------------------------------
# The 15-state SM generation (dial-stripped, non-abelian labels only):
SM_GEN = C(("su3.3", "su2.2"),              # Q  (3,2)
           ("su3.3b", "su2.1"),             # u^c
           ("su3.3b", "su2.1"),             # d^c
           ("su3.1", "su2.2"),              # L
           ("su3.1", "su2.1"))              # e^c

def branch_su2_to_u1(M):
    """(a) su(2)->u(1): keep su(3); each (r3,r2) -> dim(r2) copies of r3."""
    out = Counter()
    for (a3, a2), n in M.items():
        out[(a3,)] += n * dim_atom(a2)
    return out

SU3_TO_SU2_REG = {  # (b) regular su(3) -> su(2)xu(1):  3 -> 2 + 1
    "su3.3": [("su2.2",), ("su2.1",)],
    "su3.3b": [("su2.2",), ("su2.1",)],   # 2 is pseudoreal = self-conj
    "su3.1": [("su2.1",)],
}
SU3_TO_SU2_PRIN = {  # (b') principal su(3)_1 -> su(2)_4:  3 -> 3 (spin 1, real)
    "su3.3": [("su2.3",)],
    "su3.3b": [("su2.3",)],
    "su3.1": [("su2.1",)],
}

def branch_su3(M, rule, tag):
    """Break su(3) by `rule`; remaining non-abelian algebra = su(2)_new x su(2)_L.
    tag distinguishes the two su(2)s positionally (color-descended first)."""
    out = Counter()
    for (a3, a2), n in M.items():
        for piece in rule[a3]:
            out[(piece[0], a2)] += n
    return out

def abelianize(M):
    """(c) full abelianization: nothing non-abelian survives."""
    out = Counter()
    for r, n in M.items():
        out[("triv",)] += n * dim_rep(r)
    return out

# conformal-embedding check for (b'): su(3) level 1 -> su(2) level 4
# Dynkin index of image of the 3 of su(3): spin-1 rep of su(2), T(spin j)= (2j+1)j(j+1)/3 * (norm T(fund)=1/2)
# T(spin 1/2) = 1/2 ; T(spin 1) = 2.  Embedding index = T(image)/T(3) = 2/(1/2) = 4.
from fractions import Fraction
def su2_index(j2):  # j2 = 2j (integer); T = (2j+1)j(j+1)/3 with T(fund)=1/2
    j = Fraction(j2, 2)
    return (2 * j + 1) * j * (j + 1) / 3

emb_index = su2_index(2) / su2_index(1)          # = 4
c_su3_1 = Fraction(8 * 1, 1 + 3)                 # dim*k/(k+h_vee) = 8/4 = 2
c_su2_4 = Fraction(3 * 4, 4 + 2)                 # 12/6 = 2

# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------
def report(name, M, expected_dim=None):
    d = dim_content(M)
    ch = chiral(M)
    ok = "" if expected_dim is None else ("  [dim %d %s]" % (
        d, "OK" if d == expected_dim else "** DIM MISMATCH exp %d **" % expected_dim))
    print("  %-28s dim=%3d  chiral=%s%s" % (name, d, ch, ok))
    return ch

print("=" * 72)
print("STEP 1: 27 of E6 under B861's four maximal options (u(1) stripped)")
reg1 = {}
for name, M in step1.items():
    reg1[name] = report("%s (alg dim %d)" % (name, OPT_DIMS[name]), M, 27)

print("\nSTEP 2: {16,10,1} of so(10) under the two options")
reg2 = {}
for name, M in step2.items():
    reg2[name] = report("%s (alg dim %d)" % (name, OPT_DIMS[name]), M, 27)

print("\nSTEP 3: 27-content at su(5) under the two options")
reg3 = {}
for name, M in step3.items():
    reg3[name] = report("%s (alg dim %d)" % (name, OPT_DIMS[name]), M, 27)

print("\n" + "=" * 72)
print("B863 STEP 4: every proper descent of the SM (15-state generation)")
print("  control first: the SM itself on its own generation")
sm_ok = report("SM (control)", SM_GEN, 15)
d_a = branch_su2_to_u1(SM_GEN)
d_b = branch_su3(SM_GEN, SU3_TO_SU2_REG, "reg")
d_bp = branch_su3(SM_GEN, SU3_TO_SU2_PRIN, "prin")
d_c = abelianize(SM_GEN)
r_a = report("(a) su2->u1  [su3 left]", d_a, 15)
r_b = report("(b) su3->su2xu1 regular", d_b, 15)
r_bp = report("(b') su3_1->su2_4 princ.", d_bp, 15)
r_c = report("(c) abelianization", d_c, 15)
print("  (a) multiset under su(3):", dict(Counter({r[0]: n for r, n in d_a.items()})))
print("  (b') conformal check: emb index =", emb_index,
      " c(su3_1) =", c_su3_1, " c(su2_4) =", c_su2_4,
      " match:", c_su3_1 == c_su2_4 and emb_index == 4)

print("\n  same four descents applied to the FULL 27-content at SM level:")
M27 = step3["SM"]
r27_a = report("(a) on 27", branch_su2_to_u1(M27), 27)
r27_b = report("(b) on 27", branch_su3(M27, SU3_TO_SU2_REG, "reg"), 27)
r27_bp = report("(b') on 27", branch_su3(M27, SU3_TO_SU2_PRIN, "prin"), 27)
r27_c = report("(c) on 27", abelianize(M27), 27)

termination = (sm_ok and not (r_a or r_b or r_bp or r_c)
               and not (r27_a or r27_b or r27_bp or r27_c))
print("\nTERMINATION VERDICT: SM chiral=%s; all four proper descents vector-like"
      " (both generation conventions): %s" % (sm_ok, termination))

print("\n" + "=" * 72)
print("B994: enumerate EVERY registerable-respecting selection function")
menu = [
    [(n, OPT_DIMS[n], reg1[n]) for n in ["SO(10)xU(1)", "SU(6)xSU(2)", "Sp(8)", "SU(3)^3"]],
    [(n, OPT_DIMS[n], reg2[n]) for n in ["SU(5)xU(1)", "Pati-Salam"]],
    [(n, OPT_DIMS[n], reg3[n]) for n in ["SU(4)xU(1)", "SM"]],
]
reg_per_step = [[o for o in step if o[2]] for step in menu]
print("registerable options per step:", [len(s) for s in reg_per_step])
chains = list(product(*reg_per_step))
print("number of selection-function chains:", len(chains))
endpoints = set()
for ch in chains:
    path = " -> ".join(o[0] for o in ch)
    endpoints.add(ch[-1][0])
    print("   ", path)
print("all endpoints:", endpoints, " all SM:", endpoints == {"SM"})

def pick(rule):
    out = []
    for step in reg_per_step:
        if rule == "max-dim": out.append(max(step, key=lambda o: o[1]))
        elif rule == "min-dim": out.append(min(step, key=lambda o: o[1]))
        elif rule == "first": out.append(step[0])
        elif rule == "last": out.append(step[-1])
    return [o[0] for o in out]

for rule in ["max-dim", "first", "min-dim", "last"]:
    print("  rule %-8s: %s" % (rule, " -> ".join(pick(rule))))

print("\n" + "=" * 72)
print("CONTROLS (the instrument CAN find the excluded thing when planted)")
# C1: planted chiral step-4 descent -- a fake descent that keeps 3 unpaired
plant1 = C(("su3.3",), ("su3.1",))
print("  C1 planted chiral content {3,1} under su(3): chiral =", chiral(plant1),
      "(must be True)")
# C2: planted vector-like step-3 content: 5 + 5b + 1 + 1 under the SM subalg
#     (a genuinely self-conjugate multiset -- the instrument must KILL it)
plant2 = (C(("su3.3", "su2.1"), ("su3.1", "su2.2"))       # 5
          + C(("su3.3b", "su2.1"), ("su3.1", "su2.2"))    # 5b
          + mul(2, C(("su3.1", "su2.1"))))                # 1 x2
print("  C2 planted vector-like 5+5b+1+1 under SM: chiral =", chiral(plant2),
      "(must be False)")
# C2b: 27-content minus the 10 (5+5b+5b+singlets) is CHIRAL (5b unpaired) --
#      instrument must still register it; documents that the 10 is not the
#      only chirality carrier in the multiset sense
plant2b = (C(("su3.3", "su2.1"), ("su3.1", "su2.2"))
           + mul(2, C(("su3.3b", "su2.1"), ("su3.1", "su2.2")))
           + mul(2, C(("su3.1", "su2.1"))))
print("  C2b 27-content minus the 10 (5+5b+5b+2x1): chiral =", chiral(plant2b),
      "(must be True -- net 5b unpaired)")
# C3: plant an extra registerable option at step 3 and re-enumerate:
fake_step3 = reg_per_step[2] + [("FAKE-X", 13, True)]
fake_chains = list(product(reg_per_step[0], reg_per_step[1], fake_step3))
fake_endpoints = {c[-1][0] for c in fake_chains}
print("  C3 planted extra registerable step-3 option: chains =", len(fake_chains),
      " endpoints =", fake_endpoints,
      " uniqueness broken:", fake_endpoints != {"SM"})
# C4: conjugation self-test: conj is an involution on every atom
assert all(conj_atom(conj_atom(a)) == a for a in ATOMS)
assert all(dim_atom(conj_atom(a)) == dim_atom(a) for a in ATOMS)
print("  C4 conjugation involution + dim-preservation on all atoms: OK")

print("\nDONE (all exact integer/fraction arithmetic; no measured inputs)")
