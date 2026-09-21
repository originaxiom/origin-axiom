"""R42 finite controls of the affine-sphere bridge, not a global PDE solver.

All norms are the positive defining trace norm. The all-n analytic proof
and its external hypotheses are separate from these n=3 tensor checks.
"""
from functools import lru_cache
from itertools import product
import json

import sympy as s


def clean(value):
    fn = lambda x: s.factor(s.cancel(x))
    return value.applyfunc(fn) if isinstance(value, s.MatrixBase) else fn(value)


def comm(a, b):
    return a*b-b*a


def tensor(entries):
    def at(*indices):
        return entries.get(tuple(sorted(indices)), s.S.Zero)
    return at


@lru_cache(None)
def cubic():
    a, b, c, d, e, f, g = s.symbols('a b c d e f g', real=True)
    return tensor({(0,0,0):a, (0,0,1):b, (0,0,2):c,
                   (0,1,1):d, (0,1,2):e, (0,2,2):-a-d,
                   (1,1,1):f, (1,1,2):g, (1,2,2):-b-f,
                   (2,2,2):-c-g})


@lru_cache(None)
def quartic():
    a,b,c,d,e,f,g,h,i = s.symbols('A B C D E F G H I', real=True)
    return tensor({(0,0,0,0):a, (0,0,0,1):b, (0,0,0,2):c,
                   (0,0,1,1):d, (0,0,1,2):e, (0,0,2,2):-a-d,
                   (0,1,1,1):f, (0,1,1,2):g, (0,1,2,2):-b-f,
                   (0,2,2,2):-c-g, (1,1,1,1):h, (1,1,1,2):i,
                   (1,1,2,2):-d-h, (1,2,2,2):-e-i,
                   (2,2,2,2):a+2*d+h})


def blocks(c):
    ks = tuple(s.Matrix(3,3,lambda j,k: c(i,j,k)) for i in range(3))
    psis = tuple(s.zeros(1).row_join(s.eye(3)[i,:]).col_join(
        s.eye(3)[:,i].row_join(ks[i])) for i in range(3))
    return ks, psis


def gauss(ks):
    return {(i,j): clean(-(s.eye(3)[:,i]*s.eye(3)[j,:]
                            -s.eye(3)[:,j]*s.eye(3)[i,:])-comm(ks[i],ks[j]))
            for i,j in product(range(3), repeat=2)}


def divergence(t):
    return clean(s.Matrix(3,3,lambda j,k: sum(t(i,i,j,k) for i in range(3))))


def codazzi(t):
    return tuple(clean(t(i,j,k,l)-t(j,i,k,l))
                 for i,j,k,l in product(range(3), repeat=4))


@lru_cache(None)
def generic_controls():
    c = cubic()
    ks, psis = blocks(c)
    rs = gauss(ks)
    ric = clean(s.Matrix(3,3,lambda j,k: sum(rs[i,j][i,k] for i in range(3))))
    gram = clean(s.Matrix(3,3,lambda j,k: s.trace(ks[j]*ks[k])))
    c2 = clean(sum(c(i,j,k)**2 for i,j,k in product(range(3), repeat=3)))
    norm = clean(sum(s.trace(p*p) for p in psis))
    return dict(
        symmetric=all(p == p.T for p in psis),
        trace_free=all(clean(s.trace(p)) == 0 for p in psis),
        flat_blocks=all(clean(s.diag(s.zeros(1),rs[i,j])+comm(psis[i],psis[j])) == s.zeros(4)
                        for i,j in product(range(3), repeat=2)),
        bianchi=all(clean(rs[i,j][:,k]+rs[j,k][:,i]+rs[k,i][:,j]) == s.zeros(3,1)
                    for i,j,k in product(range(3), repeat=3)),
        ricci=ric == -2*s.eye(3)+gram,
        ricci_psi=clean(ric-s.Matrix(3,3,lambda j,k: s.trace(psis[j]*psis[k]))+4*s.eye(3)) == s.zeros(3),
        norm_identity=clean(norm-6-c2) == 0,
        codazzi=all(x == 0 for x in codazzi(quartic())),
        moment=divergence(quartic()) == s.zeros(3),
        cubic_norm=str(c2))


