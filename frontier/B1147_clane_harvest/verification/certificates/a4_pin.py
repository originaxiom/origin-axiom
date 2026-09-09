#!/usr/bin/env python3
"""A4: PIN ABOVE THE SPIN FORK — H1 arithmetic of the Gieseking extension:
both Pin-level structures restrict to the SAME spin structure on M, and it is
the beat-selected one; chi = -1 does not even extend as a character.

Setup (all previously banked pieces, re-verified here):
  Gamma   = pi1(m004) = <a,b | R(a,b)>,  R = a b A B a B A b a B
  beat    = beta: a -> a, b -> B a b A b  (an automorphism; beta^2 = Ad(a))
  Gamma_G = pi1(Gieseking N) = <a, b, t | R(a,b), t a t^-1 = a,
            t b t^-1 = beta(b), t^2 = a>
  (t^2 = a is forced: at the holonomy level (W gal)^2 = W conj(W) = A exactly
   — memo 16/28's identity, re-verified below — and the holonomy is faithful.)

THE COMPUTATION (exact integer linear algebra, Smith normal form):
  1. H1(Gamma) = Z (relator abelianizes to a = b);  H1(M; Z/2) = Z/2:
     the two spin structures (memo 28's census).
  2. H1(Gamma_G): generators a,b,t; abelianized relations a = b (relator),
     0 = 0 (t-conjugations: beta is homologically trivial — verified from the
     letter counts of beta(b)), a = 2t.  Smith form => H1(Gamma_G) = Z<t>,
     with a = b = 2t.  So H1(N; Z/2) = Z/2: exactly TWO Pin-level structures.
  3. THE RESTRICTION MAP H^1(N;Z/2) -> H^1(M;Z/2): dual to a = 2t — every
     Z/2 character of Gamma_G kills a and b.  THE MAP IS ZERO: both Pin-level
     structures restrict to the TRIVIAL character chi = +1 — the beat-selected
     spin structure of memo 28.
  4. THE OBSTRUCTION, group-cohomologically: chi = -1 (chi(a)=chi(b)=-1)
     extends to Gamma_G iff some chi~(t) in {+-1} satisfies chi~(t)^2 =
     chi(a) = -1 — impossible.  chi = +1 extends in exactly two ways
     (chi~(t) = +-1: the two Pin-level structures).
  => memo 28's selection re-derived by a THIRD independent route (holonomy
     intertwiners; rep-level closure; now H1 arithmetic of the extension),
     and the two-outcome question closes: the Pin bit is NOT the spin bit in
     disguise — it is a genuinely new (t-sign) bit living entirely over the
     selected side.
"""
from fractions import Fraction as F

# ---- holonomy re-verification of t^2 = a (exact over Q(q), q^2 = q-1)
def fadd(u,v): return (u[0]+v[0],u[1]+v[1])
def fneg(u): return (-u[0],-u[1])
def fmul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c+b*d)
def gal(u): return (u[0]+u[1],-u[1])
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); Q=(F(0),F(1))
def mmul(X,Y): return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def mgal(X): return [[gal(x) for x in row] for row in X]
def inv2(X):
    d=fadd(fmul(X[0][0],X[1][1]),fneg(fmul(X[0][1],X[1][0]))); assert d==ONE
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]
A=[[ONE,ONE],[ZERO,ONE]]; B=[[ONE,ZERO],[Q,ONE]]
d={'a':A,'A':inv2(A),'b':B,'B':inv2(B)}
def word(w):
    M=[[ONE,ZERO],[ZERO,ONE]]
    for ch in w: M=mmul(M,d[ch])
    return M
assert word('abABaBAbaB')==[[ONE,ZERO],[ZERO,ONE]]
W=[[ONE,Q],[ZERO,ONE]]
assert mmul(W,mgal(W))==A
print("holonomy: R(A,B) = +I and (W gal)^2 = W conj(W) = A exactly => t^2 = a  (faithfulness)")
# beta(b) letter counts (homological triviality of the twist)
bb='BabAb'
na=bb.count('a')-bb.count('A'); nb=bb.count('b')-bb.count('B')
print(f"beta(b) = {bb}: abelianized = {na} a + {nb} b  (expect 0 a + 1 b: beta homologically trivial)")
assert (na,nb)==(0,1)
# relator letter counts
R='abABaBAbaB'
ra=R.count('a')-R.count('A'); rb=R.count('b')-R.count('B')
print(f"relator abelianized: {ra} a + {rb} b = 0  => a = b in H1(M)")
assert (ra,rb)==(1,-1)

