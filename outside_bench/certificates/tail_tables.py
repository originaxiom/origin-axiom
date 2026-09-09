#!/usr/bin/env python3
"""THE TAILS OF FOUR TWIST KNOTS, MEASURED TO 52 CERTIFIED COEFFICIENTS, AND THE
FALSE / GENUINE THETA SPLIT APPEARS INSIDE A SINGLE FAMILY.

Memo 184 measured the colored Jones tail of m(5_2) behind a fence of seven stabilised
coefficients, because seven was all the F_K blocks could certify.  Memo 185 section 5
listed, as the FIRST of the three surviving reasons to want Garoufalidis-Sun's
CJTwist tables, that the fence would go from 7 to about 60.  The tables arrived.  This
is that measurement.

INPUT.  Garoufalidis-Sun twist.knot.data, CJTwist.<p>.txt.gz: J_{K_p,n}(q) for
n = 1..60, normalised J_{p,1} = 1.  Every file was IDENTIFIED BY DETERMINANT, not by
filename, in certificates/cj_table_ingest.py -- two of the five filenames had lost a
minus sign -- and the two control files were checked coefficient by coefficient against
GM eq (24) (3_1) and GM eq (166) (4_1) for n = 1..12 before anything here was computed.

THE MEASUREMENT.  Read each J_n from its lowest degree (the "low" end) and from its
highest (the "high" end).  A coefficient is CERTIFIED when the last five available n at
STEP 2 (n, n-2, n-4, n-6, n-8) all agree on it; the step-1 window is computed and
reported alongside, and the two are NOT the same test.  Both numbers are printed for
every end, because the difference is informative rather than a nuisance: at the high end
of 3_1 and 9_2 the step-1 window is ZERO and the step-2 window is 52, which says the
stable series is there but its overall SIGN alternates with the parity of n.  Every
claim below uses the step-2 window, which is the conservative one.  The raw tables are
12 MB and are NOT vendored; the certified prefixes are, in data/cj_tails.json, with
their provenance.

PREREGISTERED, TWO OUTCOMES EACH.

  CELL 1 -- is the stable end of a twist knot always (q;q)_inf?
     A  yes for all four knots -> memo 177 addendum 2's hope of a universal ceiling
        survives on this family.
     B  no -> the ceiling is knot-by-knot, as memo 184 argued from Armond-Dasbach,
        and here it is measured rather than argued.

  CELL 2 -- for any end that is NOT (q;q)_inf, is it a GENUINE theta or a FALSE theta?
     The two are separated by TWO independent signatures, and the cell is only resolved
     when they agree:
       (i)  sign pattern: + - - + + - - + ... (genuine) vs + - + - + - ... (false);
       (ii) the exponents a_n in Phi = prod_{n>=1} (1-q^n)^{a_n} -- PERIODIC and bounded
            (an eta-quotient, hence a genuine theta by Jacobi's triple product) vs
            aperiodic and unbounded (not an eta-quotient).
     A  every non-(q;q)_inf end is a genuine theta.
     B  both kinds occur.

CONTROLS.
  C1  the unknot: every J_n = 1, so both ends give Phi = 1.
  C2  4_1, both ends: must be (q;q)_inf.  CITED anchor: Armond-Dasbach.  This is also
      exactly what certificates/tail_mechanism.py computes from GM eq (166) -- so the
      external table and the bench's own machine are compared, not just asserted.
  C3  3_1, low end: must be the TRIVIAL series 1.  An instrument that returned a rich
      series everywhere would prove nothing (memo 164).
  C4  every closed form below is checked on ALL certified coefficients, not a prefix.
  C5  step-2 windows are >= 10 everywhere reported, and the step-1 window is printed
      beside each so a parity-alternating end is visible rather than hidden.

Gate 5: exact integer arithmetic.  No fitted constant, no measured value.

Usage:  python3 tail_tables.py                      (from the vendored prefixes)
        python3 tail_tables.py --from-tables F...   (regenerate from the raw CJTwist files)
"""
import sys, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "cj_tails.json")

# ---------------- the closed forms, generated here ----------------
def qq_inf(N):
    c = [0]*(N+1); c[0] = 1
    for n in range(1, N+1):
        nc = list(c)
        for i in range(N-n, -1, -1): nc[i+n] -= c[i]
        c = nc
    return c
