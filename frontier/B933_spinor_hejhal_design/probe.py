r"""B933 feasibility probe: the spinor (Dirac) Hejhal collocation on m004.

EXPLORATORY NUMERICS (double precision). Not a sealed run; no verdict
claims. Authorized by the B921-harvested Cell-3 spin fork (rho_1 = (A,B),
peripheral trace pattern (2,-2), non-Lie under both conventions =>
discrete Dirac spectrum, Baer dichotomy). Design document: DESIGN.md.

THE OPERATOR (conventions declared in DESIGN.md sec 2):
    D = -i [ t(sigma_1 d_x + sigma_2 d_y + sigma_3 d_t) - sigma_3 ]
acting on psi: H^3 -> C^2 in the Iwasawa-section trivialization
s(z,t) = [[sqrt t, z/sqrt t],[0, 1/sqrt t]]; self-adjoint in
L^2(t^{-3} dx dy dt) (checked three independent ways in DESIGN.md).

THE CUSP MODES (spin structure rho_1: meridian periodic, longitude
ANTIperiodic => Fourier characters on the SHIFTED lattice
mu in Lam* + u2/2, no mu = 0 term):
    psi_mu(z,t) = e^{2 pi i <mu,z>} t^{3/2}
        ( K_{i lam - 1/2}(2 pi |mu| t) ,
          -i e^{i theta_mu} K_{i lam + 1/2}(2 pi |mu| t) )
with theta_mu = arg mu and K_{i lam + 1/2}(x) = conj(K_{i lam - 1/2}(x))
for real x, lam.

THE COLLOCATION IDENTITY (vector-valued, spin-twisted):
    psi(x*_j) = conj(k_j) psi(x_j),
    k_j = s(x*_j)^{-1} rho_1(g_j) s(x_j) in SU(2)
where g_j is the FULL tracked SL(2,C) word product of the pullback
(including lattice reductions, each with its rho_1 lift sign
(-1)^{n_longitude}). The scalar instrument's PSL sign-normalization and
sign-free lattice reduction are NOT carried over.

THE CONJUGATE (gate G2b, learned from a flat-landscape failure): the
geometric frame rotation of the coordinate frame (t d_x, t d_y, t d_t)
under g is Ad(conj(k)), NOT Ad(k):  R_geom = C Ad(k) C, C = diag(1,-1,1)
(verified numerically to 1e-6 over random group elements). The spinor
automorphy twist compatible with D as written is therefore the
elementwise CONJUGATE Iwasawa factor. With the unconjugated twist the
system is inconsistent and sigma_min(lam) is flat ~0.5 with no dips --
the exact failure observed on the first scan attempt.

Stages:
    python3 probe.py validate     # gates G1/G2: operator identity, twists
    python3 probe.py scan         # sigma_min(lam) over [-4, 4]
    python3 probe.py refine       # golden refine + two-Y + pairing check
"""
import json
import os
import sys
import time
from itertools import product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

SQ3 = np.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
A = np.array([[1, 1], [0, 1]], dtype=complex)
Ai = np.array([[1, -1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-OMEGA, 1]], dtype=complex)
Bi = np.array([[1, 0], [OMEGA, 1]], dtype=complex)
GEN = {'a': A, 'A': Ai, 'b': B, 'B': Bi}
CANCEL = ('aA', 'Aa', 'bB', 'Bb')
LONG_WORD = 'bABaaBAb'   # the banked longitude (cell3_spin_fork)

SIG1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIG2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIG3 = np.array([[1, 0], [0, -1]], dtype=complex)


def wmat(w):
    m = np.eye(2, dtype=complex)
    for ch in w:
        m = m @ GEN[ch]
    return m


def reduced_words(maxlen):
    for L in range(1, maxlen + 1):
        for tup in product('abAB', repeat=L):
            w = ''.join(tup)
            if any(x + y in CANCEL for x, y in zip(w, w[1:])):
                continue
            yield w


# ----------------------------------------------------------------
# Cusp lattice (scalar machinery, unchanged: PSL-level, sign-free)
# ----------------------------------------------------------------

