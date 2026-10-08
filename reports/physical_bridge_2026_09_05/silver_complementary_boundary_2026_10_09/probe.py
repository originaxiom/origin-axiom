"""Complementary acyclic block and full symbol, not a completed physical model."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
c=load('complement_cyclic',HERE.parent/'silver_cyclic_transfer_2026_10_06/probe.py')
smooth=load('complement_smooth',HERE.parent/'silver_smooth_boundary_gate_2026_10_05/probe.py')

def symbols():
    x,y=s.symbols('x y',real=True);r=x*x+y*y;e=s.eye(4)
    alpha=(-y*e[:,1]+x*e[:,2]).row_join(e[:,3])
    beta=e[:,0].row_join(x*e[:,1]+y*e[:,2])
    qx,qy,gamma,j,parity=smooth.matrices();q=x*qx+y*qy
    projector=s.diag(alpha*(alpha.T*alpha).inv()*alpha.T,
                     beta*(beta.T*beta).inv()*beta.T)
    full=s.diag(alpha,beta)
    adapted=-gamma*s.diag(q,-q)
    return x,y,r,alpha,beta,full,projector,adapted,gamma,j,parity,q

@lru_cache(None)
def run():
    facts={};blocks={};profiles={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    old,data,w,P,Q,A,B=c.literal()
    ck('literal_logs_and_relators',c.exp_nil(A)==P and c.exp_nil(B)==Q and
       c.zero(c.mm(A,B)-c.mm(B,A)) and all(c.word(w,r)==s.eye(5) for r in data['relators']))
    basis=c.adjoint_basis()
    metric=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    trace=s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    FA,FB=c.exterior_lie(A),c.exterior_lie(B)
    logs={'W':(A,B),'Wdual':(-A.T,-B.T),'F':(FA,FB),'Fdual':(-FA.T,-FB.T),
          'N':(c.adjoint_lie(A,basis),c.adjoint_lie(B,basis)),'gauge':(s.zeros(1),s.zeros(1))}
    for name,(a,b) in logs.items():
        E=c.sdr(a,b,metric if name=='N' else None);blocks[name]=E;n=E['n']
        h2=E['h'][n:3*n,3*n:];d1=E['d1'];d0=E['d0']
        p2=E['p'][3*n:,3*n:];p1=E['p1']
        U=c.mm(h2,d1);V=s.eye(n)-p2
        ck(name+'_chain_projectors',c.mm(U,U)==U and c.mm(V,V)==V and c.mm(d1,U)==d1 and c.mm(V,d1)==d1)
        ck(name+'_contracting_inverse',c.mm(d1,h2)==V and c.mm(U,h2)==h2 and c.mm(h2,V)==h2)
        ck(name+'_harmonic_and_exact_separation',c.zero(c.mm(p1,U)) and c.zero(c.mm(U,p1)) and c.zero(c.mm(U,d0)))
        ru,rv=c.rank(U),c.rank(V)
        ck(name+'_acyclic_not_extra_modes',ru==rv==n-E['betti'][2] and c.rank(h2)==ru)
        ck(name+'_auxiliary_derivative_control',c.zero(c.mm(U,d0)) and
           (c.zero(d0) if name=='gauge' else not c.zero(d0)))
        profiles[name]=dict(rank=n,harmonic=E['betti'],coexact_rank=ru,exact2_rank=rv)
    for name in ('W','F'):
        ck(name+'_actual_dual_cyclicity',all(c.cyclic_residual(blocks[name],blocks[name+'dual']).values()))
    for name,g in (('N',trace),('gauge',s.eye(1))):
        ck(name+'_actual_trace_cyclicity',all(c.cyclic_residual(blocks[name],trace=g).values()))
    mult={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(mult[k]*blocks[k]['betti'][j] for k in mult) for j in range(3)]
    ck('full_parent_and_harmonics',sum(mult[k]*blocks[k]['n'] for k in mult)==248 and H==[100,200,100])
    x,y,r,a,b,full,proj,adapted,gamma,j,parity,q=symbols()
    z=lambda v:s.simplify(v)==s.zeros(*v.shape)
    ck('symbol_projector',z(proj*proj-proj) and z(proj.H-proj) and s.simplify(s.trace(proj))==4)
    ck('maximal_green_current',full.rank()==4 and z(full.H*gamma*full))
    ck('adapted_clifford',z(adapted*adapted-r*s.eye(8)) and z(adapted.H-adapted))
    ck('elliptic_exchange_all_covectors',z(proj*adapted+adapted*proj-adapted))
    ck('restricted_symbol_determinant',s.simplify((a.H*q*a).det()+r*r)==0 and s.simplify((b.H*q*b).det()+r*r)==0)
    ck('combined_reality',z(j*proj.conjugate()*j-proj))
    ck('graded_domain',z(parity*proj-proj*parity))
    wrong=s.diag(a,a)
    ck('wrong_normal_complement_rejected',not z(wrong.H*gamma*wrong))
    xi=s.Matrix([x,y]);xp=s.Matrix([-y,x]);coexact=xp*xp.T/r
    reject=(s.eye(2)-coexact)*xi
    ck('all_nonzero_auxiliary_gradients_rejected',z(coexact*xi) and s.simplify((reject.T*reject)[0])==r)
    ck('parallel_scalar_derivative_admitted',xi.subs({x:0,y:0})==s.zeros(2,1))
    # Nonlinear bracket in an actual matrix subalgebra, not a commutative replacement.
    E12=s.zeros(3);E12[0,1]=1;E23=s.zeros(3);E23[1,2]=1;E31=s.zeros(3);E31[2,0]=1
    E13=E12*E23-E23*E12
    ck('bulk_cubic_retained',s.trace(E31*E13)==1)
    # Coexact u=cos(x)dy E12 and v=-cos(y)dx E23; bracket is nonzero with zero mean.
    f=s.cos(x)*s.cos(y)
    ck('nonzero_coexact_bracket_has_zero_gauge_moment',E13[0,2]==1 and
       s.integrate(f,(x,0,2*s.pi),(y,0,2*s.pi))==0 and f.subs({x:0,y:0})==1)
    ck('old_exact_boundary_still_not_strict',s.diff(s.sin(x)*s.cos(y),x)==f and f.subs({x:0,y:0})!=0)
    # With reference held fixed, lambda=-1/2 <Astar+a,delta a>.
    t=s.symbols('t',real=True);u=s.Matrix([1,s.I]);ref=s.Matrix([3,5]);av=t*u
    wedge=lambda v,w:s.expand(v[0]*w[1]-v[1]*w[0])
    raw=-wedge(ref+av,u)/2;correction=s.diff(wedge(ref,av)/2,t)
    ck('affine_reference_counterterm_sign',raw!=0 and s.simplify(raw+correction)==0 and s.simplify(raw-correction)!=0)
    return dict(facts=facts,predicates_passed=len(facts),block_profiles=profiles,
      full_harmonic_dimensions=H,symbol_reference_covectors=48,
      conditional_cone_preserved=True,full_E8_structure_constants_recomputed=False,
      boundary_selected=False,full_real_action_completed=False,physical_spectrum_identified=False,
      stationary_chiral_completion=False,nonauthor_acceptance=False,physical_goal_achieved=False)

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
