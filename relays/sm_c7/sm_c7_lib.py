"""SM-C7's instruments: Eisenstein series on the thread's closed geodesic, and twisted cone zeta sums.

Conventions (step 0 of the card; every one is checked in calibrate.py on matrices outside B1737's population):
  M = [[a, b], [c, d]] acts on the fibre's H1 by v -> M v (columns); a character is chi(v) = e((i v0 + j v1)/N), fixed:
  (i, j) M = (i, j) mod N.  The lattice point (m, n) of an Eisenstein series is v = (v0, v1); the series' modulus z
  is acted on by gamma = M^T, z -> (a z + c)/(b z + d), whose fixed points beta, beta' solve b z^2 + (d - a) z - c = 0.
  L1(v) = v0 beta + v1, L2(v) = v0 beta' + v1, Q(v) = L1 L2/(beta - beta') = (b v1^2 + (a - d) v0 v1 - c v0^2)/sqrt(D)
  up to sign.  The geodesic is z(t) = (beta i e^t + beta')/(i e^t + 1), t real, ds = dt; one period is t in [t0, t0 + l],
  l = 2 log|lambda|.  e(x) = exp(2 pi i x).
Nothing here reads a measured value."""
import math, cmath, itertools
import numpy as np
from scipy.special import kv
import mpmath as mp
from fractions import Fraction as Fr


def frac(x):
    """fractional part, exact for Fractions and ints"""
    if isinstance(x, (Fr, int)):
        return float(Fr(x) % 1)
    return float(x) % 1.0

TAU = 2 * math.pi


def e(x):
    return np.exp(2j * math.pi * np.asarray(x))


def B2(x):
    return x * x - x + 1.0 / 6.0


def bern(n, x):
    return float(mp.bernpoly(n, x))


# ---------------------------------------------------------------------------- the geodesic
class Geodesic:
    def __init__(self, M):
        (a, b), (c, d) = M
        self.M = [[int(a), int(b)], [int(c), int(d)]]
        self.a, self.b, self.c, self.d = a, b, c, d
        self.tr = a + d
        self.D = (a + d) ** 2 - 4
        r = math.sqrt(self.D)
        self.beta = ((a - d) + r) / (2 * b)
        self.betap = ((a - d) - r) / (2 * b)
        if self.beta < self.betap:                 # beta > beta', so z(t) lies in the upper half-plane
            self.beta, self.betap = self.betap, self.beta
        lam = (abs(a + d) + r) / 2
        self.ell = 2 * math.log(lam)
        # direction: gamma z(t) = z(t + sigma ell)
        z0 = self.z(0.0)
        gz = self.mob(z0)
        self.sigma = 1 if abs(gz - self.z(self.ell)) < abs(gz - self.z(-self.ell)) else -1
        assert min(abs(gz - self.z(self.ell)), abs(gz - self.z(-self.ell))) < 1e-9

    def z(self, t):
        w = 1j * np.exp(t)
        return (self.beta * w + self.betap) / (w + 1)

    def dz(self, t):
        w = 1j * np.exp(t)
        return (self.beta - self.betap) * w / (w + 1) ** 2

    def mob(self, z):          # gamma = M^T
        return (self.a * z + self.c) / (self.b * z + self.d)

    def L1(self, v):
        return v[0] * self.beta + v[1]

    def L2(self, v):
        return v[0] * self.betap + v[1]

    def Q(self, v):
        return self.L1(v) * self.L2(v) / (self.beta - self.betap)

    def nodes(self, n, t0=None):
        """n equally spaced nodes over one period (the integrands are periodic, so the trapezoid rule is spectral)"""
        if t0 is None: t0 = -self.ell / 2
        t = t0 + self.ell * np.arange(n) / n
        return t, self.ell / n


