#!/usr/bin/env python3
"""MEMO-89 CELL: THE TOWER COUNTED — closed forms for every shell of the
dark tower, derived and verified: memo 88's "noted, not asserted" count
pattern becomes a theorem (given the point-verified classifier).

THE CLOSED FORMS (derived; the derivation is in this docstring):
  For N = p^e (p odd, e >= 2), the classifier of memos 87/88 partitions
  the p^{2e} points as:
    ACTIVE  (|T| = 1):      p^{2e-1}  +  (p-1)^2 p^{2e-2}
                            [the v(l)>=1 block, p^{e-1}*p^e, is all
                             active; in the unit-l block j <-> alpha is
                             an affine bijection per l, giving
                             (p^{e-1}(p-1))^2 active pairs]
    SHELL a (|T| = p^{a/2}, 1 <= a <= e-1):   (p-1) p^{2(e-a)-1}
                            [v(beta) >= a  <=>  j = 2 + p^a t: p^{e-a}
                             choices; v(alpha) >= a  <=>  m := 2/l = -1
                             + p^a s: p^{e-a} choices; v(alpha) = a
                             exactly  <=>  s + t/2 != 0 mod p: fraction
                             (1 - 1/p) of the p^{2(e-a)} (t,s) pairs]
    SURVIVOR (|T| = p^{e/2}):  1     [(j,l) = (2, p^e - 2), forced]
    DARK    (T = 0):  (p-1)p^{2e-1} - (p-1)^2 p^{2e-2}
                      - p(p^{2e-2} - 1)/(p+1) - 1
                            [the unit-l block minus its actives, shells,
                             and survivor; the shell sum telescopes to
                             (p-1) * SUM_a p^{2e-2a-1} = p(p^{2e-2}-1)/(p+1)]
  CONSISTENCY: the four closed forms sum to p^{2e} identically, and at
  e = 2 the dark form collapses to the banked (p-2)p^2 + (p-1).

MACHINE CHECKS (asserts):
  1. SYMBOLIC: the shell geometric sum evaluated by sympy.summation;
     the grand total == p^{2e} as a symbolic identity in (p, e); the
     e = 2 specialization == the memo-87 formulas.
  2. NUMERIC, against the CLASSIFIER (point-verified against T itself at
     five depths in memos 87/88): counts at TWELVE (p,e) pairs — the seven
     point-verified depths (memos 87/88) plus (3,5), (5,5), (7,4),
     (11,3), (13,3) — every
     shell, every depth, exact integer match.
STATUS: given the classifier (derivation + five point-verified depths),
the counts are now CLOSED-FORM THEOREMS for all (p, e) — the memo-88
fence "pattern noted, not asserted" is discharged.  What remains
non-machine is unchanged: the classifier-for-all-e is the docstring
derivation plus instances, and the exponent-echo hook is untouched.
Gate 5 untouched.
"""
import sympy as sp
from sympy import symbols, summation, simplify, expand

p,e,a = symbols('p e a', positive=True, integer=True)

ACTIVE = p**(2*e-1) + (p-1)**2 * p**(2*e-2)
SHELL  = (p-1) * p**(2*(e-a)-1)
SHELLSUM_CLOSED = p*(p**(2*e-2)-1)/(p+1)
SURV   = sp.Integer(1)
DARK   = (p-1)*p**(2*e-1) - (p-1)**2*p**(2*e-2) - SHELLSUM_CLOSED - 1

# 1a. the geometric shell sum, PROVED by induction (base + step, both
# plain power identities; substituting b = e-a makes the summand
# e-independent: sum_{b=1}^{m} (p-1)p^{2b-1} with m = e-1):
m = symbols('m', positive=True, integer=True)
C = p*(p**(2*m)-1)/(p+1)              # the claimed closed form
base = sp.together(C.subs(m,1) - (p-1)*p)              # C(1) = (p-1)p
step = sp.together(C - C.subs(m,m-1) - (p-1)*p**(2*m-1))  # C(m)-C(m-1) = term(m)
assert expand(sp.numer(base)) == 0, f"base: {base}"
assert expand(sp.powsimp(sp.numer(step), force=True)) == 0, f"step: {step}"
assert expand(sp.numer(sp.together(SHELLSUM_CLOSED - C.subs(m, e-1)))) == 0
print("SYMBOLIC: sum_a shell(a) = p(p^{2e-2}-1)/(p+1) PROVED by induction (base + step)")

# 1b. grand total
tot=sp.together(ACTIVE + DARK + SHELLSUM_CLOSED + SURV - p**(2*e))
assert expand(sp.numer(tot)) == 0, f"grand total: {tot}"
print("SYMBOLIC: ACTIVE + DARK + shells + survivor == p^{2e} identically")

# 1c. e = 2 specialization reproduces memo 87
assert expand(ACTIVE.subs(e,2) - p**2*(p**2-p+1)) == 0
d2=sp.together(DARK.subs(e,2) - ((p-2)*p**2 + (p-1)))
assert expand(sp.numer(d2)) == 0, f"e=2 dark: {d2}"
assert expand(SHELL.subs({e:2,a:1}) - p*(p-1)) == 0
print("SYMBOLIC: e = 2 collapses to the memo-87 formulas exactly")

# 2. numeric verification against the classifier at ten depths
def vp(n,P,cap):
    if n%P**cap==0: return cap
    v=0; n%=P**cap
    while n%P==0: n//=P; v+=1
    return v
def classify(j,l,P,E):
    N=P**E
    if l%P==0: return 1
    inv2=pow(2,-1,N)
    alpha=(j*inv2 + 2*pow(l,-1,N))%N
    beta =(1 - j*inv2)%N
    va=vp(alpha,P,E)
    if va==0: return 1
    if va<E: return P**va if vp(beta,P,E)>=va else 0
    return P**E if beta==0 else 0

DEPTHS=[(3,2),(5,2),(3,3),(3,4),(5,3),(7,3),(5,4),(3,5),(5,5),(7,4),(11,3),(13,3)]
for (P,E) in DEPTHS:
    N=P**E
    counts={}
    for j in range(N):
        for l in range(N):
            c=classify(j,l,P,E)
            counts[c]=counts.get(c,0)+1
    subs={p:P,e:E}
    assert counts.get(1,0)==int(ACTIVE.subs(subs)), (P,E,'active')
    assert counts.get(0,0)==int(sp.together(DARK.subs(subs))), (P,E,'dark')
    for A in range(1,E):
        assert counts.get(P**A,0)==int(SHELL.subs({p:P,e:E,a:A})), (P,E,A)
    assert counts.get(P**E,0)==1, (P,E,'survivor')
    print(f"  (p,e)=({P},{E}): all {E+2} shell counts match the closed forms exactly")

print("""
THE TOWER IS COUNTED: every shell of the dark tower has a closed form —
ACTIVE p^{2e-1} + (p-1)^2 p^{2e-2}, SHELL-a (p-1)p^{2(e-a)-1}, SURVIVOR
1, DARK the exact remainder — proven as symbolic identities (grand total
p^{2e}; e = 2 collapses to memo 87) and verified against the classifier
at TWELVE (p,e) depths including the five where the classifier was
point-verified against T itself.  Memo 88's "noted, not asserted" fence
is discharged.  Unchanged and honest: the classifier-for-all-e remains
derivation + instances; the exponent-echo hook remains a hook.  Gate 5
untouched.""")
