"""Actual normal Gaussian, boundary reference and charged end accounting."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
path=Path(__file__).resolve().parent.parent/'weave_cusp_anomaly_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('normal_gaussian_end',path)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
Q=s.Rational
zero=lambda a:all(s.simplify(v)==0 for v in a)
CASES=[(3,4*s.I),(12,3+4*s.I),(12,3-4*s.I)]

def end_module(j,k):
    count=0;balance=0;slots=0
    for h in (0,1):
        now=old.end_blocks(j,k,h);ref=old.end_blocks(j,0,h)
        for C,R in zip(now,ref):
            slots+=C.rows
            if C.rows==2:
                assert C.trace()==0 and C.det()<0
                continue  # Reference signs +,- follow this coupled eigenpair.
            sigma=s.sign(R[0,0]);mu=C[0,0]
            assert sigma and mu
            balance+=sigma
            if sigma*mu<0:count+=sigma
    assert balance==0
    return int(count),slots

@lru_cache(None)
def indices(n):
    out=Counter()
    for (a,b,w,q,j),mult in old.modules().items():
        out[a,b,w,q]+=mult*end_module(j,n*q)[0]
    return out

def profile(n):
    out={}
    for q,rr in old.physical.REP.items():
        vals={indices(n)[a,b,w,q] for a,b,w in rr}
        assert len(vals)==1
        out[str(q)]=int(vals.pop())
    return out

def anomaly(n,drop=None):
    out=[s.Integer(0)]*5
    for (a,b,w,q),value in indices(n).items():
        if abs(q)==drop:continue
        terms=[Q((a+2*b)**3,-6),Q(q*a*a,4),Q(q*w*w,4),q**3,q]
        out=[x+Q(1,2)*value*y for x,y in zip(out,terms)]
    return [str(x) for x in out]

@lru_cache(None)
def run():
    facts={};I=s.I;pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    gam=[s.kronecker_product(pa[0],a) for a in pa]+[s.kronecker_product(pa[1],s.eye(2))]
    g5=s.kronecker_product(pa[2],s.eye(2))
    ps=s.symbols('p0:4',real=True);mu,xi=s.symbols('mu xi',real=True)
    D4=sum((I*g*p for g,p in zip(gam,ps)),s.zeros(4));H=g5*(D4+mu*s.eye(4))
    facts['actual_normal_source_target_signs']=zero((g5*I*xi+mu*s.eye(4))-s.diag(mu+I*xi,mu+I*xi,mu-I*xi,mu-I*xi))
    facts['radial_hamiltonian_hermitian_and_square']=zero(H-H.adjoint()) and zero(H*H-(sum(p*p for p in ps)+mu*mu)*s.eye(4))
    facts['tangential_principal_anticommutes_boundary_chirality']=zero(g5*(g5*D4)+(g5*D4)*g5)
    elliptic=True;flux=True
    for sigma in (-1,1):
        P=(s.eye(4)+sigma*g5)/2
        flux &= zero(P*gam[0]*g5*P)
        for mom in ((1,0,0,0),(0,1,0,0),(1,2,2,0)):
            B=(g5*D4).subs(dict(zip(ps,mom)));p=s.sqrt(sum(x*x for x in mom))
            elliptic &= s.Matrix.vstack(s.eye(4)-P,B+p*s.eye(4)).rank()==4
    facts['normal_boundary_complementing_controls']=elliptic
    facts['lorentzian_boundary_flux_zero']=flux
    overlaps=[];eigen=True;norm=True;phase=True
    for m,z in CASES:
        E=s.sqrt(m*m+z*s.conjugate(z));N=s.sqrt(2*E*(E+m))
        vp=s.Matrix([-s.conjugate(z),E+m])/N
        vm=s.Matrix([E+m,-z])/N
        hp=s.Matrix([[m,s.conjugate(z)],[z,-m]])
        hm=s.Matrix([[-m,s.conjugate(z)],[z,m]])
        eigen &= zero(hp*vp+E*vp) and zero(hm*vm+E*vm)
        norm &= s.simplify((vp.adjoint()*vp)[0]-1)==0 and s.simplify((vm.adjoint()*vm)[0]-1)==0
        ov=s.simplify((vp.adjoint()*vm)[0]);overlaps.append(str(ov))
        phase &= s.simplify(ov+z/E)==0
    facts['mass_anchored_ground_spinors']=eigen and norm
    facts['complex_overlap_is_one_chiral_factor']=phase
    facts['absolute_value_and_unit_phase_mutants_fail']=overlaps[0]!=str(abs(-4*I/5)) and overlaps[0]!='1' and overlaps[1]!=overlaps[2]
    r,m=s.symbols('r m',positive=True);E=s.sqrt(r*r+m*m)
    aplus=s.sqrt((E+m)/(2*E));aminus=r/s.sqrt(2*E*(E+m))
    facts['boundary_overlap_has_single_zero']=s.limit(aminus/r,r,0)==1/(2*m) and s.limit(aplus,r,0)==1
    facts['opposite_vacuum_overlap_zero_not_pure_phase']=s.limit(r/E,r,0)==0 and s.limit((r/E)/r,r,0)==1/m
    t,a,L,ell,T=s.symbols('t a L ell T',positive=True)
    f=s.sqrt(2*a)*s.exp(-a*t)
    facts['normal_mode_and_normalization']=s.simplify(s.diff(f,t)+a*f)==0 and s.integrate(f*f,(t,0,s.oo))==1
    facts['finite_collar_tail_retained']=s.simplify(1-s.integrate(f*f,(t,0,L))-s.exp(-2*a*L))==0
    original=s.exp((T-t)/2)*f/s.sqrt(ell)
    facts['cusp_kinetic_measure_and_constant_gauge_overlap']=s.simplify(ell*s.exp(-(T-t))*original**2-f**2)==0
    facts['sign_and_opposite_normal_controls']=all((sigma*mass<0)==(sigma==-s.sign(mass)) for mass in (-3,-1,1,3) for sigma in (-1,1))
    facts['balanced_reference_opposes_actual_index']=all(end_module(j,k)[0]==-old.module_signature(j,k)//2 for j in range(5) for k in range(-9,10))
    facts['all_actual_horizontal_slots_retained']=sum(mult*end_module(j,2*q)[1] for (*_,q,j),mult in old.modules().items())==496
    vectors={str(n):anomaly(n) for n in range(-3,4)}
    facts['full_end_anomaly_opposes_interior']=all(anomaly(n)==[str(-v) for v in old.physical.anomaly(n)] for n in range(-3,4))
    facts['first_flux_zero_and_exotic_controls']=profile(1)['1']==0 and profile(2)['1']==1 and profile(0)=={str(q):0 for q in range(1,7)} and anomaly(2,drop=5)!=anomaly(2)
    P0=s.diag(0,1,0);shift=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
    facts['horizontal_projection_is_not_pointwise_local']=not zero(P0*shift-shift*P0) and (P0*shift-shift*P0)*s.Matrix([0,1,0])==s.Matrix([0,0,-1])
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
      'overlap_examples':overlaps,'boundary_net_profiles':{str(n):profile(n) for n in range(-3,4)},
      'boundary_anomaly_vectors':vectors,'normal_gaussian_constructed':True,
      'full_cusp_boundary_lift_derived':False,'mirror_free_cancellation_derived':False,
      'global_determinant_derived':False,'nonauthor_acceptance':False,'physical_goal_achieved':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['facts'].values()) else 1)