# ---------------------------------------------------------------------------- reduction to the fundamental domain
def reduce(z):
    """returns (w, g) with w = g z in the standard fundamental domain, g in SL(2, Z) as [[p, q], [r, s]]"""
    g = np.array([[1, 0], [0, 1]], dtype=object)
    w = complex(z)
    for _ in range(10000):
        n = math.floor(w.real + 0.5)
        if n:
            w -= n; g = np.array([[1, -n], [0, 1]], dtype=object).dot(g)
        if abs(w) < 1 - 1e-15:
            w = -1 / w; g = np.array([[0, -1], [1, 0]], dtype=object).dot(g)
        else:
            break
    return w, g


def ginv(g):
    (p, q), (r, s) = g
    return np.array([[s, -q], [-r, p]], dtype=object)


# ---------------------------------------------------------------------------- weight 0, v-twisted: E_c(z, s)
def E_fourier(c, z, s, mmax=None, kmax=None, tol=1e-17):
    """E_c(z, s) = sum'_{(m,n)} e(c1 m + c2 n) y^s |m z + n|^{-2s}, integer s >= 1, by its Fourier expansion"""
    c1, c2 = frac(c[0]), frac(c[1])
    x, y = z.real, z.imag
    S0 = (-1) ** (s + 1) * (TAU) ** (2 * s) * bern(2 * s, c2) / math.factorial(2 * s)
    tot = y ** s * S0
    if mmax is None:
        mmax = int(40 / (TAU * y * max(min(c2, 1 - c2), 1e-9 if c2 else 1.0))) + 2 if c2 else int(40 / (TAU * y)) + 2
        mmax = min(mmax, 4000)
    g = math.gamma(s)
    for m in range(1, mmax + 1):
        Y = m * y
        for sgnm in (1, -1):
            mm = sgnm * m
            acc = 0.0 + 0.0j
            kk = int(40 / (TAU * Y)) + 3
            xis = np.arange(-kk, kk + 1) - c2
            xis = xis[np.abs(xis) > 1e-15]
            acc += np.sum(e(xis * mm * x) * 2 * math.pi ** s * np.abs(xis) ** (s - 0.5) * Y ** (0.5 - s)
                          * kv(s - 0.5, TAU * np.abs(xis) * Y) / g)
            tot += y ** s * e(c1 * mm) * acc
    if c2 == 0.0:      # the xi = 0 modes, summed over m in closed form: sum_{m != 0} e(c1 m) |m|^{1-2s}
        if c1 == 0.0:
            lsum = 2 * float(mp.zeta(2 * s - 1))
        else:
            lsum = 2 * float(mp.re(mp.polylog(2 * s - 1, mp.exp(2j * mp.pi * c1))))
        tot += y ** (1 - s) * math.sqrt(math.pi) * math.gamma(s - 0.5) / g * lsum
    return complex(tot)


def kron(c, z, rmax=None):
    """the Kronecker-limit function E_c(z, 1) = 2 pi^2 y B2(b) - 2 pi log|prod_r (1 - e(c1) q^{r+1-b})(1 - e(-c1) q^{r+b})|,
    b = {c2}, c not in Z^2 (the second limit formula; derived in the page and checked against E_fourier)"""
    c1, b = frac(c[0]), frac(c[1])
    assert (c1, b) != (0.0, 0.0)
    y = z.imag
    q = cmath.exp(2j * math.pi * z)
    if rmax is None: rmax = int(40 / (TAU * y)) + 3
    r = np.arange(rmax)
    ec = cmath.exp(2j * math.pi * c1)
    t1 = 1 - ec * np.exp(2j * math.pi * z * (r + 1 - b))
    t2 = 1 - np.conj(ec) * np.exp(2j * math.pi * z * (r + b))
    return 2 * math.pi ** 2 * y * B2(b) - 2 * math.pi * float(np.sum(np.log(np.abs(t1))) + np.sum(np.log(np.abs(t2))))


def at_reduced(c, z, fn):
    """E_c(z) = E_{c'}(w), w = g z, c'^T = g c^T (weight 0)"""
    w, g = reduce(z)
    cc = (g[0][0] * c[0] + g[0][1] * c[1], g[1][0] * c[0] + g[1][1] * c[1])
    return fn(cc, w)


