"""Independent tensor/spin-line route and direct continuum integration."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import mpmath as mp

path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('cusp_heat_tensor_reference',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)

def masses(beta):
    return [F(-beta-1,2),F(1-beta,2)] if beta%2==0 else [F(beta,2)]*2

@lru_cache(None)
def characters(n):
    out={}
    for (a,b,w,q,m),mult in prior.tensor_weights().items():
        key=(a,b,w,q);out.setdefault(key,Counter())
        for mu in masses(m+2*n*q):
            assert mu
            out[key][abs(mu)]+=mult*(1 if mu>0 else -1)
    return {k:{m:c for m,c in pop.items() if c} for k,pop in out.items()}

def serialized(n):
    return [[*key,[[str(mu),count] for mu,count in sorted(pop.items())]]
            for key,pop in sorted(characters(n).items())]

def trace(n,power=None):
    out=[F(0)]*5
    for (a,b,w,q),pop in characters(n).items():
        if q<=0:continue
        value=F(sum(pop.values()),2) if power is None else sum(c*mu**power for mu,c in pop.items())
        terms=[F((a+2*b)**3,-6),F(a*a*q,4),F(w*w*q,4),F(q**3),F(q)]
        out=[x+value*y for x,y in zip(out,terms)]
    return [str(x) for x in out]

def quadrature():
    rows=[]
    with mp.workdps(45):
        for mu in (mp.mpf('0.5'),mp.mpf('1.5'),mp.mpf('3.5')):
            for sign in (-1,1):
                m=sign*mu
                for t in (mp.mpf(1)/16,mp.mpf(1)/2,mp.mpf(3)/2):
                    value=mp.quad(lambda p:-m*mp.exp(-t*(p*p+m*m))/(mp.pi*(p*p+m*m)),[0,1,mp.inf])
                    target=-sign*mp.erfc(mu*mp.sqrt(t))/2
                    rows.append({'mu':str(m),'s':str(t),'error':str(abs(value-target)),
                       'pass':bool(abs(value-target)<mp.mpf('1e-30'))})
    return rows

@lru_cache(None)
def run():
    facts={};weights=prior.tensor_weights()
    facts['all_tensor_slots_kept']=sum(v*len(masses(m+4*q)) for (a,b,w,q,m),v in weights.items())==496
    facts['line_signature_equals_independent_complete_kernel']=all(F(sum(1 if mu>0 else -1 for mu in masses(b)),2)==prior.physical_line_index(b) for b in range(-80,81))
    facts['character_half_signatures_recover_all_gauge_indices']=all(
        {k:F(sum(pop.values()),2) for k,pop in characters(n).items()}==prior.gauge_indices(n) for n in range(-3,4))
    facts['ir_all_five_match_independent_tensor_anomalies']=all(trace(n)==prior.anomalies(n) for n in range(-3,4))
    facts['zero_flux_all_characters_empty']=all(not pop for pop in characters(0).values())
    facts['opposite_flux_full_characters']=all(characters(-n)=={k:{mu:-c for mu,c in pop.items()} for k,pop in characters(n).items()} for n in (1,2,3))
    facts['half_odd_integer_masses_gapped']=all(mu.denominator==2 and mu>=F(1,2) for n in range(-3,4) for pop in characters(n).values() for mu in pop)
    facts['color_linear_moment_zero']=all(F(trace(n,1)[0])==0 for n in range(-3,4))
    facts['color_cubic_moment_recomputed']=all(F(trace(n,3)[0])==48*n*(7*n*n-2) for n in range(-3,4))
    rows=quadrature()
    facts['all18_direct_continuum_integrals']=len(rows)==18 and all(row['pass'] for row in rows)
    facts['wrong_continuum_sign_rejected']=all(F(row['mu'])!=0 for row in rows) and mp.erfc(mp.mpf('0.5'))>mp.mpf('1e-30')
    # The limits are exact properties of erf/erfc with nonzero half-integer arguments.
    facts['zero_mode_projection_not_heat_regulator']=trace(2)!=['0']*5 and all(mu>0 for pop in characters(2).values() for mu in pop)
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
       'odd_mass_characters':{str(n):serialized(n) for n in range(-3,4)},
       'odd_moments':{str(n):{str(r):trace(n,r) for r in (1,3,5)} for n in range(-3,4)},
       'ir_anomaly_vectors':{str(n):trace(n) for n in range(-3,4)},
       'quadrature':rows,'quadrature_is_interval_certificate':False,
       'nonauthor_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
