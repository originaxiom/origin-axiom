#!/usr/bin/env python3
"""MEMO-111 CELL (the owner's "when and how does it use it?"): THE
BIT'S LEDGER — the observer's one bit LOCATED at its exact
consumption point, and proved SPENT ONCE, NEVER AGAIN, at any depth.

THE QUESTION MADE PRECISE.  Memo 107 priced occupation at one bit and
memo 109 proved its setting undecidable; neither says WHEN the bit is
spent or HOW MANY TIMES.  "When" cannot have a temporal answer (the
object supplies no time — the schedule wall), so the honest form is
STRUCTURAL: at which step of the passage from grammar to realized
record does the bit become necessary, and is a further bit ever
demanded deeper down?  Both halves are decidable here.

THE LEDGER (each row exact, two-outcome):
  L1 (the bit-free floor): the presentation level costs NOTHING —
     the alphabet, the substitution grammar and the relator are
     integer/combinatorial data.  Verified: the relator found by
     memo 109 is re-derived as a word and confirmed to evaluate to
     +-I; the four founding rules are one rule up to recoding
     (memo 107, cited).  No field, no embedding, no bit.
  L2 (THE CONSUMPTION POINT): the trace field is Q(omega) with
     omega a root of X^2 - X + 1 — an ABSTRACT field, bit-free.  The
     bit is spent at exactly one step: CHOOSING AN EMBEDDING
     Q(omega) -> C, i.e. deciding which complex root of X^2 - X + 1
     the symbol omega denotes.  Verified: the polynomial has exactly
     two complex roots, they are exchanged by conjugation, and
     Gal(Q(omega)/Q) = Z/2 acts simply transitively on the two
     embeddings — ONE bit, spent ONCE, at the passage from the
     abstract record to a realized one.
  L3 (SPENT ONCE, NEVER AGAIN — the theorem): every trace of every
     reduced word to length 8 lies in Z[omega] — INTEGRAL, no
     denominators — and the ring the traces generate is EXACTLY
     Z[omega] (exhibited: tr(a) = 2 and tr(ab) = 2 - omega already
     generate it).  So the field NEVER GROWS with depth: no deeper
     computation ever demands a new irrationality, hence never a
     second Galois choice.  The one bit is the whole account, at
     every depth, forever.
  L4 (downstream determinism): once the embedding is fixed, every
     derived quantity is a FUNCTION of the traces — nothing further
     is chosen.  Exhibited on the systole and kappa at both
     embeddings: same real length, opposite torsion, no third option.
FENCE (stated, not waved): derived quantities may carry their own
UNIFORM normalization conventions (the branch of log in the complex
length, a geodesic's orientation).  Those are conventions applied
identically to every class, not additional Galois freedoms; the
FIELD-THEORETIC choice is exactly one, which is what this cell
counts.  Gate 5 untouched.
"""
from fractions import Fraction as Fr
import sympy as sp

# ---------------- pair arithmetic over Q(omega), omega^2 = omega - 1
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
def pneg(u): return (-u[0], -u[1])
ZERO, ONE = (Fr(0), Fr(0)), (Fr(1), Fr(0))
W = (Fr(0), Fr(1))
def mmul(A, B):
    return tuple(tuple(padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j]))
                 for j in range(2)) for i in range(2))
def mtr(A): return padd(A[0][0], A[1][1])
Ma = ((ONE, ONE), (ZERO, ONE))
Mb = ((ONE, ZERO), (pneg(W), ONE))
def minv(A):
    (p, q_), (r_, s_) = A
    assert padd(pmul(p, s_), pneg(pmul(q_, r_))) == ONE
    return ((s_, pneg(q_)), (pneg(r_), p))
MAT = {'a': Ma, 'b': Mb, 'A': minv(Ma), 'B': minv(Mb)}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
ID = ((ONE, ZERO), (ZERO, ONE))
NID = ((pneg(ONE), ZERO), (ZERO, pneg(ONE)))

# ---------------- L1: the bit-free floor
REL = "abaBAbabAB"
M = ID
for ch in REL:
    M = mmul(M, MAT[ch])
assert M == ID or M == NID
assert all(ch in "abAB" for ch in REL)
print("L1 (the bit-free floor): the presentation level is integer/combinatorial —")
print(f"    the relator {REL} is a WORD over the alphabet and evaluates to +-I;")
print("    the four founding rules are one rule up to recoding (memo 107).")
print("    No field, no embedding, NO BIT is required to state the record.")

