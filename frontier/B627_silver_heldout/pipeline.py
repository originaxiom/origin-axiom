"""
Generic numeric twisted-Alexander / Wada torsion pipeline for a 2-cusped-or-1-cusped
manifold given by a SnapPy deficiency-1 presentation <x1..xn | r1..r_{n-1}>, evaluated
at Sym^{2m} of the SL(2,C) discrete holonomy representation.

Strategy: high precision (mpmath) numerics, exact-degree interpolation (Lagrange) of
the numerator/denominator polynomials in t at integer nodes, exact polynomial division
(numerically, checked for near-zero remainder), monic normalization, then
tau_m = Delta_m'(1).
"""
import sympy as sp
import mpmath as mp


def alpha_map(gens, relators):
    """Integer homomorphism gens -> Z (the free part of H1), from the relator
    exponent-sum matrix; unique up to overall sign when H1 has free rank 1."""
    n = len(gens)
    idx = {g: i for i, g in enumerate(gens)}
    rows = []
    for r in relators:
        v = [0] * n
        for ch in r:
            if ch.islower():
                v[idx[ch]] += 1
            else:
                v[idx[ch.lower()]] -= 1
        rows.append(v)
    R = sp.Matrix(rows)
    ns = R.nullspace()
    assert len(ns) == 1, f"expected free rank 1, got nullspace dim {len(ns)}"
    v = ns[0]
    den = sp.lcm([sp.Rational(x).q for x in v])
    v = [sp.Rational(x) * den for x in v]
    g = sp.gcd(v)
    v = [int(x / g) for x in v]
    return dict(zip(gens, v))


def get_holonomy_hp(manifold_name, gens, dps=100):
    import snappy
    mp.mp.dps = dps + 20
    bits = int((dps + 20) * 3.33) + 32
    M = snappy.Manifold(manifold_name).high_precision()
    G = M.fundamental_group()

    def _s(x):
        return str(x).replace(' ', '').replace('E', 'e')

    def _mpc(z):
        return mp.mpc(_s(z.real()), _s(z.imag()))

    out = {}
    for g in gens:
        m = G.SL2C(g)
        out[g] = mp.matrix([[_mpc(m[0, 0]), _mpc(m[0, 1])],
                             [_mpc(m[1, 0]), _mpc(m[1, 1])]])
    return out, G


def sym_power_matrix(A, k):
    """Sym^k of a 2x2 matrix A, in the monomial basis x^k, x^{k-1}y, ..., y^k
    (basis vector i <-> x^{k-i} y^i), under (x,y) -> (a x + c y, b x + d y)
    i.e. matches column-vector action (x;y) -> A (x;y)."""
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    x, y = sp.symbols('x y')
    # substitute x -> a x + c y ; y -> b x + d y  (so that acting on the linear
    # functionals dual to the standard column-vector action is consistent)
    # We just need numeric coefficients; do it via direct multinomial expansion
    # using mpmath scalars but sympy for bookkeeping of exponents (fast: k<=23).
    from math import comb
    # (a*X + c*Y)^{k-i} * (b*X + d*Y)^{i} expanded in X^{k-j} Y^{j}
    # coefficient of X^{k-j} Y^j in (aX+cY)^{p}(bX+dY)^{q}, p=k-i, q=i, p+q=k
    out = mp.zeros(k + 1, k + 1)
    for i in range(k + 1):  # source basis index (column)
        p = k - i
        q = i
        # (aX+cY)^p = sum_{s=0}^p C(p,s) a^{p-s} c^s X^{p-s} Y^s
        # (bX+dY)^q = sum_{u=0}^q C(q,u) b^{q-u} d^u X^{q-u} Y^u
        coefs_p = [mp.mpf(comb(p, s)) * a ** (p - s) * c ** s for s in range(p + 1)]
        coefs_q = [mp.mpf(comb(q, u)) * b ** (q - u) * d ** u for u in range(q + 1)]
        # product: term X^{(p-s)+(q-u)} Y^{s+u}; total degree k; Y-exponent j = s+u
        row_of_j = [mp.mpc(0) for _ in range(k + 1)]
        for s in range(p + 1):
            for u in range(q + 1):
                j = s + u
                row_of_j[j] += coefs_p[s] * coefs_q[u]
        for j in range(k + 1):
            out[j, i] = row_of_j[j]
    return out


