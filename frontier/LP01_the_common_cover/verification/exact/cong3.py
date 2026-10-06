exec(open('cong.py').read().split("I=(ONE")[0])
def red(X,N): return tuple((e[0]%N,e[1]%N) for e in X)
def rmul(u,v,N): x,y=u;s,t=v; return ((x*s-y*t)%N,(x*t+y*s-y*t)%N)
def radd(u,v,N): return ((u[0]+v[0])%N,(u[1]+v[1])%N)
def rmm(X,Y,N):
    a,b,c,d=X;e,f,g,h=Y
    return (radd(rmul(a,e,N),rmul(b,g,N),N),radd(rmul(a,f,N),rmul(b,h,N),N),radd(rmul(c,e,N),rmul(d,g,N),N),radd(rmul(c,f,N),rmul(d,h,N),N))
def canon(X,N): nX=tuple(((-e[0])%N,(-e[1])%N) for e in X); return min(X,nX)
def closure(gens,N,limit=5_000_000):
    e=canon(red(((1,0),(0,0),(0,0),(1,0)),N),N); seen={e}; fr=[e]
    while fr:
        nx=[]
        for s in fr:
            for g in gens:
                t=canon(rmm(s,g,N),N)
                if t not in seen:
                    seen.add(t); nx.append(t)
        if len(seen)>limit: return None
        fr=nx
    return seen
T=((1,0),(1,0),(0,0),(1,0)); U=((1,0),(0,1),(0,0),(1,0)); S=((0,0),(-1,0),(1,0),(0,0)); Dg=((0,1),(0,0),(0,0),(-1,-1))
Gg=[T,U,S,Dg,minv(T),minv(U),minv(S),minv(Dg)]
import sys
for N in map(int,sys.argv[1:]):
    Gs=closure([red(g,N) for g in Gg],N); tot=len(Gs)
    out=[]
    for nm,rep in [('m004',m004),('m202',m202)]:
        gens=[red(rep[g],N) for g in rep]+[red(minv(rep[g]),N) for g in rep]
        H=closure(gens,N); out.append((nm,tot//len(H)))
    print(N,'|PSL(2,O/N)|',tot,out,flush=True)
