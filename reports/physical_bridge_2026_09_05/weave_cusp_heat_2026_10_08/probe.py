"""Cusp heat/scattering controls; analytic hypotheses live in PROOF.md."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

path=Path(__file__).resolve().parent.parent/'weave_cusp_anomaly_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('cusp_heat_end',path)
end=importlib.util.module_from_spec(spec);spec.loader.exec_module(end)
Q=s.Rational
zero=lambda mat:all(s.simplify(v)==0 for v in mat)

def extreme_masses(j,k):
    return [C[0,0] for h in (0,1) for C in end.end_blocks(j,k,h) if C.rows==1]

@lru_cache(None)
def characters(n):
    out={}
    for (a,b,w,q,j),mult in end.modules().items():
        key=(a,b,w,q);out.setdefault(key,Counter())
        for mu in extreme_masses(j,n*q):
            assert mu!=0
            out[key][abs(mu)]+=mult*int(s.sign(mu))
    return {k:{m:c for m,c in pop.items() if c} for k,pop in out.items()}

def serialized(n):
    return [[*key,[[str(mu),count] for mu,count in sorted(pop.items())]]
            for key,pop in sorted(characters(n).items())]

def trace_terms(key):
    a,b,w,q=key
    return (Q((a+2*b)**3,-6),Q(a*a*q,4),Q(w*w*q,4),s.Integer(q**3),s.Integer(q))

def moment(n,r):
    assert r>0 and r%2
    out=[s.Integer(0)]*5
    for key,pop in characters(n).items():
        v=sum(c*mu**r for mu,c in pop.items())
        out=[s.expand(x+v*y/2) for x,y in zip(out,trace_terms(key))]
    return out

def ir(n):
    out=[s.Integer(0)]*5
    for key,pop in characters(n).items():
        idx=Q(sum(pop.values()),2)
        out=[x+idx*y/2 for x,y in zip(out,trace_terms(key))]
    return [str(x) for x in out]

def heat(n,time):
    out=[s.Integer(0)]*5
    for key,pop in characters(n).items():
        value=sum(c*s.erf(mu*s.sqrt(time))/2 for mu,c in pop.items())
        out=[x+value*y/2 for x,y in zip(out,trace_terms(key))]
    return out

def module_moment(j,k,r):
    return s.expand(sum(mu**r for mu in extreme_masses(j,k)))

def symbolic_color_moment(r):
    n=s.symbols('n',integer=True)
    return s.expand(2*module_moment(2,n,r)-module_moment(1,2*n,r)
       -module_moment(3,2*n,r)+module_moment(2,4*n,r)
       -2*module_moment(0,5*n,r))

def product_checks():
    x=s.Matrix([[0,1],[1,0]]);y=s.Matrix([[0,-s.I],[s.I,0]])
    z=s.diag(1,-1);I=s.eye(2);kron=s.kronecker_product
    gam=[kron(x,x),kron(x,y),kron(x,z),kron(y,I)]
    g5=gam[0]*gam[1]*gam[2]*gam[3]
    pp=s.symbols('p0:4',real=True);p,mu=s.symbols('p mu',real=True)
    D4=sum((a*g for a,g in zip(pp,gam)),s.zeros(4))
    D=s.Matrix([[0,mu-s.I*p],[mu+s.I*p,0]])
    total=kron(D4,I)+kron(g5,D);grade=kron(g5,z)
    return {
       'euclidean_clifford_and_grading':all(zero(a*b+b*a-2*(i==j)*s.eye(4))
          for i,a in enumerate(gam) for j,b in enumerate(gam)) and zero(g5*g5-s.eye(4)),
       'total_operator_is_odd':zero(grade*total+total*grade),
       'product_square_has_no_cross_term':zero(total*total-kron(D4*D4,I)-kron(s.eye(4),D*D)),
       'curvature_gamma_trace_not_scalar_laplacian':g5.trace()==0 and
          s.simplify((g5*gam[0]*gam[1]*gam[2]*gam[3]).trace())==4}

@lru_cache(None)
def run():
    facts={}
    mu,p=s.symbols('mu p',real=True);t=s.symbols('s',positive=True)
    J=s.Matrix([[0,-1],[1,0]]);G=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]])
    D=s.I*p*J+mu*X
    facts['actual_cutoff_current_trace']=(G*J*D).trace()==-2*mu
    u=s.symbols('u',real=True);cut=1-3*u*u+2*u**3
    flux=s.integrate(s.diff(cut,u),(u,0,1))
    facts['outward_cutoff_integral_is_minus_one']=flux==-1
    gaussian=s.integrate(s.exp(-t*p*p),(p,-s.oo,s.oo))/(2*s.pi)
    facts['radial_gaussian_normalization']=s.simplify(gaussian-1/s.sqrt(4*s.pi*t))==0
    current=s.simplify(flux*(G*J*D).trace()*gaussian*s.exp(-t*mu*mu)/2)
    facts['erf_derivative_equals_end_current']=s.simplify(s.diff(s.erf(mu*s.sqrt(t))/2,t)-current)==0
    facts['wrong_sign_and_cyclic_zero_both_fail']=current.subs(mu,1)!=0 and s.simplify(current+current)!=0
    ratio=(mu-s.I*p)/(mu+s.I*p)
    density=s.simplify(s.diff(ratio,p)/ratio/(2*s.pi*s.I))
    facts['scattering_density_sign_and_normalization']=s.simplify(density+mu/(s.pi*(p*p+mu*mu)))==0
    facts['incoming_outgoing_norms_equal']=s.simplify(ratio*s.conjugate(ratio)-1)==0
    # Determinant identity permits arbitrary core mixing at common energy.
    a,b,c,d=s.symbols('a b c d',nonzero=True);mix=s.Matrix([[1,2],[3,5]])
    din=s.diag(a,b);dout=s.diag(c,d);partner=dout*mix*din.inv()
    facts['mixed_channel_scattering_determinant']=s.simplify(mix.det()/partner.det()-a*b/(c*d))==0
    pos=s.symbols('m',positive=True)
    cont=-s.erfc(pos*s.sqrt(t))/2
    facts['continuum_derivative_and_limits']=s.simplify(s.diff(cont,t)-pos*s.exp(-t*pos**2)/s.sqrt(4*s.pi*t))==0 and s.limit(cont,t,0)==-Q(1,2) and s.limit(cont,t,s.oo)==0
    facts['continuum_plus_index_is_erf']=s.simplify(cont+Q(1,2)-s.erf(pos*s.sqrt(t))/2)==0
    delta,beta,tau=s.symbols('delta beta tau',real=True)
    C=s.Matrix([[delta,tau*beta],[tau*beta,-delta]])
    facts['coupled_pairs_cancel_all_odd_functions']=C.trace()==0 and zero(C*C-(delta**2+tau**2*beta**2)*s.eye(2))
    facts['full248_and496_channels_retained']=sum(v*(2*j+1) for (*_,j),v in end.modules().items())==248 and sum(v*sum(C.rows for h in (0,1) for C in end.end_blocks(j,2*q,h)) for (a,b,w,q,j),v in end.modules().items())==496
    facts['half_signature_reproduces_prior_every_gauge_weight']=all(
       {k:Q(sum(pop.values()),2) for k,pop in characters(n).items()}==end.gauge_indices(n) for n in range(-3,4))
    facts['all_five_ir_anomalies_recovered']=all(ir(n)==end.anomaly(n) for n in range(-3,4))
    facts['first_flux_endpoint_and_exotic_retained']=ir(1)==['-1','-5','-9/2','-1002','-24'] and ir(2)==['-3','-6','-6','-1008','-30'] and any(q==5 and pop for (*_,q),pop in characters(2).items())
    facts['zero_flux_every_character_zero']=all(not pop for pop in characters(0).values())
    facts['opposite_flux_character_reversal']=all(characters(-n)=={k:{mu:-c for mu,c in pop.items()} for k,pop in characters(n).items()} for n in (1,2,3))
    facts['ultraviolet_all_weight_traces_zero']=all(s.erf(mu*s.sqrt(t)).subs(t,0)==0 for n in range(-3,4) for pop in characters(n).values() for mu in pop)
    ni=s.symbols('n',integer=True)
    facts['color_first_moment_zero']=symbolic_color_moment(1)==0
    facts['color_cubic_moment_exact_polynomial']=s.expand(symbolic_color_moment(3)-48*ni*(7*ni**2-2))==0
    facts['polynomial_matches_actual_full_weight_traces']=all(moment(n,1)[0]==0 and moment(n,3)[0]==48*n*(7*n*n-2) for n in range(-3,4))
    z=s.symbols('z')
    facts['erf_series_color_coefficient']=s.series(s.erf(z)/2,z,0,6).removeO().coeff(z,3)==-1/(3*s.sqrt(s.pi))
    facts['finite_heat_not_zero_mode_truncation']=all(heat(n,Q(1,16))[0].evalf(25)<0 for n in (1,2,3)) and heat(2,Q(1,16))[0]!=-3
    facts.update(product_checks())
    length=s.symbols('length',positive=True)
    density_even=2*s.exp(-t*pos*pos)/s.sqrt(4*s.pi*t)
    facts['positive_ungraded_end_density_diverges']=density_even.is_positive and s.limit(length*density_even,length,s.oo)==s.oo
    facts['opposite_pair_zero_odd_nonzero_even']=s.simplify(s.erf(pos*s.sqrt(t))+s.erf(-pos*s.sqrt(t)))==0 and 2*density_even!=0
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
      'odd_mass_characters':{str(n):serialized(n) for n in range(-3,4)},
      'odd_moments':{str(n):{str(r):list(map(str,moment(n,r))) for r in (1,3,5)} for n in range(-3,4)},
      'ir_anomaly_vectors':{str(n):ir(n) for n in range(-3,4)},
      'continuum_retained':True,'projected_covariant_heat_uv_zero':True,
      'consistent_ward_identity_derived':False,'determinant_phase_derived':False,
      'parity_even_quantum_action_renormalized':False,'full_quantum_completion_derived':False,
      'stable_chiral_vacuum_derived':False,'genesis_selection_derived':False,
      'nonauthor_acceptance':False,'physical_goal_achieved':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