def fox_deriv_matrix(word, xj, acts, alpha, t, d):
    """Phi (x) t^alpha applied version of d(word)/d(xj), evaluated at complex t."""
    pref = mp.eye(d)
    total = mp.zeros(d, d)
    invcache = {}
    for ch in word:
        if ch.islower():
            x = ch
            if x == xj:
                total += pref
            pref = pref * (acts[x] * (t ** alpha[x]))
        else:
            x = ch.lower()
            if x not in invcache:
                invcache[x] = acts[x] ** -1
            invmat = invcache[x] * (t ** (-alpha[x]))
            if x == xj:
                total += pref * (-invmat)
            pref = pref * invmat
    return total


def word_exponent_range(word, xj, alpha):
    """Analytic (matrix-free) min/max t-exponent contributed to d(word)/d(xj)."""
    e = 0
    lo, hi = None, None
    for ch in word:
        if ch.islower():
            x = ch
            if x == xj:
                lo = e if lo is None else min(lo, e)
                hi = e if hi is None else max(hi, e)
            e += alpha[x]
        else:
            x = ch.lower()
            e -= alpha[x]
            if x == xj:
                lo = e if lo is None else min(lo, e)
                hi = e if hi is None else max(hi, e)
    return lo, hi


def block_numerator(t, relators, kept_gens, acts, alpha, d):
    """(n-1)*d x (n-1)*d block determinant of Fox derivatives."""
    n1 = len(relators)
    assert n1 == len(kept_gens)
    N = n1 * d
    Big = mp.zeros(N, N)
    for i, r in enumerate(relators):
        for j, xj in enumerate(kept_gens):
            Bij = fox_deriv_matrix(r, xj, acts, alpha, t, d)
            for p in range(d):
                for q in range(d):
                    Big[i * d + p, j * d + q] = Bij[p, q]
    return mp.det(Big)


def denominator(t, dropped_gen, acts, alpha, d):
    M = acts[dropped_gen] * (t ** alpha[dropped_gen]) - mp.eye(d)
    return mp.det(M)


def lagrange_interp(xs, ys):
    """Exact-ish high precision Lagrange interpolation -> list of coeffs low->high
    (mpmath complex), via sympy exact rational nodes + mpmath high precision sums."""
    n = len(xs)
    coeffs = [mp.mpc(0)] * n
    for i in range(n):
        # basis polynomial coefficients (low->high) via convolution
        num = [mp.mpc(1)]
        denom = mp.mpc(1)
        for j in range(n):
            if j == i:
                continue
            newnum = [mp.mpc(0)] * (len(num) + 1)
            for k, c in enumerate(num):
                newnum[k] += c * (-xs[j])
                newnum[k + 1] += c
            num = newnum
            denom *= (xs[i] - xs[j])
        w = ys[i] / denom
        for k in range(len(num)):
            coeffs[k] += w * num[k]
    return coeffs


def trim(coeffs, tol):
    c = coeffs[:]
    while len(c) > 1 and abs(c[-1]) < tol:
        c.pop()
    return c


def analytic_shift_and_degree(relators, kept_gens, alpha, d, cushion=2):
    """Rigorous (possibly loose) bound: shift so that t^shift * Num(t) is an
    honest polynomial, and its degree bound."""
    gmin = 0
    gmax = 0
    for r in relators:
        los, his = [], []
        for xj in kept_gens:
            lo, hi = word_exponent_range(r, xj, alpha)
            los.append(lo if lo is not None else 0)
            his.append(hi if hi is not None else 0)
        gmin += d * min(los)
        gmax += d * max(his)
    shift = max(0, -gmin) + cushion
    degree = shift + gmax + cushion
    return shift, degree


