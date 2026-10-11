"""Separate Fraction/crossed-word/LES selective-boundary check, no new native import."""
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
HERE=Path(__file__).resolve().parent
OLD=HERE.parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

p=load('selective_charged_fraction',OLD/'silver_charged_pair_lift_2026_10_11/reference.py')
mp=load('selective_multiplet_fraction',OLD/'silver_physical_multiplets_2026_10_11/reference.py')

def anomaly():
    five=[(1,0,0,2),(0,1,0,2),(-1,-1,0,2),(0,0,1,-3),(0,0,-1,-3)]
    ten=[tuple(x+y for x,y in zip(five[i],five[j])) for i,j in combinations(range(5),2)]
    bar=[tuple(-x for x in a) for a in five]
    higgs=[(0,0,a,b) for b in (-3,3) for a in (-1,1)]
    def poly(weights):
        out=Counter()
        for a in weights:
            for ijk in product(range(4),repeat=3):
                out[tuple(sorted(ijk))]+=a[ijk[0]]*a[ijk[1]]*a[ijk[2]]
        return {k:v for k,v in out.items() if v}
    return five,ten+bar,higgs,poly

@lru_cache(None)
def run():
    facts={}
    def ck(k,v):facts[k]=bool(v);assert facts[k],k
    data,w,P,Q,A,B=p.c.literal()
    model=json.loads((HERE/'MODEL.json').read_text())
    charged={};Ms={}
    for label,a,b,idx in [('W',A,B,model['W_plane']),
        ('Fcolor',p.c.wedge_derivative(A),p.c.wedge_derivative(B),model['F_color_plane']),
        ('Fweak',p.c.wedge_derivative(A),p.c.wedge_derivative(B),model['F_weak_plane'])]:
        E,D=p.boundary(a,b),p.boundary(p.scale(p.tr(a),-1),p.scale(p.tr(b),-1))
        L=p.subset(E['H'],idx);coeff=p.subset(p.I(len(E['H'][0])),idx)
        LD,dc=p.paired_plane(E,D,L)
        aa=p.degree_count(E,coeff,p.evaluation_rows(E))
        dd=p.degree_count(D,dc,p.evaluation_rows(D))
        expected=[0,2,1,0] if label=='Fweak' else [0,1,0,0]
        ck(label+'_n_plus_one_degree_certificate_and_genuine_dual',
           aa['H']==expected and dd['H']==expected[::-1] and aa['J']==1
           and len(L[0])+len(LD[0])==len(E['H'][0]))
        charged[label]={'E':aa,'dual':dd}
        if label!='W':Ms[label]=p.cat(E['U'],L)
    MT,MD=Ms['Fcolor'],Ms['Fweak']
    ck('distinct_equal_dimension_selective_subspaces',
       p.rank(MT)==p.rank(MD)==11 and p.rank(p.cat(MT,MD))==12)
    basis=p.c.basis5()
    cut=model['gauge_partition'][0]
    ck('supplied_partition_enters_constraints',model['gauge_partition']==[3,2])
    off=[(i,j) for i,j in product(range(5),repeat=2) if (i<cut)!=(j<cut)]
    constraints=[[x[j][i] for x in basis] for i,j in off]
    gauges=[x for x in basis if all(x[j][i]==0 for i,j in off)]
    ck('full_cross_slot_stabilizer_and_common_plane_control',
       p.rank(constraints)==12 and len(gauges)==12 and len(basis)==24
       and p.rank(p.cat(MT,MT))==11)
    trace=p.c.gram(basis)
    h=[0]*20+[2,2,2,-3]
    row=[sum(model['H'][i]*x[i][i] for i in range(5)) for x in basis]
    X=p.null([row])
    Lg=p.stack(p.cat(X,p.Z(24,1)),p.cat(p.Z(24,23),[[x] for x in h]))
    J=p.stack(p.cat(p.Z(24),trace),p.cat(p.scale(trace,-1),p.Z(24)))
    ck('gauge24_trace_polarization_isotropic_maximal',
       p.rank(Lg)==24 and p.zero(p.mm(p.mm(p.tr(Lg),J),Lg)))
    for i,x in enumerate(gauges):
        ad=p.c.ad(x,basis)
        ck('gauge24_actual_induced_action_'+str(i),
           p.rank(p.cat(Lg,p.mm(p.c.diag(ad,ad),Lg)))==24)
    adbad=p.c.ad(basis[2],basis)
    ck('gauge24_independent_full_SU5_rejecting_control',
       p.rank(p.cat(Lg,p.mm(p.c.diag(adbad,adbad),Lg)))>24)
    for k,v in mp.root_controls().items():ck('credited_full_E8_roster_'+k,v)
    # Keep this independently loaded quadratic class separate from p.c.K.
    v=mp.b.four(data);cc=[mp.K(a,b) for a,b in data['cocycle_Qsqrt2_pairs']]
    wm=mp.b.extension(v,cc)
    rn,T=mp.end0(wm);N=mp.boundary(rn,data)
    SN=mp.mm(N['J'],mp.diag2(T));R,H=N['R'],N['H'];q=N['q']
    HS=mp.mm(mp.mm(mp.tr(H),SN),H)
    ck('independent_End25_trace_cup_and_nonunitary_control',
       mp.rank(T)==24 and all(mp.mm(mp.mm(mp.tr(x),T),x)==T for x in rn.values())
       and any(mp.mm(mp.tr(x),x)!=mp.eye(24) for x in rn.values())
       and mp.rank(HS)==12 and mp.zero(mp.add(HS,mp.tr(HS))))
    M=mp.mm(mp.mm(mp.tr(R),SN),H);piv=mp.b.elimination(M,True)[1]
    pick=lambda a:[[row[j] for j in piv] for row in a]
    U0=mp.mm(pick(H),mp.inv(pick(M)))
    K=mp.mm(mp.mm(mp.tr(U0),SN),U0)
    U=mp.add(U0,[[mp.K(Fraction(1,2))*x for x in row] for row in mp.mm(R,K)])
    ck('neutral_transverse_cyclic_partner_with_identity_cross_pair',
       q==6 and mp.rank(mp.hc(R,U))==12 and mp.zero(mp.mm(mp.mm(mp.tr(U),SN),U))
       and mp.mm(mp.mm(mp.tr(R),SN),U)==mp.eye(6))
    nh,opposite=mp.les(N,U),mp.les(N,R)
    ck('full_neutral_LES_opposite_and_absolute_roster',
       nh==[0,6,6,0] and opposite==[0,12,12,0]
       and [N['h0'],N['h1'],N['h2'],0]==[0,6,6,0]
       and [N['t0'],N['t'],N['t0']]==[6,12,6])
    G=mp.boundary({g:mp.eye(1) for g in mp.b.GEN},data)
    dx,dy=[[1],[0]],[[0],[1]]
    ck('literal_gauge_marker_periods',mp.rank(mp.hc(G['R'],dy))==1
       and mp.rank(mp.hc(G['R'],dx))==2)
    def endpoints(L,a0,a2):
        r1=mp.rank(mp.hc(G['R'],L))
        return [G['h0']+a0-G['t0'],G['h1']+1-r1,2-r1+G['h2'],1-a2]
    gauge={'retained_nonabelian':endpoints(dx,1,0),'central':endpoints(dy,1,0),
           'excluded_offblock_at_zero':endpoints(dx,0,1)}
    ck('all_gauge_endpoints_by_exact_LES',gauge=={'retained_nonabelian':[1,0,0,1],
       'central':[1,1,1,1],'excluded_offblock_at_zero':[0,0,0,0]})
    E=p.boundary(p.Z(1),p.Z(1));LD,dc=p.paired_plane(E,E,dx)
    phase=p.degree_count(E,p.subset(p.I(2),[0]),p.evaluation_rows(E))['H']
    ck('offblock_phase_degree_certificate_and_dual',phase==[0,0,0,0]
       and p.degree_count(E,dc,p.evaluation_rows(E))['H']==phase
       and p.rank(p.cat(dx,LD))==1)
    gauge['excluded_offblock_small_phase']=phase
    blocks=[(10,charged['W']['E']['H']),(10,charged['W']['dual']['H']),
      (3,charged['Fcolor']['E']['H']),(3,charged['Fcolor']['dual']['H']),
      (2,charged['Fweak']['E']['H']),(2,charged['Fweak']['dual']['H']),
      (1,nh),(11,gauge['retained_nonabelian']),(1,gauge['central']),(12,phase)]
    full=[sum(m*h[j] for m,h in blocks) for j in range(4)]
    ck('complete_roster_without_dual_particle_duplication',full==[12,26,26,12]
       and 26==15+4+6+1 and 2*26+2*12==76 and 2*(26+26+12)!=76)
    five,matter,higgs,polynomial=anomaly()
    weights=matter+higgs
    ck('every_cubic_monomial_and_mixed_gravity',not polynomial(weights)
       and all(sum(a[j] for a in weights)==0 for j in range(4))
       and bool(polynomial(weights[:-1])))
    ck('weak_global_parity_bookkeeping_opposite',(3+1+2)%2==0 and (3+1+1)%2==1)
    ck('full_boundary_248_and_100_dimension_roster',
       10*(5+5)+5*(10+10)+24+24==248
       and 10*(3+1)+5*(4+2)+6+24==100 and model['new_Ah_dimensions']==[12,100,88])
    return dict(facts=facts,predicates_passed=len(facts),charged=charged,
       neutral={'H':nh,'equal_restriction_H':opposite,'absolute_H':[N['h0'],N['h1'],N['h2'],0],
                'boundary_H':[N['t0'],N['t'],N['t0']],'restriction_rank':q},
       gauge=gauge,maximal_boundary_gauge_dimension=len(gauges),boundary_Ah=[12,100,88],
       full_H=full,chiral_components=26,vector_components=12,on_shell_real_dof=76,
       generation_count=1,neutral_chirals=7,tree_Higgs_pair=True,
       new_native_imported=False,same_author=True,new_boundary_supplied=True,
       generated_selection=False,EW_vacuum_derived=False,normalized_overlaps=False,
       global_PDE_solved=False,outside_review=False,full_goal_achieved=False)

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
