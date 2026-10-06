"""Exact cyclic SDR at the fixed silver cusp; no completed physical theory."""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
FIELD = s.QQ.algebraic_field(s.sqrt(2))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


def dm(a): return DomainMatrix.from_Matrix(a).convert_to(FIELD)
def mm(a, b): return dm(a).matmul(dm(b)).to_Matrix()
def inv(a): return dm(a).inv().to_Matrix()
def norm(a): return dm(a).to_Matrix()
def zero(a): return a == s.zeros(a.rows, a.cols) or dm(a).is_zero_matrix
def rank(a): return dm(a).rank() if a.rows and a.cols else 0


def kernel(a):
    if not a.cols: return s.zeros(0, 0)
    reduced, piv = dm(a).rref()
    reduced = reduced.to_Matrix()
    free = [j for j in range(a.cols) if j not in piv]
    out = s.zeros(a.cols, len(free))
    for k, j in enumerate(free):
        out[j, k] = 1
        for i, p in enumerate(piv): out[p, k] = -reduced[i, j]
    return norm(out)


def projector(k, g):
    return mm(mm(k, inv(mm(mm(k.T, g), k))), mm(k.T, g)) if k.cols else s.zeros(k.rows)


def log_nil(p):
    n = p.rows; z = p-s.eye(n); power = s.eye(n); out = s.zeros(n)
    for j in range(1, n+1):
        power = mm(power, z)
        if zero(power): return norm(out)
        out += s.Rational((-1)**(j+1), j)*power
    raise ValueError('nonunipotent peripheral matrix')


def exp_nil(a):
    n = a.rows; out = s.eye(n); power = s.eye(n)
    for j in range(1, n+1):
        power = mm(power, a)
        if zero(power): return norm(out)
        out += power/factorial(j)
    raise ValueError('nonnilpotent logarithm')


def integral_exp(a):
    out = s.eye(a.rows); power = s.eye(a.rows)
    for j in range(1, a.rows+1):
        power = mm(power, a)
        if zero(power): return norm(out)
        out += power/factorial(j+1)
    raise ValueError('nonnilpotent integration input')


def exterior_lie(a):
    pairs = list(combinations(range(a.rows), 2)); lookup = {p:i for i,p in enumerate(pairs)}
    out = s.zeros(len(pairs))
    for j, (u, v) in enumerate(pairs):
        for k in range(a.rows):
            for x,y,c in ((k,v,a[k,u]),(u,k,a[k,v])):
                if x != y: out[lookup[tuple(sorted((x,y)))],j] += (1 if x<y else -1)*c
    return norm(out)


def adjoint_basis():
    basis = []
    for i in range(5):
        for j in range(5):
            if i != j:
                z = s.zeros(5); z[i,j] = 1; basis.append(z)
    for i in range(4):
        z = s.zeros(5); z[i,i] = 1; z[4,4] = -1; basis.append(z)
    return basis


def adjoint_lie(a, basis):
    cols = []
    for x in basis:
        z = mm(a,x)-mm(x,a)
        assert s.trace(z) == 0
        cols.append(s.Matrix([z[i,j] for i in range(5) for j in range(5) if i!=j]+[z[i,i] for i in range(4)]))
    return s.Matrix.hstack(*cols)


def adjoint_group(a,basis):
    ai=inv(a);cols=[]
    for x in basis:
        z=mm(mm(a,x),ai)
        cols.append(s.Matrix([z[i,j] for i in range(5) for j in range(5) if i!=j]+[z[i,i] for i in range(4)]))
    return s.Matrix.hstack(*cols)


def word(rep, text):
    letters = dict(rep); letters.update({g.upper():inv(x) for g,x in rep.items()})
    out = s.eye(rep['a'].rows)
    for c in text: out = mm(out, letters[c])
    return out


