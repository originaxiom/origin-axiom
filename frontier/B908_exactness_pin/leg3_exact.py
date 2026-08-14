#!/usr/bin/env python3
"""B908 LEG 3 -- THE EXACT CERTIFICATE: I = -1 with no height bound.

Route (a), direct: the nine colorless atom lines are built EXACTLY in
characteristic 0, the banked invariant cubic is restricted to them, the six
couplings and I = prod(rows)/prod(cols) are computed exactly.

THE STRUCTURAL DISCOVERY THAT MAKES IT DIRECT
  The four pipeline torus generators on the 27 -- R8, R14, R16, R22 -- are
  RATIONAL matrices that COMMUTE EXACTLY over Q (verified here).  For every
  labeling, span{X1, Ym, W3, R14} = span{R8, R14, R16, R22} whenever g*a != 0
  (X1 = R8 + r R16, Ym = g R14 - a R16, W3 = b R16 - g R22), so the colorless
  atoms are joint eigenlines of ONE rational commuting family: the tower
  values (g, a, b) NEVER enter the atom lines.  charpoly(Mc) factors over Q as
    h_S (cubic, mult 1)   -- the three S-atoms, one Galois orbit, fields Q(r_j)
    h_A (sextic, mult 1)  -- the six non-S colorless atoms, ONE orbit of 6
    h_col (sextic, mult 3)-- the colored sector
  h_A has negative discriminant: the non-S pair in column j lives in
  K_j(beta_j), beta_j^2 = B(r_j), B in K = Q[rho]/mu13.  The hidden sign
  correlation across columns:  B = -3 w^2 with w in K (verified exactly), so
  beta_j = w(r_j) * tau with ONE global tau = sqrt(-3).  The whole colorless
  configuration is defined over Mbar = N(tau), N = splitting field of mu13
  (realized as the splitting algebra Q[rho1, rho2], dim 6), [Mbar:Q] = 12.
  Flipping tau swaps the two non-S rows (hence their equal couplings).

WHAT IS PROVEN (everything exact, no floats in any assertion; numerics are
only used to GUESS candidates which are then verified exactly):
  1. The four ops commute over Q and are exact derivations of the banked cubic.
  2. Nine explicit nonzero vectors over Mbar are joint eigenlines of the four
     ops (componentwise proportionality, all 351 coordinate pairs, all 4 ops).
  3. They reduce to the banked mod-p atom lines at ALL SEVEN full-tower primes
     under all 12 embeddings Mbar -> F_p (projective match of all 9 lines).
  4. Mod-p simplicity of the 9 colorless Mc-eigenvalues (rank 26) certifies
     the char-0 eigenlines are UNIQUE: any char-0 construction reducing to the
     banked states (the standing leg-1 assumption) has THESE atom lines.
  5. The restricted cubic's support is EXACTLY the two pencils in char 0
     (159/159 non-coupling multisets vanish IDENTICALLY in Mbar -- upgrades
     the zero-sum-certificate argument to an unconditional identity).
  6. v = P_R + P_C = 0 EXACTLY and I = P_R / P_C = -1 EXACTLY in Mbar.
     I is gauge-free (each atom appears once per pencil), so this is THE
     value; no height bound, no CRT, no reconstruction.

Bonus exact forms in this script's gauge: c_S = -disc(mu13) exactly, and the
two non-S row couplings are EQUAL integers (the 7-prime equality was real).

Environment: set SESSION_SCRATCH (dir containing leg3_base_cache.pkl, or the
B854 base is rebuilt inline) and SESSION_SCRATCH_RUN (handoff run dir with
cubic27.json, rep27.pkl).  State pickles leg3_state_<p>.pkl are read from the
arc directory (location of this file).  Output: leg3_exact_results.json.
"""
import itertools, json, os, pickle, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

ARC = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ['SESSION_SCRATCH']
RUN = os.environ['SESSION_SCRATCH_RUN']

PRIMES = [40123, 40639, 40693, 40897, 40903, 40927, 40939]
MU = [500716339200, -2075673600, -4769856, 2197]        # mu13, descending
CO = {8: 3, 14: 7, 16: 13, 22: 17}                      # Mc = 3 R8+7 R14+13 R16+17 R22

t00 = time.time()
RES = {'script': 'leg3_exact.py', 'route': 'a-direct',
       'mu13': MU, 'Mc_combination': {str(k): v for k, v in CO.items()},
       'primes': PRIMES, 'checks': {}}

def log(*a):
    print(f'[{time.time()-t00:7.1f}s]', *a, flush=True)

# ---------------------------------------------------------------- K = Q[rho]/mu13
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))

def kmul(x, y):
    c0 = x[0] * y[0]
    c1 = x[0] * y[1] + x[1] * y[0]
    c2 = x[0] * y[2] + x[1] * y[1] + x[2] * y[0]
    c3 = x[1] * y[2] + x[2] * y[1]
    c4 = x[2] * y[2]
    if c4:
        c0 += c4 * R4K[0]; c1 += c4 * R4K[1]; c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]; c1 += c3 * R3K[1]; c2 += c3 * R3K[2]
    return (c0, c1, c2)

