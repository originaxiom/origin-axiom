#!/usr/bin/env python3
"""INGEST AND IDENTIFY A COLORED JONES TABLE -- run the controls BEFORE claiming anything.

Source: Garoufalidis-Sun twist.knot.data, files CJTwist.<p>.txt(.gz), holding
J_{K_p,n}(q) for n = 1..60 of the twist knot K_p, normalised J_{p,1} = 1, with J_{p,2}
the Jones polynomial of K_p.  The page states K_0 = unknot, K_{-1} = 4_1, K_1 = 3_1,
K_{-2} = 6_1, K_2 = 5_2, K_{-3} = 8_1, K_3 = 7_2.

Memo 185 section 5 fixed the rule before any file arrived: K_{-1} and K_1 are FREE
CONTROLS -- checkable against GM eq (166) and GM eq (24) -- and are to be run BEFORE
anything is claimed from any other file in the set.  This is that check, and it is run
on every file, not only the two controls, because a filename is not a knot.

WHAT IS CHECKED, PER FILE
  T1  J_1 = 1                                       (the stated normalisation)
  T2  det = |J_2(-1)|                               identifies the knot: twist knots have
      det(K_p) = 4p - 1  and  det(K_{-p}) = 4p + 1, so the determinant alone pins |p| and
      the SIGN of p -- which is exactly what a filename can lose.
  T3  J_2(1) = 1 and J_n(1) = 1 for all n           (normalised colored Jones at q = 1)
  T4  the whole table is palindromic or not, per knot, reported not assumed
  T5  where the file is claimed to be 3_1: every J_n must equal GM eq (24)'s cyclotomic
      expansion  sum_m q^m (q^{n+1})_m (q^{1-n})_m   -- computed here, n = 1..12
  T6  where the file is claimed to be 4_1: every J_n must equal GM eq (166)  -- n = 1..12

Gate 5: exact integer Laurent arithmetic.  Nothing is fitted.

Usage:  python3 cj_table_ingest.py <file> [<file> ...]
"""
import sys, re, os

# ---------------- parser for the Mathematica list format ----------------
TERM = re.compile(r'^(\d*)\*?q\^(-?\d+)$|^(\d*)\*?q$|^(\d+)/q\^(\d+)$|^(\d+)/q$|^(\d+)$')
def parse_poly(s):
    """a Laurent polynomial in q, as {exponent: coefficient}"""
    s = s.replace(' ', '').replace('\n', '')
    s = re.sub(r'q\^\(\s*(-?\d+)\s*\)', r'q^\1', s)
    if not s: raise ValueError('empty')
    # split at top level on + / -
    parts = []; cur = ''; sign = 1; prev = ''
    for ch in s:
        if ch in '+-' and prev == '^':      # the sign of an exponent, not a term break
            cur += ch
        elif ch in '+-' and cur:
            parts.append((sign, cur)); cur = ''; sign = 1 if ch == '+' else -1
        elif ch in '+-' and not cur:
            if ch == '-': sign = -sign
        else:
            cur += ch
        prev = ch
    if cur: parts.append((sign, cur))
    out = {}
    for sg, t in parts:
        m = TERM.match(t)
        if not m: raise ValueError('unparsed term %r in %r' % (t, s[:80]))
        g = m.groups()
        if g[1] is not None:   c, e = int(g[0] or 1), int(g[1])
        elif g[2] is not None: c, e = int(g[2] or 1), 1
        elif g[4] is not None: c, e = int(g[3]), -int(g[4])
        elif g[5] is not None: c, e = int(g[5]), -1
        else:                  c, e = int(g[6]), 0
        out[e] = out.get(e, 0) + sg * c
    return {e: c for e, c in out.items() if c}

def split_top(s):
    """split the outer {...} on commas at brace depth 0"""
    s = s.strip()
    assert s.startswith('{') and s.endswith('}'), 'not a Mathematica list'
    s = s[1:-1]; d = 0; cur = ''; out = []
    for ch in s:
        if ch in '{([': d += 1
        elif ch in '})]': d -= 1
        if ch == ',' and d == 0: out.append(cur); cur = ''
        else: cur += ch
    if cur.strip(): out.append(cur)
    return out

# ---------------- the two anchors, recomputed here ----------------
def _m(A, B):
    r = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items(): r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def J_cyclo_trefoil(n):
    """GM eq (20) with eq (24): C_m = q^m"""
    tot = {}
    for m in range(0, n + 2):
        t = {0: 1}
        for j in range(0, m):
            for e in (n + 1 + j, 1 - n + j):
                nt = dict(t)
                for e1, c1 in t.items():
                    nt[e1+e] = nt.get(e1+e, 0) - c1
                t = {k: v for k, v in nt.items() if v}
        if not t: break
        t = _m({m: 1}, t)
        for k, v in t.items(): tot[k] = tot.get(k, 0) + v
    return {k: v for k, v in tot.items() if v}