def find_cusp_lattice(maxlen=8):
    trans = []
    for w in reduced_words(maxlen):
        M = wmat(w)
        if abs(M[1, 0]) > 1e-9:
            continue
        u = M[0, 0]
        if abs(u - 1) < 1e-9:
            v = M[0, 1]
        elif abs(u + 1) < 1e-9:
            v = -M[0, 1]
        else:
            continue
        if abs(v.imag) > 1e-9:
            trans.append((complex(v), w))
    if not trans:
        raise RuntimeError("no non-meridian parabolic found")
    v0, w0 = min(trans, key=lambda p: abs(p[0].imag))
    tau = v0 - round(v0.real)
    if tau.imag < 0:
        tau = -tau
    Minv = np.linalg.inv(np.array([[1.0, tau.real], [0.0, tau.imag]]))
    bad = 0
    for v, _ in trans:
        n = Minv @ np.array([v.real, v.imag])
        if np.max(np.abs(n - np.round(n))) > 1e-7:
            bad += 1
    return tau, w0, len(trans), bad


class SpinLattice:
    """Cusp lattice + the rho_1-shifted dual (antiperiodic along tau)."""

    def __init__(self, tau):
        self.tau = tau
        self.M = np.array([[1.0, tau.real], [0.0, tau.imag]])
        self.Minv = np.linalg.inv(self.M)
        U = self.Minv
        self.u1 = complex(U[0, 0], U[0, 1])
        self.u2 = complex(U[1, 0], U[1, 1])
        self.covol = abs(tau.imag)

    def reduce_counts(self, z):
        """z -> z - (n1 + n2 tau); returns (z_red, n1, n2)."""
        n = np.round(self.Minv @ np.array([z.real, z.imag]))
        n1, n2 = int(n[0]), int(n[1])
        return z - (n1 + n2 * self.tau), n1, n2

    def modes_shifted(self, Rcut):
        """All mu = m1 u1 + (m2 + 1/2) u2 with |mu| <= Rcut.

        These are exactly the characters with e^{2 pi i <mu, 1>} = +1 and
        e^{2 pi i <mu, tau>} = -1 (meridian periodic, longitude
        antiperiodic): the rho_1 spinor lattice. No mu = 0 exists."""
        covs = 1.0 / self.covol
        N1 = int(Rcut * abs(self.u2) / covs) + 3
        N2 = int(Rcut * abs(self.u1) / covs) + 3
        out = []
        for m1 in range(-N1, N1 + 1):
            for m2 in range(-N2, N2 + 1):
                mu = m1 * self.u1 + (m2 + 0.5) * self.u2
                if abs(mu) <= Rcut:
                    out.append(mu)
        return np.array(out)


def trans_lift(n1, n2, tau):
    """rho_1 lift of the translation z -> z + n1 + n2*tau.

    The meridian lift is +[[1,1],[0,1]] (trace +2); the longitude lift is
    -[[1,tau],[0,1]] (trace -2, cell3). Character: (-1)^{n2}."""
    om = n1 + n2 * tau
    return ((-1) ** (n2 % 2)) * np.array([[1, om], [0, 1]], dtype=complex)


# ----------------------------------------------------------------
# Moves WITH exact rho_1 lifts (no sign normalization!)
# ----------------------------------------------------------------

def build_spin_moves(maxlen=5, cmax=2.2):
    mats, seen = [], set()
    for w in reduced_words(maxlen):
        M = wmat(w)          # the TRUE rho_1 lift of this word
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > cmax:
            continue
        # canonicalize the KEY only (PSL dedupe); store M itself
        cc, dd = c, M[1, 1]
        if cc.real < 0 or (abs(cc.real) < 1e-12 and cc.imag < 0):
            cc, dd = -cc, -dd
        key = tuple(np.round([cc.real, cc.imag, dd.real, dd.imag], 9))
        if key in seen:
            continue
        seen.add(key)
        mats.append(M)
    return mats


def apply_m(M, z, t):
    a, b = M[0]
    c, d = M[1]
    w = c * z + d
    D = abs(w) ** 2 + abs(c) ** 2 * t * t
    return ((a * z + b) * w.conjugate() + a * c.conjugate() * t * t) / D, t / D


