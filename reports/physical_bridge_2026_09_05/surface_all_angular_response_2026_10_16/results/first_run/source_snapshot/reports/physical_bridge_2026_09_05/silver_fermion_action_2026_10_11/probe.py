"""Direct canonical fermion expansion. Not a global PDE or full SM test."""
from functools import lru_cache
import json
import sympy as s

I=s.I; Q=s.Rational; ONE=s.eye(2); ZERO=s.zeros(2)
names=['t1','t2','b1','b2']; adj={0:2,1:3,2:0,3:1}
fields={}; jets={}; momentum={}
for f in ['chi','p0','p1','p2']:
    for a in range(2):
        n=len(names); names += [f+str(a),'bar_'+f+str(a)]
        adj[n]=n+1;adj[n+1]=n;fields[f,a]=n
        for j in range(3):
            d=len(names);names += [f'd{j}_{f}{a}',f'bar_d{j}_{f}{a}']
            adj[d]=d+1;adj[d+1]=d;jets[n,j]=d;jets[n+1,j]=d+1
        momentum[n]=1;momentum[n+1]=-1
NG=len(names)
SIG=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
P=[2,3,5,7]

def mz(a):return all(s.expand(x)==0 for x in a)
def clean(a):return {u:c.applyfunc(s.expand) for u,c in a.items() if not mz(c)}
def add(*args):
    z={}
    for a in args:
        for u,c in a.items():z[u]=z.get(u,ZERO)+c
    return clean(z)
def scale(a,c):return clean({u:c*v for u,v in a.items()})
def mul(a,b):
    z={}
    for u,c in a.items():
        for v,d in b.items():
            if u&v:continue
            swaps=0;w=u
            while w:
                bit=w&-w;swaps+=(v&(bit-1)).bit_count();w-=bit
            z[u|v]=z.get(u|v,ZERO)+(-1)**swaps*c*d
    return clean(z)
def gen(j,c=ONE):return {1<<j:c}
def left(a,j):return clean({u^(1<<j):(-1)**((u&((1<<j)-1)).bit_count())*c for u,c in a.items() if u&(1<<j)})
def dag(a):
    z={}
    for u,c in a.items():
        term={0:c.H}
        for j in reversed(range(NG)):
            if u&(1<<j):term=mul(term,gen(adj[j]))
        z=add(z,term)
    return z
def eq(a,b):return not add(a,scale(b,-1))
def ext(a,mu):return clean({u:I*P[mu]*sum(v for j,v in momentum.items() if u&(1<<j))*c for u,c in a.items()})
def dint(a,j):
    z={}
    for u,c in a.items():
        seq=[k for k in range(NG) if u&(1<<k)]
        for k in seq:
            if (k,j) not in jets:continue
            term={0:c}
            for l in seq:term=mul(term,gen(jets[k,j] if l==k else l))
            z=add(z,term)
    return z
def tr(a):return {u:s.expand(s.trace(c)) for u,c in a.items() if s.expand(s.trace(c))!=0}
def integrate(a,mask,c):
    # Superspace generators precede every component generator.
    return clean({u^mask:c*v for u,v in a.items() if u&15==mask})
def d4(a):return integrate(a,15,Q(-1,4))
def d2(a):return integrate(a,3,Q(1,2))
def dot(a,b):return add(mul(a[0],b[1]),scale(mul(a[1],b[0]),-1))
def comm(p,a):return add(mul({0:p},a),scale(mul(a,{0:p}),-1))
def cov(a,j,AA,BB,sign):return add(dint(a,j),scale(comm(AA[j],a),I),scale(comm(BB[j],a),sign))
def shift(a,X):
    first=add(*(scale(mul(X[mu],ext(a,mu)),I) for mu in range(4)))
    second=add(*(scale(mul(X[mu],mul(X[nu],ext(ext(a,nu),mu))),Q(-1,2)) for mu in range(4) for nu in range(4)))
    return add(a,first,second)