# ---------------------------------------------------------------------------- weight 2
def G_v(c, z):
    """v-twisted weight 2: G_c(z) = sum'_{(m,n)} e(c1 m + c2 n) (m z + n)^{-2} (m outer; c != 0, holomorphic)"""
    c1, c2 = frac(c[0]), frac(c[1])
    assert (c1, c2) != (0.0, 0.0)
    tot = 2 * math.pi ** 2 * B2(c2)
    y = z.imag
    mmax = int(40 / (TAU * y * max(min(c2, 1 - c2) if c2 else 1.0, 1e-9))) + 3
    mmax = min(mmax, 4000)
    for m in range(1, mmax + 1):
        kk = int(40 / (TAU * m * y)) + 3
        for sgn, cc1 in ((1, c1), (-1, -c1)):
            b = c2 if sgn == 1 else -c2
            xis = np.arange(-kk, kk + 2) - b
            xis = xis[xis > 1e-15]
            tot += -4 * math.pi ** 2 * e(cc1 * m) * np.sum(xis * e(xis * m * z))
    return complex(tot)


def G_u(u, z):
    """u-shifted weight 2, Hecke's limit: G^(u)*(z) = sum_{m in u1+Z} sum_{n in u2+Z} (m z + n)^{-2} - pi/y"""
    u1, u2 = frac(u[0]), frac(u[1])
    y = z.imag
    tot = -math.pi / y
    if u1 == 0.0:
        tot += (math.pi ** 2 / 3) if u2 == 0.0 else float(mp.zeta(2, u2) + mp.zeta(2, 1 - u2))
    M = int(40 / (TAU * y)) + 3
    ms = [m for m in (np.arange(-M, M + 1) + u1) if abs(m) > 1e-15]
    for m in ms:
        R = int(40 / (TAU * abs(m) * y)) + 3
        r = np.arange(1, R + 1)
        if m > 0:
            tot += -4 * math.pi ** 2 * np.sum(r * e(r * (m * z + u2)))
        else:
            tot += -4 * math.pi ** 2 * np.sum(r * e(r * (abs(m) * z - u2)))
    return complex(tot)


def w2_reduced(idx, z, fn, kind):
    """weight 2 at a reduced point: F(z) = F'(w) (gamma' w + delta')^2 with (gamma', delta') the bottom row of g^{-1};
    v-twist: c'^T = g c^T; u-shift: u' = u g^{-1}"""
    w, g = reduce(z)
    gi = ginv(g)
    if kind == "v":
        cc = (g[0][0] * idx[0] + g[0][1] * idx[1], g[1][0] * idx[0] + g[1][1] * idx[1])
    else:
        cc = (idx[0] * gi[0][0] + idx[1] * gi[1][0], idx[0] * gi[0][1] + idx[1] * gi[1][1])
    jj = float(gi[1][0]) * w + float(gi[1][1])
    return fn(cc, w) * jj ** 2


# ---------------------------------------------------------------------------- twisted cone sums
def parallelogram(w, w2):
    det = w[0] * w2[1] - w[1] * w2[0]
    xs = [0, w[0], w2[0], w[0] + w2[0]]; ys = [0, w[1], w2[1], w[1] + w2[1]]
    from fractions import Fraction as Fr
    out = []
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            t1 = Fr(x * w2[1] - y * w2[0], det); t2 = Fr(w[0] * y - w[1] * x, det)
            if 0 < t1 <= 1 and 0 <= t2 < 1: out.append((x, y))
    assert len(out) == abs(det)
    return out


def stirling2(n, k):
    return int(mp.stirling2(n, k))


_T = {}


def Tj(x, J):
    """T_j(x) = sum_{k>=0} k^j x^k (Abel), j = 0..J, for |x| = 1, x != 1"""
    key = (round(x.real, 15), round(x.imag, 15), J)
    if key in _T: return _T[key]
    X = mp.mpc(x)
    wv = X / (1 - X)
    out = []
    for n in range(J + 1):
        li = sum(mp.factorial(k) * stirling2(n + 1, k + 1) * wv ** (k + 1) for k in range(n + 1))
        out.append(complex(li + (1 if n == 0 else 0)))
    _T[key] = np.array(out)
    return _T[key]


