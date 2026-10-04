"""Cyclic cohomological completion, not a physical boundary-domain producer."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest, path = line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


v = load('silver_cyclic_variation', HERE.parent/'silver_boundary_variation_2026_10_04/verify.py')
b = load('silver_cyclic_complex', HERE.parent/'silver_boundary_complex_2026_10_04/verify.py')
g, m = v.t.g, v.t.m
red, mul, rank, kernel, zero, inverse = g.red, g.mul, g.rank, g.kernel, g.zero, g.inverse


def basis(n):
    off = [(i,j) for i in range(n) for j in range(n) if i != j]
    out = []
    for i,j in off:
        B = s.zeros(n); B[i,j] = 1; out.append(B)
    for i in range(n-1):
        B = s.zeros(n); B[i,i] = 1; B[n-1,n-1] = -1; out.append(B)
    return out


def coords(B):
    n = B.rows
    assert s.expand(s.trace(B)) == 0
    return s.Matrix([B[i,j] for i in range(n) for j in range(n) if i != j]
                    + [B[i,i] for i in range(n-1)])


def adjoint(G):
    bas = basis(G.rows)
    GI = inverse(G)
    cols = []
    for B in bas:
        X = mul(mul(G,B),GI)
        col = coords(X)
        assert zero(sum((col[i]*T for i,T in enumerate(bas)),s.zeros(G.rows))-X)
        cols.append(col)
    return s.Matrix.hstack(*cols)


def neutral(rep, state):
    bas = basis(5)
    S = s.Matrix([[s.trace(A*B) for B in bas] for A in bas])
    assert rank(S) == 24
    ar = {name:adjoint(A) for name,A in rep.items()}
    for A in ar.values():
        assert zero(mul(mul(A.T,S),A)-S)
    E = m.Global(ar,state)
    F = (s.eye(24)-E.Q).row_join(E.P-s.eye(24))
    Z = kernel(F)
    H = m.independent_modulo(E.D,Z)
    R = m.independent_modulo(E.D,E.RZ)
    J = mul(g.group_cup(E),s.diag(S,S))
    assert zero(mul(mul(E.D.T,J),Z)) and zero(mul(mul(Z.T,J),E.D))
    omega = mul(mul(H.T,J),H)
    assert zero(omega+omega.T) and rank(omega) == H.cols
    assert zero(mul(mul(R.T,J),R))
    assert H.cols == 2*E.t0 == 2*R.cols
    assert R.cols == E.h1-E.interior
    return {'H0_global':E.h0,'H1_global':E.h1,'H1_interior':E.interior,
            'H0_boundary':E.t0,'H1_boundary':H.cols,'restriction_dimension':R.cols,
            'trace_rank':24,'cup_rank':rank(omega),'isotropic':True}


@lru_cache(None)
def controls():
    H = s.diag(1,-1); E = s.Matrix([[0,1],[0,0]]); F = E.T; O = s.zeros(2)
    # forms: 0=scalar, 1=dx, 2=dy, 3=dx^dy
    wedge = {(0,0):(1,0),(0,1):(1,1),(0,2):(1,2),(0,3):(1,3),
             (1,0):(1,1),(2,0):(1,2),(3,0):(1,3),
             (1,2):(1,3),(2,1):(-1,3)}
    def vector(A,form):
        out = s.zeros(12,1)
        out[3*form:3*form+3,0] = coords(A)
        return out
    def bracket(a,c):
        A,p=a; B,q=c
        if (p,q) not in wedge:
            return s.zeros(12,1)
        sign,r = wedge[p,q]
        return vector(sign*(A*B-B*A),r)
    allowed = [(H,0),(H,1),(E,2),(F,2),(E,3),(F,3)]
    A = s.Matrix.hstack(*(vector(*z) for z in allowed))
    assert rank(A) == 6
    P = s.zeros(12)
    bas = basis(2)
    for p in range(4):
        for q in range(4):
            if (p,q) in wedge and wedge[p,q][1] == 3:
                P[3*p:3*p+3,3*q:3*q+3] = wedge[p,q][0]*s.Matrix([[s.trace(x*y) for y in bas] for x in bas])
    assert rank(P) == 12 and zero(A.T*P*A)
    products = s.Matrix.hstack(*(bracket(x,y) for x in allowed for y in allowed))
    assert rank(A.row_join(products)) == rank(A)
    one = allowed[1:4]
    quadratic = s.Matrix.hstack(*(bracket(x,y) for x in one for y in one))
    assert rank(quadratic) == 2
    old = A[:,:4]
    assert rank(old.row_join(quadratic))-rank(old) == 2
    bad = bracket((E,0),(H,1))
    assert rank(A.row_join(bad))-rank(A) == 1
    # Trace self-duality holds for nonunitary conjugation, too.
    G = s.Matrix([[1,1+s.I],[0,1]])
    S = s.Matrix([[s.trace(x*y) for y in bas] for x in bas])
    ad = adjoint(G)
    assert zero(mul(mul(ad.T,S),ad)-S)
    return {'status':'PASS','allowed_dimension':6,'ambient_dimension':12,
            'quadratic_bracket_rank':2,'old_A2_zero_escape':2,
            'enlarged_gauge_escape':1,'nonunitary_trace_self_duality':True}


@lru_cache(None)
def actual_members():
    old,data,records = m.inputs()
    rows = []
    for label,state in data['states'].items():
        old.check_marking(label,state)
        f = old.four(state)
        for member in state['members']:
            char = member['nu on a, b, t']
            saved = next(r for r in records if r['signed_word']==label and r['character']==char)
            c = s.Matrix([s.sympify(z) for z in saved['peripherally_zero_cocycle']])
            V = {k:char[k]*f[k] for k in m.GEN}
            amps = {}
            for amplitude in (0,1):
                print(json.dumps({'progress':'neutral and charged boundary','carrier':state['SnapPy'],
                                  'character':char,'amplitude':amplitude}),flush=True)
                rep = old.extension(V,amplitude*c)
                adj = neutral(rep,state)
                one = g.analyze(rep,state,saved['splitW' if amplitude==0 else 'W'])
                two = g.analyze({k:old.exterior(A) for k,A in rep.items()},state,
                                saved['split_wedge2W' if amplitude==0 else 'wedge2W'])
                iso = [v.paired_isotropy(pair) for pair in (one,two)]
                pairs = [b.pair(pair,state) for pair in (one,two)]
                dims0 = 24+adj['H0_boundary']+sum(mult*(pair['E'].t0+pair['D'].t0)
                                               for mult,pair in ((10,one),(5,two)))
                dims1 = 48+adj['H1_boundary']+sum(mult*item['paired_H1_dimension']
                                               for mult,item in zip((10,5),iso))
                dimL = 24+adj['restriction_dimension']+sum(mult*item['allowed_dimension']
                                                          for mult,item in zip((10,5),iso))
                assert dims1 == 2*dims0 and 2*dimL == dims1
                allowed = [24,dimL,dims0-24]
                assert 2*sum(allowed) == 2*dims0+dims1
                diff = [pair['H1_differences']['reversed'] for pair in pairs]
                assert diff == ([0,0] if amplitude==0 else [0,-1])
                amps[str(amplitude)] = {'neutral':adj,'parent_H':[dims0,dims1,dims0],
                    'allowed_A':allowed,'charged_pair_isotropy':iso,'charged_reversed_H1_difference':diff,
                    'charged_complexes':pairs,'full_closure':'authored cyclic lemma with k=constant gauge sl5'}
            result = {'carrier':state['SnapPy'],'signed_word':label,'character':char,'amplitudes':amps}
            rows.append(result)
            print(json.dumps({'member':result},sort_keys=True),flush=True)
    assert len(rows) == 4
    return rows


if __name__ == '__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows = actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),'scope':'cohomological full-parent construction only'}),flush=True)
