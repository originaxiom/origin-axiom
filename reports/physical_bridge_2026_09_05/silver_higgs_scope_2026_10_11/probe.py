"""Full-slot SM invariants and actual old-plane compatibility controls.

The new selective boundary is NOT a constructed physical domain.
Reuses sealed literal/pencil arithmetic; never imports stored outputs.
"""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parents[1]

def source():
    spec = importlib.util.spec_from_file_location('higgs_pinned_pencil', BASE/'silver_charged_pair_lift_2026_10_11/probe.py')
    p = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p)
    return p

def unit(i, j):
    return s.Matrix(5, 5, lambda a, b: int(a == i and b == j))

@lru_cache(None)
def run():
    p = source(); cy = p.cy; facts = {}
    def ck(k, v):
        facts[k] = bool(v)
        assert facts[k], k
    H = s.diag(2,2,2,-3,-3)
    semisimple = [unit(i,j) for i,j in [(0,1),(1,0),(1,2),(2,1),(3,4),(4,3)]]
    generators = semisimple+[H]
    basis = cy.adjoint_basis()
    def invariants(actions, n):
        return n-p.rank(s.Matrix.vstack(*actions))
    def adjoint_dim(gens):
        return invariants([cy.adjoint_lie(g,basis) for g in gens],24)
    inv = {'structure24':24,'gauge24':adjoint_dim(generators)}
    for label, actions, multiplicity in [
        ('10_W', [cy.exterior_lie(g) for g in generators], 5),
        ('bar10_Wdual', [-cy.exterior_lie(g).T for g in generators], 5),
        ('5_Fdual', generators, 10),
        ('bar5_F', [-g.T for g in generators], 10)]:
        inv[label] = multiplicity*invariants(actions,actions[0].rows)
        ck(label+'_no_SM_invariant', inv[label] == 0)
    ck('full248_roster',24+24+10*5+10*5+5*10+5*10==248)
    ck('full_SM_commutant_dimension25',sum(inv.values())==25 and inv['gauge24']==1)
    joint = s.Matrix.vstack(*(cy.adjoint_lie(g,basis) for g in generators))
    hcoords = s.Matrix([0]*20+[2,2,2,-3])
    ck('actual_gauge_commutant_is_H',p.zero(p.mm(joint,hcoords)) and p.rank(joint)==23)
    noy = 24+adjoint_dim(semisimple)+5*invariants([cy.exterior_lie(g) for g in semisimple],10)+5*invariants([-cy.exterior_lie(g).T for g in semisimple],10)+10*invariants(semisimple,5)+10*invariants([-g.T for g in semisimple],5)
    ck('omitting_hypercharge_changes_full_commutant35',noy==35 and noy!=sum(inv.values()))

    compact = []
    for i,j in [(0,1),(0,2),(1,2),(3,4)]:
        compact += [unit(i,j)+unit(j,i),s.I*(unit(i,j)-unit(j,i))]
    compact += [unit(i,i)-unit(4,4) for i in range(4)]
    ck('twelve_independent_unbroken_Hermitian_generators',len(compact)==12 and s.Matrix.hstack(*(s.Matrix(list(c)) for c in compact)).rank()==12 and all(c.H==c and s.trace(c)==0 and H*c==c*H for c in compact))
    omega = [s.Integer(1),s.Integer(2),s.Integer(3)]
    for j,c in enumerate(compact):
        ck('one_generator_curvature_zero_'+str(j),all(p.zero(omega[a]*omega[b]*(c*c-c*c)) for a,b in combinations(range(3),2)))
        ck('one_generator_moment_zero_'+str(j),p.zero(sum((v*v*(c*c-c*c) for v in omega),s.zeros(5))))
    U,V=compact[0],compact[-4]
    comm = U*V-V*U
    ck('joint_complex_modes_need_not_be_moduli',not p.zero(comm) and s.trace(comm.H*comm)>0)
    ck('quartic_countercontrol_not_quadratic_lifting',s.trace(comm.H*comm)==2)

    _,_,_,_,_,a,b=cy.literal();a,b=cy.exterior_lie(a),cy.exterior_lie(b)
    E,D=p.boundary(a,b),p.boundary(-a.T,-b.T)
    ck('actual_F_harmonic_and_coexact_dimensions',E['n']==10 and E['t0']==3 and E['H'].cols==6 and E['U'].cols==7)
    summaries={};planes={};duals={}
    for name, subset, expected in [('exceptional',[0,1,2,3],[0,2,1,0]),('protected',[0,1,2,4],[0,1,0,0])]:
        L=E['H'][:,subset];LD=p.dual_plane(E,D,L)
        planes[name]=E['U'].row_join(L);duals[name]=D['U'].row_join(LD)
        row=p.pencil_count(E,L);other=p.pencil_count(D,LD)
        ck(name+'_prior_F_witness_reconstructed',row['H']==expected and row['J']==1)
        ck(name+'_actual_dual_reversal',other['H']==expected[::-1] and other['J']==-1)
        scaled={}
        for h in (-2,3):
            r=p.rank(p.mm(E['pencil'].subs(p.z,h*p.z),planes[name],p.z),p.z)
            ck(name+'_physical_weight_'+str(h)+'_generic_rank',r==row['rank'])
            scaled[str(h)]=r
        summaries[name]={'subset':subset,'H':row['H'],'dual_H':other['H'],'rank':row['rank'],'scaled_ranks':scaled}
    ck('selective_planes_are_distinct_equal_dimensions',planes['protected'].cols==planes['exceptional'].cols==11 and p.rank(planes['protected'].row_join(planes['exceptional']))==12)
    slot_planes=[planes['protected']]*3+[planes['exceptional']]*2
    def stable(g):
        action=-g.T
        return all(p.rank(slot_planes[i].row_join(slot_planes[j]))==slot_planes[i].cols for i in range(5) for j in range(5) if action[i,j]!=0)
    ck('selective_bar5_space_SM_stable',all(stable(g) for g in generators))
    ck('selective_bar5_space_NOT_OLD_full_k_stable',not stable(unit(3,0)))
    ck('common_exceptional_plane_keeps_colored_pair',summaries['exceptional']['scaled_ranks']['-2']==9 and summaries['exceptional']['scaled_ranks']['3']==9)
    ck('common_protected_plane_removes_doublet_pair_too',summaries['protected']['scaled_ranks']['-2']==10 and summaries['protected']['scaled_ranks']['3']==10)
    ck('dual_selective_planes_also_different',p.rank(duals['protected'].row_join(duals['exceptional']))>duals['protected'].cols)
    return {'facts':facts,'predicates_passed':len(facts),'full_SM_invariants':inv,
            'without_hypercharge_commutant_dimension':noy,'F_planes':summaries,
            'conditional_adjoints_persist':12,'old_full_k_selective_boundary_admitted':False,
            'new_physical_boundary_constructed':False,'normalized_mass_computed':False,
            'generated_selection':False,'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