def reduce_pt_spin(lat, moves, z, t, itmax=400):
    """Pullback with full SL(2,C) tracking. Returns (z*, t*, G, moved)."""
    G = np.eye(2, dtype=complex)
    z, n1, n2 = lat.reduce_counts(z)
    if n1 or n2:
        G = trans_lift(-n1, -n2, lat.tau) @ G
    moved = False
    for _ in range(itmax):
        best = None
        for M in moves:
            z2, t2 = apply_m(M, z, t)
            if t2 > t * (1 + 1e-13) and (best is None or t2 > best[1]):
                best = (z2, t2, M)
        if best is None:
            break
        z, t, M = best
        G = M @ G
        z, n1, n2 = lat.reduce_counts(z)
        if n1 or n2:
            G = trans_lift(-n1, -n2, lat.tau) @ G
        moved = True
    return z, t, G, moved


def s_mat(z, t):
    rt = np.sqrt(t)
    return np.array([[rt, z / rt], [0, 1 / rt]], dtype=complex)


def s_inv(z, t):
    rt = np.sqrt(t)
    return np.array([[1 / rt, -z / rt], [0, rt]], dtype=complex)


def twist(zstar, tstar, G, z, t):
    """k = s(x*)^{-1} G s(x); in SU(2) iff G maps x to x* (Iwasawa)."""
    return s_inv(zstar, tstar) @ G @ s_mat(z, t)


def su2_dev(k):
    return max(np.abs(k @ k.conj().T - np.eye(2)).max(),
               abs(np.linalg.det(k) - 1))


# ----------------------------------------------------------------
# K_{i lam - 1/2} via the exponentially convergent trapezoid
# ----------------------------------------------------------------

def bessel_nodes(lmax, xmin, tol_exp=45.0):
    h = min(0.15, 2 * np.pi / (2 * lmax + 30.0))
    T0 = np.arccosh((np.pi * lmax / 2 + tol_exp) / xmin)
    Tmax = np.arccosh((np.pi * lmax / 2 + tol_exp + T0 / 2 + 1) / xmin)
    Q = int(np.ceil(Tmax / h)) + 1
    ts = h * np.arange(Q)
    wts = np.full(Q, h)
    wts[0] = h / 2
    return ts, wts


def K_column(ts, wts, lam):
    """Weight column: E @ col = K_{i lam - 1/2}(x) for E = exp(-x cosh ts).

    K_{i lam - 1/2}(x) = int_0^inf e^{-x cosh u}
        [cosh(u/2) cos(lam u) - i sinh(u/2) sin(lam u)] du."""
    return (np.cosh(ts / 2) * np.cos(lam * ts)
            - 1j * np.sinh(ts / 2) * np.sin(lam * ts)) * wts


def sample_points(lat, npts, rng_seed=11):
    rng = np.random.default_rng(rng_seed)
    L2 = abs(lat.tau)
    n1 = int(np.ceil(np.sqrt(npts / L2)))
    n2 = int(np.ceil(npts / n1))
    zs = []
    for i1 in range(n1):
        for i2 in range(n2):
            s1 = (i1 + 0.5 + rng.uniform(-0.2, 0.2)) / n1
            s2 = (i2 + 0.5 + rng.uniform(-0.2, 0.2)) / n2
            zs.append(s1 + s2 * lat.tau)
    return zs[:max(npts, n1 * n2)]


# ----------------------------------------------------------------
# The collocation system
# ----------------------------------------------------------------