def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])

def ksub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])

def kscale(x, s):
    return (x[0] * s, x[1] * s, x[2] * s)

def kis0(x):
    return not (x[0] or x[1] or x[2])

def kinv(x):
    cols = [kmul(x, KONE), kmul(x, (Fr(0), Fr(1), Fr(0))), kmul(x, (Fr(0), Fr(0), Fr(1)))]
    Aug = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)] for i in range(3)]
    for c in range(3):
        pr = next(r for r in range(c, 3) if Aug[r][c] != 0)
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        iv = Aug[c][c]
        Aug[c] = [e / iv for e in Aug[c]]
        for r in range(3):
            if r != c and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(4)]
    return (Aug[0][3], Aug[1][3], Aug[2][3])

def kred(x, r0, p):
    def rq(fr):
        return (fr.numerator % p) * pow(fr.denominator % p, -1, p) % p
    return (rq(x[0]) + rq(x[1]) * r0 + rq(x[2]) * r0 * r0) % p

# ---------------------------------------------------------------- N = splitting algebra
# basis {rho1^i rho2^j : i<=2, j<=1}; mu(rho1)=0; rho2^2 = -P rho2 - Q with
# P = b + rho1, Q = c + b rho1 + rho1^2 (b = B/A, c = C/A); r3 = -b - rho1 - rho2.
b_mu = Fr(MU[1], MU[0]); c_mu = Fr(MU[2], MU[0])
P_N = (b_mu, Fr(1), Fr(0))
Q_N = (c_mu, b_mu, Fr(1))
NZERO = (KZERO, KZERO)
NONE_ = (KONE, KZERO)

def nmul(a, b):
    a0, a1 = a; b0, b1 = b
    x00 = kmul(a0, b0); x11 = kmul(a1, b1)
    x01 = kadd(kmul(a0, b1), kmul(a1, b0))
    return (ksub(x00, kmul(x11, Q_N)), ksub(x01, kmul(x11, P_N)))

def nadd(a, b):
    return (kadd(a[0], b[0]), kadd(a[1], b[1]))

def nsub(a, b):
    return (ksub(a[0], b[0]), ksub(a[1], b[1]))

def nscale(a, s):
    return (kscale(a[0], s), kscale(a[1], s))

def nis0(a):
    return kis0(a[0]) and kis0(a[1])

def nred(a, r1, r2, p):
    return (kred(a[0], r1, p) + kred(a[1], r1, p) * r2) % p

def sigma(j, x):
    """the embedding K -> N, rho -> r_j (r1 = rho1, r2 = rho2, r3 = -b-rho1-rho2)."""
    c0, c1, c2 = x
    if j == 0:
        return ((c0, c1, c2), KZERO)
    if j == 1:
        return (ksub((c0, Fr(0), Fr(0)), kscale(Q_N, c2)),
                ksub((c1, Fr(0), Fr(0)), kscale(P_N, c2)))
    R3N = ((-b_mu, Fr(-1), Fr(0)), (Fr(-1), Fr(0), Fr(0)))
    acc = ((Fr(c0), Fr(0), Fr(0)), KZERO)
    acc = nadd(acc, nscale(R3N, c1))
    acc = nadd(acc, nscale(nmul(R3N, R3N), c2))
    return acc

# ---------------------------------------------------------------- Mbar = N[tau]/(tau^2+3)
class TR:
    def mul(self, a, b):
        X = nsub(nmul(a[0], b[0]), nscale(nmul(a[1], b[1]), Fr(3)))
        Y = nadd(nmul(a[0], b[1]), nmul(a[1], b[0]))
        return (X, Y)
    def add(self, a, b):
        return (nadd(a[0], b[0]), nadd(a[1], b[1]))
    def sub(self, a, b):
        return (nsub(a[0], b[0]), nsub(a[1], b[1]))
    def scale(self, a, s):
        return (nscale(a[0], s), nscale(a[1], s))
    def is0(self, a):
        return nis0(a[0]) and nis0(a[1])
    def red(self, a, r1, r2, tp, p):
        return (nred(a[0], r1, r2, p) + tp * nred(a[1], r1, r2, p)) % p

TZERO = (NZERO, NZERO)
TONE = (NONE_, NZERO)

# ---------------------------------------------------------------- Q linear algebra
def qkernel(M):
    m, n = len(M), len(M[0])
    A = [row[:] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if A[r][c] != 0), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = A[rr][c]
        A[rr] = [e / iv for e in A[rr]]
        for r in range(m):
            if r != rr and A[r][c]:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[rr][j] for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A[i][fc]
        ker.append(v)
    return ker

def qsolve_span(basis, vec):
    k, n = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n)]
    piv = []; rr = 0
    for c in range(k):
        pr = next((r for r in range(rr, n) if Aug[r][c] != 0), None)
        if pr is None:
            continue
        Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
        iv = Aug[rr][c]
        Aug[rr] = [e / iv for e in Aug[rr]]
        for r in range(n):
            if r != rr and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(k + 1)]
        piv.append(c); rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n):
        if sum(sol[j] * basis[j][i] for j in range(k)) != vec[i]:
            return None
    return sol

