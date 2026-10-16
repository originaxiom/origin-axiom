"""Actual full WZ expansion in the credited free matrix-odd algebra."""
import importlib.util
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('full_parent_graded',HERE.parent/'surface_real_superfield_2026_10_16/analysis.py')
sf=importlib.util.module_from_spec(sp);sp.loader.exec_module(sf)
add=sf.add;scale=sf.scale;mul=sf.mul;comm=sf.comm;trace=sf.trace;letter=sf.letter
nmul=sf.nmul;lift=sf.lift;ntrace=sf.ntrace;component=sf.component;clean=sf.clean;spin=sf.spin
def hermitian_label(a):
    q=a.split(':');b=q[-1]
    if b.startswith('~') and (b[1:]=='D' or b[1:].startswith('v')):q[-1]=b[1:]
    return ':'.join(q)
def dag(p):
    out={}
    for (th,w),c in sf.ndagger(p).items():
        key=(th,tuple(hermitian_label(a) for a in w));out[key]=out.get(key,0)+c
    return clean(out)
def adj(p):return component(dag(lift(p)),(),1)
def op(p,name):
    out={}
    for w,c in p.items():
        for j,a in enumerate(w):
            k=w[:j]+(sf.alter(a,name),)+w[j+1:];out[k]=out.get(k,0)+c
    return clean(out)
def nop(p,name):return add(*(lift(op({w:c},name),th) for (th,w),c in p.items()))
def left(p,j):
    return clean({(th[:k]+th[k+1:],w):(-1)**k*c for (th,w),c in p.items() for k,a in enumerate(th) if a==j})
def theta(j):return lift({():s.Integer(1)},(j,))
one=lift({():s.Integer(1)})
def d4(p):return component(p,(0,1,2,3),-s.Rational(1,4))
def d2(p):return component(p)
def anti2(p):return component(p,(2,3),s.Rational(1,2))
def ncomm(a,b):return add(nmul(a,b),scale(nmul(b,a),-1))
def eq(a,b):return not add(a,scale(b,-1))
def eqtr(a,b):return eq(ntrace(a),ntrace(b))
def fermions(p):return trace({w:c for w,c in p.items() if sum(sf.odd(a) for a in w)==2})
def body(p):return trace({w:c for w,c in p.items() if not any(sf.odd(a) for a in w)})
def jet_quotient(p):
    """Explicit IBP on quadratic derivative terms; keep every primitive."""
    out={};currents={}
    for w,c in trace(p).items():
        candidates=[(j,a.split(':')[:-1]) for j,a in enumerate(w) if ':' in a]
        if len(w)==2 and len(candidates)==1 and len(candidates[0][1])==1 and all(sf.odd(a) for a in w):
            j,ops=candidates[0];other=1-j;name=ops[0]
            if sf.base(w[j])<sf.base(w[other]):
                primitive=w[:j]+(sf.base(w[j]),)+w[j+1:]
                changed=primitive[:other]+(sf.alter(primitive[other],name),)+primitive[other+1:]
                out[changed]=out.get(changed,0)-c
                cc=currents.setdefault(name,{})
                cc[primitive]=cc.get(primitive,0)+c
                continue
        out[w]=out.get(w,0)+c
    return trace(out),{k:trace(v) for k,v in currents.items() if trace(v)}
def current_div(currents):return trace(add(*(op(v,k) for k,v in currents.items())))

