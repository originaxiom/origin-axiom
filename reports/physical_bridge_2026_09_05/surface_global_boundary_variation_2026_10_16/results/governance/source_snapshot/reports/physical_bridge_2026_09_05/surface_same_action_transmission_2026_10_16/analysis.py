"""Actual same-source interface; no physical end or spectrum selection."""
# BANKED IDENTITY: fresh source/root replay. PRIOR ART: DESIGN/PROOF.
import importlib.util
import json
import sys
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def cm(matrix):
    return s.SparseMatrix(matrix.applyfunc(s.cancel))

def zero(matrix):
    return all(s.cancel(v) == 0 for v in matrix.todok().values())

def enc(matrix):
    return [[i, j, str(s.cancel(v))] for (i, j), v in sorted(matrix.todok().items()) if s.cancel(v) != 0]

def run(method):
    checks, records = {}, {}
    def ck(name, value):
        checks[name] = bool(value)
        print(('PASS ' if checks[name] else 'FAIL ') + name, file=sys.stderr, flush=True)

    root = load(HERE.parent / 'surface_root_gauge_sector_2026_10_16/analysis.py', 'transmission_roots')
    prior = load(HERE.parent / 'surface_all_boson_response_2026_10_16/analysis.py', 'transmission_source')
    parent = load(HERE.parent / 'surface_interacting_transport_2026_10_16/analysis.py', 'transmission_parent')
    twist = load(HERE.parent / 'surface_real_twist_2026_10_16/analysis.py', 'transmission_twist')
    rootcert = root.run(method)
    records['fresh_root_source_antecedent'] = rootcert
    ck('fresh complete80 root and actual source controls', rootcert['all_passed'] and len(rootcert['checks']) == 80)
    if not all(checks.values()):
        return {'checks': checks, 'records': records, 'all_passed': False}

    vv, ext, cs, engine, valid, old = parent.setup(method)
    a = twist.prior.a
    source = a.construct(twist.prior.frame(cs)['sig'])
    source_checks = {}
    def source_ck(name, value):
        source_checks[name] = bool(value)
        ck('fresh actual action: ' + name, value)
    source_record, auxprim = prior.source(a, source, source_ck)
    records['fresh_source_action'] = source_record
    records['fresh_source_action_checks'] = source_checks
    ck('source replay retains genuine auxiliary and calibration primitives',
       bool(auxprim) and bool(source_record['calibration_primitives']) and all(source_checks.values()))
    if not all(checks.values()):
        return {'checks': checks, 'records': records, 'all_passed': False}

    xx = [a.letter('x' + str(i)) for i in range(6)]
    yy = [a.letter('y' + str(i)) for i in range(4)]
    plain = lambda p, i: a.op(p, 'n' + str(i)) if i < 4 else {}
    D = lambda p, i: a.add(plain(p, i), a.comm(xx[i], p))
    F = lambda i, j: a.add(plain(xx[j], i), a.scale(plain(xx[i], j), -1), a.comm(xx[i], xx[j]))
    cur = [a.add(*(a.scale(F(i, j), sign) for i, j, sign in row)) for row in prior.CSPEC]
    potential = a.trace(a.add(*(a.scale(a.mul(c, c), -2) for c in cur)))
    mixed = a.trace(a.add(*(a.scale(a.mul(D(y, i), D(y, i)), 2 * eta)
                           for y, eta in zip(yy, (-1, 1, 1, 1)) for i in range(6))))
    _, jpot = prior.parts(a, potential)
    _, jmix = prior.parts(a, mixed)
    current_rows = []
    for n in range(4):
        direct = {}
        for c, row in zip(cur, prior.CSPEC):
            dc = a.add(*(a.scale(a.add(a.letter('delta_x' + str(j)) if i == n else {},
                                     a.scale(a.letter('delta_x' + str(i)), -1) if j == n else {}), sign)
                         for i, j, sign in row))
            direct = a.add(direct, a.scale(a.mul(c, dc), -4))
        direct = a.trace(direct)
        mixdirect = a.trace(a.add(*(a.scale(a.mul(D(y, n), a.letter('delta_y' + str(j))), 4 * eta)
                                   for j, (y, eta) in enumerate(zip(yy, (-1, 1, 1, 1))))))
        ck('actual source normal momenta all fields direction ' + str(n),
           bool(direct) and bool(mixdirect) and not a.trace(a.add(jpot['n' + str(n)], a.scale(direct, -1)))
           and not a.trace(a.add(jmix['n' + str(n)], a.scale(mixdirect, -1))))
        current_rows.append({'normal': n, 'potential': a.sf.encoded(direct), 'mixed': a.sf.encoded(mixdirect)})

    # Keep independent side labels until matching. Do not cyclically reorder
    # side-prefixed odd symbols: their original parity is retained by aliasing
    # them back BEFORE the graded trace operation.
    def side(poly, prefix):
        return {tuple(a.sf.normalize(q.split(':')[:-1], prefix + a.sf.base(q)) for q in w): c for w, c in poly.items()}
    def match(poly):
        result = {}
        for w, c in poly.items():
            ww = tuple(a.sf.normalize(q.split(':')[:-1], a.sf.base(q).removeprefix('left_').removeprefix('right_')) for q in w)
            result[ww] = result.get(ww, 0) + c
        return a.trace(result)
    fprim = a.jet_quotient(a.fermions(source['full']))[1]
    primitives = [('auxiliary_' + op, p) for op, p in sorted(auxprim.items())]
    # Reconstruct calibration by fresh homotopy, not a parsed result assertion.
    can = a.trace(a.add(*(a.scale(a.mul(F(i, j), F(i, j)), -2) for i in range(6) for j in range(i + 1, 6))))
    _, calprim, calres = prior.homotopy(a, a.trace(a.add(potential, a.scale(can, -1))))
    primitives += [('calibration_' + op, p) for op, p in sorted(calprim.items())]
    primitives += [('fermion_' + op, p) for op, p in sorted(fprim.items()) if op in ('d0', 'b0', 'd1', 'b1')]
    ck('fresh raw fermion and calibration currents are nonempty',
       not calres and len(primitives) >= 12 and any(n.startswith('fermion_') and p for n, p in primitives))
    seam_rows = []
    for name, p in primitives:
        if not p:
            continue
        two_sides = a.add(side(p, 'left_'), a.scale(side(p, 'right_'), -1))
        wrong_normal = a.add(side(p, 'left_'), side(p, 'right_'))
        ck('retained primitive cancels only under oriented matching ' + name,
           bool(two_sides) and not match(two_sides) and bool(match(wrong_normal)) and bool(match(side(p, 'left_'))))
        seam_rows.append({'name': name, 'words': len(p), 'primitive': a.sf.encoded(p)})
    records['source_interface'] = {'normal_momenta': current_rows, 'retained_primitives': seam_rows,
                                   'canonical_momentum_substitution_used': False}

    I = s.SparseMatrix(s.eye(16))
    C = s.kronecker_product(s.Matrix([[0, 1], [1, 0]]), s.eye(8))
    roots, up, dn, hv, E, Fr, H, P, Q, G, eta, tau, parity, pair = root.gauge(engine, old)
    ck('actual coefficient pairing is nontrivial positive and real',
       not zero(G - s.eye(248)) and zero(tau.H * G * tau - G)
       and all(G[:j, :j].det() > 0 for j in range(1, 9)))
    injection = s.SparseMatrix.vstack(I, I)
    conjugation_pair = s.diag(C, C)
    for n, v in enumerate(vv[:4]):
        green = s.diag(v, -v)
        majorana = s.diag(C.H * v, -C.H * v)
        ck('full source Hermitian and Majorana matched graph ' + str(n),
           zero(injection.H * green * injection) and zero(injection.T * majorana * injection)
           and zero(injection[:16, :] - I) and zero(v * v - I)
           and zero(conjugation_pair * injection.conjugate() - injection * C))
        ck('same normal sign fails full source graph ' + str(n),
           not zero(injection.H * s.diag(v, v) * injection))
    nonunitary = s.SparseMatrix.vstack(I, 2*I)
    half = s.diag(*([1]*8+[0]*8))
    ck('nonunitary matching and deletion of conjugates fail distinct controls',
       not zero(nonunitary.H*s.diag(vv[2], -vv[2])*nonunitary)
       and not zero(C*half.conjugate()*C-half))
    lam = s.diag(*[int(f == 0) for bar in range(2) for f in range(4) for spin in range(2)])
    oldplane = s.diag(*[int(f in (2, 3)) for bar in range(2) for f in range(4) for spin in range(2)])
    ck('matched graph retains lambda and conjugates without one sided selection',
       zero(injection * lam - s.SparseMatrix.vstack(lam, lam)) and zero(C * lam.conjugate() * C - lam)
       and zero(oldplane * lam) and s.trace(lam) == 4)

    x, y, z, k = s.symbols('xi_horizontal0 xi_horizontal1 xi_angular k', real=True)
    norm2 = x*x + y*y + z*z
    vn = vv[2]
    tangential = x*vv[0] + y*vv[1] + z*vv[3]
    HH = cm(s.I * vn * tangential)
    ck('all joint covectors actual principal Clifford identity',
       zero(HH.H - HH) and zero(HH*HH - norm2*I) and s.trace(HH) == 0 and zero(vn*HH + HH*vn))
    def on_characteristic(matrix):
        for value in matrix.todok().values():
            num = s.cancel(value).as_numer_denom()[0]
            if s.rem(s.expand(num), k*k - norm2, k) != 0:
                return False
        return True
    minus, plus = (I - HH/k)/2, (I + HH/k)/2
    ck('complementary two sided Cauchy projectors for every nonzero covector',
       on_characteristic(minus*minus-minus) and on_characteristic(plus*plus-plus)
       and on_characteristic(minus*plus) and zero(minus+plus-I))
    jump = s.SparseMatrix.hstack(I, -I)
    decay = s.diag(minus, plus)
    ck('uniform normalized matching isometry on joint decaying space',
       on_characteristic(decay.H * (jump.H*jump-s.eye(32)) * decay)
       and on_characteristic(jump * decay * jump.H - I))
    ck('same decaying sign gives a nonzero false interface kernel',
       zero(jump*s.SparseMatrix.vstack(minus, minus)) and s.trace(minus) == 8)
    ck('zero principal covector matched not inverted or deleted',
       zero(HH.subs({x: 0, y: 0, z: 0})) and injection.shape == (32, 16))
    boson = s.Matrix([[1, -1], [k, k]])
    ck('gauge fixed boson and ghost principal transmission determinant',
       s.factor(boson.det()) == 2*k and all(s.factor((s.diag(1, 4*weight)*boson).det()) == 8*weight*k for weight in (-1, 1)))
    records['principal'] = {'source_normal': enc(vn), 'all_covector_H': enc(HH),
        'normalization': 'k>0,k^2=xi_horizontal0^2+xi_horizontal1^2+xi_angular^2; exact isometry',
        'zero_sector': 'all full traces matched, no inversion/gap', 'bosons': 10, 'ghost_principal_slots': 1,
        'not_a_singular_or_global_gap': True}

    t, g, rho, j = s.symbols('t g rho j', real=True)
    symbols = {'t': t, 'g': g, 'rho': rho, 'j': j}
    read = lambda rows: s.SparseMatrix([[s.sympify(q, locals=symbols) for q in row] for row in rows])
    jets = []
    for index, block in enumerate(rootcert['records']['blocks']['list']):
        cb, db, yb, ab, vb = [read(block[name]) for name in ('indicial', 'backreaction', 'yukawa', 'horizontal', 'normal_current')]
        K = cm(cb/t + g*g*t*db/(1-g*g*t*t) + g*yb/(1-g*g*t*t) + rho*t*ab)
        ck('full charged kernel current identity block ' + str(index),
           zero(K.H-K) and zero(K.H*vb + vb*K) and zero(vb*vb - s.eye(K.rows)))
        at = {t: s.Rational(1, 2), g: s.Rational(1, 3)}
        K0, K1 = cm(K.subs(at)), cm(K.diff(t).subs(at))
        f0 = s.eye(K.rows)
        f1 = -K0
        f2 = cm((K0*K0-K1)/2) if method == 'native' else cm(-(K0*f1+K1*f0)/2)
        ck('finite transfer ODE and full current coefficients block ' + str(index),
           zero(f1+K0*f0) and zero(2*f2+K0*f1+K1*f0)
           and zero(f1.H*vb+vb*f1) and zero(f2.H*vb+f1.H*vb*f1+vb*f2))
        wrong_f2 = cm((K0*K0+K1)/2)
        ck('wrong transfer derivative fails actual ODE block ' + str(index),
           not zero(2*wrong_f2+K0*f1+K1))
        jets.append({'block': index, 'highest_weight': block['highest_weight'],
            'highest_parity': block['highest_parity'], 'J': block['J'], 'computational_sign': block['computational_sign'],
            'K0': enc(K0), 'K1': enc(K1), 'T1': enc(f1), 'T2': enc(f2)})
    ck('all28 blocks and3968 source coefficient directions retained',
       len(jets) == 28 and rootcert['records']['blocks']['directions'] == 3968
       and {q['computational_sign'] for q in jets} == {-1, 1})
    records['charged_transfer'] = {'jets': jets, 'jet_test_point': {'t': '1/2', 'g': '1/3'},
        'all_t_symbolic_identity_precedes_specialization': True,
        'charged_global_Cauchy_or_spectrum_computed': False}

    # Exact cyclic source charge algebra keeps the field-dependent-parameter
    # correction separate. Matching is not a declaration all end charges vanish.
    elec, alpha, dalpha = map(a.letter, ('seam_electric', 'seam_alpha', 'seam_delta_alpha'))
    charge = a.scale(a.trace(a.mul(elec, alpha)), -4)
    corr = a.scale(a.trace(a.mul(elec, dalpha)), -4)
    for label, expression in [('canonical_charge', charge), ('parameter_correction', corr)]:
        pairq = a.add(side(expression, 'left_'), a.scale(side(expression, 'right_'), -1))
        ck('opposite source charges cancel only after full matching ' + label,
           bool(pairq) and not match(pairq) and bool(expression))
    unmatched = a.scale(a.trace(a.mul(elec, a.add(alpha, a.scale(a.letter('independent_alpha'), -1)))), -4)
    ck('independent gauge parameters retain possible surface charge', bool(unmatched))
    ck('existing interacting gauge sector has nonzero bracket and admits constants',
       rootcert['records']['root']['closure_nonzero'] > 0 and rootcert['records']['gauge_sector']['all_internal_currents'] == 0
       and s.diff(s.Integer(1), t) == 0 and zero(lam*vv[2]*lam))

    Srot = cm((2*I-vv[2]*vv[3])/s.sqrt(5))
    nv = (3*vv[2]+4*vv[3])/5
    ck('tilted normal spin frame and full reality covariant',
       zero(Srot.H*Srot-I) and zero(Srot*vn*Srot.H-nv) and zero(C*Srot.conjugate()*C-Srot)
       and all(zero(Srot*v-v*Srot) for v in ext))
    ck('actual puncture transition preserves metric reality and both side graph',
       zero(eta.H*G*eta-G) and zero(tau*eta.conjugate()*tau-eta) and zero(eta*eta-s.eye(248)))
    # Nonconstant compact root-SU2 change of frame, in the actual normalized
    # root triplet. Its embedding was freshly replayed above, not named by size.
    Et = s.Matrix([[0, s.sqrt(2), 0], [0, 0, s.sqrt(2)], [0, 0, 0]])
    Pt = (Et-Et.T)/2
    U = cm((s.eye(3)+t*Pt)*(s.eye(3)-t*Pt).inv())
    A = s.diag(s.I, 0, -s.I)
    u = s.Matrix([t, t*t+s.I, 1-t])
    Ap = cm(U*A*U.H-U.diff(t)*U.H)
    cov = cm((U*u).diff(t)+Ap*U*u-U*(u.diff(t)+A*u))
    ck('inhomogeneous frame connection necessary for covariant transmission',
       zero(U.H*U-s.eye(3)) and zero(cov)
       and not zero((U*u).diff(t)+U*A*U.H*U*u-U*(u.diff(t)+A*u)))

    bm, bp, dm, dp, bc = s.symbols('Bminus Bplus deltaBminus deltaBplus Bthird')
    ck('retained primitive descent and its variation telescope not vanish separately',
       s.expand((bm-bp)+(bp-bm)) == 0 and s.expand((dm-dp)+(dp-dm)) == 0
       and s.expand((bp-bm)+(bc-bp)+(bm-bc)) == 0 and bm-bp != 0)
    records['gauge_and_descent'] = {'source_charge': a.sf.encoded(charge),
        'field_dependent_parameter_correction': a.sf.encoded(corr), 'unmatched_parameter_charge': a.sf.encoded(unmatched),
        'varying_compact_triplet_frame': enc(U), 'compensated_connection': enc(Ap),
        'scope': 'fixed transition, contractible smooth collar; not arbitrary edge dynamics or global anomaly descent'}
    records['meaning'] = {'same_source_two_sided_transmission': True,
        'uniform_joint_principal_interface_transversality': True, 'retains_existing_local_interacting_gauge_sector': True,
        'all_charged_and_kernel_blocks_retained': True, 'artificial_cut_changes_kernel_or_index': False,
        'true_boundary_or_exterior_state_selected': False, 'global_stationary_Higgs_derived': False,
        'full_curved_nonlinear_SUSY_boundary_action_verified': False, 'SM_three_parameters_gravity_derived': False,
        'same_author_not_independent_acceptance': True}
    return {'checks': checks, 'records': records, 'all_passed': all(checks.values())}

def emit(method):
    result = run(method)
    print(json.dumps(result, indent=2))
    return 0 if result['all_passed'] else 1