def poly_eval(coeffs, t):
    v = mp.mpc(0)
    for c in reversed(coeffs):
        v = v * t + c
    return v


def robust_shifted_numerator_poly(relators, kept_gens, acts, alpha, d, shift, degree,
                                   validate_extra=6, tol=None, log=None):
    """Evaluate t^shift * block_numerator(t) at enough integer points, fit an exact
    (degree) polynomial, and validate against extra held-out points."""
    npts_fit = degree + 1
    npts_total = npts_fit + validate_extra
    xs, ys = [], []
    p = 1
    while len(xs) < npts_total:
        t = mp.mpf(p)
        nv = block_numerator(t, relators, kept_gens, acts, alpha, d)
        ys.append(nv * (t ** shift))
        xs.append(t)
        p += 1
        if log and len(xs) % 5 == 0:
            log(f"    numerator eval pt {len(xs)}/{npts_total}")
    fit_xs, fit_ys = xs[:npts_fit], ys[:npts_fit]
    coeffs = lagrange_interp(fit_xs, fit_ys)
    if tol is None:
        tol = mp.mpf(10) ** (-(mp.mp.dps - 15))
    maxerr = mp.mpf(0)
    for t, y in zip(xs[npts_fit:], ys[npts_fit:]):
        pred = poly_eval(coeffs, t)
        relerr = abs(pred - y) / max(mp.mpf(1), abs(y))
        maxerr = max(maxerr, relerr)
    return coeffs, maxerr


def poly_divide(num_coeffs, den_coeffs, tol=None):
    """Exact (high precision) polynomial division, low->high coeff lists.
    Returns (quotient, remainder_max_abs)."""
    num = num_coeffs[:]
    den = den_coeffs[:]
    while den and abs(den[-1]) < mp.mpf('1e-40'):
        den.pop()
    dd = len(den) - 1
    dlead_inv = 1 / den[-1]
    rem = num[:]
    qlen = max(len(rem) - dd, 1)
    q = [mp.mpc(0)] * qlen
    remainder_max = mp.mpf(0)
    while len(rem) - 1 >= dd and any(abs(c) > mp.mpf('1e-30') for c in rem):
        if abs(rem[-1]) < mp.mpf('1e-30'):
            rem.pop()
            continue
        shift_ = len(rem) - 1 - dd
        c = rem[-1] * dlead_inv
        if shift_ < len(q):
            q[shift_] = c
        for j in range(len(den)):
            rem[shift_ + j] -= c * den[j]
        while rem and abs(rem[-1]) < mp.mpf('1e-25'):
            rem.pop()
    remainder_max = max([abs(c) for c in rem], default=mp.mpf(0))
    return q, remainder_max


def compute_tau(m_exp, gens, relators, kept_gens, dropped_gen, acts, alpha, dps,
                 log=None):
    """Full pipeline: build Sym^{2m} blocks, get shifted numerator poly, exact
    denominator poly, divide, monic-normalize, return (tau, degree, coeffs)."""
    mp.mp.dps = dps
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix(acts[g], k) for g in gens}
    shift, degbound = analytic_shift_and_degree(relators, kept_gens, alpha, d)
    if log:
        log(f"  m={m_exp} d={d}: shift={shift} degbound={degbound}")
    numP, maxerr = robust_shifted_numerator_poly(relators, kept_gens, sym_acts, alpha,
                                                  d, shift, degbound, log=log)
    if log:
        log(f"  m={m_exp}: numerator validation max relerr = {maxerr}")
    # denominator: det(t*Phi(dropped) - I), exact degree d, get via interpolation too
    dxs = [mp.mpf(i) for i in range(1, d + 3)]
    dys = [denominator(t, dropped_gen, sym_acts, alpha, d) for t in dxs]
    denP = lagrange_interp(dxs, dys)
    denP = trim(denP, mp.mpf(10) ** (-(dps - 20)))
    numP = trim(numP, mp.mpf(10) ** (-(dps - 20)))
    q, remmax = poly_divide(numP, denP)
    q = trim(q, mp.mpf(10) ** (-(dps - 20)))
    if log:
        log(f"  m={m_exp}: division remainder max = {remmax}; quotient degree {len(q)-1}")
    lead = q[-1]
    qn = [c / lead for c in q]
    tau = sum(i * c for i, c in enumerate(qn))
    return tau, qn, maxerr, remmax


