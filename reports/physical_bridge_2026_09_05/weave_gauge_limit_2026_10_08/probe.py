"""Actual mass principal slots, local heat jets and cutoff controls."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/probe.py'
spec=importlib.util.spec_from_file_location('gauge_limit_mass',path)
physical=importlib.util.module_from_spec(spec);spec.loader.exec_module(physical)
Q=s.Rational
zero=lambda a:all(s.expand(x)==0 for x in a)
J=s.diag(-s.I,-s.I,s.I,s.I)

def heat_trace(B,C,Bx,By,Cx,Cy):
    ax=C-B;ayp=J*B+C*J;aym=B*J+J*C
    bp=-Bx+J*By+C*B;bm=Cx+J*Cy+B*C
    divp=Cx-Bx+J*By+Cy*J;divm=Cx-Bx+By*J+J*Cy
    Ep=-bp+divp/2-(ax*ax+ayp*ayp)/4
    Em=-bm+divm/2-(ax*ax+aym*aym)/4
    return s.expand(s.trace(Ep-Em)),s.expand(s.trace(ayp*ayp-aym*aym))

@lru_cache(None)
def run():
    facts={};kx,ky=s.symbols('kx ky',real=True)
    p=s.I*kx-ky
    q=s.Matrix([[1+s.I,2],[0,1-s.I]])
    r=s.Matrix([[0,1],[2*s.I,1]])
    H=s.diag(s.eye(2),s.eye(2)/s.sqrt(2),s.eye(2),s.eye(2))
    row=s.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    P=s.kronecker_product(row,s.eye(2))
    canon=P*H*physical.mass(q,r,p,1)*H.inv()
    phi=canon.subs({kx:0,ky:0});JJ=s.kronecker_product(J,s.eye(2))
    facts['actual_metric_normalized_principal_slots']=zero(canon-phi-s.I*kx*s.eye(8)-s.I*ky*JJ)
    facts['actual_Q_R_are_off_block']=zero(phi[:4,:4]) and zero(phi[4:,4:]) and not zero(phi[:4,4:]) and not zero(phi[4:,:4])
    facts['actual_potential_has_zero_two_traces']=s.trace(phi)==0 and s.trace(JJ*phi)==0 and zero(JJ*phi+phi*JJ)
    wrong=P*physical.mass(q,r,p,1)-P*physical.mass(q,r,0,1)
    facts['omitted_kinetic_metric_fails']=not zero(wrong-s.I*kx*s.eye(8)-s.I*ky*JJ)
    mats=[s.Matrix(4,4,s.symbols(name+':16')) for name in ('b','c','bx','by','cx','cy')]
    B,C,Bx,By,Cx,Cy=mats
    result,squared=heat_trace(*mats)
    expected=s.trace(Bx+Cx-J*By+J*Cy)
    facts['arbitrary_matrix_heat_identity']=s.expand(result-expected)==0
    facts['connection_square_trace_cancels']=squared==0
    off=lambda A:s.Matrix(4,4,lambda i,j:A[i,j] if (i<2)!=(j<2) else 0)
    facts['off_block_potential_first_jets_do_not_shift_density']=heat_trace(*map(off,mats))[0]==0
    O=s.zeros(4);D=s.diag(1,0,0,0)
    facts['diagonal_potential_mutant_is_detected']=heat_trace(O,O,D,O,D,O)[0]==2
    beta=s.symbols('beta')
    slots=[1-beta,1-beta,-beta,2-beta];signs=[1,1,-1,-1]
    rank=sum(signs);degree=s.expand(sum(e*a for e,a in zip(signs,slots)))
    facts['full_virtual_rank_and_curvature_cancel']=rank==0 and degree==0
    facts['lost_physical_slot_fails']=s.expand(sum(e*a for e,a in zip(signs[:-1],slots[:-1])))!=0 and sum(signs[:-1])!=0
    u=s.symbols('u',real=True);eta=1-3*u*u+2*u**3
    normpoly=s.expand((1-eta)**2+s.diff(eta,u)**2)
    cost=s.simplify(s.integrate(s.exp(-u)*normpoly,(u,0,1))+s.exp(-1))
    facts['transition_joins_value_and_first_derivative']=eta.subs(u,0)==1 and eta.subs(u,1)==0 and all(s.diff(eta,u).subs(u,e)==0 for e in (0,1))
    facts['graph_cost_positive_with_tail']=bool(cost>0) and s.simplify(cost-s.integrate(s.exp(-u)*normpoly,(u,0,1)))==s.exp(-1)
    rho=s.symbols('rho',positive=True)
    facts['graph_cost_decays_not_end_value']=s.limit(cost*s.exp(-rho),rho,s.oo)==0
    # At trace height R+2 the compact gauge parameter is already zero.
    facts['separated_trace_shell_has_zero_parameter']=all((1-3*x*x+2*x**3 if 0<x<1 else (1 if x<=0 else 0))==0 for x in (Q(2),Q(5,2),Q(3)))
    overlap=s.integrate(eta*s.diff(eta,u),(u,0,1))
    facts['overlapping_shell_is_not_zero']=overlap==-Q(1,2)
    vectors={str(n):[str(v) for v in physical.anomaly(n)] for n in range(-3,4)}
    facts['nonzero_color_and_first_flux_kept']=vectors['1'][0]=='-1' and vectors['2'][0]=='-3'
    facts['zero_and_opposite_flux_kept']=vectors['0']==['0']*5 and all(physical.anomaly(-n)==[-v for v in physical.anomaly(n)] for n in (1,2,3))
    facts['complete_roster_not_a_selected_subsector']=sum(physical.full_weights().values())==248 and physical.anomaly(2,drop_charge=5)!=physical.anomaly(2)
    facts={k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
       'anomaly_vectors':vectors,'virtual_rank_degree':[rank,int(degree)],
       'cutoff_norm_constant':str(s.expand(cost)),'overlap_integral':str(overlap),
       'compact_parameter_current_limit':0,
       'local_gaussian_phase_derived':False,'anomaly_cancellation_derived':False,
       'all_quantum_completions_excluded':False,'nonauthor_acceptance':False,
       'physical_goal_achieved':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['facts'].values()) else 1)
