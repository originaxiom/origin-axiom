"""Exact full-torus flag cones. No physical particle identification is made."""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sys

import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'noncompact_admission' / 'candidate.json'
INPUT_SHA = '6e433ff754f80944fb39defe9e75ca8363bb6ebe2add6b7ecbf4d435dc23669b'
ROOT2 = s.sqrt(2)
GEN = 'abt'


def clean(M):
    def quadratic(x):
        # Canonical exact radical reduction avoids inferred number-field embeddings.
        y = s.expand(s.radsimp(x))
        b = y.coeff(ROOT2)
        a = s.expand(y-b*ROOT2)
        assert a.is_Rational and b.is_Rational, ('outside Qsqrt2 in normalization',x,y)
        return a+b*ROOT2
    return s.Matrix(M).applyfunc(quadratic)


def mul(A, B):
    return clean(A * B)


def inverse(A):
    return clean(A.inv(method='DM'))


def zero(A):
    return clean(A) == s.zeros(*A.shape)


def rank(A):
    if not A.rows or not A.cols:
        return 0
    return DomainMatrix.from_Matrix(A, extension=True).rank()


def invword(word):
    return word.swapcase()[::-1]


def reduceword(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter.swapcase():
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)


def word(rep, w):
    n = rep['a'].rows
    A = s.eye(n)
    inv = {g: inverse(rep[g]) for g in GEN}
    for letter in w:
        A = mul(A, rep[letter] if letter in GEN else inv[letter.lower()])
    return A


def fox(rep, w):
    n = rep['a'].rows
    prefix = s.eye(n)
    out = [s.zeros(n) for _ in GEN]
    inv = {g: inverse(rep[g]) for g in GEN}
    for letter in w:
        g = letter.lower()
        k = GEN.index(g)
        if letter == g:
            out[k] = clean(out[k] + prefix)
            prefix = mul(prefix, rep[g])
        else:
            prefix = mul(prefix, inv[g])
            out[k] = clean(out[k] - prefix)
    return s.Matrix.hstack(*out)


def wedge2(A):
    pairs = list(combinations(range(A.rows), 2))
    return clean(s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                           for k,l in pairs] for i,j in pairs]))


def selector(n, indices):
    return s.Matrix(len(indices), n, lambda i,j: int(indices[i] == j))


def from_candidate(data, split):
    basis = [s.Matrix([[1,0],[0,0]]), s.Matrix([[0,0],[0,1]]),
             s.Matrix([[0,1],[1,0]]), s.Matrix([[0,s.I],[-s.I,0]])]
    cocycle = s.Matrix([s.Rational(a)+s.Rational(b)*ROOT2
                       for a,b in data['cocycle_Qsqrt2_pairs']])
    V, W = {}, {}
    for k,g in enumerate(GEN):
        M = s.Matrix([[s.Rational(a)+s.I*s.Rational(b) for a,b in row]
                      for row in data['holonomy'][g]])
        norm = s.sqrt(s.simplify(M.det()*s.conjugate(M.det())))
        columns = []
        for X in basis:
            Z = s.simplify(M*X*M.conjugate().T/norm)
            columns.append(s.Matrix([Z[0,0],Z[1,1],(Z[0,1]+Z[1,0])/2,
                                     (Z[0,1]-Z[1,0])/(2*s.I)]))
        V[g] = clean(data['nu'][g]*s.Matrix.hstack(*columns))
        W[g] = s.eye(5)
        W[g][:4,:4] = V[g]
        W[g][:4,4] = s.zeros(4,1) if split else cocycle[4*k:4*k+4,0]
    return V,W,cocycle


def core_and_boundary(rep, data):
    n = rep['a'].rows
    B = s.Matrix.vstack(*(rep[g]-s.eye(n) for g in GEN))
    F = s.Matrix.vstack(*(fox(rep,w) for w in data['relators']))
    p,q = data['cusp_words']
    P,Q = word(rep,p),word(rep,q)
    D = s.Matrix.vstack(P-s.eye(n),Q-s.eye(n))
    G = (s.eye(n)-Q).row_join(P-s.eye(n))
    R1 = s.Matrix.vstack(fox(rep,p),fox(rep,q))
    Ti = inverse(rep['t'])
    R2 = -mul(mul(Q,fox(rep,p)[:,:2*n]),s.diag(Ti,Ti))
    return (B,F),(D,G),(s.eye(n),R1,R2),(P,Q)