def dft_nodes(N):
    return [mp.exp(2j * mp.pi * k / N) for k in range(N)]


def dft_coeffs_from_values(ys, N):
    """Inverse-DFT: recover low->high coeffs of degree<=N-1 poly from values at
    the N-th roots of unity t_k = exp(2 pi i k/N)."""
    coeffs = []
    for j in range(N):
        s = mp.mpc(0)
        for k in range(N):
            s += ys[k] * mp.exp(-2j * mp.pi * j * k / N)
        coeffs.append(s / N)
    return coeffs


def robust_shifted_numerator_poly_dft(relators, kept_gens, acts, alpha, d, shift,
                                       degree, extra=4, log=None):
    """Evaluate t^shift * block_numerator(t) at N=degree+1+extra roots of unity
    and recover the degree-(N-1) polynomial by inverse DFT; verify the top
    `extra` coefficients (which should be ~0, since true degree <= degree) are
    negligible -- that both certifies the degree bound and the fit."""
    N = degree + 1 + extra
    nodes = dft_nodes(N)
    ys = []
    for i, t in enumerate(nodes):
        nv = block_numerator(t, relators, kept_gens, acts, alpha, d)
        ys.append(nv * (t ** shift))
        if log and (i + 1) % 8 == 0:
            log(f"    numerator eval (dft) {i+1}/{N}")
    coeffs = dft_coeffs_from_values(ys, N)
    tail = coeffs[degree + 1:]
    tailmax = max([abs(c) for c in tail], default=mp.mpf(0))
    bodymax = max([abs(c) for c in coeffs[:degree + 1]], default=mp.mpf(1))
    return coeffs[:degree + 1], (tailmax / max(bodymax, mp.mpf(1)))


def denominator_poly_dft(dropped_gen, acts, alpha, d, extra=2):
    N = d + 1 + extra
    nodes = dft_nodes(N)
    ys = [denominator(t, dropped_gen, acts, alpha, d) for t in nodes]
    coeffs = dft_coeffs_from_values(ys, N)
    tail = coeffs[d + 1:]
    tailmax = max([abs(c) for c in tail], default=mp.mpf(0))
    return coeffs[:d + 1], tailmax


def compute_tau_dft(m_exp, gens, relators, kept_gens, dropped_gen, acts, alpha, dps,
                     log=None, extra=4):
    mp.mp.dps = dps
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix(acts[g], k) for g in gens}
    shift, degbound = analytic_shift_and_degree(relators, kept_gens, alpha, d)
    if log:
        log(f"  m={m_exp} d={d}: shift={shift} degbound={degbound}")
    numP, tailrel = robust_shifted_numerator_poly_dft(relators, kept_gens, sym_acts,
                                                        alpha, d, shift, degbound,
                                                        extra=extra, log=log)
    if log:
        log(f"  m={m_exp}: numerator dft tail/body ratio = {tailrel}")
    denP, dtail = denominator_poly_dft(dropped_gen, sym_acts, alpha, d, extra=extra)
    if log:
        log(f"  m={m_exp}: denominator dft tail = {dtail}")
    tol = mp.mpf(10) ** (-(dps - 25))
    numP = trim(numP, tol * max([abs(c) for c in numP], default=mp.mpf(1)))
    denP = trim(denP, tol * max([abs(c) for c in denP], default=mp.mpf(1)))
    q, remmax = poly_divide(numP, denP)
    q = trim(q, tol * max([abs(c) for c in q], default=mp.mpf(1)))
    if log:
        log(f"  m={m_exp}: division remainder max = {remmax}; quotient degree {len(q)-1}")
    lead = q[-1]
    qn = [c / lead for c in q]
    tau = sum(i * c for i, c in enumerate(qn))
    return tau, qn, tailrel, remmax


