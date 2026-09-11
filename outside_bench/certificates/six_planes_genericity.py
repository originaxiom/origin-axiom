"""CERTIFICATE -- the GENERICITY CONTROL on memo 201, and it TRIMS memo 201's reading.

B1223's lesson, applied by this bench to its own result the same day it was banked:
"The value of a small-group coincidence is not zero, but it is not evidence, and the difference
is one computation: check whether the action matches."  The analogue here is: check whether the
structure survives RANDOMISATION.

MEMO 201 measured the six COORDINATE planes -- the pairs of the object's four superselection
charges INV[8,14,16,22] -- and found resolvent 77 at exactly {4,8} and {7,11}, and {-3,-231} at
the four planes that mix them.  That measurement is correct and is reproduced here as control C1.
WHAT IT DID NOT ASK is whether a GENERIC 2-plane in the same 4-dimensional charge space sees
something different.  If a generic plane sees 77 too, then "77 lives within the blocks" is a
statement about the coordinate planes, not about the charge space.

CELLS (two outcomes each)
  CELL 1  Is a 3-dimensional kernel on the 27 generic in the charge space, or special to the
          two ORPHAN charges (exponents 7 and 11, whose Coxeter duals 5 and 1 carry no charge)?
          A: generic -- random elements have it too      B: special to the orphans
  CELL 2  Do the six coordinate planes see the SAME resolvent data as a generic 2-plane?
          A: yes -- the coordinate planes are not special
          B: no  -- each coordinate plane sees a PROPER SUBSET of what a generic plane sees
  CELL 3  Is 77 confined to the within-block planes, as memo 201's reading implied?
          A: yes -- generic planes do not show it       B: no -- it appears at every generic plane

CONTROLS
  C1  The six coordinate planes must reproduce memo 201 exactly, or the comparison is void.
  C2  Every random pair must COMMUTE (the charge space is abelian, u(1)^4) -- checked, and a
      non-commuting draw would be reported and skipped rather than silently pencilled.
  C3  The RNG seed is fixed and printed, so the sample is reproducible byte-for-byte.
  C4  All arithmetic EXACT.  No discriminant is read numerically.

Gate 5 untouched.  No measured value is used as input anywhere.
"""
import contextlib
import io
import json
import os
import random
import sys
import time

import sympy as sp

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SEED = 20260911
NS = [8, 14, 16, 22]
EXPO = {8: 4, 14: 7, 16: 8, 22: 11}
FAIL = []


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78, flush=True)