def check_map(C,T,f):
    B,F = C
    D,G = T
    f0,f1,f2 = f
    assert zero(mul(F,B)) and zero(mul(G,D)), 'not a complex'
    assert zero(mul(f1,B)-mul(D,f0)), 'not a chain map in degree zero'
    assert zero(mul(f2,F)-mul(G,f1)), 'not a chain map in degree one'


def cone(C,T,f):
    check_map(C,T,f)
    B,F = C
    D,G = T
    f0,f1,f2 = f
    n0,n1,n2 = B.cols,B.rows,F.rows
    t0,t1,t2 = D.cols,D.rows,G.rows
    dims = [n0,n1+t0,n2+t1,t2]
    d0 = B.col_join(f0)
    d1 = F.row_join(s.zeros(n2,t0)).col_join(f1.row_join(-D))
    d2 = f2.row_join(-G)
    return dims,(d0,d1,d2)


def full_fiber(C,T,f,A,inc):
    """Keep the entire attached complex, including its nonzero differential."""
    check_map(C,T,f)
    check_map(A,T,inc)
    B,F = C
    D,G = T
    BA,FA = A
    n0,n1,n2 = B.cols,B.rows,F.rows
    a0,a1,a2 = BA.cols,BA.rows,FA.rows
    t0,t1,t2 = D.cols,D.rows,G.rows
    dims = [n0+a0,n1+a1+t0,n2+a2+t1,t2]
    d0 = s.zeros(dims[1],dims[0])
    d0[:n1,:n0] = B
    d0[n1:n1+a1,n0:] = BA
    d0[n1+a1:,:n0] = f[0]
    d0[n1+a1:,n0:] = -inc[0]
    d1 = s.zeros(dims[2],dims[1])
    d1[:n2,:n1] = F
    d1[n2:n2+a2,n1:n1+a1] = FA
    d1[n2+a2:,:n1] = f[1]
    d1[n2+a2:,n1:n1+a1] = -inc[1]
    d1[n2+a2:,n1+a1:] = -D
    d2 = f[2].row_join(-inc[2]).row_join(-G)
    return dims,(d0,d1,d2)


