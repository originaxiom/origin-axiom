#!/usr/bin/env python3
"""MEMO-45 CELL: THE ONLY SPINOR IN THE ROOM — every e6 module the closing
owns is integer-spin under the Lorentz double; the SAME holonomy embeds either
fermion-capably (internal, odd) or bosonically (Lorentz-slot, even); the one
spin-1/2 module in the whole record is the holonomy's own C^2 — and on it the
beat squares to the MERIDIAN, not to a sign.

Exact content (all over Q(q) in the twisted_double stack; the orthogonal
A2-triple found from scratch as in b2_yukawa):
  1. LORENTZ BI-WEIGHTS OF THE 27: with h1, h2 the principal-sl2 Cartans of two
     orthogonal A2 slots (the Lorentz double's two factors), the joint weight
     multiset of the 27 is {(±2,±2):1, (±2,0):4, (0,±2):4, (0,0):7} — ALL EVEN
     (the banked spending-order fact, recomputed here in-frame): the 27 is
     INTEGER-SPIN under the Lorentz double.  Same check for the adjoint 78:
     all bi-weights even.  NO HALF-INTEGER LORENTZ CONTENT EXISTS in the
     closing's modules.
  2. THE TWO BRIDGES: the holonomy composes functorially through ANY sl2
     triple.  (a) minimal A1 (e = e_r): relator +I on the 27, stratum weights
     {±1:6, 0:15} — ODD, the fermion-capable seat (memo 29, re-verified).
     (b) Lorentz-slot A1 (the principal triple of an A2 slot): relator +I on
     the 27, stratum weights ALL EVEN, central element C = diag((-1)^wt) = I
     — the two lifts give the SAME rep: this embedding is LIFT-FREE/bosonic
     (the projectivity dictionary's even row, realized as a holonomy bridge).
  => the choice of stratum decides what the holonomy's spin-1/2 becomes
     downstream: internal doublets (odd rows) or integer-spin content (even
     rows).  Nothing in the 27/78 is ever spin-1/2 under the Lorentz double.
  3. THE SPINOR THAT REMAINS: the holonomy module C^2 itself — the defining
     rep of the covering SL(2,C) — is the record's only spin-1/2 object.  On
     it the beat acts antilinearly as W o conj with (W o conj)^2 = W conj(W)
     = A = the MERIDIAN (re-verified): the antiunitary square of the beat on
     the one spinor is a GROUP ELEMENT, not the +-1 of textbook
     time-reversal — the kinematic novelty, stated and fenced.
"""
import itertools, random
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

