"""Independent exact replay; no imports from other scientific packets."""
import json
from itertools import combinations
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parent
RT = s.sqrt(2)
GEN = 'abt'


def dm(m):
    return DomainMatrix.from_Matrix(m).convert_to(s.QQ)


def rank(m):
    return dm(m).rank()


def inverse(m):
    return dm(m).inv().to_Matrix()


def kernel(m):
    return dm(m).nullspace().to_Matrix().T


def pairs(x):
    x = s.expand(x)
    b = x.coeff(RT)
    a = s.expand(x - b * RT)
    assert a.is_Rational and b.is_Rational, ('outside Q(sqrt(2))', x)
    return a, b


def restrict(m):
    r = s.zeros(2 * m.rows, 2 * m.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            a, b = pairs(m[i, j])
            r[2*i:2*i+2, 2*j:2*j+2] = s.Matrix([[a, 2*b], [b, a]])
    return r


def field_vector(v):
    assert v.cols == 1 and v.rows % 2 == 0
    return s.Matrix([v[i, 0] + RT * v[i+1, 0] for i in range(0, v.rows, 2)])


def rational_vector(v):
    return s.Matrix([x for entry in v for x in pairs(entry)])


def dual(rep):
    n = next(iter(rep.values())).rows
    t = s.diag(*([s.Integer(2), s.Integer(4)] * (n // 2)))
    ti = s.diag(*([s.Rational(1, 2), s.Rational(1, 4)] * (n // 2)))
    return {g: ti * inverse(m).T * t for g, m in rep.items()}


def exterior(m):
    ij = list(combinations(range(m.rows), 2))
    return s.Matrix([[s.expand(m[i,k]*m[j,l]-m[i,l]*m[j,k])
                      for k,l in ij] for i,j in ij])


def inv_word(w):
    return w.swapcase()[::-1]


def reduce_word(w):
    stack = []
    for c in w:
        if stack and c == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


def substitute(w, images):
    return reduce_word(''.join(images[c] if c in images else inv_word(images[c.lower()])
                               for c in w))


def check_marking(label, state):
    images = {'a': 'a', 'b': 'b'}
    for letter in reversed(label[1:]):
        step = {'a': 'ab', 'b': 'b'} if letter == 'L' else {'a': 'a', 'b': 'ba'}
        images = {g: substitute(w, step) for g,w in images.items()}
    if label[0] == '-':
        images = {g: substitute(w, {'a': 'A', 'b': 'B'}) for g,w in images.items()}
    assert state['relators'] == ['t'+g+'T'+inv_word(images[g]) for g in 'ab']
    correction = 'ab' if label[0] == '-' else ''
    assert state['cusp words'] == ['abAB', correction+'t']
    assert substitute('abAB', images) == reduce_word(inv_word(correction)+'abAB'+correction)


def four(state):
    h = [s.Matrix([[1,0],[0,0]]), s.Matrix([[0,0],[0,1]]),
         s.Matrix([[0,1],[1,0]]), s.Matrix([[0,s.I],[-s.I,0]])]
    q = s.Matrix([[0,s.Rational(1,2),0,0], [s.Rational(1,2),0,0,0],
                  [0,0,-1,0], [0,0,0,-1]])
    out = {}
    for g, entries in state['holonomy (PGL(2, Q(i)); entries [re, im])'].items():
        m = s.Matrix([[s.Rational(a)+s.I*s.Rational(b) for a,b in row] for row in entries])
        modulus = s.sqrt(s.expand(m.det() * s.conjugate(m.det())))
        cols = []
        for basis in h:
            z = (m*basis*m.conjugate().T/modulus).applyfunc(s.simplify)
            cols.append(s.Matrix([z[0,0],z[1,1],(z[0,1]+z[1,0])/2,
                                  (z[0,1]-z[1,0])/(2*s.I)]).applyfunc(s.simplify))
        a = s.Matrix.hstack(*cols)
        restrict(a)  # exact field containment, before any field restriction
        assert s.expand(a.det()) == 1
        assert (a.T*q*a-q).applyfunc(s.expand) == s.zeros(4)
        out[g] = a
    return out


class Complex:
    def __init__(self, rep, state):
        self.rep = rep
        self.n = n = rep['a'].rows  # dimension over Q, twice the K dimension
        assert n % 2 == 0
        self.letters = dict(rep)
        self.letters.update({g.upper(): inverse(m) for g,m in rep.items()})
        for word in state['relators']:
            assert self.evaluate(word) == s.eye(n), ('relator violation', word)
        p,q = [self.evaluate(w) for w in state['cusp words']]
        assert p*q == q*p
        self.B = s.Matrix.vstack(*(rep[g]-s.eye(n) for g in GEN))
        self.F = s.Matrix.vstack(*(self.fox(w) for w in state['relators']))
        self.R = s.Matrix.vstack(*(self.fox(w) for w in state['cusp words']))
        self.D = s.Matrix.vstack(p-s.eye(n),q-s.eye(n))
        self.M = self.F.row_join(s.zeros(self.F.rows,n)).col_join(self.R.row_join(-self.D))
        assert self.F*self.B == s.zeros(self.F.rows,n)
        assert self.R*self.B == self.D
        assert self.M*self.B.col_join(s.eye(n)) == s.zeros(self.M.rows,n)
        torus_relation = (s.eye(n)-q).row_join(p-s.eye(n))
        assert torus_relation*self.D == s.zeros(n)
        # Torus evaluations of group cocycles satisfy the boundary relation.
        assert rank(self.F.col_join(torus_relation*self.R)) == rank(self.F)

    def evaluate(self, word):
        p = s.eye(self.n)
        for c in word:
            p = p*self.letters[c]
        return p

    def fox(self, word):
        n = self.n
        p = s.eye(n)
        blocks = [s.zeros(n) for _ in GEN]
        for c in word:
            j = GEN.index(c.lower())
            if c.islower():
                blocks[j] += p
                p = p*self.letters[c]
            else:
                p = p*self.letters[c]
                blocks[j] -= p
        return s.Matrix.hstack(*blocks)

    def profile(self):
        n = self.n
        b,f,d,m = [rank(x) for x in (self.B,self.F,self.D,self.M)]
        vals = {'h0_absolute':n-b, 'h0_boundary':n-d,
                'h1_absolute':3*n-f-b, 'h1_relative':3*n-m,
                'restriction_rank':m-f-d,
                'h1_interior':3*n-b-m+d}
        assert all(v >= 0 and v % 2 == 0 for v in vals.values()), vals
        out = {k:v//2 for k,v in vals.items()}
        assert out['h1_relative'] == out['h0_boundary']-out['h0_absolute']+out['h1_interior']
        return out

    def nonexact(self, c):
        return rank(self.B.row_join(c)) > rank(self.B)

    def interior_cocycle(self):
        basis = kernel(self.M)
        for j in range(basis.cols):
            c, w = basis[:3*self.n,j], basis[3*self.n:,j]
            if self.nonexact(c):
                c0 = c-self.B*w
                assert self.F*c0 == s.zeros(self.F.rows,1)
                assert self.R*c0 == s.zeros(self.R.rows,1)
                assert self.nonexact(c0)
                v = field_vector(c0)
                scale = next(x for x in v if x != 0)
                v = v.applyfunc(lambda x: s.simplify(x/scale))
                c0 = rational_vector(v)
                assert self.nonexact(c0) and self.R*c0 == s.zeros(self.R.rows,1)
                return v
        raise AssertionError('no nonzero interior class')


def extension(v, cocycle):
    d = v['a'].rows
    return {g: v[g].row_join(cocycle[j*d:(j+1)*d,:]).col_join(
            s.zeros(1,d).row_join(s.ones(1,1))) for j,g in enumerate(GEN)}


def pair_profiles(rep, state):
    dre = dual(rep)
    assert dual(dre) == rep
    a,b = Complex(rep,state).profile(), Complex(dre,state).profile()
    assert a['h1_relative'] == b['h1_absolute']-b['h0_absolute']
    assert b['h1_relative'] == a['h1_absolute']-a['h0_absolute']
    assert a['h0_boundary'] == b['h0_boundary']
    return {'E':a, 'dual':b, 'difference':{
        k:a[k]-b[k] for k in ('h1_absolute','h1_relative','h1_interior')}}


def member(label, state, spec, f):
    signs = spec['nu on a, b, t']
    v = {g: signs[g]*f[g] for g in GEN}
    vc = Complex({g:restrict(m) for g,m in v.items()},state)
    vp = vc.profile()
    assert vp['h1_interior'] == 1, ('received one-dimensional interior failed',vp)
    c = vc.interior_cocycle()
    assert not vc.nonexact(s.zeros(3*vc.n,1))
    w = extension(v,c)
    wr = {g:restrict(m) for g,m in w.items()}
    wc = Complex(wr,state)
    for word in state['cusp words']:
        assert wc.evaluate(word) == s.diag(vc.evaluate(word),s.eye(2))
    assert all(s.expand(m.det()) == 1 for m in w.values())
    main = pair_profiles(wr,state)
    wedge = pair_profiles({g:restrict(exterior(m)) for g,m in w.items()},state)
    split = extension(v,s.zeros(12,1))
    split_main = pair_profiles({g:restrict(m) for g,m in split.items()},state)
    split_wedge = pair_profiles({g:restrict(exterior(m)) for g,m in split.items()},state)
    assert all(x == 0 for p in (split_main,split_wedge) for x in p['difference'].values())
    # Gauge-equivalent splitting, independently recomputed on W and exterior square.
    u = s.Matrix([1,2,3,4])
    cg = c+s.Matrix.vstack(*((v[g]-s.eye(4))*u for g in GEN))
    wg = extension(v,cg)
    assert pair_profiles({g:restrict(m) for g,m in wg.items()},state) == main
    assert pair_profiles({g:restrict(exterior(m)) for g,m in wg.items()},state) == wedge
    # Bad input is detected before a class count is accepted.
    bad = dict(wr)
    bad['a'] = 2*bad['a']
    rejected = False
    try:
        Complex(bad,state)
    except AssertionError as error:
        rejected = 'relator violation' in str(error)
    assert rejected
    return {'carrier':state['SnapPy'],'signed_word':label,'character':signs,
            'V':vp,'peripherally_zero_cocycle':[str(x) for x in c],
            'W':main,'wedge2W':wedge,'splitW':split_main,'split_wedge2W':split_wedge,
            'controls':'PASS'}


def scalar_controls():
    a = s.Matrix([[1+RT,2-RT],[RT,3]])
    b = s.Matrix([[2,1],[1-RT,RT]])
    assert restrict((a*b).applyfunc(s.expand)) == restrict(a)*restrict(b)
    assert dual({'a':restrict(a)})['a'] == restrict(a.inv().T.applyfunc(s.simplify))
    # Exterior functor and dual functor tested on a nonsymmetric invertible matrix.
    q = s.Matrix([[1,RT,0],[0,2,1],[1,0,3]])
    assert restrict(exterior(q*q)) == restrict(exterior(q))*restrict(exterior(q))
    assert dual({'a':restrict(exterior(q))})['a'] == restrict(exterior(q.inv().T).applyfunc(s.simplify))


def run():
    scalar_controls()
    data = json.loads((ROOT/'members.json').read_text())
    out = []
    for label,state in data['states'].items():
        check_marking(label,state)
        tr = Complex({g:s.eye(2) for g in GEN},state).profile()
        assert (tr['h1_absolute'],tr['h1_relative'],tr['h1_interior']) == (1,0,0), tr
        f = four(state)
        for spec in state['members']:
            result = member(label,state,spec,f)
            out.append(result)
            print(json.dumps({'member':result},sort_keys=True),flush=True)
    print(json.dumps({'status':'PASS','members':len(out),
                      'scope':'marked compact pair cohomology; no physical domain selected'}),flush=True)
    return out


if __name__ == '__main__':
    run()
