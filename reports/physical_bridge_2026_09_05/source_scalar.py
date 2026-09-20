"""R37 exact ADDED tube-scalar controls; not a hyperbolic spectrum/phase.

Execute only after SOURCE_SCALAR_DESIGN and all scientific files are sealed.
The flat comparator is separate from the nonzero sourced background.
"""
from functools import lru_cache
import json

import sympy as sp

t = sp.Symbol('t', real=True)
e = sp.Symbol('epsilon', positive=True)
r = sp.Symbol('r', real=True)
f, eta, W, lam = sp.symbols('f eta W lambda_S', positive=True)


def res(a, b=0):
    a, b = sp.sympify(a), sp.sympify(b)
    if a.has(sp.Float) or b.has(sp.Float):
        raise ValueError('exact operands required before subtraction')
    return sp.simplify(sp.trigsimp(sp.cancel(sp.expand(a-b))))


def matrix_res(a, b):
    return (a-b).applyfunc(res)


@lru_cache(maxsize=1)
def action_control():
    """Ten complex S components, full source feedback and Cartesian variation."""
    C, k, sig, lq, g = sp.symbols('C kappa sigma lambda_Q g', positive=True)
    d, curl, B, A, X, Y, pX, pY = sp.symbols('d curl B A X Y pX pY', real=True)
    xs, ys = sp.symbols('x0:10', real=True), sp.symbols('y0:10', real=True)
    px, py = sp.symbols('px0:10', real=True), sp.symbols('py0:10', real=True)
    S = [(x+sp.I*y)/sp.sqrt(2) for x, y in zip(xs, ys)]
    Q = (X+sp.I*Y)/sp.sqrt(2)
    N, n = sum((x*x+y*y)/2 for x, y in zip(xs, ys)), (X*X+Y*Y)/2
    SS = sum(z*z for z in S)
    D = d-k*sig*(4*n+2*N)
    potential = C*(curl**2+D**2)+B**2/(2*g*g)+sig*(
        lq*(n-f*f)**2+r*N+lam*N*N-eta*(sp.conjugate(Q)*SS+Q*sp.conjugate(SS)))
    QS = (pX+sp.I*pY)/sp.sqrt(2)+4*sp.I*A*Q
    DS = [(a+sp.I*b)/sp.sqrt(2)+2*sp.I*A*z for a, b, z in zip(px, py, S)]
    kinetic = sig*(sp.conjugate(QS)*QS+sum(sp.conjugate(z)*z for z in DS))
    total = potential+kinetic
    S_res = []
    for j in range(10):
        variation = (sp.diff(potential, xs[j])+sp.I*sp.diff(potential, ys[j]))/(sp.sqrt(2)*sig)
        target = (r+2*lam*N-4*C*k*D)*S[j]-2*eta*Q*sp.conjugate(S[j])
        S_res.append(res(variation, target))
    Q_var = (sp.diff(potential, X)+sp.I*sp.diff(potential, Y))/(sp.sqrt(2)*sig)
    Q_res = res(Q_var, (2*lq*(n-f*f)-8*C*k*D)*Q-eta*SS)
    current = 2*sig*(4*sp.im(sp.conjugate(Q)*QS)+2*sum(sp.im(sp.conjugate(z)*dz) for z, dz in zip(S, DS)))
    current_res = res(sp.diff(kinetic, A), current)
    variables = [d, curl, B, A, X, Y, pX, pY]+list(xs+ys+px+py)
    point = {v: 0 for v in variables}
    point.update({X: sp.sqrt(2)*f, d: 4*k*sig*f*f})
    gradient = [res(sp.diff(total, v).subs(point)) for v in variables]
    hessian = sp.hessian(potential, xs+ys).subs(point)/sig
    target_hess = sp.diag(*([r-2*eta*f]*10+[r+2*eta*f]*10))
    old = [d, curl, B, A, X, Y, pX, pY]
    mixed = sp.Matrix(20, len(old), lambda i, j: sp.diff(total, (xs+ys)[i], old[j]).subs(point))
    # Treating the source as independent of S is an incorrect off-shell variation.
    missing_feedback = -4*C*k*D*S[0]
    witness = res(missing_feedback.subs({xs[0]: 1, **{v: 0 for v in xs[1:]+ys}, X: 0, Y: 0, d: 0}))
    # All 45 real vector generators: the additional D5 current vanishes at S=0.
    d5_zero = []
    zero_s = {v: 0 for v in xs+ys}
    for a in range(10):
        for b in range(a+1, 10):
            value = 2*sig*sp.re(sp.conjugate(DS[a])*S[b]-sp.conjugate(DS[b])*S[a])
            d5_zero.append(res(value.subs(zero_s)))
    return dict(S_variations=S_res, Q_variation=Q_res,
                h_variation=res(sp.diff(potential, d), 2*C*D),
                central_current=current_res, stationary=gradient,
                scalar_hessian=matrix_res(hessian, target_hess), mixed_hessian=mixed,
                missing_feedback_witness=witness, D5_currents_at_zero=d5_zero)


