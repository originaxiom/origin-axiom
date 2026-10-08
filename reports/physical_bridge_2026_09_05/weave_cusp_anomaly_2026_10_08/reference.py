"""Separate line-end and tensor route; no native or new-block imports."""
from collections import Counter
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path

path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('cusp_anomaly_ref',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)

def sign(x):return int(x>0)-int(x<0)
def end(a):return F(sign(1-a),2) if a%2==0 else F(0)
def idx(beta):return 2*end(1-beta)-end(-beta)-end(2-beta)

def weights(n):
    out=Counter()
    for (a,b,w,q,m),mult in prior.tensor_weights().items():
        out[a,b,w,q]+=mult*idx(m+2*n*q)
    return out

def profiles(n):
    values={}
    for (*_,q),v in weights(n).items():
        if q>0:values.setdefault(q,set()).add(v)
    assert all(len(v)==1 for v in values.values())
    return {str(q):int(next(iter(v))) for q,v in sorted(values.items())}

def anomalies(n):
    # One sign per charge pair; no half of a doubled root sum.
    out=[F(0)]*5
    for (a,b,w,q),v in weights(n).items():
        if q<=0:continue
        terms=[F((a+2*b)**3,-6),F(q*a*a,4),F(q*w*w,4),F(q**3),F(q)]
        out=[x+v*y for x,y in zip(out,terms)]
    return list(map(str,out))

def run():
    facts={}
    facts['line_end_from_global_kernel_formula']=all(
        prior.h(a)-prior.h(2-a)==F(a-1,2)+end(a) for a in range(-40,41))
    facts['all_four_slots_from_line_ends']=all(idx(b)==prior.physical_line_index(b) for b in range(-40,41))
    facts['even_and_odd_angular_controls']=end(0)==F(1,2) and end(1)==0 and end(2)==F(-1,2)
    facts['virtual_rank_and_degree_cancel']=2-1-1==0 and all(
        2*(1-b)-(-b)-(2-b)==0 for b in range(-40,41))
    facts['tensor_population248']=sum(prior.tensor_weights().values())==248
    facts['tensor_end_equals_complete_physical_counts']=all(weights(n)==prior.gauge_indices(n) for n in range(-3,4))
    facts['tensor_anomaly_matches_previous_physical']=all(anomalies(n)==prior.anomalies(n) for n in range(-3,4))
    facts['first_flux_control']=profiles(1)['1']==0 and profiles(2)['1']==-1
    facts['nonzero_and_zero_anomaly']=anomalies(2)==['-3','-6','-6','-1008','-30'] and anomalies(0)==['0']*5
    facts['opposite_end_orientation_flips']=all(idx(-b)==-idx(b) for b in range(-40,41))
    facts['boundary_not_compensating_new_matter']=anomalies(2)!=[str(-F(x)) for x in anomalies(2)]
    module=[];closed=True
    for j in range(5):
        for k in range(-4,5):
            val=sum(idx(m+2*k) for m in range(-j,j+1))
            a=F(j+1,2) if j%2==0 else F(j,2)
            extreme=F((-1 if j%2==0 else 1)*(sign(k+a)+sign(k-a)),2)
            closed=closed and val==extreme
            module.append([j,k,int(val)])
    facts['extreme_formula_from_independent_line_sum']=closed
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
        'end_index_profiles':{str(n):profiles(n) for n in range(-3,4)},
        'end_anomaly_vectors':{str(n):anomalies(n) for n in range(-3,4)},
        'module_end_indices':module,'nonauthor_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