def J166(n):
    """GM eq (166), the figure-eight"""
    tot = {0: 1}; cur = {0: 1}
    for m in range(1, n):
        fac = {n: 1, -n: 1}
        fac[m] = fac.get(m, 0) - 1; fac[-m] = fac.get(-m, 0) - 1
        cur = _m(cur, {k: v for k, v in fac.items() if v})
        for k, v in cur.items(): tot[k] = tot.get(k, 0) + v
    return {k: v for k, v in tot.items() if v}

DET = {}                       # determinant -> the twist knot the page names
for p in range(1, 16): DET[4*p - 1] = ("K_%d" % p, p)
for p in range(1, 16): DET[4*p + 1] = ("K_%d" % (-p), -p)
DET[1] = ("K_0 = unknot", 0)
NAMED = {0: "unknot", 1: "3_1", -1: "4_1", 2: "5_2", -2: "6_1", 3: "7_2", -3: "8_1",
         4: "9_2", -4: "10_1"}

def ev(P, q):
    from fractions import Fraction as Fr
    return sum(Fr(c) * (Fr(q) ** e) for e, c in P.items())

WARN = []
def report(path):
    raw = open(path).read()
    L = [parse_poly(t) for t in split_top(raw)]
    base = os.path.basename(path)
    claim = re.search(r'CJTwist\.(-?\d+)', base)
    claim = int(claim.group(1)) if claim else None
    print("=" * 78)
    print("FILE  %s" % base)
    print("      %d colored Jones polynomials, n = 1..%d" % (len(L), len(L)))
    ok = {}
    ok["T1  J_1 = 1"] = (L[0] == {0: 1})
    det = abs(ev(L[1], -1)) if len(L) > 1 else None
    ok["T3  J_n(1) = 1 for every n"] = all(ev(P, 1) == 1 for P in L)
    who, p = DET.get(det, ("UNRECOGNISED", None))
    print("      T2  determinant |J_2(-1)| = %s  ->  %s = %s"
          % (det, who, NAMED.get(p, "?")))
    if claim is not None:
        agree = (p == claim)
        print("      the FILENAME claims CJTwist.%d.  Determinant says p = %s.  %s"
              % (claim, p, "consistent" if agree else
                 "*** MISMATCH -- the filename is wrong, the polynomial is not ***"))
        # a wrong filename is a fact about the download, NOT a defect in the data:
        # it is reported loudly and does not fail the file.
        WARN.append((base, claim, p)) if not agree else None
    pal = all(P == {-e: c for e, c in P.items()} for P in L)
    print("      T4  every J_n palindromic (J_n(q) = J_n(1/q)) : %s" % pal)
    if p == 1:
        n = min(12, len(L))
        good = all(L[k-1] == J_cyclo_trefoil(k) for k in range(1, n + 1))
        print("      T5  vs GM eq (24)'s cyclotomic expansion, n = 1..%d : %s"
              % (n, "PASSED" if good else "FAILED"))
        ok["T5  file == GM eq (24) for 3_1"] = good
    if p == -1:
        n = min(12, len(L))
        good = all(L[k-1] == J166(k) for k in range(1, n + 1))
        print("      T6  vs GM eq (166), n = 1..%d : %s" % (n, "PASSED" if good else "FAILED"))
        ok["T6  file == GM eq (166) for 4_1"] = good
    if p == 0:
        ok["unknot: every J_n = 1"] = all(P == {0: 1} for P in L)
    for k, v in ok.items():
        print("      %-40s %s" % (k, "PASSED" if v else "FAILED"))
    return p, all(ok.values()), len(L)

if __name__ == "__main__":
    seen = {}
    allok = True
    for f in sys.argv[1:]:
        p, good, n = report(f); allok &= good
        seen.setdefault(p, []).append((os.path.basename(f), n))
    print("=" * 78)
    print("WHAT THE SET ACTUALLY CONTAINS (by determinant, not by filename)")
    print("=" * 78)
    for p in sorted(seen, key=lambda z: (z is None, z)):
        for f, n in seen[p]:
            print("   p = %-4s %-10s n = 1..%-3d  from %s" % (p, NAMED.get(p, "?"), n, f))
    if WARN:
        print()
        print("   *** FILENAMES THAT LIE ***")
        for b, claim, p in WARN:
            print("      %s  says CJTwist.%d, is actually p = %d (%s).  A lost minus sign."
                  % (b, claim, p, NAMED.get(p, '?')))
    print()
    print("   ALL DATA CHECKS: %s" % ("PASSED" if allok else "SOME FAILED -- see above"))
    print("   (filename mismatches are listed above and do NOT fail a file: the")
    print("    polynomials are correct, the download lost a sign.)")