@lru_cache(None)
def literal():
    old = load('cyclic_literal_native', HERE.parent/'silver_operator_gate_2026_10_05/probe.py')
    data = json.loads((HERE.parent/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v = old.four(data)
    c = s.Matrix([s.Rational(a)+s.sqrt(2)*s.Rational(b) for a,b in data['cocycle_Qsqrt2_pairs']])
    w = old.extension(v,c)
    assert all(word(w,r)==s.eye(5) for r in data['relators'])
    p,q = [word(w,r) for r in data['cusp_words']]
    assert all(word(w,r)==s.diag(word(v,r),1) for r in data['cusp_words'])
    a,b = log_nil(p),log_nil(q)
    return old,data,w,p,q,a,b


def sdr(a,b,g=None):
    n = a.rows; g = s.eye(n) if g is None else g
    d0 = a.col_join(b); d1 = (-b).row_join(a)
    g1 = s.diag(g,g); da0 = mm(mm(inv(g),d0.T),g1); da1 = mm(mm(inv(g1),d1.T),g)
    p0 = projector(kernel(d0),g); p2 = projector(kernel(da1),g)
    r0 = inv(mm(da0,d0)+p0)-p0; r2 = inv(mm(d1,da1)+p2)-p2
    h1,h2 = mm(r0,da0),mm(da1,r2)
    p1 = norm(s.eye(2*n)-mm(d0,h1)-mm(h2,d1))
    d = s.zeros(4*n); d[n:3*n,:n]=d0; d[3*n:,n:3*n]=d1
    h = s.zeros(4*n); h[:n,n:3*n]=h1; h[n:3*n,3*n:]=h2
    p = s.diag(p0,p1,p2)
    return dict(d=d,h=h,p=p,d0=d0,d1=d1,p1=p1,
                betti=[rank(p0),rank(p1),rank(p2)],n=n)


def wedge_gram(g):
    n=g.rows; out=s.zeros(4*n)
    out[:n,3*n:]=g;out[3*n:,:n]=g
    out[n:2*n,2*n:3*n]=g;out[2*n:3*n,n:2*n]=-g
    return out


def cyclic_residual(E,D=None,trace=None):
    n=E['n']; parity=s.diag(s.eye(n),-s.eye(2*n),s.eye(n))
    if D is None:
        d,h,p=E['d'],E['h'],E['p']; pairing=wedge_gram(trace)
    else:
        d,h,p=[s.diag(E[k],D[k]) for k in ('d','h','p')]
        j=wedge_gram(s.eye(n));pairing=s.zeros(8*n);pairing[:4*n,4*n:]=j;pairing[4*n:,:4*n]=j
        parity=s.diag(parity,parity)
    return dict(d=zero(mm(d.T,pairing)+mm(mm(parity,pairing),d)),
                h=zero(mm(h.T,pairing)-mm(mm(parity,pairing),h)),
                p=zero(mm(p.T,pairing)-mm(pairing,p)),
                isotropic=zero(mm(mm(h.T,pairing),h)))


def cell_comparison(a,b):
    n=a.rows;p,q=exp_nil(a),exp_nil(b);u,v=integral_exp(a),integral_exp(b)
    T=s.diag(u,v);T2=mm(u,v);d0=a.col_join(b);d1=(-b).row_join(a)
    g0=(p-s.eye(n)).col_join(q-s.eye(n));g1=(s.eye(n)-q).row_join(p-s.eye(n))
    td=s.diag(integral_exp(-a.T),integral_exp(-b.T))
    j=s.zeros(n).row_join(inv(p).T).col_join((-inv(q).T).row_join(s.zeros(n)))
    j0=s.zeros(n).row_join(s.eye(n)).col_join((-s.eye(n)).row_join(s.zeros(n)))
    ZE,ZD=kernel(d1),kernel(b.T.row_join(-a.T))
    difference=mm(mm(T.T,j),td)-j0
    return dict(T=T,checks=dict(chain0=zero(mm(T,d0)-g0),chain1=zero(mm(g1,T)-mm(T2,d1)),
        invertible=s.simplify(T.det())==1 and s.simplify(T2.det())==1,
        cup_on_all_closed=zero(mm(mm(ZE.T,difference),ZD))))


@lru_cache(None)
def trees(n):
    if n==1:return (None,)
    return tuple((x,y) for i in range(1,n) for x in trees(i) for y in trees(n-i))


def leaves(t):return 1 if t is None else leaves(t[0])+leaves(t[1])


def gauge_case(t,pos,root=True):
    assert t is not None
    nl=leaves(t[0]);side=0 if pos<nl else 1
    own,other=t[side],t[1-side]
    if own is None:
        return 'harmonic' if other is None else ('root_propagator' if root else 'internal_propagator')
    return gauge_case(own,pos if side==0 else pos-nl,False)


@lru_cache(None)
def run():
    old,data,w,P,Q,A,B=literal();checks={};blocks={}
    def ck(k,v):checks[k]=bool(v);assert checks[k],k
    ck('literal_relators_and_peripheral_split',all(word(w,r)==s.eye(5) for r in data['relators']) and all(word(w,r)==s.diag(word(old.four(data),r),1) for r in data['cusp_words']))
    ck('two_unipotent_logs',exp_nil(A)==P and exp_nil(B)==Q and zero(mm(A,B)-mm(B,A)))
    span=rank(s.Matrix.hstack(s.Matrix(list(A)),s.Matrix(list(B))))
    ck('cusp_log_directions_not_principal_singleton',span==2)
    basis=adjoint_basis();trace=s.Matrix([[s.trace(x*y) for y in basis] for x in basis]);metric=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    NA,NB=adjoint_lie(A,basis),adjoint_lie(B,basis)
    ck('neutral_invariant_trace',zero(mm(NA.T,trace)+mm(trace,NA)) and zero(mm(NB.T,trace)+mm(trace,NB)))
    ck('neutral_positive_induced_metric',metric==s.diag(s.eye(20),s.eye(4)+s.ones(4)) and metric.det()>0)
    logs={'W':(A,B),'F':(exterior_lie(A),exterior_lie(B)), 'N':(NA,NB),'gauge':(s.zeros(1),s.zeros(1))}
    ck('induced_exterior_and_neutral_logs_are_actual_holonomies',all(exp_nil(x)==y for x,y in ((logs['F'][0],old.wedge(P)),(logs['F'][1],old.wedge(Q)),(NA,adjoint_group(P,basis)),(NB,adjoint_group(Q,basis)))))
    native_flag_planes={}
    for label,(a,b) in logs.items():
        E=sdr(a,b,metric if label=='N' else None);blocks[label]=E
        n=E['n'];d,h,p=E['d'],E['h'],E['p'];I=s.eye(4*n)
        ck(label+'_SDR',zero(mm(d,d)) and zero(mm(d,h)+mm(h,d)-(I-p)) and zero(mm(h,h)) and zero(mm(h,p)) and zero(mm(p,h)) and zero(mm(p,p)-p) and zero(mm(d,p)) and zero(mm(p,d)))
        ck(label+'_nonvacuous_sign_control',zero(d) if label=='gauge' else not zero(mm(d,-h)+mm(-h,d)-(I-p)))
        if label in ('W','F'):
            D=sdr(-a.T,-b.T);blocks[label+'dual']=D
            ck(label+'_dual_SDR',zero(mm(D['d'],D['h'])+mm(D['h'],D['d'])-(I-D['p'])) and zero(mm(D['h'],D['h'])) and zero(mm(D['p'],D['h'])) and zero(mm(D['h'],D['p'])))
            for key,value in cyclic_residual(E,D).items():ck(label+'_cyclic_'+key,value)
            cmp=cell_comparison(a,b)
            for key,value in cmp['checks'].items():ck(label+'_cell_'+key,value)
            spectral=load('cyclic_spectral_source_'+label,HERE.parent/'silver_spectral_completion_2026_10_05/probe.py')
            rep=w if label=='W' else {g:old.wedge(m) for g,m in w.items()}
            ce,cd=[spectral.Complex(r,data) for r in (rep,{g:inv(m).T for g,m in rep.items()})]
            transformed=mm(mm(E['p1'],inv(cmp['T'])),ce.flag)
            J0=s.zeros(n).row_join(s.eye(n)).col_join((-s.eye(n)).row_join(s.zeros(n)))
            td=s.diag(integral_exp(-a.T),integral_exp(-b.T))
            good=[]
            for ell in range(ce.H.cols+1):
                L=ce.flag[:,:ell];LD=mm(cd.H,kernel(mm(mm(L.T,spectral.cup(ce)),cd.H)))
                LL=transformed[:,:ell];DL=mm(mm(D['p1'],inv(td)),LD)
                good.append(rank(LL)==ell and rank(DL)==ce.H.cols-ell and zero(mm(mm(LL.T,J0),DL)))
            ck(label+'_all_previous_flag_planes_transport',all(good))
            native_flag_planes[label]=len(good)
        else:
            for key,value in cyclic_residual(E,trace=trace if label=='N' else s.eye(1)).items():ck(label+'_cyclic_'+key,value)
            if label=='N':
                for key,value in cell_comparison(a,b)['checks'].items():ck(label+'_cell_'+key,value)
        ck(label+'_higher_gauge_leaf_contraction',zero(mm(h,p)) and zero(mm(h,h)) and zero(mm(p,h)))
    wrong=sdr(-A.T,-B.T,s.diag(1,2,3,4,5))
    ck('wrong_dual_metric_still_SDR',zero(mm(wrong['d'],wrong['h'])+mm(wrong['h'],wrong['d'])-(s.eye(20)-wrong['p'])))
    ck('wrong_dual_metric_not_cyclic',not cyclic_residual(blocks['W'],wrong)['h'])
    x,y,z=basis[0]-basis[4],basis[5]-basis[9],basis[8]-basis[1]
    ck('compact_gauge_binary_action_not_deleted',all(t.T==-t for t in (x,y,z)) and s.trace(x*(y*z-z*y))==2)
    ck('all24_gauge_generators_have_nonzero_5_and_10_actions',len(basis)==24 and all(not zero(x) and not zero(exterior_lie(x)) and not zero(adjoint_lie(x,basis)) for x in basis))
    cases={'harmonic':0,'internal_propagator':0,'root_propagator':0};nodes=0
    for n in range(3,8):
        for t in trees(n):
            for pos in range(n):cases[gauge_case(t,pos)]+=1;nodes+=1
    ck('complete_bounded_tree_instrument',nodes==sum(n*len(trees(n)) for n in range(3,8)) and min(cases.values())>0)
    multiplicity={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(multiplicity[k]*v['betti'][j] for k,v in blocks.items()) for j in range(3)]
    fulln=sum(multiplicity[k]*v['n'] for k,v in blocks.items())
    Ldim=10*blocks['W']['betti'][1]+5*blocks['F']['betti'][1]+blocks['N']['betti'][1]//2+24
    ck('full248_roster_and_harmonic_Lagrangian_dimension',fulln==248 and H==[100,200,100] and Ldim==100 and 24+Ldim+(H[2]-24)==sum(H)//2)
    return dict(checks=checks,passed=len(checks),failed=[],profile=dict(cusp_log_span=span,
        boundary_betti={k:v['betti'] for k,v in blocks.items()},full_coefficient_dimension=fulln,
        full_H=H,Ah_dimensions=[24,Ldim,H[2]-24],tree_leaf_cases=cases,tree_positions=nodes,
        gauge_basis_count=len(basis)),native_only_flag_dimensions_checked=native_flag_planes,
        all_order_charged_physical_completion=False,physical_action_stationary=False,
        genesis_boundary_selected=False,physical_goal_achieved=False,non_author_acceptance=False)


if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
