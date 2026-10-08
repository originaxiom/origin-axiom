"""Actual four-Weyl mass map, complete charged index, anomaly diagnostic."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

Q=s.Rational
path=Path(__file__).resolve().parent.parent/'weave_two_neutral_index_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('physical_mass_two_neutral',path)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
mag=old.magnetic
zero=mag.zero
comm=mag.comm

def mass(q,r,p,om):
    n=q.rows;I=s.eye(n);O=s.zeros(n);sq=s.sqrt(2);pc=s.conjugate(p)
    return s.BlockMatrix([
        [O,pc*I/(sq*om**2),sq*s.I*q.adjoint()/om,sq*s.I*r.adjoint()/om],
        [-sq*pc*I,O,-2*s.I*r,2*s.I*q],
        [-sq*s.I*q.adjoint(),s.I*r/om,O,p*I/om],
        [-sq*s.I*r.adjoint(),-s.I*q/om,-p*I/om,O]]).as_explicit()

def maps(q,r,p,om):
    n=q.rows;I=s.eye(n);O=s.zeros(n)
    d0,d1,d2=old.complex_matrices(q,r,p)
    h0=om**2*I;h1=s.diag(I/2,om*I,om*I)
    h2=s.diag(I/om,I/om,2*I);h3=2*I/om**2
    a0=h0.inv()*d0.adjoint()*h1
    a2=h2.inv()*d2.adjoint()*h3
    T=s.Matrix.vstack(s.Matrix.hstack(a0,O),s.Matrix.hstack(d1,a2))
    U=s.BlockMatrix([[O,I,O,O],[O,O,I,O],[O,O,O,I],
                     [s.I*om**2*I/s.sqrt(2),O,O,O]]).as_explicit()
    V=s.BlockMatrix([[I,O,O,O],[O,O,O,2*s.I*I],
                     [O,O,I/om,O],[O,-I/om,O,O]]).as_explicit()
    hf=s.diag(h0,h1)
    return T,U,V,hf,s.diag(h1,h3),s.diag(h0,h2)

@lru_cache(None)
def operator_checks():
    om=s.Integer(3);p=2+3*s.I
    q=s.Matrix([[1+s.I,2],[0,1+s.I]])
    results=[]
    for r in ((2-s.I)*s.eye(2),s.Matrix([[0,0],[1,0]])):
        T,U,V,hf,hs,ht=maps(q,r,p,om);M=mass(q,r,p,om)
        B=hf*M
        Md=mass(-q.T,-r.T,-p,om)
        results.append({
            'map':zero(M-V*T*U),
            'input_unitary':zero(U.adjoint()*hs*U-hf),
            'output_unitary':zero(V.adjoint()*hf*V-ht),
            'transpose':zero(B-(hf*Md).T),
            'norm_square':zero(s.simplify(M.adjoint()*hf*M-
                          U.adjoint()*T.adjoint()*ht*T*U)),
            'wrong_dual_fails':not zero(B-(hf*mass(q,r,-p,om)).T),
            'no_R_fails':not zero(M-mass(q,s.zeros(2),p,om)),
            'wrong_input_phase_fails':not zero(M-V*T*
                            (U*s.diag(-s.I*s.eye(2),s.eye(6)))),
            'wrong_metric_fails':not zero(U.adjoint()*(2*hs)*U-hf)
        })
    return {key:all(row[key] for row in results) for key in results[0]}

@lru_cache(None)
def hessian_checks():
    x,t,h=s.symbols('x t h',real=True)
    E=lambda i,j: s.eye(3)[:,i]*s.eye(3)[j,:]
    A=E(0,1)+E(1,0)
    q=E(1,2)+(1+s.I)*E(2,0)
    r=E(2,1)+2*E(0,2)
    f=x*(1-x)
    a=f*(E(0,2)+s.I*E(1,0));u=f*(E(2,1)+E(0,1))
    v=f*x*(E(1,2)+2*s.I*E(2,0))
    b=f*x*(E(1,0)+E(2,1));w=f*(E(2,0)+s.I*E(0,2))
    z=f*(1+x)*(E(0,1)+E(1,2))
    D=lambda X:s.diff(X,x)-s.I*comm(A,X)
    p1=D(u)+s.I*comm(q,a);p2=D(v)+s.I*comm(r,a)
    tt=comm(q,v)-comm(r,u)
    H=s.trace(s.I*b*tt+w*p2-z*p1)
    W=lambda AA,qq,rr:s.trace(qq*(s.diff(rr,x)-s.I*comm(AA,rr))-
                   rr*(s.diff(qq,x)-s.I*comm(AA,qq)))/2
    expanded=s.expand(W(A+t*a+h*b,q+t*u+h*w,r+t*v+h*z))
    coeff=expanded.coeff(t,1).coeff(h,1)
    swapped=s.trace(s.I*a*(comm(q,z)-comm(r,w))+
                u*(D(z)+s.I*comm(r,b))-v*(D(w)+s.I*comm(q,b)))
    integrate=lambda value:s.simplify(s.integrate(s.expand(value),(x,0,1)))
    wrong=s.trace(s.I*b*(comm(q,v)+comm(r,u))+w*p2-z*p1)
    return {'full_W_hessian':integrate(coeff-H)==0,
            'symmetric_bilinear':integrate(H-swapped)==0,
            'nonzero_vertex':integrate(H)!=0,
            'wrong_mixed_sign_fails':integrate(wrong-H)!=0,
            'boundary_profiles_zero':all(z.subs(x,e)==s.zeros(3)
                      for z in (a,u,v,b,w,z) for e in (0,1))}

def full_weights():
    c1=(1,-1,0,0,0,0,0,0);c2=(0,1,-1,0,0,0,0,0)
    weak=(Q(1,2),)*8
    out=Counter((int(mag.dot(c1,r)),int(mag.dot(c2,r)),
                 int(mag.dot(weak,r)),int(mag.dot(mag.Z,r)),
                 int(mag.dot(mag.W,r))) for r in mag.roots())
    out[0,0,0,0,0]+=8
    return out

FUND=((1,0),(-1,1),(0,-1))
ANTI=tuple((-a,-b) for a,b in FUND)
REP={
  1:[(a,b,w) for a,b in FUND for w in (-1,1)],
  2:[(a,b,0) for a,b in ANTI],
  3:[(0,0,w) for w in (-1,1)],
  4:[(a,b,0) for a,b in FUND],
  5:[(a,b,w) for a,b in ANTI for w in (-1,1)],
  6:[(0,0,0)]}

def gauge_weight_indices(n):
    out=Counter()
    for (a,b,w,q,m),mult in full_weights().items():
        out[a,b,w,q]+=mult*old.line_index(m+2*n*q)
    return out

def net_multiplicities(n):
    ww=gauge_weight_indices(n)
    out={}
    for q,rr in REP.items():
        vals={ww[a,b,w,q] for a,b,w in rr}
        if len(vals)!=1:raise ValueError('nonuniform physical representation')
        out[str(q)]=vals.pop()
    return out

def anomaly(n,positive_only=False,drop_charge=None):
    vals=[s.Integer(0)]*5
    for (a,b,w,q,m),mult in full_weights().items():
        if positive_only and q<=0:continue
        if drop_charge is not None and abs(q)==drop_charge:continue
        nu=mult*old.line_index(m+2*n*q)
        terms=[Q((a+2*b)**3,-6),Q(a*a*q,4),Q(w*w*q,4),q**3,q]
        for i,value in enumerate(terms):vals[i]+=nu*value
    factor=1 if positive_only else Q(1,2)
    return [s.simplify(factor*x) for x in vals]

def simple_anomaly(rows):
    # nu,color dimension,color cubic sign,weak dimension,Z
    vals=[s.Integer(0)]*5
    for nu,d3,sign,d2,q in rows:
        terms=[d2*sign,Q(d2*q,2) if d3==3 else 0,
               Q(d3*q,2) if d2==2 else 0,d3*d2*q**3,d3*d2*q]
        vals=[a+nu*b for a,b in zip(vals,terms)]
    return vals

@lru_cache(None)
def run():
    facts={}
    facts.update(operator_checks());facts.update(hessian_checks())
    y=s.symbols('y',positive=True);om=s.Function('om')(y)
    lam=s.Function('lam')(y);sig=s.I*om**2*lam/s.sqrt(2)
    facts['variable_metric_derivative_cancels']=s.simplify(
        -2*s.I*s.diff(sig/om**2,y)-s.sqrt(2)*s.diff(lam,y))==0
    facts['derivative_before_metric_cancellation_is_wrong']=s.simplify(
        -2*s.I*s.diff(sig,y)/om**2-s.sqrt(2)*s.diff(lam,y))!=0
    Z=s.diag(1,1,-2);e=s.zeros(3);e[0,1]=1
    facts['neutral_gaugino_not_quotiented_out']=zero(comm(Z,e)) and zero(
        comm(Z,e.adjoint())) and zero(comm(Z,(2+s.I)*Z))
    ww=full_weights()
    facts['full248_and_all_charge_pairs']=sum(ww.values())==248 and all(
        ww[tuple(-x for x in key)]==mult for key,mult in ww.items())
    # Reconstruct the whole root population as actual SM weights times
    # the internal modules, then the neutral representations explicitly.
    charged=Counter()
    for q,rr in REP.items():
        js=(1,3) if q in (2,3) else (0,) if q==5 else (2,)
        for a,b,w in rr:
            for j in js:
                for m in range(-j,j+1):
                    charged[a,b,w,q,m]+=1
                    charged[-a,-b,-w,-q,-m]+=1
    facts['every_charged_weight_has_actual_representation']=Counter({
        key:mult for key,mult in ww.items() if key[3]})==charged
    hi={'1':-1,'2':2,'3':2,'4':-1,'5':-1,'6':-1}
    lo={**hi,'1':0}
    facts['higher_flux_full_net_multiplicities']=all(net_multiplicities(n)==hi
                                                   for n in (2,3,7))
    facts['first_flux_endpoint_retained']=net_multiplicities(1)==lo
    facts['zero_flux_charged_index_zero']=all(v==0 for v in gauge_weight_indices(0).values())
    facts['opposite_flux_reverses_net']=all(net_multiplicities(-n)=={
        q:-v for q,v in net_multiplicities(n).items()} for n in (1,2,3,7))
    facts['all_integer_scope_weight_bound']=all(m+2*abs(q)>=0
                       and m+4*abs(q)>0 for a,b,w,q,m in ww if q)
    facts['physical_index_matches_whole_Hodge_index']=all(
        {q:sum(v for (a,b,w,z),v in gauge_weight_indices(n).items() if z==q)
         for q in range(-6,7)}==old.charge_indices(n) for n in (-3,-2,-1,0,1,2,3))
    expected_hi=[-3,-6,-6,-1008,-30]
    expected_lo=[-1,-5,Q(-9,2),-1002,-24]
    facts['higher_flux_anomaly_vector']=all(anomaly(n)==expected_hi for n in (2,3,7))
    facts['first_flux_anomaly_vector']=anomaly(1)==expected_lo
    facts['opposite_and_zero_anomaly_controls']=anomaly(0)==[0]*5 and all(
        anomaly(-n)==[-v for v in anomaly(n)] for n in (1,2,3,7))
    facts['one_per_conjugate_pair_not_double']=all(
        anomaly(n)==anomaly(n,positive_only=True) for n in (1,2,3))
    facts['exotic_cannot_be_deleted']=anomaly(2,drop_charge=5)!=anomaly(2)
    sm=[(1,3,1,2,1),(1,3,-1,1,-4),(1,3,-1,1,2),
        (1,1,0,2,-3),(1,1,0,1,6)]
    facts['one_standard_generation_anomaly_control']=simple_anomaly(sm)==[0]*5
    facts['vector_pair_anomaly_control']=simple_anomaly(
        [(1,3,1,2,5),(1,3,-1,2,-5)])==[0]*5
    facts['wrong_double_count_fails']=anomaly(2)!=[2*v for v in anomaly(2)]
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
        'net_multiplicities':{str(n):net_multiplicities(n) for n in range(-3,4)},
        'anomaly_vectors':{str(n):[str(v) for v in anomaly(n)] for n in range(-3,4)},
        'weight_roster':[list(k)+[v] for k,v in sorted(ww.items())],
        'physical_mass_identification_derived':True,
        'conditional_charged_index_computed':True,
        'full_kernel_multiplicities_computed':False,
        'anomaly_completion_derived':False,'stable_magnetic_vacuum_derived':False,
        'genesis_selection_derived':False,'nonauthor_acceptance':False,
        'physical_goal_achieved':False,
        'analytic_grade':'Authored complete-domain dictionary; not independently accepted'}

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
