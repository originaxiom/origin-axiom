"""Exact tensor-closed cohomology screen, not a physical-domain theorem."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from types import SimpleNamespace

import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
spec=importlib.util.spec_from_file_location('silver_tensor_base',HERE.parent/'silver_global_boundary_2026_10_04/verify.py')
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
m=g.m
red,mul,rank,kernel,zero,inverse=g.red,g.mul,g.rank,g.kernel,g.zero,g.inverse


def sign(indices):
    if len(set(indices))!=len(indices):
        return 0
    return (-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))


def tensor(p,q):
    left=list(combinations(range(5),p)); right=list(combinations(range(5),q))
    target=list(combinations(range(5),2 if p+q in (2,3) else 1))
    out=s.zeros(len(target),len(left)*len(right))
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            ab=a+b
            for k,c in enumerate(target):
                if p+q==2:
                    out[k,i*len(right)+j]=sign(ab) if tuple(sorted(ab))==c else 0
                else:
                    out[k,i*len(right)+j]=sign(ab+c)
    return out


def channels():
    out=[('E','E','F',tensor(1,1)),('E','F','F*',tensor(1,2)),('F','F','E*',tensor(2,2))]
    swap=lambda x:x[:-1] if x.endswith('*') else x+'*'
    return out+[(swap(a),swap(b),swap(c),T) for a,b,c,T in out]


def apply(T,u,v):
    return mul(T,s.kronecker_product(u,v))


def columns(rows,n):
    return s.Matrix.hstack(*rows) if rows else s.zeros(n,0)


def cup(T,A,B,X,Y):
    n,k=A.n,B.n
    return columns([red(apply(T,X[:n,i],mul(B.P,Y[k:,j]))-
                        apply(T,X[n:,i],mul(B.Q,Y[:k,j])))
                    for i in range(X.cols) for j in range(Y.cols)],T.rows)


def action(T,X,Y,second=False):
    n=Y.rows//2
    op=(lambda u,v:apply(T,v,u)) if second else (lambda u,v:apply(T,u,v))
    return columns([op(X[:,i],Y[:n,j]).col_join(op(X[:,i],Y[n:,j]))
                    for i in range(X.cols) for j in range(Y.cols)],2*T.rows)


def quotient(C,B):
    base_rank=rank(B)
    escaped_rank=rank(B.row_join(C))-base_rank
    witness=None
    if escaped_rank:
        j=next(j for j in range(C.cols) if rank(B.row_join(C[:,j]))>base_rank)
        witness=[str(x) for x in C[:,j]]
        assert rank(B.row_join(C[:,j]))==base_rank+1
    return {'rank':escaped_rank,'witness':witness}


def analyze_channel(A,B,H,T):
    # Here each record contains actual torus and global generator matrices.
    for name in A.rep:
        assert zero(mul(T,s.kronecker_product(A.rep[name],B.rep[name]))-mul(H.rep[name],T)), ('tensor equivariance',name)
    for name in ('P','Q'):
        assert zero(mul(T,s.kronecker_product(getattr(A,name),getattr(B,name)))-mul(getattr(H,name),T))
    inv=columns([apply(T,A.H0[:,i],B.H0[:,j])
                 for i in range(A.H0.cols) for j in range(B.H0.cols)],H.n)
    assert zero(mul(H.D,inv))
    c01=action(T,A.H0,B.L)
    c10=action(T,B.H0,A.L,second=True)
    assert zero(mul(H.Ft,c01)) and zero(mul(H.Ft,c10))
    allowed=H.D.row_join(H.L)
    # Degree-zero/one products descend under a change by an exact.
    assert quotient(action(T,A.H0,B.D),H.D)['rank']==0
    assert quotient(action(T,B.H0,A.D,second=True),H.D)['rank']==0
    c11=cup(T,A,B,A.L,B.L)
    assert quotient(cup(T,A,B,A.D,B.H),H.Ft)['rank']==0
    assert quotient(cup(T,A,B,A.H,B.D),H.Ft)['rank']==0
    # Graded exchange on the full harmonic bases, using the flipped tensor.
    flipped=s.zeros(T.rows,A.n*B.n)
    for i in range(A.n):
        for j in range(B.n):
            flipped[:,j*A.n+i]=T[:,i*B.n+j]
    direct=cup(T,A,B,A.H,B.H)
    reverse=cup(flipped,B,A,B.H,A.H)
    reverse=columns([reverse[:,j*A.H.cols+i] for i in range(A.H.cols)
                     for j in range(B.H.cols)],H.n)
    assert quotient(red(direct+reverse),H.Ft)['rank']==0
    return {'degree_01':quotient(c01,allowed),'degree_10':quotient(c10,allowed),
            'degree_11':quotient(c11,H.Ft),'equivariant':True,
            'descends_to_cohomology':True,'graded_exchange':True}


def record(E,B,L):
    return SimpleNamespace(n=E.n,rep=E.rep,P=E.P,Q=E.Q,D=E.D,
                           Ft=B.F,H=B.H,H0=kernel(E.D),L=L)


def make_spaces(one,two):
    return {'E':record(one['E'],one['BE'],one['BE'].L),
            'E*':record(one['D'],one['BD'],one['LD']),
            'F':record(two['E'],two['BE'],two['BE'].L),
            'F*':record(two['D'],two['BD'],two['LD'])}


def run_spaces(spaces):
    return {a+' x '+b+' -> '+h:analyze_channel(spaces[a],spaces[b],spaces[h],T)
            for a,b,h,T in channels()}


def trivial(n,tau):
    I=s.eye(n)
    return SimpleNamespace(n=n,rep={'a':I},P=I,Q=I,D=s.zeros(2*n,n),
                           Ft=s.zeros(n,2*n),H=s.eye(2*n),H0=I,L=I.col_join(tau*I))


@lru_cache(None)
def controls():
    spaces={name:trivial(5 if name.startswith('E') else 10,s.I) for name in ('E','E*','F','F*')}
    common=run_spaces(spaces)
    assert all(c[k]['rank']==0 for c in common.values() for k in ('degree_01','degree_10','degree_11'))
    E,F=trivial(5,0),trivial(10,1)
    C=cup(tensor(1,2),E,F,E.L,F.L)
    assert rank(C)==10
    T=tensor(1,1)
    q=s.diag(2,3,5,7,s.Rational(1,210))
    old,_,_=m.inputs()
    exterior=old.exterior(q)
    assert zero(mul(T,s.kronecker_product(q,q))-mul(exterior,T))
    assert not zero(mul(T,s.kronecker_product(q,q))-mul(inverse(exterior).T,T))
    a,b=trivial(5,0),trivial(5,1)
    direct=cup(T,a,b,a.L,b.L)
    reverse=cup(T,b,a,b.L,a.L)
    reverse=columns([reverse[:,j*5+i] for i in range(5) for j in range(5)],10)
    assert zero(direct-reverse) and rank(direct+reverse)>0
    return {'status':'PASS','common_line_all_six_channels_close':True,
            'distinct_line_cup_rank':rank(C),'wrong_dual_detected':True,
            'wrong_exchange_sign_detected':True}


@lru_cache(None)
def actual_members():
    old,data,records=m.inputs()
    output=[]
    for label,state in data['states'].items():
        old.check_marking(label,state)
        f=old.four(state)
        for member in state['members']:
            char=member['nu on a, b, t']
            saved=next(r for r in records if r['signed_word']==label and r['character']==char)
            c=s.Matrix([s.sympify(x) for x in saved['peripherally_zero_cocycle']])
            V={k:char[k]*f[k] for k in m.GEN}
            print(json.dumps({'progress':'starting','carrier':state['SnapPy'],'character':char}),flush=True)
            amplitudes={}
            for amplitude in (0,1):
                rep=old.extension(V,amplitude*c)
                one=g.analyze(rep,state,saved['splitW' if amplitude==0 else 'W'])
                two=g.analyze({k:old.exterior(A) for k,A in rep.items()},state,
                              saved['split_wedge2W' if amplitude==0 else 'wedge2W'])
                spaces=make_spaces(one,two)
                results=run_spaces(spaces)
                amplitudes[str(amplitude)]={'channels':results,
                    'dimensions':{k:{'H0':v.H0.cols,'H1':v.H.cols,'L':v.L.cols} for k,v in spaces.items()},
                    'interior_pair':[one['summary']['difference'],two['summary']['difference']],
                    'all_tested_products_close':all(r[k]['rank']==0 for r in results.values()
                                                   for k in ('degree_01','degree_10','degree_11'))}
            row={'carrier':state['SnapPy'],'signed_word':label,'character':char,'amplitudes':amplitudes}
            output.append(row)
            print(json.dumps({'member':row},sort_keys=True),flush=True)
    return output


if __name__=='__main__':
    print(json.dumps({'controls':controls()},sort_keys=True),flush=True)
    rows=actual_members()
    print(json.dumps({'status':'PASS','members':len(rows),
                     'scope':'cohomology tensor-closure diagnostic, not physical admission'}),flush=True)