def D(a,alpha):return add(left(a,alpha),*(scale(mul(gen(b+2),ext(a,mu)),I*SIG[mu][alpha,b]) for mu in range(4) for b in range(2)))
def BD(a,b):return add(scale(left(a,b+2),-1),*(scale(mul(gen(alpha),ext(a,mu)),-I*SIG[mu][alpha,b]) for mu in range(4) for alpha in range(2)))
def BD2(a):return scale(BD(BD(a,1),0),-2)
def current(a,b):
    au=[scale(a[1],-1),a[0]];bu=[scale(b[1],-1),b[0]]
    return add(*(scale(mul(au[x],ext(bu[y],mu)),SIG[mu][x,y]) for mu in range(4) for x in range(2) for y in range(2)))

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v)
    X=s.diag(1,-1);Y=s.Matrix([[0,1+I],[1-I,0]]);T=s.Matrix([[1,I],[-I,-1]])
    AA=[X,Y,T];BB=[T,X,2*Y]
    mats=[X+I*Y,Y+2*I*T,T-I*X,2*X+I*T]
    ff={f:[gen(fields[f,a],mats[i]+a*Y) for a in range(2)] for i,f in enumerate(['chi','p0','p1','p2'])}
    chi=ff['chi'];psi=[ff['p'+str(i)] for i in range(3)]
    bc=[dag(c) for c in chi];bp=[[dag(c) for c in p] for p in psi]
    th2={3:2*ONE};bar2=dag(th2)
    tc=add(*(mul(gen(a),chi[a]) for a in range(2)))
    half=scale(mul(bar2,tc),1/s.sqrt(2));V=add(half,dag(half))
    G=add({0:ONE},scale(V,2));Gi=add({0:ONE},scale(V,-2))
    XX=[add(*(scale(mul(gen(a),gen(b+2)),SIG[mu][a,b]) for a in range(2) for b in range(2))) for mu in range(4)]
    PP=[shift(add({0:AA[i]+I*BB[i]},scale(add(*(mul(gen(a),psi[i][a]) for a in range(2))),I*s.sqrt(2))),XX) for i in range(3)]
    Z=[add(mul(Gi,dint(G,j)),scale(mul(mul(Gi,dag(PP[j])),G),I),scale(PP[j],-I)) for j in range(3)]
    ck('V_actual_reality',eq(V,dag(V)))
    ck('G_exact_inverse',eq(mul(G,Gi),{0:ONE}) and not mul(V,V))
    ck('Phi_actual_chirality',all(not BD(p,b) for p in PP for b in range(2)))
    ck('Z_twisted_reality',all(eq(dag(z),mul(mul(G,z),Gi)) for z in Z))
    rawK=scale(d4(add(*(mul(z,z) for z in Z))),Q(1,4))
    rawplus=scale(add(*(dot(psi[j],[cov(c,j,AA,BB,1) for c in chi]) for j in range(3))),Q(-1,2))
    rawminus=scale(add(*(dot(psi[j],[cov(c,j,AA,BB,-1) for c in chi]) for j in range(3))),Q(-1,2))
    kineticP=scale(add(*(current(p,b) for p,b in zip(psi,bp))),-I/2)
    expected=add(rawplus,dag(rawplus),kineticP)
    ck('direct_K_raw_plus_connection',tr(rawK)==tr(expected))
    ck('wrong_gaugino_connection_rejected',tr(rawK)!=tr(add(rawminus,dag(rawminus),kineticP)))
    ck('nonzero_B_gaugino_interaction',tr(add(rawplus,scale(rawminus,-1)))!={})
    surface=scale(add(*(add(dot(psi[j],dint_spin(chi,j)),dot(dint_spin(psi[j],j),chi)) for j in range(3))),Q(-1,2))
    bulk=scale(add(*(dot(chi,[cov(c,j,AA,BB,1) for c in psi[j]]) for j in range(3))),Q(1,2))
    ck('gaugino_IBP_retains_surface',tr(rawplus)==tr(add(bulk,surface)))
    ck('gaugino_surface_nonzero',bool(tr(surface)))
    rawW={}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                e=s.LeviCivita(i,j,k)
                if e:rawW=add(rawW,scale(mul(PP[i],dint(PP[k],j)),e),scale(mul(PP[i],add(mul(PP[j],PP[k]),scale(mul(PP[k],PP[j]),-1))),I*e/3))
    curl=scale(add(*(scale(dot(psi[i],[cov(c,j,AA,BB,-1) for c in psi[k]]),s.LeviCivita(i,j,k)) for i in range(3) for j in range(3) for k in range(3) if s.LeviCivita(i,j,k))),Q(1,4))
    ck('direct_CS_holomorphic_curl',tr(scale(d2(rawW),Q(1,4)))==tr(curl))
    wrongcurl=scale(add(*(scale(dot(psi[i],[cov(c,j,AA,BB,1) for c in psi[k]]),s.LeviCivita(i,j,k)) for i in range(3) for j in range(3) for k in range(3) if s.LeviCivita(i,j,k))),Q(1,4))
    ck('wrong_curl_connection_rejected',tr(curl)!=tr(wrongcurl))
    Ws=[scale(BD2(mul(Gi,D(G,a))),Q(-1,4)) for a in range(2)]
    WW=add(mul(Ws[0],Ws[1]),scale(mul(Ws[1],Ws[0]),-1))
    holG=scale(d2(WW),Q(1,16));gauge=add(holG,dag(holG))
    kineticC=scale(current(chi,bc),-I/2)
    ck('direct_gauge_kinetic_norm',tr(gauge)==tr(kineticC))
    ck('kinetic_norm_nonzero',bool(tr(kineticC)) and bool(tr(kineticP)))
    ck('wrong_relative_kinetic_norm_rejected',tr(gauge)!=tr(scale(kineticC,2)))
    ck('odd_adjoints_involutive',all(eq(dag(dag(p)),p) for p in PP+[V]))
    # Local operator map: even coordinates (scalar, star(twoform)); odd
    # coordinates (oneform, volume coefficient). Coefficient order is kept.
    aa=[I*a for a in AA];bb=BB
    # Adjoint representation operators on the four matrix-unit coordinates.
    basis=[s.Matrix(2,2,lambda r,c:int(r==i and c==j)) for i in range(2) for j in range(2)]
    def admat(a):return s.Matrix.hstack(*(s.Matrix(list(a*c-c*a)) for c in basis))
    avec=[admat(a) for a in aa];bvec=[admat(b) for b in bb]
    km=[s.Integer(2),s.Integer(3),s.Integer(5)]
    minus=[I*km[j]*s.eye(4)+avec[j]-bvec[j] for j in range(3)]
    plus=[I*km[j]*s.eye(4)+avec[j]+bvec[j] for j in range(3)]
    Z4=s.zeros(4);R=s.zeros(16)
    # R on (lambda,rho_x,rho_y,rho_z).
    for j in range(3):
        R[0:4,4+4*j:8+4*j]=plus[j]
        R[4+4*j:8+4*j,0:4]=-plus[j]
        for k in range(3):
            val=sum((s.LeviCivita(j,l,k)*minus[l] for l in range(3)),Z4)
            R[4+4*j:8+4*j,4+4*k:8+4*k]=val
    # Build d with actual form masks and adjoint, independently of R blocks.
    masks=list(range(8));d=s.zeros(32)
    for m in masks:
        for j in range(3):
            if m&(1<<j):continue
            sign=(-1)**((m&((1<<j)-1)).bit_count())
            n=m|(1<<j);d[4*n:4*n+4,4*m:4*m+4]=sign*minus[j]
    Qop=d+d.H
    So=s.zeros(32,16);Se=s.zeros(32,16)
    So[28:32,0:4]=s.eye(4)
    for j in range(3):So[4*(1<<j):4*(1<<j)+4,4+4*j:8+4*j]=s.eye(4)
    Se[0:4,0:4]=-s.eye(4)
    for j,(m,sg) in enumerate([(6,1),(5,-1),(3,1)]):Se[4*m:4*m+4,4+4*j:8+4*j]=sg*s.eye(4)
    ck('coefficient_A_skew_B_Hermitian',all(a.H==-a for a in avec) and all(b.H==b for b in bvec))
    ck('actual_connection_adjoint',all(minus[j].H==-plus[j] for j in range(3)))
    ck('component_maps_isometric',So.H*So==s.eye(16) and Se.H*Se==s.eye(16) and So.H*Se==s.zeros(16))
    ck('full_operator_intertwining',mz(Qop*So-Se*R))
    ck('full_adjoint_intertwining',mz(Qop*Se-So*R.H))
    ck('wrong_adjoint_operator_rejected',not mz(Qop*Se-So*R))
    ck('B_zero_order_not_discarded',any(not mz(b) for b in bvec))
    result={'facts':facts,'predicates_passed':sum(facts.values()),
        'normalizations':{'chi_kinetic':'-i/2','psi_kinetic':'-i/2','raw_gaugino':'-psi D_plus chi/2','bulk_gaugino':'chi D_plus psi/2','curl':'epsilon psi D_minus psi/4'},
        'map':{'left_Weyl':'odd: rho_1+lambda_3','conjugate':'even: -bar_lambda_0+star_bar_rho_2','canonical_rescaling':'chi=sqrt(2)lambda, psi=sqrt(2)rho'},
        'native_matrix_controls_not_global_PDE':True,'physical_operator_identified_conditionally':True,
        'physical_kernel_census_recomputed':False,'nonlinear_full_domain_closed':False,
        'boundary_selected':False,'nonauthor_analytic_review':False,'physical_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(facts.values()),[k for k,v in facts.items() if not v]
    return result

def dint_spin(a,j):return [dint(c,j) for c in a]

if __name__=='__main__':run()
