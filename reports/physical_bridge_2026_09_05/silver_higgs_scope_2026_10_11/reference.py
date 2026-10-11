"""Separate Fraction reconstruction and degree-bound certificates.

No SymPy, new native, native output or census producer execution.
"""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]

def source():
    spec=importlib.util.spec_from_file_location('higgs_fraction_pencil',BASE/'silver_charged_pair_lift_2026_10_11/reference.py')
    p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
    return p

@lru_cache(None)
def run():
    p=source();c=p.c;facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    def unit(i,j):
        a=c.Z(5);a[i][j]=1;return a
    H=[[([2,2,2,-3,-3][i] if i==j else 0) for j in range(5)] for i in range(5)]
    sem=[unit(i,j) for i,j in [(0,1),(1,0),(1,2),(2,1),(3,4),(4,3)]]
    gens=sem+[H];basis=c.basis5()
    def dim(actions,n):return n-p.rank(sum(actions,[]))
    inv={ 'structure24':24, 'gauge24':dim([c.ad(g,basis) for g in gens],24)}
    slots=[('10_W',[c.wedge_derivative(g) for g in gens],5),
           ('bar10_Wdual',[c.scale(c.tr(c.wedge_derivative(g)),-1) for g in gens],5),
           ('5_Fdual',gens,10),('bar5_F',[c.scale(c.tr(g),-1) for g in gens],10)]
    for name,acts,mult in slots:
        inv[name]=mult*dim(acts,len(acts[0]));ck(name+'_no_SM_invariant',inv[name]==0)
    ck('joint_full_commutant25',sum(inv.values())==25 and inv['gauge24']==1)
    noy=24+dim([c.ad(g,basis) for g in sem],24)+5*dim([c.wedge_derivative(g) for g in sem],10)+5*dim([c.scale(c.tr(c.wedge_derivative(g)),-1) for g in sem],10)+10*dim(sem,5)+10*dim([c.scale(c.tr(g),-1) for g in sem],5)
    ck('semisimple_only35_not_SM',noy==35 and noy!=sum(inv.values()))
    x=c.add(unit(0,1),unit(1,0))
    v=c.add(unit(0,0),unit(4,4),-1)
    comm=c.add(c.mm(x,v),c.mm(v,x),-1)
    ck('noncommuting_complex_quartic_control',sum(a*a for row in comm for a in row)==2)
    ck('commuting_single_generator_control',c.zero(c.add(c.mm(x,x),c.mm(x,x),-1)))
    ck('unbroken_H_commutes_with_compact_root',c.equal(c.mm(H,x),c.mm(x,H)))

    _,_,_,_,a,b=c.literal();a,b=c.wedge_derivative(a),c.wedge_derivative(b)
    E,D=p.boundary(a,b),p.boundary(c.scale(c.tr(a),-1),c.scale(c.tr(b),-1))
    ck('actual_F_dimensions',E['n']==10 and E['t0']==3 and len(E['U'][0])==7 and len(E['H'][0])==6)
    erows,drows=p.evaluation_rows(E),p.evaluation_rows(D)
    summaries={};planes={};duals={}
    for name,subset,expected in [('exceptional',[0,1,2,3],[0,2,1,0]),('protected',[0,1,2,4],[0,1,0,0])]:
        coeff=p.subset(c.I(6),subset);L=p.subset(E['H'],subset);LD,dualcoeff=p.paired_plane(E,D,L)
        row=p.degree_count(E,coeff,erows);other=p.degree_count(D,dualcoeff,drows)
        planes[name]=c.cat(E['U'],L);duals[name]=c.cat(D['U'],LD)
        ck(name+'_exact_degree_certificate',row['H']==expected and row['J']==1 and other['H']==expected[::-1])
        values={}
        for h in (-2,3):
            ranks=[p.rank(c.mm(c.cat(c.add(c.scale(b,-1),c.scale(c.I(10),-h*t)),a),planes[name])) for t in range(11)]
            values[str(h)]=max(ranks)
            ck(name+'_scaled_degree_certificate_'+str(h),max(ranks)==row['rank'])
        summaries[name]={'subset':subset,'H':row['H'],'dual_H':other['H'],'rank':row['rank'],'scaled_ranks':values}
    ck('two_actual_planes_not_equal',p.rank(c.cat(planes['protected'],planes['exceptional']))==12)
    slot=[planes['protected']]*3+[planes['exceptional']]*2
    def stable(g):
        action=c.scale(c.tr(g),-1)
        return all(p.rank(c.cat(slot[i],slot[j]))==len(slot[i][0]) for i in range(5) for j in range(5) if action[i][j])
    ck('SM_stability_actual_bar5',all(stable(g) for g in gens))
    ck('OLD_SU5_stability_fails',not stable(unit(3,0)))
    ck('dual_selective_subspaces_not_equal',p.rank(c.cat(duals['protected'],duals['exceptional']))>len(duals['protected'][0]))
    return {'facts':facts,'predicates_passed':len(facts),'full_SM_invariants':inv,
            'without_hypercharge_commutant_dimension':noy,'F_planes':summaries,
            'new_native_imported':False,'degree_bound_certificate':True,
            'new_physical_boundary_constructed':False,'generated_selection':False,
            'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
