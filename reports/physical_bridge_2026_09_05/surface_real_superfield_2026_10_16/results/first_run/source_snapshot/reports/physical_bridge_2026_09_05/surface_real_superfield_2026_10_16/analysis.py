"""Real F-sector and full boundary multiplet; no science on import.

Extends credited cyclic words with actual matrix-odd parity. Separate
theta expansion/component product, shared author/trace conventions.
"""
import importlib.util,json,sys
from itertools import permutations
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sp=importlib.util.spec_from_file_location('real_superfield_wedge',HERE.parent/'surface_variational_join_2026_10_16/analysis.py')
prior=importlib.util.module_from_spec(sp);sp.loader.exec_module(prior)
wedge=prior.wedge
def clean(p):return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}
def add(*args):
    out={}
    for p in args:
        for k,c in p.items():out[k]=out.get(k,0)+c
    return clean(out)
def scale(p,c):return clean({k:c*v for k,v in p.items()})
def letter(name):return {(name,):s.Integer(1)}
def normalize(ops,base):return ':'.join(sorted(ops)+[base])
def alter(a,op):
    parts=a.split(':');return normalize(parts[:-1]+[op],parts[-1])
def base(a):return a.split(':')[-1]
def odd(a):return int(base(a).lstrip('~').startswith('f'))
def parity(w):return sum(odd(a) for a in w)%2
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():out[u+v]=out.get(u+v,0)+c*d
    return clean(out)
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def derivative(p,j):
    out={}
    for w,c in p.items():
        for k,a in enumerate(w):
            ww=w[:k]+(alter(a,'d'+str(j)),)+w[k+1:]
            out[ww]=out.get(ww,0)+c
    return clean(out)
def variation(p):
    out={}
    for w,c in p.items():
        for k,a in enumerate(w):
            ww=w[:k]+(alter(a,'v'),)+w[k+1:]
            out[ww]=out.get(ww,0)+c
    return clean(out)
def trace(p):
    out={}
    for w,c in p.items():
        if not w:out[()]=out.get((),0)+c;continue
        rots=[(w[k:]+w[:k],(-1)**(parity(w[:k])*parity(w[k:]))) for k in range(len(w))]
        key=min(a for a,b in rots);signs={b for a,b in rots if a==key}
        if len(signs)>1:continue
        out[key]=out.get(key,0)+c*next(iter(signs))
    return clean(out)
def conjugate_letter(a):
    v=a.split(':');ops=[('b'+q[1:] if q.startswith('d') else 'd'+q[1:] if q.startswith('b') else q) for q in v[:-1]]
    return normalize(ops,v[-1][1:] if v[-1].startswith('~') else '~'+v[-1])
def dagger(p):
    out={}
    for w,c in p.items():
        k=tuple(conjugate_letter(a) for a in reversed(w));out[k]=out.get(k,0)+s.conjugate(c)
    return clean(out)
def same(a,b):return not add(a,scale(b,-1))
def encoded(p):return [[list(k),str(v)] for k,v in sorted(p.items())]
def spin(a,b):return add(scale(mul(a[0],b[1]),-1),mul(a[1],b[0]))

# Full superspace monomials: theta tuple, matrix word. Coefficient odd
# matrices anticommute with theta, not with each other as matrix products.
def nmul(a,b,commuting_fermion=False):
    out={}
    for (u,w),c in a.items():
        for (v,z),d in b.items():
            for uv,e in wedge({u:1},{v:1}).items():
                key=(uv,w+z);sign=1 if commuting_fermion else (-1)**(parity(w)*len(v))
                out[key]=out.get(key,0)+c*d*e*sign
    return clean(out)
def lift(p,theta=()):return {(theta,w):c for w,c in p.items()}
def nder(p,j):
    return add(*(lift(derivative({w:c},j),th) for (th,w),c in p.items()))
def nvar(p):return add(*(lift(variation({w:c}),th) for (th,w),c in p.items()))
def ntrace(p):return add(*(lift(trace({w:c}),th) for (th,w),c in p.items()))
def ndagger(p):
    out={};swap={0:2,1:3,2:0,3:1}
    for (th,w),c in p.items():
        new=tuple(swap[j] for j in reversed(th))
        inv=sum(a>b for k,a in enumerate(new) for b in new[k+1:])
        sign=(-1)**(inv+parity(w)*len(th));ww=tuple(conjugate_letter(a) for a in reversed(w))
        key=(tuple(sorted(new)),ww);out[key]=out.get(key,0)+sign*s.conjugate(c)
    return clean(out)