def binoms(s, J):
    """binom(-s, n), n = 0..J"""
    out = np.empty(J + 1, dtype=complex); out[0] = 1
    for n in range(1, J + 1):
        out[n] = out[n - 1] * (-s - n + 1) / n
    return out


def taylor1(al, a1, s, J, bn):
    """coefficients of t^n in (al + a1 t)^{-s}, vectorised over arrays al (shape [...]): returns [..., J+1]"""
    al = np.asarray(al, dtype=float)
    r = (a1 / al)[..., None] ** np.arange(J + 1)
    return bn * r * np.exp(-s * np.log(al))[..., None]


def conv_last(A, B, J):
    out = np.zeros(np.broadcast_shapes(A.shape, B.shape), dtype=complex)
    for n in range(J + 1):
        out[..., n] = np.sum(A[..., :n + 1] * B[..., n::-1], axis=-1)
    return out


def taylor2(al, a1, a2, s, J, bn):
    """C[i, j]: coefficient of t^i u^j in (al + a1 t + a2 u)^{-s}, i + j <= J"""
    C = np.zeros((J + 1, J + 1), dtype=complex)
    base = np.exp(-s * math.log(al))
    for n in range(J + 1):
        for i in range(n + 1):
            C[i, n - i] = bn[n] * base * math.comb(n, i) * (a1 / al) ** i * (a2 / al) ** (n - i)
    return C


def conv2(A, B, J):
    out = np.zeros((J + 1, J + 1), dtype=complex)
    for i1 in range(J + 1):
        for j1 in range(J + 1 - i1):
            a = A[i1, j1]
            if a == 0: continue
            for i2 in range(J + 1 - i1):
                jmax = J + 1 - i1 - i2 - j1
                if jmax <= 0: continue
                out[i1 + i2, j1:j1 + jmax] += a * B[i2, :jmax]
    return out


def cone_sum(geo, w, G, chi, s, K=120, J=36):
    """sum over v in the half-open cone {a w + b G w : a > 0, b >= 0} of chi(v) |Q(v)|^{-s}: the cone mod <G>.
    chi is a function of an integer vector; x = chi(w) must not be 1.  Twisted Euler-Maclaurin tails (Abel)."""
    w = tuple(int(t) for t in w)
    w2 = tuple(int(t) for t in np.array(G, dtype=object).dot(np.array(w, dtype=object)))
    x = complex(chi(w))
    assert abs(x - 1) > 1e-9 and abs(complex(chi(w2)) - x) < 1e-9
    A1, A2 = abs(geo.L1(w)), abs(geo.L1(w2)); B1, B2_ = abs(geo.L2(w)), abs(geo.L2(w2))
    scale = abs(geo.beta - geo.betap) ** s
    T = Tj(x, J)
    bn = binoms(s, J)
    k = np.arange(K)
    xk = x ** k
    tot = 0.0 + 0.0j
    for p in parallelogram(w, w2):
        A0, B0 = abs(geo.L1(p)), abs(geo.L2(p))
        Ak = A0 + k[:, None] * A1 + k[None, :] * A2
        Bk = B0 + k[:, None] * B1 + k[None, :] * B2_
        direct = np.sum(xk[:, None] * xk[None, :] * np.exp(-s * (np.log(Ak) + np.log(Bk))))
        # k >= K, l < K
        ca = taylor1(A0 + K * A1 + k * A2, A1, s, J, bn); cb = taylor1(B0 + K * B1 + k * B2_, B1, s, J, bn)
        tail_k = x ** K * np.sum(xk * (conv_last(ca, cb, J) @ T))
        # l >= K, all k
        ca = taylor1(A0 + k * A1 + K * A2, A2, s, J, bn); cb = taylor1(B0 + k * B1 + K * B2_, B2_, s, J, bn)
        hco = np.sum(xk[:, None] * conv_last(ca, cb, J), axis=0)
        CAB = conv2(taylor2(A0 + K * A1 + K * A2, A1, A2, s, J, bn), taylor2(B0 + K * B1 + K * B2_, B1, B2_, s, J, bn), J)
        for jdx in range(J + 1):
            hco[jdx] += x ** K * np.sum(CAB[:J + 1 - jdx, jdx] * T[:J + 1 - jdx])
        tail_l = x ** K * np.sum(hco * T)
        tot += complex(chi(p)) * (direct + tail_k + tail_l)
    return tot * scale


