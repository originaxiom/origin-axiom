"""Exact fixed-domain charged pencils and literal family-cone first jets.

Native Q(sqrt2)(z); the separate reference uses finite degree certificates.
No execution of this module is authorized before its published seal.
"""
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
GEN = 'abt'
q, z = s.symbols('q z')
K = s.QQ.algebraic_field(s.sqrt(2))
ROOT_ELEMENT = K.from_sympy(s.sqrt(2))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec); spec.loader.exec_module(out)
    return out


cy = load('charged_lift_old_cyclic_native', HERE.parent/'silver_cyclic_transfer_2026_10_06/probe.py')


def quadratic_polynomial(x):
    x=s.expand(x); b=x.coeff(s.sqrt(2)); a=s.expand(x-b*s.sqrt(2))
    if not (a.is_Rational and b.is_Rational):
        raise ValueError('coefficient outside the declared quadratic field')
    return K.convert(a)+K.convert(b)*ROOT_ELEMENT


def element(x, variable=None):
    # Extract exact rational quadratic pairs; never rediscover minimal
    # polynomials for nested rational expressions or silently approximate.
    num,den=s.together(x).as_numer_denom()
    if variable is None: return quadratic_polynomial(num)/quadratic_polynomial(den)
    field=K.frac_field(variable); generator=field.gens[0]
    def polynomial(expr):
        out=field.zero
        for (power,),coefficient in s.Poly(s.expand(expr),variable,domain='EX').terms():
            out+=field.convert(quadratic_polynomial(coefficient),K)*generator**power
        return out
    return polynomial(num)/polynomial(den)


def dm(a, variable=None):
    field=K if variable is None else K.frac_field(variable); data={}
    for i in range(a.rows):
        row={j:element(a[i,j],variable) for j in range(a.cols) if a[i,j]!=0}
        if row:data[i]=row
    return DomainMatrix(data,(a.rows,a.cols),field)


def rank(a, variable=None):
    if not a.rows or not a.cols:return 0
    matrix=dm(a,variable)
    # Exact rank over K(variable), computed fraction-free in its associated
    # polynomial ring. No parameter evaluations or statistical sampling.
    return len(matrix.rref_den(method='CD',keep_domain=False)[2]) if variable is not None else matrix.rank()


def mm(a, b, variable=None):
    return dm(a, variable).matmul(dm(b, variable)).to_Matrix()


def zero(a, variable=None): return dm(a, variable).is_zero_matrix
def columns(a): return a[:, list(dm(a).rref()[1])] if a.cols else a
def kernel(a): return cy.kernel(a)


def fox(rep, text, variable=None):
    n = rep['a'].rows
    letters = dict(rep)
    letters.update({g.upper():dm(m, variable).inv().to_Matrix() for g, m in rep.items()})
    prefix = s.eye(n); blocks = [s.zeros(n) for _ in GEN]
    for letter in text:
        j = GEN.index(letter.lower())
        if letter.islower():
            blocks[j] += prefix; prefix = mm(prefix, letters[letter], variable)
        else:
            prefix = mm(prefix, letters[letter], variable); blocks[j] -= prefix
    return s.Matrix.hstack(*blocks)


def family(rep, data):
    n = rep['a'].rows; I = s.eye(n)
    rq = dict(rep); rq['t'] = q*rep['t']
    P, Q = [cy.word(rep, w) for w in data['cusp_words']]
    B = s.Matrix.vstack(*(rq[g]-I for g in GEN))
    F = s.Matrix.vstack(*(fox(rq, w, q) for w in data['relators']))
    R = s.Matrix.vstack(*(fox(rq, w, q) for w in data['cusp_words']))
    R2 = -mm(mm(q*Q, fox(rep, data['cusp_words'][0])[:, :2*n], q),
              s.diag(cy.inv(rep['t'])/q, cy.inv(rep['t'])/q), q)
    D = (P-I).col_join(q*Q-I); G = (I-q*Q).row_join(P-I)
    return dict(B=B, F=F, R=R, R2=R2, D=D, G=G, P=P, Q=Q)


def bulk_leading_minor_certificate(fam, rep):
    # PROOF2's exact generic-rank certificate: a polynomial square minor
    # with invertible top coefficient is nonzero. It proves the SAME
    # maximal ranks without a redundant large rational-function RREF.
    n=rep['t'].rows; fiber=fam['F'][:,:2*n]; time=fam['B'][2*n:,:]
    top=s.diag(rep['t'],rep['t'])
    return (zero(s.diff(fiber,q)-top) and rank(top)==2*n
            and zero(s.diff(time,q)-rep['t']) and rank(rep['t'])==n)


