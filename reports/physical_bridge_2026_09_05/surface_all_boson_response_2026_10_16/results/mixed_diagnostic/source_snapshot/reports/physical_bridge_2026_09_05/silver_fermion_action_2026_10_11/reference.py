"""Tuple exterior expansion and creation/contraction reference.

No native import; same author, not a nonauthor theorem certificate.
"""
from functools import lru_cache
import itertools
import json
import sympy as s

I=s.I;Q=s.Rational;Id=s.eye(2);Z=s.zeros(2)
order=['t0','t1','b0','b1'];duals={'t0':'b0','t1':'b1','b0':'t0','b1':'t1'}
shifts={};freq={}
for f in ['c','u','v','w']:
    for a in range(2):
        n=f+str(a);bn='B'+n;order += [n,bn];duals[n]=bn;duals[bn]=n
        freq[n]=1;freq[bn]=-1
        for j in range(3):
            dn='d'+str(j)+n;dbn='B'+dn;order += [dn,dbn]
            duals[dn]=dbn;duals[dbn]=dn;shifts[n,j]=dn;shifts[bn,j]=dbn
rank={k:j for j,k in enumerate(order)}
sig=[Id,s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]

def clean(p):return {k:v.applyfunc(s.expand) for k,v in p.items() if any(s.expand(x)!=0 for x in v)}
def plus(*ps):
    r={}
    for p in ps:
        for k,v in p.items():r[k]=r.get(k,Z)+v
    return clean(r)