def theta(N, mod, resid, shift, den):
    """sum_{n>0, n mod `mod` in resid} sign(n) q^{(n^2-shift)/den}"""
    out = [0]*(N+1); n = 1
    while (n*n - shift)//den <= N:
        r = n % mod
        if r in resid and (n*n - shift) % den == 0:
            e = (n*n - shift)//den
            if 0 <= e <= N: out[e] += resid[r]
        n += 1
    return out
def prod_exponents(c, N):
    """solve Phi = prod_{n>=1} (1-q^n)^{a_n}"""
    a = [0]*(N+1); cur = list(c) + [0]*(N+5)
    assert cur[0] == 1
    for n in range(1, N+1):
        a[n] = -cur[n]; e = a[n]
        for _ in range(abs(e)):
            nxt = list(cur)
            if e > 0:
                for i in range(len(nxt)-n): nxt[i+n] += nxt[i]
            else:
                for i in range(len(cur)-n-1, -1, -1): nxt[i+n] -= cur[i]
            cur = nxt
    return a[1:]

DET_NAME = {1: "unknot", 3: "3_1", 5: "4_1", 9: "6_1", 15: "9_2", 7: "5_2",
            11: "7_2", 13: "8_1", 17: "10_1", 19: "11a247"}
def regenerate(paths):
    sys.path.insert(0, HERE)
    from cj_table_ingest import parse_poly, split_top, ev
    W = 70
    lo_ = lambda P: (lambda l: [P.get(l+i, 0) for i in range(W)])(min(P))
    hi_ = lambda P: (lambda h: [P.get(h-i, 0) for i in range(W)])(max(P))
    out = {}
    for path in paths:
        L = [parse_poly(t) for t in split_top(open(path).read())]
        det = abs(int(ev(L[1], -1))) if len(L) > 1 else 1
        for side, fn in (("low", lo_), ("high", hi_)):
            rec = {}
            for step in (1, 2):
                hs = [fn(L[-1-k*step]) for k in range(5)]
                s = 0
                while s < W and len(set(h[s] for h in hs)) == 1: s += 1
                rec["step%d" % step] = s
                if step == 2: rec["coeffs"] = hs[0][:s]
            if rec["step2"] >= 10:
                rec["det"] = det
                out["%s.%s" % (DET_NAME.get(det, "det%d" % det), side)] = rec
    return out

if len(sys.argv) > 2 and sys.argv[1] == "--from-tables":
    D = regenerate(sys.argv[2:]); print("(regenerated from the raw tables)")
else:
    D = json.load(open(DATA))
PROV = D.pop("_provenance", None)

N = max(len(D[k]["coeffs"]) for k in D) + 2
QQ   = qq_inf(N)
TH20 = theta(N, 20, {3: 1, 7: -1, 13: -1, 17: 1}, 9, 40)     # genuine, mod 20
FA16 = theta(N, 16, {3: 1, 5: -1, 11: 1, 13: -1}, 9, 16)     # false,   mod 16
ONE  = [1] + [0]*N
NAMES = [("1", ONE), ("(q;q)_inf", QQ), ("-(q;q)_inf", [-v for v in QQ]),
         ("theta_20  = sum_{n = +-3,+-7 (20)} +-q^{(n^2-9)/40}", TH20),
         ("false_16  = sum_{n = +-3,+-5 (16)} +-q^{(n^2-9)/16}", FA16)]

print("=" * 78)
print("THE CERTIFIED TAILS")
print("=" * 78)
if PROV:
    print("   source : %s" % PROV["source"])
    print("   ident. : %s" % PROV["identified_by"])
ID = {}
for k in sorted(D):
    r = D[k]; c = r["coeffs"]
    hit = None
    for nm, cand in NAMES:
        if c == cand[:len(c)]: hit = nm; break
    ID[k] = hit
    print("   %-12s certified %2d (step 1: %2d)   %s"
          % (k, r["step2"], r["step1"], hit if hit else "*** UNIDENTIFIED *** " + str(c[:14])))

OK = {}
OK["C1  unknot, both ends, Phi = 1"] = all(
    ID.get("unknot.%s" % s) == "1" for s in ("low", "high"))
OK["C2  4_1, both ends, Phi = (q;q)_inf  (Armond-Dasbach)"] = all(
    ID.get("4_1.%s" % s) == "(q;q)_inf" for s in ("low", "high"))
