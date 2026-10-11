"""Canonical WZ recovery and full normal Ward control, not a full PDE."""
from functools import lru_cache
import json
import sympy as s
I=s.I;Q=s.Rational;N=4;Id=s.eye(N);Z=s.zeros(N)
x,z=s.symbols('x z',real=True)
ng=12;adj={0:2,1:3,2:0,3:1,4:6,5:7,6:4,7:5,8:10,9:11,10:8,11:9}
p=[2,3,5,7]
sig=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]

def mz(a):return all(s.expand(c)==0 for c in a)
def clean(a):return {u:c.applyfunc(s.expand) for u,c in a.items() if not mz(c)}
def add(*args):
    out={}
    for a in args:
        for u,c in a.items():out[u]=out.get(u,Z)+c
    return clean(out)
def scale(a,c):return clean({u:c*v for u,v in a.items()})
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if u&v:continue
            sw=0;w=u
            while w:
                bit=w&-w;sw+=(v&(bit-1)).bit_count();w-=bit
            out[u|v]=out.get(u|v,Z)+(-1)**sw*c*d
    return clean(out)
def gen(j,c=Id):return {1<<j:c}
def dag(a):
    out={}
    for u,c in a.items():
        term={0:c.H}
        for j in reversed(range(ng)):
            if u&(1<<j):term=mul(term,gen(adj[j]))
        out=add(out,term)
    return out
def left(a,j):return clean({u^(1<<j):(-1)**((u&((1<<j)-1)).bit_count())*c for u,c in a.items() if u&(1<<j)})
def ext(a,mu):return clean({u:p[mu]*c.diff(x) for u,c in a.items()})
def op(a,j,bar=False,supercharge=False):
    if not bar:
        sign=-1 if supercharge else 1
        return add(left(a,j),*(scale(mul(gen(b+2),ext(a,mu)),sign*I*sig[mu][j,b]) for mu in range(4) for b in range(2)))
    sign=1 if supercharge else -1
    return add(scale(left(a,j+2),-1),*(scale(mul(gen(k),ext(a,mu)),sign*I*sig[mu][k,j]) for mu in range(4) for k in range(2)))
def susy(a):return add(*(mul(gen(j+8),op(a,j,supercharge=True)) for j in range(2)),*(scale(mul(gen(j+10),op(a,j,bar=True,supercharge=True)),-1) for j in range(2)))
XX=[add(*(scale(mul(gen(a),gen(b+2)),sig[mu][a,b]) for a in range(2) for b in range(2))) for mu in range(4)]
def chiral(a):return add(a,*(scale(mul(XX[mu],ext(a,mu)),I) for mu in range(4)),*(scale(mul(XX[mu],mul(XX[nu],ext(ext(a,nu),mu))),Q(-1,2)) for mu in range(4) for nu in range(4)))
def pure(a):return {u:c for u,c in a.items() if u&15 in (1,2,3)}
def comp(a):return scale(chiral(pure(susy(a))),2*I)
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def exp2(v):return add({0:Id},scale(v,2),scale(mul(v,v),2))
def inv2(v):return add({0:Id},scale(v,-2),scale(mul(v,v),2))
def logvar(g,dg):
    u=add(g,{0:-Id})
    return scale(add(dg,scale(add(mul(dg,u),mul(u,dg)),Q(-1,2))),Q(1,2))
def normal_logvar(g,dg,gn,dgn):
    u=add(g,{0:-Id})
    return scale(add(dgn,scale(add(mul(dgn,u),mul(dg,gn),mul(gn,dg),mul(u,dgn)),Q(-1,2))),Q(1,2))
