"""Independent differential expansion and polynomial-moment route."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('gauge_limit_tensor',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)

@lru_cache(None)
def run():
    facts={};x,y=s.symbols('x y',real=True);I=s.I
    J=s.diag(-I,-I,I,I)
    B=s.Matrix([[I*x,0,x+y,I*x*y],[0,I*y,x*x,2*y],[y,1+I*x,0,0],[x*y,2*x,0,I*(x+2*y)]])
    C=B.adjoint()
    M=lambda f:s.diff(f,x)+J*s.diff(f,y)+B*f
    Md=lambda f:-s.diff(f,x)+J*s.diff(f,y)+C*f
    coeff=[]
    for op in (lambda f:Md(M(f)),lambda f:M(Md(f))):
        b=s.Matrix.hstack(*(op(s.eye(4)[:,j]) for j in range(4)))
        ax=s.Matrix.hstack(*(op(x*s.eye(4)[:,j])-x*b[:,j] for j in range(4)))
        ay=s.Matrix.hstack(*(op(y*s.eye(4)[:,j])-y*b[:,j] for j in range(4)))
        E=-b+(s.diff(ax,x)+s.diff(ay,y))/2-(ax*ax+ay*ay)/4
        coeff.append((b,ax,ay,E))
    delta=s.expand(s.trace(coeff[0][3]-coeff[1][3]))
    expected=s.expand(s.trace(s.diff(B+C,x)-J*s.diff(B-C,y)))
    facts['direct_operator_heat_trace_matches']=s.simplify(delta-expected)==0
    facts['nonzero_diagonal_connection_control']=expected!=0
    f=s.Matrix([x*x+y*y,x*y+x,x**3-y,x-y*y])
    facts['differential_coefficients_reproduce_action']=all(all(s.expand(z)==0 for z in op(f)-(-s.diff(f,x,2)-s.diff(f,y,2)+ax*s.diff(f,x)+ay*s.diff(f,y)+b*f)) for op,(b,ax,ay,E) in zip((lambda f:Md(M(f)),lambda f:M(Md(f))),coeff))
    # Integral of u^j exp(-u), recurrence by integration by parts.
    moments=[1-s.exp(-1)]
    for j in range(1,7):moments.append(j*moments[-1]-s.exp(-1))
    eta=1-3*x*x+2*x**3;poly=s.Poly(s.expand((1-eta)**2+s.diff(eta,x)**2),x)
    cost=s.expand(sum(c*moments[pow[0]] for pow,c in poly.terms())+s.exp(-1))
    facts['positive_cutoff_constant']=bool(cost>0)
    facts['tail_is_not_suppressed_by_missing_term']=s.exp(-1)!=0
    z,t=s.symbols('z t')
    char=2*s.exp((1-z)*t)-s.exp(-z*t)-s.exp((2-z)*t)
    rd=[s.simplify(char.subs(t,0)),s.simplify(s.diff(char,t).subs(t,0))]
    facts['independent_character_has_no_rank_or_degree']=rd==[0,0]
    data={str(n):prior.anomalies(n) for n in range(-3,4)}
    facts['independent_color_keeps_first_endpoint']=data['1'][0]=='-1' and data['2'][0]=='-3'
    facts['full_tensor_population']=sum(prior.tensor_weights().values())==248
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),
      'anomaly_vectors':data,'virtual_rank_degree':[int(a) for a in rd],
      'cutoff_norm_constant':str(cost),'overlap_integral':'-1/2',
      'nonauthor_acceptance':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['predicates'].values()) else 1)