def matmulQ(X, Y):
    n = len(X); m = len(Y[0]); kk = len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(kk) if X[i][t]) for j in range(m)]
            for i in range(n)]

# ---------------------------------------------------------------- numeric-guided finders
# (numerics ONLY propose candidates; every acceptance is an exact identity)
import mpmath as mp

def _ratrec_real(x, maxden):
    f = mp.mpf(x)
    p0, q0, p1, q1 = mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0)
    r = f
    for _ in range(4000):
        a = mp.floor(r)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if q1 > maxden or r == a:
            break
        den = r - a
        if den == 0:
            break
        r = 1 / den
    if q1 > maxden:
        p1, q1 = p0, q0
    if q1 == 0:
        return None
    num, den = int(mp.nint(p1)), int(mp.nint(q1))
    if den < 0:
        num, den = -num, -den
    return Fr(num, den) if den else None

def _mu_roots_numeric(dps=400):
    mp.mp.dps = dps
    rts = mp.polyroots([mp.mpf(c) for c in MU], maxsteps=300, extraprec=400)
    return [mp.re(r) for r in rts]

def _kev_num(x, r):
    return (mp.mpf(x[0].numerator) / mp.mpf(x[0].denominator)
            + (mp.mpf(x[1].numerator) / mp.mpf(x[1].denominator)) * r
            + (mp.mpf(x[2].numerator) / mp.mpf(x[2].denominator)) * r * r)

def _interp_K(vals, mu_roots, maxden, hmax):
    M3 = mp.matrix(3, 3)
    for i in range(3):
        M3[i, 0] = 1; M3[i, 1] = mu_roots[i]; M3[i, 2] = mu_roots[i] ** 2
    try:
        sol = mp.lu_solve(M3, mp.matrix(vals))
    except Exception:
        return None
    cand = []
    for v in sol:
        r = _ratrec_real(v, maxden)
        if r is None or max(abs(r.numerator), r.denominator) > hmax:
            return None
        cand.append(r)
    return tuple(cand)