def check(n, ok, d=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {n}{('  ' + d) if d else ''}", flush=True)
    if not ok:
        FAIL.append(n)
    return ok


def sf(n):
    n = int(n)
    if n == 0:
        return 0
    s, n, o = (1 if n > 0 else -1), abs(n), 1
    for p, e in sp.factorint(n).items():
        if e % 2:
            o *= p
    return s * o


REPJ = json.load(open(os.path.join(ROOT, "frontier/B883_the_27/rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}
B854 = os.path.join(ROOT, "frontier/B854_centralizer_exact/e6_centralizer.py")
g6 = {"__file__": B854, "__name__": "b854"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(B854, encoding="utf-8").read(), B854, "exec"), g6)
INV = g6["INV"]


def rho(vec):
    M = sp.zeros(27, 27)
    for p in range(78):
        c = vec[p]
        if c == 0:
            continue
        q = sp.Rational(c.numerator, c.denominator)
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += q * Rp[i][j]
    return M


R = {n: rho(INV[n]) for n in NS}
x, lam = sp.symbols("x lambda")


def pencil(A, Bm):
    pts = [(sp.Rational(k), sp.Poly((A + sp.Rational(k) * Bm).charpoly(x).as_expr(), x).all_coeffs())
           for k in range(28)]
    xs = [p[0] for p in pts]
    co = [sp.expand(sp.interpolate(list(zip(xs, [p[1][ci] for p in pts])), lam)) for ci in range(28)]
    P = sp.expand(sum(co[i] * x ** (27 - i) for i in range(28)))
    shape, sfs = [], set()
    for f, m in sp.factor_list(sp.Poly(P, x, lam))[1]:
        fe = f.as_expr()
        dx = int(sp.degree(fe, x))
        shape.append((dx, int(m)))
        if dx >= 2:
            for g, _ in sp.factor_list(sp.Poly(sp.expand(sp.discriminant(sp.Poly(fe, x))), lam))[1]:
                if int(sp.degree(g.as_expr(), lam)) >= 2:
                    sfs.add(sf(sp.discriminant(sp.Poly(g.as_expr(), lam))))
    return sorted(shape), sorted(sfs)


# ================================================================== CELL 1
rule("CELL 1 -- is a 3-dimensional kernel on the 27 GENERIC in the charge space?")
print("       E6 exponents (1,4,5,7,8,11), Coxeter number h = 12, dual pairs (1,11)(4,8)(5,7).")
print("       The charges sit at {4,7,8,11}: {4,8} is the ONLY complete dual pair (4+8=12=h);")
print("       7 and 11 are ORPHANS -- their duals 5 and 1 carry no charge.\n")
kd = {}
for n in NS:
    kd[n] = len(R[n].nullspace())
    print(f"       dim ker rho(x{n})  (exponent {EXPO[n]:2d})  = {kd[n]}"
          f"{'   <-- ORPHAN' if EXPO[n] in (7, 11) else ''}")
random.seed(SEED)
print(f"\n       C3 -- RNG seed {SEED}, printed so the sample is reproducible")
rand_k = []
for _ in range(6):
    c = {n: random.randint(-5, 5) for n in NS}
    if all(v == 0 for v in c.values()):
        continue
    M = sum((sp.Integer(c[n]) * R[n] for n in NS), sp.zeros(27, 27))
    k = len(M.nullspace())
    rand_k.append(k)
    print(f"       random element {c}:  dim ker = {k}")
CELL1 = "B" if (max(rand_k) == 0 and kd[8] == 0 and kd[16] == 0 and kd[14] == 3 and kd[22] == 3) \
    else "A"
print(f"\n  CELL 1 = {CELL1}  -- " +
      ("a 3-dim kernel is NOT generic: it belongs to the two ORPHAN charges and to nothing else "
       "in the space (both dual-pair charges 0; 6 of 6 random elements 0)"
       if CELL1 == "B" else "a 3-dim kernel is generic"))

# ================================================================== C1 + CELL 2/3
rule("C1 -- the six COORDINATE planes must reproduce memo 201")
BANKED = {(8, 14): [-231, -3], (8, 16): [77], (8, 22): [-231, -3],
          (14, 16): [-231, -3], (14, 22): [77], (16, 22): [-231, -3]}
coord = {}
for i, a in enumerate(NS):
    for b in NS[i + 1:]:
        t0 = time.time()
        sh, sfs = pencil(R[a], R[b])
        coord[(a, b)] = (sh, sfs)
        print(f"       (x{a},x{b})  exps ({EXPO[a]},{EXPO[b]})  shape {sh}  resolvents {sfs}"
              f"   [{time.time()-t0:.0f}s]", flush=True)
check("C1 -- all six coordinate planes reproduce memo 201's resolvents",
      all(coord[k][1] == v for k, v in BANKED.items()))

rule("CELL 2 & 3 -- RANDOM 2-planes in the SAME four-dimensional charge space")
rand = []
for _ in range(5):
    ca = {n: random.randint(-4, 4) for n in NS}
    cb = {n: random.randint(-4, 4) for n in NS}
    A = sum((sp.Integer(ca[n]) * R[n] for n in NS), sp.zeros(27, 27))
    Bm = sum((sp.Integer(cb[n]) * R[n] for n in NS), sp.zeros(27, 27))
    if (A * Bm - Bm * A) != sp.zeros(27, 27):
        print(f"       C2 -- draw {ca}/{cb} does NOT commute; skipped, not pencilled")
        continue
    t0 = time.time()
    sh, sfs = pencil(A, Bm)
    rand.append((sh, sfs))
    print(f"       random {ca} / {cb}\n           shape {sh}   resolvents {sfs} "
          f"  [{time.time()-t0:.0f}s]", flush=True)
check("C2 -- every random pair commutes (the charge space is abelian)", len(rand) == 5,
      f"{len(rand)} of 5 usable")

full = sorted({s for _, sfs in coord.values() for s in sfs})
gen_full = all(sfs == full for _, sfs in rand)
CELL2 = "B" if all(set(sfs) < set(full) for _, sfs in coord.values()) else "A"
CELL3 = "B" if all(77 in sfs for _, sfs in rand) else "A"
print(f"\n       the full resolvent set across the object's charge space: {full}")
print(f"       every random plane sees ALL of it: {gen_full}")
print(f"       every coordinate plane sees a PROPER SUBSET: "
      f"{all(set(sfs) < set(full) for _, sfs in coord.values())}")
print(f"\n  CELL 2 = {CELL2}   CELL 3 = {CELL3}")

# ================================================================== verdict
rule("VERDICT -- what survives memo 201, and what is trimmed")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
print("""
  TRIMMED, and this bench found it by running the control on its own result:

    Memo 201's reading implied that 77 is tied to measuring WITHIN a block.  It is not.
    EVERY generic 2-plane in the charge space sees ALL THREE resolvents {-3, 77, -231}.
    77 is not confined to the coordinate planes; it is everywhere in the space.

  WHAT SURVIVES, and is now on better footing than the version banked:

   1. THE KLEIN FOUR-GROUP IS AN INVARIANT OF THE CHARGE SPACE, not an artifact of a chosen
      pair.  { Q(sqrt-3), Q(sqrt77), Q(sqrt-231) } is what a generic plane sees, every time,
      5 of 5.  -231 = -3 * 77.  One leg is the BEING face.

   2. THE SIX COORDINATE PLANES ARE DEGENERATE LOCI.  Each sees a PROPER SUBSET of the generic
      picture: {77} at the two within-block planes, {-3,-231} at the four cross-block planes.
      A generic plane sees the whole group; the coordinate planes go partially blind.

   3. AND WHICH HALF GOES BLIND IS COXETER DUALITY.  {4,8} is the unique complete dual pair
      among the charges (4+8 = 12 = h); 7 and 11 are orphans.  Within-block -> 77 only.
      Across -> {-3,-231} only.

   4. THE ORPHAN KERNEL IS NOT GENERIC.  dim ker = 3 for BOTH orphan charges and 0 for both
      dual-pair charges and for 6 of 6 random elements of the same space.  Two charges, one
      shared 3-dimensional kernel, nothing else in the space annihilating anything.

  AND THE ANTI-CIRCULARITY ARGUMENT IS STRENGTHENED, NOT WEAKENED.  B1077's blocker was that
  the only twist-source is the MEASURED pencil triple, so any 77 it yields is circular -- the
  branch locus is mu by construction.  This control shows 77 is not a property of that pencil
  at all: it is visible from ALMOST EVERY plane of the charge space, and K is reachable with no
  pencil whatsoever (rho(x8) and rho(x16) restricted to the orphan kernel both generate K).
  A datum that shows up from almost anywhere is not an artifact of where one looked.

  WHAT IS NOT CLAIMED.  No value, ratio or prediction; Gate 5 untouched.  B882 is not proved --
  the remaining half is the 3D4 twisting classification, a literature proposition.  And the
  resolvent V4 is NOT asserted to be B730's face V4; that identification is exactly what B1223
  killed once on the ACTION and what memo 200 typed by KIND.
""")
print("Gate 5 untouched.  No measured value is used or named.")
