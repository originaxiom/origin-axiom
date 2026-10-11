"""Tuple exterior, exponential inverse variation and eta response.

Separate algorithm, same author; no native import or outside acceptance.
"""
from functools import lru_cache
import itertools
import json
import sympy as s
I=s.I;Q=s.Rational;Id=s.eye(4);Zero=s.zeros(4)
x,y=s.symbols('x y',real=True)
order=['t1','t2','b1','b2','c1','c2','C1','C2','e1','e2','E1','E2'];rk={n:j for j,n in enumerate(order)}
dual=dict(zip(order,['b1','b2','t1','t2','C1','C2','c1','c2','E1','E2','e1','e2']))
sig=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]

def clean(a):return {k:v.applyfunc(s.expand) for k,v in a.items() if any(s.expand(c)!=0 for c in v)}
def add(*args):
    z={}
    for a in args:
        for k,v in a.items():z[k]=z.get(k,Zero)+v
    return clean(z)
def times(a,c):return clean({k:c*v for k,v in a.items()})
def mon(seq,c):
    if len(seq)!=len(set(seq)):return {}
    return {tuple(sorted(seq,key=rk.get)):(-1)**sum(rk[seq[a]]>rk[seq[b]] for a in range(len(seq)) for b in range(a+1,len(seq)))*c}
def prod(a,b):return add(*(mon(k+l,v*w) for k,v in a.items() for l,w in b.items()))
def term(n,c=Id):return {(n,):c}
def dagger(a):return add(*(mon(tuple(dual[n] for n in reversed(k)),v.H) for k,v in a.items()))
def left(a,n):return clean({k[:j]+k[j+1:]:(-1)**j*v for k,v in a.items() for j in range(len(k)) if k[j]==n})
def dx(a):return clean({k:v.diff(x) for k,v in a.items()})
def sq(a,j,bar=False):
    if bar:return add(times(left(a,'b'+str(j+1)),-1),times(prod(term('t'+str(j+1)),dx(a)),I))
    return add(left(a,'t'+str(j+1)),times(prod(term('b'+str(j+1)),dx(a)),-I))
def bd(a,j):return add(times(left(a,'b'+str(j+1)),-1),times(prod(term('t'+str(j+1)),dx(a)),-I))
def ss(a):return add(*(prod(term('e'+str(j+1)),sq(a,j)) for j in range(2)),*(times(prod(term('E'+str(j+1)),sq(a,j,True)),-1) for j in range(2)))
X=add(prod(term('t1'),term('b1')),prod(term('t2'),term('b2')))
def shift(a):return add(a,times(prod(X,dx(a)),I),times(prod(X,prod(X,dx(dx(a)))),Q(-1,2)))
def forbidden(a):return {k:v for k,v in a.items() if not any(n.startswith('t') for n in k) or not any(n.startswith('b') for n in k)}
def puretheta(a):return {k:v for k,v in a.items() if any(n.startswith('t') for n in k) and not any(n.startswith('b') for n in k)}
def comm(a,b):return add(prod(a,b),times(prod(b,a),-1))
def invexpvariation(v,dg):return times(add(dg,times(add(prod(v,dg),prod(dg,v)),-1)),Q(1,2))
def d_invexpvariation(v,dg,vn,dgn):return times(add(dgn,times(add(prod(vn,dg),prod(v,dgn),prod(dgn,v),prod(dg,vn)),-1)),Q(1,2))
def eq(a,b):return not add(a,times(b,-1))
K=[s.kronecker_product(t,s.eye(2)) for t in sig[1:]]
@lru_cache(None)
def mean(c):return s.expand(s.integrate(s.expand(c),(y,0,2*s.pi))/(2*s.pi))
def project(a):return clean({k:sum((mean(s.trace(t*v))*t/s.trace(t*t) for t in K),Zero) for k,v in a.items()})

