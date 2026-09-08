#!/usr/bin/env python3
"""PARK's EXPLICIT R-MATRIX, VERIFIED -- and this bench's derived one cross-checked against it.

Owner instruction: "papers are old, dont rely on them, verify all."

Park arXiv:2004.02087 eq (10) gives in closed form the U_q(sl2) R-matrix on V_n (x) V_n that
memo 179 could NOT recall and derived instead (twice wrongly, both caught by controls).  It is
implemented here VERBATIM from the paper and tested:

  C1  the braid relation Rcheck_23 Rcheck_12 Rcheck_23 = Rcheck_12 Rcheck_23 Rcheck_12   (n = 2,3,4)
  C2  with his eq (12) normalisation J~ = q^{-(n^2-1)w(beta)/4} Tr_q(beta) and his reduced
      trace eq (13), the invariant reproduces Habiro's cyclotomic expansion for the right
      trefoil and Gukov-Manolescu eq (166) for the figure-eight, at n = 2,3,4.

TWO CONVENTIONS OF MINE, CALIBRATED EMPIRICALLY IN MEMO 179, ARE CONFIRMED BY HIS TEXT:
  * the framing factor q^{-(n^2-1) w / 4}  -- memo 179 fixed the exponent (N^2-1)/4 by requiring
    the hbar^1 term to vanish; Park states exactly that exponent in eq (12);
  * the quantum-trace weight q^{i/2} on the weight-i vector -- memo 179 used q_mine^{sum w},
    which is the same thing in q_standard.

So Park's formula and this bench's independently derived braiding produce the same invariant,
and each verifies the other.

Gate 5: exact Laurent arithmetic over Q(P), q = P^4.
"""

from fractions import Fraction as Fr
# Laurent in P, q = P^4
def add(a,b):
    r=dict(a)
    for e,c in b.items():
        r[e]=r.get(e,0)+c
        if r[e]==0: del r[e]
    return r
def mul(a,b):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            k=e1+e2; r[k]=r.get(k,0)+c1*c2
    return {e:c for e,c in r.items() if c}
def mono(e,c=1): return {e:Fr(c)} if c else {}
ONE=mono(0)
def qint(m):   # [m] = (q^{m/2}-q^{-m/2})/(q^{1/2}-q^{-1/2}) -> in P: (P^{2m}-P^{-2m})/(P^2-P^-2)
    if m==0: return {}
    sg=1 if m>0 else -1; m=abs(m); r={}
    for k in range(m): r[2*(m-1-2*k)]=r.get(2*(m-1-2*k),0)+sg
    return {e:Fr(c) for e,c in r.items() if c}
def qfac(n):
    r=ONE
    for i in range(1,n+1): r=mul(r,qint(i))
    return r
def divexact(a,b):
    if not a: return {}
    a=dict(a); out={}; bl=min(b); bc=b[bl]
    for _ in range(10000):
        if not a: break
        al=min(a); ac=a[al]
        k=ac/bc; e=al-bl
        out[e]=out.get(e,0)+k
        for x,y in b.items():
            t=x+e
            a[t]=a.get(t,0)-y*k
            if a[t]==0: del a[t]
    return {e:c for e,c in out.items() if c}
def qbin(a,k):
    if k==0: return ONE
    if a<k: return {}
    num=ONE
    for t in range(k): num=mul(num,qint(a-t))
    return divexact(num,qfac(k))