def root_in_K(h_coeffs, dps=400, hmax=10 ** 120):
    """the root in K of a rational poly with exactly one K-root; exact verify."""
    mu_roots = _mu_roots_numeric(dps)
    hh = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) for c in h_coeffs]
    h_roots = mp.polyroots(hh, maxsteps=400, extraprec=400)
    reals = [mp.re(r) for r in h_roots if abs(mp.im(r)) < mp.mpf(10) ** (-dps // 2)]
    maxden = mp.mpf(10) ** (dps // 3)
    for pick in itertools.permutations(range(len(reals)), 3):
        cand = _interp_K([reals[pick[j]] for j in range(3)], mu_roots, maxden, hmax)
        if cand is None:
            continue
        acc = (Fr(sp.Rational(h_coeffs[0]).p, sp.Rational(h_coeffs[0]).q), Fr(0), Fr(0))
        for c in h_coeffs[1:]:
            acc = kmul(acc, cand)
            acc = (acc[0] + Fr(sp.Rational(c).p, sp.Rational(c).q), acc[1], acc[2])
        if kis0(acc):
            return cand
    return None

def sqrt_in_K(target, dps=400, hmax=10 ** 120):
    """w in K with w^2 = target (a K-element), exact verify; None if not a square."""
    mu_roots = _mu_roots_numeric(dps)
    tv = [_kev_num(target, r) for r in mu_roots]
    if any(t < 0 for t in tv):
        return None
    sq = [mp.sqrt(t) for t in tv]
    maxden = mp.mpf(10) ** (dps // 3)
    for signs in itertools.product((1, -1), repeat=2):
        vals = [sq[0], signs[0] * sq[1], signs[1] * sq[2]]
        cand = _interp_K(vals, mu_roots, maxden, hmax)
        if cand is None:
            continue
        if kis0(ksub(kmul(cand, cand), target)):
            return cand
    return None

def sqrt_mod(a, p):
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r

# ---------------------------------------------------------------- base (B854)
def load_base():
    cache = os.path.join(SCRATCH, 'leg3_base_cache.pkl')
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    # isolated rebuild (see the exec-pitfall note in the arc): fresh namespace,
    # chdir to scratch so relative-path artifacts cannot clobber the arc.
    import contextlib, io
    src = open(os.path.join(ARC, '..', 'B854_centralizer_exact',
                            'e6_centralizer.py')).read()
    cwd = os.getcwd()
    nsdict = {'__file__': os.path.join(SCRATCH, 'b854_shadow.py')}
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, 'b854', 'exec'), nsdict)
    finally:
        os.chdir(cwd)
    D = pickle.load(open(os.path.join(RUN, 'rep27.pkl'), 'rb'))
    base = dict(INV=nsdict['INV'], ns=nsdict['ns'], REP=D['REP'],
                ADS={n: sp.Matrix(nsdict['ADS'][n]).tolist() for n in nsdict['ns']})
    with open(cache, 'wb') as f:
        pickle.dump(base, f)
    return base

def load_state(p):
    return pickle.load(open(os.path.join(ARC, f'leg3_state_{p}.pkl'), 'rb'))

# ================================================================ PHASE 1
def phase1():
    base = load_base()
    ns = base['ns']
    assert sorted(ns) == [8, 14, 16, 22]
    R27x = {}
    for n in ns:
        Mx = [[Fr(0)] * 27 for _ in range(27)]
        for k, c in enumerate(base['INV'][n]):
            cc = sp.Rational(c)
            if cc:
                Rk = base['REP'][k]
                fc = Fr(cc.p, cc.q)
                for a in range(27):
                    for b2 in range(27):
                        if Rk[a][b2]:
                            rr2 = sp.Rational(Rk[a][b2])
                            Mx[a][b2] += fc * Fr(rr2.p, rr2.q)
        R27x[n] = Mx
    for p in PRIMES[:2]:
        st = load_state(p)
        for n in ns:
            for a in range(27):
                for b2 in range(27):
                    x = R27x[n][a][b2]
                    assert (x.numerator % p) * pow(x.denominator % p, -1, p) % p \
                        == int(st['R27'][n][a][b2]) % p
    log('phase1: exact R27 matrices == pickled pipeline matrices mod', PRIMES[:2])
    for i in range(4):
        for j in range(i + 1, 4):
            assert matmulQ(R27x[ns[i]], R27x[ns[j]]) == matmulQ(R27x[ns[j]], R27x[ns[i]])
    log('phase1: all six commutators [Rm, Rn] = 0 EXACTLY over Q')
    RES['checks']['R27_match_pipeline_mod_2primes'] = True
    RES['checks']['four_ops_commute_exactly_over_Q'] = True
    CB = json.load(open(os.path.join(RUN, 'cubic27.json')))
    TRIP = [tuple(t) for t in CB['triples']]
    COEF = [int(sp.Rational(c)) for c in CB['coeffs']]
    assert len(TRIP) == 45 and set(COEF) <= {1, -1}
    T3 = {}
    for (a, b, c), cf in zip(TRIP, COEF):
        for pi in set(itertools.permutations((a, b, c))):
            T3[pi] = T3.get(pi, 0) + cf
    for n in ns:
        Mx = R27x[n]
        colnz = [[l for l in range(27) if Mx[l][i]] for i in range(27)]
        for i in range(27):
            for j in range(i, 27):
                for k in range(j, 27):
                    s = Fr(0)
                    for l in colnz[i]:
                        v = T3.get((l, j, k))
                        if v:
                            s += Mx[l][i] * v
                    for l in colnz[j]:
                        v = T3.get((i, l, k))
                        if v:
                            s += Mx[l][j] * v
                    for l in colnz[k]:
                        v = T3.get((i, j, l))
                        if v:
                            s += Mx[l][k] * v
                    assert s == 0
    log('phase1: the four exact ops are EXACT derivations of the banked 45-monomial cubic')
    RES['checks']['four_ops_exact_derivations_of_cubic'] = True
    return dict(ns=ns, R27x=R27x, TRIP=TRIP, COEF=COEF)

# ================================================================ PHASE 2
def phase2(P1):
    ns, R27x = P1['ns'], P1['R27x']
    Mc = [[sum(Fr(CO[n]) * R27x[n][i][j] for n in ns) for j in range(27)] for i in range(27)]
    # mod-p separation + simplicity certificates at two primes
    def rq(x, p):
        return (x.numerator % p) * pow(x.denominator % p, -1, p) % p
    for p in PRIMES[:2]:
        st = load_state(p)
        Mp = np.array([[rq(Mc[i][j], p) for j in range(27)] for i in range(27)], dtype=np.int64)
        lams = []
        for lbl, v in st['LINES']:
            w = (Mp @ v) % p
            nz = np.nonzero(v)[0][0]
            lv = int(w[nz]) * pow(int(v[nz]), -1, p) % p
            assert np.array_equal(w % p, (lv * v) % p)
            lams.append(lv)
        assert len(set(lams)) == 9
        def rankp(A):
            A = [[int(x) % p for x in row] for row in A.tolist()]
            rr = 0
            for c in range(27):
                pr = next((x for x in range(rr, 27) if A[x][c] % p), None)
                if pr is None:
                    continue
                A[rr], A[pr] = A[pr], A[rr]
                iv = pow(A[rr][c], -1, p)
                A[rr] = [(e * iv) % p for e in A[rr]]
                for x in range(27):
                    if x != rr and A[x][c]:
                        f = A[x][c]
                        A[x] = [(A[x][j] - f * A[rr][j]) % p for j in range(27)]
                rr += 1
            return rr
        for lv in lams:
            assert rankp((Mp - lv * np.eye(27, dtype=np.int64)) % p) == 26
    log('phase2: mod-p: atoms are Mc-eigenlines, 9 distinct SIMPLE eigenvalues (rank 26), 2 primes')
    RES['checks']['Mc_colorless_eigenvalues_simple_mod_2primes'] = True
    # exact charpoly + factorization
    x = sp.Symbol('x')
    cp = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                    Mc[i][j].denominator)).charpoly(x)
    fl = sp.factor_list(cp.as_expr())
    facs = sorted([(sp.degree(f, x), m, sp.Poly(f, x)) for f, m in fl[1]])
    assert [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)], facs
    h_S = [int(c) for c in facs[0][2].all_coeffs()]
    h_A = [int(c) for c in facs[1][2].all_coeffs()]
    log('phase2: charpoly(Mc) factors /Q as cubic*sextic*(sextic)^3')
    log('        h_S =', h_S)
    log('        h_A lc =', h_A[0])
    RES['h_S'] = [str(c) for c in h_S]
    RES['h_A'] = [str(c) for c in h_A]
    # rational blocks
    def poly_mat(coeffs):
        Acc = [[Fr(coeffs[0]) if i == j else Fr(0) for j in range(27)] for i in range(27)]
        for c in coeffs[1:]:
            Acc = matmulQ(Acc, Mc)
            for i in range(27):
                Acc[i][i] += Fr(c)
        return Acc
    W3 = qkernel(poly_mat(h_S))
    W6 = qkernel(poly_mat(h_A))
    assert len(W3) == 3 and len(W6) == 6
    log('phase2: rational blocks: dim ker h_S(Mc) = 3, dim ker h_A(Mc) = 6')
    Me = [[Fr(3) * R27x[8][i][j] + Fr(13) * R27x[16][i][j] for j in range(27)]
          for i in range(27)]
    Mo = [[Fr(7) * R27x[14][i][j] + Fr(17) * R27x[22][i][j] for j in range(27)]
          for i in range(27)]
    def restrict(Mbig, W):
        Crows = []
        for w in W:
            img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j]) for i in range(27)]
            sol = qsolve_span(W, img)
            assert sol is not None, 'block not invariant'
            Crows.append(sol)
        return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]
    C_S = restrict(Mc, W3)
    C_E = restrict(Me, W6)
    C_O = restrict(Mo, W6)
    C_A = restrict(Mc, W6)
    C_S_O = restrict(Mo, W3)
    assert all(C_S_O[i][j] == 0 for i in range(3) for j in range(3))
    log('phase2: W3, W6 invariant under Mc, Me, Mo; Mo|W3 = 0 (S-atoms kill R14, R22)')
    RES['checks']['Mo_annihilates_S_block'] = True
    cpS = sp.Matrix(3, 3, lambda i, j: sp.Rational(C_S[i][j].numerator,
                                                   C_S[i][j].denominator)).charpoly(x)
    assert [int(c) for c in sp.Poly(cpS.as_expr(), x).all_coeffs()] == h_S
    cpA = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_A[i][j].numerator,
                                                   C_A[i][j].denominator)).charpoly(x)
    assert sp.Poly(cpA.as_expr(), x).all_coeffs() == \
        [sp.Rational(c, h_A[0]) for c in h_A]
    cpE = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_E[i][j].numerator,
                                                   C_E[i][j].denominator)).charpoly(x)
    flE = sp.factor_list(cpE.as_expr())
    gs = [(f, m) for f, m in flE[1] if sp.degree(f, x) > 0]
    assert len(gs) == 1 and gs[0][1] == 2 and sp.degree(gs[0][0], x) == 3
    g_even = sp.Poly(gs[0][0], x).all_coeffs()
    g_even = [sp.Rational(c, g_even[0]) for c in g_even]
    cpO = sp.Matrix(6, 6, lambda i, j: sp.Rational(C_O[i][j].numerator,
                                                   C_O[i][j].denominator)).charpoly(x)
    co = sp.Poly(cpO.as_expr(), x).all_coeffs()
    assert co[1] == 0 and co[3] == 0 and co[5] == 0
    h_B = [co[0], co[2], co[4], co[6]]
    log('phase2: charpoly cross-checks pass; char(Me|W6) = g^2, char(Mo|W6) even in x')
    RES['checks']['charpoly_crosschecks'] = True
    return dict(W3=W3, W6=W6, C_S=C_S, C_E=C_E, C_O=C_O, g_even=g_even, h_B=h_B)

