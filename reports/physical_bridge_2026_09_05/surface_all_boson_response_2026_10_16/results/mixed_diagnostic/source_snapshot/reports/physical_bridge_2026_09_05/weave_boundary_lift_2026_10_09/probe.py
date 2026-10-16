"""Actual full angular symbol, unchanged-reference witness and local comparator."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
BASE=Path(__file__).resolve().parent.parent
def load(folder,name):
    sp=importlib.util.spec_from_file_location(name,BASE/folder/'probe.py')
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
physical=load('weave_physical_mass_2026_10_08','boundary_physical')
end=load('weave_cusp_anomaly_2026_10_08','boundary_end')
zero=lambda A:all(s.simplify(z)==0 for z in A)
I=s.I
R=s.diag(1,1,-1,-1);J=-I*R
P=s.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]])
def sigma(theta):
    B=I*s.diag(s.exp(I*theta/2),s.exp(-I*theta/2))
    return s.BlockMatrix([[s.zeros(2),B],[B.adjoint(),s.zeros(2)]]).as_explicit()
def clifford():
    pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    gam=[s.kronecker_product(pa[0],a) for a in pa]+[s.kronecker_product(pa[1],s.eye(2))]
    return gam,s.kronecker_product(pa[2],s.eye(2))
@lru_cache(None)
def run():
    facts={};x,y=s.symbols('x y',real=True)
    h=s.diag(1,1/s.sqrt(2),1,1);q=s.zeros(1)
    M=P*h*physical.mass(q,q,I*x-y,1)*h.inv()
    facts['principal_from_actual_mass_and_metric']=zero(M-I*x*s.eye(4)-I*y*J)
    K=J.adjoint();V=K*P
    facts['normal_target_phase_and_reality_map']=zero(K*K.adjoint()-s.eye(4)) and zero(V.adjoint()-V) and zero(V*V-s.eye(4)) and zero(V.conjugate()+V)
    gam,g5=clifford();mom=s.symbols('p0:4',real=True);r,pt=s.symbols('r pt',real=True)
    D4=sum((I*g*p for g,p in zip(gam,mom)),s.zeros(4))
    H4=s.kronecker_product(g5*D4,s.eye(4));H=H4-r*s.kronecker_product(g5,R)
    Ha=H4+r*s.kronecker_product(g5,R);G5=s.kronecker_product(g5,s.eye(4))
    norm=sum(p*p for p in mom)+r*r
    facts['full_symbol_hermitian_and_norm']=zero(H-H.adjoint()) and zero(H*H-norm*s.eye(16))
    normal=I*pt*s.eye(4)+I*r*K
    block=s.BlockMatrix([[s.kronecker_product(s.eye(2),normal),s.kronecker_product(D4[:2,2:],s.eye(4))],
      [s.kronecker_product(D4[2:,:2],s.eye(4)),s.kronecker_product(s.eye(2),normal.adjoint())]]).as_explicit()
    facts['four_weyl_packaging_matches_full_operator']=zero(block-G5*(I*pt*s.eye(16)+H))
    th=s.symbols('theta',real=True);S=sigma(th);B=s.kronecker_product(g5,S)
    facts['local_projector_hermitian_involution']=zero(S-S.adjoint()) and zero(S*S-s.eye(4)) and s.trace(B)==0
    facts['all_covectors_operator_and_adjoint_complement']=zero(B*H+H*B) and zero(B*Ha+Ha*B)
    plus=(s.eye(16)+B)/2;minus=s.eye(16)-plus
    facts['adjoint_green_pairing']=zero(plus*G5*minus)
    flux=s.kronecker_product(gam[0]*g5,s.eye(4))
    facts['lorentz_current_vanishes']=zero(plus*flux*plus)
    facts['spin_seam_descends']=zero(sigma(th+2*s.pi)-R*S*R)
    facts['actual_conjugate_fields_compatible']=zero(V*S.conjugate()*V+S)
    const=sigma(0)
    facts['constant_mixing_fails_seam']=not zero(const-R*const*R)
    wrong=s.BlockMatrix([[s.zeros(2),s.exp(I*th/2)*s.eye(2)],[s.exp(-I*th/2)*s.eye(2),s.zeros(2)]]).as_explicit()
    facts['scalar_phase_fails_reality']=not zero(V*wrong.conjugate()*V+wrong)
    A=s.Matrix(3,3,s.symbols('a0:9'));SG=s.kronecker_product(S,s.eye(3));GG=s.kronecker_product(s.eye(4),A)
    facts['arbitrary_gauge_action_commutes']=zero(SG*GG-GG*SG)
    yy=s.symbols('yy',positive=True);kk=s.symbols('k',real=True)
    f=s.Function('f')(yy);Dz=lambda f:-I*s.diff(f,yy)+I*kk*f/yy
    lam=I*s.sqrt(yy)*Dz(s.sqrt(yy)*f)
    aa=I*yy**s.Rational(3,2)*Dz(f/s.sqrt(yy))
    reference_signs=[int(s.sign(s.simplify((op-yy*s.diff(f,yy))/f).subs(kk,0))) for op in (lam,aa)]
    facts['actual_cusp_extreme_drifts']=s.simplify(lam-yy*s.diff(f,yy)-(s.Rational(1,2)-kk)*f)==0 and s.simplify(aa-yy*s.diff(f,yy)-(-s.Rational(1,2)-kk)*f)==0
    facts['drifts_agree_with_existing_end_blocks']=all(sorted([C[0,0] for h0 in (0,1) for C in end.end_blocks(0,k,h0)])==[ -s.Rational(1,2)-k,s.Rational(1,2)-k] for k in range(-4,5))
    roster=physical.full_weights();q5=[(key,v) for key,v in roster.items() if abs(key[3])==5]
    facts['charged_witness_not_a_deleted_exotic']=sum(v for key,v in q5)==12 and all(key[4]==0 for key,v in q5)
    witness=s.kronecker_product(s.eye(4)[:,0],s.eye(4)[:,0])
    ang=H.subs(dict(zip(mom,[0]*4))).subs(r,1)
    facts['old_allowed_lambda_has_decaying_angular_symbol']=zero((ang+s.eye(16))*witness)
    allowed_old=s.kronecker_product(g5,s.diag(1,-1,1,-1))
    facts['old_reference_trace_keeps_the_witness']=zero((allowed_old-s.eye(16))*witness)
    facts['new_trace_does_not_reuse_old_witness']=not zero((B-s.eye(16))*witness)
    facts['new_sigma_mixes_angular_parity']=zero(R*S+S*R) and not zero(R*S-S*R)
    ranks=[]
    for pp,rr in [((0,0,0,0),1),((0,0,0,0),-1),((1,2,2,0),4),((1,0,0,0),0)]:
        subs=dict(zip(mom,pp));subs[r]=rr;rho=s.sqrt(sum(v*v for v in pp)+rr*rr)
        for adj in (False,True):
            hh=(Ha if adj else H).subs(subs)
            bc=(s.eye(16)+B if adj else s.eye(16)-B).subs(th,0)
            ranks.append(s.Matrix.vstack(bc,hh+rho*s.eye(16)).rank())
    facts['finite_full_symbol_rank_controls']=ranks==[16]*8
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
      'full_symbol_ranks':ranks,'j0_reference_signs':reference_signs,
      'charged_witness_weights':int(sum(v for key,v in q5)),
      'different_local_kinetic_boundary_constructed':True,
      'old_reference_has_local_elliptic_lift':False,
      'old_anomaly_transfers_to_new_boundary':False,'interacting_boundary_completion':False,
      'stable_chiral_spectrum_derived':False,'nonauthor_acceptance':False,'physical_goal_achieved':False}
if __name__=='__main__':
    d=run();print(json.dumps(d,indent=2,sort_keys=True));raise SystemExit(0 if all(d['facts'].values()) else 1)
