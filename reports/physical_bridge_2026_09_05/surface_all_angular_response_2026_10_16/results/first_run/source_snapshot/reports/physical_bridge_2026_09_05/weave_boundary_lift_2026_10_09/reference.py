"""Separate exterior Clifford construction and Cauchy-space intersection test."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
I=s.I
def clifford():
    # Creation/contraction on exterior algebra of C^2; no native import.
    creators=[]
    for bit in (0,1):
        a=s.zeros(4)
        for mask in range(4):
            if not mask & (1<<bit):
                a[mask|(1<<bit),mask]=(-1)**sum((mask>>j)&1 for j in range(bit))
        creators.append(a)
    gam=[]
    for a in creators:gam.extend([a+a.T,I*(a-a.T)])
    # Chirality anticommutes with every generator.
    g5=s.diag(1,-1,-1,1)
    return gam,g5
zero=lambda A:all(s.simplify(v)==0 for v in A)
@lru_cache(None)
def run():
    facts={};gam,g5=clifford();R=s.diag(1,1,-1,-1)
    facts['independent_clifford_algebra']=all(zero(a*b+b*a-(2*s.eye(4) if i==j else s.zeros(4))) for i,a in enumerate(gam) for j,b in enumerate(gam)) and all(zero(g5*a+a*g5) for a in gam)
    theta=s.symbols('theta',real=True)
    # Direct column assembly of the four-slot pairing.
    z=s.exp(I*theta/2)
    S=s.Matrix([[0,0,I*z,0],[0,0,0,I/z],[-I/z,0,0,0],[0,-I*z,0,0]])
    V=s.Matrix([[0,I,0,0],[-I,0,0,0],[0,0,0,I],[0,0,-I,0]])
    facts['bundle_transition_and_duality']=zero(S.subs(theta,theta+2*s.pi)-R*S*R) and zero(V*S.conjugate()*V+S)
    facts['unitary_slot_graph']=zero(S*S-s.eye(4)) and zero(S-S.adjoint())
    sig=s.kronecker_product(g5,S.subs(theta,0));full=s.eye(16)
    ranks=[];good=True
    for pp,rr in [((0,0,0,0),1),((0,0,0,0),-1),((1,2,2,0),4),((1,0,0,0),0)]:
        d=sum((I*a*v for a,v in zip(gam,pp)),s.zeros(4))
        rho=s.sqrt(sum(v*v for v in pp)+rr*rr)
        for adj in (False,True):
            H=s.kronecker_product(g5*d,s.eye(4))+(1 if adj else -1)*rr*s.kronecker_product(g5,R)
            allowed=(sig+(full if adj else -full)).nullspace()
            decaying=(H+rho*full).nullspace()
            union=s.Matrix.hstack(*(allowed+decaying));rank=union.rank();ranks.append(rank)
            good &= len(allowed)==8 and len(decaying)==8 and union.det()!=0
    facts['independent_cauchy_spaces_are_complementary']=good
    bad=s.kronecker_product(g5,s.diag(1,-1,1,-1))
    old_allowed=(bad-full).nullspace()
    H=-s.kronecker_product(g5,R);decay=(H+full).nullspace()
    facts['old_angular_intersection_is_nonzero']=s.Matrix.hstack(*(old_allowed+decay)).rank()<16
    # Direct action on y^a after physical kinetic-density rescalings.
    y=s.symbols('y',positive=True);k=s.symbols('k',real=True)
    residuals=[]
    for power in (0,1,2,-1):
        f=y**power
        dz=lambda v:-I*s.diff(v,y)+I*k*v/y
        L=I*s.sqrt(y)*dz(s.sqrt(y)*f)
        A=I*y**s.Rational(3,2)*dz(f/s.sqrt(y))
        if power==0:reference_signs=[int(s.sign(s.simplify(v).subs(k,0))) for v in (L,A)]
        residuals.extend([s.simplify(L-(power+s.Rational(1,2)-k)*f),
                          s.simplify(A-(power-s.Rational(1,2)-k)*f)])
    facts['independent_density_drift_action']=all(v==0 for v in residuals)
    path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
    sp=importlib.util.spec_from_file_location('boundary_tensor',path)
    old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
    rows=[(key,v) for key,v in old.tensor_weights().items() if abs(key[3])==5]
    facts['independent_charged_witness_population']=sum(v for key,v in rows)==12 and all(key[4]==0 for key,v in rows)
    vector=s.eye(4)[:,0]
    facts['new_condition_changes_old_horizontal_data']=not zero(S*vector-vector) and zero(R*S*vector+S*vector)
    facts['relative_phase_and_constant_seam_mutants']=not zero(V*S.subs(theta,0).conjugate()*V-S.subs(theta,0)) and not zero(S.subs(theta,0)-R*S.subs(theta,0)*R)
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
      'full_symbol_ranks':ranks,'j0_reference_signs':reference_signs,
      'charged_witness_weights':int(sum(v for key,v in rows)),
      'nonauthor_acceptance':False}
if __name__=='__main__':
    d=run();print(json.dumps(d,indent=2,sort_keys=True));raise SystemExit(0 if all(d['predicates'].values()) else 1)
