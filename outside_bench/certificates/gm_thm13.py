#!/usr/bin/env python3
"""GUKOV-MANOLESCU THEOREM 1.3 VERIFIED -- the last unverified GM input in memo 180's ledger.

Memo 180's ledger, row "Thm 1.3 -- F_K for torus knots":
   "not independently verified.  Now checkable with memo 179's calculator; not yet done"
and its section 5 lists it first among what remains.  Memo 177 addendum 2's torus arm
(c_eff = 0 at every slope, because every Xi_k is a single monomial) rests on it.

It is checked here against a DIFFERENT paper's machine: Park's large color R-matrix on
the lowest weight Verma module (arXiv:2004.02087 eq (17), (18), (25)-(26)), which this
bench implemented from scratch in certificates/park_large_color.py and controlled there
against every block Park prints for m(5_2).  Neither theorem is used to derive the other.

GM eq (2):  F_{T(s,t)}(x,q) = q^{(s-1)(t-1)/2} (1/2) sum_{m>=1} eps_m (x^{m/2} - x^{-m/2})
                              q^{(m^2 - (st-s-t)^2)/(4st)}
GM eq (3):  eps_m = -1 if m = st+s+t or st-s-t  (mod 2st)
                    +1 if m = st+s-t or st-s+t  (mod 2st)
                     0 otherwise
GM p.5:     for the mirror (negative torus knot),  F_{m(K)}(x,q) = F_K(x, q^{-1}).

The negative torus knot T(2,-t) is the closure of sigma_1^{-t} on two strands, which is
the setting Park's lowest weight Verma R-matrix is built for.

WHAT COMES OUT:

   f_j  =  exactly GM's monomial, for every j where eps_{2j+1} != 0,
   f_j  =  0,                     for every j where eps_{2j+1}  = 0,

with NO normalisation factor at all.  Every sign, every exponent, and the whole
vanishing pattern of eps_m is reproduced.

Gate 5: exact integer arithmetic.  No fitted constant.

CONTROLS:
  C1  the blocks are stable in the weight cutoff: identical at W = 12 and W = 16, so
      the stratified sum has converged and the answer is read, not guessed.  How many
      were already settled at W = 8 is reported too, so the convergence is visible.
  C2  two knots, T(2,-3) and T(2,-5), with different eps patterns and different
      vanishing sets.
"""
import sys
from fractions import Fraction as Fr
sys.path.insert(0, '/tmp/k52')

# ---- Park's lowest weight Verma R-matrix (same code as park_large_color.py) --------
def pmul(A, B):
    r = {}
    for (a1,b1), c1 in A.items():
        for (a2,b2), c2 in B.items():
            k = (a1+a2, b1+b2); r[k] = r.get(k,0)+c1*c2
    return {k:c for k,c in r.items() if c}
def padd(A, B, sc=1):
    r = dict(A)
    for k,c in B.items():
        r[k] = r.get(k,0)+sc*c
        if r[k] == 0: del r[k]
    return r
ONE = {(0,0):1}
def mono(a,b,c=1): return {(a,b):c}
def qint(m):  return {(m-1-2*i,0):1 for i in range(m)}
def qfact(m):
    r = dict(ONE)
    for i in range(1,m+1): r = pmul(r, qint(i))
    return r
def pdivexact(num, den):
    num = {a:c for (a,b),c in num.items()}; den = {a:c for (a,b),c in den.items()}
    res = {}; cur = dict(num)
    while cur:
        lo = min(cur); dl = min(den)
        k = Fr(cur[lo], den[dl]); res[lo-dl] = res.get(lo-dl,0)+k
        for x,y in den.items():
            t = lo-dl+x; cur[t] = cur.get(t,0)-y*k
            if cur[t] == 0: del cur[t]
    out = {}
    for a,c in res.items():
        assert Fr(c).denominator == 1
        if c: out[(a,0)] = int(c)
    return out
_QB = {}
def qbin(n,k):
    if k < 0 or k > n: return {}
    if (n,k) not in _QB: _QB[(n,k)] = pdivexact(qfact(n), pmul(qfact(k), qfact(n-k)))
    return _QB[(n,k)]
_RM = {}
def Rminus(a,b):
    if (a,b) in _RM: return _RM[(a,b)]
    j,i = b,a; out = {}
    for k in range(0,i+1):
        coef = dict(qbin(i,k))
        for l in range(1,k+1):
            coef = pmul(coef, padd(ONE, mono(-2*(j+l),2), -1))
        e = i-k
        coef = pmul(coef, mono(-(2*(e*j)+e*k+(e+j+1)), 1+(e+j)))
        t = (j+k, e); out[t] = padd(out.get(t,{}), coef)
    _RM[(a,b)] = {t:v for t,v in out.items() if v}
    return _RM[(a,b)]
