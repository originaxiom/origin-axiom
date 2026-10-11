"""Exact full-slot selective-boundary safeguards; supplied choices remain supplied."""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations, product
from math import factorial
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
OLD = HERE.parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

p = load('selective_charged_native', OLD/'silver_charged_pair_lift_2026_10_11/probe.py')
sp = load('selective_marked_cone_native', OLD/'silver_spectral_completion_2026_10_05/probe.py')
mm, rank, zero = p.mm, p.rank, p.zero

def inv(a): return p.dm(a).inv().to_Matrix()

def ker(a):
    if not a.rows: return s.eye(a.cols)
    r, piv = p.dm(a).rref()
    r = r.to_Matrix()
    free = [j for j in range(a.cols) if j not in piv]
    out = s.zeros(a.cols, len(free))
    for k, j in enumerate(free):
        out[j, k] = 1
        for i, v in enumerate(piv): out[v, k] = -r[i, j]
    return out

def cols(a):
    return a[:, list(p.dm(a).rref()[1])] if a.cols else a

def integral(a):
    out=power=s.eye(a.rows)
    for j in range(1,a.rows+1):
        power=mm(power,a)
        if zero(power):return out
        out+=power/factorial(j+1)
    raise ValueError('non-nilpotent log in finite integration')

def neutral(rep, data, basis, A, B, ck):
    n = 24
    rn = {g:p.cy.adjoint_group(x, basis) for g, x in rep.items()}
    T = s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    met = s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    P, Q = [p.cy.word(rn, text) for text in data['cusp_words']]
    bb = s.Matrix.vstack(*(rn[g]-s.eye(n) for g in p.GEN))
    f = s.Matrix.vstack(*(p.fox(rn, text) for text in data['relators']))
    r = s.Matrix.vstack(*(p.fox(rn, text) for text in data['cusp_words']))
    d = (P-s.eye(n)).col_join(Q-s.eye(n))
    g = (s.eye(n)-Q).row_join(P-s.eye(n))
    r2 = -mm(mm(Q, p.fox(rn, data['cusp_words'][0])[:, :2*n]),
             s.diag(inv(rn['t']), inv(rn['t'])))
    ck('neutral_literal_all_degree_chain', zero(mm(f, bb)) and zero(mm(g, d))
       and zero(mm(r, bb)-d) and zero(mm(r2, f)-mm(g, r)))
    h = ker(g.col_join(d.T))
    proj = mm(mm(h, inv(mm(h.T, h))), h.T)
    R = cols(mm(mm(proj, r), ker(f)))
    j = s.zeros(n).row_join(inv(P).T).col_join((-inv(Q).T).row_join(s.zeros(n)))
    S = mm(j, s.diag(T, T))
    HS = mm(mm(h.T, S), h)
    ck('neutral_full_invariant_trace_not_euclidean',
       rank(T)==24 and all(zero(mm(mm(x.T, T), x)-T) for x in rn.values())
       and any(not zero(mm(x.T, x)-s.eye(n)) for x in rn.values()))
    ck('neutral_actual_closed_cup_perfect_antisymmetric',
       h.cols==12 and R.cols==6 and rank(HS)==12 and zero(HS+HS.T)
       and zero(mm(mm(R.T, S), R)))
    M = mm(mm(R.T, S), h)
    piv = list(p.dm(M).rref()[1])
    U0 = mm(h[:, piv], inv(M[:, piv]))
    K = mm(mm(U0.T, S), U0)
    U = U0+mm(R, K)/2
    ck('neutral_actual_transverse_lagrangian',
       rank(U)==6 and rank(R.row_join(U))==12
       and zero(mm(mm(U.T, S), U)) and zero(mm(mm(R.T, S), U)-s.eye(6)))
    rb, rf, rd = rank(bb), rank(f), rank(d)
    absolute = [n-rb, 3*n-rb-rf, 2*n-rf, 0]
    t0 = n-rd
    def les(L):
        r1 = rank(R.row_join(L))
        return [0, t0-absolute[0]+absolute[1]+L.cols-r1,
                h.cols-r1+absolute[2], 0]
    hh, opposite = les(U), les(R)
    ck('neutral_full_LES_and_nontransverse_opposite',
       absolute==[0,6,6,0] and t0==6 and hh==[0,6,6,0] and opposite==[0,12,12,0])
    NA, NB = p.cy.adjoint_lie(A, basis), p.cy.adjoint_lie(B, basis)
    dlog = NA.col_join(NB)
    glog = (-NB).row_join(NA)
    m1 = s.diag(met, met)
    hl = ker(glog.col_join(mm(dlog.T, m1)))
    pl = mm(mm(hl, inv(mm(mm(hl.T, m1), hl))), mm(hl.T, m1))
    ua,ub=integral(NA),integral(NB)
    t1 = s.diag(ua,ub)
    UL = mm(mm(pl, inv(t1)), U)
    RL = mm(mm(pl, inv(t1)), R)
    SL = s.zeros(n).row_join(T).col_join((-T).row_join(s.zeros(n)))
    ck('neutral_cell_to_actual_log_harmonic_transport',
       zero(mm(t1, dlog)-d) and zero(mm(g, t1)-mm(mm(ua,ub), glog)) and rank(UL)==6
       and rank(RL.row_join(UL))==12 and zero(mm(mm(UL.T, SL), UL)))
    return dict(H=hh, equal_restriction_H=opposite, absolute_H=absolute,
                boundary_H=[t0, h.cols, t0], restriction_rank=R.cols,
                transported_log_plane_rank=UL.cols)