@lru_cache(None)
def hyperbolic(wrong_sign=False):
    x,y,z = s.symbols('x y z', real=True, positive=True)
    coords = (x,y,z)
    h = s.eye(3)/z**2
    hi = h.inv()
    gammas = tuple(s.Matrix(3,3,lambda a,b: sum(hi[a,k]*(
        s.diff(h[k,b],coords[i])+s.diff(h[k,i],coords[b])-s.diff(h[i,b],coords[k]))/2
        for k in range(3))) for i in range(3))
    aa = tuple(s.diag(s.zeros(1),g) for g in gammas)
    ps = tuple(s.zeros(1).row_join(h[i,:]).col_join(
        ((-1 if wrong_sign else 1)*s.eye(3)[:,i]).row_join(s.zeros(3))) for i in range(3))
    dd = tuple(aa[i]+ps[i] for i in range(3))
    flat = tuple(clean(dd[j].diff(coords[i])-dd[i].diff(coords[j])+comm(dd[i],dd[j]))
                 for i in range(3) for j in range(i+1,3))
    moment = s.zeros(4)
    for i,j in product(range(3), repeat=2):
        term = ps[j].diff(coords[i])+comm(aa[i],ps[j])
        term -= sum((gammas[i][k,j]*ps[k] for k in range(3)), s.zeros(4))
        moment -= hi[i,j]*term
    coeff = s.diag(1,h)
    compatible = tuple(clean(coeff.diff(coords[i])-aa[i].T*coeff-coeff*aa[i]) for i in range(3))
    self_adjoint = tuple(clean(coeff*ps[i]-ps[i].T*coeff) for i in range(3))
    return dict(flat=flat, moment=clean(moment), compatible=compatible,
                self_adjoint=self_adjoint,
                norm=clean(sum(hi[i,j]*s.trace(ps[i]*ps[j]) for i,j in product(range(3), repeat=2))))


@lru_cache(None)
def simplex():
    coords = s.symbols('u v w', real=True)
    rows = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    f = s.Matrix([s.exp(sum(a*x for a,x in zip(row,coords)))/2 for row in rows])
    frame = s.Matrix.hstack(f,*(f.diff(x) for x in coords))
    c = tensor({(0,1,2):s.S.One})
    ks, ps = blocks(c)
    residuals = tuple(s.simplify(f.diff(coords[i],coords[j])-(f if i==j else s.zeros(4,1))
                              -sum((ks[i][k,j]*f.diff(coords[k]) for k in range(3)),s.zeros(4,1)))
                      for i,j in product(range(3), repeat=2))
    return dict(frame_det=s.simplify(frame.det()), residuals=residuals,
                commutators=tuple(comm(ps[i],ps[j]) for i,j in product(range(3), repeat=2)),
                cubic_norm=sum(c(i,j,k)**2 for i,j,k in product(range(3), repeat=3)),
                psi_norm=sum(s.trace(p*p) for p in ps),
                curvature=gauss(ks))


Q = s.symbols('q', positive=True)


@lru_cache(None)
def generators(q=Q):
    t = q/2
    return (s.Matrix([[1,0,1,t-1],[0,1,1,t],[0,0,1,t+s.Rational(1,2)],[0,0,0,1]]),
            s.Matrix([[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]]))


def word(text, matrices):
    m,n = matrices
    letters = {'m':m,'M':m.inv(),'n':n,'N':n.inv()}
    answer = s.eye(4)
    for letter in text:
        answer = clean(answer*letters[letter])
    return answer


@lru_cache(None)
def holonomy():
    m,n = generators()
    w = word('nMNm',(m,n))
    ell = word('nMNmmNMn',(m,n))
    x = s.symbols('X')
    return dict(relation=clean(m*w-w*n) == s.zeros(4),
        unipotent=all(clean((a-s.eye(4))**4) == s.zeros(4) for a in (m,n)),
        determinant=clean(m.det()) == 1 and clean(n.det()) == 1 and clean(ell.det()) == 1,
        commute=clean(comm(m,ell)) == s.zeros(4),
        characteristic=clean(ell.charpoly(x).as_expr()-(x-Q)**3*(x-Q**-3)) == 0,
        mismatch=clean(s.trace(ell)-s.trace(ell.inv())),
        torus_determinant=clean((ell-s.eye(4)).det()), longitude=ell)


def run():
    h = hyperbolic()
    w = hyperbolic(True)
    c = simplex()
    b = holonomy()
    generic = generic_controls()
    return dict(generic=generic,
        hyperbolic=dict(flat=all(x == s.zeros(4) for x in h['flat']),
            moment=h['moment'] == s.zeros(4), compatible=all(x == s.zeros(4) for x in h['compatible']),
            self_adjoint=all(x == s.zeros(4) for x in h['self_adjoint']), norm=str(h['norm']),
            wrong_sign_fails=any(x != s.zeros(4) for x in w['flat'])),
        simplex=dict(volume_normalized=c['frame_det']**2 == 1,
            structure=all(x == s.zeros(4,1) for x in c['residuals']),
            flat=all(x == s.zeros(4) for x in c['commutators']),
            cubic_norm=str(c['cubic_norm']), psi_norm=str(c['psi_norm']),
            ricci_flat=all(x == s.zeros(3) for x in c['curvature'].values())),
        holonomy={key:(str(value) if key in ('mismatch','torus_determinant') else value)
                  for key,value in b.items() if key != 'longitude'},
        analytic_grade='Authored proof using external existence/compactness; finite tests do not certify it.',
        base_metric='Blaschke metric of the chosen projective structure, not fixed hyperbolic g0',
        physical_chirality_proved=False, four_dimensional_gravity_derived=False)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True))