def component(p,theta=(0,1),factor=-s.Rational(1,2)):
    return clean({w:factor*c for (th,w),c in p.items() if th==theta})
def rawfield(i):
    return add(lift(letter('c'+str(i))),scale(lift(letter('f'+str(i)+'_1'),(0,)),-s.sqrt(2)),
        scale(lift(letter('f'+str(i)+'_0'),(1,)),s.sqrt(2)),scale(lift(letter('g'+str(i)),(0,1)),-2))

class Native:
    field=staticmethod(rawfield);plus=staticmethod(add);times=staticmethod(scale)
    product=staticmethod(nmul);d=staticmethod(nder);tr=staticmethod(ntrace);var=staticmethod(nvar)
    F=staticmethod(component)
    @staticmethod
    equal(a,b):return same(a,b)
    @staticmethod
    body(a):return component(a,(),1)

# Reference never multiplies theta; it propagates full chiral components
# by the separate ordered product rule, including both Weyl components.
class Reference:
    @staticmethod
    field(i):return (letter('c'+str(i)),(letter('f'+str(i)+'_0'),letter('f'+str(i)+'_1')),letter('g'+str(i)))
    @staticmethod
    plus(*xs):return (add(*(a[0] for a in xs)),tuple(add(*(a[1][j] for a in xs)) for j in range(2)),add(*(a[2] for a in xs)))
    @staticmethod
    times(a,c):return (scale(a[0],c),tuple(scale(p,c) for p in a[1]),scale(a[2],c))
    @staticmethod
    product(a,b):return (mul(a[0],b[0]),tuple(add(mul(a[0],b[1][j]),mul(a[1][j],b[0])) for j in range(2)),
        add(mul(a[0],b[2]),mul(a[2],b[0]),scale(spin(a[1],b[1]),-1)))
    @staticmethod
    d(a,j):return (derivative(a[0],j),tuple(derivative(p,j) for p in a[1]),derivative(a[2],j))
    @staticmethod
    tr(a):return (trace(a[0]),tuple(trace(p) for p in a[1]),trace(a[2]))
    @staticmethod
    var(a):return (variation(a[0]),tuple(variation(p) for p in a[1]),variation(a[2]))
    @staticmethod
    F(a):return a[2]
    @staticmethod
    body(a):return a[0]
    @staticmethod
    equal(a,b):return same(a[0],b[0]) and all(same(x,y) for x,y in zip(a[1],b[1])) and same(a[2],b[2])