def cov(z, charge, A):
    return sp.diff(z, t)+sp.I*charge*A*z


@lru_cache(maxsize=1)
def weighted_green():
    u, v, b0, sig, J, A, F = [sp.Function(n)(t) for n in ('u', 'v', 'b0', 'sigma', 'J', 'A', 'F')]
    q = sp.Symbol('q', real=True)
    weight = sig*J
    Lu = -cov(weight*cov(u, 2, A), 2, A)/weight
    Lv = -cov(weight*cov(v, -2, A), -2, A)/weight
    boundary = weight*(u*cov(v, -2, A)-v*cov(u, 2, A))
    green = res(weight*(v*Lu-u*Lv), sp.diff(boundary, t))
    wrongL = -cov(J*cov(u, 2, A), 2, A)/J
    omitted_weight = res(Lu, wrongL)
    # R36 identity on a tube: retain both interface terms and weight derivatives.
    b, w = sig*b0, u*v
    lap = lambda z, charge: cov(J*cov(z, charge, A), charge, A)/J
    h = lambda z: -lap(z, 1)+(q*q*sp.diff(F, t)**2-q*sp.diff(J*sp.diff(F, t), t)/J)*z
    du = cov(u, 1, A)+q*sp.diff(F, t)*u
    dv = cov(v, 1, A)+q*sp.diff(F, t)*v
    flux = cov(w, 2, A)/2+q*sp.diff(F, t)*w
    correction = lap(b, -2)/2-q*sp.diff(F, t)*cov(b, -2, A)
    interface = J*(b*flux-w*cov(b, -2, A)/2)
    overlap = res(b*(du*dv-(u*h(v)+v*h(u))/2)-w*correction, sp.diff(interface, t)/J)
    return dict(scalar_green=green, missing_weight_derivative=omitted_weight,
                weighted_overlap=overlap, natural_flux=weight*cov(u, 2, A))


@lru_cache(maxsize=1)
def canonical_control():
    x, y, Q4 = sp.symbols('x y Q4', real=True)
    S4 = (x+sp.I*y)/sp.sqrt(2)
    s0 = 1/sp.sqrt(W)
    quartic = res(W*lam*s0**4)
    locking = res(W*eta*s0**3)
    pot4 = r*(x*x+y*y)/2+quartic*(x*x+y*y)**2/4-locking*Q4*(x*x-y*y)
    hess = sp.hessian(pot4, (x, y)).subs({x: 0, y: 0, Q4: sp.sqrt(W)*f})
    length, radius = sp.symbols('L radius', positive=True)
    sig = 1/(sp.pi*sp.sinh(radius)**2)
    tube_weight = res(sig*2*sp.pi*length*sp.integrate(sp.sinh(t)*sp.cosh(t), (t, 0, radius)))
    return dict(norm=res(W*s0*s0, 1), quartic=quartic, locking=locking,
                hessian=matrix_res(hess, sp.diag(r-2*eta*f, r+2*eta*f)),
                masses=(r-2*eta*f, r+2*eta*f), tube_weight=tube_weight,
                tube_weight_residual=res(tube_weight, length))


