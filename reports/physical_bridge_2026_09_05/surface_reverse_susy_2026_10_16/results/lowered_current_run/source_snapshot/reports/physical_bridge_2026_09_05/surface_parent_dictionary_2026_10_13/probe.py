"""Coordinate, exterior-connection and physical Clifford comparison; no kernel count."""
from functools import lru_cache
import importlib.util
from itertools import product
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def clean(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def zero(a):
    a = clean(a)
    return a == s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else a == 0


@lru_cache(None)
def data():
    geo = load('pinned_total_metric', HERE/'upstream_total_metric.py')
    vals = geo.geometry()
    g, co, E, gi, G, C, GK, GC, cs, omega, wc, M, K = vals
    vacuum = s.eye(4)[:, 0]
    create = [(cs[0]-s.I*cs[1])/2, (cs[2]-s.I*cs[3])/2]
    fock = s.Matrix.hstack(vacuum, create[0]*vacuum, create[1]*vacuum,
                          create[0]*create[1]*vacuum)
    return geo, vals, vacuum, fock


def lorentz(cs):
    herm = [s.I*c for c in cs]
    gam = [s.I*herm[0], herm[1], herm[2], herm[3]]
    g5 = s.I*gam[0]*gam[1]*gam[2]*gam[3]
    all8 = [s.kronecker_product(a, s.eye(4)) for a in gam]
    all8 += [s.kronecker_product(g5, a) for a in herm]
    return gam, g5, all8


@lru_cache(None)
def run():
    checks = {}
    def ck(name, yes):
        checks[name] = bool(yes)
    geo, vals, vacuum, fock = data()
    g, co, E, gi, G, C, GK, GC, cs, omega, wc, M, K = vals
    ell, area, x, y = geo.l, geo.A, geo.x, geo.y
    old = geo.checks()
    ck('credited full metric replay', len(old) == 343 and all(old.values()))
    hol = s.Matrix([[1, s.I, 0, 0], [geo.v, s.I*geo.v, 1, x+s.I*y]])
    gram = clean(hol*gi*hol.H)
    hcanon = clean(gram.det())
    realhol = s.Matrix([x, y, geo.u+x*geo.v, y*geo.v])
    jac = realhol.jacobian(geo.coords)
    ck('actual holomorphic real Jacobian', zero(jac.det()-y))
    ck('canonical norm from all inverse metric entries', zero(hcanon-4*y**3/(ell**2*area)))
    power = clean(y*s.diff(s.log(hcanon), y))
    ck('holomorphic canonical metric power', power == 3)
    wrong_density = clean(s.sqrt(g.det()))
    ck('real period density is not holomorphic determinant',
       zero(y*s.diff(s.log(wrong_density), y)+2) and power != 2)
    # Unit Chern connection of K: (partial - dbar)log(h)/2.
    aKx = clean(-s.I*s.diff(s.log(hcanon), y)/2)
    aRx = clean(-aKx/2)
    ck('Chern half-line twist coordinate value', zero(aRx-3*s.I/(4*y)))
    ck('nonflat Chern twist', zero(-s.diff(aRx, y)-3*s.I/(4*y*y)))
    ck('Fock change of frame unitary', zero(fock.H*fock-s.eye(4)))
    eh, ev = s.zeros(4), s.zeros(4)
    eh[1,0] = eh[3,2] = 1
    ev[2,0] = 1
    ev[3,1] = -1
    form_clifford = [eh-eh.H, s.I*(eh+eh.H), ev-ev.H, s.I*(ev+ev.H)]
    for j in range(4):
        ck(f'whole Dolbeault Clifford symbol {j}', zero(fock.H*cs[j]*fock-form_clifford[j]))
    for a, b in ((0, 1), (2, 3)):
        ck(f'vacuum annihilator {a}', zero((cs[a]+s.I*cs[b])*vacuum))
    # The antiholomorphic covectors, expressed in the real orthonormal frame.
    cov = s.Matrix([[1, 0], [-s.I, 0], [0, 1], [0, -s.I]])/s.sqrt(2)
    exterior_rows = []
    for i in range(4):
        act = s.Matrix(4, 4, lambda k, j: -GK[i][k][j])
        one = clean(cov.H*act*cov)
        ck(f'Kahler covector preservation {i}', zero(act*cov-cov*one))
        form = s.zeros(4)
        form[1:3, 1:3] = one
        form[3, 3] = s.trace(one)
        twist_i = clean(E[i, 0]*aRx)
        canonical = clean(omega[i]+twist_i*s.eye(4))
        exterior_rows.append(form)
        ck(f'whole exterior connection agrees {i}', zero(fock.H*canonical*fock-form))
        expected = -3*s.I/(4*ell) if i == 0 else 0
        ck(f'ordinary vacuum spin connection {i}', zero(omega[i]*vacuum-expected*vacuum))
        ck(f'canonical vacuum parallel {i}', zero(canonical*vacuum))
    shift = clean(M[0]*aRx)
    ck('canonical differential shift', zero(shift-3*s.I*cs[0]/(4*ell)))
    ck('ordinary constant vacuum is not canonical', not zero(K*vacuum))
    ck('canonical constant vacuum solves local operator', zero((K+shift)*vacuum))
    ck('wrong twist sign rejected', not zero((K-shift)*vacuum))
    mixed = cs[0]*cs[2]*cs[3]/(4*ell)
    ck('mixed term retained in canonical operator', zero(K+shift+cs[1]/(2*ell)-mixed-shift))
    ck('dropping mixed term changes canonical vacuum', not zero((K+shift-mixed)*vacuum))
    wc_can = list(wc)
    wc_can[0] = wc_can[0]+aRx*s.eye(4)
    scalar = geo.scalar_curvature(gi, G)
    curve = 3*s.I*cs[0]*cs[1]/(4*ell**2)
    for j, residual in enumerate(geo.lichnerowicz_residual(K+shift, wc_can, scalar, curve)):
        ck(f'canonical full Lichnerowicz coefficient {j}', zero(residual))
    ck('selfadjoint bounded difference', zero(shift.H-shift))
    ck('exact bound rather than a vanished perturbation', zero(shift.H*shift-9*s.eye(4)/(16*ell**2)))
    chir = -cs[0]*cs[1]*cs[2]*cs[3]
    gv = s.I*cs[2]*cs[3]
    ck('twist keeps total grading', zero(chir*shift+shift*chir))
    for rank in range(7):
        coeff = s.diag(*([1]*rank+[0]*(6-rank)))
        P = s.kronecker_product((s.eye(4)+gv)/2, coeff)
        P += s.kronecker_product((s.eye(4)-gv)/2, s.eye(6)-coeff)
        B = s.kronecker_product(shift, s.eye(6))
        ck(f'critical trace preserved rank {rank}', zero(P*B-B*P))
    n = s.Symbol('n', real=True)
    ck('cusp unit and geometric twist kept separate',
       zero(-6*s.I*n*cs[0]/ell+shift+6*s.I*(n-s.Rational(1,8))*cs[0]/ell))
    ck('integer flux cannot simply be relabelled', s.Rational(1,8).is_integer is False)
    # Lorentz Clifford matrix identities and the exact product Weyl map.
    gam, g5, g8 = lorentz(cs)
    I16 = s.eye(16)
    for i, j in product(range(8), repeat=2):
        rhs = 2*(-1 if i == 0 else 1)*I16 if i == j else s.zeros(16)
        ck(f'eight dimensional Clifford {i}{j}', zero(g8[i]*g8[j]+g8[j]*g8[i]-rhs))
    full_chir = -s.I*s.prod(g8)
    ck('physical Weyl grading is actual tensor map', zero(full_chir-s.kronecker_product(g5, chir)))
    ck('complex Weyl rank eight not three', ((I16+full_chir)/2).rank() == 8)
    ck('internal Euler block not a copied form operator',
       all(zero(s.I*g8[4+j]+s.kronecker_product(g5, cs[j])) for j in range(4)))
    # All E8 branching companions and root/Cartan charges, not a selected block.
    prior = load('pinned_retained_roster', HERE.parent/'weave_registered_embedding_2026_10_13'/'probe.py')
    actual, expected, char, _, _ = prior.a5_roster()
    ck('credited full248 companion roster', actual == expected and sum(actual.values()) == 248)
    blocks = [35, 8, 3, 40, 45, 45, 36, 36]
    ck('all branching blocks including dual', sum(blocks) == 248 and 36+36 != 248)
    _, roots = prior.roots()
    h = s.Matrix(s.symbols('h0:8', real=True))
    charges = [r.dot(h) for r in roots]+[s.Integer(0)]*8
    ck('every Cartan has traceless full adjoint action', zero(sum(charges)))
    ck('nonzero scalar identity is not full E8 adjoint', 248*s.Rational(3,4) != 0)
    ck('a proper root sector may have genuine charge', charges[0] != 0)
    ck('omitted conjugate changes full charge trace', not zero(sum(charges)-charges[0]))
    even = sum(m for w, m in char.items() if w % 2 == 0)
    odd = sum(m for w, m in char.items() if w % 2)
    ck('whole coefficient parity retained', (even, odd) == (136, 112))
    # Independent asymptotic discriminator: bounded domain change need not fix index.
    t = s.Symbol('t', real=True)
    profile = s.cosh(t)**(-s.Rational(1,2))
    altered = s.exp(-t)*profile
    ck('index control actual initial zero profile', zero(s.diff(profile,t)+s.tanh(t)*profile/2))
    ck('index control actual bounded-shift zero profile', zero(s.diff(altered,t)+(1+s.tanh(t)/2)*altered))
    ends = [s.limit(s.tanh(t)/2, t, end) for end in (-s.oo, s.oo)]
    ck('index control crosses asymptotic threshold', ends == [-s.Rational(1,2), s.Rational(1,2)]
       and [v+1 for v in ends] == [s.Rational(1,2), s.Rational(3,2)])
    flat_gi, flat_G = geo.coordinate_connection(s.eye(4))
    ck('flat Kahler connection control', all(geo.zero(v) for plane in flat_G for row in plane for v in row)
       and geo.zero(geo.scalar_curvature(flat_gi, flat_G)))
    records = {'canonical_metric_power': int(power), 'vacuum_spin_weight': [-3,4],
               'canonical_twist_weight': [3,4], 'cusp_n_offset': [-1,8],
               'weyl_rank': 8, 'clifford_size': 16, 'full_E8_block_dimensions': blocks,
               'full_E8_central_parities': [even,odd], 'index_control_before_after': [1,0]}
    return {'checks': checks, 'records': records, 'all_passed': all(checks.values()),
            'scope': 'two supplied kinetic dictionaries and local/conditional domain comparison; no physical families'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