class SpinSystem:
    def __init__(self, lat, moves, Y, lmax, margin=21.0, oversample=0.75,
                 seed=11):
        self.Y = Y
        xcut = np.pi * lmax / 2 + margin
        Rcut = xcut / (2 * np.pi * Y)
        self.mus = lat.modes_shifted(Rcut)
        nmodes = len(self.mus)
        zs = sample_points(lat, int(np.ceil(oversample * nmodes)),
                           rng_seed=seed)
        zstar = np.empty(len(zs), dtype=complex)
        tstar = np.empty(len(zs))
        ks = np.empty((len(zs), 2, 2), dtype=complex)
        mv = np.zeros(len(zs), dtype=bool)
        sudev = 0.0
        for j, z in enumerate(zs):
            zs_, ts_, G, m = reduce_pt_spin(lat, moves, z, Y)
            zstar[j], tstar[j], mv[j] = zs_, ts_, m
            # base point = the ORIGINAL z: the tracked G maps z -> z*
            # (including the initial lattice reduction); phases below are
            # evaluated at the same original z, so twist and phases match.
            # G2b: the automorphy twist is the CONJUGATE Iwasawa factor.
            k = twist(zs_, ts_, G, z, Y)
            sudev = max(sudev, su2_dev(k))
            ks[j] = np.conj(k)
        keep = mv & (tstar > Y * (1 + 1e-9))
        self.zs = np.array(zs)[keep]
        self.zstar, self.tstar, self.ks = zstar[keep], tstar[keep], ks[keep]
        self.su2_dev_max = sudev
        absmu = np.abs(self.mus)
        self.norms, self.nrm_idx = np.unique(np.round(absmu, 12),
                                             return_inverse=True)
        self.theta_fac = -1j * np.exp(1j * np.angle(self.mus))
        self.heights = np.concatenate([[Y], self.tstar])
        args = (2 * np.pi * np.outer(self.norms, self.heights))
        self.arg_shape = args.shape
        flat = args.ravel()
        self.ts, self.wts = bessel_nodes(lmax, flat.min())
        self.E = np.exp(-np.outer(flat, np.cosh(self.ts)))
        d0 = (np.outer(self.zs.real, self.mus.real)
              + np.outer(self.zs.imag, self.mus.imag))
        d1 = (np.outer(self.zstar.real, self.mus.real)
              + np.outer(self.zstar.imag, self.mus.imag))
        self.P0 = np.exp(2j * np.pi * d0)
        self.P1 = np.exp(2j * np.pi * d1)

    def sigma(self, lam, nsv=3):
        K = (self.E @ K_column(self.ts, self.wts, lam)).reshape(
            self.arg_shape)
        K1Y = K[self.nrm_idx, 0]                  # (nmodes,)
        K1s = K[self.nrm_idx, 1:]                 # (nmodes, npts)
        Y32 = self.Y ** 1.5
        t32 = self.tstar ** 1.5
        c1x = Y32 * K1Y[None, :] * self.P0
        c2x = Y32 * (self.theta_fac * np.conj(K1Y))[None, :] * self.P0
        c1s = t32[:, None] * K1s.T * self.P1
        c2s = (t32[:, None] * (self.theta_fac[None, :] * np.conj(K1s.T))
               * self.P1)
        k = self.ks
        R1 = c1s - (k[:, 0, 0][:, None] * c1x + k[:, 0, 1][:, None] * c2x)
        R2 = c2s - (k[:, 1, 0][:, None] * c1x + k[:, 1, 1][:, None] * c2x)
        V = np.vstack([R1, R2])
        cn = np.linalg.norm(V, axis=0)
        cn[cn == 0] = 1.0
        sv = np.linalg.svd(V / cn[None, :], compute_uv=False)
        return sv[-nsv:][::-1]                    # smallest first


def golden_min(f, a, b, tol=2e-8):
    g = (np.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    while b - a > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a)
            fd = f(d)
    return (a + b) / 2, min(fc, fd)


# ----------------------------------------------------------------
# Stage: validate  (gates G1, G2 of the design)
# ----------------------------------------------------------------