@lru_cache(maxsize=None)
def integral_1d(expression, limit):
    return res(sp.integrate(sp.expand_trig(expression), (t, -limit, limit)))


@lru_cache(maxsize=1)
def flat_control():
    cs = (sp.cos(t), sp.sin(t))
    factors = [(cs[i], cs[j]) for i in range(2) for j in range(2)]
    M, P, flux, norm = [sp.zeros(4) for _ in range(4)]
    rawM, rawP = sp.zeros(4), sp.zeros(4)
    eigen, caps = [], []
    sigma = 1/(4*e*e)
    for i, (a, b) in enumerate(factors):
        eigen.append(res(-sp.diff(a, t, 2)*b-a*sp.diff(b, t, 2), 2*a*b))
        for j, (c, d) in enumerate(factors):
            xx, yy = integral_1d(a*c, e), integral_1d(b*d, e)
            dx = integral_1d(sp.diff(a, t)*sp.diff(c, t), e)
            dy = integral_1d(sp.diff(b, t)*sp.diff(d, t), e)
            rawM[i, j] = xx*yy/sp.pi**2
            rawP[i, j] = (dx*yy+xx*dy)/(2*sp.pi**2)
            M[i, j], P[i, j] = res(sigma*rawM[i, j]), res(sigma*rawP[i, j])
            norm[i, j] = res(integral_1d(a*c, sp.pi)*integral_1d(b*d, sp.pi)/sp.pi**2)
            # Opposite normals on the two x and two y faces; z derivatives vanish.
            xface = sp.diff(a*c, t).subs(t, e)-sp.diff(a*c, t).subs(t, -e)
            yface = sp.diff(b*d, t).subs(t, e)-sp.diff(b*d, t).subs(t, -e)
            zface = sp.diff(sp.Integer(1), t).subs(t, 1)-sp.diff(sp.Integer(1), t).subs(t, 0)
            caps.append(zface)
            flux[i, j] = res(sigma*(xface*yy+xx*yface+zface*xx*yy)/(2*sp.pi**2))
    a = sp.Rational(1, 2)+sp.sin(2*e)/(4*e)
    b = 1-a
    expectedM = sp.diag(a*a, a*b, a*b, b*b)/sp.pi**2
    expectedP = sp.diag(a*b, (a*a+b*b)/2, (a*a+b*b)/2, a*b)/sp.pi**2
    norm_v = sp.zeros(4)
    for i, (aa, bb) in enumerate(factors):
        for j, (cc, dd) in enumerate(factors):
            norm_v[i, j] = res((integral_1d(sp.diff(aa, t)*sp.diff(cc, t), sp.pi)*integral_1d(bb*dd, sp.pi)
                +integral_1d(aa*cc, sp.pi)*integral_1d(sp.diff(bb, t)*sp.diff(dd, t), sp.pi))/(2*sp.pi**2))
    return dict(M=M, P=P, flux=flux, M_formula=matrix_res(M, expectedM),
                P_formula=matrix_res(P, expectedP), scalar_norm=norm,
                one_form_norm=norm_v, eigen_residuals=eigen, axial_caps=caps,
                interface=matrix_res(2*P, 2*M+flux), omitted_interface=res((2*P-2*M)[0, 0]),
                unweighted_M=rawM.applyfunc(res), unweighted_P=rawP.applyfunc(res),
                measure_M=matrix_res(rawM, 4*e*e*M), measure_P=matrix_res(rawP, 4*e*e*P))