# ---- Smith normal form
def smith(Mrows):
    import copy
    M=[row[:] for row in Mrows]
    m=len(M); n=len(M[0]) if m else 0
    r=0; c=0; divs=[]
    while r<m and c<n:
        # find pivot with minimal nonzero abs value
        best=None
        for i in range(r,m):
            for j in range(c,n):
                if M[i][j]!=0 and (best is None or abs(M[i][j])<abs(M[best[0]][best[1]])):
                    best=(i,j)
        if best is None: break
        bi,bj=best
        M[r],M[bi]=M[bi],M[r]
        for row in M: row[c],row[bj]=row[bj],row[c]
        again=True
        while again:
            again=False
            for i in range(r+1,m):
                if M[i][c]!=0:
                    qd=M[i][c]//M[r][c]
                    M[i]=[x-qd*y for x,y in zip(M[i],M[r])]
                    if M[i][c]!=0:
                        M[r],M[i]=M[i],M[r]; again=True
            for j in range(c+1,n):
                if M[r][j]!=0:
                    qd=M[r][j]//M[r][c]
                    for i2 in range(m): M[i2][j]-=qd*M[i2][c]
                    if M[r][j]!=0:
                        for i2 in range(m): M[i2][c],M[i2][j]=M[i2][j],M[i2][c]
                        again=True
        divs.append(abs(M[r][c])); r+=1; c+=1
    return divs, (n - len([d for d in divs if d!=0]))

# H1(Gamma): gens a,b; relation a - b = 0
divs,free=smith([[1,-1]])
print(f"H1(M): invariant factors {divs}, free rank {free}  => Z  (H1(M;Z/2) = Z/2: 2 spin structures)")
assert divs==[1] and free==1

# H1(Gamma_G): gens a,b,t; relations: a-b=0 (relator); 0 (t a t^-1 a^-1); 0 (t b t^-1 beta(b)^-1); a-2t=0
divs,free=smith([[1,-1,0],[0,0,0],[0,0,0],[1,0,-2]])
print(f"H1(N): invariant factors {divs}, free rank {free}  => Z<t> with a = b = 2t")
assert [d for d in divs if d!=0]==[1,1] and free==1
print("H1(N;Z/2) = Z/2: exactly TWO Pin-level structures on the Gieseking")

# restriction map on Z/2 characters: phi in Hom(H1(N),Z/2) -> phi|_M determined by phi(a),phi(b)
# a = 2t => phi(a) = 2 phi(t) = 0 mod 2, same for b
print("restriction H^1(N;Z/2) -> H^1(M;Z/2): phi(a) = phi(2t) = 0 => THE ZERO MAP")
print("=> both Pin-level structures restrict to chi = +1 — the beat-selected spin structure")

# extension obstruction for chi = -1 (multiplicative check over Z)
# chi~(t)^2 = chi(a): with chi(a) = -1 need x^2 = -1, x in {1,-1}: impossible
sols_neg=[x for x in (1,-1) if x*x==-1]
sols_pos=[x for x in (1,-1) if x*x==1]
print(f"chi=-1 extensions: chi~(t) solutions of x^2 = -1 in {{+-1}}: {sols_neg}  (NONE: does not extend)")
print(f"chi=+1 extensions: chi~(t) solutions of x^2 = +1 in {{+-1}}: {sols_pos}  (TWO: the Pin-level pair)")
assert sols_neg==[] and len(sols_pos)==2

print("""
A4 CLOSED: the Pin-level bit is NOT the spin bit in disguise — the restriction
map is ZERO, both structures upstairs land on the beat-selected chi = +1 spin
structure, the chi = -1 structure does not even admit a character extension to
the Gieseking group, and the genuinely new bit is the t-sign (which structure
upstairs), living entirely over the selected side.  Memo 28's selection now has
a THIRD independent derivation: pure H1 arithmetic of the extension t^2 = a.""")