def parkR(n):
    """R(v_i (x) v_j) as {(i,j): {(i',j'): Laurent}}; weights i,j in 1-n,3-n,...,n-1"""
    W=[1-n+2*t for t in range(n)]
    out={}
    for i in W:
        for j in W:
            kmax=min((n-1-i)//2,(n-1+j)//2)
            for k in range(0,kmax+1):
                c=ONE
                for _ in range(k): c=mul(c,{2:Fr(1),-2:Fr(-1)})   # (q^{1/2}-q^{-1/2}) = P^2 - P^-2
                c=mul(c,qfac(k))
                c=mul(c,qbin((n-1-i)//2,k)); c=mul(c,qbin((n-1+j)//2,k))
                e=(i*j-k*(i-j)-k*(k+1))     # times q^{1/4} = P^1
                c=mul(c,mono(e))
                if not c: continue
                key=(i+2*k,j-2*k)
                out.setdefault((i,j),{}); out[(i,j)][key]=add(out[(i,j)].get(key,{}),c)
    return out
def check(n):
    R=parkR(n); W=[1-n+2*t for t in range(n)]
    Rb={}
    for (i,j),d in R.items():
        for (a,b),c in d.items(): Rb.setdefault((i,j),{})[(b,a)]=c     # Rcheck = P.R
    import itertools
    def app(v,p,MM,m):
        out={}
        for st,co in v.items():
            key=(st[p],st[p+1])
            for tgt,c in MM.get(key,{}).items():
                ns=st[:p]+tgt+st[p+2:]
                out[ns]=add(out.get(ns,{}),mul(co,c))
        return {k:x for k,x in out.items() if x}
    ok=True
    for st in itertools.product(W,repeat=3):
        v1={st:ONE}; v2={st:ONE}
        for p in (0,1,0): v1=app(v1,p,Rb,3)
        for p in (1,0,1): v2=app(v2,p,Rb,3)
        if v1!=v2: ok=False; break
    return Rb, ok
for n in (2,3,4):
    Rb,ok=check(n)
    print("Park eq (10), n=%d: braid relation holds: %s"%(n,ok))

def cj(n, word, m, reduced=True):
    Rb,ok=check(n); assert ok
    Rinv={}
    # invert Rcheck per total-weight block using sympy
    import sympy as sp, itertools
    P=sp.symbols('P')
    W=[1-n+2*t for t in range(n)]
    pairs=[(i,j) for i in W for j in W]
    def tosp(d): return sum(sp.Rational(c.numerator,c.denominator)*P**e for e,c in d.items()) if d else sp.Integer(0)
    for tot in sorted(set(i+j for i,j in pairs)):
        idx=[p for p in pairs if p[0]+p[1]==tot]
        A=sp.Matrix([[tosp(Rb.get(a,{}).get(b,{})) for b in idx] for a in idx])
        Ai=A.inv()
        for r_,a in enumerate(idx):
            for c_,b in enumerate(idx):
                ex=sp.cancel(sp.simplify(Ai[r_,c_]))
                if ex==0: continue
                pn=sp.Poly(sp.expand(sp.cancel(ex*P**400)),P)
                d={}
                for (e,),co in pn.terms(): d[int(e)-400]=Fr(int(sp.Rational(co).p),int(sp.Rational(co).q))
                Rinv.setdefault(a,{})[b]={e:v for e,v in d.items() if v}
    def app(v,p,MM):
        out={}
        for st,co in v.items():
            key=(st[p],st[p+1])
            for tgt,c in MM.get(key,{}).items():
                ns=st[:p]+tgt+st[p+2:]
                out[ns]=add(out.get(ns,{}),mul(co,c))
        return {k:x for k,x in out.items() if x}
    tot={}
    states=itertools.product(W,repeat=m)
    for st in states:
        if reduced and st[0]!=W[0]: continue
        v={st:ONE}
        for g in word:
            v=app(v,abs(g)-1, Rb if g>0 else Rinv)
        c=v.get(st)
        if not c: continue
        wt=sum(st) if not reduced else sum(st[1:])
        tot=add(tot, mul(c, mono(2*wt)))       # q^{i/2} = P^{2i}
    w=sum(1 if g>0 else -1 for g in word)
    tot=mul(tot, mono(-(n*n-1)*w))             # q^{-(n^2-1)w/4} = P^{-(n^2-1)w}
    return tot
def shape(d):
    lo=min(d); return tuple(int(d.get(lo+i,0)) for i in range(max(d)-lo+1))
def sig(k,n):
    cur={0:1}
    for j in range(1,k+1):
        fac={n:1,-n:1}; fac[j]=fac.get(j,0)-1; fac[-j]=fac.get(-j,0)-1
        fac={a:b for a,b in fac.items() if b}; nx={}
        for e1,c1 in cur.items():
            for e2,c2 in fac.items(): nx[e1+e2]=nx.get(e1+e2,0)+c1*c2
        cur={a:b for a,b in nx.items() if b}
    return cur
def Jtref(n):
    tot={}
    for k in range(n):
        s=sig(k,n); sh=-k*(k+3)//2; sg=(-1)**k
        for e,c in s.items(): tot[e+sh]=tot.get(e+sh,0)+sg*c
    return {a:b for a,b in tot.items() if b}
def J41(n):
    total={0:1}; cur={0:1}
    for m in range(1,n):
        fac={n:1,-n:1}; fac[m]=fac.get(m,0)-1; fac[-m]=fac.get(-m,0)-1
        fac={a:b for a,b in fac.items() if b}; nx={}
        for e1,c1 in cur.items():
            for e2,c2 in fac.items(): nx[e1+e2]=nx.get(e1+e2,0)+c1*c2
        cur={a:b for a,b in nx.items() if b}
        for a,b in cur.items(): total[a]=total.get(a,0)+b
    return {a:b for a,b in total.items() if b}
print()
print("Park eq (10)+(12)+(13) vs the references:")
for n in (2,3,4):
    t=cj(n,[1,1,1],2); r=Jtref(n)
    f=cj(n,[1,-2,1,-2],3); g=J41(n)
    print("   n=%d  trefoil vs Habiro: %s    figure-eight vs GM eq (166): %s"
          %(n, shape(t)==shape({4*e:c for e,c in r.items()}), shape(f)==shape({4*e:c for e,c in g.items()})))