def compute_tau_direct(m_exp, gens, relators, kept_gens, dropped_gen, acts, alpha, dps,
                        log=None, extra=4):
    """Interpolate Q(t) = t^shift * Num(t) / Den(t) DIRECTLY (no separate poly
    division step) via inverse-DFT at roots of unity -- avoids precision loss
    from dividing two independently-interpolated, badly-conditioned polynomials."""
    mp.mp.dps = dps
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix(acts[g], k) for g in gens}
    shift, degbound = analytic_shift_and_degree(relators, kept_gens, alpha, d)
    qdeg = degbound - d
    N = qdeg + 1 + extra
    if log:
        log(f"  m={m_exp} d={d}: shift={shift} degbound={degbound} qdeg={qdeg} N={N}")
    nodes = dft_nodes(N)
    ys = []
    for i, t in enumerate(nodes):
        nv = block_numerator(t, relators, kept_gens, sym_acts, alpha, d)
        dv = denominator(t, dropped_gen, sym_acts, alpha, d)
        ys.append(nv * (t ** shift) / dv)
        if log and (i + 1) % 8 == 0:
            log(f"    Q eval (dft) {i+1}/{N}")
    coeffs = dft_coeffs_from_values(ys, N)
    tail = coeffs[qdeg + 1:]
    tailmax = max([abs(c) for c in tail], default=mp.mpf(0))
    body = coeffs[:qdeg + 1]
    bodymax = max([abs(c) for c in body], default=mp.mpf(1))
    if log:
        log(f"  m={m_exp}: Q tail/body ratio = {tailmax/max(bodymax, mp.mpf(1))}")
    tol = bodymax * mp.mpf(10) ** (-30)
    body = trim(body, tol)
    lead = body[-1]
    qn = [c / lead for c in body]
    tau = sum(i * c for i, c in enumerate(qn))
    return tau, qn, tailmax / max(bodymax, mp.mpf(1))


def compute_tau_intnodes(m_exp, gens, relators, kept_gens, dropped_gen, acts, alpha,
                          dps, log=None, extra=6, start=2):
    """Direct Q(t)=t^shift*Num(t)/Den(t) evaluation at REAL positive integer
    nodes (avoids proximity-to-pole blowups seen with roots-of-unity nodes),
    Lagrange-interpolated, with a held-out validation tail."""
    mp.mp.dps = dps
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix(acts[g], k) for g in gens}
    shift, degbound = analytic_shift_and_degree(relators, kept_gens, alpha, d)
    qdeg = degbound - d
    npts = qdeg + 1 + extra
    if log:
        log(f"  m={m_exp} d={d}: shift={shift} qdeg={qdeg} npts={npts}")
    xs, ys = [], []
    tv = start
    while len(xs) < npts:
        t = mp.mpf(tv)
        dv = denominator(t, dropped_gen, sym_acts, alpha, d)
        if abs(dv) > mp.mpf('1e-20'):
            nv = block_numerator(t, relators, kept_gens, sym_acts, alpha, d)
            xs.append(t)
            ys.append(nv * (t ** shift) / dv)
            if log and len(xs) % 8 == 0:
                log(f"    Q eval {len(xs)}/{npts}")
        tv += 1
    fit_xs, fit_ys = xs[:qdeg + 1], ys[:qdeg + 1]
    coeffs = lagrange_interp(fit_xs, fit_ys)
    maxrel = mp.mpf(0)
    for t, y in zip(xs[qdeg + 1:], ys[qdeg + 1:]):
        pred = poly_eval(coeffs, t)
        relerr = abs(pred - y) / max(mp.mpf(1), abs(y))
        maxrel = max(maxrel, relerr)
    bodymax = max([abs(c) for c in coeffs], default=mp.mpf(1))
    tol = bodymax * mp.mpf(10) ** (-30)
    coeffs = trim(coeffs, tol)
    lead = coeffs[-1]
    qn = [c / lead for c in coeffs]
    tau = sum(i * c for i, c in enumerate(qn))
    return tau, qn, maxrel


