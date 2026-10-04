"""Charged graded boundary candidate, with its compact-gauge obstruction."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest,path = line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
spec = importlib.util.spec_from_file_location('charged_boundary_cyclic',HERE.parent/'silver_cyclic_boundary_2026_10_04/verify.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
v,t,g,m,b = c.v,c.v.t,c.g,c.m,c.b
red,mul,rank,kernel,zero,inverse = c.red,c.mul,c.rank,c.kernel,c.zero,c.inverse


def independent(A):
    return m.independent_modulo(s.zeros(A.rows,0),A)


def contraction():
    pairs = list(combinations(range(5),2))
    T = s.zeros(5,50)
    for j,(a,z) in enumerate(pairs):
        T[z,10*a+j] = 1
        T[a,10*z+j] = -1
    return T


def reconstruct(x):
    return red(sum((x[i]*M for i,M in enumerate(c.basis(5))),s.zeros(5)))


def trace_rank_one(p,alpha):
    X = mul(p,alpha.T)
    return c.coords(red(X-s.trace(X)*s.eye(5)/5))


def neutral_action(p,L):
    return t.columns([mul(reconstruct(L[:24,j]),p).col_join(mul(reconstruct(L[24:,j]),p))
                      for j in range(L.cols)],10)


def lagrangian_complete(O,W):
    assert O.rows == O.cols and rank(O) == O.rows and zero(O+O.T)
    assert O.rows % 2 == 0 and zero(mul(mul(W.T,O),W))
    out = independent(W)
    while 2*out.cols < O.rows:
        choices = m.independent_modulo(out,kernel(mul(out.T,O)))
        assert choices.cols > 0
        out = out.row_join(choices[:,0])
    assert 2*out.cols == O.rows and zero(mul(mul(out.T,O),out))
    assert rank(out.row_join(W)) == out.cols
    return out


def neutral_data(rep,state):
    N = m.Global({key:c.adjoint(A) for key,A in rep.items()},state)
    bas = c.basis(5)
    S = s.Matrix([[s.trace(x*y) for y in bas] for x in bas])
    for A in N.rep.values():
        assert zero(mul(mul(A.T,S),A)-S)
    F = (s.eye(24)-N.Q).row_join(N.P-s.eye(24))
    D = independent(N.D)
    H = m.independent_modulo(D,kernel(F))
    DH = D.row_join(H)
    pivots = m.dm(DH.T).rref()[1]
    left = inverse(DH.extract(pivots,list(range(DH.cols))))
    Q = s.zeros(H.cols,48)
    for j,pivot in enumerate(pivots):
        Q[:,pivot] = left[D.cols:,j]
    assert zero(mul(Q,D)) and zero(mul(Q,H)-s.eye(H.cols))
    J = mul(g.group_cup(N),s.diag(S,S))
    O = mul(mul(H.T,J),H)
    assert rank(O) == H.cols == 2*N.t0 and zero(O+O.T)
    R = m.independent_modulo(D,N.RZ)
    assert zero(mul(mul(R.T,J),R)) and 2*R.cols == H.cols
    return N,F,H,Q,O,R


def charged_complex(one,p,state):
    E,D = one['E'],one['D']
    R2,F = b.restriction2(E,state)
    R2D,FD = b.restriction2(D,state)
    H2,H2D = kernel(F.conjugate().T),kernel(FD.conjugate().T)
    A2D = mul(H2D,kernel(mul(p.T,H2D)))
    assert H2D.cols-A2D.cols == 1 and zero(mul(p.T,A2D))
    left = b.fiber((E.B,E.F),(E.D,F),(s.eye(5),E.R,R2),(p,one['BE'].L,H2))
    right = b.fiber((D.B,D.F),(D.D,FD),(s.eye(5),D.R,R2D),
                    (s.zeros(5,0),one['LD'],A2D))
    assert left['H'] == right['H'][::-1]
    return {'E':left,'dual':right,'H1_difference':left['H'][1]-right['H'][1],
            'A0_dimensions':[1,0],'A2_dimensions':[H2.cols,A2D.cols]}


@lru_cache(None)
def controls():
    O = s.zeros(3).row_join(s.eye(3)).col_join((-s.eye(3)).row_join(s.zeros(3)))
    W = s.eye(6)[:,[0,1]]
    L = lagrangian_complete(O,W)
    bad = s.eye(6)[:,[0,3]]
    assert not zero(bad.T*O*bad)
    # The actual ten-dimensional sl5 module has no common fixed vectors.
    bas = c.basis(5); pairs = list(combinations(range(5),2)); mods = []
    for A in bas:
        M = s.zeros(10)
        for j,(a,z) in enumerate(pairs):
            for i,(u,w) in enumerate(pairs):
                M[i,j] = (A[u,a]*int(w==z)-A[w,a]*int(u==z)
                          +A[w,z]*int(u==a)-A[u,z]*int(w==a))
        mods.append(M)
    assert kernel(s.Matrix.vstack(*mods)).cols == 0
    # ad of a vector in the abelian ideal maps sl5 to the ideal and squares to zero.
    p = s.eye(10)[:,0]
    N = s.zeros(34)
    N[24:,:24] = s.Matrix.hstack(*(-M*p for M in mods))
    assert rank(N) > 0 and N*N == s.zeros(34)
    # Compact positive: the real su2 cross-product adjoints are skew for I.
    compact = [s.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),
               s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),
               s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
    assert all(A.T+A == s.zeros(3) for A in compact)
    E = s.Matrix([[0,1],[0,0]])
    assert E != s.zeros(2) and E*E == s.zeros(2)
    assert -s.I*(s.I*(E+E.T)) + (E-E.T) == 2*E
    # Complex nilpotence does not exclude the compact real form su2.
    T = contraction()
    assert t.apply(T,s.eye(5)[:,0],s.eye(10)[:,0]) == s.eye(5)[:,1]
    return {'status':'PASS','symplectic_extension_dimension':L.cols,
            'nonisotropic_input_detected':True,'module_fixed_dimension':0,
            'abelian_ideal_adjoint_rank':rank(N),'abelian_ideal_adjoint_square_zero':True,
            'compact_su2_positive':True,'complex_nilpotent_alone_is_not_obstruction':True,
            'contraction_orientation_control':True}


@lru_cache(None)
def actual_members():
    old,data,records = m.inputs()
    out = []
    for label,state in data['states'].items():
        old.check_marking(label,state)
        four = old.four(state)
        for member in state['members']:
            char = member['nu on a, b, t']
            saved = next(r for r in records if r['signed_word']==label and r['character']==char)
            coc = s.Matrix([s.sympify(z) for z in saved['peripherally_zero_cocycle']])
            V = {key:char[key]*four[key] for key in m.GEN}
            amps = {}
            for amp in (0,1):
                print(json.dumps({'progress':'charged and neutral closure','carrier':state['SnapPy'],
                                  'character':char,'amplitude':amp}),flush=True)
                rep = old.extension(V,amp*coc)
                one = g.analyze(rep,state,saved['splitW' if amp==0 else 'W'])
                two = g.analyze({key:old.exterior(A) for key,A in rep.items()},state,
                                saved['split_wedge2W' if amp==0 else 'wedge2W'])
                spaces = t.make_spaces(one,two)
                pars = v.surviving_parameters(spaces)
                K = s.Matrix([[s.sympify(z) for z in row] for row in pars['E']['kernel_coordinates']])
                p = mul(spaces['E'].H0,K)
                assert p.cols == rank(p) == 1 and zero(mul(spaces['E'].D,p))
                assert zero(t.apply(t.tensor(1,1),p,p))
                errors = []
                Pform = s.diag(p,p)
                allowedE = spaces['E'].D.row_join(spaces['E'].L)
                rowsE = kernel(allowedE.T).T
                form_choices = kernel(mul(rowsE,Pform))
                alpha = spaces['E*'].L
                evals = mul(p.T,alpha[:5,:]).col_join(mul(p.T,alpha[5:,:]))
                phi = form_choices[:,0] if form_choices.cols else s.zeros(2,0)
                if phi.cols == 0 or rank(phi.row_join(evals)) != 1:
                    errors.append('no common gauge form line')
                T = contraction()
                for key in m.GEN:
                    assert zero(mul(T,s.kronecker_product(rep[key],spaces['F*'].rep[key]))-
                                mul(spaces['E*'].rep[key],T))
                charged = {}
                for name,target,tensor in [('E','F',t.tensor(1,1)),('F','F*',t.tensor(1,2)),('F*','E*',T)]:
                    prod = t.action(tensor,p,spaces[name].L)
                    assert zero(mul(spaces[target].Ft,prod))
                    charged[name+' to '+target] = t.quotient(prod,spaces[target].D.row_join(spaces[target].L))
                if any(row['rank'] for row in charged.values()):
                    errors.append('charged action escapes')
                N,F,H,Q,O,R = neutral_data(rep,state)
                forced = t.columns([trace_rank_one(p,alpha[:5,j]).col_join(trace_rank_one(p,alpha[5:,j]))
                                    for j in range(alpha.cols)],48)
                assert zero(mul(F,forced))
                W = independent(mul(Q,forced))
                wi = zero(mul(mul(W.T,O),W))
                L = lagrangian_complete(O,W) if wi else None
                if not wi:
                    errors.append('forced neutral space not isotropic')
                old_escape = t.quotient(neutral_action(p,R),allowedE)
                new_escape = None
                if L is not None:
                    LN = mul(H,L)
                    assert rank(L.row_join(mul(Q,forced))) == L.cols
                    new_escape = t.quotient(neutral_action(p,LN),allowedE)
                    if new_escape['rank']:
                        errors.append('new neutral action escapes')
                    # Check the exact orthogonal constraint space, not only the chosen L.
                    Vn = kernel(mul(rowsE,neutral_action(p,H)))
                    expected = kernel(mul(W.T,O))
                    assert rank(Vn.row_join(expected)) == Vn.cols == expected.cols
                end = charged_complex(one,p,state)
                ext = b.pair(two,state)
                diff = [end['H1_difference'],ext['H1_differences']['reversed']]
                if diff != ([0,0] if amp==0 else [-1,-1]):
                    errors.append('charged H1 target not recovered')
                full0 = 24+N.t0+10*(one['E'].t0+one['D'].t0)+5*(two['E'].t0+two['D'].t0)
                row = {'status':'PASS' if not errors else 'CONSTRUCTION_FAIL','errors':errors,
                    'E_parameter':[str(z) for z in p],'gauge_form_choices':form_choices.cols,
                    'gauge_form':[str(z) for z in phi],'gauge_evaluation_rank':rank(evals),
                    'charged_actions':charged,'neutral_H1':H.cols,'forced_neutral_rank':W.cols,
                    'forced_neutral_isotropic':wi,'old_neutral_escape':old_escape,'new_neutral_escape':new_escape,
                    'neutral_L_coordinates':None if L is None else [[str(z) for z in L.row(i)] for i in range(L.rows)],
                    'fundamental_complex':end,'exterior_complex':ext,'H1_differences':diff,
                    'parent_H':[full0,2*full0,full0],'allowed_A':[34,full0,full0-34],
                    'compact_gauge_identification':'excluded for k itself by noncentral abelian radical',
                    'physical_fermion_domain':'not derived'}
                amps[str(amp)] = row
            result = {'carrier':state['SnapPy'],'signed_word':label,'character':char,'amplitudes':amps}
            out.append(result)
            print(json.dumps({'member':result},sort_keys=True),flush=True)
    assert len(out) == 4
    return out


if __name__ == '__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows = actual_members()
    ok = sum(a['status']=='PASS' for row in rows for a in row['amplitudes'].values())
    print(json.dumps({'status':'EXECUTION_COMPLETE','members':len(rows),'complex_constructions_pass':ok,
                      'physical_completion':False}),flush=True)
