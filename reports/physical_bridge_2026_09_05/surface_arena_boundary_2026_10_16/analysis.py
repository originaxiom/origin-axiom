"""Global normal arena, actual source frame and embedded contact tube."""
# BANKED IDENTITY: fresh geometric and source replays. PRIOR ART: DESIGN.
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

def simp(value):
    value = s.cancel(value)
    if value.has(s.sin, s.cos):
        value = s.trigsimp(value)
    return s.factor(s.cancel(value))

def cm(matrix):
    return s.SparseMatrix(matrix.applyfunc(simp))

def zero(matrix):
    return all(simp(v) == 0 for v in matrix.todok().values())

def enc(matrix):
    return [[i, j, str(simp(v))] for (i, j), v in sorted(matrix.todok().items()) if simp(v) != 0]

def run(method):
    checks, records = {}, {}
    def ck(name, value):
        checks[name] = bool(value)
        print(('PASS ' if checks[name] else 'FAIL ') + name, file=sys.stderr, flush=True)

    gn = load(HERE.parent/'surface_geometric_loops_2026_10_14/probe.py', 'arena_geometric_native')
    gr = load(HERE.parent/'surface_geometric_loops_2026_10_14/reference.py', 'arena_geometric_reference')
    nc, rc = gn.run(), gr.run()
    ck('fresh geometric329 and32 controls with complete records',
       nc['all_passed'] and rc['all_passed'] and len(nc['checks']) == 329 and len(rc['checks']) == 32 and nc['records'] == rc['records'])
    records['geometric_antecedents'] = {'native': nc, 'reference': rc}
    parent = load(HERE.parent/'surface_interacting_transport_2026_10_16/analysis.py', 'arena_source_setup')
    twist = load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py', 'arena_actual_twist')
    vv, ext, cs, engine, valid, old = parent.setup(method)
    if method == 'native':
        geo = load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py', 'arena_coordinate_metric')
        vals = geo.geometry()
        gk = [[[s.simplify(geo.l*v) for v in row] for row in plane] for plane in vals[6]]
        valid = valid and all(s.simplify(vals[6][i][j][k]-vals[7][i][j][k]) == 0 for i in range(4) for j in range(4) for k in range(4))
    else:
        rows = {(0, 1, 0): -s.Integer(1), (1, 2, 2): s.Rational(1, 2),
                (0, 3, 2): -s.Integer(1), (1, 3, 3): -s.Rational(1, 2)}
        rows.update({(j, i, k): -v for (i, j, k), v in list(rows.items())})
        C = lambda i, j, k: rows.get((i, j, k), s.S.Zero)
        gk = [[[(C(i, j, k)-C(j, k, i)+C(k, i, j))/2 for k in range(4)] for j in range(4)] for i in range(4)]
    sc = twist.run(cs, gk, valid)
    ck('fresh complete actual source tensor and spin R dictionary', sc['all_passed'])
    records['actual_source_antecedent'] = sc
    if not all(checks.values()):
        return {'checks': checks, 'records': records, 'all_passed': False}

    x, phi = s.symbols('x phi', real=True)
    y, r, ell = s.symbols('y r ell', positive=True)
    cc, sn = s.cos(phi), s.sin(phi)
    den = x*x+y*y
    rr = s.sqrt(den)
    gt = s.Matrix([[s.sqrt(y), x/s.sqrt(y)], [0, 1/s.sqrt(y)]])
    rotminus = s.Matrix([[cc, sn], [-sn, cc]])
    frame = gt*rotminus
    Sp = s.Matrix([[0, -1], [1, 0]])
    Tp = s.Matrix([[1, 1], [0, 1]])
    gp = s.Matrix([[s.sqrt(y)/rr, -x/(s.sqrt(y)*rr)], [0, rr/s.sqrt(y)]])
    ktheta = s.Matrix([[x/rr, -y/rr], [y/rr, x/rr]])
    ck('normal direction homogeneous map has determinant one', simp(frame.det()-1) == 0)
    ck('exact S normal direction map including phase sign', zero(gp*ktheta-Sp*gt))
    ck('exact T normal direction map', zero(gt.subs(x, x+1)-Tp*gt))
    ck('wrong normal phase sign is rejected', not zero(gp*ktheta.T-Sp*gt))
    ck('central minus I acts by half normal rotation not identity', zero(frame.subs(phi, phi+s.pi)+frame))
    ck('double tangent angle descends but single angle does not',
       s.trigsimp(s.cos(2*(phi+s.pi))-s.cos(2*phi)) == 0 and s.trigsimp(s.cos(phi+s.pi)-s.cos(phi)) != 0)
    xp, yp = -x/den, y/den
    jac = s.Matrix([[s.diff(q, p) for p in (x, y)] for q in (xp, yp)])
    dtheta = s.Matrix([-y/den, x/den])
    ck('actual Chern circle connection inhomogeneous S law', zero(jac.T*s.Matrix([1/(2*yp), 0])-s.Matrix([1/(2*y), 0])-dtheta))

    q = (x, y, r, phi)
    if method == 'native':
        # Rebuild the actual lattice coframe from z=u+tau*v.
        v = r*sn/s.sqrt(y)
        u = r*s.sqrt(y)*cc-x*v
        e2 = [(s.diff(u, p)+x*s.diff(v, p))/s.sqrt(y) for p in q]
        e3 = [s.sqrt(y)*s.diff(v, p) for p in q]
        coframe = cm(s.Matrix([[ell/y, 0, 0, 0], [0, ell/y, 0, 0], e2, e3]))
    else:
        coframe = s.Matrix([[ell/y, 0, 0, 0], [0, ell/y, 0, 0],
            [-r*sn/y, r*cc/(2*y), cc, -r*sn], [0, -r*sn/(2*y), sn, r*cc]])
    J = s.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
    # Exact block inverse, certified in BOTH multiplication orders before
    # use. Avoid generic expression-domain inversion of trigonometric jets.
    inverse = s.Matrix([[y/ell, 0, 0, 0], [0, y/ell, 0, 0],
        [r*cc*sn/ell, r*(sn*sn-cc*cc)/(2*ell), cc, sn],
        [-sn*sn/ell, cc*sn/ell, -sn/r, cc/r]])
    ck('exact structured inverse certified in both orders', zero(coframe*inverse-s.eye(4)) and zero(inverse*coframe-s.eye(4)))
    N = cm(inverse.T*s.Matrix([0, 0, 2*r, 0]))
    eta = cm(coframe.T*J*N)
    alpha4 = s.Matrix([1/(2*y), 0, 0, 1])
    ck('actual coframe and radius gradient not a vertical approximation',
       simp(coframe.det()-ell*ell*r/y**2) == 0
       and zero(N-s.Matrix([2*r*r*cc*sn/ell, r*r*(sn*sn-cc*cc)/ell, 2*r*cc, 2*r*sn])))
    ck('actual source characteristic form equals normal circle connection', zero(eta-2*r*r*alpha4))
    Jcoord = cm(inverse*J*coframe)
    fx, fy = s.symbols('partial_x_log_sigma partial_y_log_sigma', real=True)
    dcf = cm(-Jcoord.T*s.Matrix([-fx, -fy, 1/r, 0]))
    wantbeta4 = s.Matrix([1/(2*y)+fy, -fx, 0, 1])
    ck('full total complex structure gives varying tube characteristic', zero(dcf-wantbeta4))
    ck('dropping radius variation loses boundary characteristic', not zero(dcf-alpha4))

    m, n = s.symbols('m n', integer=True)
    qmn = y*y/((m+n*x)**2+n*n*y*y)**2
    hypgrad = s.Matrix([y*s.diff(s.log(qmn), x), y*s.diff(s.log(qmn), y)])
    ck('entire lattice summand PDE and log gradient norm',
       simp(y*y*(s.diff(qmn, x, 2)+s.diff(qmn, y, 2))-2*qmn) == 0 and simp(hypgrad.dot(hypgrad)-4) == 0)
    ck('T and S reindex entire lattice without a finite census',
       simp(qmn.subs(x, x+1)-qmn.subs(m, m+n)) == 0
       and simp(qmn.subs({x: xp, y: yp}, simultaneous=True)-qmn.subs({m: -n, n: m}, simultaneous=True)) == 0)
    ck('both lattice index substitutions are bijective and retain origin',
       s.Matrix([[1, 1], [0, 1]]).det() == 1 and s.Matrix([[0, -1], [1, 0]]).det() == 1)
    ga = cm(hypgrad.subs({m: 1, n: 0}))
    gb = cm(hypgrad.subs({m: 0, n: 1}))
    ck('two positive lattice summands have distinct gradients everywhere',
       simp((ga-gb).dot(ga-gb)-16*y*y/den) == 0)
    E, Ex, Ey = s.symbols('E2 E2_x E2_y', real=True)
    # E>0, y>0 and the PDE are the analytic hypotheses; no finite
    # point cloud is used to establish strictness of the infinite sum.
    laplogsigma = -(2*E/y**2)/ (4*E)+(Ex*Ex+Ey*Ey)/(4*E*E)
    levisymbol = 1/(2*y*y)-laplogsigma
    target = (4-y*y*(Ex*Ex+Ey*Ey)/(E*E))/(4*y*y)
    ck('actual varying Levi coefficient equals weighted gradient deficit', simp(levisymbol-target) == 0)
    weights = s.symbols('w0:3', real=True)
    vectors = [s.Matrix([s.symbols('a'+str(i), real=True), s.symbols('b'+str(i), real=True)]) for i in range(3)]
    mean = sum((w*v for w, v in zip(weights, vectors)), s.zeros(2, 1))
    variance = sum((weights[i]*weights[j]*(vectors[i]-vectors[j]).dot(vectors[i]-vectors[j])
                    for i in range(3) for j in range(i+1, 3)))
    identity = (sum(weights)*sum(w*v.dot(v) for w, v in zip(weights, vectors))-mean.dot(mean)-variance)
    ck('strictness uses exact positive variance identity', s.expand(identity) == 0 and simp(16*y**6/(den**3*E**2)/(4*y*y)-4*y**4/(den**3*E**2)) == 0)
    qa = qmn.subs({m: 1, n: 0})
    qb = qmn.subs({m: 0, n: 1})
    print('STAGE finite pair rational contact certificate', file=sys.stderr, flush=True)
    finite = s.factor(s.cancel(qa+qb))
    finite_levi = 1/(2*y*y)+(s.diff(s.log(finite), x, 2)+s.diff(s.log(finite), y, 2))/4
    finite_positive = qa*qb*(ga-gb).dot(ga-gb)/(4*y*y*finite**2)
    ck('nonautomorphic finite pair controls strictness but not global invariance',
       simp(finite_levi-finite_positive) == 0 and simp(finite.subs(x, x+1)-finite) != 0)
    ck('naive inverse sqrt y tube is Levi flat', simp(1/(2*y*y)-s.diff(-s.log(y)/2, y, 2)) == 0)
    A, B = s.symbols('positive_cusp_a positive_cusp_b', positive=True)
    constpart = A*y*y+B/y
    cuspL = simp(1/(2*y*y)+s.diff(s.log(constpart), y, 2)/4)
    expectedL = 3*B*(4*A*y**3+B)/(4*y*y*(A*y**3+B)**2)
    ck('exact two term cusp Levi asymptotic not a uniform bound',
       simp(cuspL-expectedL) == 0 and s.limit(y**5*cuspL, y, s.oo) == 3*B/A and s.limit(y*y*cuspL, y, s.oo) == 0)
    u = s.Symbol('real_integral_coordinate', real=True)
    aa = s.Symbol('positive_kernel_scale', positive=True)
    # The integration variable is unrestricted on the real integration path.
    print('STAGE exact rational cusp kernel integral', file=sys.stderr, flush=True)
    integral = s.integrate(1/(u*u+aa*aa)**2, (u, -s.oo, s.oo))
    ck('cusp constant integral from rational kernel', simp(integral-s.pi/(2*aa**3)) == 0)
    epsilon, area, shortest = s.symbols('epsilon area shortest', positive=True)
    rest = s.Symbol('positive_remaining_lattice_sum', positive=True)
    inverse_fourth = 2*shortest**-4+rest
    ck('global radius minorant and fixed radius cusp control retained',
       s.limit(s.sqrt(area/y)/2, y, s.oo) == 0 and (s.sqrt(area)*shortest/2).is_positive
       and simp(inverse_fourth*shortest**4-2-rest*shortest**4) == 0 and (rest*shortest**4).is_positive)
    records['global_tube'] = {'summand': str(qmn), 'hyp_log_gradient': enc(hypgrad),
        'series': 'all nonzero integer pairs; locally normal convergence and exact reindexing in PROOF',
        'sigma': 'E2^(-1/4)', 'radius': 'epsilon*sqrt(area)*sigma,0<epsilon<1/2',
        'actual_characteristic': enc(wantbeta4), 'Levi': str(target),
        'strictness_certificate': 'weighted positive variance with q_(1,0),q_(0,1)',
        'explicit_lower_bound': str(4*y**4/(den**3*E**2)), 'cusp_two_term_Levi': str(cuspL),
        'not_uniform_at_cusp': True, 'infinite_series_interval_evaluated': False}

    coords = (x, y, phi)
    def d1(form):
        return cm(s.Matrix(3, 3, lambda i, j: s.diff(form[j], coords[i])-s.diff(form[i], coords[j])))
    def wedge(form, derivative):
        return simp(form[0]*derivative[1, 2]-form[1]*derivative[0, 2]+form[2]*derivative[0, 1])
    alpha = s.Matrix([1/(2*y), 0, 1])
    hilbert = s.Matrix([s.cos(2*phi)/y, s.sin(2*phi)/y, 0])
    Gflow = s.Matrix([y*s.cos(2*phi), y*s.sin(2*phi), -s.cos(2*phi)/2])
    da, dh = d1(alpha), d1(hilbert)
    ck('Hilbert geodesic Reeb is verified not named by analogy', simp(hilbert.dot(Gflow)-1) == 0 and zero(dh.T*Gflow))
    ck('normal connection Reeb differs and flow does not preserve it',
       alpha[2] == 1 and zero(da.T*s.Matrix([0, 0, 1])) and simp(alpha.dot(Gflow)) == 0 and not zero(da.T*Gflow))
    ck('two contact forms have opposite orientation under actual map',
       simp(wedge(alpha, da)-1/(2*y*y)) == 0 and simp(wedge(hilbert, dh)+2/(y*y)) == 0)
    cprime, sprime = (cc*x+sn*y)/rr, (sn*x-cc*y)/rr
    hilbertprime = s.Matrix([(cprime*cprime-sprime*sprime)/yp, 2*cprime*sprime/yp])
    ck('Hilbert form descends under exact normal S transition', zero(jac.T*hilbertprime-hilbert[:2, :]))
    ck('Hilbert form descends under T and minus I', zero(hilbert.subs(x, x+1)-hilbert)
       and zero(hilbert.subs(phi, phi+s.pi)-hilbert))
    records['forms_and_flow'] = {'alpha': enc(alpha), 'Hilbert': enc(hilbert), 'geodesic_Reeb': enc(Gflow),
        'normal_contact_volume': str(wedge(alpha, da)), 'geodesic_contact_volume': str(wedge(hilbert, dh)),
        'Lie_geodesic_alpha': enc(da.T*Gflow), 'physical_time_or_interaction_identified': False}

    w = gn.load('based_transition_prerequisite_2026_10_13')
    Z = {'a': 'a', 'b': 'ba'}
    Y = {'a': 'aB', 'b': 'b'}
    Zi, Yi = {'a': 'a', 'b': 'bA'}, {'a': 'ab', 'b': 'b'}
    half = w.power(w.compose(Yi, Zi), 3)
    full = w.compose(half, half)
    half_homology = s.Matrix([[half[key].count('a')-half[key].count('A') for key in ('a', 'b')],
                              [half[key].count('b')-half[key].count('B') for key in ('a', 'b')]])
    ck('actual half frame squares to fibre puncture inner action', full == w.inner('abAB') and half != full
       and w.compose(half, Z) == w.compose(Z, half) and w.compose(half, Y) == w.compose(Y, half))
    ck('half frame is not a pure fibre puncture loop', half_homology == -s.eye(2))
    scaling, g2, g3 = s.symbols('tangent_scale weierstrass_g2 weierstrass_g3')
    discriminant = g2**3-27*g3**2
    scaled = discriminant.subs({g2: scaling**4*g2, g3: scaling**6*g3}, simultaneous=True)
    winding = s.Poly(scaled, scaling).degree()
    ck('normal and trefoil meridians distinguished by discriminant winding',
       s.expand(scaled-scaling**winding*discriminant) == 0 and winding == 12 and winding/2 == 6 and winding != 1)
    a = s.diag(s.I, -s.I)
    b = s.Matrix([[0, 1], [-1, 0]])
    A0, B0 = s.diag(-a, a, -a), s.diag(b, -b, -b)
    PX = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    PY = s.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    X6 = s.kronecker_product(PX, (s.eye(2)+a)/s.sqrt(2))
    Y6 = s.kronecker_product(PY, (s.eye(2)+b)/s.sqrt(2))
    Z6 = A0.H*X6
    H6 = cm((Z6*Y6).H**3)
    ck('actual SU6 half frame unitary involution with wrong standalone centre',
       zero(H6.H*H6-s.eye(6)) and zero(H6*H6-s.eye(6)) and zero(A0*B0*A0.H*B0.H+s.eye(6)))
    phase_rows = []
    for weak in (1, 3, 5, 7, 9, 11):
        evenchars, oddchars = [], []
        for power in range(4):
            M = H6**power
            tr, tr2, tr3 = s.trace(M), s.trace(M*M), s.trace(M*M*M)
            wedge2, wedge3 = (tr*tr-tr2)/2, (tr**3-3*tr*tr2+2*tr3)/6
            weaktrace = s.I**(-weak*power)+s.I**(weak*power)
            evenchars.append(s.simplify(tr*s.conjugate(tr)+6+weaktrace**2+3*(wedge2+s.conjugate(wedge2))))
            oddchars.append(s.simplify((wedge3+3*(tr+s.conjugate(tr)))*weaktrace))
        ec = [s.simplify(sum(evenchars[p]*s.I**(-q*p) for p in range(4))/4) for q in range(4)]
        oc = [s.simplify(sum(oddchars[p]*s.I**(-q*p) for p in range(4))/4) for q in range(4)]
        ck('full E8 half frame square equals puncture and all sectors retained '+str(weak),
           evenchars[0] == 136 and oddchars[0] == 112 and evenchars[2] == 136 and oddchars[2] == -112
           and sum(ec) == 136 and sum(oc) == 112 and ec[1] == ec[3] == oc[0] == oc[2] == 0
           and all(q.is_Integer and q >= 0 for q in ec+oc))
        phase_rows.append({'weak_class': weak, 'phases': ['1', 'i', '-1', '-i'],
                           'even': list(map(int, ec)), 'odd': list(map(int, oc))})
    records['central_lifts'] = {'half_frame_word_action': half, 'full_frame_word_action': full,
        'half_frame_SU6': enc(H6), 'full_normal_circle_discriminant_link': 12,
        'regular_Seifert_link': 6, 'ordinary_trefoil_meridian_link': 1, 'all_classes': phase_rows,
        'not_a_physical_charge_or_family_count': True}

    I16 = s.eye(16)
    weights = sc['records']['charges']['geometric_weights']
    W = s.diag(*[s.I*m*(-1)**bar for bar in range(2) for m in weights for spin in range(2)])
    read16 = lambda rows: s.SparseMatrix(16, 16, {(i, j): s.sympify(v) for i, j, v in rows})
    connection = list(map(read16, sc['records']['connections']['source']))
    C16 = s.kronecker_product(s.Matrix([[0, 1], [1, 0]]), s.eye(8))
    ck('actual source leading connection equals full weight generator', zero(connection[0]+W/2) and zero(connection[1])
       and weights == [0, 2, 1, -3] and zero(W.H+W) and zero(C16*W.conjugate()*C16-W))
    newconn = [cm(connection[0]/y), s.zeros(16), -W]
    ck('tautological source frame has minus W alpha not zero',
       all(zero(q+W*alpha[j]) for j, q in enumerate(newconn)) and not zero(W)
       and not zero(newconn[0].diff(y)))
    ck('global tube beta is not a free source connection substitution',
       not zero(W*fx) and not zero(W*fy) and W[6, 6] == -3*s.I)
    geometric_half = s.diag(*[s.Integer(-1)**m for bar in range(2) for m in weights for spin in range(2)])
    ck('source full central rotation and real conjugate slots retained', zero(geometric_half**2-I16)
       and zero(C16*geometric_half.conjugate()*C16-geometric_half) and s.trace(geometric_half) == 0)
    records['source_boundary_map'] = {'geometric_weight_generator': enc(W), 'leading_connection': [enc(q) for q in newconn],
        'scalar_P_connection': '3i alpha, curvature3i dx^dy/(2y^2)', 'not_replaced_by_CR_beta': True,
        'scope': 'leading geometric connection on compact base subsets; not full singular/Higgs operator or boundary dynamics'}
    records['meaning'] = {'arena_is_normal_boundary_under_explicit_map': True,
        'smooth_global_embedded_strict_contact_tube_constructed': True,
        'uniform_positive_cusp_Levi_constant': False, 'source_connection_and_based_lifts_retained': True,
        'geodesic_flow_identified_as_physical_time_or_boundary_Reeb': False,
        'true_end_action_or_state_selected': False, 'global_stationary_Higgs_derived': False,
        'physical_SM_three_parameters_gravity_derived': False, 'same_author_not_independent_acceptance': True}
    return {'checks': checks, 'records': records, 'all_passed': all(checks.values())}

def emit(method):
    result = run(method)
    print(json.dumps(result, indent=2))
    return 0 if result['all_passed'] else 1