def validate():
    import mpmath as mp
    out = {}
    print("=" * 72)
    print("VALIDATE: lattice, longitude lift, Bessel, operator FD, twists")
    print("=" * 72)

    tau, w0, nfound, nbad = find_cusp_lattice()
    print(f"\n[lattice] tau = {tau:.12f} (word '{w0}', {nfound} parabolics, "
          f"{nbad} outside Z+Z*tau)")
    assert nbad == 0
    dev_tau = abs(tau - 2j * SQ3)
    print(f"[lattice] |tau - 2 sqrt(-3)| = {dev_tau:.2e}")
    out['tau'] = [tau.real, tau.imag]
    out['tau_vs_2sqrtm3'] = float(dev_tau)
    lat = SpinLattice(tau)

    # longitude lift: trace -2, parabolic at infinity, translation in Z+Ztau
    L = wmat(LONG_WORD)
    trL = np.trace(L)
    print(f"\n[longitude] rho_1({LONG_WORD}): tr = {trL:.2e}, "
          f"c = {abs(L[1,0]):.2e}")
    assert abs(trL + 2) < 1e-9 and abs(L[1, 0]) < 1e-9
    vL = -L[0, 1]  # L = -[[1, v],[0,1]] since tr = -2
    nvec = lat.Minv @ np.array([vL.real, vL.imag])
    print(f"[longitude] translation {vL:.6f} = "
          f"({nvec[0]:.6f}, {nvec[1]:.6f}) in lattice basis")
    assert np.max(np.abs(nvec - np.round(nvec))) < 1e-9
    assert int(round(nvec[1])) % 2 == 1, \
        "longitude must be ODD in the tau-direction for the spin character"
    out['longitude_lattice_coords'] = [float(nvec[0]), float(nvec[1])]

    # shifted lattice: minimal |mu|
    mus = lat.modes_shifted(3.0)
    mumin = np.min(np.abs(mus))
    print(f"\n[modes] shifted-lattice |mu|_min = {mumin:.9f} "
          f"(theory 1/(4 sqrt3) = {1/(4*SQ3):.9f}); "
          f"modes |mu|<=3: {len(mus)}")
    assert abs(mumin - 1 / (4 * SQ3)) < 1e-9
    out['mu_min'] = float(mumin)

    # mode antiperiodicity/periodicity (the spin character wiring)
    rng = np.random.default_rng(5)
    mu = mus[rng.integers(len(mus))]
    z = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
    ph = lambda zz: np.exp(2j * np.pi * (mu.real * zz.real
                                         + mu.imag * zz.imag))
    dev_m = abs(ph(z + 1) - ph(z))
    dev_l = abs(ph(z + tau) + ph(z))
    print(f"[modes] meridian periodicity dev = {dev_m:.2e}, "
          f"longitude ANTIperiodicity dev = {dev_l:.2e}")
    assert dev_m < 1e-12 and dev_l < 1e-12

    # Bessel trapezoid vs mpmath (complex order i*lam - 1/2)
    mp.mp.dps = 30
    print("\n[bessel] trapezoid K_{i lam - 1/2}(x) vs mpmath:")
    maxrel = 0.0
    for lam in (0.0, 0.7, 2.3, 4.0):
        ts, wts = bessel_nodes(4.0, 0.4)
        for x in (0.45, 1.2, 3.0, 8.0, 20.0):
            got = np.exp(-x * np.cosh(ts)) @ K_column(ts, wts, lam)
            ref = mp.besselk(mp.mpc(-0.5, lam), x)
            ref = complex(ref)
            rel = abs(got - ref) / abs(ref)
            maxrel = max(maxrel, rel)
        print(f"  lam = {lam}: max rel err so far {maxrel:.2e}")
    assert maxrel < 1e-9
    out['bessel_max_rel_err'] = float(maxrel)

    # G1: the operator identity D psi_mu = lam psi_mu by finite differences
    # (mpmath, dps 40, h = 1e-8: FD truncation ~1e-16 relative)
    print("\n[G1] FD check of D psi = lam psi on modes "
          "(D = -i[t sigma.d - sigma_3], mpmath dps 40):")
    mp.mp.dps = 40
    h = mp.mpf(10) ** -8

    def mode_mp(zx, zy, t, mu, lam):
        k2p = 2 * mp.pi * abs(mu)
        phv = mp.e ** (2j * mp.pi * (mu.real * zx + mu.imag * zy))
        th = mp.atan2(mu.imag, mu.real)
        K1 = mp.besselk(mp.mpc(-0.5, lam), k2p * t)
        K2 = mp.besselk(mp.mpc(0.5, lam), k2p * t)
        w = t ** mp.mpf(1.5)
        return (phv * w * K1,
                phv * w * (-1j) * mp.e ** (1j * th) * K2)

    maxres = 0.0
    rng = np.random.default_rng(17)
    for trial in range(4):
        mu = complex(mus[rng.integers(len(mus))])
        lam = [1.234, -0.777, 2.9, 0.0][trial]
        zx = mp.mpf(str(rng.uniform(-0.4, 0.4)))
        zy = mp.mpf(str(rng.uniform(-0.4, 0.4)))
        t = mp.mpf(str(rng.uniform(0.6, 1.1)))
        f0 = mode_mp(zx, zy, t, mu, lam)
        dx = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx + h, zy, t, mu, lam), mode_mp(zx - h, zy, t, mu, lam))]
        dy = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx, zy + h, t, mu, lam), mode_mp(zx, zy - h, t, mu, lam))]
        dt = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx, zy, t + h, mu, lam), mode_mp(zx, zy, t - h, mu, lam))]
        # sigma.d psi
        s1 = (dx[1], dx[0])                      # sigma_1 (swap)
        s2 = (-1j * dy[1], 1j * dy[0])           # sigma_2
        s3 = (dt[0], -dt[1])                     # sigma_3
        Dpsi = [-1j * (t * (s1[c] + s2[c] + s3[c])
                       - (f0[c] if c == 0 else -f0[c]))
                for c in range(2)]
        scale = max(abs(f0[0]), abs(f0[1]))
        res = max(abs(Dpsi[c] - lam * f0[c]) for c in range(2)) / (
            abs(lam) * scale if lam != 0 else scale)
        maxres = max(maxres, float(res))
        print(f"  mu = {mu:.4f}, lam = {lam}: rel residual = {float(res):.2e}")
    assert maxres < 1e-10, "operator identity FAILED"
    out['G1_fd_max_rel_residual'] = maxres

    # G2: twists. Peripheral twists must be EXACTLY +-1; cocycle closes.
    print("\n[G2] twists:")
    z0, t0 = complex(0.13, 0.44), 0.8
    kM = twist(z0 + 1, t0, wmat('a'), z0, t0)
    kL = twist(z0 + vL, t0, L, z0, t0)
    dM = np.abs(kM - np.eye(2)).max()
    dL = np.abs(kL + np.eye(2)).max()
    print(f"  meridian twist - (+I): {dM:.2e};  longitude twist - (-I): "
          f"{dL:.2e}")
    assert dM < 1e-12 and dL < 1e-12
    out['twist_meridian_dev'] = float(dM)
    out['twist_longitude_dev'] = float(dL)

    # G2b: the frame gate. The automorphy twist must implement the
    # GEOMETRIC rotation of the coordinate frame (t d_x, t d_y, t d_t)
    # in the declared sigma-assignment: Ad(conj(k)) = R_geom.
    print("\n[G2b] frame gate: Ad(conj k) vs the numeric frame rotation:")
    C3 = np.diag([1.0, -1.0, 1.0])
    sig = [SIG1, SIG2, SIG3]

    def frame_rot_geom(g, z, t, eps=1e-6):
        z0, t0 = apply_m(g, z, t)
        R = np.zeros((3, 3))
        for j, (dz, dt_) in enumerate([(eps * t, 0), (1j * eps * t, 0),
                                       (0, eps * t)]):
            z1, t1 = apply_m(g, z + dz, t + dt_)
            R[0, j] = (z1 - z0).real / (eps * t0)
            R[1, j] = (z1 - z0).imag / (eps * t0)
            R[2, j] = (t1 - t0) / (eps * t0)
        return R

    def frame_rot_ad(k):
        ki = np.linalg.inv(k)
        return np.array([[0.5 * np.trace(sig[i] @ k @ sig[j] @ ki).real
                          for j in range(3)] for i in range(3)])

    rng = np.random.default_rng(9)
    maxfr = 0.0
    for _ in range(6):
        w = ''.join(rng.choice(list('abAB'), size=rng.integers(2, 5)))
        g = wmat(w)
        z = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        t = rng.uniform(0.5, 1.0)
        z1, t1 = apply_m(g, z, t)
        k = twist(z1, t1, g, z, t)
        dev = np.abs(frame_rot_geom(g, z, t)
                     - frame_rot_ad(np.conj(k))).max()
        maxfr = max(maxfr, dev)
    print(f"  max |R_geom - Ad(conj k)| over 6 random elements: {maxfr:.2e}")
    assert maxfr < 1e-5, "frame gate FAILED"
    out['G2b_frame_gate_max_dev'] = float(maxfr)

    rng = np.random.default_rng(23)
    maxco = 0.0
    for _ in range(20):
        w1 = ''.join(rng.choice(list('abAB'), size=rng.integers(1, 5)))
        w2 = ''.join(rng.choice(list('abAB'), size=rng.integers(1, 5)))
        g1, g2 = wmat(w1), wmat(w2)
        z = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        t = rng.uniform(0.4, 1.2)
        z2, t2 = apply_m(g2, z, t)
        z12, t12 = apply_m(g1 @ g2, z, t)
        k_a = twist(z12, t12, g1 @ g2, z, t)
        k_b = twist(z12, t12, g1, z2, t2) @ twist(z2, t2, g2, z, t)
        maxco = max(maxco, np.abs(k_a - k_b).max())
    print(f"  cocycle k(g1 g2) = k(g1)k(g2): max dev over 20 = {maxco:.2e}")
    assert maxco < 1e-10
    out['cocycle_max_dev'] = float(maxco)

    # SU(2)ness along real pullbacks
    moves = build_spin_moves()
    print(f"\n[moves] {len(moves)} moves (exact rho_1 lifts)")
    rng = np.random.default_rng(3)
    maxsu = 0.0
    for _ in range(40):
        z = complex(rng.uniform(-1, 1), rng.uniform(-2, 2))
        t = rng.uniform(0.4, 0.8)
        zs_, ts_, G, m = reduce_pt_spin(lat, moves, z, t)
        k = twist(zs_, ts_, G, z, t)
        maxsu = max(maxsu, su2_dev(k))
    print(f"[G2] SU(2) deviation over 40 pullback twists: {maxsu:.2e}")
    assert maxsu < 1e-9
    out['su2_max_dev'] = float(maxsu)

    with open(os.path.join(HERE, 'validate_out.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print("\nVALIDATE COMPLETE (gates G1, G2 pass at double/mpmath "
          "precision).")


# ----------------------------------------------------------------
# Stage: scan
# ----------------------------------------------------------------

def pick_Y(lat, moves):
    for Yc in (0.75, 0.68, 0.62, 0.56, 0.50, 0.45):
        zs = sample_points(lat, 150, rng_seed=3)
        rise = sum(1 for z in zs
                   if reduce_pt_spin(lat, moves, z, Yc)[1] > Yc * (1 + 1e-9))
        if rise >= 0.97 * len(zs):
            return Yc
    return 0.45


def scan(lmin=-4.0, lmax_=4.0, dl=0.02):
    t0 = time.time()
    tau, _, _, _ = find_cusp_lattice()
    lat = SpinLattice(tau)
    moves = build_spin_moves()
    Y = pick_Y(lat, moves)
    print(f"[scan] Y = {Y}")
    lmax_abs = max(abs(lmin), abs(lmax_))
    S = SpinSystem(lat, moves, Y, lmax_abs)
    print(f"[scan] modes: {len(S.mus)}, pts kept: {len(S.zs)} "
          f"(rows {2*len(S.zs)}), su2_dev {S.su2_dev_max:.2e}, "
          f"bessel nodes {len(S.ts)}, build {time.time()-t0:.0f}s")

    lam_vals = np.arange(lmin, lmax_ + dl / 2, dl)
    sig = np.full((len(lam_vals), 3), np.nan)
    for i, lam in enumerate(lam_vals):
        sig[i] = S.sigma(lam)
        if i % 40 == 0:
            el = time.time() - t0
            print(f"[scan] {i}/{len(lam_vals)} elapsed {el:.0f}s "
                  f"eta {el/max(i,1)*(len(lam_vals)-i):.0f}s", flush=True)

    med = np.nanmedian(sig[:, 0])
    dips = []
    for i in range(1, len(lam_vals) - 1):
        if (sig[i, 0] < sig[i - 1, 0] and sig[i, 0] < sig[i + 1, 0]
                and sig[i, 0] < 0.5 * med):
            dips.append({'lam': float(lam_vals[i]),
                         'sigma': float(sig[i, 0]),
                         'sigma2': float(sig[i, 1])})
    print(f"[scan] median sigma_min = {med:.3e}; {len(dips)} dips:")
    for d in dips:
        print(f"    lam = {d['lam']:+.4f}  sigma = {d['sigma']:.3e} "
              f"(2nd {d['sigma2']:.3e})")
    np.savez(os.path.join(HERE, 'scan_results.npz'),
             lam_vals=lam_vals, sig=sig, Y=Y,
             nmodes=len(S.mus), npts=len(S.zs))
    with open(os.path.join(HERE, 'scan_dips.json'), 'w') as f:
        json.dump({'Y': Y, 'nmodes': int(len(S.mus)),
                   'npts': int(len(S.zs)),
                   'su2_dev_max': float(S.su2_dev_max),
                   'lmin': lmin, 'lmax': lmax_, 'dl': dl,
                   'median_sigma': float(med), 'dips': dips,
                   'scan_seconds': time.time() - t0}, f, indent=1)
    print(f"[scan] saved. total {time.time()-t0:.0f}s")


# ----------------------------------------------------------------
# Stage: refine (golden + second Y + second seed + pairing check)
# ----------------------------------------------------------------

def refine(Y2=0.62, halfwidth=0.03):
    t0 = time.time()
    with open(os.path.join(HERE, 'scan_dips.json')) as f:
        sc = json.load(f)
    tau, _, _, _ = find_cusp_lattice()
    lat = SpinLattice(tau)
    moves = build_spin_moves()
    lmax_abs = max(abs(sc['lmin']), abs(sc['lmax']))
    print(f"[refine] building S1 (Y={sc['Y']}, seed 11) and "
          f"S2 (Y={Y2}, seed 23) ...")
    S1 = SpinSystem(lat, moves, sc['Y'], lmax_abs, seed=11)
    S2 = SpinSystem(lat, moves, Y2, lmax_abs, seed=23)
    print(f"[refine] S1 {len(S1.mus)}m/{len(S1.zs)}p  "
          f"S2 {len(S2.mus)}m/{len(S2.zs)}p  build {time.time()-t0:.0f}s")

    results = []
    for d in sc['dips']:
        l0 = d['lam']
        f1 = lambda x: S1.sigma(x, 1)[0]
        f2 = lambda x: S2.sigma(x, 1)[0]
        l1, s1 = golden_min(f1, l0 - halfwidth, l0 + halfwidth)
        l2, s2 = golden_min(f2, l1 - halfwidth, l1 + halfwidth)
        dev = abs(l1 - l2)
        stable = bool(dev < 5e-4 and s2 < 0.1 * sc['median_sigma'])
        results.append({'lam_Y1': l1, 'sigma_Y1': s1, 'lam_Y2': l2,
                        'sigma_Y2': s2, 'dev': dev, 'stable': stable})
        print(f"  dip {l0:+.4f}: Y1 -> {l1:+.8f} ({s1:.2e}), "
              f"Y2 -> {l2:+.8f} ({s2:.2e}), |dl| = {dev:.2e} "
              f"{'STABLE' if stable else 'UNSTABLE/spurious'}")

    stab = [r['lam_Y1'] for r in results if r['stable']]
    # |lam| < 1e-6 = the kernel candidate; excluded from +- pairing
    pos = sorted(x for x in stab if x > 1e-6)
    neg = sorted((-x for x in stab if x < -1e-6))
    pairs = []
    for p in pos:
        m = min(neg, key=lambda q: abs(q - p)) if neg else None
        pairs.append({'pos': p, 'neg_abs': m,
                      'pair_dev': abs(m - p) if m is not None else None})
    print(f"\n[refine] stable: {len(stab)}; +/- pairing "
          f"(amphichirality gate, reported not enforced):")
    for pr in pairs:
        print(f"    +{pr['pos']:.6f} vs {pr['neg_abs']} "
              f"(dev {pr['pair_dev']})")
    vol = 2.029883212819307
    weyl = 2 * vol / (6 * np.pi ** 2)
    Lw = max((abs(x) for x in stab), default=0)
    print(f"[refine] Weyl screen: N(|lam|<={Lw:.2f}) ~ "
          f"{weyl * Lw ** 3:.1f} expected, {len(stab)} found "
          f"(cusp terms ignored)")
    with open(os.path.join(HERE, 'refined.json'), 'w') as f:
        json.dump({'Y1': sc['Y'], 'Y2': Y2, 'results': results,
                   'stable_lam': stab, 'pairing': pairs,
                   'weyl_expected_at_max': weyl * Lw ** 3,
                   'refine_seconds': time.time() - t0}, f, indent=1)
    print(f"[refine] saved. total {time.time()-t0:.0f}s")


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'validate'
    if cmd == 'validate':
        validate()
    elif cmd == 'scan':
        kw = {}
        if len(sys.argv) > 2:
            kw['lmin'] = float(sys.argv[2])
        if len(sys.argv) > 3:
            kw['lmax_'] = float(sys.argv[3])
        if len(sys.argv) > 4:
            kw['dl'] = float(sys.argv[4])
        scan(**kw)
    elif cmd == 'refine':
        refine()
    else:
        print(f"unknown command {cmd}")
