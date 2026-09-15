#!/usr/bin/env python3
"""MEMO-56 ADDENDUM CELL: is the family/dark split beat-stable?

Memo 56 found the frame-paid matter parity P and the object-paid lock C_27
are independent Z/2s.  This addendum asks the stability question: does the
object's own mirror (the beat, U27 o gal on the 27) preserve the family
grading 16 (+) 10 (+) 1 and its parity P — the way it preserves the lock
(memo 50 FACT D)?

PREREGISTERED (two-outcome): since the bridge root carries family charge
q(r0) = -3 (odd), U27 = exp(q E27) shifts charges by -3 per rung, so the
expectation is NO on both counts: the beat neither preserves the family
classes nor the parity P.  Either branch is the result; counts measured.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# family classes (as in dark_ledger.py)
q3={a: 3*ipr(weights[a], omega1) for a in range(27)}
q3={a:int(q3[a]) for a in q3}
cnt=Counter(q3.values())
c16=next(v for v,m in cnt.items() if m==16); c10=next(v for v,m in cnt.items() if m==10)
cls={a:('16' if q3[a]==c16 else '10' if q3[a]==c10 else '1') for a in range(27)}
Ppar={a:(-1 if cls[a]=='16' else 1) for a in range(27)}

# the beat operator on the 27: U27 (gal acts only on coefficients, basis fixed)
r0=ROOTS[0]
E27p=toF(rho27_Q(evec(r0)))
U27=nilexp(E27p,QQ)
Z=(F(0),F(0))
mix_class=0; mix_par=0; pure=0
for a in range(27):
    sup=[l for l in range(27) if U27[l][a]!=Z]
    if any(cls[l]!=cls[a] for l in sup): mix_class+=1
    if any(Ppar[l]!=Ppar[a] for l in sup): mix_par+=1
    if sup==[a]: pure+=1
print(f"beat (U27) on the 27: {mix_class}/27 basis states leave their family class;")
print(f"                      {mix_par}/27 flip parity-P components; {pure}/27 untouched")
# the lock, for contrast (banked memo 50, re-checked here on the 27 alone)
wtc={a:int(rho27_Q([F(r0[k]) if k<N else F(0) for k in range(DIM)])[a][a]) for a in range(27)}
c27={a:(1 if wtc[a]%2==0 else -1) for a in range(27)}
lock_ok=all(all(c27[l]==c27[a] for l in range(27) if U27[l][a]!=Z) for a in range(27))
print(f"contrast — the lock C_27 is preserved by the beat on every state: {lock_ok}")
assert lock_ok
assert mix_class>0 and mix_par>0
print("""
=> the family/dark split (16+10+1) and its matter parity P are NOT
   beat-covariant: the object's mirror moves states across the family
   classes (charge shift -3 per E27 rung).  The ONLY mirror-stable Z/2 on
   this list is the object's own lock.  The dark parity is real once the
   D5 frame is fixed, but the frame itself is not respected by the
   object's involution — frame-paid in the strong sense.""")
