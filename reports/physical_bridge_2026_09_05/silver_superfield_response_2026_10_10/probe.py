"""Exact surface/linear-slot controls. Not a physical spectrum certificate."""
from functools import lru_cache
import json
import sympy as s

I=s.I

def clean(a):
    return {w:s.expand(c) for w,c in a.items() if s.expand(c)!=0}

def add(*args):
    out={}
    for a in args:
        for w,c in a.items():out[w]=out.get(w,0)+c
    return clean(out)

def scale(a,c):return clean({w:c*v for w,v in a.items()})
def word(x):return {(x,):s.Integer(1)}
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():out[u+v]=out.get(u+v,0)+c*d
    return clean(out)
def bracket(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def trace_words(a):
    out={}
    for w,c in a.items():
        key=min(w[i:]+w[:i] for i in range(len(w))) if w else ()
        out[key]=out.get(key,0)+c
    return clean(out)

# Exterior algebra includes fermion fields, not just four superspace generators.
# t1,t2,b1,b2,psi1,psi2,barpsi1,barpsi2,chi1n,chi2n,barchi1n,barchi2n.
DAG=(2,3,0,1,6,7,4,5,10,11,8,9)
def odd(j):return {1<<j:s.Integer(1)}
def gmul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if u&v:continue
            swaps=sum((v&((1<<j)-1)).bit_count() for j in range(12) if u&(1<<j))
            key=u|v;out[key]=out.get(key,0)+(-1)**swaps*c*d
    return clean(out)
def dagger(a):
    out={}
    for mask,c in a.items():
        term={0:s.conjugate(c)}
        for j in reversed(range(12)):
            if mask&(1<<j):term=gmul(term,odd(DAG[j]))
        out=add(out,term)
    return out
def chain(*args):
    out={0:s.Integer(1)}
    for a in args:out=gmul(out,a)
    return out
def suppress(a,indices):
    kill=sum(1<<j for j in indices)
    return {u:c for u,c in a.items() if not u&kill}

@lru_cache(None)
def components():
    t1,t2,b1,b2=(odd(j) for j in range(4))
    q=s.symbols('q0:4',real=True)
    an=s.symbols('An0:4',real=True)
    a,B,fr,fi,dn=s.symbols('a B fr fi Dn',real=True)
    sig=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    def mixed(coeff):
        return add(*(scale(gmul(odd(i),odd(j+2)),sum(coeff[m]*sig[m][i,j] for m in range(4)))
                     for i in range(2) for j in range(2)))
    x=mixed(q)
    base=add({0:a+I*B},gmul(t1,odd(4)),gmul(t2,odd(5)),scale(gmul(t1,t2),fr+I*fi))
    shift=add({0:s.Integer(1)},scale(x,I),scale(gmul(x,x),s.Rational(-1,2)))
    phi=gmul(shift,base)
    gc=add(chain(t1,t2,b1,odd(10)),chain(t1,t2,b2,odd(11)))
    jet=add(scale(mixed(an),-1),gc,dagger(gc),scale(chain(t1,t2,b1,b2),dn/2))
    z=add(scale(jet,2),scale(add(dagger(phi),scale(phi,-1)),I))
    return z,jet,phi,x,q,an,(a,B,fr,fi,dn)

def zmatrix(g,gn,p):return g.inv()*gn+I*g.inv()*p.H*g-I*p

@lru_cache(None)
def run():
    facts={}
    A,C,P,e,de,T,dP=(word(x) for x in ('A','C','Phi','eta','deta','Ginv_dbarPhi_G','dPhi'))
    z=add(A,scale(C,I),scale(P,-I))
    direct=add(de,bracket(A,e),scale(bracket(C,e),I),scale(T,I),scale(dP,-I))
    proposed=add(de,scale(bracket(P,e),I),bracket(z,e),scale(T,I),scale(dP,-I))
    facts['universal_nonlinear_variation']=direct==proposed
    facts['missing_Phi_commutator_rejected']=direct!=add(proposed,scale(bracket(P,e),-I))
    facts['cyclic_Z_commutator_zero']=trace_words(mul(z,bracket(z,e)))=={}
    facts['other_bulk_commutator_not_zero']=trace_words(mul(z,bracket(P,e)))!={}

    # Positive Hermitian G, noncommuting Hermitian jets and complex Phi.
    g=s.Matrix([[2,1],[1,1]])
    gn=s.Matrix([[1,2+I],[2-I,-1]])
    dg=s.Matrix([[3,1-I],[1+I,-2]])
    dgn=s.Matrix([[2,3-I],[3+I,1]])
    p=s.Matrix([[1+I,2-I],[3+2*I,-1-I]])
    dp=s.Matrix([[I,1+I],[-2,-I]])
    eta=g.inv()*dg
    deta=-g.inv()*gn*eta+g.inv()*dgn
    zz=zmatrix(g,gn,p)
    direct_m=-eta*g.inv()*gn+g.inv()*dgn+I*(-eta*g.inv()*p.H*g+g.inv()*dp.H*g+g.inv()*p.H*dg)-I*dp
    pred=deta+I*(p*eta-eta*p)+zz*eta-eta*zz+I*g.inv()*dp.H*g-I*dp
    zero=lambda m:all(s.expand(v)==0 for v in m)
    facts['matrix_nonlinear_variation']=zero(direct_m-pred)
    facts['twisted_Z_reality']=zero(zz.H-g*zz*g.inv())
    facts['real_eta_twisted_reality']=zero(eta.H-g*eta*g.inv())
    facts['surface_pair_real']=s.simplify(s.trace(zz*eta)-s.conjugate(s.trace(zz*eta)))==0
    root=s.diag(2,s.Rational(1,2));gg=root**2
    h=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    zreal=[root.inv()*v*root for v in h]
    etareal=[root.inv()*v*root for v in h]
    pairing=s.Matrix(3,3,lambda i,j:s.trace(zreal[i]*etareal[j]))
    facts['real_pairing_nondegenerate']=pairing==2*s.eye(3) and pairing.det()==8
    facts['variations_are_real']=all(zero((gg*v).H-gg*v) for v in etareal)

    # Arbitrary nonzero normal g-jet cancels; boundary value alone is restricted.
    u=s.Matrix([[1,1],[0,1]]);un=s.Matrix([[1,2-I],[3+I,-2]])
    gp=u.H*g*u
    gpn=un.H*g*u+u.H*gn*u+u.H*g*un
    pp=u.inv()*p*u-I*u.inv()*un
    facts['normal_gauge_jet_cancels']=zero(zmatrix(gp,gpn,pp)-u.inv()*zz*u)
    facts['normal_gauge_jet_is_nonzero']=un!=s.zeros(2) and not zero(pp-u.inv()*p*u)
    facts['freezing_transformed_normal_vector_jet_fails']=not zero(zmatrix(gp,u.H*gn*u,pp)-u.inv()*zz*u)

    x=s.symbols('x',real=True)
    facts['integrated_not_pointwise']=s.integrate(s.cos(x),(x,0,2*s.pi))==0 and s.cos(x).subs(x,0)==1
    facts['constant_gauge_flux_rejected']=s.integrate(s.Integer(1),(x,0,2*s.pi))==2*s.pi
    facts['tangential_total_derivative_projects_zero']=s.integrate(s.diff(s.sin(x),x),(x,0,2*s.pi))==0

    zc,jet,phi,xx,q,an,fields=components()
    a,B,fr,fi,dn=fields
    facts['all_superspace_slots_present']=set(u&15 for u in zc)==set(range(16))
    facts['full_linear_response_real']=dagger(zc)==zc
    facts['chiral_actual_conjugate']=dagger(dagger(phi))==phi
    facts['odd_product_opposing_control']=gmul(odd(0),odd(4))==scale(gmul(odd(4),odd(0)),-1)
    facts['lowest_normal_scalar']=zc[0]==2*B
    noferm=suppress(zc,range(4,12))
    expected_vector=add(*(scale(gmul(odd(i),odd(j+2)),
                       -2*sum((an[m]-q[m]*a)*[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)][m][i,j] for m in range(4)))
                       for i in range(2) for j in range(2)))
    facts['mixed_gauge_normal_response']={u:c for u,c in noferm.items() if u in (5,6,9,10)}==expected_vector
    facts['normal_auxiliary_slots']=noferm[3]==fi-I*fr and noferm[12]==-fi-I*fr
    box=q[0]**2-q[1]**2-q[2]**2-q[3]**2
    facts['highest_normal_auxiliary_jet']=s.expand(noferm[15]-dn-2*box*B)==0
    no_psi=suppress(zc,range(4,8))
    chi_terms={u:c for u,c in no_psi.items() if u>>8}
    expected_chi={u:c for u,c in scale(jet,2).items() if u>>8}
    facts['secondary_chi_jets_after_primary']=chi_terms==expected_chi and len(chi_terms)==4
    facts['primary_trace_not_whole_offshell_law']=chi_terms!={}
    facts['zero_normal_chi_jets_remove_secondary']=not {u:c for u,c in suppress(no_psi,range(8,12)).items() if u>>4}

    # For each two-component Weyl chirality: psi normal zero, plus its normal
    # equation. Curl has zero integrated k projection by Stokes, not by a fit.
    primary=s.Matrix([[0,0,1,0],[0,0,0,1]])
    eom=s.Matrix([[1,0,q[0]+q[3],q[1]-I*q[2]],
                  [0,1,q[1]+I*q[2],q[0]-q[3]]])
    secondary=s.Matrix([[1,0,0,0],[0,1,0,0]])
    facts['secondary_redundant_on_linear_solutions']=primary.col_join(eom).rank()==primary.col_join(eom).col_join(secondary).rank()==4
    facts['secondary_independent_offshell']=primary.rank()==2 and primary.col_join(secondary).rank()==4

    # All 24 gauge sl5 generators, not a single scalar dimensional analogy.
    e5=s.eye(5);kb=[]
    for i in range(5):
        for j in range(5):
            if i!=j:
                m=s.zeros(5);m[i,j]=1;kb.append(m)
    for i in range(4):
        m=s.zeros(5);m[i,i]=1;m[4,4]=-1;kb.append(m)
    structures=[s.diag(1,-1,0,0,0),s.Matrix(5,5,lambda i,j:1 if (i,j)==(0,4) else 0)]
    facts['all_24_gauge_generators_tracefree']=len(kb)==24 and all(s.trace(v)==0 for v in kb)
    facts['commuting_factor_background_response']=all(
        zero(s.kronecker_product(st,e5)*s.kronecker_product(e5,k)-s.kronecker_product(e5,k)*s.kronecker_product(st,e5))
        and s.trace(s.kronecker_product(st,k))==0 for st in structures for k in kb)
    facts['nonzero_structure_flux_retained']=s.trace(structures[0]**2)>0
    facts['gauge_flux_opposing_control']=s.trace(kb[-1]**2)==2
    out={'facts':facts,'predicates_passed':sum(facts.values()),
         'component_polynomial':{str(u):str(s.expand(c)) for u,c in sorted(zc.items())},
         'superspace_slots':16,'gauge_generators':24,
         'coefficient_recomputed':False,'full_E8_structure_constants_recomputed':False,
         'nonlinear_component_domain_completed':False,'quadratic_energy_derived':False,
         'physical_kernel_computed':False,'boundary_selected':False,
         'nonauthor_analytic_review':False,'physical_goal_achieved':False}
    assert all(facts.values()),[k for k,v in facts.items() if not v]
    return out

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