# ---------------------------------------------------------------------------- the total twisted zeta and Hecke's side
def char(i, j, N):
    return lambda v: complex(cmath.exp(2j * math.pi * ((i * v[0] + j * v[1]) % N) / N))


def find_w(geo, chi, same, avoid_one=True, which=0):
    """a primitive vector in the open cone L1 > 0 and L2 > 0 (same) or L1 > 0 > L2 (opposite) with chi(w) != 1"""
    found = []
    for r in range(1, 40):
        for w in itertools.product(range(-r, r + 1), repeat=2):
            if max(abs(w[0]), abs(w[1])) != r or math.gcd(*w) != 1: continue
            a1, a2 = geo.L1(w), geo.L2(w)
            ok = (a1 > 0 and a2 > 0) if same else (a1 > 0 and a2 < 0)
            if ok and (not avoid_one or abs(chi(w) - 1) > 1e-9):
                found.append(w)
        if len(found) > which: return found[which]
    raise ValueError("no w")


def Z_total(geo, i, j, N, s, K=120, J=36, which=0):
    """sum over v in (Z^2 - 0)/<M> of chi(v) |Q(v)|^{-s}, the four cones (two when tr M < 0)"""
    chi = char(i, j, N); chib = char(-i, -j, N)
    M = geo.M
    if geo.tr > 0:
        tot = 0
        for same in (True, False):
            w = find_w(geo, chi, same, which=which)
            tot += cone_sum(geo, w, M, chi, s, K, J) + cone_sum(geo, w, M, chib, s, K, J)
        return tot
    M2 = np.array(M, dtype=object).dot(np.array(M, dtype=object)).tolist()
    tot = 0
    for same in (True, False):
        w = find_w(geo, chi, same, which=which)
        tot += cone_sum(geo, w, M2, chi, s, K, J)
    return tot


def H(s):
    return 2.0 ** (-s) * math.sqrt(math.pi) * math.gamma(s / 2) / math.gamma((s + 1) / 2)


def hecke_side(geo, c, s, n=64):
    """the integral of E_c(z, s) ds over one period of the geodesic (trapezoid; periodic integrand)"""
    t, h = geo.nodes(n)
    fn = (lambda cc, w: kron(cc, w)) if s == 1 else (lambda cc, w: E_fourier(cc, w, s))
    return h * sum(at_reduced(c, geo.z(tt), fn) for tt in t)


def period(geo, idx, kind, n=64, reverse=False):
    """the integral of G(z) dz from z0 to gamma z0 along the geodesic (reverse: from gamma z0 to z0); G the v-twisted
    (kind 'v') or u-shifted (kind 'u') weight-2 series, evaluated at reduced points"""
    t, h = geo.nodes(n)
    fn = G_v if kind == "v" else G_u
    sgn = geo.sigma * (-1 if reverse else 1)
    return sgn * h * sum(w2_reduced(idx, geo.z(tt), fn, kind) * geo.dz(tt) for tt in t)


def Z0_b1737(geo, i, j, N):
    """B1737's Z(0, chi): the positive cone mod <gen>, gen = M (tr > 0) or M^2 halved (tr < 0)"""
    chi = char(i, j, N)
    w = find_w(geo, chi, True)
    G = geo.M if geo.tr > 0 else np.array(geo.M, dtype=object).dot(np.array(geo.M, dtype=object)).tolist()
    w2 = tuple(int(t) for t in np.array(G, dtype=object).dot(np.array(w, dtype=object)))
    z = sum(chi(p) for p in parallelogram(w, w2)) / (1 - chi(w)) ** 2
    return z if geo.tr > 0 else z / 2