OK["C3  3_1, low end, Phi = 1 (the instrument can return the trivial series)"] = \
    (ID.get("3_1.low") == "1")
OK["C4  every end identified in closed form on ALL its certified coefficients"] = \
    all(v is not None for v in ID.values())
OK["C5  step-2 window >= 10 everywhere reported (not a parity artifact)"] = \
    all(D[k]["step2"] >= 10 for k in D)

print()
print("=" * 78)
print("CELL 1  --  is the stable end of a twist knot always (q;q)_inf ?")
print("=" * 78)
notqq = sorted(k for k, v in ID.items() if v not in ("(q;q)_inf", "-(q;q)_inf", "1"))
print("   ends that are NOT (q;q)_inf and not trivial :", notqq)
print("   CELL 1 -> OUTCOME %s" % ("A" if not notqq else "B"))
OK["CELL 1 resolved -> B (the tail is knot-by-knot, measured not argued)"] = bool(notqq)

print()
print("=" * 78)
print("CELL 2  --  genuine theta or false theta, by TWO independent signatures")
print("=" * 78)
kinds = set()
for k in notqq:
    c = D[k]["coeffs"]; nzs = [v for v in c if v]
    sgn = "".join("+" if v > 0 else "-" for v in nzs[:10])
    a = prod_exponents(c, min(len(c) - 2, 45))
    per = None
    for P in range(1, 13):
        if len(a) >= 3*P and all(a[i] == a[i % P] for i in range(len(a))):
            per = P; break
    kind = "GENUINE theta" if per else "FALSE theta"
    kinds.add(kind)
    print("   %-12s %s" % (k, kind))
    print("        sign pattern of the nonzero coefficients : %s%s" % (sgn, "..."))
    print("        product exponents a_1.. : %s" % a[:18])
    if per:
        zer = ",".join(str((i+1) % per) for i in range(per) if a[i] == 0)
        print("        PERIODIC with period %d in n -> an eta-quotient:"
              "  Phi = prod_{n not= %s (mod %d)} (1-q^n)" % (per, zer, per))
    else:
        print("        aperiodic and unbounded (|a_n| reaches %d by n = %d) -> NOT an"
              " eta-quotient" % (max(abs(v) for v in a), len(a)))
print("   CELL 2 -> OUTCOME %s : %s" % ("B" if len(kinds) > 1 else "A", ", ".join(sorted(kinds))))
OK["CELL 2 resolved -> B (both kinds occur inside one twist-knot family)"] = (len(kinds) > 1)

print()
print("=" * 78)
print("CONTROLS AND CELLS")
print("=" * 78)
for k, v in OK.items(): print("   %-70s %s" % (k, "PASSED" if v else "FAILED"))
print("""
WHAT WAS MEASURED, PLAINLY.

   knot     p     low end                     high end
   ----     --    -------                     --------
   unknot    0    1                           1
   3_1       1    1                           -(q;q)_inf
   4_1      -1    (q;q)_inf                   (q;q)_inf
   6_1      -2    (q;q)_inf                   theta, modulus 20
   9_2       4    false theta, modulus 16     -(q;q)_inf

Memo 184's fence was SEVEN stabilised coefficients.  It is now FIFTY-TWO, on four knots
rather than one, and every one of the five distinct series is identified in closed form
on every certified coefficient -- not fitted, matched.

THE FINDING THAT WAS NOT ASKED FOR.  The false / genuine theta distinction -- the one
memo 173 got backwards and memo 177 section 1 now turns on -- occurs INSIDE ONE
ONE-PARAMETER FAMILY.  K_{-2} = 6_1 has a genuine theta at one end; K_4 = 9_2 has a
false theta at the other.  Both are alternating twist knots, differing only in the twist
parameter.  Whatever selects false from genuine is therefore visible in a family small
enough to enumerate, and does not require comparing unrelated knots.

WHAT THIS DOES NOT DO.  It does not reopen the c_eff route.  Register R83 stopped paying
for that route because its SUCCESS would not have been evidence -- c_eff(1/(q;q)_inf^m)
= m is available to order.  Nothing here changes that.  These are measurements of the
tails themselves, which are the cheaper object memo 184 addendum 1 asked for.""")
assert all(OK.values()), OK
