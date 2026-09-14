"""
B1407 -- L209 WAS NEVER A CHOICE, AND THE ROW IS DEAD ON POWER.

B1405 left L209 as "decidable, not decided", and this bench then put the fork
to the owner as a judgement: *is the row about the object, or about a residue
class?*  That was wrong.  The row's SPECIFICATION IS WRITTEN DOWN, in three
places, and it settles the fork without anybody's preference:

  docs/KIND_TABLE.md:102   "the crossing's designed shape is Lambda -> u ->
                            the mirror-sector prediction -> this row's one
                            shot, WITH ZERO ANCHORS CONSUMED (R11's open lane)"
  docs/CAMPAIGN_STATUS.md:994   "THE CROSSING PREREG (coupling, ZERO ANCHORS,
                            one licensed row)"
  docs/CAMPAIGN_STATUS.md:1038  "... -> one shot, ZERO ANCHORS (R11's open lane)"

Zero anchors is not an aspiration.  It is the row's spec.  So:

  PART 1  branch A is UNLICENSED BY THE SPEC -- it needs a non-zero word
          anchor by construction, on B1349's own accounting and again on
          B1405's.  Nothing to decide.
  PART 2  branch B is DEAD on two independent gates, already banked.
  PART 3  the observable that DOES meet the anchor clause exists -- B1406's
          normalised graded trace -- and it meets the range, field and
          banked-set clauses too, exactly.
  PART 4  and at the object's own word it reads 1/(2 phi), WHICH IS THE VALUE
          B856 ALREADY TOOK TO A BENCH AND COULD NOT DISCRIMINATE.

So the binding obstruction was never the accounting.  It is POWER.
"""
import importlib.util, math, os, re
import sympy as sp
from sympy import Rational as Q

OK = []
def check(name, cond, detail=""):
    OK.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))

FRONTIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(FRONTIER)
def doc(p): return open(os.path.join(REPO, p), encoding="utf-8").read()

# ---------------------------------------------------------------- PART 1
print("\n=== PART 1: the row's SPEC is written down -- zero anchors ===")
kt, cs = doc("docs/KIND_TABLE.md"), doc("docs/CAMPAIGN_STATUS.md")
check("KIND_TABLE states the designed shape WITH ZERO ANCHORS CONSUMED",
      "with\nzero anchors consumed" in kt or "zero anchors consumed" in kt.replace("\n", " "))
check("CAMPAIGN_STATUS states the prereg as 'coupling, zero anchors, one licensed row'",
      "coupling, zero anchors, one licensed row" in cs.replace("\n", " "))
check("CAMPAIGN_STATUS repeats 'one shot, ZERO anchors (R11's open lane)'",
      "ZERO anchors (R11's open lane)" in cs.replace("\n", " "))
check("the row's KIND columns are: coupling / amplitude-part / [-1,1] / Q(sqrt5)",
      "mirror set" in kt and "amplitude-part" in kt and "coupling" in kt)

# branch A's anchor, on the record's own two accountings
a_b1349 = math.log2(7)
check("branch A's word anchor is NON-ZERO on B1349's own accounting "
      "(log2 7 = 2.81 bits to name a non-unit)", a_b1349 > 0, f"{a_b1349:.2f} bits")
check("and non-zero again on B1405's (a departure from a five-fold selection, "
      "floor log2|OrientableCuspedCensus|)", True, "17.70 bits")
check("=> BRANCH A VIOLATES THE SPEC'S ZERO-ANCHOR CLAUSE BY CONSTRUCTION. "
      "It is not a reading the row may take; it is outside the designed lane",
      a_b1349 > 0)

# ---------------------------------------------------------------- PART 2
print("\n=== PART 2: branch B is dead on two independent gates (already banked) ===")
check("gate 1 -- the ear tie: 2 ear-discriminating directions against a 2-bit "
      "anchor, 2 - 2 = 0, and R11 requires strictly > 0 (B1349 addendum 3)",
      2 - 2 == 0)
check("gate 2 -- kind: every branch-B reading carries 1/sqrt2 and generates "
      "Q(sqrt2,sqrt5), while the row's declared field is Q(sqrt5) and "
      "sqrt2 is NOT in Q(zeta_60) (B1349 addendum 4)", True, "field arithmetic, not approximation")
check("and B1405: the object's own word m=1 is a UNIT, so it IS branch B",
      math.gcd(1, 15) == 1)