# ================================================================ PHASE 3
def phase3(P2):
    xS = root_in_K([sp.Rational(int(c)) for c in RES['h_S']])
    assert xS is not None
    alph = root_in_K(P2['g_even'])
    assert alph is not None
    Bk = root_in_K(P2['h_B'])
    assert Bk is not None
    wK = sqrt_in_K(kscale(Bk, Fr(-1, 3)))
    assert wK is not None
    assert kis0(ksub(kmul(wK, wK), kscale(Bk, Fr(-1, 3))))
    log('phase3: exact K-data (all verified by exact identities):')
    log('   x_S(rho)  =', list(xS), ' (h_S root: S-atom Mc-eigenvalue)')
    log('   alpha(rho)=', list(alph), ' (g root: nonS even eigenvalue; alpha = -x_S/2:',
        kis0(kadd(kscale(xS, Fr(1, 2)), alph)), ')')
    log('   B(rho)    =', list(Bk), ' (h_B root: beta^2)')
    log('   w(rho)    =', list(wK), ' with w^2 = -B/3 EXACT (tau = sqrt(-3) global)')
    RES['x_S'] = [str(c) for c in xS]
    RES['alpha'] = [str(c) for c in alph]
    RES['B'] = [str(c) for c in Bk]
    RES['w'] = [str(c) for c in wK]
    RES['checks']['alpha_equals_minus_half_xS'] = kis0(kadd(kscale(xS, Fr(1, 2)), alph))
    RES['checks']['B_equals_minus_3_w_squared'] = True
    return dict(xS=xS, alph=alph, Bk=Bk, wK=wK)