def census(complex_data):
    dims,ds = complex_data
    assert zero(mul(ds[1],ds[0])) and zero(mul(ds[2],ds[1])), 'd squared nonzero'
    ranks = [rank(d) for d in ds]
    h = [dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
    assert min(h) >= 0
    chi = sum((-1)**j*v for j,v in enumerate(h))
    assert chi == sum((-1)**j*v for j,v in enumerate(dims))
    return {'dimensions':dims,'ranks':ranks,'H':h,'chi':chi}


def pack(M):
    data = []
    for x in M:
        x = s.expand(x)
        b = x.coeff(ROOT2)
        a = s.expand(x-b*ROOT2)
        assert a.is_Rational and b.is_Rational, ('outside Qsqrt2',x)
        data.append([str(a),str(b)])
    return {'rows':M.rows,'cols':M.cols,'Qsqrt2_pairs':data}


def main(out):
    assert hashlib.sha256(INPUT.read_bytes()).hexdigest() == INPUT_SHA
    data = json.loads(INPUT.read_text())
    assert data['cusp_words'] == ['abAB','abt']
    assert data['relators'] == ['taTbba','tbTbbabbab']
    checks = []

    def check(name, flag):
        assert flag, name
        checks.append(name)

    phi = {'a':'ABB','b':'BABBABB'}
    p,c = 'abAB','ab'
    phip = reduceword(''.join(phi[x] if x.islower() else invword(phi[x.lower()]) for x in p))
    check('puncture conjugacy as free words', phip == reduceword(invword(c)+p+c))
    rp = 't'+p+'T'+invword(phip)
    q = c+'t'
    check('two cell orientation as free words',
          reduceword(p+q+invword(p)+invword(q)) == reduceword(c+invword(rp)+invword(c)))
    rows,matrices = {},{}
    wrong_sign_seen = False
    attached_d_seen = False
    for split in (False,True):
        mode = 'split' if split else 'nonsplit'
        V,W,cocycle = from_candidate(data,split)
        BV = s.Matrix.vstack(*(V[g]-s.eye(4) for g in GEN))
        actual_c = s.zeros(12,1) if split else cocycle
        check(mode+' extension splitting test',
              (rank(BV.row_join(actual_c)) == rank(BV)) == split)
        exterior = {g:wedge2(W[g]) for g in GEN}
        reps = {'W':W,'Wdual':{g:inverse(W[g]).T for g in GEN},
                'wedge2W':exterior,'wedge2Wdual':{g:inverse(exterior[g]).T for g in GEN}}
        baseq = [1,1,1,1,-4]
        wq = [baseq[i]+baseq[j] for i,j in combinations(range(5),2)]
        weights = {'W':baseq,'Wdual':[-x for x in baseq],
                   'wedge2W':wq,'wedge2Wdual':[-x for x in wq]}
        for sector,rep in reps.items():
            label = mode+'/'+sector
            print(json.dumps({'starting':label}),flush=True)
            n = rep['a'].rows
            check(label+' no neutral coefficient', all(weights[sector]))
            for j,r in enumerate(data['relators']):
                check(label+' relator '+str(j), zero(word(rep,r)-s.eye(n)))
            C,T,f,(P,Q) = core_and_boundary(rep,data)
            check_map(C,T,f)
            check(label+' full restriction identities', True)
            pos = [j for j,v in enumerate(weights[sector]) if v>0]
            neg = [j for j,v in enumerate(weights[sector]) if v<0]
            Sp,Sm = selector(n,pos),selector(n,neg)
            for name,H in [('P',P),('Q',Q)]:
                check(label+' literal peripheral split '+name,
                      zero(mul(mul(Sp,H),Sm.T)) and zero(mul(mul(Sm,H),Sp.T)))
            def torus(S):
                m = S.rows
                PP,QQ = mul(mul(S,P),S.T),mul(mul(S,Q),S.T)
                return (s.Matrix.vstack(PP-s.eye(m),QQ-s.eye(m)),
                        (s.eye(m)-QQ).row_join(PP-s.eye(m)))
            Tp,Tm = torus(Sp),torus(Sm)
            fp = (Sp,mul(s.diag(Sp,Sp),f[1]),mul(Sp,f[2]))
            compact = cone(C,Tp,fp)
            attached = full_fiber(C,T,f,Tm,(Sm.T,s.diag(Sm.T,Sm.T),Sm.T))
            relative = cone(C,T,f)
            models = {'positive_cone':compact,'full_fiber':attached,'full_relative':relative}
            results = {name:census(model) for name,model in models.items()}
            check(label+' quotient and full fiber agree',
                  results['positive_cone']['H'] == results['full_fiber']['H'])
            check(label+' whole torus Euler identity', results['positive_cone']['chi'] == 0)
            B,F = C
            rb,rf = rank(B),rank(F)
            ordinary = [n-rb,3*n-rb-rf,2*n-rf,0]
            if not split:
                previous = {'W':[0,2],'Wdual':[1,3],'wedge2W':[0,4],'wedge2Wdual':[0,3]}
                check(label+' previous absolute core control', ordinary[:2] == previous[sector])
            if not zero(mul(-f[2],F)-mul(T[1],f[1])):
                wrong_sign_seen = True
            attached_d_seen |= any(not zero(x) for x in Tm)
            mixed_core = any(not zero(mul(mul(Sp,H),Sm.T)) or
                             not zero(mul(mul(Sm,H),Sp.T)) for H in rep.values())
            check(label+' core split versus nonsplit control', mixed_core != split)
            rows[label] = {'positive_rank':len(pos),'negative_rank':len(neg),
                           'weights':weights[sector],'ordinary_H':ordinary,
                           'models':results,'globally_split_in_flag_basis':not mixed_core}
            matrices[label] = {name:{'dimensions':model[0],
                                      'differentials':[pack(x) for x in model[1]]}
                               for name,model in models.items()}
            print(json.dumps({'finished':label,'H':results['positive_cone']['H']}),flush=True)
        for sector in ('W','wedge2W'):
            left,right = rows[mode+'/'+sector],rows[mode+'/'+sector+'dual']
            check(mode+'/'+sector+' weighted duality',
                  left['models']['positive_cone']['H'] == right['models']['positive_cone']['H'][::-1])
            for U,Z in ((left,right),(right,left)):
                check(mode+'/'+sector+' relative absolute duality '+str(U is left),
                      U['models']['full_relative']['H'] == Z['ordinary_H'][::-1])
    check('wrong two cell sign detected on actual input',wrong_sign_seen)
    check('attached boundary differential actually nonzero',attached_d_seen)
    result = {'status':'PASS','checks':checks,'check_count':len(checks),'cases':rows,
              'scope':'full weighted flag cochain model; analytic identification is separately authored'}
    for name,record in [('MATRICES.json',matrices),('RESULTS.json',result)]:
        target = out/name
        with target.open('x') as stream:
            json.dump(record,stream,indent=2,sort_keys=True)
            stream.write('\n')
    print(json.dumps({'status':'PASS','check_count':len(checks),'cases':len(rows)}),flush=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: verify.py EXISTING_NEW_OUTPUT_DIRECTORY')
    main(Path(sys.argv[1]))
