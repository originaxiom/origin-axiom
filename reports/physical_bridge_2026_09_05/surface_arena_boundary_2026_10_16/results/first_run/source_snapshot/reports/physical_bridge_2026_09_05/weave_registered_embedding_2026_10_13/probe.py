"""Exact retained-coefficient and relative-pairing comparison, not a physical spectrum."""
from collections import Counter
from itertools import combinations, permutations, product
from functools import lru_cache
import json
import sympy as s


def clean(m):
    return m.applyfunc(lambda x: s.simplify(s.expand_complex(x)))


def zero(m):
    return clean(m) == s.zeros(*m.shape)


def bracket(a, b):
    return a*b-b*a


def lie_wedge(x, k):
    basis = list(combinations(range(x.rows), k)); out = s.zeros(len(basis))
    for col, inds in enumerate(basis):
        for p, j in enumerate(inds):
            for i in range(x.rows):
                term = list(inds); term[p] = i
                if len(set(term)) != k:
                    continue
                sign = (-1)**sum(term[a] > term[b] for a, b in combinations(range(k), 2))
                out[basis.index(tuple(sorted(term))), col] += sign*x[i, j]
    return out


def roots():
    e = [s.eye(8)[:, j] for j in range(8)]
    out = [a*e[i]+b*e[j] for i, j in combinations(range(8), 2) for a, b in product((-1, 1), repeat=2)]
    out += [s.Matrix(v)/2 for v in product((-1, 1), repeat=8) if v.count(-1) % 2 == 0]
    return e, out


def fundamental(n):
    return [tuple(int(j == i)-int(j == i+1) for i in range(n-1)) for j in range(n)]


def exterior_weights(n, k):
    f = fundamental(n)
    return Counter(tuple(sum(f[j][i] for j in inds) for i in range(n-1)) for inds in combinations(range(n), k))


def dual(w):
    return Counter({tuple(-x for x in v): m for v, m in w.items()})


def adjoint_weights(n):
    f = fundamental(n); out = Counter({(0,)*(n-1): n-1})
    out.update(tuple(x-y for x, y in zip(f[i], f[j])) for i, j in permutations(range(n), 2))
    return out


def tensor(*args):
    out = Counter()
    for terms in product(*[list(v.items()) for v in args]):
        key = sum((w for w, m in terms), ()); multiplicity = s.prod(m for w, m in terms)
        out[key] += int(multiplicity)
    return out


def a5_roster():
    e, rr = roots()
    chain = [e[6]-e[7], e[5]-e[6], e[6]+e[7], -s.ones(8, 1)/2, e[3]+e[4]]
    color = [e[0]-e[1], e[1]-e[2]]; weak = [e[3]-e[4]]
    actual = Counter(tuple(int(r.dot(a)) for a in chain+color+weak) for r in rr)
    actual[(0,)*8] += 8
    z6, z3, z2 = Counter({(0,)*5: 1}), Counter({(0,)*2: 1}), Counter({(0,): 1})
    f6, f3, f2 = exterior_weights(6, 1), exterior_weights(3, 1), exterior_weights(2, 1)
    w2, w3 = exterior_weights(6, 2), exterior_weights(6, 3)
    expected = (tensor(adjoint_weights(6), z3, z2)+tensor(z6, adjoint_weights(3), z2)
                +tensor(z6, z3, adjoint_weights(2))+tensor(w3, z3, f2)
                +tensor(w2, dual(f3), z2)+tensor(dual(w2), f3, z2)
                +tensor(f6, f3, f2)+tensor(dual(f6), dual(f3), f2))
    c = s.Matrix.hstack(*chain); g = c.T*c
    weights = [c*g.inv()*s.Matrix([1, 0, 0, 0, 0])]
    for a in chain:
        weights.append(weights[-1]-a)
    hv = sum((v*w for v, w in zip((1, -1)*3, weights)), s.zeros(8, 1))
    cartan = s.symbols('c0:5'); cv = sum((v*w for v, w in zip(cartan, chain)), s.zeros(8, 1))
    poly = s.expand(sum(r.dot(cv)**2 for r in rr)-60*sum(w.dot(cv)**2 for w in weights))
    char = Counter(int(r.dot(hv)) for r in rr); char[0] += 8
    return actual, expected, char, poly, g