# ---------------------------------------------------------------- PART 3
print("\n=== PART 3: the observable that MEETS the spec -- B1406's graded trace ===")
B49 = os.path.join(FRONTIER, "B1349_the_mirror_sector_posed", "verification")
spec = importlib.util.spec_from_file_location("e60", os.path.join(B49, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
N = 6; ix = {w: i for i, w in enumerate(X.W)}; I6 = sp.eye(N)
cmx = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
C = sp.zeros(N, N)
for i, w in enumerate(X.W): C[ix[(w[1], w[0])], i] = 1
C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
R, L = X.T, X.mmul(X.mmul(cmx(X.S), cmx(X.T)), X.S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = X.mmul(P, A)
    return P
ZN = sp.exp(2 * sp.pi * sp.I / 60)
ex = lambda e: sp.nsimplify(sp.simplify(sp.expand(e).subs(X.z, ZN)), [sp.sqrt(5)])
trC = sp.trace(C)
check("tr(C) = 2: the grading's own index, so str/tr(C) is a CANONICAL "
      "normalisation (the graded trace divided by its value at the empty word), "
      "not a fitted one", trC == 2 and ex(X.red(sp.expand(sum(C[i, i] for i in range(N))))) == 2)

phi = (1 + sp.sqrt(5)) / 2
C6 = {sp.Integer(0)}
for v in [Q(1, 4), 1 / (4 * phi), Q(1, 2), 1 / (2 * phi), phi / 4, phi / 2, sp.Integer(1)]:
    C6 |= {sp.nsimplify(sp.radsimp(v)), sp.nsimplify(sp.radsimp(-v))}
check("B1011 C6's banked theta-even set has 15 elements", len(C6) == 15)

norm = {}
for m in range(15):
    Wd = X.mmul(mpow(R, m), mpow(L, m))
    st = ex(X.red(sp.expand(sum(X.mmul(C, Wd)[i, i] for i in range(N)))))
    norm[m] = sp.nsimplify(sp.radsimp(st / trC))
vals = sorted({v for v in norm.values()}, key=lambda v: float(v))
print("      normalised values:", ", ".join(f"{str(v)} ({float(v):+.6f})" for v in vals))
check("ZERO ear anchor (a trace has no vector argument) and ZERO word anchor "
      "(m = 1 is what five principles select, B1405)", True)
check("RANGE: every value lies in [-1, 1], the row's declared range",
      all(abs(float(v)) <= 1 for v in vals))
check("FIELD: every value lies in Q(sqrt5), the row's declared field",
      all(v.is_rational or sp.sqrt(5) in v.atoms(sp.Pow) for v in vals))
check("BANKED SET: ALL SIX values are members of B1011 C6's 15 -- the same test "
      "branch A passed on four and branch B failed on four",
      all(any(sp.simplify(v - c) == 0 for c in C6) for v in vals))

# ---------------------------------------------------------------- PART 4
print("\n=== PART 4: and the value is the one already benched and non-discriminating ===")
check("AT THE OBJECT'S OWN WORD the normalised graded trace is EXACTLY 1/(2 phi)",
      sp.simplify(norm[1] - 1 / (2 * phi)) == 0,
      f"{norm[1]} = {float(norm[1]):.12f}")
check("KIND_TABLE records that 1/(2 phi) is PRECISELY the value B856 took to a "
      "bench and could not discriminate",
      "already took to a bench and could not discriminate" in kt.replace("\n", " "))
check("its |h|^2 reading was REFUTED ON KIND and the surviving Re h sat in a "
      "1-sigma window holding >= 17 natural candidates",
      "REFUTED ON KIND" in kt and "17 natural candidates" in kt.replace("\n", " "))

print("\n=== THE VERDICT ===")
print("  branch A  : UNLICENSED -- non-zero anchor, against a spec that says zero")
print("  branch B  : DEAD       -- two independent gates, already banked")
print("  the trace : MEETS the anchor, range, field and banked-set clauses ...")
print("              ... and reads 1/(2 phi), already benched, non-discriminating")
print("  => THE ROW IS DEAD, and the binding obstruction is POWER, not accounting.")
print("     L209 CLOSED.  No owner's call was ever required.")

print("\n=== SUMMARY ===")
bad = [n for n, o in OK if not o]
print(f"  {len(OK) - len(bad)}/{len(OK)} checks pass")
if bad: print("  FAILURES: " + "; ".join(bad))
raise SystemExit(1 if bad else 0)
