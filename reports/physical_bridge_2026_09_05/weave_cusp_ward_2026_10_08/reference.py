"""Separate spin-line color roster, block phase and Gaussian integration."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import mpmath as mp
import sympy as s

path=Path(__file__).resolve().parent.parent/'weave_cusp_heat_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('cusp_ward_tensor_reference',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)

@lru_cache(None)
def coefficients(n):
    out=Counter()
    for (a,b,w,q,m),mult in prior.prior.tensor_weights().items():
        if q<=0:continue
        color=F((a+2*b)**3,-6)
        for mu in prior.masses(m+2*n*q):out[abs(mu)]+=F(mult,2)*color*(1 if mu>0 else -1)
    return {mu:c for mu,c in out.items() if c}

def serialized(n):return [[str(mu),str(c)] for mu,c in sorted(coefficients(n).items())]

def quadratures():
    rows=[]
    with mp.workdps(45):
        for n in range(-3,4):
            pop=[(mp.mpf(mu.numerator)/mu.denominator,mp.mpf(c.numerator)/c.denominator) for mu,c in coefficients(n).items()]
            for z in (mp.mpf(0),mp.mpf(1)/16,mp.mpf(1),mp.mpf(4)):
                # s=u^2 removes the integrable endpoint singularity.
                fun=lambda u:sum(2*c*mu*mp.exp(-(mu*mu+z)*u*u)/mp.sqrt(mp.pi) for mu,c in pop)
                value=mp.quad(fun,[0,1,mp.inf]);target=sum(c*mu/mp.sqrt(mu*mu+z) for mu,c in pop)
                rows.append({'n':n,'z':str(z),'error':str(abs(value-target)),
                    'pass':bool(abs(value-target)<mp.mpf('1e-30'))})
    return rows

@lru_cache(None)
def run():
    facts={};K=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    A=s.diag(1,2,-3);C=s.diag(1,0,0)
    dK=s.I*(A*K-K*A);dKd=s.I*(A*K.adjoint()-K.adjoint()*A)
    source=(C*K.inv()*dK).trace();target=(C*K.adjoint().inv()*dKd).trace()
    phase=-(source-target)/2
    facts['block_phase_source_and_target_kept']=s.simplify(phase/s.I)==-s.Rational(5,2) and source!=target
    facts['full_trace_unweighted_phase_zero']=(K.inv()*dK).trace()-(K.adjoint().inv()*dKd).trace()==0
    facts['independent_tensor_slots_complete']=sum(prior.prior.tensor_weights().values())==248
    facts['independent_color_ir_coefficients']=all(str(sum(coefficients(n).values(),F(0)))==prior.prior.anomalies(n)[0] for n in range(-3,4))
    facts['zero_flux_response_empty']=not coefficients(0)
    facts['opposite_flux_every_mass']=all(coefficients(-n)=={mu:-c for mu,c in coefficients(n).items()} for n in (1,2,3))
    # Cartan weights of the explicit smooth background, not a copied matrix trace.
    t=(1,1,-2);c=(1,0,-1)
    weighted=8*sum(x**3 for x in t);bracket=8*sum(a*b*b for a,b in zip(c,t))
    facts['weighted_torus_insertion_from_eigenvalues']=weighted==-48 and bracket==-24
    rows=quadratures()
    facts['all28_end_resolvent_integrals']=len(rows)==28 and all(row['pass'] for row in rows)
    facts['not_a_zero_end_by_convention']=sum(coefficients(2).values())==-3
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
      'color_end_coefficients':{str(n):serialized(n) for n in range(-3,4)},
      'color_response_at_zero':{str(n):str(sum(coefficients(n).values(),F(0))) for n in range(-3,4)},
      'graded_control_phase_over_i':str(s.simplify(phase/s.I)),
      'weighted_color_integral_over_pi4_h2':str(weighted),'bracket_integral_over_pi4_h2':str(bracket),
      'quadratures':rows,'quadrature_is_certificate':False,'nonauthor_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