def step(vec):
    out = {}
    for st, co in vec.items():
        for (na,nb), cc in Rminus(st[0], st[1]).items():
            ns = (na,nb); p = pmul(co, cc)
            if not p: continue
            out[ns] = padd(out.get(ns,{}), p)
    return {s:v for s,v in out.items() if v}
def blocks(t, W, JM):
    """F^+ of the closure of sigma_1^{-t} on two strands, weights w <= W"""
    TOT = {}
    for w in range(0, W+1):
        st = (0, w); vec = {st: dict(ONE)}
        for _ in range(t): vec = step(vec)
        d = vec.get(st)
        if d: TOT = padd(TOT, pmul(d, mono(1+2*w, -1)))   # x^{-1/2} q^{1/2} q^w, N = 2
    F = padd(pmul(TOT, mono(0,1)), pmul(TOT, mono(0,-1)), -1)
    B = {}
    for (a,b), c in F.items():
        if b % 2 == 0 or a % 2: continue
        j = (b-1)//2
        if 0 <= j <= JM: B.setdefault(j,{})[a//2] = B.setdefault(j,{}).get(a//2,0)+c
    return {j:{e:v for e,v in d.items() if v} for j,d in B.items()}

def gm(s, t, J):
    """GM eq (2)-(3) for the MIRROR T(s,-t): exponent negated"""
    st = s*t; M = 2*st; c = st-s-t
    E = {(st+s+t) % M: -1, (st-s-t) % M: -1, (st+s-t) % M: 1, (st-s+t) % M: 1}
    out = {}
    for j in range(J+1):
        m = 2*j+1; e = E.get(m % M, 0)
        if not e: out[j] = None; continue
        assert (m*m - c*c) % (4*st) == 0
        out[j] = (e, -(Fr((s-1)*(t-1), 2) + Fr(m*m-c*c, 4*st)))
    return out
def times1mq(d):
    r = dict(d)
    for e,c in d.items():
        r[e+1] = r.get(e+1,0)-c
        if r[e+1] == 0: del r[e+1]
    return {e:c for e,c in r.items() if c}

JM = 9
OK = {}
for (s_, t_, Ws) in ((2, 3, (8, 12, 16)), (2, 5, (8, 12, 16))):
    print("="*78)
    print("T(%d,-%d) = closure of sigma_1^{-%d} on two strands  vs  GM Theorem 1.3" % (s_, t_, t_))
    print("="*78)
    G = gm(s_, t_, JM)
    snaps = {}
    for W in Ws:
        B = blocks(t_, W, JM)
        snaps[W] = {j: B.get(j, {}) for j in range(JM+1)}
    stable = all(snaps[Ws[-2]][j] == snaps[Ws[-1]][j] for j in range(JM+1))
    part = sum(1 for j in range(JM+1) if snaps[Ws[0]][j] == snaps[Ws[-1]][j])
    print("   blocks identical at weight cutoffs %d and %d : %s   (already at cutoff %d: %d of %d)"
          % (Ws[-2], Ws[-1], stable, Ws[0], part, JM+1))
    match = True
    for j in range(JM+1):
        d = snaps[Ws[-1]][j]; g = G[j]
        tgt = {} if g is None else {g[1]: g[0]}
        ok = (d == tgt)
        match &= ok
        print("   f_%-2d = %-18s   GM Thm 1.3, mirrored : %-18s  %s"
              % (j, " ".join("%+d q^{%s}" % (c, e) for e, c in sorted(d.items())) or "0",
                 "0" if g is None else "%+d q^{%s}" % (g[0], g[1]), "ok" if ok else "MISMATCH"))
    OK["C1 stable T(%d,-%d)" % (s_, t_)] = stable
    OK["C2 matches T(%d,-%d)" % (s_, t_)] = match
print("="*78)
print("CONTROLS:", {k: ("PASSED" if v else "FAILED") for k, v in OK.items()})
if not all(OK.values()): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("""
GM Theorem 1.3 is reproduced EXACTLY for T(2,-3) and T(2,-5), with no normalisation
factor: every eps_m = +-1 gives GM's monomial with its sign and its exponent, and every
eps_m = 0 gives exactly zero.  The check runs on a different paper's machine -- Park's
large color R-matrix on the lowest weight Verma module -- so neither theorem is used to
derive the other.  Memo 180's last unverified GM input is closed.""")