# ---------------- L2: the consumption point
x = sp.symbols('x')
minpoly = x**2 - x + 1
roots = sp.solve(sp.Eq(minpoly, 0), x)
assert len(roots) == 2
r1, r2 = [sp.simplify(r) for r in roots]
assert sp.simplify(r1 - sp.conjugate(r2)) == 0          # exchanged by conjugation
assert sp.simplify(r1 + r2 - 1) == 0 and sp.simplify(r1*r2 - 1) == 0
# the Galois group is Z/2 acting simply transitively on the two embeddings
assert sp.simplify(r1 - r2) != 0
print("\nL2 (THE CONSUMPTION POINT): the trace field is the ABSTRACT field")
print("    Q[X]/(X^2 - X + 1) — stating it costs nothing.  The bit is spent at")
print("    exactly ONE step: choosing which complex root the symbol omega denotes.")
print(f"    The two roots {sp.nsimplify(r1)}, {sp.nsimplify(r2)} are exchanged by")
print("    conjugation; Gal = Z/2 acts SIMPLY TRANSITIVELY on the two embeddings.")
print("    => the bit is spent at the passage ABSTRACT RECORD -> REALIZED RECORD,")
print("    and there is exactly one such passage.")

# ---------------- L3: spent once, never again
seen = set()
nonintegral = 0
uses_omega = False
frontier = [("", ID)]
count = 0
for L in range(8):
    nxt = []
    for w, Mm in frontier:
        for ch in "abAB":
            if w and INV[w[-1]] == ch:
                continue
            nxt.append((w + ch, mmul(Mm, MAT[ch])))
    for w, Mm in nxt:
        t = mtr(Mm)
        if t[0].denominator != 1 or t[1].denominator != 1:
            nonintegral += 1
        if t[1] != 0:
            uses_omega = True
        seen.add((t[0], t[1]))
        count += 1
    frontier = nxt
assert nonintegral == 0
assert uses_omega
# the traces generate exactly Z[omega]: tr(a) = 2 and tr(ab) = 2 - omega
tr_a = mtr(MAT['a']); tr_ab = mtr(mmul(MAT['a'], MAT['b']))
assert tr_a == (Fr(2), Fr(0)) and tr_ab == (Fr(2), Fr(-1))
# 2 - (2 - omega) = omega  => omega is in the generated ring => ring = Z[omega]
gen_omega = padd(tr_a, pneg(tr_ab))
assert gen_omega == W
print(f"\nL3 (SPENT ONCE, NEVER AGAIN): all {count} reduced words to length 8 have")
print(f"    traces in Z[omega] — {nonintegral} non-integral, {len(seen)} distinct values;")
print("    and the traces GENERATE exactly Z[omega] (tr(a) - tr(ab) = omega).")
print("    THE FIELD NEVER GROWS WITH DEPTH: no deeper computation demands a new")
print("    irrationality, so NO SECOND GALOIS CHOICE IS EVER REQUIRED.  The one")
print("    bit is the whole account, at every depth, forever.")

# ---------------- L4: downstream determinism
om1, om2 = r1, r2
def realize(t, om): return sp.simplify(sp.nsimplify(t[0]) + sp.nsimplify(t[1])*om)
syst1, syst2 = realize(tr_ab, om1), realize(tr_ab, om2)
kappa = mtr(mmul(mmul(MAT['a'], MAT['b']), mmul(MAT['A'], MAT['B'])))
k1, k2 = realize(kappa, om1), realize(kappa, om2)
assert sp.simplify(sp.re(syst1) - sp.re(syst2)) == 0
assert sp.simplify(sp.im(syst1) + sp.im(syst2)) == 0
assert sp.simplify(sp.re(k1) - sp.re(k2)) == 0 and sp.simplify(sp.im(k1) + sp.im(k2)) == 0
print("\nL4 (downstream determinism): with the embedding fixed, every quantity is a")
print("    FUNCTION of the traces — nothing further is chosen.  On the systole")
print(f"    trace and kappa at both embeddings: real parts EQUAL, imaginary parts")
print("    OPPOSITE, and no third option exists (the polynomial has two roots).")

print("""
THE ANSWER — WHEN AND HOW THE BIT IS USED:
  WHEN: not at a moment.  The object supplies no time (the schedule
    wall), so the bit is not spent AT an instant — it is presupposed
    BY any realized description.  It is logically prior to the first
    tick, not located after it.  The bit is spent whenever the
    abstract record is COORDINATIZED, and that passage happens once
    per description, not once per event.
  HOW: by choosing an embedding of the abstract trace field into C —
    literally, by deciding which complex root of X^2 - X + 1 the
    symbol omega names.  That single act fixes, simultaneously and
    rigidly, the sign of every torsion, the CS sign, the CP sign and
    the chirality label (memo 110's odd column).
  HOW MANY TIMES: EXACTLY ONCE, EVER (L3).  Because the trace ring
    never grows, no deeper structure — no longer word, no finer
    invariant, no later epoch — ever demands a second choice.  The
    observer's discrete cost does NOT accumulate with the depth or
    the age of what is described.
IMPLICATIONS (interpretive, labeled): emergence in this record is not
a process that spends choices as it unfolds; the entire tower is
determined by the forced content plus ONE embedding, fixed once and
never revisited.  A universe like this does not become more
contingent the longer it runs, and an observer does not pay again for
looking deeper.  Gate 5 untouched.""")