def probe_degree(relators, kept_gens, dropped_gen, acts, alpha, d, shift, dps=60,
                  tstart=10 ** 4, log=None):
    """Determine the EXACT degree of Q(t)=t^shift*Num(t)/Den(t) by large-t
    asymptotics (log|Q(t)|/log t -> integer degree). Robust against cases
    where the polynomial's true leading coefficient is much smaller than its
    peak (skew-palindromic torsion polys with tiny +-1 ends and huge middle
    coefficients) -- a magnitude-relative trim can wrongly amputate those."""
    old = mp.mp.dps
    mp.mp.dps = dps
    tv = mp.mpf(tstart)
    ests = []
    deg = None
    for _ in range(10):
        dv = denominator(tv, dropped_gen, acts, alpha, d)
        nv = block_numerator(tv, relators, kept_gens, acts, alpha, d)
        Q = nv * (tv ** shift) / dv
        est = mp.log(abs(Q)) / mp.log(tv)
        ests.append(est)
        if log:
            log(f"    probe_degree t={tv}: est={est}")
        if len(ests) >= 2 and abs(ests[-1] - ests[-2]) < mp.mpf('1e-4'):
            cand = int(mp.nint(ests[-1]))
            if abs(ests[-1] - cand) < mp.mpf('1e-3'):
                deg = cand
                break
        tv *= 10
    mp.mp.dps = old
    if deg is None:
        raise RuntimeError(f"probe_degree failed to converge: {ests}")
    return deg


def compute_tau_exact(m_exp, gens, relators, kept_gens, dropped_gen, acts, alpha, dps,
                       log=None, extra=6, probe_dps=80, probe_tstart=10 ** 4):
    """Full robust pipeline: (1) analytic shift bound, (2) EXACT degree via
    large-t asymptotic probing (immune to tiny-leading-coefficient traps),
    (3) Lagrange fit at real integer nodes with that exact degree + validation
    at held-out points, (4) monic-normalize (leading coeff is now trustworthy
    since the degree is exact, not a magnitude-trimmed guess), (5) tau=Q'(1)."""
    mp.mp.dps = dps
    k = 2 * m_exp
    d = k + 1
    sym_acts = {g: sym_power_matrix(acts[g], k) for g in gens}
    shift, _ = analytic_shift_and_degree(relators, kept_gens, alpha, d)
    qdeg = probe_degree(relators, kept_gens, dropped_gen, sym_acts, alpha, d, shift,
                         dps=probe_dps, tstart=probe_tstart, log=log)
    if log:
        log(f"  m={m_exp} d={d}: shift={shift} EXACT qdeg={qdeg}")
    npts = qdeg + 1 + extra
    xs, ys = [], []
    tv = 2
    while len(xs) < npts:
        t = mp.mpf(tv)
        dv = denominator(t, dropped_gen, sym_acts, alpha, d)
        if abs(dv) > mp.mpf('1e-20'):
            nv = block_numerator(t, relators, kept_gens, sym_acts, alpha, d)
            xs.append(t)
            ys.append(nv * (t ** shift) / dv)
            if log and len(xs) % 8 == 0:
                log(f"    Q eval {len(xs)}/{npts}")
        tv += 1
    fit_xs, fit_ys = xs[:qdeg + 1], ys[:qdeg + 1]
    coeffs = lagrange_interp(fit_xs, fit_ys)
    maxrel = mp.mpf(0)
    for t, y in zip(xs[qdeg + 1:], ys[qdeg + 1:]):
        pred = poly_eval(coeffs, t)
        relerr = abs(pred - y) / max(mp.mpf(1), abs(y))
        maxrel = max(maxrel, relerr)
    if log:
        log(f"  m={m_exp}: held-out maxrel = {maxrel}")
    lead = coeffs[-1]
    qn = [c / lead for c in coeffs]
    tau = sum(i * c for i, c in enumerate(qn))
    return tau, qn, maxrel, qdeg