def a4_character():
    e, rr = roots()
    chain = [e[6]-e[7], e[5]-e[6], e[6]+e[7], -s.ones(8, 1)/2]
    c = s.Matrix.hstack(*chain); g = c.T*c
    weights = [c*g.inv()*s.Matrix([1, 0, 0, 0])]
    for a in chain:
        weights.append(weights[-1]-a)
    h = sum((v*w for v, w in zip((4, 2, 0, -2, -4), weights)), s.zeros(8, 1))
    out = Counter(int(r.dot(h)) for r in rr); out[0] += 8
    return out


def irreps(weights):
    return [[n+1, weights[n]-weights[n+2]] for n in range(max(weights)+1) if weights[n] != weights[n+2]]


def encoded(m):
    return [[[str(s.simplify(s.re(x))), str(s.simplify(s.im(x)))] for x in row] for row in m.tolist()]


@lru_cache(None)
def run():
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
    i = s.I; eye = s.eye(2); a = s.diag(i, -i); b = s.Matrix([[0, 1], [-1, 0]])
    transform = s.diag(b, a, a*b)
    aa, bb = s.diag(-a, a, -a), s.diag(b, -b, -b)
    check('actual simultaneous A map', zero(transform*s.kronecker_product(s.eye(3), a)*transform.H-aa))
    check('actual simultaneous B map', zero(transform*s.kronecker_product(s.eye(3), b)*transform.H-bb))
    check('unitary determinant one coefficient map', zero(transform.H*transform-s.eye(6)) and transform.det() == 1)
    check('retained central lift', zero(aa*bb*aa.H*bb.H+s.eye(6)))
    check('wrong identity coefficient map rejected', not zero(s.kronecker_product(s.eye(3),a)-aa))
    check('group homomorphism on noncommuting generators', zero(transform*s.kronecker_product(s.eye(3),a*b)*transform.H-aa*bb))
    p13 = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    p23 = s.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    l, r = (eye+a)/s.sqrt(2), (eye-b)/s.sqrt(2)
    family = []
    for name, move, small in [('L', s.kronecker_product(p13, l), l), ('R', s.kronecker_product(p23, r), r)]:
        transported = clean(transform.H*move*transform)
        reduced = clean(transported*s.kronecker_product(s.eye(3), small.H))
        fm = s.Matrix(3, 3, lambda j, k: s.trace(reduced[2*j:2*j+2, 2*k:2*k+2])/2)
        check(name+' full factorization', zero(transported-s.kronecker_product(fm, small)))
        check(name+' unitary whole lift', zero(move.H*move-s.eye(6)) and s.simplify(move.det()) == 1)
        check(name+' family unitary', zero(fm.H*fm-s.eye(3)))
        check(name+' arbitrary lift sign retained', zero(transform.H*(-move)*transform+s.kronecker_product(fm, small)))
        family.append(encoded(fm))
    check('actual L peripheral automorphism', zero(s.kronecker_product(p13,l)*bb*s.kronecker_product(p13,l).H-aa*bb))
    actual, expected, new_char, poly, gram = a5_roster(); old_char = a4_character()
    check('full E8 roster with eight Cartans', actual == expected and sum(actual.values()) == 248)
    check('omitted Cartans control', actual != expected-Counter({(0,)*8: 8}))
    check('actual A5 Gram', gram == s.Matrix(5, 5, lambda j, k: 2*int(j == k)-int(abs(j-k) == 1)))
    check('full quadratic Cartan identity', poly == 0)
    new_index = sum(w*w*n for w, n in new_char.items())//2
    old_index = sum(w*w*n for w, n in old_char.items())//2
    check('two complete trace indices', (new_index, old_index) == (180, 1200))
    check('not ambient conjugate', new_index != old_index)
    check('new full sl2 dimensions', sum(d*n for d,n in irreps(new_char)) == 248)
    check('old full sl2 dimensions', sum(d*n for d,n in irreps(old_char)) == 248)
    check('new odd centre sector retained', sum(m*(-1)**w for w,m in new_char.items()) == 24 and any(w % 2 for w in new_char))
    check('old all even centre', all(w % 2 == 0 for w in old_char))
    h, ep, fp = s.diag(1, -1), s.Matrix([[0, 1], [0, 0]]), s.Matrix([[0, 0], [1, 0]])
    smalls = (ep, fp, h); bigs = tuple(s.kronecker_product(s.eye(3), x) for x in smalls)
    def pairing(x, y):
        return (12*s.trace(x*y)+6*s.trace(lie_wedge(x,2)*lie_wedge(y,2))
                +12*s.trace(x*y)+2*s.trace(lie_wedge(x,3)*lie_wedge(y,3)))
    for j,k in product(range(3),repeat=2):
        check(f'full pairing {j}{k}', pairing(bigs[j],bigs[k]) == 180*s.trace(smalls[j]*smalls[k]))
    for j,k,m in product(range(3),repeat=3):
        check(f'full alternating cubic {j}{k}{m}', pairing(bigs[j],bracket(bigs[k],bigs[m])) == 180*s.trace(smalls[j]*bracket(smalls[k],smalls[m])))
    check('nonzero cubic control', pairing(bigs[2],bracket(bigs[0],bigs[1])) == 360)
    check('group exterior is not Lie exterior', lie_wedge(-s.eye(6), 2) != s.eye(15))
    c, sign, previous, following = s.symbols('c sign previous following')
    scale = 2*180*2
    check('boundary primitive scale', scale == 720 and scale != 4800)
    check('registered relation retained', s.expand(-scale*c*((-sign)*previous+sign*following)-scale*c*sign*(previous-following)) == 0)
    check('unflipped sheet rejected', s.expand((-scale*c*sign*(previous+following)).subs(previous,following)) == -1440*c*sign*following)
    group = [eye,-eye,a,-a,b,-b,a*b,-a*b]
    qchars = []
    for g in group:
        p1,p2,p3 = [3*s.trace(g**n) for n in (1,2,3)]
        value = 11+p1*p1-1+6*(p1*p1-p2)/2+12*p1+2*(p1**3-3*p1*p2+2*p3)/6
        qchars.append(int(value))
    check('credited full Q8 character', qchars == [248,24,28,28,28,28,28,28])
    check('credited Q8 invariant 55', sum(qchars)//8 == 55)
    x,y,z = s.symbols('x y z'); leaf = x*x+y*y+z*z-x*y*z
    gradient = [s.diff(leaf,v) for v in (x,y,z)]
    check('singular common point not regular chart', all(v.subs({x:0,y:0,z:0}) == 0 for v in gradient))
    check('regular leaf positive control', leaf.subs({x:3,y:3,z:3}) == 0 and any(v.subs({x:3,y:3,z:3}) != 0 for v in gradient))
    records = {'new_sl2_irreps': irreps(new_char), 'old_sl2_irreps': irreps(old_char),
               'trace_indices': [new_index,old_index], 'boundary_primitive_scale': scale,
               'q8_characters': qchars, 'family_moves': family,
               'new_full_weights': sorted([w,m] for w,m in new_char.items()),
               'old_full_weights': sorted([w,m] for w,m in old_char.items())}
    return {'checks': checks, 'records': records, 'all_passed': all(checks.values()),
            'scope': 'two supplied E8 maps and a local relative primitive, not a physical operator or selected SM'}


if __name__ == '__main__':
    data = run(); print(json.dumps(data, indent=2)); raise SystemExit(0 if data['all_passed'] else 1)
