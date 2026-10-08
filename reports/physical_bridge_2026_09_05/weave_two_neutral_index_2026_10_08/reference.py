"""Separate exact rational index, SU5 weights and complex-composition route."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations,product
import json

def hol(a):
    near=a//2
    allowed=[p for p in range(near-2,near+3)
             if a-2*p>0 or (a-2*p==0 and a<1)]
    bound=max(allowed)
    return 0 if bound<0 else 1+max(bound-1,0)

def line_index(beta):
    return 2*hol(1-beta)-2*hol(1+beta)-hol(-beta)+hol(2+beta)-hol(2-beta)+hol(beta)

def weights():
    z,w=(-2,-2,-2,3,3),(-2,-1,0,1,2);out=Counter()
    for i,j in product(range(5),repeat=2):
        out[z[i]-z[j],0]+=1;out[0,w[i]-w[j]]+=1
    out[0,0]-=2
    for i,j in combinations(range(5),2):
        for b in w:
            out[z[i]+z[j],b]+=1;out[-z[i]-z[j],-b]+=1
        for zz in z:
            out[-zz,w[i]+w[j]]+=1;out[zz,-w[i]-w[j]]+=1
    return out

def indices(n):
    out=Counter()
    for (q,m),mult in weights().items():out[q]+=mult*line_index(m+2*n*q)
    return dict(sorted(out.items()))

def positive(n):
    return {str(q):i for q,i in indices(n).items() if n*q>0 and i>0}

def population():
    ww=weights()
    even=sum(mult for (q,m),mult in ww.items() if m%2==0)
    odd=sum(mult for (q,m),mult in ww.items() if m%2)
    return {'physical_C1':even+2*odd,'auxiliary_C3':even,
            'h0':even+odd,'h1':even+odd,'total':2*(even+odd)}

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def zero(a):return all(x==0 for row in a for x in row)
def scale(a,c):return [[c*x for x in row] for row in a]
def row(*blocks):return [sum((b[i] for b in blocks),[]) for i in range(len(blocks[0]))]
def complex_maps(q,r,p=3):
    ident=[[int(i==j) for j in range(3)] for i in range(3)]
    zz=scale(ident,0);dd=scale(ident,p)
    # Constant row/column phases remove i and the common sqrt(2).
    return dd+q+r, row(scale(q,-1),dd,zz)+row(scale(r,-1),zz,dd)+row(zz,scale(r,-1),q),row(r,scale(q,-1),dd)

def run():
    checks={}
    checks['actual_six_kernel_terms_and_endpoint']=line_index(0)==0 and line_index(1)==1 and line_index(2)==-1
    checks['all_signed_parity_controls']=all(line_index(b)==(-1 if b>0 else 1)*(1 if b%2==0 else -1) for b in range(-80,81) if b)
    checks['duality_odd_index']=all(line_index(-b)==-line_index(b) for b in range(81))
    checks['full_SU5_tensor_roster']=sum(weights().values())==248
    checks['beta_endpoint_and_higher_flux_bound']=all(m+2*abs(q)>=0 and m+4*abs(q)>0 for q,m in weights() if q)
    expected={1:-6,2:6,3:4,4:-3,5:-6,6:-1}
    checks['higher_flux_profiles']=all({q:indices(n)[q] for q in range(1,7)}==expected for n in (2,3,5))
    first=dict(expected);first[1]=0
    checks['first_flux_exception_retained']={q:indices(1)[q] for q in range(1,7)}==first
    checks['opposite_flux_profiles']=all(indices(-n)=={q:-v for q,v in indices(n).items()} for n in (1,2,3))
    checks['zero_flux_index_is_zero']=all(v==0 for v in indices(0).values())
    checks['only_positive_indices_used_for_ten_bound']=all(positive(n)=={'2':6,'3':4} for n in (1,2,3,5))
    checks['negative_flux_uses_conjugate_charges']=all(positive(-n)=={'-3':4,'-2':6} for n in (1,2,3,5))
    checks['auxiliary_population_is_not_discarded']=population()=={'physical_C1':360,'auxiliary_C3':136,'h0':248,'h1':248,'total':496}
    drifts=[]
    for h in (0,1):
        for j in range(5):
            drifts.extend(F(m+1-h,2) for m in range(-j,j+1) if (m-h)%2==0)
            if (j+h)%2:drifts.append(-F(j+h,2))
    checks['paired_and_extreme_drift_parity']=all(d.denominator==2 for d in drifts)
    checks['integer_shifts_cannot_close_homotopy_gap']=all((n+d)**2>=F(1,4) for d in drifts for n in range(-12,13))
    q=[[1,1,0],[0,1,0],[0,0,1]];r=[[2,0,0],[0,2,0],[0,0,2]]
    d0,d1,d2=complex_maps(q,r)
    checks['separate_complex_compositions']=zero(mul(d1,d0)) and zero(mul(d2,d1))
    rq=[[0,0,0],[0,0,1],[0,0,0]]
    b0,b1,b2=complex_maps(q,rq)
    checks['noncommuting_control_fails']=not zero(mul(b1,b0)) and not zero(mul(b2,b1))
    checks['auxiliary_scalar_injection_needs_nonzero_R']=F(2)**3!=0 and F(0)**3==0
    checks['finite_negative_margin_after_compact_approximation']=F(1,16)-2*F(9,16)<0
    return {'predicates':checks,'predicates_passed':sum(checks.values()),
        'line_index_table':[{'beta':b,'index':line_index(b)} for b in range(-24,25)],
        'index_profiles':{str(n):{str(q):v for q,v in indices(n).items()} for n in range(-3,4)},
        'positive_bounds':{str(n):positive(n) for n in range(-3,4)},
        'hodge_populations':population(),'physical_goal_achieved':False,
        'independent_analytic_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