# ================================================================ PHASE 4
def phase4(P2, P3):
    xS, alph, Bk = P3['xS'], P3['alph'], P3['Bk']
    def kkernel(M):
        m, n = len(M), len(M[0])
        A = [row[:] for row in M]
        piv = []; rr = 0
        for c in range(n):
            pr = next((r for r in range(rr, m) if not kis0(A[r][c])), None)
            if pr is None:
                continue
            A[rr], A[pr] = A[pr], A[rr]
            iv = kinv(A[rr][c])
            A[rr] = [kmul(iv, e) for e in A[rr]]
            for r in range(m):
                if r != rr and not kis0(A[r][c]):
                    f = A[r][c]
                    A[r] = [ksub(A[r][j], kmul(f, A[rr][j])) for j in range(n)]
            piv.append(c); rr += 1
        ker = []
        for fc in [c for c in range(n) if c not in piv]:
            v = [KZERO] * n
            v[fc] = KONE
            for i, c in enumerate(piv):
                v[c] = kscale(A[i][fc], Fr(-1))
            ker.append(v)
        return ker
    CmK = [[ksub((Fr(P2['C_S'][i][j]), Fr(0), Fr(0)), xS if i == j else KZERO)
            for j in range(3)] for i in range(3)]
    kerS = kkernel(CmK)
    assert len(kerS) == 1
    vS3 = kerS[0]
    # F = K[beta]/(beta^2 - B): pairs (X, Y); kernel of [(C_E - alpha); (C_O - beta)]
    def fmul(a, b):
        return (kadd(kmul(a[0], b[0]), kmul(Bk, kmul(a[1], b[1]))),
                kadd(kmul(a[0], b[1]), kmul(a[1], b[0])))
    def fsub(a, b):
        return (ksub(a[0], b[0]), ksub(a[1], b[1]))
    def fis0(a):
        return kis0(a[0]) and kis0(a[1])
    def finv(a):
        den = ksub(kmul(a[0], a[0]), kmul(Bk, kmul(a[1], a[1])))
        di = kinv(den)
        return (kmul(a[0], di), kscale(kmul(a[1], di), Fr(-1)))
    rows = []
    for i in range(6):
        rows.append([(ksub((Fr(P2['C_E'][i][j]), Fr(0), Fr(0)),
                           alph if i == j else KZERO), KZERO) for j in range(6)])
    for i in range(6):
        rows.append([((Fr(P2['C_O'][i][j]), Fr(0), Fr(0)),
                      (Fr(-1), Fr(0), Fr(0)) if i == j else KZERO) for j in range(6)])
    m, n = len(rows), 6
    A = [row[:] for row in rows]
    piv = []; rr = 0
    for c in range(n):
        pr = next((r for r in range(rr, m) if not fis0(A[r][c])), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = finv(A[rr][c])
        A[rr] = [fmul(iv, e) for e in A[rr]]
        for r in range(m):
            if r != rr and not fis0(A[r][c]):
                f = A[r][c]
                A[r] = [fsub(A[r][j], fmul(f, A[rr][j])) for j in range(n)]
        piv.append(c); rr += 1
    FZ = (KZERO, KZERO)
    kerA = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [FZ] * n
        v[fc] = (KONE, KZERO)
        for i, c in enumerate(piv):
            v[c] = fsub(FZ, A[i][fc])
        kerA.append(v)
    assert len(kerA) == 1
    vA6 = kerA[0]
    log('phase4: eigen-kernels: S over K dim 1; nonS over K(beta) dim 1 '
        '(free coordinates exactly 1 -- the nonvanishing certificates)')
    RES['checks']['kernel_dims_1_1'] = True
    return dict(vS3=vS3, vA6=vA6)

# ================================================================ PHASE 5
def phase5(P2, P3, P4):
    wK = P3['wK']
    def lift(coords, W):
        out = []
        for i in range(27):
            acc = KZERO
            for a, cf in enumerate(coords):
                if W[a][i]:
                    acc = kadd(acc, kscale(cf, W[a][i]))
            out.append(acc)
        return out
    vS27 = lift(P4['vS3'], P2['W3'])
    u27 = lift([f[0] for f in P4['vA6']], P2['W6'])
    wt27 = lift([f[1] for f in P4['vA6']], P2['W6'])
    wodd27 = [kmul(wK, kt) for kt in wt27]      # beta = tau * w substitution
    def normalize(vec):
        L = 1
        for kt in vec:
            for x2 in kt:
                if x2:
                    d = x2.denominator
                    L = L * d // sp.gcd(L, d)
        vec2 = [kscale(kt, Fr(L)) for kt in vec]
        G = 0
        for kt in vec2:
            for x2 in kt:
                G = sp.gcd(G, x2.numerator)
        G = int(G)
        if G > 1:
            vec2 = [kscale(kt, Fr(1, G)) for kt in vec2]
        return vec2
    vS27 = normalize(vS27)
    uw = normalize(u27 + wodd27)
    u27, wodd27 = uw[:27], uw[27:]
    hS = max(max(abs(x2.numerator), x2.denominator) for kt in vS27 for x2 in kt)
    hA = max(max(abs(x2.numerator), x2.denominator) for kt in uw for x2 in kt)
    log(f'phase5: atom entry heights: S ~ 10^{len(str(hS))}, nonS ~ 10^{len(str(hA))} '
        f'(far beyond the 7-prime CRT bound ~ 10^16 -- why leg-2 CRT could not pin them)')
    RES['atom_heights_digits'] = {'S': len(str(hS)), 'nonS': len(str(hA))}
    atoms = {}
    for j in range(3):
        atoms[f'S{j}'] = [(sigma(j, kt), NZERO) for kt in vS27]
        for sgn, tag in ((1, 'p'), (-1, 'm')):
            atoms[f'A{j}{tag}'] = [(sigma(j, u27[i]),
                                    nscale(sigma(j, wodd27[i]), Fr(sgn)))
                                   for i in range(27)]
    return dict(atoms=atoms, vS27=vS27, u27=u27, wodd27=wodd27)

# ================================================================ PHASE 6
def phase6(P1, P5):
    T = TR()
    for name, vec in P5['atoms'].items():
        for n in P1['ns']:
            R = P1['R27x'][n]
            w = []
            for i in range(27):
                acc = TZERO
                for jj in range(27):
                    if R[i][jj] and not T.is0(vec[jj]):
                        acc = T.add(acc, T.scale(vec[jj], R[i][jj]))
                w.append(acc)
            for i in range(27):
                for k in range(i + 1, 27):
                    assert T.is0(T.sub(T.mul(w[i], vec[k]), T.mul(w[k], vec[i]))), \
                        (name, n, i, k)
    log('phase6: all 9 atoms are EXACT joint eigenlines of R8, R14, R16, R22 in Mbar '
        '(componentwise proportionality, all coordinate pairs)')
    RES['checks']['nine_atoms_joint_eigenlines_exact'] = True

# ================================================================ PHASE 7
def phase7(P5):
    T = TR()
    atoms = P5['atoms']
    names = sorted(atoms)
    embtab = {}
    for p in PRIMES:
        st = load_state(p)
        rs = [d[0] for d in st['DATA']]
        canon = {}
        for lbl, v in st['LINES']:
            nz = np.nonzero(v)[0][0]
            s = pow(int(v[nz]), -1, p)
            canon[tuple((s * v) % p)] = tuple(lbl)
        t3 = sqrt_mod(-3 % p, p)
        assert t3 is not None
        found = []
        for (i1, i2) in itertools.permutations(range(3), 2):
            for stau in (1, -1):
                tp = stau * t3 % p
                match = {}
                ok = True
                for nm in names:
                    vec = [T.red(c, rs[i1], rs[i2], tp, p) for c in atoms[nm]]
                    nz = next((i for i in range(27) if vec[i]), None)
                    if nz is None:
                        ok = False; break
                    s = pow(vec[nz], -1, p)
                    key = tuple(x2 * s % p for x2 in vec)
                    if key not in canon:
                        ok = False; break
                    match[nm] = canon[key]
                if ok and len(set(match.values())) == 9:
                    found.append(dict(rho1_slot=i1, rho2_slot=i2, stau=stau,
                                      match=match))
        assert len(found) == 12, f'{p}: {len(found)}'
        embtab[p] = found
        log(f'phase7: p={p}: 12/12 embeddings Mbar -> F_p match all 9 banked atom lines')
    RES['checks']['embeddings_match_all7primes'] = {str(p): len(embtab[p]) for p in PRIMES}
    return embtab

# ================================================================ PHASE 8
def phase8(P1, P5, P7):
    T = TR()
    TRIP, COEF = P1['TRIP'], P1['COEF']
    st = load_state(PRIMES[0])
    lbl2idx = {tuple(l): i for i, (l, v) in enumerate(st['LINES'])}
    match = P7[PRIMES[0]][0]['match']
    name_by_idx = {lbl2idx[lbl]: nm for nm, lbl in match.items()}
    order = [name_by_idx[i] for i in range(9)]
    RES['atom_identification_ref40123'] = {
        str(i): [order[i], list(match[order[i]])] for i in range(9)}
    log('phase8: atom <-> banked index:',
        {i: order[i] for i in range(9)})
    vecs = [P5['atoms'][nm] for nm in order]
    def cubT(u, v, w):
        s = TZERO
        for (a, b, c), cf in zip(TRIP, COEF):
            t = TZERO
            for x2, y2, z2 in itertools.permutations((a, b, c)):
                if not (T.is0(u[x2]) or T.is0(v[y2]) or T.is0(w[z2])):
                    t = T.add(t, T.mul(T.mul(u[x2], v[y2]), w[z2]))
            if not T.is0(t):
                s = T.add(s, T.scale(t, Fr(cf)))
        return s
    vals = {}
    nz_support = []
    for i in range(9):
        for j in range(i, 9):
            for k in range(j, 9):
                val = cubT(vecs[i], vecs[j], vecs[k])
                if not T.is0(val):
                    nz_support.append((i, j, k))
                    vals[(i, j, k)] = val
    T_tris = sorted(tuple(t) for t, c in st['T'])
    support_ok = sorted(nz_support) == T_tris
    log(f'phase8: EXACT char-0 support = {sorted(nz_support)}')
    log(f'phase8: support == the banked two pencils: {support_ok} '
        f'(159/159 non-couplings vanish IDENTICALLY in Mbar)')
    assert support_ok
    RES['checks']['char0_support_exactly_two_pencils'] = True
    RES['support'] = [list(t) for t in sorted(nz_support)]
    side = st['side']
    tri_by_a = {a: tuple(sorted(st['T'][a][0])) for a in range(6)}
    rows = [tri_by_a[a] for a in range(6) if side[a] == 0]
    cols = [tri_by_a[a] for a in range(6) if side[a] == 1]
    SA = tuple(sorted(i for i in range(9) if 'S' in match[order[i]]))
    assert SA in rows
    P_R = TONE
    for t in rows:
        P_R = T.mul(P_R, vals[t])
    P_C = TONE
    for t in cols:
        P_C = T.mul(P_C, vals[t])
    v_is_0 = T.is0(T.add(P_R, P_C))
    def as_rational(tel):
        X, Y = tel
        if not nis0(Y):
            return None
        XK, XR = X
        if not kis0(XR) or XK[1] or XK[2]:
            return None
        return XK[0]
    pr_q = as_rational(P_R); pc_q = as_rational(P_C)
    I_val = as_rational(T.scale(P_R, 1 / pc_q)) if pc_q else None
    log(f'phase8: v = P_R + P_C == 0 EXACTLY in Mbar: {v_is_0}')
    log(f'phase8: P_R = {pr_q}')
    log(f'phase8: P_C = {pc_q}')
    log(f'phase8: I = P_R / P_C = {I_val}   <<< THE VERDICT (gauge-free)')
    disc_mu = sp.Poly([int(c) for c in MU], sp.Symbol('x')).discriminant()
    cS_val = as_rational(vals[SA])
    crow_vals = [as_rational(vals[t]) for t in rows if t != SA]
    log(f'phase8: in this gauge  c_S = {cS_val}  ( == -disc(mu13): '
        f'{cS_val == -disc_mu} )')
    log(f'phase8: non-S rows EQUAL exact integers: '
        f'{crow_vals[0] == crow_vals[1]} ({crow_vals[0]})')
    ccol_desc = {}
    for t in cols:
        X, Y = vals[t]
        assert nis0(Y), 'column coupling has tau part'
        ccol_desc[str(t)] = [str(c) for c in X[0]] + [str(c) for c in X[1]]
    RES.update(rows=[list(t) for t in rows], cols=[list(t) for t in cols],
               v_is_0=v_is_0, P_R=str(pr_q), P_C=str(pc_q), I=str(I_val),
               c_S=str(cS_val), c_S_equals_minus_disc_mu13=bool(cS_val == -disc_mu),
               c_row_nonS=[str(crow_vals[0]), str(crow_vals[1])],
               c_row_nonS_equal=bool(crow_vals[0] == crow_vals[1]),
               c_cols_K_conjugates_coeffs=ccol_desc)
    RES['checks']['v_is_0_exactly'] = v_is_0
    RES['checks']['I_is_minus_1_exactly'] = (str(I_val) == '-1')
    return dict(I=I_val, v_is_0=v_is_0)

# ================================================================ main
if __name__ == '__main__':
    P1 = phase1()
    P2 = phase2(P1)
    P3 = phase3(P2)
    P4 = phase4(P2, P3)
    P5 = phase5(P2, P3, P4)
    phase6(P1, P5)
    P7 = phase7(P5)
    P8 = phase8(P1, P5, P7)
    RES['runtime_seconds'] = round(time.time() - t00, 1)
    RES['verdict'] = ('I = -1 EXACTLY (v = P_R + P_C = 0 exactly) over the char-0 '
                      'field Mbar = N(sqrt(-3)); no height bound; identification '
                      'with the banked pipeline pinned at all 7 primes x 12 '
                      'embeddings + mod-p simplicity.')
    with open(os.path.join(ARC, 'leg3_exact_results.json'), 'w') as f:
        json.dump(RES, f, indent=1)
    log('wrote leg3_exact_results.json')
    log('VERDICT:', RES['verdict'])