def construct(sig):
    def ext(p,mu):return nop(p,'e'+str(mu))
    X=[add(*(scale(nmul(theta(a),theta(b+2)),sig[mu][a,b]) for a in range(2) for b in range(2))) for mu in range(4)]
    def shift(p):
        return add(p,*(scale(nmul(X[mu],ext(p,mu)),s.I) for mu in range(4)),
            *(scale(nmul(X[mu],nmul(X[nu],ext(ext(p,nu),mu))),-s.Rational(1,2)) for mu in range(4) for nu in range(4)))
    th2=lift({():s.Integer(-2)},(0,1));bar2=dag(th2)
    ff=lambda k,a:lift(letter('f'+str(k)+'_'+str(a)))
    tc=add(scale(nmul(theta(0),ff(0,1)),-1),nmul(theta(1),ff(0,0)))
    vg=scale(nmul(bar2,tc),-s.I)
    V=add(*(scale(nmul(X[mu],lift(letter('v'+str(mu)))),-1) for mu in range(4)),
        vg,dag(vg),scale(nmul(th2,nmul(bar2,lift(letter('D')))),s.Rational(1,2)))
    VV=nmul(V,V);G=add(one,V,scale(VV,s.Rational(1,2)));Gi=add(one,scale(V,-1),scale(VV,s.Rational(1,2)))
    C=[]
    for j in range(3):
        psi=add(scale(nmul(theta(0),ff(j+1,1)),-1),nmul(theta(1),ff(j+1,0)))
        C.append(shift(add(lift(letter('c'+str(j))),scale(psi,s.sqrt(2)),nmul(th2,lift(letter('g'+str(j)))))))
    def dint(p,j,bar=False):return {} if j==2 else nop(p,('b' if bar else 'd')+str(j))
    K={}
    for j in range(3):
        a=add(scale(dint(Gi,j,True),s.sqrt(2)),nmul(dag(C[j]),Gi))
        b=add(scale(dint(G,j),-s.sqrt(2)),nmul(C[j],G))
        K=add(K,nmul(a,b),nmul(dint(Gi,j,True),dint(G,j)))
    def DD(p,a):return add(left(p,a),*(scale(nmul(theta(b+2),ext(p,mu)),s.I*sig[mu][a,b]) for mu in range(4) for b in range(2)))
    def BD(p,b):return add(scale(left(p,b+2),-1),*(scale(nmul(theta(a),ext(p,mu)),-s.I*sig[mu][a,b]) for mu in range(4) for a in range(2)))
    def BD2(p):return scale(BD(BD(p,1),0),-2)
    W=[scale(BD2(nmul(Gi,DD(G,a))),-s.Rational(1,4)) for a in range(2)]
    WW=add(nmul(W[1],W[0]),scale(nmul(W[0],W[1]),-1))
    gauge_holo=scale(d2(ntrace(WW)),s.Rational(1,4))
    gauge=trace(add(gauge_holo,adj(gauge_holo)))
    from itertools import permutations
    CS={}
    for i,j,k in permutations(range(3)):
        sign=(-1)**sum(a>b for m,a in enumerate((i,j,k)) for b in (i,j,k)[m+1:])
        CS=add(CS,scale(nmul(C[i],dint(C[k],j)),s.Rational(sign,2)),
            scale(nmul(C[i],ncomm(C[j],C[k])),-s.Rational(sign,6)/s.sqrt(2)))
    F=trace(add(d2(ntrace(CS)),anti2(ntrace(dag(CS)))))
    return {'V':V,'V2':VV,'G':G,'Gi':Gi,'C':C,'K':K,'W':W,'CS':CS,
        'K_component':trace(d4(K)),'gauge_component':gauge,'F_component':F,
        'full':trace(add(d4(K),gauge,F)), 'BD':BD}

def ordered_components(sig):
    psi=[tuple(letter('f'+str(j+1)+'_'+str(a)) for a in range(2)) for j in range(3)]
    lam=tuple(letter('f0_'+str(a)) for a in range(2));cc=[letter('c'+str(j)) for j in range(3)]
    bc=[adj(c) for c in cc]
    kin={}
    for f in [lam]+psi:
        for mu in range(4):
            xx=scale(letter('v'+str(mu)),1/(2*s.I))
            for a in range(2):
                for b in range(2):
                    df=add(op(adj(f[b]),'e'+str(mu)),comm(xx,adj(f[b])))
                    kin=add(kin,scale(mul(f[a],df),-s.I*sig[mu][a,b]))
    raw={}
    for j in range(3):
        derlam=tuple(op(a,'b'+str(j)) if j<2 else {} for a in lam)
        raw=add(raw,scale(spin(derlam,psi[j]),-s.I),scale(spin(lam,tuple(comm(bc[j],a) for a in psi[j])),s.I/s.sqrt(2)))
    cov=lambda a,j:add(op(a,'d'+str(j)),scale(comm(cc[j],a),-1/s.sqrt(2)))
    fermi=add(scale(spin(psi[2],tuple(add(cov(psi[1][a],0),scale(cov(psi[0][a],1),-1)) for a in range(2))),-1),
        scale(mul(cc[2],add(spin(psi[0],psi[1]),scale(spin(psi[1],psi[0]),-1))),1/s.sqrt(2)))
    fprim=scale(add(op(spin(psi[0],psi[2]),'d1'),scale(op(spin(psi[1],psi[2]),'d0'),-1)),-s.Rational(1,2))
    return {'raw_K_chiral':trace(raw),'F_bulk_chiral':trace(fermi),'F_primitive_chiral':trace(fprim),
        'kinetic':trace(kin),'full':trace(add(kin,raw,adj(raw),fermi,adj(fermi),fprim,adj(fprim)))}