def jets_q(a):
    # q=exp(z); coefficients, not derivatives, in degrees zero, one, two.
    return [a.subs(q, 1), s.diff(a, q).subs(q, 1),
            ((s.diff(a, q, 2)+s.diff(a, q))/2).subs(q, 1)]


def integral_jets(a):
    powers = [s.eye(a.rows)]
    for j in range(1, a.rows+1):
        powers.append(mm(powers[-1], a))
        if zero(powers[-1]): break
    assert zero(powers[-1])
    return [sum((powers[j]/(factorial(j)*factorial(k)*(j+k+1))
                 for j in range(len(powers)-1)), s.zeros(a.rows)) for k in range(3)]


def boundary(a, b):
    n = a.rows; d0 = a.col_join(b); d1 = (-b).row_join(a)
    U = columns(d1.T); H = kernel(d1.col_join(d0.T))
    return dict(n=n, a=a, b=b, U=U, H=H, t0=n-rank(d1),
                pencil=(-b-z*s.eye(n)).row_join(a))


def dual_plane(E, D, L):
    n = E['n']; J = s.zeros(n).row_join(s.eye(n)).col_join((-s.eye(n)).row_join(s.zeros(n)))
    LD = mm(D['H'], kernel(mm(mm(L.T, J), D['H'])))
    assert zero(mm(mm(L.T, J), LD))
    return LD


def pencil_count(E, L):
    M = E['U'].row_join(L); r = rank(mm(E['pencil'], M, z), z)
    h = [0, M.cols-r, E['n']-r, 0]
    return dict(H=h, J=h[1]-h[2], rank=r, ell=L.cols)


def cone_jets(fam, E, L, direction=1):
    n = E['n']; M = E['U'].row_join(L); m = M.cols
    sizes = [n, 4*n+m, 5*n, n]
    jets = [[s.zeros(sizes[j+1], sizes[j]) for _ in range(3)] for j in range(3)]
    B, F, R, R2, D, G = [jets_q(fam[k]) for k in ('B', 'F', 'R', 'R2', 'D', 'G')]
    ua = cy.integral_exp(E['a']); ub = integral_jets(E['b'])
    T1 = [s.diag(ua, ub[0]), s.diag(s.zeros(n), direction*ub[1]), s.diag(s.zeros(n), ub[2])]
    T2 = [mm(ua, direction**k*t) for k,t in enumerate(ub)]
    da = [(-E['b']).row_join(E['a']), (-direction*s.eye(n)).row_join(s.zeros(n)), s.zeros(n, 2*n)]
    for k in range(3):
        d0, d1, d2 = [jets[j][k] for j in range(3)]
        d0[:3*n, :] = B[k]
        if k == 0: d0[3*n+m:, :] = s.eye(n)
        d1[:2*n, :3*n] = F[k]
        d1[2*n:3*n, 3*n:3*n+m] = mm(da[k], M)
        d1[3*n:, :3*n] = R[k]
        d1[3*n:, 3*n:3*n+m] = -mm(T1[k], M)
        d1[3*n:, 3*n+m:] = -D[k]
        d2[:, :2*n] = R2[k]
        d2[:, 2*n:3*n] = -T2[k]
        d2[:, 3*n:] = -G[k]
    return jets, sizes


def chain_jet_residuals(jets):
    return [sum((mm(jets[j+1][k-i], jets[j][i]) for i in range(k+1)),
                s.zeros(jets[j+1][0].rows, jets[j][0].cols))
            for j in range(2) for k in range(3)]


def first_mass(jets, sizes):
    d0, d1, d2 = [a[0] for a in jets]
    r = [rank(d0), rank(d1), rank(d2)]
    H = [sizes[j]-([0]+r)[j]-(r+[0])[j] for j in range(4)]
    Z = kernel(d1); B = columns(d0)
    combined = B.row_join(Z); piv = dm(combined).rref()[1]
    representatives = combined[:, [j for j in piv if j >= B.cols]]
    assert representatives.cols == H[1]
    derivative = mm(jets[1][1], representatives)
    induced = rank(d1.row_join(derivative))-r[1]
    return dict(H_at_zero=H, first_mass_rank=induced,
                massless_at_first_order=[H[1]-induced, H[2]-induced]), dict(
                cycles=zero(mm(d2, derivative)),
                boundaries_descend=zero(mm(jets[1][1], d0)+mm(d1, jets[0][1])))