@lru_cache(None)
def run():
    checks={}
    def ck(k,v):checks[k]=bool(v)
    A=[(1+x*x)*K[2],K[0]+x*K[1],2*K[1]+x*K[2],K[2]+x*K[0]]
    t2={('t1','t2'):2*Id};b2=dagger(t2)
    chi=[term('c1',K[1]+I*(1+x)*K[2]),term('c2',x*K[0]+I*K[1])]
    vh=times(prod(b2,add(prod(term('t1'),chi[0]),prod(term('t2'),chi[1]))),1/s.sqrt(2))
    V=add(*(times(prod(add(*(times(prod(term('t'+str(a+1)),term('b'+str(b+1))),sig[mu][a,b]) for a in range(2) for b in range(2))),{():A[mu]}),-1) for mu in range(4)),vh,dagger(vh),times(prod(prod(t2,b2),{():K[1]+x*K[0]}),Q(1,2)))
    G=add({():Id},times(V,2),times(prod(V,V),2));Gi=add({():Id},times(V,-2),times(prod(V,V),2))
    # Solve forbidden delta-G slots, not the native's delta-V construction.
    L=times(shift(puretheta(ss(G))),I);Lb=dagger(L)
    DG=add(ss(G),times(prod(G,L),I),times(prod(Lb,G),-I))
    DV=invexpvariation(V,DG)
    ck('tuple_real_vector_and_inverse',eq(V,dagger(V)) and eq(prod(G,Gi),{():Id}))
    ck('tuple_nonzero_nonlinearity',bool(prod(V,V)) and not prod(prod(V,V),V))
    ck('tuple_chiral_compensator',all(not bd(L,j) for j in range(2)))
    ck('tuple_forbidden_slots_recovered',bool(forbidden(ss(V))) and not forbidden(DV))
    ck('tuple_inverse_exponential_not_abelian',eq(DG,add(times(DV,2),times(add(prod(V,DV),prod(DV,V)),2))) and not eq(DV,times(DG,Q(1,2))))
    ck('tuple_abelian_variation_forbidden_slots_blind',not forbidden(times(DG,Q(1,2))))
    ck('tuple_compensator_stays_in_gauge_factor',eq(project(L),L))
    bad=invexpvariation(V,add(ss(G),times(prod(G,L),-I),times(prod(Lb,G),I)))
    ck('tuple_wrong_sign_rejected',bool(forbidden(bad)))
    lam=(1+x*x)*K[1]+(2+x)*s.kronecker_product(sig[3],sig[1])+x*s.kronecker_product(sig[2],sig[2])
    lc=shift({():lam});lb=dagger(lc)
    Gn=add(times(prod(G,lc),I),times(prod(lb,G),-I));Vn=invexpvariation(V,Gn)
    # Different slot-based normal compensation from derivative of delta G.
    Gsn=ss(Gn);Ln=times(shift(puretheta(Gsn)),I)
    Struct=s.kronecker_product(s.eye(2),sig[2])
    Phi=add({():I*Struct+I*s.cos(y)*K[0]},lc);bar=dagger(Phi)
    ZZ=add(prod(Gi,Gn),times(prod(prod(Gi,bar),G),I),times(Phi,-I))
    dGn=add(Gsn,times(prod(Gn,L),I),times(prod(G,Ln),I),times(prod(dagger(Ln),G),-I),times(prod(Lb,Gn),-I))
    dP=add(ss(Phi),times(comm(Phi,L),I),Ln)
    # eta response is NOT the native's direct inverse/product variation.
    eta=prod(Gi,DG);eta_n=add(times(prod(prod(prod(Gi,Gn),Gi),DG),-1),prod(Gi,dGn))
    dZ=add(eta_n,times(comm(Phi,eta),I),comm(ZZ,eta),times(prod(prod(Gi,dagger(dP)),G),I),times(dP,-I))
    want=add(ss(ZZ),times(comm(ZZ,L),I))
    ck('tuple_full_eta_response_Ward',eq(dZ,want))
    ck('tuple_integrated_entire_response',not project(ZZ) and not project(dZ))
    ck('tuple_pointwise_flux_would_change_law',bool(project({k:v.subs(y,0) for k,v in ZZ.items()})))
    ck('tuple_nonzero_structure_flux',ZZ.get((),Zero).subs(y,s.pi/2)==2*Struct)
    ck('tuple_normal_WZ_recovered',not forbidden(d_invexpvariation(V,DG,Vn,dGn)))
    ck('tuple_nonzero_normal_compensation',bool(Ln) and bool(project(Ln)))
    frozenGN=add(Gsn,times(prod(Gn,L),I),times(prod(Lb,Gn),-I))
    fp=add(ss(Phi),times(comm(Phi,L),I))
    fe_n=add(times(prod(prod(prod(Gi,Gn),Gi),DG),-1),prod(Gi,frozenGN))
    fz=add(fe_n,times(comm(Phi,eta),I),comm(ZZ,eta),times(prod(prod(Gi,dagger(fp)),G),I),times(fp,-I))
    ck('tuple_consistent_omission_Ward_blind',eq(fz,want) and not project(fz))
    ck('tuple_frozen_normal_WZ_rejected',bool(forbidden(d_invexpvariation(V,DG,Vn,frozenGN))))
    iz=add(eta_n,times(comm(Phi,eta),I),comm(ZZ,eta),times(prod(prod(Gi,dagger(fp)),G),I),times(fp,-I))
    ck('tuple_inconsistent_omission_rejected',not eq(iz,want) and bool(project(iz)))
    ck('tuple_external_dependent_projector_rejected',not eq(times(project(ss(V)),x),ss(times(project(V),x))))
    ck('tuple_genuine_averaging',mean(s.cos(y))==0 and mean(s.cos(y)**2)==Q(1,2))
    # Independent operator-matrix check for ALL four external covectors.
    masks=list(range(16));E=[];C=[]
    for j in range(4):
        e=s.zeros(16);c=s.zeros(16)
        for m in masks:
            sg=(-1)**sum(bool(m&(1<<k)) for k in range(j))
            if m&(1<<j):c[m^(1<<j),m]=sg
            else:e[m|(1<<j),m]=sg
        E.append(e);C.append(c)
    q=s.symbols('q0:4',real=True)
    QQ=[C[a]-I*sum((sig[mu][a,b]*q[mu]*E[b+2] for mu in range(4) for b in range(2)),s.zeros(16)) for a in range(2)]
    BQ=[-C[b+2]+I*sum((sig[mu][a,b]*q[mu]*E[a] for mu in range(4) for a in range(2)),s.zeros(16)) for b in range(2)]
    BD=[-C[b+2]-I*sum((sig[mu][a,b]*q[mu]*E[a] for mu in range(4) for a in range(2)),s.zeros(16)) for b in range(2)]
    ck('operator_Q_algebra_all_covectors',all((QQ[a]*BQ[b]+BQ[b]*QQ[a]-2*I*sum(sig[mu][a,b]*q[mu] for mu in range(4))*s.eye(16)).applyfunc(s.expand)==s.zeros(16) for a in range(2) for b in range(2)))
    ck('operator_Q_barD_all_covectors',all((QQ[a]*BD[b]+BD[b]*QQ[a]).applyfunc(s.expand)==s.zeros(16) for a in range(2) for b in range(2)))
    ck('operator_same_chirality_algebra',all((QQ[a]*QQ[b]+QQ[b]*QQ[a]).applyfunc(s.expand)==s.zeros(16) and (BQ[a]*BQ[b]+BQ[b]*BQ[a]).applyfunc(s.expand)==s.zeros(16) for a in range(2) for b in range(2)))
    u=s.symbols('u',nonzero=True)
    ck('twist_character_split',s.expand((u+1/u)**2-(1+(u*u+1+1/(u*u))))==0)
    eps=s.Matrix([[0,1],[-1,0]])
    ck('twist_singlet_tensor_action',all(t*eps+eps*t.T==s.zeros(2) for t in sig[1:]))
    ck('non_singlet_control_rejected',any(t*s.eye(2)+s.eye(2)*t.T!=s.zeros(2) for t in sig[1:]))
    result={'predicates':checks,'predicates_passed':sum(checks.values()),'native_imported':False,
        'off_shell_superfield_covariance':all(checks.values()),'outside_review':False,'well_posed_multiplet_proved':False,
        'physical_census_recomputed':False,'generated_selection':False,'full_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return result

if __name__=='__main__':run()