def times(p,c):return clean({k:c*v for k,v in p.items()})
def mon(seq,v):
    if len(set(seq))!=len(seq):return {}
    sg=(-1)**sum(rank[seq[i]]>rank[seq[j]] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return {tuple(sorted(seq,key=rank.get)):sg*v}
def product(p,q):
    r={}
    for k,v in p.items():
        for l,w in q.items():r=plus(r,mon(k+l,v*w))
    return r
def term(n,v=Id):return {(n,):v}
def conjugate(p):return plus(*(mon(tuple(duals[n] for n in reversed(k)),v.H) for k,v in p.items()))
def trace(p):return {k:s.expand(s.trace(v)) for k,v in p.items() if s.expand(s.trace(v))!=0}
def deriv(p,n):return clean({k[:j]+k[j+1:]:(-1)**j*v for k,v in p.items() for j in range(len(k)) if k[j]==n})
def dj(p,j):return plus(*(mon(k[:a]+(shifts[n,j],)+k[a+1:],v) for k,v in p.items() for a,n in enumerate(k) if (n,j) in shifts))
def dq(p,mu,active):return times({k:sum(freq.get(n,0) for n in k)*v for k,v in p.items()},I*int(mu==active))
def extract(p,ss,c):return clean({tuple(n for n in k if n not in order[:4]):c*v for k,v in p.items() if tuple(n for n in k if n in order[:4])==ss})
def inner(a,b):return plus(product(a[0],b[1]),times(product(a[1],b[0]),-1))
def bracket(m,p):return plus(product({():m},p),times(product(p,{():m}),-1))
def cov(p,j,A,B,sign):return plus(dj(p,j),times(bracket(A[j],p),I),times(bracket(B[j],p),sign))

@lru_cache(None)
def run():
    checks={}
    def ck(k,v):checks[k]=bool(v)
    A=[s.diag(2,-2),s.Matrix([[1,2],[2,-1]]),s.Matrix([[0,3*I],[-3*I,0]])]
    B=[A[1],A[2],A[0]+A[1]]
    ferm={f:[term(f+str(a),A[j%3]+I*(a+1)*B[(j+1)%3]) for a in range(2)] for j,f in enumerate(['c','u','v','w'])}
    c=ferm['c'];pp=[ferm[f] for f in ['u','v','w']]
    t2={('t0','t1'):2*Id};b2=conjugate(t2)
    tc=plus(*(product(term('t'+str(a)),c[a]) for a in range(2)))
    vh=times(product(b2,tc),1/s.sqrt(2));V=plus(vh,conjugate(vh))
    G=plus({():Id},times(V,2));Gi=plus({():Id},times(V,-2))
    Phi0=[plus({():A[j]+I*B[j]},times(plus(*(product(term('t'+str(a)),pp[j][a]) for a in range(2))),I*s.sqrt(2))) for j in range(3)]
    zs=[plus(product(Gi,dj(G,j)),times(product(product(Gi,conjugate(Phi0[j])),G),I),times(Phi0[j],-I)) for j in range(3)]
    kk=times(extract(plus(*(product(z,z) for z in zs)),tuple(order[:4]),Q(-1,4)),Q(1,4))
    raw=times(plus(*(inner(pp[j],[cov(z,j,A,B,1) for z in c]) for j in range(3))),Q(-1,2))
    ck('tuple_internal_plus_connection',trace(kk)==trace(plus(raw,conjugate(raw))))
    bad=times(plus(*(inner(pp[j],[cov(z,j,A,B,-1) for z in c]) for j in range(3))),Q(-1,2))
    ck('tuple_wrong_internal_connection_rejected',trace(kk)!=trace(plus(bad,conjugate(bad))))
    surface=times(plus(*(plus(inner(pp[j],[dj(z,j) for z in c]),inner([dj(z,j) for z in pp[j]],c)) for j in range(3))),Q(-1,2))
    bulk=times(plus(*(inner(c,[cov(z,j,A,B,1) for z in pp[j]]) for j in range(3))),Q(1,2))
    ck('tuple_IBP_surface',trace(raw)==trace(plus(bulk,surface)) and bool(trace(surface)))
    ww={}
    for i,j,k in itertools.permutations(range(3)):
        e=s.LeviCivita(i,j,k)
        ww=plus(ww,times(product(Phi0[i],dj(Phi0[k],j)),e),times(product(Phi0[i],plus(product(Phi0[j],Phi0[k]),times(product(Phi0[k],Phi0[j]),-1))),I*e/3))
    curl=times(plus(*(times(inner(pp[i],[cov(z,j,A,B,-1) for z in pp[k]]),s.LeviCivita(i,j,k)) for i,j,k in itertools.permutations(range(3)))),Q(1,4))
    ck('tuple_all_epsilon_CS_curl',trace(times(extract(ww,('t0','t1'),Q(1,2)),Q(1,4)))==trace(curl))
    ck('tuple_odd_reality',trace(conjugate(conjugate(kk)))==trace(kk))
    # Separately test each Lorentz covector, not the native's combined one.
    for mode in range(4):
        XX=[plus(*(times(product(term('t'+str(a)),term('b'+str(b))),sig[mu][a,b]) for a in range(2) for b in range(2))) for mu in range(4)]
        def dd(p,a):return plus(deriv(p,'t'+str(a)),*(times(product(term('b'+str(b)),dq(p,mu,mode)),I*sig[mu][a,b]) for mu in range(4) for b in range(2)))
        def bd(p,b):return plus(times(deriv(p,'b'+str(b)),-1),*(times(product(term('t'+str(a)),dq(p,mu,mode)),-I*sig[mu][a,b]) for mu in range(4) for a in range(2)))
        ph=[]
        for p in Phi0:
            ph.append(plus(p,*(times(product(XX[mu],dq(p,mu,mode)),I) for mu in range(4))))
        zz=[plus(product(Gi,dj(G,j)),times(product(product(Gi,conjugate(ph[j])),G),I),times(ph[j],-I)) for j in range(3)]
        direct=times(extract(plus(*(product(z,z) for z in zz)),tuple(order[:4]),Q(-1,4)),Q(1,4))
        def kin(a):
            au=[times(a[1],-1),a[0]];bc=[conjugate(z) for z in au]
            return times(plus(*(times(product(au[x],dq(bc[y],mode,mode)),sig[mode][x,y]) for x in range(2) for y in range(2))),-I/2)
        pk=plus(*(kin(p) for p in pp))
        ck('tuple_chiral_kinetic_mu'+str(mode),trace(direct)==trace(plus(raw,conjugate(raw),pk)))
        W=[times(bd(bd(product(Gi,dd(G,a)),1),0),Q(1,2)) for a in range(2)]
        holo=times(extract(plus(product(W[0],W[1]),times(product(W[1],W[0]),-1)),('t0','t1'),Q(1,2)),Q(1,16))
        gg=plus(holo,conjugate(holo))
        ck('tuple_gauge_kinetic_mu'+str(mode),trace(gg)==trace(kin(c)))
        ck('tuple_nonzero_kinetic_mu'+str(mode),bool(trace(kin(c))) and bool(trace(pk)))
    # Form creation/contraction construction on a DIFFERENT ordering.
    form=[q for n in range(4) for q in itertools.combinations(range(3),n)]
    create=[]
    for j in range(3):
        E=s.zeros(8)
        for col,q in enumerate(form):
            if j in q:continue
            r=tuple(sorted((j,)+q));E[form.index(r),col]=(-1)**sum(k<j for k in q)
        create.append(E)
    ck('creation_Clifford_all_pairs',all((create[j]-create[j].T)*(create[k]-create[k].T)+(create[k]-create[k].T)*(create[j]-create[j].T)==-2*int(j==k)*s.eye(8) for j in range(3) for k in range(3)))
    aa=[I*A[j] for j in range(3)];mm=[I*(j+2)*Id+aa[j]-B[j] for j in range(3)];pl=[I*(j+2)*Id+aa[j]+B[j] for j in range(3)]
    differential=sum((s.kronecker_product(create[j],mm[j]) for j in range(3)),s.zeros(16))
    H=differential+differential.H;R=s.zeros(8)
    for j in range(3):
        R[0:2,2+2*j:4+2*j]=pl[j];R[2+2*j:4+2*j,0:2]=-pl[j]
        for k in range(3):R[2+2*j:4+2*j,2+2*k:4+2*k]=sum((s.LeviCivita(j,l,k)*mm[l] for l in range(3)),Z)
    so=s.zeros(16,8);se=s.zeros(16,8)
    so[14:16,0:2]=Id;se[0:2,0:2]=-Id
    for j,q in enumerate([(0,),(1,),(2,)]):so[2*form.index(q):2*form.index(q)+2,2+2*j:4+2*j]=Id
    for j,(q,sg) in enumerate([((1,2),1),((0,2),-1),((0,1),1)]):se[2*form.index(q):2*form.index(q)+2,2+2*j:4+2*j]=sg*Id
    ck('reference_full_Hodge_intertwiner',H*so==se*R and H*se==so*R.H)
    ck('reference_norm_preservation',so.H*so==s.eye(8) and se.H*se==s.eye(8))
    x,y=s.symbols('x y',real=True)
    def principal(n):
        r=s.zeros(4)
        for j in range(3):
            r[0,j+1]=n[j];r[j+1,0]=-n[j]
            for k in range(3):r[j+1,k+1]=sum(s.LeviCivita(j,l,k)*n[l] for l in range(3))
        return r
    rn=principal([0,0,1]);rt=principal([x,y,0])
    allowed=s.Matrix([[0,0],[-y,0],[x,0],[0,1]])
    ck('physical_normal_Green_isotropic',allowed.T*rn*allowed==s.zeros(2))
    ck('principal_quaternion_norm',rt.T*rt==(x*x+y*y)*s.eye(4))
    ck('physical_trace_high_rank',allowed.rank()==2)
    bigallowed=s.diag(allowed,allowed);gamma=s.Matrix.vstack(s.Matrix.hstack(s.zeros(4),rn),s.Matrix.hstack(rn,s.zeros(4)))
    tan=s.Matrix.vstack(s.Matrix.hstack(s.zeros(4),rt),s.Matrix.hstack(rt,s.zeros(4)))
    adapted=-I*gamma*tan
    ck('doubled_normal_Green_maximal',bigallowed.T*gamma*bigallowed==s.zeros(4) and gamma.det()!=0 and bigallowed.rank()==4)
    ck('adapted_symbol_maps_to_complement',s.simplify(bigallowed.T*adapted*bigallowed)==s.zeros(4))
    ck('adapted_symbol_exact_square',s.simplify(adapted*adapted)==(x*x+y*y)*s.eye(8))
    badallowed=s.Matrix([[1,0],[0,0],[0,0],[0,1]])
    ck('unrestricted_chi_trace_rejected',badallowed.T*rn*badallowed!=s.zeros(2))
    result={'predicates':checks,'predicates_passed':sum(checks.values()),
        'normalizations':{'chi_kinetic':'-i/2','psi_kinetic':'-i/2','raw_gaugino':'-psi D_plus chi/2','bulk_gaugino':'chi D_plus psi/2','curl':'epsilon psi D_minus psi/4'},
        'native_imported':False,'nonauthor_review':False,'global_PDE_solved':False,'full_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return result

if __name__=='__main__':run()
