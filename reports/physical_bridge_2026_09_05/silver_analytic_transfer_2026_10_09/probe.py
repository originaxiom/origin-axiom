"""Exact inputs for analytic silver transfer; no completed physical boundary."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from math import comb
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
c=load('analytic_cyclic_native',HERE.parent/'silver_cyclic_transfer_2026_10_06/probe.py')

def pairs(z):
    z=s.expand(z);b=z.coeff(s.sqrt(2));a=s.expand(z-b*s.sqrt(2))
    assert a.is_Rational and b.is_Rational
    return a,b

def bound(a):
    return sum(abs(x)+2*abs(y) for x,y in map(pairs,a))

def powers(a):
    out=[s.eye(a.rows)]
    for _ in range(a.rows):
        nxt=c.mm(out[-1],a)
        if c.zero(nxt):return out
        out.append(nxt)
    raise ValueError('not nilpotent')

def coefficient(v):
    out=s.zeros(5)
    for z,x in zip(v,c.adjoint_basis()):out+=z*x
    return c.norm(out)

def coords(a):
    return s.Matrix([a[i,j] for i in range(5) for j in range(5) if i!=j]+[a[i,i] for i in range(4)])

def quadratic(x,y):
    a,b=coefficient(x[:24,0]),coefficient(y[24:,0])
    return coords(c.mm(a,b)-c.mm(b,a))

def encoded(matrices):
    body=[[[str(a),str(b)] for a,b in map(pairs,v)] for v in matrices]
    return hashlib.sha256(json.dumps(body,separators=(',',':')).encode()).hexdigest()

def catalans(limit):
    out=[1]
    for n in range(1,limit+1):out.append(sum(out[j]*out[n-1-j] for j in range(n)))
    return out

@lru_cache(None)
def run():
    facts={};blocks={};orders={};h_bounds={};inv_bounds={}
    def ck(key,val):
        facts[key]=bool(val)
        assert facts[key],key
    old,data,w,P,Q,A,B=c.literal()
    ck('literal_peripheral_logs_and_relators',c.exp_nil(A)==P and c.exp_nil(B)==Q and
       all(c.word(w,r)==s.eye(5) for r in data['relators']) and c.zero(c.mm(A,B)-c.mm(B,A)))
    basis=c.adjoint_basis()
    metric=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    trace=s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    ck('neutral_metric_bound_is_earned',metric==s.diag(s.eye(20),s.eye(4)+s.ones(4)) and
       sorted(metric.eigenvals().items())==[(s.Integer(1),23),(s.Integer(5),1)])
    logs={'W':(A,B),'Wdual':(-A.T,-B.T),
          'F':(c.exterior_lie(A),c.exterior_lie(B)),
          'Fdual':(-c.exterior_lie(A).T,-c.exterior_lie(B).T),
          'N':(c.adjoint_lie(A,basis),c.adjoint_lie(B,basis)),
          'gauge':(s.zeros(1),s.zeros(1))}
    for name,(a,b) in logs.items():
        E=c.sdr(a,b,metric if name=='N' else None);blocks[name]=E
        d,h,p=E['d'],E['h'],E['p'];identity=s.eye(d.rows)
        ck(name+'_exact_SDR',c.zero(c.mm(d,h)+c.mm(h,d)-(identity-p)) and
           c.zero(c.mm(h,h)) and c.zero(c.mm(h,p)) and c.zero(c.mm(p,h)))
        ck(name+'_wrong_homotopy_sign_rejected',c.zero(d) if name=='gauge' else
           not c.zero(-c.mm(d,h)-c.mm(h,d)-(identity-p)))
        pp=[powers(x) for x in (a,b)]
        orders[name]=[len(x) for x in pp]
        ck(name+'_finite_inverse_last_term_is_needed',all(not c.zero(x[-1]) for x in pp))
        h_bounds[name]=3*bound(h)
        inv_bounds[name]=max(3*sum(bound(v)/s.Integer(6)**(j+1) for j,v in enumerate(x)) for x in pp)
    for name in ('W','F'):
        ck(name+'_cyclic_for_actual_dual',all(c.cyclic_residual(blocks[name],blocks[name+'dual']).values()))
    for name,g in (('N',trace),('gauge',s.eye(1))):
        ck(name+'_cyclic_for_actual_trace',all(c.cyclic_residual(blocks[name],trace=g).values()))
    C0=max(h_bounds.values());C1=max(inv_bounds.values());C=max(1,C0,C1)
    ck('positive_finite_uniform_homotopy_bound',all(x>=0 and x.is_Rational for x in h_bounds.values()) and C>=1 and C1>0)
    mult={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(mult[k]*blocks[k]['betti'][j] for k in mult) for j in range(3)]
    ck('full_248_and_harmonic_roster',sum(mult[k]*blocks[k]['n'] for k in mult)==248 and H==[100,200,100])
    cat=catalans(32)
    ck('catalan_recursion_matches_closed_formula',cat==[comb(2*n,n)//(n+1) for n in range(33)])
    ck('tree_majorant_geometric_bound',all(cat[n]<=4**n for n in range(33)))
    rho,eps=s.symbols('rho eps',positive=True)
    # At epsilon=1/(8rho), radius R=2epsilon: image and derivative bounds.
    e=1/(8*rho);R=2*e
    ck('contraction_ball_and_lipschitz_margin',s.simplify(e+rho*R**2/2-R)<0 and s.simplify(rho*R)==s.Rational(1,4))
    ck('oversized_ball_is_not_certified',s.simplify(rho*(2/rho))>1)

    E=blocks['N'];n=24
    h2=E['h'][n:3*n,3*n:];h1=E['h'][:n,n:3*n]
    p2=E['p'][3*n:,3*n:];p1=E['p1'];d1=E['d1']
    jets=[];curves=[];profiles=[];all_slice=[];all_curvature=[]
    for j in range(4):
        eta=c.mm(p1,s.Matrix([((i+3*j)**2 % 7)-3 for i in range(48)]))
        aa=[s.zeros(48,1),eta];kk=[s.zeros(24,1),s.zeros(24,1)]
        for r in range(2,5):
            q=sum((quadratic(aa[i],aa[r-i]) for i in range(1,r)),s.zeros(24,1))
            ar=-c.mm(h2,q);kr=c.mm(p2,q)
            aa.append(ar);kk.append(kr)
            all_slice.append(c.zero(c.mm(h1,ar)) and c.zero(c.mm(p1,ar)))
            all_curvature.append(c.zero(c.mm(d1,ar)+q-kr))
        ck('neutral_harmonic_input_'+str(j),c.zero(c.mm(d1,eta)) and c.zero(c.mm(h1,eta)) and c.mm(p1,eta)==eta)
        jets.append(aa[1:]);curves.append(kk[1:])
        profiles.append(dict(nonzero_corrections=[not c.zero(x) for x in aa[2:]],
          nonzero_obstructions=[not c.zero(x) for x in kk[2:]],
          exact_jet_sha256=encoded(aa[1:]+kk[1:])))
    ck('neutral_jets_obey_Kuranishi_slice',all(all_slice))
    ck('neutral_curvature_is_harmonic_through_order4',all(all_curvature))
    V=s.Matrix.hstack(*(x for jet in jets for x in jet))
    J=s.zeros(24).row_join(trace).col_join((-trace).row_join(s.zeros(24)))
    O=c.mm(c.mm(V.T,J),V)
    ck('neutral_jet_pairings_preserve_harmonic_form',all(O[i,j]==0 for i in range(16) for j in range(16) if i%4 or j%4))
    x=s.zeros(5);x[0,1]=1
    y=s.zeros(5);y[1,0]=1
    z=s.zeros(5);z[0,2]=1
    comm=c.mm(x,y)-c.mm(y,x)
    ck('analytic_lift_is_not_automatically_flat',comm==s.diag(1,-1,0,0,0))
    ck('commuting_flat_control_retains_bracket',c.zero(c.mm(x,z)-c.mm(z,x)) and not c.zero(comm))
    return dict(facts=facts,predicates_passed=len(facts),nilpotence_orders=orders,
      homotopy_bounds={k:str(v) for k,v in h_bounds.items()},
      inverse_bounds={k:str(v) for k,v in inv_bounds.items()},
      global_bounds=dict(C0=str(C0),C1=str(C1),c=str(C)),
      full_harmonic_dimensions=H,neutral_jets=profiles,
      some_neutral_nonlinear_correction=any(any(x['nonzero_corrections']) for x in profiles),
      full_canonical_boundary_convergence=False,all_harmonic_inputs_flat=False,
      boundary_selected=False,stationary_chiral_completion=False,
      full_E8_structure_constants_recomputed=False,nonauthor_acceptance=False,
      physical_goal_achieved=False)

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
