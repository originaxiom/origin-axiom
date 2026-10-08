"""Paired Gaussian and exact nonabelian descent controls; not a full determinant."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
import importlib.util
import json
from pathlib import Path
import sympy as s

path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('paired_phase_physical',path)
physical=importlib.util.module_from_spec(spec);spec.loader.exec_module(physical)
Q=s.Rational
DEG={'a':1,'f':2,'u':0,'U':1,'v':0,'V':1}
clean=lambda p:{w:s.expand(c) for w,c in p.items() if s.expand(c)!=0}
def add(*polys):
    p=defaultdict(lambda:s.S.Zero)
    for poly in polys:
        for w,c in poly.items():p[w]+=c
    return clean(p)
def scale(p,c):return clean({w:c*v for w,v in p.items()})
def mul(p,q):
    out=defaultdict(lambda:s.S.Zero)
    for w,c in p.items():
        for z,b in q.items():out[w+z]+=c*b
    return clean(out)
def word(*w):return {tuple(w):s.S.One}
def degree(w):return sum(DEG[x] for x in w)
def derivative(p):
    out={};dm={'a':'f','u':'U','v':'V'}
    for w,c in p.items():
        for j,x in enumerate(w):
            if x in dm:out=add(out,{w[:j]+(dm[x],)+w[j+1:]:c*(-1)**degree(w[:j])})
    return out
def trace(p):
    out={}
    for w,c in p.items():
        if not w:out=add(out,{w:c});continue
        rotations=[(w[j:]+w[:j],(-1)**(degree(w[:j])*degree(w[j:]))) for j in range(len(w))]
        key=min(k for k,sgn in rotations);signs={sgn for k,sgn in rotations if k==key}
        if len(signs)==1:out=add(out,{key:c*next(iter(signs))})
    return out
def variation(p,parameter):
    dp={'u':'U','v':'V'}[parameter]
    da=add(word(dp),word('a',parameter),scale(word(parameter,'a'),-1))
    rules={'a':da,'f':derivative(da)};out={}
    for w,c in p.items():
        for j,x in enumerate(w):
            if x in rules:out=add(out,scale(mul(mul(word(*w[:j]),rules[x]),word(*w[j+1:])),c))
    return out
def anomaly(parameter,cubic=Q(1,2),covariant=False):
    if covariant:
        curv=add(word('f'),word('a','a'));body=mul(curv,curv)
    else:body=derivative(add(word('a','f'),scale(word('a','a','a'),cubic)))
    return mul(parameter,body)
def residual(cubic=Q(1,2),covariant=False):
    bracket=add(word('u','v'),scale(word('v','u'),-1))
    return trace(add(variation(anomaly(word('v'),cubic,covariant),'u'),
       scale(variation(anomaly(word('u'),cubic,covariant),'v'),-1),
       scale(anomaly(bracket,cubic,covariant),-1)))
@lru_cache(None)
def exact_columns():
    cols={}
    for size in range(2,6):
        for w in product(DEG,repeat=size):
            if degree(w)!=3 or sum(x in ('u','U') for x in w)!=1 or sum(x in ('v','V') for x in w)!=1:continue
            canonical=trace(word(*w))
            if not canonical:continue
            key=next(iter(canonical));d=trace(derivative(word(*key)))
            if d:cols[key]=d
    return cols
def exact_witness(poly):
    cols=exact_columns();keys=sorted(cols);rows=sorted(set(poly).union(*(set(v) for v in cols.values())))
    B=s.Matrix([[cols[k].get(w,0) for k in keys] for w in rows]);v=s.Matrix([poly.get(w,0) for w in rows])
    if B.rank()!=B.row_join(v).rank():return None
    solution,params=B.gauss_jordan_solve(v);solution=solution.subs({x:0 for x in params})
    witness={keys[j]:x for j,x in enumerate(solution) if x}
    assert trace(derivative(witness))==poly
    return witness
def reflect(v):
    v=s.Matrix(v);return s.eye(len(v))-2*v*v.T/(v.dot(v))
def polar_control():
    left=reflect([2,0,1,1,3]);right=reflect([1,2,3,4]);B=s.zeros(5,4);E=s.zeros(5,4)
    for i,m in enumerate((2,3,5)):B[i,i]=m;E[i,i]=1
    M=left*B*right.T;U=left*E*right.T;T=right*s.diag(2,3,5,0)*right.T
    return M,U,T,right
zero=lambda a:all(s.simplify(x)==0 for x in a)
def vectors():return {str(n):[str(x) for x in physical.anomaly(n)] for n in range(-3,4)}
@lru_cache(None)
def run():
    facts={};M,U,T,R=polar_control();pp=s.eye(4)-U.T*U;pm=s.eye(5)-U*U.T
    facts['actual_rectangular_polar_factorization']=zero(M-U*T) and zero(M.T*M-T*T)
    facts['both_kernel_projectors_retained']=zero(pp*pp-pp) and zero(pm*pm-pm) and zero(M*pp) and zero(M.T*pm)
    facts['kernel_minus_cokernel_not_pair_count']=pp.trace()==1 and pm.trace()==2 and pp.trace()-pm.trace()==-1
    facts['target_positive_square_intertwines']=zero(M*M.T-U*T*T*U.T)
    col=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
    facts['polar_map_keeps_complete_gauge_representation']=zero(s.kronecker_product(s.eye(5),col)*s.kronecker_product(U,s.eye(3))-s.kronecker_product(U,s.eye(3))*s.kronecker_product(s.eye(4),col))
    E=R*s.Matrix([[Q(3,5),0],[0,1],[Q(4,5),0],[0,0]]);TN=E.T*T*E
    facts['paired_compression_comes_from_mass_action']=zero((U*E).T*M*E-TN) and zero(E.T*E-s.eye(2))
    facts['compression_positive_not_commuting_assumption']=TN==s.diag(Q(98,25),3) and not zero(E*E.T*T-T*E*E.T)
    facts['unmatched_target_compression_detected']=not zero(E.T*M[:4,:]*E-TN)
    m=s.symbols('m',positive=True);b=s.Matrix([[1,1+s.I],[0,2]]);O=s.zeros(2)
    H=s.BlockMatrix([[O,b.adjoint()],[b,O]]).as_explicit();G=s.diag(1,1,-1,-1)
    determinant=s.expand((m*s.eye(4)+s.I*H).det())
    facts['massive_actual_gaussian_block']=zero(H.adjoint()-H) and zero(H*G+G*H) and s.simplify(determinant-(m*m*s.eye(2)+b.adjoint()*b).det())==0
    facts['positive_mass_has_no_gauge_phase']=determinant==m**4+7*m*m+4 and all(c>0 for c in s.Poly(determinant,m).all_coeffs() if c)
    C=s.diag(1,s.I,-1,-s.I)
    facts['vector_gauge_similarity_preserves_gaussian']=s.simplify((C*(m*s.eye(4)+s.I*H)*C.adjoint()).det()-determinant)==0
    facts['one_spectral_sign_is_not_a_dirac_pair']=s.im(m+s.I)!=0
    facts['d_squared_and_signed_cyclic_controls']=not derivative(derivative(word('u','a','v','a'))) and not trace(word('a','a')) and trace(word('u','a'))==trace(word('a','u'))
    res=residual();wit=exact_witness(res)
    facts['consistent_nonabelian_residual_is_exact']=wit is not None and bool(res) and trace(derivative(wit))==res
    facts['wrong_cubic_coefficient_fails']=exact_witness(residual(0)) is None
    facts['covariant_polynomial_is_not_consistent']=exact_witness(residual(covariant=True)) is None
    facts['full248_gauge_weight_population']=sum(physical.full_weights().values())==248
    facts['color_nonzero_with_first_flux_endpoint']=physical.anomaly(1)[0]==-1 and physical.anomaly(2)[0]==-3
    facts['all_opposite_and_zero_indices_kept']=physical.anomaly(0)==[0]*5 and all(physical.anomaly(-n)==[-x for x in physical.anomaly(n)] for n in (1,2,3))
    facts['exotic_cannot_be_discarded']=physical.anomaly(2,drop_charge=5)!=physical.anomaly(2)
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),'anomaly_vectors':vectors(),
      'polar_kernel_dimensions':[int(pp.trace()),int(pm.trace())],
      'massive_gaussian_polynomial':str(determinant),
      'consistent_residual':{' '.join(k):str(v) for k,v in sorted(res.items())},
      'exact_form_witness':None if wit is None else {' '.join(k):str(v) for k,v in sorted(wit.items())},
      'phase_prescription_is_supplied':True,'internally_local_regulator_derived':False,
      'gauge_invariant_nonzero_flux_phase':False,'full_quantum_action_derived':False,
      'all_quantum_completions_excluded':False,'nonauthor_acceptance':False,'physical_goal_achieved':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['facts'].values()) else 1)
