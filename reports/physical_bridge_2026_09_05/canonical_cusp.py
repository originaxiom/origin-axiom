"""R44 finite algebraic controls. These do not certify the global proof."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s

_spec = importlib.util.spec_from_file_location(
    'r42_canonical_input', Path(__file__).with_name('affine_background.py'))
prior = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prior)

Q = s.symbols('q', positive=True)
R = s.symbols('R', positive=True)
K = s.symbols('k', real=True, nonzero=True)
BETA = s.symbols('beta', real=True)
W = s.symbols('omega', real=True)
I4 = s.eye(4)
N0 = s.zeros(4)
N0[0, 2] = N0[2, 3] = 1
P = N0**2
D = s.diag(1, -3, 1, 1)
J = s.diag(5, -3, 1, -3)/8


def clean(a):
    return a.applyfunc(s.factor) if isinstance(a, s.MatrixBase) else s.factor(a)


def comm(a, b):
    return a*b-b*a


@lru_cache(None)
def peripheral(q=Q):
    m, n = prior.generators(q)
    ell = prior.word('nMNmmNMn', (m, n))
    logm = (m-I4)-(m-I4)**2/2
    pi = ((ell-q*I4)/(q**-3-q))**2
    p3 = (I4-pi)*I4[:, 3]
    basis = s.Matrix.hstack(logm**2*p3, pi*I4[:, 0], logm*p3, p3)
    inv = basis.inv()
    beta = 6/(q-1/q)
    return {'basis': clean(basis), 'det': clean(basis.det()),
            'meridian': clean(inv*m*basis),
            'longitude': clean(inv*ell*basis),
            'expected_longitude': s.diag(q, q**-3, q, q)*(I4+beta*P),
            'pi_residual': clean(pi*pi-pi), 'beta': beta}


def radial_changes(wrong_sign=False):
    x0, z, y, c, ell = s.symbols('x0 z y c ell', real=True)
    sign = -1 if wrong_sign else 1
    # ell=log(z) is an independent coordinate to avoid branch simplification.
    radial = x0+sign*c*ell-y**2/2
    mer = radial.subs({x0:x0+y+s.Rational(1,2), y:y+1}, simultaneous=True)
    lon = radial.subs({x0:x0+4*c*K, ell:ell-4*K}, simultaneous=True)
    return clean(mer-radial), clean(lon-radial)


def rescaling():
    return s.diag(R**(-s.Rational(5,8)), R**s.Rational(3,8),
                  R**(-s.Rational(1,8)), R**s.Rational(3,8))


def connection(omit_radial=False, dual=False):
    bx, bt, br = N0/s.sqrt(R), K*D+BETA*P/R, J/R
    if omit_radial:
        br = s.zeros(4)
    if dual:
        bx, bt, br = -bx.T, -bt.T, -br.T
    curvature = (clean(comm(bx,bt)), clean(bx.diff(R)+comm(br,bx)),
                 clean(bt.diff(R)+comm(br,bt)))
    return bx, bt, br, curvature


def fourier_inverse(dual=False):
    a = s.I*W*I4+K*D
    nil = BETA*P/R
    if dual:
        a, nil = s.I*W*I4-K*D.T, -nil.T
    inv = a.inv()-a.inv()*nil*a.inv()
    return a+nil, clean(inv)


@lru_cache(None)
def product_metric(alpha=s.Rational(3,8), beta=s.Rational(1,4)):
    x0, z, y = s.symbols('x0 z y', real=True)
    rad = x0-y*y/2
    coords = (x0,z,y)
    logu = beta*s.log(z)+alpha*s.log(rad)
    gradient = s.Matrix([s.diff(logu,x) for x in coords])
    h = clean(-s.hessian(logu,coords)-gradient*gradient.T)
    return {'h':h, 'point':h.subs({x0:1,z:1,y:0}),
            'density_constant':clean(h.det()*z**2*rad**3),
            'ma_powers':(8*alpha-3,8*beta-2)}


def exterior_operators():
    """Wedge/contraction matrices on ALL exterior degrees of (R,x,t)."""
    wedge, contraction = [], []
    for axis in range(3):
        w, i = s.zeros(8), s.zeros(8)
        for bits in range(8):
            parity = sum(bool(bits & (1 << a)) for a in range(axis))
            sign = (-1)**parity
            if not bits & (1 << axis):
                w[bits | (1 << axis), bits] = sign
            else:
                i[bits ^ (1 << axis), bits] = sign
        wedge.append(w)
        contraction.append(i)
    return wedge, contraction


def run():
    data = peripheral()
    p = product_metric()
    t, inv = fourier_inverse()
    td, invd = fourier_inverse(True)
    sc = rescaling()
    return {
        'literal_meridian':data['meridian'] == I4+N0+P/2,
        'literal_longitude':clean(data['longitude']-data['expected_longitude']) == s.zeros(4),
        'basis_determinant':str(data['det']),
        'radial_invariant':radial_changes() == (0,0),
        'wrong_log_sign_rejected':radial_changes(True)[1] != 0,
        'SL_rescaling':clean(sc.det()-1) == 0,
        'flat':all(a == s.zeros(4) for a in connection()[3]),
        'dual_flat':all(a == s.zeros(4) for a in connection(dual=True)[3]),
        'radial_omission_rejected':any(a != s.zeros(4) for a in connection(True)[3]),
        'fourier_inverse':clean(t*inv-I4) == s.zeros(4),
        'dual_fourier_inverse':clean(td*invd-I4) == s.zeros(4),
        'product_MA_constant':str(p['density_constant']),
        'product_MA_powers':list(map(str,p['ma_powers'])),
        'product_metric_at_point':str(p['point']),
        'analytic_grade':'Authored global proof; external inputs; finite controls only.',
        'physical_chirality_derived':False,
        'compact_resolvent_claimed':False}


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True))