def L_odd1(geo, i, j, N, K=100, J=34):
    """sum over (Z^2 - 0)/<M> of chi(v) sign(Q(v)) |Q(v)|^{-1}, with sign(Q) = +1 on the cone L1 L2 > 0"""
    chi = char(i, j, N); chib = char(-i, -j, N); M = geo.M
    tot = 0
    for same, sg in ((True, 1), (False, -1)):
        w = find_w(geo, chi, same)
        if geo.tr > 0:
            tot += sg * (cone_sum(geo, w, M, chi, 1, K, J) + cone_sum(geo, w, M, chib, 1, K, J))
        else:
            M2 = np.array(M, dtype=object).dot(np.array(M, dtype=object)).tolist()
            tot += sg * cone_sum(geo, w, M2, chi, 1, K, J)
    return tot


# ---------------------------------------------------------------------------- vectorised evaluators (production)
CUT = 46.0


def E_fast(c, z, s):
    """E_c(z, s), integer s >= 1, Fourier expansion vectorised over (m, xi)"""
    c1, c2 = frac(c[0]), frac(c[1])
    x, y = z.real, z.imag
    tot = y ** s * (-1) ** (s + 1) * TAU ** (2 * s) * bern(2 * s, c2) / math.factorial(2 * s)
    g = math.gamma(s)
    xmin = min(c2, 1 - c2) if c2 else 1.0
    mmax = int(CUT / (TAU * y * xmin)) + 2
    m = np.arange(1, mmax + 1)
    kk = int(CUT / (TAU * y)) + 3
    xi = np.arange(-kk, kk + 2) - c2
    xi = xi[np.abs(xi) > 1e-15]
    MM, XI = np.meshgrid(m, xi, indexing="ij")
    keep = TAU * np.abs(XI) * MM * y < CUT
    MM, XI = MM[keep], XI[keep]
    Y = MM * y
    core = 2 * math.pi ** s * np.abs(XI) ** (s - 0.5) * Y ** (0.5 - s) * kv(s - 0.5, TAU * np.abs(XI) * Y) / g
    tot += y ** s * np.sum(core * (e(c1 * MM) * e(XI * MM * x) + e(-c1 * MM) * e(-XI * MM * x)))
    if c2 == 0.0:
        lsum = 2 * float(mp.zeta(2 * s - 1)) if c1 == 0.0 else 2 * float(mp.re(mp.polylog(2 * s - 1, mp.exp(2j * mp.pi * c1))))
        tot += y ** (1 - s) * math.sqrt(math.pi) * math.gamma(s - 0.5) / g * lsum
    return complex(tot)


def G_u_fast(u, z):
    u1, u2 = frac(u[0]), frac(u[1])
    y = z.imag
    tot = -math.pi / y
    if u1 == 0.0:
        tot += (math.pi ** 2 / 3) if u2 == 0.0 else float(mp.zeta(2, u2) + mp.zeta(2, 1 - u2))
    Mx = int(CUT / (TAU * y)) + 3
    m = np.arange(-Mx, Mx + 1) + u1
    m = m[np.abs(m) > 1e-15]
    R = int(CUT / (TAU * y * np.min(np.abs(m)))) + 3
    r = np.arange(1, R + 1)
    MM, RR = np.meshgrid(m, r, indexing="ij")
    keep = TAU * RR * np.abs(MM) * y < CUT
    MM, RR = MM[keep], RR[keep]
    arg = np.where(MM > 0, RR * (MM * z + u2), RR * (np.abs(MM) * z - u2))
    tot += -4 * math.pi ** 2 * np.sum(RR * e(arg))
    return complex(tot)