@lru_cache(maxsize=1)
def spectral_control():
    a, b = sp.symbols('a b', real=True)
    M = sp.diag(a*a, a*b, a*b, b*b)/sp.pi**2
    P = sp.diag(a*b, (a*a+b*b)/2, (a*a+b*b)/2, a*b)/sp.pi**2
    U = sp.Matrix([[1, 1, 1, 1], [1, sp.I, -1, -sp.I], [1, -1, 1, -1], [1, -sp.I, -1, sp.I]])/2
    MM, PP = U.conjugate().T*M*U.conjugate(), U.T*P*U
    z = sp.Symbol('z')
    pol = lambda K: (K.H*K).charpoly(z).as_expr()
    av = sp.Rational(1, 2)+sp.sin(2*e)/(4*e)
    bv = 1-av
    limits_M = [sp.limit(value.subs({a: av, b: bv}), e, 0, dir='+') for value in M.diagonal()]
    limits_P = [sp.limit(value.subs({a: av, b: bv}), e, 0, dir='+') for value in P.diagonal()]
    return dict(unitary=matrix_res(U.H*U, sp.eye(4)),
                mirror_singular_polynomial=res(pol(MM), pol(M)),
                ordinary_singular_polynomial=res(pol(PP), pol(P)),
                entries_change=any(res(MM[i, j], M[i, j]) != 0 for i in range(4) for j in range(4)),
                M_limits=limits_M, P_limits=limits_P,
                selected_ratio_scaled=sp.limit(e*e*av/bv, e, 0, dir='+'),
                whole_norm_ratio_limit=sp.limit(2*av*av/(av*av+bv*bv), e, 0, dir='+'),
                unweighted_limits=[sp.limit(4*e*e*value.subs({a: av, b: bv}), e, 0, dir='+')
                                   for value in list(M.diagonal())+list(P.diagonal())])


def all_results():
    ac, wg, cc, fc, sc = action_control(), weighted_green(), canonical_control(), flat_control(), spectral_control()
    checks = dict(
        coupled_variations=ac['S_variations'] == [0]*10 and ac['Q_variation'] == ac['h_variation'] == 0,
        gauge_currents=ac['central_current'] == 0 and ac['D5_currents_at_zero'] == [0]*45,
        stationary_point=all(v == 0 for v in ac['stationary']),
        scalar_hessian_and_decoupling=ac['scalar_hessian'] == sp.zeros(20) and ac['mixed_hessian'] == sp.zeros(20, 8),
        source_feedback_required=ac['missing_feedback_witness'] != 0,
        weighted_green=wg['scalar_green'] == wg['weighted_overlap'] == 0 and wg['missing_weight_derivative'] != 0,
        canonical_scalar=cc['norm'] == cc['tube_weight_residual'] == 0 and cc['hessian'] == sp.zeros(2),
        exact_modes=fc['scalar_norm'] == fc['one_form_norm'] == sp.eye(4) and fc['eigen_residuals'] == [0]*4,
        all_overlap_entries=fc['M_formula'] == fc['P_formula'] == sp.zeros(4),
        full_interface=fc['interface'] == sp.zeros(4) and fc['axial_caps'] == [0]*16 and fc['omitted_interface'] != 0,
        basis_invariant=sc['unitary'] == sp.zeros(4) and sc['mirror_singular_polynomial'] == sc['ordinary_singular_polynomial'] == 0 and sc['entries_change'],
        selected_vs_whole=sc['selected_ratio_scaled'] == 3 and sc['whole_norm_ratio_limit'] == 2,
        measure_discriminator=fc['measure_M'] == fc['measure_P'] == sp.zeros(4) and sc['unweighted_limits'] == [0]*8)
    # Keep readable scalar results; the zero matrices/variations remain fully available to tests.
    return dict(checks=checks, all_checks_pass=all(checks.values()),
                action=ac, weighted=wg, canonical=cc, flat=fc, spectra=sc,
                scope='Added finite-width scalar action and complete flat eigenvalue-two control, not sourced hyperbolic selectivity or a quantum phase.')


def serial(v):
    if isinstance(v, dict):
        return {k: serial(w) for k, w in v.items()}
    if isinstance(v, sp.MatrixBase):
        return serial(v.tolist())
    if isinstance(v, (tuple, list)):
        return [serial(w) for w in v]
    if isinstance(v, sp.Basic):
        return str(v)
    return v


if __name__ == '__main__':
    result = all_results()
    print(json.dumps(serial(result), indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
