"""Separate tensor and zero-Higgs kernel calculation; no native imports."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
import json
import sympy as s

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)

def tensor_weights():
    gauge=[(1,0,0,-2),(-1,1,0,-2),(0,-1,0,-2),
           (0,0,1,3),(0,0,-1,3)]
    bundle=list(range(-2,3))
    wedge=[add(gauge[i],gauge[j]) for i,j in combinations(range(5),2)]
    bwedge=[bundle[i]+bundle[j] for i,j in combinations(range(5),2)]
    out=Counter()
    for i in range(5):
        for j in range(5):
            if i!=j:
                out[add(gauge[i],neg(gauge[j]))+(0,)]+=1
                out[(0,0,0,0,bundle[i]-bundle[j])]+=1
    out[(0,0,0,0,0)]+=8
    for gw in wedge:
        for m in bundle:
            key=gw+(m,);out[key]+=1;out[neg(key)]+=1
    for gw in gauge:
        for m in bwedge:
            key=neg(gw)+(m,);out[key]+=1;out[neg(key)]+=1
    return out

def h(a):
    bound=a//2 if a<=0 else (a+1)//2-1
    # Independent Weierstrass pole-order basis, not a degree proxy.
    orders=[0]+[i for i in range(2,bound+1)]
    return sum(p<=bound for p in orders)

def physical_line_index(beta):
    source=h(2+beta)+2*h(1-beta)+h(beta)
    target=h(-beta)+2*h(1+beta)+h(2-beta)
    return source-target

def gauge_indices(n):
    out=Counter()
    for key,mult in tensor_weights().items():
        a,b,w,q,m=key
        out[a,b,w,q]+=mult*physical_line_index(m+2*n*q)
    return out

def profiles(n):
    byq={}
    for (a,b,w,q),value in gauge_indices(n).items():
        if q>0:byq.setdefault(q,set()).add(value)
    assert all(len(vals)==1 for vals in byq.values())
    return {str(q):next(iter(v)) for q,v in sorted(byq.items())}

def anomalies(n):
    out=[F(0)]*5
    # One representative per conjugate pair, unlike native's half-full sum.
    for (a,b,w,q),value in gauge_indices(n).items():
        if q<=0:continue
        terms=[F((a+2*b)**3,-6),F(q*a*a,4),F(q*w*w,4),F(q**3),F(q)]
        out=[x+value*y for x,y in zip(out,terms)]
    return [str(x) for x in out]

def matrix_check():
    # Build the mass DENSITY directly from symmetric Weyl pairings,
    # using ell=sqrt(2)*lambda to keep rational normalization factors.
    om=s.Integer(5);p=1+2*s.I;pc=s.conjugate(p);O=s.zeros(2);I=s.eye(2)
    q=s.Matrix([[2+s.I,1],[0,2+s.I]]);r=(3-s.I)*I
    density=s.BlockMatrix([
      [O,pc*I/2,s.I*om*q.adjoint(),s.I*om*r.adjoint()],
      [-pc*I/2,O,-s.I*r,s.I*q],
      [-s.I*om*q.adjoint(),s.I*r,O,p*I],
      [-s.I*om*r.adjoint(),-s.I*q,-p*I,O]]).as_explicit()
    hf=s.diag(om**2*I/2,I/2,om*I,om*I)
    # T applied to (a,u,v,i*om^2*ell/2), then dual output rows.
    Tinput=s.BlockMatrix([
      [O,pc*I/(s.sqrt(2)*om**2),s.sqrt(2)*s.I*q.adjoint()/om,
         s.sqrt(2)*s.I*r.adjoint()/om],
      [s.I*om*r.adjoint(),s.I*q,p*I,O],
      [-s.I*om*q.adjoint(),s.I*r,O,p*I],
      [s.I*pc*I/2,O,-r,q]]).as_explicit()
    out=s.BlockMatrix([[s.sqrt(2)*I,O,O,O],[O,O,O,2*s.I*I],
                      [O,O,I/om,O],[O,-I/om,O,O]]).as_explicit()
    actual=hf.inv()*density
    zero=lambda mat:all(s.simplify(x)==0 for x in mat)
    # Output ell-dual has an extra sqrt(2); first T row is D0 adjoint.
    return zero(actual-out*Tinput),not zero(actual-Tinput),zero(
        density[:2,2:4]+density[2:4,:2])

@lru_cache(None)
def run():
    facts={}
    weights=tensor_weights()
    facts['complete_tensor248']=sum(weights.values())==248
    facts['every_tensor_weight_conjugate_retained']=all(
        weights[neg(k)]==v for k,v in weights.items())
    facts['spin_endpoint_three_zero_indices']=(physical_line_index(0)==0
          and h(0)==h(1)==h(2)==1 and h(-1)==0)
    facts['four_slot_kernel_minus_cokernel_formula']=all(
        physical_line_index(b)==(0 if b==0 else
          -(1 if b>0 else -1)*(1 if b%2==0 else -1))
          for b in range(-100,101))
    mc=matrix_check()
    facts['independent_density_matches_normalized_Hodge_action']=mc[0]
    facts['no_untyped_slot_identity']=mc[1]
    facts['integration_by_parts_derivative_sign']=mc[2]
    hi={'1':-1,'2':2,'3':2,'4':-1,'5':-1,'6':-1}
    facts['tensor_higher_net_profile']=all(profiles(n)==hi for n in (2,3,9))
    facts['tensor_first_endpoint']=profiles(1)=={**hi,'1':0}
    facts['tensor_zero_flux']=all(v==0 for v in gauge_indices(0).values())
    facts['all_flux_conjugation']=all(profiles(-n)=={
        k:-v for k,v in profiles(n).items()} for n in (1,2,9))
    facts['higher_anomaly_coefficients']=anomalies(2)==['-3','-6','-6','-1008','-30']
    facts['first_anomaly_coefficients']=anomalies(1)==['-1','-5','-9/2','-1002','-24']
    facts['conjugate_and_zero_anomaly']=anomalies(0)==['0']*5 and all(
        list(map(F,anomalies(-n)))==[-F(x) for x in anomalies(n)] for n in (1,2,9))
    facts['all_integer_weight_inequality']=all(m+2*abs(q)>=0 and m+4*abs(q)>0
        for a,b,w,q,m in weights if q)
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
       'net_multiplicities':{str(n):profiles(n) for n in range(-3,4)},
       'anomaly_vectors':{str(n):anomalies(n) for n in range(-3,4)},
       'weight_roster':[list(k)+[v] for k,v in sorted(weights.items())],
       'nonauthor_acceptance':False}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