def G_v_fast(c, z):
    c1, c2 = frac(c[0]), frac(c[1])
    y = z.imag
    tot = 2 * math.pi ** 2 * B2(c2)
    xmin = min(c2, 1 - c2) if c2 else 1.0
    mmax = int(CUT / (TAU * y * xmin)) + 3
    m = np.arange(1, mmax + 1)
    kk = int(CUT / (TAU * y)) + 3
    for sgn, cc1, b in ((1, c1, c2), (-1, -c1, -c2)):
        xi = np.arange(-kk, kk + 2) - b
        xi = xi[xi > 1e-15]
        MM, XI = np.meshgrid(m, xi, indexing="ij")
        keep = TAU * XI * MM * y < CUT
        MM, XI = MM[keep], XI[keep]
        tot += -4 * math.pi ** 2 * np.sum(e(cc1 * MM) * XI * e(XI * MM * z))
    return complex(tot)


# ---------------------------------------------------------------------------- production cone sums (two twists, batched)
_TT = {}


def Tvec(x, J2):
    """T_j(x) = sum_{k>=0} k^j x^k (Abel), j = 0..J2, at 40 digits"""
    key = (round(x.real, 14), round(x.imag, 14), J2)
    if key in _TT: return _TT[key]
    with mp.workdps(40):
        X = mp.mpc(x); wv = X / (1 - X)
        S = [[mp.mpf(0)] * (J2 + 2) for _ in range(J2 + 2)]
        S[0][0] = mp.mpf(1)
        for n in range(1, J2 + 2):
            for k in range(1, n + 1):
                S[n][k] = k * S[n - 1][k] + S[n - 1][k - 1]
        out = []
        for n in range(J2 + 1):
            li = mp.fsum(mp.factorial(k) * S[n + 1][k + 1] * wv ** (k + 1) for k in range(n + 1))
            out.append(complex(li + (1 if n == 0 else 0)))
    _TT[key] = np.array(out)
    return _TT[key]


def F_all(geo, w, w2, s, pairs, K, J):
    """F[p, q] = sum_{k,l>=0} x1^k x2^l |L1(v) L2(v)|^{-s}, v = p + k w + l w2, for p in the parallelogram and the
    pairs q = (x1, x2) (both != 1); returns (points, F) with the factor |beta - beta'|^s applied"""
    pts = parallelogram(w, w2)
    A1, A2 = abs(geo.L1(w)), abs(geo.L1(w2)); B1, B2_ = abs(geo.L2(w)), abs(geo.L2(w2))
    bn = binoms(s, 2 * J)
    k = np.arange(K)
    X1 = np.array([[q[0] ** kk for kk in k] for q in pairs]); X2 = np.array([[q[1] ** kk for kk in k] for q in pairs])
    x1K = np.array([q[0] ** K for q in pairs]); x2K = np.array([q[1] ** K for q in pairs])
    T1 = np.array([Tvec(q[0], 2 * J) for q in pairs]); T2 = np.array([Tvec(q[1], 2 * J) for q in pairs])
    out = np.zeros((len(pts), len(pairs)), dtype=complex)
    idx = np.arange(J + 1)
    H1 = T1[:, idx[:, None] + idx[None, :]]; H2 = T2[:, idx[:, None] + idx[None, :]]
    for ip, p in enumerate(pts):
        A0, B0 = abs(geo.L1(p)), abs(geo.L2(p))
        f = np.exp(-s * (np.log(A0 + k[:, None] * A1 + k[None, :] * A2) + np.log(B0 + k[:, None] * B1 + k[None, :] * B2_)))
        direct = np.einsum("qk,kl,ql->q", X1, f, X2)
        a = conv_last(taylor1(A0 + K * A1 + k * A2, A1, s, J, bn[:J + 1]), taylor1(B0 + K * B1 + k * B2_, B1, s, J, bn[:J + 1]), J)
        tail_k = x1K * np.einsum("ql,lj,qj->q", X2, a, T1[:, :J + 1])
        b = conv_last(taylor1(A0 + k * A1 + K * A2, A2, s, J, bn[:J + 1]), taylor1(B0 + k * B1 + K * B2_, B2_, s, J, bn[:J + 1]), J)
        tail_l = x2K * np.einsum("qk,kj,qj->q", X1, b, T2[:, :J + 1])
        CA = taylor2(A0 + K * A1 + K * A2, A1, A2, s, J, bn); CB = taylor2(B0 + K * B1 + K * B2_, B1, B2_, s, J, bn)
        corner = x1K * x2K * np.einsum("ab,qac,cd,qbd->q", CA, H1, CB, H2)
        out[ip] = direct + tail_k + tail_l + corner
    return pts, out * abs(geo.beta - geo.betap) ** s


