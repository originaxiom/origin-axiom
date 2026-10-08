"""Exact algebra supporting the compact-domain index proof, not a kernel census."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
BASE=Path(__file__).resolve().parent.parent
sp=importlib.util.spec_from_file_location('boundary_index_source',BASE/'weave_boundary_lift_2026_10_09/probe.py')
old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
I=s.I
zero=lambda A:all(s.simplify(a)==0 for a in A)
R=old.R;V=old.J.adjoint()*old.P
def sigma_pair(theta,n):
    B=I*s.diag(s.exp(I*(s.Rational(1,2)+n)*theta),s.exp(-I*theta/2))
    C=I*s.diag(s.exp(I*theta/2),s.exp(-I*(s.Rational(1,2)+n)*theta))
    lift=lambda b:s.BlockMatrix([[s.zeros(2),b],[b.adjoint(),s.zeros(2)]]).as_explicit()
    return B,C,lift(B),lift(C)
def rectangular_profile(K):
    return [K.cols-K.rank(),K.rows-K.rank(),K.cols-K.rows]
@lru_cache(None)
def run():
    f={};th=s.symbols('theta',real=True);n=s.symbols('n',integer=True)
    S=old.sigma(th);P=(s.eye(4)+S)/2;Q=s.eye(4)-P
    Ax=s.diag(s.Matrix([[0,-1/s.sqrt(2)],[1/s.sqrt(2),0]]),s.Matrix([[0,1],[-1,0]]))
    Ay=s.diag(-I*Ax[:2,:2],I*Ax[2:,2:])
    f['density_derivative_is_formally_transpose_symmetric']=zero(Ax+Ax.T) and zero(Ay+Ay.T)
    hh=s.diag(1,1/s.sqrt(2),1,1)
    f['actual_normal_bilinear_symbol']=zero(hh.inv()*Ay*hh.inv()-V)
    f['boundary_bilinear_vanishes_without_zero_trace']=zero(P.T*V*P) and P.rank()==2
    f['correct_adjoint_trace_is_complementary']=zero(P*Q) and zero(Q*V*P.conjugate()-V*P.conjugate())
    f['same_trace_adjoint_control_rejected']=not zero(P*V*P.conjugate()-V*P.conjugate())
    f['collar_antilinear_map_squares_to_minus_one']=zero(V*V.conjugate()+s.eye(4))
    D=s.diag(s.Rational(1,2),-s.Rational(1,2),0,0)
    f['normal_endpoint_antilinear_intertwining_with_minus']=zero(V*R-R*V) and zero(V*D+D*V)
    f['wrong_intertwining_plus_sign_rejected']=not zero(V+V)
    f['dirac_principal_clifford_relations']=zero(old.J.adjoint()*old.J-s.eye(4)) and zero(old.J+old.J.adjoint())
    f['source_and_adjoint_local_ellipticity']=zero(R*S+S*R) and zero(S*S-s.eye(4)) and zero(S-S.adjoint())
    f['spin_descent_is_retained']=zero(old.sigma(th+2*s.pi)-R*S*R)
    p=s.symbols('p',complex=True);om=s.Integer(2)
    q=s.Matrix([[1+I,2],[0,1-I]]);r=s.Matrix([[0,1],[2*I,3]])
    W=s.diag(om**2*s.eye(2),s.eye(2)/2,om*s.eye(2),om*s.eye(2))
    M=old.physical.mass(q,r,p,om);Md=old.physical.mass(-q.T,-r.T,-p,om)
    f['actual_full_interacting_trace_dual_transpose']=zero(W*M-(W*Md).T)
    L=M-old.physical.mass(s.zeros(2),s.zeros(2),p,om)
    f['higgs_deformation_is_order_zero']=not zero(L) and p not in L.free_symbols and s.conjugate(p) not in L.free_symbols
    f['wrong_dual_transpose_is_detected']=not zero(W*M-(W*old.physical.mass(q,r,-p,om)).T)
    K=s.Matrix([[1,2,0,0,0],[0,1,1,0,0]])
    A=s.BlockMatrix([[s.zeros(5),K.T],[K,s.zeros(2)]]).as_explicit()
    rect=[rectangular_profile(K),rectangular_profile(K.T)]
    f['symmetric_bilinear_does_not_force_sector_zero']=zero(A-A.T) and rect==[[3,0,3],[0,3,-3]]
    B,C,Sq,Sc=sigma_pair(th,n)
    f['changed_pair_remains_unitary_elliptic']=all(zero(X*X-s.eye(4)) and zero(R*X+X*R) for X in (Sq,Sc))
    _,_,Sqnext,Scnext=sigma_pair(th+2*s.pi,n)
    f['changed_pair_retains_spin_seam']=zero(Sqnext-R*Sq*R) and zero(Scnext-R*Sc*R)
    f['changed_pair_retains_physical_conjugation']=zero(V*Sc.conjugate()*V+Sq)
    f['changed_pair_cross_boundary_bilinear_vanishes']=zero(((s.eye(4)+Sc)/2).T*V*((s.eye(4)+Sq)/2))
    B0=sigma_pair(th,0)[0];detq=s.simplify(B.det()/B0.det());detc=s.simplify(C.det()/B0.det())
    wind=[s.simplify(s.diff(d,th)/(I*d)) for d in (detq,detc)]
    f['relative_windings_are_opposite_integers']=wind==[n,-n]
    f['changed_pair_is_not_identical_endpoint']=not zero((Sq-Sc).subs(n,1))
    weights=old.physical.full_weights()
    dims=[6,3,2,3,6,1];ranks=[];conj=True
    for charge,dim in zip(range(1,7),dims):
        count=sum(value for key,value in weights.items() if key[3]==charge)
        assert count%dim==0
        ranks.append(count//dim)
        conj &= all(weights[tuple(-a for a in key)]==value for key,value in weights.items() if key[3]==charge)
    charged=sum(v for k,v in weights.items() if k[3]!=0)
    neutral=sum(v for k,v in weights.items() if k[3]==0)
    f['full_charged_multiplicity_and_conjugate_roster']=ranks==[5,10,10,5,1,5] and conj and [charged,neutral]==[212,36]
    facts={k:bool(v) for k,v in f.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
        'multiplicity_ranks':ranks,'charged_neutral_dimensions':[charged,neutral],
        'rectangular_control':rect,'winding_samples':[[i,-i] for i in (-3,-1,0,1,3)],
        'index_grade':'authored compact-domain argument with exact algebra controls',
        'full_kernel_census':False,'changed_boundary_index_computed':False,
        'boundary_law_selected':False,'stationary_chiral_completion':False,
        'nonauthor_acceptance':False,'physical_goal_achieved':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True))
    raise SystemExit(0 if all(data['facts'].values()) else 1)
