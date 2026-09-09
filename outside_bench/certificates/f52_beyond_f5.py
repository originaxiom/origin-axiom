#!/usr/bin/env python3
"""MEMO 183 ADDENDUM 4's BLOCKER IS BROKEN: f_6, f_7, f_8 ... for m(5_2), by Park's
inverted Habiro route, with every step checked against something this bench already owned.

THE BLOCKER.  The reduced quantum trace gives f_0..f_5 for m(5_2) and no more.  Memo 183
addendum 4 showed the sequential single-index fit past f_5 CANNOT close: delta_d determines
only U_d(0) = sum_i c_{i,d} Q^i, not the five c_{i,d} separately, so each wrong split is
absorbed into the next correction.  Memo 185 then closed the NAIVE cyclotomic route by
computation, and named exactly one survivor: Park's *inverted* Habiro series
(arXiv:2106.03942), which the bench did not hold.  It arrived 2026-09-09.

THE ROUTE, and it is Park's, not this bench's.
  Conjecture 2:  F_K(x,q) = -(x^{1/2}-x^{-1/2}) sum_{m>=1} a_{-m}(K) / prod_{j=0}^{m-1}
                            (x + x^{-1} - q^j - q^{-j}),  expanded as a power series in x.
  The a_m are Habiro's coefficients in the prod (x + x^{-1} - q^j - q^{-j}) basis -- the
  basis memo 185 section 8's convention note singled out -- and a_{-m} is their extension
  to negative index, fixed by the quantum C-polynomial recursion
      Chat_{5_2}(Ehat,Qhat,q) = Ehat^2 + (q^2+q^3) Ehat Qhat + (q^6 - q^3 Ehat) Qhat^2
                                + (-q^7 + q^4 Ehat) Qhat^3,
      Qhat E^-m = q^m E^-m,   Ehat E^-m = E^-(m-1),
  plus the boundary ansatz that fixes a_{-1}.

PREREGISTERED.
  CELL -- do the blocks this route generates reproduce f_0..f_5, which were computed
  independently from Park's large-colour Verma R-matrix (park_large_color.py, memo 183
  addendum 1)?
     A  yes -> the route is live, and f_6 and beyond are DETERMINED.
     B  no  -> it is not, and the blocker stands.

CONTROLS -- every one against something already held, not against the paper's word.
  C1  the recursion is DERIVED here from Chat, and must reproduce BOTH of the relations
      Park prints for a_{-1} and a_{-2}.  (R80-1: his printed relations are checked, not
      assumed.)
  C2  the chain's a_{-1} must reproduce Park's printed series through every term he gives,
      -q^-1 + 1 - q^2 + q^5 - q^9 + q^14 - q^20 + q^27.
  C3  the FORWARD coefficients a_0..a_3, converted from THIS BENCH's own C_m(5_2) -- which
      came from the R-matrix state sum on Park's braid word, memo 185 addendum 3, touching
      no table and no paper -- must equal the a_m Park prints.
  C4  Conjecture 2 itself is checked on a knot where the answer is published: 4_1, whose
      a_{-m} = 1, against GM eq (11)'s four printed blocks.

Gate 5: exact Fraction arithmetic throughout.  No measured value.
"""
import os, json
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
QMAX, XMAX, DEPTH = 60, 9, 26

def qmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1 + e2
            if e <= QMAX: r[e] = r.get(e, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def qadd(a, b, s=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + s*c
        if r[e] == 0: del r[e]
    return r
def qdiv(num, den):
    if not num: return {}
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo - dl > QMAX: break
        k = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0) + k
        for a_, b_ in den.items():
            t = lo-dl+a_; cur[t] = cur.get(t, 0) - Fr(b_)*k
            if cur[t] == 0: del cur[t]
    return {e: c for e, c in res.items() if c}
def mono(e, c=1): return {e: Fr(c)}

# ---------- the recursion, DERIVED from Chat ----------
# coefficient of E^{-l} in Chat sum_m a_m E^{-m}:  a_{l+2} + A(l) a_{l+1} + B(l) a_l = 0
def A(l):
    d = {}
    for e, c in ((l+3, 1), (l+4, 1), (2*l+5, -1), (3*l+7, 1)): d[e] = d.get(e, 0) + c
    return {e: Fr(c) for e, c in d.items() if c}
def B(l):
    d = {}
    for e, c in ((2*l+6, 1), (3*l+7, -1)): d[e] = d.get(e, 0) + c
    return {e: Fr(c) for e, c in d.items() if c}

OK = {}
print("=" * 78); print("C1  the derived recursion vs the two relations Park PRINTS"); print("=" * 78)
import sympy as sp
qs = sp.symbols('q'); am2, am3 = sp.symbols('am2 am3')
def tosym(d): return sum(sp.Rational(c) * qs**e for e, c in d.items())
sol1 = sp.solve(sp.expand(1 + tosym(A(-2))*sp.Symbol('am1') + tosym(B(-2))*am2), sp.Symbol('am1'))[0]
park1 = sp.together((-qs**-1 + (1-qs)*am2)/(1+qs))
c1a = sp.simplify(sol1 - park1) == 0
sub = sp.simplify(sp.expand(sp.Symbol('am1') + tosym(A(-3))*am2 + tosym(B(-3))*am3).subs(sp.Symbol('am1'), sol1))
sol2 = sp.solve(sub, am2)[0]
park2 = sp.together((qs + (1+qs-qs**2-qs**3)*am3)/(1+qs**2+qs**3+qs**4))
c1b = sp.simplify(sol2 - park2) == 0
print("   a_-1 relation identical to Park's : %s" % c1a)
print("   a_-2 relation identical to Park's : %s" % c1b)
OK["C1  both printed relations derived from Chat, exactly"] = (c1a and c1b)

# ---------- the chain ----------
N, M = {}, {}
N[1] = qdiv(mono(0, -1), A(-2)); M[1] = qdiv({e: -c for e, c in B(-2).items()}, A(-2))
for k in range(2, DEPTH+1):
    den = qadd(M[k-1], A(-k-1))
    N[k] = qdiv({e: -c for e, c in N[k-1].items()}, den)
    M[k] = qdiv({e: -c for e, c in B(-k-1).items()}, den)
v = {DEPTH: N[DEPTH]}
for k in range(DEPTH-1, 0, -1): v[k] = qadd(N[k], qmul(M[k], v[k+1]))

print(); print("=" * 78); print("C2  a_-1 against every term Park prints"); print("=" * 78)
REF = {-1: -1, 0: 1, 2: -1, 5: 1, 9: -1, 14: 1, 20: -1, 27: 1}
got = v[1]
c2 = all(got.get(e, 0) == Fr(c) for e, c in REF.items()) and \
     all(got.get(e, 0) == 0 for e in range(-1, 28) if e not in REF)
print("   computed : %s" % " ".join("%+d q^%d" % (got[e], e) for e in sorted(got) if e <= 27 and got[e]))
print("   Park     : -1 q^-1 +1 q^0 -1 q^2 +1 q^5 -1 q^9 +1 q^14 -1 q^20 +1 q^27")
print("   every printed term reproduced, and every zero between them : %s" % c2)
OK["C2  a_-1 reproduces Park's printed series through q^27"] = c2

print(); print("=" * 78); print("C3  THIS BENCH's own C_m(5_2) -> a_m, vs Park's printed a_m")
print("=" * 78)
D52 = json.load(open(os.path.join(DATA, "cyclotomic_52.json")))
C = [dict((int(e), Fr(int(c))) for e, c in t) for t in D52["5_2"]["C"]]
PARK_A = {0: {0: 1}, 1: {2: -1, 4: -1}, 2: {5: 1, 7: 1, 8: 1, 11: 1},
          3: {9: -1, 11: -1, 12: -1, 13: -1, 15: -1, 16: -1, 17: -1, 21: -1}}
c3 = True
for m in range(4):
    conv = {e + m*(m+1)//2: ((-1)**m)*c for e, c in C[m].items()}
    good = conv == {e: Fr(c) for e, c in PARK_A[m].items()}
    c3 &= good
    print("   a_%d from our C_%d : %s" % (m, m, "MATCHES Park's printed a_%d" % m if good else "MISMATCH"))
OK["C3  our R-matrix C_m give Park's printed a_0..a_3 exactly"] = c3

# ---------- Conjecture 2 ----------
def blocks(aneg):
    def xmul(P, Q):
        R = [{} for _ in range(XMAX+1)]
        for i, pi in enumerate(P):
            if not pi: continue
            for j, qj in enumerate(Q):
                if i+j > XMAX or not qj: continue
                R[i+j] = qadd(R[i+j], qmul(pi, qj))
        return R
    def inv_quad(c):
        R = [{} for _ in range(XMAX+1)]; R[0] = {0: Fr(1)}
        for n in range(1, XMAX+1):
            t = qmul(c, R[n-1])
            if n >= 2: t = qadd(t, R[n-2], -1)
            R[n] = t
        return R
    S = [{} for _ in range(XMAX+1)]
    prod = [{} for _ in range(XMAX+1)]; prod[0] = {0: Fr(1)}
    for m in range(1, XMAX+1):
        c = {0: Fr(2)} if m == 1 else qadd({m-1: Fr(1)}, {-(m-1): Fr(1)})
        prod = xmul(prod, inv_quad(c))
        if m not in aneg: break
        for i in range(0, XMAX+1-m):
            S[m+i] = qadd(S[m+i], qmul(aneg[m], prod[i]))
    return [qadd(S[j+1], S[j], -1) for j in range(XMAX)]

print(); print("=" * 78); print("C4  Conjecture 2 on 4_1 (a_-m = 1), vs GM eq (11)"); print("=" * 78)
F41 = blocks({m: {0: Fr(1)} for m in range(1, XMAX+1)})
GM11 = [{0: Fr(1)}, {0: Fr(2)}, {-1: Fr(1), 0: Fr(3), 1: Fr(1)},
        {-2: Fr(2), -1: Fr(2), 0: Fr(5), 1: Fr(2), 2: Fr(2)}]
c4 = all(F41[j] == GM11[j] for j in range(4))
for j in range(4):
    print("   f_%d = %-40s  GM eq (11) : %s" % (j, dict(sorted(F41[j].items())), dict(sorted(GM11[j].items()))))
print("   all four blocks identical, no normalisation factor : %s" % c4)
OK["C4  Conjecture 2 exact on 4_1 against GM eq (11)"] = c4

print(); print("=" * 78); print("THE CELL  --  Conjecture 2 for m(5_2) vs the Verma-trace blocks")
print("=" * 78)
F = blocks(v)
BJ = json.load(open(os.path.join(DATA, "park_f52_blocks_w16.json")))
BL = {int(k): {int(e): Fr(int(c)) for e, c in t.items()} for k, t in BJ["blocks"].items()}
NC = {int(k): n for k, n in BJ["_counts"].items()}
cell = True
for j in sorted(BL):
    if j >= len(F): break
    pred, act = F[j], BL[j]
    lo = min(act); hor = min(lo + NC[j] - 1, QMAX - 2)
    ex = list(range(int(min(min(pred) if pred else lo, lo)), int(hor)+1))
    bad = [e for e in ex if pred.get(e, 0) != act.get(e, 0)]
    cell &= not bad
    print("   f_%d : %-9s over q^%d..q^%d  (%d coefficients)"
          % (j, "MATCH" if not bad else "MISMATCH", ex[0], ex[-1], len(ex)))
print("   CELL -> OUTCOME %s" % ("A" if cell else "B"))
OK["CELL -> A : the route reproduces every block the Verma trace could reach"] = cell

print(); print("=" * 78); print("PAST THE BLOCKER"); print("=" * 78)
NEW = {}
for j in range(6, XMAX):
    d = F[j]
    if not d: continue
    NEW[j] = d
    lo = min(d)
    print("   f_%d = %s ..." % (j, " ".join("%+d q^%d" % (d[lo+i], lo+i)
                                            for i in range(12) if d.get(lo+i, 0))))
json.dump({"_provenance": "Park arXiv:2106.03942 Conjecture 2 driven by his quantum "
           "C-polynomial recursion; every step controlled in certificates/f52_beyond_f5.py",
           "blocks": {str(j): {str(e): str(c) for e, c in d.items()} for j, d in NEW.items()}},
          open(os.path.join(DATA, "f52_blocks_beyond.json"), "w"))

print(); print("=" * 78); print("CONTROLS AND CELL"); print("=" * 78)
for k, val in OK.items(): print("   %-64s %s" % (k, "PASSED" if val else "FAILED"))
print("""
WHAT THIS CLOSES.  Memo 183 addendum 4's blocker -- f_6 and beyond for m(5_2) -- is broken.
The route is Park's and the credit is his; what is this bench's is that every step was
checked against something already held rather than taken from the page: his two printed
recursion relations were DERIVED from his own Chat, his a_-1 was RECOMPUTED and matches
every term he prints, his forward a_0..a_3 were reproduced from this bench's OWN R-matrix
colored Jones, and the conjecture itself was first verified on a knot with a published
answer.  Only then were f_6, f_7, f_8 read off.

WHAT IT DOES NOT CLOSE.  Conjecture 2 is a CONJECTURE.  What is established is that it
holds on 4_1 exactly and reproduces all six independently computed blocks of m(5_2); the
blocks past f_5 rest on it and are labelled as resting on it.  They are not theorems.""")
assert all(OK.values()), OK
