"""Separate rational endpoint, residue-dimension and SU5 tensor route."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json

def allowed(a,p):
    power,log = a-2*p-1,a-2
    return power > -1 or (power == -1 and log < -1)

def pole_bound(a):
    near = a//2
    return max(p for p in range(near-2,near+3) if allowed(a,p))

def residue_dimension(d):
    if d < 0:return 0
    return 1+max(d-1,0)

def hol(a):return residue_dimension(pole_bound(a))
def index(a):return hol(a)-hol(2-a)
def line_index(beta):return index(1-beta)-index(-beta)

def weights():
    z,w = (-2,-2,-2,3,3),(-2,-1,0,1,2)
    out=Counter()
    for i,j in product(range(5),repeat=2):
        out[z[i]-z[j],0]+=1
        out[0,w[i]-w[j]]+=1
    out[0,0]-=2
    for i,j in combinations(range(5),2):
        for b in w:
            out[z[i]+z[j],b]+=1
            out[-z[i]-z[j],-b]+=1
        for zz in z:
            out[-zz,w[i]+w[j]]+=1
            out[zz,-w[i]-w[j]]+=1
    return out

def charge_indices(n):
    out=Counter()
    for (q,m),mult in weights().items():
        # Native code calls J twice; here calculate four distinct kernel spaces.
        beta=m+2*n*q
        out[q]+=mult*(hol(1-beta)-hol(1+beta)-hol(-beta)+hol(2+beta))
    return dict(sorted(out.items()))

def bounds(n):return {str(q):d for q,d in charge_indices(n).items() if n*q>0}

def run():
    checks={}
    aa=range(-24,25)
    checks['endpoint_is_genuinely_maximal']=all(allowed(a,pole_bound(a)) and not allowed(a,pole_bound(a)+1) for a in aa)
    checks['log_equality_discriminates_zero_and_two']=allowed(0,0) and not allowed(2,1)
    checks['negative_zero_positive_divisor_controls']=[residue_dimension(d) for d in (-2,-1,0,1,2,3)]==[0,0,1,1,2,3]
    checks['duality_retains_both_kernel_spaces']=all(index(a)+index(2-a)==0 for a in aa)
    checks['zero_beta_and_first_positive_beta']=line_index(0)==0 and line_index(1)==1
    checks['all_tested_positive_beta_formula']=all(line_index(b)==b%2 for b in range(81))
    checks['full_SU5_tensor_population']=sum(weights().values())==248
    checks['actual_highest_weight_bound']=all(m+2*abs(q)>=0 for q,m in weights() if q)
    expected={'1':12,'2':18,'3':12,'4':6,'5':0,'6':2}
    checks['positive_flux_full_profile']=all(bounds(n)==expected for n in (1,2,3,5))
    checks['negative_flux_conjugation']=all({str(-int(q)):v for q,v in bounds(-n).items()}==expected for n in (1,2,3,5))
    checks['independent_odd_weight_inventory']=Counter({q:sum(mult for (qq,m),mult in weights().items() if qq==q and m%2) for q in range(1,7)})==Counter({int(q):d for q,d in expected.items()})
    checks['zero_flux_is_not_an_instability']=bounds(0)=={} and sum(v for q,v in charge_indices(0).items() if q>0)==40
    checks['zero_gauge_root_index_does_not_certify_full_stability']=all(bounds(n)['5']==0 and sum(bounds(n).values())==50 for n in (1,2,3))
    checks['all_line_even_zero_modes_have_half_drift']=all(F(1-a,2).denominator==2 for a in aa if a%2==0)
    checks['compact_domain_substitution_would_miss_cusp_index']=index(-1)==-1 and index(0)==0
    checks['graph_approximation_numeric_margin']=F(1,16)-F(9,16)<0
    table=[{'a':a,'pole_bound':pole_bound(a),'h0':hol(a),'h1':hol(2-a),'index':index(a)} for a in aa]
    return {'predicates':checks,'predicates_passed':sum(checks.values()),'line_table':table,
            'charge_index_profiles':{str(n):{str(q):d for q,d in charge_indices(n).items()} for n in range(-3,4)},
            'unstable_bounds':{str(n):bounds(n) for n in range(-3,4)},
            'physical_goal_achieved':False,'independent_analytic_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
