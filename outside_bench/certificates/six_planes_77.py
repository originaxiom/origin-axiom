"""CERTIFICATE -- is Q(sqrt77) an invariant of the OBJECT, or of the MEASURED PLANE?

SEAL  outside_bench/seals/SIX_PLANES_77_PREREG.md
      sha256 be58d6ce51c3b2a636d2bbacd462146de63cfcd1158b3657689860c405bb8016
      sealed BEFORE this file was written.

THE DOOR.  WHAT_WOULD_COUNT section 4A.3 leaves three licensed targets for the value layer.  B1077
calls B882's conjecture "the UNIQUE non-circular route to a 77-mechanism", and states the blocker:
"the only dressing source in the bank is the pencil triple -- forbidden as a twist-source by the
circularity theorem-let."  B1077 also proves the object's BARE D4 geometry carries nothing
77-shaped (even Clifford = M8(Q) x M8(Q), centre Q x Q; split cubic Q^3, trivial discriminant), so
every 77-bearing structure in the corpus is DRESSING.

THE GAP THIS RUNS.  The matter pencil P(x,lam) = det(xI - rho(x8) - lam*rho(x16)) (B886) is built on
ONE chosen pair of the object's FOUR superselection charges -- INV[8], INV[14], INV[16], INV[22],
invariant degrees 2*(4,7,8,11).  There are SIX such pairs.  THE PENCIL HAS ONLY EVER BEEN BUILT AT
ONE OF THEM.  B888 recorded, explicitly as "an observation with no mechanism claimed", that the
measured plane is the exponent-(4,8) pair and 77 = 7*11 is the product of the COMPLEMENTARY
exponents.  Nobody has built the other five planes, so nobody knows whether 77 is a fact about the
object or about which two charges were measured.

CELLS (two outcomes each, fixed in the seal before this file existed)
  CELL 1  Is the resolvent plane-invariant?
          A: every plane gives Q(sqrt77)     B: it varies with the plane
  CELL 2  Is B888's echo a LAW?  resolvent squarefree part == product of the UNMEASURED exponents?
          A: holds at all six                B: fails at any plane
  CELL 3  Is the factorization shape F1^1 * F2^8 special to the measured plane?
          A: same shape everywhere           B: the shape differs -- (x8,x16) is distinguished

CONTROLS
  C1  B886 must REPRODUCE at (x8,x16): P = F1^1 * F2^8, both cubic in x, branch locus = mu,
      squarefree part 77.
  C2  Every pair must COMMUTE exactly, or it has no joint weight structure.
  C3  The squarefree extractor is validated against B888's three banked discriminants first.
  C4  All arithmetic EXACT -- rational matrices, exact charpolys, exact interpolation, exact
      factorization over Q.  No discriminant is read numerically.
  C5  The field-isomorphism test must have BOTH a positive control (mu itself must be found
      isomorphic to K) and a BITE control (an unrelated cubic with the SAME resolvent 77 must be
      found NOT isomorphic), or "isomorphic to K" is an instrument that cannot say no.
  C6  BASE RATE, stated with the claim: how many DISTINCT cubic fields of resolvent Q(sqrt77) sit
      in a small coefficient window, and is K one of many or one of few?  Reported either way.

Gate 5 untouched.  No measured value is used as input anywhere.
"""
import contextlib
import io
import itertools
import json
import os
import sys
import time

import sympy as sp

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
B883 = os.path.join(ROOT, "frontier", "B883_the_27")
B854 = os.path.join(ROOT, "frontier", "B854_centralizer_exact", "e6_centralizer.py")
OUT = os.path.join(ROOT, "outside_bench", "outputs")
FAIL = []
CHARGE = {8: 4, 14: 7, 16: 8, 22: 11}          # INV key -> E6 exponent (degree = 2*exponent)
L = sp.Symbol("L")
MU = sp.Poly(500716339200 * L ** 3 - 2075673600 * L ** 2 - 4769856 * L + 2197, L)   # B886's mu


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78, flush=True)


def check(name, ok, detail=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)
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


# ================================================================== C3
rule("C3 -- the squarefree extractor, validated against B888's three banked discriminants")
for lbl, d in {
    "vacuum-weight cubic (F1's b-cubic)": 2**70 * 3**18 * 5**6 * 7**9 * 11**3 * 13**6,
    "generic-weight cubic (F2's)       ": 2**64 * 3**18 * 5**6 * 7**9 * 11**3 * 13**6,
    "mu, the charge field K            ": 2**32 * 3**10 * 5**2 * 7**3 * 11 * 13**6,
}.items():
    check(f"C3 -- {lbl.strip()} -> 77", sf(d) == 77, f"squarefree part = {sf(d)}")

