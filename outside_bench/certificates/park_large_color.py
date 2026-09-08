#!/usr/bin/env python3
"""PARK'S LARGE COLOR R-MATRIX, IMPLEMENTED FROM THE PAPER AND CONTROLLED.

Source: Sunghyuk Park, arXiv:2004.02087v2.
  eq (17)  Rcheck on the LOWEST weight Verma module V^l_infty
  eq (18)  Rcheck^{-1} = P Rcheck|_{x->1/x, q->1/q} P
  eq (25)  reduced stratified quantum trace, Tr'_{q,eta} beta_{V^l}
             = x^{-(N-1)/2} q^{(N-1)/2} sum_{w>=0} Tr beta'(w) q^w eta^w
  eq (26)  Tr'_q beta = lim_{eta -> 1}
  eq (31)  (x^{1/2} - x^{-1/2}) Tr'_q beta_{V^l} = F^+_{m(5_2)} = x^{1/2} sum_j f_j x^j
           for beta = sigma_2^{-3} sigma_1^{-1} sigma_2 sigma_1^{-1}

WHY THIS EXISTS.  Memo 183 shows the quantum A-polynomial printed in Park eq (32)
does not annihilate F^+_{m(5_2)}, so the recursion route to f_4 and beyond is dead.
Eq (32) is not the only route: the blocks come from the R-matrix directly, which is
Park's own method and needs no A-polynomial at all.  This is that computation.

WHAT IT SETTLES.  Park's printed f_0, f_1, f_2, f_3 are all REPRODUCED here, from an
implementation that shares nothing with them but the paper's braid word -- so the
defect memo 183 localises is in eq (32) and NOT in his blocks.  That was the one
remaining way memo 183 could have been wrong.

Gate 5: exact integer arithmetic in u = q^{1/2}, s = x^{1/2}.  No measured input.

CONTROLS (all must fire):
  C1  f_0, f_1, f_2, f_3 reproduce Park's printed series, every coefficient.
  C2  the answer does not depend on the x-degree truncation: the same blocks come
      out at margin M and margin M+5.  (An earlier margin that was too tight gave a
      STABLE BUT WRONG f_3 -- recorded, because a stability check alone did not
      catch it; only widening the window did.  Memo 164: control passing is not
      instrument working.)
  C3  the stratified sum has converged in the total weight w: the reported
      coefficients are identical at cutoffs w = W-1 and w = W.
"""
import sys, json
from fractions import Fraction as Fr

W      = int(sys.argv[1]) if len(sys.argv) > 1 else 13
JTGT   = int(sys.argv[2]) if len(sys.argv) > 2 else 4      # blocks f_0..f_JTGT wanted
MARGIN = int(sys.argv[3]) if len(sys.argv) > 3 else 5      # extra x-degree head-room

# ---------- Laurent polynomials in (u, s), key (a,b) = (2*exp q, 2*exp x) ----------
def pmul(A, B):
    r = {}
    for (a1,b1), c1 in A.items():
        for (a2,b2), c2 in B.items():
            k = (a1+a2, b1+b2); r[k] = r.get(k,0) + c1*c2
    return {k:c for k,c in r.items() if c}
def padd(A, B, sc=1):
    r = dict(A)
    for k,c in B.items():
        r[k] = r.get(k,0) + sc*c
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
            t = lo-dl+x; cur[t] = cur.get(t,0) - y*k
            if cur[t] == 0: del cur[t]
    out = {}
    for a,c in res.items():
        assert Fr(c).denominator == 1
        if c: out[(a,0)] = int(c)
    return out
_QB = {}
def qbin(n,k):
    if k < 0 or k > n: return {}
    if (n,k) not in _QB:
        _QB[(n,k)] = pdivexact(qfact(n), pmul(qfact(k), qfact(n-k)))
    return _QB[(n,k)]

# ---------- eq (17) and eq (18); the framing factor q^{(n^2-1)/4} is dropped ----------
_RP = {}; _RM = {}
def Rplus(a,b):
    if (a,b) in _RP: return _RP[(a,b)]
    j,i = a,b; out = {}
    for k in range(0,i+1):
        coef = dict(qbin(i,k))
        for l in range(1,k+1):
            coef = pmul(coef, padd(ONE, mono(2*(j+l),-2), -1))     # 1 - x^-1 q^{j+l}
        e = i-k
        coef = pmul(coef, mono(2*(e*j)+e*k+(e+j+1), -1-(e+j)))
        t = (e, j+k); out[t] = padd(out.get(t,{}), coef)
    _RP[(a,b)] = {t:v for t,v in out.items() if v}
    return _RP[(a,b)]
def Rminus(a,b):
    if (a,b) in _RM: return _RM[(a,b)]
    j,i = b,a; out = {}
    for k in range(0,i+1):
        coef = dict(qbin(i,k))                                     # q-binomial is q<->1/q even
        for l in range(1,k+1):
            coef = pmul(coef, padd(ONE, mono(-2*(j+l),2), -1))     # 1 - x q^{-(j+l)}
        e = i-k
        coef = pmul(coef, mono(-(2*(e*j)+e*k+(e+j+1)), 1+(e+j)))
        t = (j+k, e); out[t] = padd(out.get(t,{}), coef)           # P applied
    _RM[(a,b)] = {t:v for t,v in out.items() if v}
    return _RM[(a,b)]