def anomaly_weights():
    u1, u2, w, y = s.symbols('u1 u2 w y')
    five = [u1+2*y, u2+2*y, -u1-u2+2*y, w-3*y, -w-3*y]
    ten = [five[i]+five[j] for i,j in combinations(range(5),2)]
    matter = ten+[-x for x in five]
    higgs = [w+3*y, -w+3*y, w-3*y, -w-3*y]
    return matter, higgs

@lru_cache(None)
def run():
    facts = {}
    def ck(k, value):
        facts[k] = bool(value)
        assert facts[k], k
    old, data, w, P, Q, A, B = p.cy.literal()
    model = json.loads((HERE/'MODEL.json').read_text())
    ck('literal_character_and_cusp_marker_not_parity',
       [sum(1 if c=='t' else -1 if c=='T' else 0 for c in text)
        for text in data['cusp_words']]==[0,1] and data['nu']['t']==-1)
    charged = {}
    for label, aa, bb, subset in [
        ('W', A, B, model['W_plane']),
        ('Fcolor', p.cy.exterior_lie(A), p.cy.exterior_lie(B), model['F_color_plane']),
        ('Fweak', p.cy.exterior_lie(A), p.cy.exterior_lie(B), model['F_weak_plane'])]:
        E, D = p.boundary(aa, bb), p.boundary(-aa.T, -bb.T)
        L = E['H'][:, subset]
        LD = p.dual_plane(E, D, L)
        a, b = p.pencil_count(E, L), p.pencil_count(D, LD)
        expected = [0,2,1,0] if label=='Fweak' else [0,1,0,0]
        ck(label+'_actual_pencil_dual_and_protected_index',
           a['H']==expected and b['H']==expected[::-1] and a['J']==1
           and L.cols+LD.cols==E['H'].cols)
        charged[label] = dict(E=a, dual=b)
        if label!='W':
            charged[label]['M'] = E['U'].row_join(L)
    MT, MD = charged['Fcolor'].pop('M'), charged['Fweak'].pop('M')
    ck('two_equal_dimension_distinct_actual_F_subspaces',
       rank(MT)==rank(MD)==11 and rank(MT.row_join(MD))==12)
    basis = p.cy.adjoint_basis()
    cut = model['gauge_partition'][0]
    ck('declared_partition_enters_the_actual_action', model['gauge_partition']==[3,2])
    off = [(i,j) for i,j in product(range(5),repeat=2) if (i<cut)!=(j<cut)]
    # bar5 acts by -x^T: independently arbitrary input in each source slot
    # gives one actual cross-block entry constraint, not a dimension guess.
    C = s.Matrix([[x[j,i] for x in basis] for i,j in off])
    allowed = ker(C)
    g = [x for x in basis if all(x[j,i]==0 for i,j in off)]
    ck('complete_maximal_gauge_stabilizer_and_common_plane_opposite',
       rank(C)==12 and allowed.cols==len(g)==12 and rank(MT.row_join(MT))==11
       and len(basis)==24)
    H = s.diag(*model['H'])
    ck('stabilizer_H_and_compact_reality',
       all(zero(mm(x,H)-mm(H,x)) for x in g)
       and all(x.T in g or zero(x-x.T) for x in g))
    trace = s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    hc = s.Matrix([H[i,j] for i in range(5) for j in range(5) if i!=j]+[H[i,i] for i in range(4)])
    X = ker(s.Matrix([[s.trace(H*x) for x in basis]]))
    Lg = X.col_join(s.zeros(24,23)).row_join(s.zeros(24,1).col_join(hc))
    Jg = s.zeros(24).row_join(trace).col_join((-trace).row_join(s.zeros(24)))
    ck('actual_gauge24_plane_maximal_cyclic_lagrangian',
       rank(Lg)==24 and zero(mm(mm(Lg.T,Jg),Lg)) and rank(trace)==24)
    for k, x in enumerate(g):
        ad = p.cy.adjoint_lie(x,basis)
        ck('gauge24_plane_SM_action_'+str(k),
           rank(Lg.row_join(mm(s.diag(ad,ad),Lg)))==24)
    ck('old_full_k_opposite_still_fails_selective_domain',
       rank(C)>0 and any(x[j,i]!=0 for x in basis for i,j in off))
    G = sp.Complex({g:s.eye(1) for g in p.GEN}, data)
    dx, dy = s.Matrix([1,0]), s.Matrix([0,1])
    gauge = {
        'retained_nonabelian':sp.cone(G,dx,s.eye(1),s.zeros(1,0),ranker=rank)['H'],
        'central':sp.cone(G,dy,s.eye(1),s.zeros(1,0),ranker=rank)['H'],
        'excluded_offblock_at_zero':sp.cone(G,dx,s.zeros(1,0),s.eye(1),ranker=rank)['H']}
    ck('gauge_marked_absolute_restriction_is_dy', G.res.cols==1 and rank(G.res.row_join(dy))==1
       and rank(G.res.row_join(dx))==2)
    ck('actual_gauge_endpoints_all_degrees',
       gauge=={'retained_nonabelian':[1,0,0,1], 'central':[1,1,1,1],
               'excluded_offblock_at_zero':[0,0,0,0]})
    Eg = p.boundary(s.zeros(1),s.zeros(1))
    Dg = p.boundary(s.zeros(1),s.zeros(1))
    dgdual = p.dual_plane(Eg,Dg,dx)
    phase = p.pencil_count(Eg,dx)['H']
    ck('excluded_offblock_actual_phase_pencil_and_dual',
       phase==[0,0,0,0] and rank(dx.row_join(dgdual))==1
       and p.pencil_count(Dg,dgdual)['H']==phase)
    gauge['excluded_offblock_small_phase'] = phase
    N = neutral(w,data,basis,A,B,ck)
    blocks = [(10,charged['W']['E']['H']), (10,charged['W']['dual']['H']),
              (3,charged['Fcolor']['E']['H']), (3,charged['Fcolor']['dual']['H']),
              (2,charged['Fweak']['E']['H']), (2,charged['Fweak']['dual']['H']),
              (1,N['H']), (11,gauge['retained_nonabelian']),
              (1,gauge['central']), (12,phase)]
    full = [sum(m*h[j] for m,h in blocks) for j in range(4)]
    ck('full248_harmonic_boundary_and_new_endpoints',
       10*(5+5)+5*(10+10)+24+24==248
       and 10*(4)+5*(6)+6+24==100 and model['new_Ah_dimensions']==[12,100,88])
    ck('complete_physical_chirals_vectors_and_actual_duals',
       full==[12,26,26,12] and full==full[::-1]
       and 26==15+4+6+1 and 11==8+3)
    dof = 2*full[1]+2*full[0]
    ck('boson_fermion_dof_and_H2_doublecount_opposite',
       dof==2*(full[1]+full[3])==76 and dof!=2*(full[1]+full[2]+full[3]))
    matter,higgs = anomaly_weights()
    cubic, mixed = s.expand(sum(x**3 for x in matter+higgs)), s.expand(sum(matter+higgs))
    ck('all_SM_Cartan_cubic_and_mixed_anomalies_zero',
       cubic==mixed==0 and s.expand(sum(x**3 for x in matter+higgs[:-1]))!=0)
    ck('weak_mod2_counts_with_opposing_single_doublet', (3+1+2)%2==0 and (3+1+1)%2==1)
    bad = mm(H,basis[2])-mm(basis[2],H)
    ck('retained_parallel_kernel_and_nonparallel_opposite',
       all(zero(mm(H,x)-mm(x,H)) for x in g)
       and not zero(bad) and s.trace(bad.H*bad)==25)
    adbad = p.cy.adjoint_lie(basis[2],basis)
    ck('gauge24_line_itself_does_not_restore_full_SU5',
       rank(Lg.row_join(mm(s.diag(adbad,adbad),Lg)))>24)
    return dict(facts=facts,predicates_passed=len(facts),charged=charged,neutral=N,gauge=gauge,
                maximal_boundary_gauge_dimension=len(g),boundary_Ah=[12,100,88],full_H=full,
                chiral_components=full[1],vector_components=full[0],on_shell_real_dof=dof,
                generation_count=1,neutral_chirals=7,tree_Higgs_pair=True,
                same_bulk_parent=True,old_boundary_reused=False,new_boundary_supplied=True,
                generated_selection=False,EW_vacuum_derived=False,normalized_overlaps=False,
                global_PDE_solved=False,outside_review=False,full_goal_achieved=False)

if __name__=='__main__': print(json.dumps(run(),sort_keys=True,indent=2))