CART=[[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
def ip2(r,s): return sum(r[i]*sum(CART[i][j]*s[j] for j in range(N)) for i in range(N))
Rset=set(ROOTS)
def a2sys(r,s): return {r,s,tuple(a+b for a,b in zip(r,s)),tuple(-x for x in r),tuple(-x for x in s),tuple(-(a+b) for a,b in zip(r,s))}
pairs=[(r,s) for r,s in itertools.combinations(ROOTS,2) if ip2(r,s)==-1 and tuple(a+b for a,b in zip(r,s)) in Rset]
found=None
for (r1,s1) in pairs:
    S1_=a2sys(r1,s1)
    rest1=[p for p in pairs if all(ip2(p[0],t)==0 and ip2(p[1],t)==0 for t in (r1,s1))]
    for (r2,s2) in rest1:
        S2_=a2sys(r2,s2)
        if S2_&S1_: continue
        found=((r1,s1),(r2,s2)); break
    if found: break
(r1,s1),(r2,s2)=found
print("two orthogonal A2 slots found (the Lorentz double's factors)")

def prin(rs):
    r,s=rs
    e=[a+b for a,b in zip(evec(r),evec(s))]
    h=[F(0)]*DIM
    for k in range(N): h[k]=F(2*(r[k]+s[k]))
    f=[-2*(a+b) for a,b in zip(evec(tuple(-x for x in r)),evec(tuple(-x for x in s)))]
    assert br(e,f)==h and br(h,e)==[2*x for x in e] and br(h,f)==[-2*x for x in f]
    return e,h,f
e1,h1,f1=prin((r1,s1)); e2,h2,f2=prin((r2,s2))
H1=rho27_Q(h1); H2=rho27_Q(h2)

# 1. Lorentz bi-weights on the 27
bw=Counter((int(H1[a][a]),int(H2[a][a])) for a in range(27))
sym={ (abs(k[0]),abs(k[1])): 0 for k in bw }
print("27 Lorentz bi-weight multiset:", dict(bw))
expected={(2,2):1,(2,-2):1,(-2,2):1,(-2,-2):1,(2,0):4,(-2,0):4,(0,2):4,(0,-2):4,(0,0):7}
assert dict(bw)==expected
alleven27=all(k[0]%2==0 and k[1]%2==0 for k in bw)
print("ALL 27 bi-weights even (integer spin under the double):", alleven27); assert alleven27
# and the adjoint 78: ad-eigenvalues of h1,h2 on root vectors = <r,h> values; Cartan weight (0,0)
bw78=Counter()
def pair_h(h,r):
    v=br(h,evec(r))
    ev=evec(r)
    k=next(i for i in range(DIM) if ev[i]!=0)
    return v[k]/ev[k]
for r in ROOTS:
    bw78[(int(pair_h(h1,r)),int(pair_h(h2,r)))]+=1
bw78[(0,0)]+=6
alleven78=all(k[0]%2==0 and k[1]%2==0 for k in bw78)
print("78 bi-weight multiset:", dict(bw78))
print("ALL 78 bi-weights even:", alleven78); assert alleven78

# 2. the two bridges on the 27
def bridge(e,f,label,expect_odd):
    E27=toF(rho27_Q(e)); F27=toF(rho27_Q(f))
    A27=nilexp(E27,ONE); B27=nilexp(F27,QQ)
    A27i=nilexp(E27,fneg(ONE)); B27i=nilexp(F27,fneg(QQ))
    d27={'a':A27,'A':A27i,'b':B27,'B':B27i}
    Rel=wordmat('a'+'bABa'+'B'+'AbaB',d27)
    h=br(e,f)
    Hm=rho27_Q(h)
    wts=Counter(int(Hm[a][a]) for a in range(27))
    odd=any(k%2!=0 for k in wts)
    Cid=all((Hm[a][a]%2==0) for a in range(27))
    print(f"  bridge[{label}]: relator = +I: {Rel==eye(27)}; stratum weights {dict(wts)}; odd: {odd}; C = I (lift-free): {Cid}")
    assert Rel==eye(27) and odd==expect_odd and Cid==(not expect_odd)
r0=ROOTS[0]
bridge(evec(r0), [-x for x in evec(tuple(-t for t in r0))], "minimal A1 (internal seat)", True)
bridge(e1, f1, "Lorentz-slot A1 (principal of slot 1)", False)

# 3. the spinor that remains: the beat on C^2 squares to the meridian
def fmul2(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c+b*d)
def gal2(u): return (u[0]+u[1],-u[1])
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
def m2(X,Y): return [[ (lambda s: s)( tuple(map(sum,zip(fmul2(X[i][0],Y[0][j]),fmul2(X[i][1],Y[1][j])))) ) for j in range(2)] for i in range(2)]
W2=[[O,Qp],[Z,O]]
Wc=[[gal2(x) for x in row] for row in W2]
sq=m2(W2,Wc)
A2m=[[O,O],[Z,O]]
print("on the holonomy C^2: (W o conj)^2 = W conj(W) =", "A (the meridian)" if sq==A2m else sq)
assert sq==A2m

print("""
THE ONLY SPINOR IN THE ROOM: the closing's own modules carry no half-integer
Lorentz content anywhere — the 27 and the 78 are integer-spin under the
Lorentz double, exactly.  The holonomy bridges functorially into the algebra
two inequivalent ways: through an odd stratum it seeds the fermion-capable
internal doublets (the seat); through the Lorentz slot it is lift-free and
bosonic (C = I: the two spin structures become indistinguishable downstream).
So 4d fermions cannot come from the e6 modules; the record's one spin-1/2
object is the holonomy's own C^2 — where the kinematics is already fully
banked, and where the beat's antiunitary square is not a textbook +-1 but the
MERIDIAN itself.  The internal->spacetime bridge gap is now a single sharp
question: what carries the holonomy's C^2 into spacetime — and the no-go half
(not through the closing's modules) is exact.""")