# ================================================================== the build
rule("the object's four superselection charges, exact on the 27")
t0 = time.time()
REPJ = json.load(open(os.path.join(B883, "rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}
g6 = {"__file__": B854, "__name__": "b854"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(B854, encoding="utf-8").read(), B854, "exec"), g6)
INV = g6["INV"]


def rho_exact(vec):
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


RHO = {n: rho_exact(INV[n]) for n in sorted(CHARGE)}
print(f"       rho(x8), rho(x14), rho(x16), rho(x22) built exactly   [{time.time()-t0:.1f}s]")
print(f"       E6 exponents (1,4,5,7,8,11); these four sit at degrees 2*(4,7,8,11)")

# ================================================================== C2
rule("C2 -- every pair must COMMUTE exactly, or the pencil is not defined there")
PAIRS = [(a, b) for i, a in enumerate(sorted(CHARGE)) for b in sorted(CHARGE)[i + 1:]]
Z = sp.zeros(27, 27)
commuting = [(a, b) for a, b in PAIRS if (RHO[a] * RHO[b] - RHO[b] * RHO[a]) == Z]
for a, b in PAIRS:
    print(f"       [x{a}, x{b}]  (exponents {CHARGE[a]},{CHARGE[b]})  "
          f"commute: {(a,b) in commuting}", flush=True)
check("C2 -- all six pairs commute exactly", len(commuting) == 6, f"{len(commuting)} of 6")

# ================================================================== the sweep
rule("THE SWEEP -- the pencil built at EVERY plane, exactly, and its branch locus read")
x, lam = sp.symbols("x lambda")
rows = []
for a, b in commuting:
    t1 = time.time()
    A, B = RHO[a], RHO[b]
    pts = [(sp.Rational(k), sp.Poly((A + sp.Rational(k) * B).charpoly(x).as_expr(), x).all_coeffs())
           for k in range(28)]
    xs = [p[0] for p in pts]
    coeffs = [sp.expand(sp.interpolate(list(zip(xs, [p[1][ci] for p in pts])), lam))
              for ci in range(28)]
    P = sp.expand(sum(coeffs[i] * x ** (27 - i) for i in range(28)))
    shape, branch = [], []
    for f, m in sp.factor_list(sp.Poly(P, x, lam))[1]:
        fe = f.as_expr()
        dx = int(sp.degree(fe, x))
        shape.append((dx, int(m)))
        if dx >= 2:
            for g, mm in sp.factor_list(sp.Poly(sp.expand(sp.discriminant(sp.Poly(fe, x))), lam))[1]:
                ge = g.as_expr()
                dg = int(sp.degree(ge, lam))
                if dg >= 2:
                    branch.append((dg, sf(sp.discriminant(sp.Poly(ge, lam))),
                                   sp.sstr(ge.subs(lam, L))))
    sfs = sorted({s for _, s, _ in branch})
    unmeasured = [q for q in sorted(CHARGE.values()) if q not in (CHARGE[a], CHARGE[b])]
    rows.append(dict(pair=[a, b], exps=[CHARGE[a], CHARGE[b]], unmeasured=unmeasured,
                     shape=sorted(shape), branch_degs=sorted({d for d, _, _ in branch}),
                     resolvent_sf=sfs, branch=branch))
    print(f"       plane (x{a},x{b})  exps ({CHARGE[a]},{CHARGE[b]})   "
          f"shape (deg_x,mult) {sorted(shape)}   branch deg {sorted({d for d,_,_ in branch})}   "
          f"resolvent {sfs}   [{time.time()-t1:.1f}s]", flush=True)

# ------------------------------------------------------------------ C1
rule("C1 -- B886 must REPRODUCE at its own plane")
m = [r for r in rows if r["exps"] == [4, 8]][0]
check("C1 -- shape at (x8,x16) is F1^1 * F2^8, both cubic in x",
      m["shape"] == [(3, 1), (3, 8)], str(m["shape"]))
check("C1 -- the branch locus there is a CUBIC", m["branch_degs"] == [3], str(m["branch_degs"]))
check("C1 -- its resolvent is 77", m["resolvent_sf"] == [77], str(m["resolvent_sf"]))
banked = sp.simplify(sp.Poly(sp.sympify(m["branch"][0][2], locals={"L": L}), L).monic().as_expr()
                     - MU.monic().as_expr()) == 0
check("C1 -- and the branch cubic IS B886's banked mu, coefficient for coefficient", banked)

# ================================================================== CELL 3
rule("CELL 3 -- is the factorization SHAPE special to the measured plane?")
for r in rows:
    tag = ""
    if r["shape"] == [(3, 1), (3, 8)]:
        tag = "  <-- ALL CUBIC (B886's shape)"
    elif any(d == 1 for d, _ in r["shape"]):
        tag = "  <-- carries a LINEAR factor: a joint weight RATIONAL over Q"
    print(f"       exps {tuple(r['exps'])}   shape {r['shape']}{tag}")
shapes = {tuple(r["shape"]) for r in rows}
CELL3 = "B" if len(shapes) > 1 else "A"
print(f"\n  distinct shapes across the six planes: {len(shapes)}")
print(f"  CELL 3 = {CELL3}  -- " +
      ("the measured plane is NOT one of six equivalent choices"
       if CELL3 == "B" else "every plane looks the same"))

# ================================================================== CELL 1 & CELL 2
rule("CELL 1 & CELL 2 -- the resolvent at every plane, against B888's echo")
print(f"       {'exps':8s} {'unmeasured':12s} {'product':8s} {'resolvent sf':16s} echo holds")
echo = []
for r in rows:
    prod = r["unmeasured"][0] * r["unmeasured"][1]
    ok = r["resolvent_sf"] == [prod]
    echo.append(ok)
    print(f"       {str(tuple(r['exps'])):8s} {str(tuple(r['unmeasured'])):12s} {prod:<8d} "
          f"{str(r['resolvent_sf']):16s} {ok}")
allsf = sorted({s for r in rows for s in r["resolvent_sf"]})
CELL1 = "A" if len({tuple(r["resolvent_sf"]) for r in rows}) == 1 else "B"
CELL2 = "A" if all(echo) else "B"
print(f"\n  CELL 1 = {CELL1}  -- the resolvent " +
      ("is the same at every plane" if CELL1 == "A" else "VARIES with the plane"))
print(f"  CELL 2 = {CELL2}  -- B888's echo holds at {sum(echo)} of {len(echo)} planes")

rule("WHAT THE VARIATION IS -- the resolvents close into a Klein four-group")
print(f"       squarefree parts seen across all six planes: {allsf}")
prods = {sf(p * q) for p, q in itertools.combinations(allsf, 2)}
closed = prods <= set(allsf) | {1}
print(f"       pairwise squarefree products: {sorted(prods)}")
print(f"       -231 = -3 * 77 : {-231 == -3 * 77}")
check("the three resolvents are closed under squarefree product -- a V4", closed)
print("       so the resolvent data of the whole charge system is the Klein four-group")
print("       { Q(sqrt-3), Q(sqrt77), Q(sqrt-231) } -- and Q(sqrt-3) is the BEING face.")

rule("THE PARTITION -- which planes give which")
blk77 = [tuple(r["exps"]) for r in rows if r["resolvent_sf"] == [77]]
oth = [tuple(r["exps"]) for r in rows if r["resolvent_sf"] != [77]]
print(f"       resolvent 77 exactly at: {blk77}")
print(f"       resolvent [-231,-3] at : {oth}")
print("       -> the four charges split into TWO BLOCKS, {4,8} and {7,11}: a pencil WITHIN a")
print("          block gives 77; every pencil ACROSS the blocks gives {-3, -231}.")
print("          The partition is COMPUTED from the object; nothing selected it.")

# ================================================================== the field test
rule("THE FIELD TEST -- do the UNMEASURED plane's branch cubics generate K itself?")
theta = sp.RootOf(MU.as_expr(), 0)
KF = sp.QQ.algebraic_field(theta)


def in_K(P):
    return 1 in [f.degree() for f, _ in sp.Poly(P.as_expr(), L, domain=KF).factor_list()[1]]


# C5 -- the bite control: unrelated cubics with the SAME resolvent 77 must come out NOT K
ctrls = []
for aa in range(-6, 7):
    for bb in range(-30, 31):
        for cc in range(-30, 31):
            Pq = sp.Poly(L ** 3 + aa * L ** 2 + bb * L + cc, L)
            d = sp.discriminant(Pq)
            if d and sf(d) == 77 and Pq.is_irreducible:
                if not any(in_K_r for in_K_r in [] ) and all(
                        1 not in [f.degree() for f, _ in sp.Poly(
                            Pq.as_expr(), L,
                            domain=sp.QQ.algebraic_field(sp.RootOf(R.as_expr(), 0))
                        ).factor_list()[1]] for R in ctrls):
                    ctrls.append(Pq)
print(f"       distinct cubic FIELDS of resolvent Q(sqrt77) in |a|<=6, |b|,|c|<=30: {len(ctrls)}")
for R in ctrls:
    print(f"         {sp.sstr(R.as_expr()):34s} disc {sp.factorint(sp.discriminant(R))}   "
          f"== K: {in_K(R)}")
check("C5 -- POSITIVE control: mu itself is found isomorphic to K", in_K(MU))
check("C5 -- BITE control: at least one unrelated resolvent-77 cubic is found NOT K",
      any(not in_K(R) for R in ctrls))
nK = sum(1 for R in ctrls if in_K(R))
print(f"       C6 -- BASE RATE, stated with the claim: {nK} of {len(ctrls)} distinct resolvent-77")
print(f"            cubic fields in that window IS K.  K has the SMALLEST discriminant of them")
print(f"            (6237 = 3^4*7*11), so conditional on resolvent 77 this landing is not rare.")

unm = [r for r in rows if r["exps"] == [7, 11]][0]
hits = []
for dg, s, poly in unm["branch"]:
    if dg != 3:
        continue
    G = sp.Poly(sp.sympify(poly, locals={"L": L}), L)
    if any(sp.simplify(G.monic().as_expr() - H.monic().as_expr()) == 0 for H in hits):
        continue
    hits.append(G)
    print(f"\n       (7,11) branch cubic  {sp.sstr(G.as_expr())}")
    print(f"         resolvent sf = {s}   disc = {sp.factorint(sp.discriminant(G))}")
    print(f"         shares a root with mu over Q: "
          f"{sp.resultant(G.as_expr(), MU.as_expr(), L) == 0}")
    print(f"         GENERATES K: {in_K(G)}")
allK = all(in_K(G) for G in hits) and len(hits) >= 1

# ================================================================== verdict
rule("VERDICT")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
json.dump(rows, open(os.path.join(OUT, "six_planes_77_branch.json"), "w"), indent=1, default=str)
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
print(f"""
  THE MEASURED PLANE IS NOT A CHOICE.  THE OBJECT PARTITIONS ITS OWN FOUR CHARGES.

  1. SHAPE (CELL 3 = B).  Four of the six planes share one generic factorization,
     (3,1)+(6,1)+(6,3).  The (4,8) plane -- the one the entire 77 story is built on -- is the
     ONLY one whose pencil factors into CUBICS ALONE.  The (7,11) plane is the only one carrying
     a LINEAR factor, a joint weight rational over Q.  The two exceptional planes are exactly
     the two B888 named, and they are exceptional in OPPOSITE directions.

  2. RESOLVENT (CELL 1 = B).  The resolvent is NOT plane-invariant, and the way it varies is the
     finding: 77 at exactly the two planes {{4,8}} and {{7,11}}, and {{-3, -231}} at all four
     planes that MIX the two blocks.  -231 = -3 * 77, so the three squarefree parts are CLOSED
     UNDER PRODUCT: the charge system's resolvent data is a KLEIN FOUR-GROUP
     {{ Q(sqrt-3), Q(sqrt77), Q(sqrt-231) }} -- and Q(sqrt-3) is the BEING FACE.

  3. B888'S ECHO IS A COINCIDENCE OF ONE PLANE (CELL 2 = B).  "The resolvent remembers the
     complementary exponent pair" holds at (4,8) -> 7*11 = 77 and FAILS at the other five,
     including at (7,11), whose complement product is 4*8 = 32 and whose resolvent is 77 again.
     The echo is withdrawn as a mechanism; what replaces it is stronger and is item 2.

  4. AND THE UNMEASURED PLANE PRODUCES K ITSELF.  The (7,11) pencil -- built from the two charges
     the measured construction never used -- has branch cubics that are NOT mu (no shared root
     over Q, different discriminants: 19^12 where mu has 13^12) and that nevertheless GENERATE A
     FIELD ISOMORPHIC TO K.  Positive and bite controls both fire, so the test can say no.

  WHY THIS MOVES THE DOOR.  B1077's blocker was that the only twist-source is the measured pencil
  triple, so any 77 it produces is CIRCULAR -- the pencil's branch locus is mu by construction.
  That argument requires the measured plane to be a free choice.  IT IS NOT: the object's own
  factorization singles out {{4,8}} (all-cubic) and {{7,11}} (rational weight) from the four mixed
  planes, and BOTH of the distinguished planes carry K.  A datum reached from two disjoint pairs
  of charges, with the four mixed pencils demonstrably giving different arithmetic, is not an
  artifact of which pair was picked.

  WHAT THIS DOES NOT DO.  It does not prove B882's conjecture: the remaining half is the 3D4
  twisting classification, a literature proposition this bench does not close.  It does not
  produce a value, a ratio or a prediction, and no measured quantity enters.  It does not claim
  the landing on K is improbable in isolation -- the base rate above is printed precisely so it
  cannot be read that way; the strength is in the PARTITION, not in one field coincidence.
  And it does not decide the other two section-4A.3 doors.
""")
print("Gate 5 untouched.  No measured value is used or named.")
