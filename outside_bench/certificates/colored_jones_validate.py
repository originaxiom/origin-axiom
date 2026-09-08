#!/usr/bin/env python3
"""THE SIX CONTROLS ON certificates/colored_jones_core.py.  Nothing is reported unless all fire."""
import os, sys, itertools
from fractions import Fraction as Fr
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'colored_jones_core.py')).read().split('"""',2)[2])
import sympy as sp
U=sp.symbols('U')

_R={}
def RD(N):
    if N not in _R: _R[N]=Rdicts(N)
    return _R[N]

def raw(N, word, m):
    Rp,Rm=RD(N); w=[N-1-2*i for i in range(N)]; tot={}
    for st in itertools.product(range(N),repeat=m):
        v={st:ONE}
        for g in word:
            p=abs(g)-1; MM=Rp if g>0 else Rm; out={}
            for s2,c in v.items():
                key=(s2[p],s2[p+1])
                for tgt,ex in MM.get(key,{}).items():
                    ns=s2[:p]+tgt+s2[p+2:]
                    out[ns]=add(out.get(ns,{}), mul(c,ex))
            v={k:x for k,x in out.items() if x}
        c=v.get(st)
        if c: tot=add(tot, mul(c, mono(4*sum(w[i] for i in st))))
    return tot

def Jn(N, word, m, framed=True):
    t=raw(N,word,m)
    a=sum(c*U**e for e,c in t.items()); b=sum(U**(4*(N-1-2*k)) for k in range(N))
    rd=to_dict(sp.cancel(sp.simplify(a/b)))
    if not framed:
        return rd                      # raw u-exponents; only the shape is used
    wr=sum(1 if g>0 else -1 for g in word)
    sh=Fr(-wr*(N*N-1),4)*8; assert sh.denominator==1
    rd={e+int(sh):c for e,c in rd.items()}
    assert all(e%8==0 for e in rd), sorted(rd)[:4]
    return {Fr(e,8):c for e,c in rd.items()}

def hbar(J,K):
    out=[Fr(0)]*(K+1)
    for e,c in J.items():
        t=Fr(1)
        for m in range(K+1):
            out[m]+=Fr(c)*t; t=t*Fr(e)/(m+1)
    return out

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
def shape(d):
    lo=min(d); n=int(max(d)-lo)+1
    return tuple(int(d.get(lo+i,0)) for i in range(n))

ok={}
print("C1/C2  braid relation, invertibility, Laurent entries")
for N in (2,3,4):
    M=Rcheck(N)
    lau=all(sp.denom(sp.cancel(v)).is_Pow or sp.denom(sp.cancel(v))==1 for v in M.values())
    def app(vec,p):
        out={}
        for st,c in vec.items():
            key=(st[p],st[p+1])
            for (src,tgt),ex in M.items():
                if src!=key: continue
                ns=st[:p]+tgt+st[p+2:]; out[ns]=sp.expand(out.get(ns,0)+c*ex)
        return {k:sp.cancel(v) for k,v in out.items() if sp.simplify(v)!=0}
    br=True
    for st in itertools.product(range(N),repeat=3):
        v1={st:sp.Integer(1)}; v2={st:sp.Integer(1)}
        for p in (0,1,0): v1=app(v1,p)
        for p in (1,0,1): v2=app(v2,p)
        if any(sp.simplify(v1.get(k,0)-v2.get(k,0))!=0 for k in set(v1)|set(v2)): br=False; break
    print(f"   N={N}  braid relation {br}   Laurent {lau}")
    ok[f'C1N{N}']=br; ok[f'C2N{N}']=lau
print("C3  unknot quantum trace = [N]")
for N in (2,3):
    t=raw(N,[],1); ref={4*(N-1-2*k):Fr(1) for k in range(N)}
    print(f"   N={N}: {t==ref}"); ok[f'C3N{N}']=(t==ref)
print("C4  right trefoil vs Habiro   /   C5  figure-eight vs GM eq (166)")
for N in (2,3,4):
    a=shape(Jn(N,[1,1,1],2,framed=False))==shape({8*e:c for e,c in Jtref(N).items()})
    b=shape(Jn(N,[1,-2,1,-2],3,framed=False))==shape({8*e:c for e,c in J41(N).items()})
    print(f"   N={N}: trefoil {a}   figure-eight {b}"); ok[f'C4N{N}']=a; ok[f'C5N{N}']=b
print("C6  framing: J_n(1)=1, no hbar^1, hbar^2 = +-(n^2-1)   [GM eq (168)]")
for nm,word,m,sgn in (('4_1',[1,-2,1,-2],3,1),('3_1',[1,1,1],2,-1)):
    good=True
    for n in (1,2,3,4):
        h=hbar(Jn(n,word,m),2)
        good &= (h[0]==1 and h[1]==0 and h[2]==sgn*(n*n-1))
    print(f"   {nm}: {good}"); ok[f'C6{nm}']=good
print()
print("ALL CONTROLS PASSED:", all(ok.values()))
if not all(ok.values()): raise SystemExit(1)
print("\nq_standard = u^8, fixed by C4/C5 rather than assumed.")