def eq(a,b):return not add(a,scale(b,-1))
def forbid(a):return {u:c for u,c in a.items() if u&15 in (0,1,2,3,4,8,12)}
def average(c):
    poly=s.Poly(s.expand(c),z)
    return s.expand(sum(v*(0 if n[0]%2 else s.binomial(n[0],n[0]//2)/2**n[0]) for n,v in poly.terms()))
KK=[s.kronecker_product(t,s.eye(2)) for t in sig[1:]]
def project(a):return clean({u:sum((average(s.trace(k*c))*k/s.trace(k*k) for k in KK),Z) for u,c in a.items()})

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v)
    KX,KY,KZ=KK
    S=s.kronecker_product(s.eye(2),sig[3]);T=s.kronecker_product(s.eye(2),sig[1])
    A=[(1+x)*KX+x*x*KY,KY+x*KZ,KZ+2*x*KX,KX+KY+x*KZ]
    cc=[gen(4,(1+x)*KX+I*KY),gen(5,KZ+I*(1+x)*KY)]
    th2={3:2*Id};bar2=dag(th2);top=mul(th2,bar2)
    fhalf=scale(mul(bar2,add(mul(gen(0),cc[0]),mul(gen(1),cc[1]))),1/s.sqrt(2))
    V=add(*(scale(mul(XX[mu],{0:A[mu]}),-1) for mu in range(4)),fhalf,dag(fhalf),scale(mul(top,{0:KX+x*KY}),Q(1,2)))
    G=exp2(V);Gi=inv2(V)
    ck('actual_WZ_reality',eq(dag(V),V))
    ck('nonzero_V_square_retained',bool(mul(V,V)) and not mul(mul(V,V),V))
    ck('exact_nonabelian_exponential_inverse',eq(mul(G,Gi),{0:Id}))
    ck('real_supertranslation',eq(dag(susy(V)),susy(V)))
    ck('even_supertranslation_product_rule',eq(susy(mul(V,V)),add(mul(susy(V),V),mul(V,susy(V)))))
    for a in range(2):
        for b in range(2):
            anti=add(op(op(V,b,bar=True,supercharge=True),a,supercharge=True),op(op(V,a,supercharge=True),b,bar=True,supercharge=True))
            rhs=add(*(scale(ext(V,mu),2*I*sig[mu][a,b]) for mu in range(4)))
            ck('Q_barQ_algebra_'+str(a)+str(b),eq(anti,rhs))
            ck('Q_barD_anticommutes_'+str(a)+str(b),not add(op(op(V,b,bar=True),a,supercharge=True),op(op(V,a,supercharge=True),b,bar=True)))
    L=comp(V);Ld=dag(L)
    dSG=susy(G);dG=add(dSG,scale(mul(G,L),I),scale(mul(Ld,G),-I))
    dv=logvar(G,dG)
    ck('uncompensated_WZ_slots_nonzero',bool(forbid(susy(V))))
    ck('compensator_chiral_zero_scalar',all(not op(L,j,bar=True) for j in range(2)) and all(u&15!=0 for u in L))
    ck('compensator_boundary_in_k',eq(project(L),L))
    ck('canonical_compensated_WZ_slots_zero',not forbid(dv))
    ck('full_exponential_linearization',eq(dG,add(scale(dv,2),scale(add(mul(V,dv),mul(dv,V)),2))))
    bad=logvar(G,add(dSG,scale(mul(G,L),-I),scale(mul(Ld,G),I)))
    ck('wrong_compensator_sign_rejected',bool(forbid(bad)))
    ck('abelian_deltaV_rule_rejected',not eq(dv,scale(dG,Q(1,2))))
    ck('abelian_rule_can_preserve_forbidden_slots',not forbid(scale(dG,Q(1,2))))
    # A residual real scalar gauge generates NONZERO admissible normal jets.
    lam=(1+x*x)*KX+(1+x)*s.kronecker_product(sig[1],sig[1])+x*s.kronecker_product(sig[2],sig[3])
    lc=chiral({0:lam});lb=dag(lc)
    normalG=add(scale(mul(G,lc),I),scale(mul(lb,G),-I))
    nv=logvar(G,normalG);normalL=comp(nv)
    Phi=add({0:T+I*S+I*z*KZ},lc);barPhi=dag(Phi)
    Zn=add(mul(Gi,normalG),scale(mul(mul(Gi,barPhi),G),I),scale(Phi,-I))
    ck('normal_WZ_jet_admitted',not forbid(nv) and bool(nv))
    ck('normal_compensator_jet_nonzero',bool(normalL) and bool(project(normalL)))
    ck('normal_Phi_is_chiral',all(not op(Phi,j,bar=True) for j in range(2)))
    ck('initial_integrated_response_zero',not project(Zn))
    ck('zero_mean_gauge_flux_not_pointwise_zero',bool(project({u:c.subs(z,1) for u,c in Zn.items()})))
    ck('nonzero_structure_flux_retained',Zn.get(0,Z).subs(z,0)==2*S)
    ck('nonlinear_normal_response_present',any(u&15!=0 for u in Zn))
    # Complete compensated transformations with genuine normal Lambda jets.
    dnDG=add(susy(normalG),scale(mul(normalG,L),I),scale(mul(G,normalL),I),scale(mul(dag(normalL),G),-I),scale(mul(Ld,normalG),-I))
    dPhi=add(susy(Phi),scale(comm(Phi,L),I),normalL)
    dBar=dag(dPhi);dGi=scale(mul(mul(Gi,dG),Gi),-1)
    dZn=add(mul(dGi,normalG),mul(Gi,dnDG),scale(mul(mul(dGi,barPhi),G),I),scale(mul(mul(Gi,dBar),G),I),scale(mul(mul(Gi,barPhi),dG),I),scale(dPhi,-I))
    ward=add(susy(Zn),scale(comm(Zn,L),I))
    ck('full_normal_compensated_Ward_identity',eq(dZn,ward))
    ck('normal_WZ_recovery',not forbid(normal_logvar(G,dG,normalG,dnDG)))
    ck('every_projected_response_slot_preserved',not project(dZn))
    ck('fixed_projection_commutes_with_SUSY',eq(project(susy(Zn)),susy(project(Zn))))
    ck('fixed_projection_equivariant',eq(project(comm(Zn,L)),comm(project(Zn),L)))
    # Delete ONLY the normal compensator jets; keep all other transformations.
    frozenDN=add(susy(normalG),scale(mul(normalG,L),I),scale(mul(Ld,normalG),-I))
    frozenP=add(susy(Phi),scale(comm(Phi,L),I));frozenBar=dag(frozenP)
    frozenZ=add(mul(dGi,normalG),mul(Gi,frozenDN),scale(mul(mul(dGi,barPhi),G),I),scale(mul(mul(Gi,frozenBar),G),I),scale(mul(mul(Gi,barPhi),dG),I),scale(frozenP,-I))
    ck('consistent_jet_omission_is_Ward_blind',eq(frozenZ,ward) and not project(frozenZ))
    ck('frozen_compensator_normal_WZ_rejected',bool(forbid(normal_logvar(G,dG,normalG,frozenDN))))
    # An INCONSISTENT omission in Phi alone really does break the Ward law.
    inconsistentZ=add(mul(dGi,normalG),mul(Gi,dnDG),scale(mul(mul(dGi,barPhi),G),I),scale(mul(mul(Gi,frozenBar),G),I),scale(mul(mul(Gi,barPhi),dG),I),scale(frozenP,-I))
    ck('inconsistent_jet_omission_Ward_rejected',not eq(inconsistentZ,ward))
    ck('inconsistent_jet_omission_projection_rejected',bool(project(inconsistentZ)))
    varying=lambda a:scale(project(a),x)
    ck('external_dependent_projection_rejected',not eq(varying(susy(V)),susy(varying(V))))
    ck('averaging_does_not_discard_squared_flux',average(z)==0 and average(z*z)==Q(1,2))
    # Actual diagonal-twist scalar map, not only a dimension match.
    e=s.Matrix([0,1,-1,0])/s.sqrt(2)
    J=[(s.kronecker_product(t,s.eye(2))+s.kronecker_product(s.eye(2),t))/2 for t in sig[1:]]
    Cas=sum((j*j for j in J),s.zeros(4));Ps=e*e.H;Pt=s.eye(4)-Ps
    ck('explicit_twist_singlet_and_norm',e.H*e==s.ones(1) and all(j*e==s.zeros(4,1) for j in J))
    ck('explicit_twist_triplet_complement',Cas==2*Pt and Ps.rank()==1 and Pt.rank()==3)
    wrong=[(s.kronecker_product(t,s.eye(2))-s.kronecker_product(s.eye(2),t))/2 for t in sig[1:]]
    ck('wrong_diagonal_twist_rejected',any(j*e!=s.zeros(4,1) for j in wrong))
    result={'facts':facts,'predicates_passed':sum(facts.values()),
      'off_shell_superfield_boundary_covariance':all(facts.values()),'normal_compensator_jets_retained':True,
      'twist_supplied_not_generated':True,'full_E8_structure_constants_recomputed':False,
      'well_posed_multiplet_boundary_proved':False,'physical_kernel_recomputed':False,
      'nonauthor_analytic_review':False,'boundary_selected':False,'full_goal_achieved':False}
    print(json.dumps(result,indent=2,sort_keys=True))
    assert all(facts.values()),[k for k,v in facts.items() if not v]
    return result

if __name__=='__main__':run()