def cone_vectors(geo, same, count=4):
    out = []
    for r in range(1, 60):
        for w in itertools.product(range(-r, r + 1), repeat=2):
            if max(abs(w[0]), abs(w[1])) != r or math.gcd(*w) != 1: continue
            a1, a2 = geo.L1(w), geo.L2(w)
            if (a1 > 0 and a2 > 0) if same else (a1 > 0 and a2 < 0):
                out.append(w)
        if len(out) >= count: return out[:count]
    return out


def level_zetas(geo, chars, s_list, Kmin=80, J=36):
    """for every character (i, j, N) of a level: Z_same(s) and Z_opp(s), sums over the cone's lattice points mod <M>,
    at every s in s_list.  The cone C mod <G>, G = M (tr > 0) or -M (tr < 0), with chi and its conjugate: every <M>-orbit
    of C and -C is met once (for tr < 0 the orbits of v and -v share one <-M>-orbit of C, and chi(v) + chi(-v) is
    invariant under -M).  chi is evaluated pointwise.  Returns {(i,j,N): {s: [Z_same, Z_opp]}}"""
    M = geo.M
    G = M if geo.tr > 0 else [[-M[0][0], -M[0][1]], [-M[1][0], -M[1][1]]]
    res = {ch: {s: [0j, 0j] for s in s_list} for ch in chars}
    for t_idx, same in enumerate((True, False)):
        ws = cone_vectors(geo, same)
        # assign each character a w with chi(w) != 1 and chi(G w) != 1
        plan = {}
        for (i, j, N) in chars:
            chi = char(i, j, N)
            for w in ws:
                w2 = tuple(int(t) for t in np.array(G, dtype=object).dot(np.array(w, dtype=object)))
                if abs(chi(w) - 1) > 1e-9 and abs(chi(w2) - 1) > 1e-9:
                    plan.setdefault(w, []).append((i, j, N)); break
            else:
                raise ValueError("no cone vector for %s" % ((i, j, N),))
        for w, chs in plan.items():
            w2 = tuple(int(t) for t in np.array(G, dtype=object).dot(np.array(w, dtype=object)))
            jobs = []          # (character, conjugate?)
            for ch in chs:
                jobs.append((ch, False)); jobs.append((ch, True))
            pairs = []
            for (ch, cj) in jobs:
                i, j, N = ch
                chi = char(-i, -j, N) if cj else char(i, j, N)
                pairs.append((complex(chi(w)), complex(chi(w2))))
            upairs = sorted(set((round(a.real, 12), round(a.imag, 12), round(b.real, 12), round(b.imag, 12)) for a, b in pairs))
            uq = [(complex(a, b), complex(c, d)) for a, b, c, d in upairs]
            thmin = min(min(abs(cmath.phase(q[0])), abs(cmath.phase(q[1]))) for q in uq)
            K = max(Kmin, int(math.ceil(42 / thmin)))
            for s in s_list:
                pts, F = F_all(geo, w, w2, s, uq, K, J)
                key = {u: n for n, u in enumerate(upairs)}
                for (ch, cj), pq in zip(jobs, pairs):
                    i, j, N = ch
                    chi = char(-i, -j, N) if cj else char(i, j, N)
                    col = key[(round(pq[0].real, 12), round(pq[0].imag, 12), round(pq[1].real, 12), round(pq[1].imag, 12))]
                    val = sum(chi(p) * F[ip, col] for ip, p in enumerate(pts))
                    res[ch][s][t_idx] += val
    return res