def run(engine):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    e=engine;plus=e.plus;times=e.times;prod=e.product;d=e.d;tr=e.tr
    cm=lambda a,b:plus(prod(a,b),times(prod(b,a),-1))
    C=[e.field(i) for i in range(3)]
    A=[times(a,-1/s.sqrt(2)) for a in C[:2]];P=times(C[2],s.sqrt(2))
    zero=times(C[0],0);DD=lambda a,j:d(a,j) if j<2 else zero
    eps=lambda t:(-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
    derivative_part=plus(*(times(prod(C[i],DD(C[k],j)),eps((i,j,k))) for i,j,k in permutations(range(3))))
    cubic=plus(*(times(prod(C[i],cm(C[j],C[k])),eps((i,j,k))) for i,j,k in permutations(range(3))))
    parent=times(tr(plus(derivative_part,times(cubic,-1/(3*s.sqrt(2))))),s.Rational(1,2))
    F=plus(d(A[1],0),times(d(A[0],1),-1),cm(A[0],A[1]))
    W=times(tr(prod(P,F)),-1)
    primitive=times(plus(d(tr(prod(C[0],C[2])),1),times(d(tr(prod(C[1],C[2])),0),-1)),s.Rational(1,2))
    ck('whole superfield two derivative reduction',e.equal(parent,plus(W,primitive)))
    ck('six cubic permutations retained',e.equal(tr(cubic),times(tr(prod(C[2],cm(C[0],C[1]))),6)))
    ck('nonzero full transgression not dropped',bool(e.F(primitive)) and not e.equal(parent,W))
    ck('nonlinear curvature not omitted',not e.equal(F,plus(d(A[1],0),times(d(A[0],1),-1))))
    # Expand predicted component density in actual rescaled reduced fields.
    bodies=[e.body(a) for a in A];p=e.body(P)
    psi=[tuple(scale(letter('f'+str(i)+'_'+str(j)),-1/s.sqrt(2)) for j in range(2)) for i in range(2)]
    chi=tuple(scale(letter('f2_'+str(j)),s.sqrt(2)) for j in range(2))
    G=[scale(letter('g'+str(i)),-1/s.sqrt(2)) for i in range(2)];H=scale(letter('g2'),s.sqrt(2))
    cov=lambda a,j:add(derivative(a,j),comm(bodies[j],a))
    rawaux=trace(add(scale(mul(H,e.body(F)),-1),scale(mul(p,add(cov(G[1],0),scale(cov(G[0],1),-1))),-1)))
    fpsi=tuple(add(cov(psi[1][j],0),scale(cov(psi[0][j],1),-1)) for j in range(2))
    ferm=trace(add(spin(chi,fpsi),mul(p,add(spin(psi[0],psi[1]),scale(spin(psi[1],psi[0]),-1)))))
    ck('all actual fermion auxiliary F components',same(e.F(W),add(rawaux,ferm)))
    auxbulk=trace(add(scale(mul(H,e.body(F)),-1),mul(cov(p,0),G[1]),scale(mul(cov(p,1),G[0]),-1)))
    auxend=add(scale(derivative(trace(mul(p,G[1])),0),-1),derivative(trace(mul(p,G[0])),1))
    ck('auxiliary integration by parts keeps boundary',same(rawaux,add(auxbulk,auxend)))
    ck('auxiliary primitive nonzero control',bool(auxend) and not same(rawaux,auxbulk))
    ck('both derivative and cubic fermions nonzero',bool(ferm) and not same(e.F(W),rawaux))
    vA=[e.var(a) for a in A];vP=e.var(P)
    covS=lambda a,j:plus(d(a,j),cm(A[j],a))
    bulk=plus(times(tr(prod(vP,F)),-1),tr(prod(covS(P,0),vA[1])),times(tr(prod(covS(P,1),vA[0])),-1))
    surface=plus(times(d(tr(prod(P,vA[1])),0),-1),d(tr(prod(P,vA[0])),1))
    ck('whole superfield first variation with surface',e.equal(e.var(W),plus(bulk,surface)))
    ck('variation surface cannot be dropped',not e.equal(e.var(W),bulk))
    normal=tr(prod(P,vA[0]));nf=e.F(normal)
    def kill(a,names):return {w:c for w,c in a.items() if not any(base(q).lstrip('~') in names for q in w)}
    fixed={'c0','g0','f0_0','f0_1'}
    ck('whole tangential chiral Dirichlet cancels F surface',not kill(nf,fixed))
    ck('lowest boson Dirichlet alone fails boundary multiplet',bool(kill(nf,{'c0'})))
    ck('boundary auxiliary and fermion terms both retained',any(any(base(q)=='g0' for q in w) for w in nf) and any(any(base(q).startswith('f0') for q in w) for w in nf))
    # Full native dagger of an actual superfield, NOT a filled lower block.
    nC=[Native.field(j) for j in range(3)];nA=[scale(a,-1/s.sqrt(2)) for a in nC[:2]];nP=scale(nC[2],s.sqrt(2))
    nF=add(nder(nA[1],0),scale(nder(nA[0],1),-1),nmul(nA[0],nA[1]),scale(nmul(nA[1],nA[0]),-1))
    nW=scale(ntrace(nmul(nP,nF)),-1)
    anti=component(ndagger(nW),(2,3),s.Rational(1,2));ch=component(nW)
    ck('actual whole superfield conjugate F extraction',same(trace(anti),trace(dagger(ch))))
    real=add(trace(ch),trace(anti))
    ck('actual real F action involution',bool(real) and same(trace(dagger(real)),real))
    ck('wrong anti Berezin sign rejected',not same(scale(anti,-1),dagger(ch)))
    ck('dagger exact anti multiplicative and involutive',same(ndagger(nmul(nC[0],nC[1])),nmul(ndagger(nC[1]),ndagger(nC[0]))) and same(ndagger(ndagger(nW)),nW))
    t=lift({():1},(0,));f=lift(letter('f0_0'))
    ck('theta odd matrix anticommutes',same(nmul(t,f),scale(nmul(f,t),-1)) and bool(nmul(t,f)))
    wrong=component(nmul(nC[0],nC[1],True));right=component(nmul(nC[0],nC[1]))
    ck('commuting fermion instrument fails F term',not same(wrong,right))
    ff=letter('f0_0');gg=letter('f1_1')
    ck('actual graded trace cyclicity',same(trace(mul(ff,gg)),scale(trace(mul(gg,ff)),-1)) and bool(trace(mul(ff,gg))))
    # Formal unrestricted small-gauge covariance, with all derivative jets.
    lam=letter('Lambda');a=bodies;pp=p
    da=[add(derivative(lam,j),comm(a[j],lam)) for j in range(2)]
    fbody=e.body(F)
    df=add(derivative(da[1],0),scale(derivative(da[0],1),-1),comm(da[0],a[1]),comm(a[0],da[1]))
    ck('all small gauge curvature jets covariant',same(df,comm(fbody,lam)))
    ck('real parent holomorphic trace gauge invariant',not trace(add(mul(comm(pp,lam),fbody),mul(pp,df))))
    missing=add(df,scale(derivative(derivative(lam,1),0),-1),derivative(derivative(lam,0),1))
    ck('paired second derivative deletion Ward blind',same(missing,df))
    # Deleting both second derivatives is blind since they commute; delete
    # the FIRST derivative commutator compensation instead, independently.
    nojets=[comm(a[j],lam) for j in range(2)]
    bad=add(derivative(nojets[1],0),scale(derivative(nojets[0],1),-1),comm(nojets[0],a[1]),comm(a[0],nojets[1]))
    ck('omitted gauge connection derivative detected',not same(bad,comm(fbody,lam)))
    ck('tangential gauge derivative violates cutoff law',bool(derivative(lam,0)))
    # Positive reduced chiral metric follows the actual field rescalings.
    h=(s.Integer(2),s.Integer(2),s.Rational(1,2));inverse=[]
    for j,hj in enumerate(h):
        x,y,bx,by=s.symbols('x y bx by',real=True)
        ll=hj*(x*x+y*y)+2*(bx*x-by*y);sol={x:-bx/hj,y:by/hj}
        ck('actual auxiliary Gaussian '+str(j),s.expand(ll.diff(x).subs(sol))==0 and s.expand(ll.diff(y).subs(sol))==0 and s.expand(ll.subs(sol)+(bx*bx+by*by)/hj)==0)
        inverse.append(str(1/hj))
    ck('auxiliary inverse metric not copied',inverse==['1/2','1/2','2'])
    records['F_components']={'parent':encoded(e.F(parent)),'reduced':encoded(e.F(W)),
        'transgression':encoded(e.F(primitive)),'auxiliary_bulk':encoded(auxbulk),'auxiliary_end':encoded(auxend),
        'all_fermions':encoded(ferm),'first_variation_surface':encoded(e.F(surface)),
        'normal_boundary_full_F':encoded(nf),'actual_conjugate':encoded(anti),'real_F_density':encoded(real)}
    records['metrics']={'chiral':['2','2','1/2'],'auxiliary_inverse':inverse,
        'F_potential':'2|F01|^2+(|D0p|^2+|D1p|^2)/2','scope':'real F-sector, not full D/gaugino/MW action map'}
    records['boundary']={'finite_cutoff':'V=0,A_t=0 as whole superfields; A_normal,P free',
        'gauge_cost':'boundary value externally/tangentially constant, normal jet free',
        'scope':'smooth supplied cutoff law, not singular limit or prior Dirac-domain identification'}
    records['status']='real reduced F action and retained whole superfield boundary; full component/MW/kinetic/singular/global physical joint unearned'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(engine):
    data=run(engine);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
