"""Actual end-current and gauge-curl controls, not a full determinant."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

path=Path(__file__).resolve().parent.parent/'weave_cusp_heat_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('cusp_ward_heat',path)
heat=importlib.util.module_from_spec(spec);spec.loader.exec_module(heat)
Q=s.Rational
comm=lambda a,b:a*b-b*a
zero=lambda a:all(s.simplify(v)==0 for v in a)

@lru_cache(None)
def color_coefficients(n):
    out=Counter()
    for key,pop in heat.characters(n).items():
        for mu,count in pop.items():out[mu]+=heat.trace_terms(key)[0]*count/4
    return {mu:c for mu,c in out.items() if c}

def serialized(n):return [[str(mu),str(c)] for mu,c in sorted(color_coefficients(n).items())]
def response(n,z):return sum(c*mu/s.sqrt(mu*mu+z) for mu,c in color_coefficients(n).items())

def graded_control():
    P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]]);I=s.eye(3);O=s.zeros(3)
    D=s.BlockMatrix([[O,P.T],[P,O]]).as_explicit();G=s.diag(I,-I)
    C=s.diag(1,0,0);chi=s.diag(C,C);A=s.diag(1,2,-3);alpha=s.diag(A,A)
    st=lambda x:s.trace(G*x)
    R=D.inv()*D.inv();delta=s.I*comm(alpha,D)
    omega=-st(chi*D*R*delta)/2
    bulk=s.I*st(chi*D*D*R*alpha)
    end=s.I*st(comm(D,chi)*D*R*alpha)/2
    full=-st(D*R*delta)/2
    return D,G,chi,alpha,omega,bulk,end,full

def color_control():
    T=s.diag(1,1,-2);X=s.zeros(3);Y=s.zeros(3)
    X[0,2]=X[2,0]=Q(1,2);Y[0,2]=-s.I/2;Y[2,0]=s.I/2
    alpha=X;beta=2*Y;c=-s.I*comm(alpha,beta);F2=T*T
    first=s.trace(beta*s.I*comm(alpha,F2))
    second=s.trace(alpha*s.I*comm(beta,F2))
    bracket=s.trace(c*F2)
    return T,X,Y,c,first,second,bracket

@lru_cache(None)
def run():
    facts={};D,G,chi,alpha,omega,bulk,end,full=graded_control()
    facts['finite_control_has_actual_grading']=zero(G*D+D*G) and D==D.adjoint() and zero(comm(chi,alpha))
    facts['finite_gauge_variation_includes_end']=s.simplify(omega-bulk-end)==0
    facts['dropping_end_fails_nonzero_control']=omega!=0 and bulk==0 and omega!=bulk
    facts['outward_sign_reversal_fails']=s.simplify(omega-bulk+end)!=0
    facts['ordinary_full_cutoff_control_zero']=full==0
    facts['exact_control_value']=s.simplify(omega/s.I)==Q(-5,2)
    m,z,t=s.symbols('m z t',positive=True)
    deriv=m*s.exp(-m*m*t)/s.sqrt(s.pi*t)
    integral=s.integrate(s.exp(-z*t)*deriv,(t,0,s.oo))
    facts['end_propagator_laplace_transform']=s.simplify(integral-m/s.sqrt(m*m+z))==0
    facts['integrable_end_derivative_has_index_limit']=s.limit(m/s.sqrt(m*m+z),z,0)==1 and s.limit(m/s.sqrt(m*m+z),z,s.oo)==0
    facts['all_color_end_responses_recover_ir']=all(s.simplify(response(n,0)-s.sympify(heat.ir(n)[0]))==0 for n in range(-3,4))
    facts['first_flux_not_high_flux']=response(1,0)==-1 and response(2,0)==-3
    facts['opposite_flux_and_zero_kept']=not color_coefficients(0) and all(color_coefficients(-n)=={mu:-c for mu,c in color_coefficients(n).items()} for n in (1,2,3))
    facts['heat_uv_and_propagator_end_are_distinct']=heat.heat(2,0)[0]==0 and response(2,0)==-3
    facts['all_parent_color_generator_norms_bounded']=max(abs(a+2*b) for a,b,w,q,m in heat.end.physical.full_weights())==3
    h=s.symbols('h',positive=True);x1,x3=s.symbols('x1 x3',real=True)
    T,X,Y,c,first,second,bracket=color_control()
    common=s.integrate(s.cos(x1)**2,(x1,0,2*s.pi))*s.integrate(s.cos(x3)**2,(x3,0,2*s.pi))*(2*s.pi)**2
    weighted=2*h*h*s.trace(T**3)*common
    bracket_weighted=2*h*h*s.trace(c*T*T)*common
    facts['smooth_gauge_insertion_is_nonzero']=s.simplify(weighted+48*s.pi**4*h*h)==0
    facts['global_topological_integral_zero']=s.integrate(s.cos(x1),(x1,0,2*s.pi))*s.integrate(s.cos(x3),(x3,0,2*s.pi))==0
    facts['strict_external_gap_control']=Q(1,2)-6*Q(1,24)>0 and Q(1,2)-6*Q(1,12)==0
    facts['nonabelian_bracket_is_actual_color_generator']=c==s.diag(1,0,-1) and s.simplify(bracket_weighted+24*s.pi**4*h*h)==0
    facts['gauge_covariance_has_factor_two']=first==bracket and second==-bracket and first-second==2*bracket
    facts['consistency_curl_is_nonzero']=first-second-bracket==bracket and bracket==-3
    facts['commuting_parameters_curl_control_zero']=zero(comm(T,c))
    # Product end numerator: external D4 part traces to zero, internal part keeps gamma5.
    sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1)
    gam=[s.kronecker_product(sx,a) for a in (sx,sy,sz)]+[s.kronecker_product(sy,s.eye(2))]
    g5=gam[0]*gam[1]*gam[2]*gam[3]
    facts['end_product_keeps_chiral_external_trace']=all(g.trace()==0 for g in gam) and zero(g5*g5*g5-g5)
    # Dilation identity, not a numerical computation of the external heat kernel.
    L=s.symbols('L',positive=True);lam=s.symbols('lam',positive=True)
    facts['external_dilation_preserves_finite_L_gap']=s.simplify(s.exp(-t*(lam/L)**2)-s.exp(-(t/L**2)*lam**2))==0 and (lam/L).is_positive
    spectral=lam*s.exp(-t*lam/2)
    facts['positive_spectrum_shell_bound_control']=s.simplify(s.diff(spectral,lam).subs(lam,2/t))==0 and s.simplify(spectral.subs(lam,2/t)-2/(s.E*t))==0 and s.limit(spectral,lam,s.oo)==0
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
      'color_end_coefficients':{str(n):serialized(n) for n in range(-3,4)},
      'color_response_at_zero':{str(n):str(response(n,0)) for n in range(-3,4)},
      'graded_control_phase_over_i':str(s.simplify(omega/s.I)),
      'weighted_color_integral_over_pi4_h2':str(s.simplify(weighted/(s.pi**4*h*h))),
      'bracket_integral_over_pi4_h2':str(s.simplify(bracket_weighted/(s.pi**4*h*h))),
      'covariant_heat_positive_retained':True,'candidate_phase_is_integrable':False,
      'all_quantum_completions_excluded':False,'consistent_quantum_action_derived':False,
      'full_loop_renormalization_derived':False,'stable_chiral_vacuum_derived':False,
      'genesis_selection_derived':False,'nonauthor_acceptance':False,'physical_goal_achieved':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