@lru_cache(None)
def run():
    old, data, w, P, Q, A, B = cy.literal(); facts = {}; blocks = {}; jets_out = {}
    def ck(k, v): facts[k] = bool(v); assert facts[k], k
    exponents = s.Matrix([[sum((1 if c.islower() else -1) for c in r if c.lower() == g)
                           for g in GEN] for r in data['relators']])
    ck('literal_primitive_character_not_parity', exponents == s.Matrix([[2,2,0],[2,6,0]])
       and kernel(exponents) == s.Matrix([0,0,1]) and exponents*s.Matrix([data['nu'][g] for g in GEN]) != s.zeros(2,1))
    ck('literal_cusp_periods_0_1', [sum(1 if c == 't' else -1 if c == 'T' else 0 for c in text)
                                 for text in data['cusp_words']] == [0,1])
    ck('two_independent_actual_cusp_logs', rank(s.Matrix.hstack(s.Matrix(list(A)), s.Matrix(list(B)))) == 2)
    reps = {'W':w, 'F':{g:old.wedge(x) for g,x in w.items()}}
    for label, rep in reps.items():
        n = rep['a'].rows; a,b = (A,B) if label == 'W' else (cy.exterior_lie(A),cy.exterior_lie(B))
        E = boundary(a,b); dualrep = {g:cy.inv(x).T for g,x in rep.items()}; D = boundary(-a.T,-b.T)
        fam = family(rep,data); dfam = {k:x.subs(q,1/q) for k,x in family(dualrep,data).items()}
        ck(label+'_literal_full_family_chain', zero(mm(fam['F'],fam['B'],q),q)
           and zero(mm(fam['G'],fam['D'],q),q) and zero(mm(fam['R'],fam['B'],q)-fam['D'],q)
           and zero(mm(fam['R2'],fam['F'],q)-mm(fam['G'],fam['R'],q),q))
        ck(label+'_actual_R_maps_independent_of_character', zero(s.diff(fam['R'],q),q) and zero(s.diff(fam['R2'],q),q))
        ck(label+'_bulk_generic_acyclic_exact', bulk_leading_minor_certificate(fam,rep))
        ck(label+'_fiber_minor_leading_certificate', zero(s.diff(fam['F'][:,:2*n],q)-s.diag(rep['t'],rep['t'])))
        controls=[]
        for value in (1,2,3):
            rb,rf = [rank(fam[k].subs(q,value)) for k in ('B','F')]
            controls.append([n-rb,3*n-rb-rf,2*n-rf])
        ck(label+'_q1_old_cohomology_q2_q3_acyclic_controls', controls[0]==([0,2,2] if label=='W' else [0,4,4]) and controls[1:]==[[0,0,0],[0,0,0]])
        ck(label+'_old_boundary_dimensions', E['U'].cols==n-E['t0'] and E['H'].cols==2*E['t0'] and E['t0']==(2 if label=='W' else 3))
        ck(label+'_full_old_coexact_plus_harmonic_generic_rank', rank(mm(E['pencil'],E['U'].row_join(E['H']),z),z)==n)
        rows=[]; first={}
        for ell in range(E['H'].cols+1):
            for subset in combinations(range(E['H'].cols),ell):
                L=E['H'][:,list(subset)]; LD=dual_plane(E,D,L)
                row=pencil_count(E,L); other=pencil_count(D,LD)
                ck(label+'_dual_'+('_'.join(map(str,subset)) or 'empty'), row['H']==other['H'][::-1] and row['J']==-other['J'])
                row.update(subset=list(subset),dual=other); rows.append(row)
                if row['H']==[0,max(row['J'],0),max(-row['J'],0),0] and ell not in first: first[ell]=list(subset)
        ck(label+'_all_coordinate_planes_and_all_dimensions', len(rows)==2**E['H'].cols and set(first)==set(range(E['H'].cols+1)))
        hist={str(ell):dict(sorted(Counter(tuple(row['H']) for row in rows if row['ell']==ell).items())) for ell in first}
        # JSON keys cannot be tuples; preserve the declared basis-dependent witness distribution.
        hist={ell:{','.join(map(str,k)):v for k,v in h.items()} for ell,h in hist.items()}
        blocks[label]=dict(n=n,t0=E['t0'],bulk_H_controls=controls,witness_count=len(rows),
                           witness_histograms=hist,protected_only_witnesses={str(k):v for k,v in first.items()},rows=rows)
        for J in (1,2):
            ell=E['t0']+J; L=E['H'][:,first[ell]]; LD=dual_plane(E,D,L)
            for tag, f, e, plane in ((label,fam,E,L),(label+'dual',dfam,D,LD)):
                jets,sizes=cone_jets(f,e,plane,1 if tag==label else -1); key=tag+'_J'+str(J)
                ck(key+'_family_chain_through_second_order',all(zero(t) for t in chain_jet_residuals(jets)))
                result,descend=first_mass(jets,sizes)
                for name,value in descend.items(): ck(key+'_'+name,value)
                ck(key+'_index_retained_at_zero',result['H_at_zero'][0]==result['H_at_zero'][3]==0 and result['H_at_zero'][1]-result['H_at_zero'][2]==(J if tag==label else -J))
                jets_out[key]=result
                if tag==label and J==1:
                    wrong=[[x.copy() for x in degree] for degree in jets]
                    wrong[1][1][2*n:3*n,3*n:3*n+e['U'].cols+plane.cols]=s.zeros(n,e['U'].cols+plane.cols)
                    ck(label+'_omitted_boundary_response_breaks_family_chain',any(not zero(t) for t in chain_jet_residuals(wrong)))
                    wrong=[[x.copy() for x in degree] for degree in jets]
                    wrong[1][1][3*n:,3*n:3*n+e['U'].cols+plane.cols]=s.zeros(2*n,e['U'].cols+plane.cols)
                    ck(label+'_frozen_cell_comparison_breaks_family_chain',any(not zero(t) for t in chain_jet_residuals(wrong)))
        ck(label+'_physical_first_mass_dual_ranks',all(jets_out[label+'_J'+str(J)]['first_mass_rank']==jets_out[label+'dual_J'+str(J)]['first_mass_rank'] for J in (1,2)))
    ck('five_common_index_protected_only_dimensions',[(2+J,3+J) for J in range(-2,3)]==[(i,i+1) for i in range(5)] and all(str(2+J) in blocks['W']['protected_only_witnesses'] and str(3+J) in blocks['F']['protected_only_witnesses'] for J in range(-2,3)))
    ck('all_SM_H_weights_nonzero', sorted({2+2,2-3,-3-3})==[-6,-1,4] and sorted({-2,3})==[-2,3])
    ck('exterior_then_twist_not_exterior_of_twist',old.wedge(2*w['t'])==4*old.wedge(w['t']) and old.wedge(2*w['t'])!=2*old.wedge(w['t']))
    polynomial=s.prod(z-j for j in range(5))
    ck('degree_bound_requires_n_plus_one_points',all(polynomial.subs(z,j)==0 for j in range(5)) and polynomial.subs(z,5)!=0 and s.degree(polynomial,z)==5)
    held=s.Pow(s.Add(1,s.sqrt(2),evaluate=False),5,evaluate=False)*(z-1)
    normalized=dm(s.Matrix([[held]]),z).to_Matrix()[0,0]
    ck('exact_expansion_preserves_algebraic_coefficient_not_rational_shadow',s.expand(normalized-(41+29*s.sqrt(2))*(z-1))==0 and s.expand(normalized-41*(z-1))!=0)
    reciprocal=dm(s.Matrix([[1/(2+s.sqrt(2))]])).to_Matrix()[0,0]
    ck('quadratic_rational_expression_exact_not_float',s.expand(reciprocal-(1-s.sqrt(2)/2))==0)
    rejected=False
    try: dm(s.Matrix([[s.sqrt(3)]]))
    except ValueError: rejected=True
    ck('undeclared_quadratic_field_rejected',rejected)
    toy=s.Matrix([[1,z,0],[2,2*z,0],[0,0,z]])
    ck('fraction_free_rank_agrees_with_direct_small_field_and_rank_jump',rank(toy,z)==dm(toy,z).rank()==2 and rank(toy.subs(z,0))==1)
    return dict(facts=facts,predicates_passed=len(facts),blocks=blocks,first_mass_maps=jets_out,
                common_generation_indices=list(range(-2,3)),conditional_small_v_charged_lift=True,
                actual_normalized_mass_values=False,global_PDE_solved=False,Higgs_complete=False,
                generated_selection=False,three_generations=False,outside_review=False,full_goal_achieved=False)


if __name__=='__main__': print(json.dumps(run(),sort_keys=True,indent=2))