WORD = [(2,-1),(2,-1),(2,-1),(1,-1),(2,+1),(1,-1)]    # bottom to top, Park's convention
def step(vec, pos, sign, BLO, BHI):
    out = {}; R = Rplus if sign > 0 else Rminus
    for st, co in vec.items():
        a, b = st[pos-1], st[pos]
        for (na,nb), cc in R(a,b).items():
            ns = st[:pos-1] + (na,nb) + st[pos+1:]
            p = {}
            for (a1,b1), c1 in co.items():
                for (a2,b2), c2 in cc.items():
                    bb = b1+b2
                    if bb < BLO or bb > BHI: continue
                    k = (a1+a2, bb); p[k] = p.get(k,0) + c1*c2
            p = {k:c for k,c in p.items() if c}
            if not p: continue
            cur = out.get(ns)
            if cur is None: out[ns] = p
            else:
                for k,c in p.items():
                    cur[k] = cur.get(k,0)+c
                    if cur[k] == 0: del cur[k]
    return {s:v for s,v in out.items() if v}

def run(W, JMAX):
    TOT = {}; SNAP = {}
    for w in range(0, W+1):
        BHI = 2*JMAX+5+(1+w); BLO = 4-w-3
        acc = {}
        for A in range(w+1):
            vec = {(0,A,w-A): dict(ONE)}
            for pos, sg in WORD: vec = step(vec, pos, sg, BLO, BHI)
            d = vec.get((0,A,w-A))
            if d: acc = padd(acc, d)
        acc = pmul(acc, mono(2+2*w, -2))              # x^{-(N-1)/2} q^{(N-1)/2} q^w, N=3
        TOT = padd(TOT, acc); SNAP[w] = dict(TOT)
    return SNAP
def blocks(T, JMAX):
    F = padd(pmul(T, mono(0,1)), pmul(T, mono(0,-1)), -1)     # (x^{1/2} - x^{-1/2}) Tr'
    B = {}
    for (a,b), c in F.items():
        if b % 2 == 0 or a % 2: continue                       # F^+ = x^{1/2} sum f_j x^j
        j = (b-1)//2
        if 0 <= j <= JMAX: B.setdefault(j,{})[a//2] = B.setdefault(j,{}).get(a//2,0)+c
    return {j:{e:c for e,c in d.items() if c} for j,d in B.items()}

PARK = {0:(-1,[-1,1,0,-1,0,0,1,0,0,0,-1]),
        1:(-1,[-1,1,1,-1,-1,-1,1,1,1,1]),
        2:(-1,[-1,2,1,-1,-2,-2,1,1,3,2,0,-1]),
        3:( 0,[2,1,-2,-2,-3,0,2,4,4,2,0,-3])}
print("="*78)
print("Park's large color R-matrix on m(5_2), beta = s2^-3 s1^-1 s2 s1^-1")
print("   weight strata w = 0..%d ; blocks wanted f_0..f_%d ; x-margin %d"%(W,JTGT,MARGIN))
print("="*78)
S2 = run(W, JTGT+MARGIN)
WC = min(W, 10)                                   # margin check at a cheaper cutoff
S1 = run(WC, JTGT+MARGIN+5)
B1 = blocks(S1[WC], JTGT); Bc = blocks(S2[WC], JTGT)
B2 = blocks(S2[W], JTGT); Bprev = blocks(S2[W-1], JTGT)
c1 = c2 = c3 = True
for j in range(0, JTGT+1):
    d = B2.get(j, {})
    if not d: print("   f_%d : EMPTY"%j); c3 = False; continue
    lo = min(d)
    # C2 truncation independence, over the range both computed
    hi2 = max(d); a1 = B1.get(j,{}); ac = Bc.get(j,{})
    c2 &= (a1 == ac)                       # same blocks at margin M and M+5, same cutoff
    # C3 stratum convergence: report ONLY the prefix that is stable in w
    n = 0
    while lo+n <= hi2 and Bprev.get(j,{}).get(lo+n,0) == d.get(lo+n,0): n += 1
    tag = ""
    if j in PARK:
        plo, pc = PARK[j]
        ok = ([int(d.get(plo+i,0)) for i in range(len(pc))] == pc and lo == plo
              and plo+len(pc) <= lo+n)     # Park's range must lie inside the stable prefix
        c1 &= ok
        tag = "   vs Park's printed f_%d : %s"%(j, "MATCH" if ok else "MISMATCH")
    print("   f_%d : q^%-3d %s%s"%(j, lo, [int(d.get(lo+i,0)) for i in range(min(12, n))], tag))
    print("        %d leading coefficients stable in w (cutoffs %d and %d); beyond that, not reported"%(n, W-1, W))
    c3 &= (n >= 1)
print("-"*78)
print("   C1 Park's printed f_0..f_3 reproduced :", "PASSED" if c1 else "FAILED")
print("   C2 independent of the x-truncation    :", "PASSED" if c2 else "FAILED")
print("   C3 converged in the weight strata     :", "PASSED" if c3 else "FAILED")
STABLE={}
for j in range(0,JTGT+1):
    d=B2.get(j,{})
    if not d: continue
    lo=min(d); n=0
    while lo+n<=max(d) and Bprev.get(j,{}).get(lo+n,0)==d.get(lo+n,0): n+=1
    STABLE[j]={e:d[e] for e in range(lo,lo+n) if d.get(e)}
import os
_dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data',
                    'park_f52_blocks_w%d.json' % W)
os.makedirs(os.path.dirname(_dst), exist_ok=True)
json.dump({"_provenance": "written by certificates/park_large_color.py",
           "_cutoff": W, "_margin": MARGIN,
           "_counts": {str(j): len(d) for j, d in sorted(STABLE.items())},
           "blocks": {str(j): {str(e): int(c) for e, c in d.items()} for j, d in STABLE.items() if d}},
          open(_dst, 'w'), indent=1, sort_keys=True)
print("   converged blocks written to", os.path.normpath(_dst))
if not (c1 and c2 and c3): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
