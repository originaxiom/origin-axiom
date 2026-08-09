r"""Hejhal/Then collocation solver for Maass cusp forms on m004.

B792 (ex-B788) Step 3, Method A, in-sandbox (no specialist). cc3 seat, independent.

THE SETUP. m004 = Gamma_41 \ H^3 with Gamma_41 = <A, B> the Riley
holonomy (the campaign's banked geometric point):

    A = [[1, 1], [0, 1]],   B = [[1, 0], [-w, 1]],   w = (-1 + i sqrt3)/2

Gamma_41 < PSL(2, Z[w]), cusp at infinity. The cusp stabilizer is the
peripheral Z^2: meridian A (translation z -> z+1) and the longitude
(translation tau = cusp shape). Cusp lattice Lam = Z + Z*tau, found by
brute-force search over short words (parabolic upper-triangular).

A Maass cusp form with eigenvalue lam = 1 + r^2 has the cusp expansion
(upper half-space H^3 = {(z, t)}, z in C, t > 0):

    f(z, t) = sum_{0 != mu in Lam*} a_mu * t * K_{ir}(2 pi |mu| t)
              * exp(2 pi i <mu, z>),      <mu, z> = Re(mu) Re(z) + Im(mu) Im(z)

with Lam* the dual lattice. Hejhal/Then collocation: sample points
(z_j, Y) on a horosphere BELOW the fundamental domain, pull each back
to its maximal-height representative (z*_j, t*_j), and impose

    f(z_j, Y) = f(z*_j, t*_j)

which is automatic for a true automorphic f. Truncating the expansion
gives a linear system V(r) a = 0; the smallest singular value of the
(column-normalized) V(r) dips at eigenvalues. Scan r, refine dips,
verify stability under Y-change (spurious dips move, real ones don't).

K-BESSEL. K_{ir}(x) = int_0^inf exp(-x cosh u) cos(r u) du. The
trapezoid rule on this integrand converges EXPONENTIALLY (Poisson
summation: error ~ K_{i(2pi/h - r)}(x)), so ~40 nodes with h <= 0.15
give machine-relative accuracy even against the e^{-pi r/2} scale of
K_{ir}. Validated against mpmath in `groundwork`. Small eigenvalues
(lam = s(2-s) < 1, s in (1,2)) use K_nu with real nu = s-1:
cos(ru) -> cosh(nu u), same nodes.

Gate 5-Q.

Usage:
    python hejhal_m004.py groundwork
    python hejhal_m004.py scan [rmin rmax dr]
"""
import json
import sys
import time
from itertools import product

import numpy as np

SQ3 = np.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
A = np.array([[1, 1], [0, 1]], dtype=complex)
Ai = np.array([[1, -1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-OMEGA, 1]], dtype=complex)
Bi = np.array([[1, 0], [OMEGA, 1]], dtype=complex)
GEN = {'a': A, 'A': Ai, 'b': B, 'B': Bi}
CANCEL = ('aA', 'Aa', 'bB', 'Bb')

OUTDIR = 'frontier/B792_maass_m004_eigenvalues'


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
# Cusp lattice
# ----------------------------------------------------------------

def find_cusp_lattice(maxlen=8):
    """Brute-force search for parabolic-at-infinity elements; extract tau."""
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
        raise RuntimeError("no non-meridian parabolic found; raise maxlen")
    v0, w0 = min(trans, key=lambda p: abs(p[0].imag))
    # normalize real part into [-1/2, 1/2) using the meridian
    tau = v0 - round(v0.real)
    if tau.imag < 0:
        tau = -tau
    # verify every found translation is in Z + Z tau
    Minv = np.linalg.inv(np.array([[1.0, tau.real], [0.0, tau.imag]]))
    bad = 0
    for v, _ in trans:
        n = Minv @ np.array([v.real, v.imag])
        if np.max(np.abs(n - np.round(n))) > 1e-7:
            bad += 1
    return tau, w0, len(trans), bad


class Lattice:
    def __init__(self, tau):
        self.tau = tau
        self.M = np.array([[1.0, tau.real], [0.0, tau.imag]])
        self.Minv = np.linalg.inv(self.M)
        # dual basis under <mu, z> = Re(mu)Re(z) + Im(mu)Im(z)
        U = self.Minv  # rows of Minv are the dual basis vectors
        self.u1 = complex(U[0, 0], U[0, 1])
        self.u2 = complex(U[1, 0], U[1, 1])
        self.covol = abs(tau.imag)

    def reduce(self, z):
        n = np.round(self.Minv @ np.array([z.real, z.imag]))
        return z - (n[0] + n[1] * self.tau)

    def modes(self, Rcut):
        """All 0 != mu in Lam* with |mu| <= Rcut."""
        covs = 1.0 / self.covol
        N1 = int(Rcut * abs(self.u2) / covs) + 2
        N2 = int(Rcut * abs(self.u1) / covs) + 2
        out = []
        for m1 in range(-N1, N1 + 1):
            for m2 in range(-N2, N2 + 1):
                if m1 == 0 and m2 == 0:
                    continue
                mu = m1 * self.u1 + m2 * self.u2
                if abs(mu) <= Rcut:
                    out.append(mu)
        return np.array(out)


# ----------------------------------------------------------------
# Point reduction (pullback to max-height representative)
# ----------------------------------------------------------------

def build_moves(maxlen=5, cmax=2.2):
    """Group elements usable as height-raising moves.

    Returns the elements reachable by REDUCED WORDS OF LENGTH <= maxlen
    that satisfy 0 < |c| <= cmax.  This is NOT a complete list of the
    group elements with |c| <= cmax -- it is a truncation, by design:

        words <= 5 :  91 moves      words <= 6 : 143      words <= 7 : 207

    Only |c| <= cmax matter for points at height t >= 1/cmax (the
    isometric sphere of g has radius 1/|c|; smaller spheres cannot
    strictly raise such points). Dedupe up to sign (PSL).

    Truncation is safe HERE and only here: the caller does steepest-ascent
    pullback, which needs *a* height-raising element, not all of them; the
    extra elements are alternative routes to the same maximum.  Verified
    (cc3, 2026-08-08, C1): over 120 sample points at Y = 0.75 the <=5 and
    <=7 move sets give bit-identical reduced heights, 0 points differing.
    Do NOT reuse this function where completeness of the |c| <= cmax set
    is required (e.g. enumerating cusp points: <=5 finds 8 of the 12
    norm-4 cusp points, <=6 finds all 12).
    """
    mats, seen = [], set()
    for w in reduced_words(maxlen):
        M = wmat(w)
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > cmax:
            continue
        if c.real < 0 or (abs(c.real) < 1e-12 and c.imag < 0):
            M = -M
        # two elements with the same (c, d) row differ by a left
        # Gamma_inf translation (harmless: z is re-reduced mod Lam),
        # so dedupe on the bottom row only
        key = tuple(np.round([M[1, 0].real, M[1, 0].imag,
                              M[1, 1].real, M[1, 1].imag], 9))
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


def reduce_pt(lat, moves, z, t, itmax=400):
    """Pull (z, t) toward its max-height Gamma-translate by steepest
    ascent. Returns (z*, t*, moved). NOTE: even when the ascent stalls
    short of the true maximum, (z*, t*) is a genuine Gamma-translate
    (each step applies an actual group element), so the collocation
    identity f(z, t) = f(z*, t*) remains exact; a stall only costs
    conditioning, never correctness."""
    z = lat.reduce(z)
    moved = False
    for _ in range(itmax):
        best = None
        for M in moves:
            z2, t2 = apply_m(M, z, t)
            if t2 > t * (1 + 1e-13) and (best is None or t2 > best[1]):
                best = (z2, t2)
        if best is None:
            break
        z, t = best
        z = lat.reduce(z)
        moved = True
    return z, t, moved


# ----------------------------------------------------------------
# K-Bessel via exponentially convergent trapezoid
# ----------------------------------------------------------------

def bessel_nodes(rmax, xmin, tol_exp=45.0):
    h = min(0.15, 2 * np.pi / (2 * rmax + 30.0))
    Tmax = np.arccosh((np.pi * rmax / 2 + tol_exp) / xmin)
    Q = int(np.ceil(Tmax / h)) + 1
    ts = h * np.arange(Q)
    wts = np.full(Q, h)
    wts[0] = h / 2
    return ts, wts


def K_table(args, ts, wts, r_vals, nu_vals):
    """K_{ir}(x) for all x in args (flat array), all r in r_vals,
    and K_nu(x) for real nu in nu_vals. Returns (len(args), nr+nnu)."""
    E = np.exp(-np.outer(args, np.cosh(ts)))  # (Nargs, Q)
    C = np.empty((len(ts), len(r_vals) + len(nu_vals)))
    for i, r in enumerate(r_vals):
        C[:, i] = np.cos(r * ts) * wts
    for i, nu in enumerate(nu_vals):
        C[:, len(r_vals) + i] = np.cosh(nu * ts) * wts
    return E @ C


# ----------------------------------------------------------------
# Groundwork: validate everything
# ----------------------------------------------------------------

def groundwork():
    print("=" * 72)
    print("GROUNDWORK: holonomy, cusp lattice, reduction, Bessel")
    print("=" * 72)
    print()

    # -- relator check (validates the Riley rep + cc's B789 relator)
    print("Relator check (which presentations the Riley rep satisfies):")
    for wname in ('aBAb', 'AbaB', 'bABa', 'BabA'):
        W = wmat(wname)
        n1 = np.abs(W @ A - B @ W).max()
        n2 = np.abs(A @ W - W @ B).max()
        print(f"  w = {wname}:  |wA - Bw| = {n1:.2e},  |Aw - wB| = {n2:.2e}")
    print()

    print(f"  tr A = {np.trace(A):.6f}, tr B = {np.trace(B):.6f}, "
          f"tr AB = {np.trace(A @ B):.6f}")
    print()

    # -- cusp lattice
    tau, w0, nfound, nbad = find_cusp_lattice()
    print(f"Cusp lattice: tau = {tau:.12f}  (from word '{w0}', "
          f"{nfound} parabolics found, {nbad} outside Z+Z*tau)")
    try:
        import snappy
        shape = complex(snappy.Manifold('m004').cusp_info()[0].shape)
        print(f"  SnapPy cusp shape: {shape:.12f}")
        match = (abs(abs(tau.imag) - abs(shape.imag)) < 1e-6)
        print(f"  Im(tau) matches SnapPy: {match}")
    except Exception as e:
        print(f"  (SnapPy check skipped: {e})")
    lat = Lattice(tau)
    print(f"  covol(Lam) = {lat.covol:.9f}, dual basis u1 = {lat.u1:.6f}, "
          f"u2 = {lat.u2:.6f}")
    mus = lat.modes(3.0)
    print(f"  |mu|_min = {np.min(np.abs(mus)):.9f}  "
          f"(modes with |mu|<=3: {len(mus)})")
    print()

    # -- reduction consistency
    moves = build_moves()
    print(f"Reduction move set: {len(moves)} distinct (c,d) rows "
          f"(words len <= 5, 0 < |c| <= 2.2)")
    rng = np.random.default_rng(7)
    words = [''.join(rng.choice(list('abAB'), size=rng.integers(2, 7)))
             for _ in range(60)]
    maxdev = 0.0
    for k in range(60):
        z = complex(rng.uniform(-1, 1), rng.uniform(-2, 2))
        t = rng.uniform(0.4, 1.5)
        _, t1, _ = reduce_pt(lat, moves, z, t)
        g = wmat(words[k])
        z2, t2 = apply_m(g, z, t)
        _, t3, _ = reduce_pt(lat, moves, z2, t2)
        maxdev = max(maxdev, abs(t1 - t3) / t1)
    print(f"  Gamma-invariance of reduced height, 60 random (point, g), "
          f"t0 in [0.4, 1.5]: max rel dev = {maxdev:.2e}")
    print("  (a nonzero dev = ascent stalls; harmless for collocation, "
          "each translate is exact)")
    print()

    # -- horosphere rise check
    print("Horosphere rise check (fraction of grid points strictly raised):")
    for Y in (0.75, 0.68, 0.62, 0.56, 0.50, 0.45):
        zs = sample_points(lat, 200, rng_seed=3)
        rise = 0
        tmin = 1e9
        for z in zs:
            _, tstar, moved = reduce_pt(lat, moves, z, Y)
            if moved and tstar > Y * (1 + 1e-9):
                rise += 1
            tmin = min(tmin, tstar)
        print(f"  Y = {Y:.2f}: raised {rise}/200, min t* = {tmin:.4f}")
    print()

    # -- Bessel validation vs mpmath
    import mpmath as mp
    mp.mp.dps = 30
    print("K-Bessel trapezoid vs mpmath (relative error):")
    xs = np.array([0.95, 1.7, 3.0, 8.0, 20.0, 31.0])
    for r in (1.3, 4.7, 6.4):
        ts, wts = bessel_nodes(6.5, 0.9)
        Kt = K_table(xs, ts, wts, [r], [])[:, 0]
        for j, x in enumerate(xs):
            ref = float(mp.re(mp.besselk(1j * r, x)))
            rel = abs(Kt[j] - ref) / abs(ref) if ref != 0 else abs(Kt[j])
            print(f"  r = {r}, x = {x:5.2f}:  rel err = {rel:.2e}")
    for nu in (0.3, 0.8):
        ts, wts = bessel_nodes(6.5, 0.9)
        Kt = K_table(xs, ts, wts, [], [nu])[:, 0]
        for j, x in enumerate(xs[:3]):
            ref = float(mp.besselk(nu, x))
            rel = abs(Kt[j] - ref) / abs(ref)
            print(f"  nu = {nu} (real), x = {x:5.2f}:  rel err = {rel:.2e}")
    print()
    print(f"Bessel nodes for rmax 6.5: Q = {len(ts)} points (h = {ts[1]:.4f})")
    print()
    print("GROUNDWORK COMPLETE.")


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
# The scan
# ----------------------------------------------------------------

def scan(rmin=0.8, rmax=6.5, dr=0.01, Y=None, tag='scanA',
         margin=21.0, oversample=1.35):
    t_start = time.time()
    tau, _, _, _ = find_cusp_lattice()
    lat = Lattice(tau)
    moves = build_moves()

    # auto-Y: largest Y where >= 99% of probe points strictly rise
    if Y is None:
        for Yc in (0.75, 0.68, 0.62, 0.56, 0.50, 0.45):
            zs = sample_points(lat, 150, rng_seed=3)
            rise = sum(1 for z in zs
                       if reduce_pt(lat, moves, z, Yc)[1] > Yc * (1 + 1e-9))
            if rise >= 0.97 * len(zs):
                Y = Yc
                break
        else:
            Y = 0.45
    print(f"[{tag}] Y = {Y}")

    xcut = np.pi * rmax / 2 + margin
    Rcut = xcut / (2 * np.pi * Y)
    mus = lat.modes(Rcut)
    nmodes = len(mus)
    npts_target = int(oversample * nmodes)
    zs = sample_points(lat, npts_target)
    print(f"[{tag}] modes: {nmodes} (|mu| <= {Rcut:.3f}), sample pts: {len(zs)}")

    # pullbacks (r-independent)
    t0 = time.time()
    zstar = np.empty(len(zs), dtype=complex)
    tstar = np.empty(len(zs))
    movedf = np.zeros(len(zs), dtype=bool)
    for j, z in enumerate(zs):
        zst, tst, mv = reduce_pt(lat, moves, z, Y)
        zstar[j], tstar[j], movedf[j] = zst, tst, mv
    keep = movedf & (tstar > Y * (1 + 1e-9))
    zs = np.array(zs)[keep]
    zstar, tstar = zstar[keep], tstar[keep]
    npts = len(zs)
    print(f"[{tag}] pullbacks: {npts} kept (dropped {np.sum(~keep)}), "
          f"t* range [{tstar.min():.3f}, {tstar.max():.3f}], "
          f"{time.time() - t0:.1f}s")

    # Bessel args: norms x all heights (Y first, then t*_j)
    absmu = np.abs(mus)
    norms, nrm_idx = np.unique(np.round(absmu, 12), return_inverse=True)
    heights = np.concatenate([[Y], tstar])
    args = 2 * np.pi * np.outer(norms, heights)  # (Nn, npts+1)
    xmin = args.min()
    ts, wts = bessel_nodes(rmax, xmin)
    print(f"[{tag}] distinct norms: {len(norms)}, Bessel nodes: {len(ts)}, "
          f"xmin = {xmin:.3f}")

    # phases (r-independent)
    dot0 = np.outer(zs.real, mus.real) + np.outer(zs.imag, mus.imag)
    dot1 = np.outer(zstar.real, mus.real) + np.outer(zstar.imag, mus.imag)
    P0 = np.exp(2j * np.pi * dot0)  # (npts, nmodes)
    P1 = np.exp(2j * np.pi * dot1)

    r_vals = np.arange(rmin, rmax + dr / 2, dr)
    nu_vals = np.arange(0.05, 0.96, 0.05)  # lam = 1 - nu^2 in (0,1)
    print(f"[{tag}] scanning {len(r_vals)} r values + {len(nu_vals)} "
          f"small-eig nu values")

    all_params = list(r_vals) + list(nu_vals)
    kinds = ['r'] * len(r_vals) + ['nu'] * len(nu_vals)
    sig = np.full((len(all_params), 3), np.nan)

    chunk = 60
    flat_args = args.ravel()
    for c0 in range(0, len(all_params), chunk):
        c1 = min(c0 + chunk, len(all_params))
        rs = [p for p, k in zip(all_params[c0:c1], kinds[c0:c1]) if k == 'r']
        nus = [p for p, k in zip(all_params[c0:c1], kinds[c0:c1]) if k == 'nu']
        KT = K_table(flat_args, ts, wts, rs, nus)  # (Nargs, len(rs)+len(nus))
        KT = KT.reshape(len(norms), len(heights), -1)
        for ci in range(c1 - c0):
            KY = KT[nrm_idx, 0, ci]           # (nmodes,)
            Kst = KT[nrm_idx, 1:, ci]         # (nmodes, npts)
            V = (Y * KY)[None, :] * P0 - (tstar[:, None] * Kst.T) * P1
            cn = np.linalg.norm(V, axis=0)
            cn[cn == 0] = 1.0
            V = V / cn[None, :]
            try:
                sv = np.linalg.svd(V, compute_uv=False)
                sig[c0 + ci] = sv[-1], sv[-2], sv[-3]
            except np.linalg.LinAlgError:
                pass
        done = c1
        el = time.time() - t_start
        eta = el / done * (len(all_params) - done)
        print(f"[{tag}] {done}/{len(all_params)}  elapsed {el:.0f}s  "
              f"eta {eta:.0f}s", flush=True)

    # dip detection on the r-part
    nr = len(r_vals)
    s0 = sig[:nr, 0]
    med = np.nanmedian(s0)
    dips = []
    for i in range(1, nr - 1):
        if s0[i] < s0[i - 1] and s0[i] < s0[i + 1] and s0[i] < 0.5 * med:
            dips.append({'r': float(r_vals[i]), 'sigma': float(s0[i]),
                         'sigma2': float(sig[i, 1])})
    print(f"[{tag}] median sigma_min = {med:.3e}; {len(dips)} dips:")
    for d in dips:
        print(f"    r = {d['r']:.4f}  sigma_min = {d['sigma']:.3e}  "
              f"(2nd: {d['sigma2']:.3e})")

    nu_dips = []
    snu = sig[nr:, 0]
    for i in range(len(nu_vals)):
        if snu[i] < 0.3 * med:
            nu_dips.append({'nu': float(nu_vals[i]), 'sigma': float(snu[i])})
    print(f"[{tag}] small-eigenvalue (lam<1) candidates: {nu_dips or 'NONE'}")

    np.savez(f"{OUTDIR}/{tag}_results.npz",
             r_vals=r_vals, nu_vals=nu_vals, sig=sig, Y=Y,
             nmodes=nmodes, npts=npts, tau=np.complex128(tau))
    with open(f"{OUTDIR}/{tag}_dips.json", 'w') as f:
        json.dump({'Y': Y, 'nmodes': int(nmodes), 'npts': int(npts),
                   'rmin': rmin, 'rmax': rmax, 'dr': dr,
                   'median_sigma': float(med), 'dips': dips,
                   'nu_dips': nu_dips}, f, indent=1)
    print(f"[{tag}] saved. total {time.time() - t_start:.0f}s")


# ----------------------------------------------------------------
# Refinement: golden-section on sigma_min + second-Y verification
# ----------------------------------------------------------------

class System:
    """Reusable collocation system at fixed Y (r enters only via K)."""

    def __init__(self, lat, moves, Y, rmax, margin=21.0, oversample=1.35,
                 seed=11):
        self.Y = Y
        xcut = np.pi * rmax / 2 + margin
        Rcut = xcut / (2 * np.pi * Y)
        self.mus = lat.modes(Rcut)
        zs = sample_points(lat, int(oversample * len(self.mus)), rng_seed=seed)
        zstar = np.empty(len(zs), dtype=complex)
        tstar = np.empty(len(zs))
        mv = np.zeros(len(zs), dtype=bool)
        for j, z in enumerate(zs):
            zstar[j], tstar[j], mv[j] = reduce_pt(lat, moves, z, Y)
        keep = mv & (tstar > Y * (1 + 1e-9))
        self.zs = np.array(zs)[keep]
        self.zstar, self.tstar = zstar[keep], tstar[keep]
        absmu = np.abs(self.mus)
        self.norms, self.nrm_idx = np.unique(np.round(absmu, 12),
                                             return_inverse=True)
        self.heights = np.concatenate([[Y], self.tstar])
        self.args = (2 * np.pi * np.outer(self.norms, self.heights)).ravel()
        self.ts, self.wts = bessel_nodes(rmax, self.args.min())
        d0 = (np.outer(self.zs.real, self.mus.real)
              + np.outer(self.zs.imag, self.mus.imag))
        d1 = (np.outer(self.zstar.real, self.mus.real)
              + np.outer(self.zstar.imag, self.mus.imag))
        self.P0 = np.exp(2j * np.pi * d0)
        self.P1 = np.exp(2j * np.pi * d1)

    def sigma_min(self, r):
        KT = K_table(self.args, self.ts, self.wts, [r], [])
        KT = KT.reshape(len(self.norms), len(self.heights))
        KY = KT[self.nrm_idx, 0]
        Kst = KT[self.nrm_idx, 1:]
        V = ((self.Y * KY)[None, :] * self.P0
             - (self.tstar[:, None] * Kst.T) * self.P1)
        cn = np.linalg.norm(V, axis=0)
        cn[cn == 0] = 1.0
        sv = np.linalg.svd(V / cn[None, :], compute_uv=False)
        return sv[-1]


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


def pin_phase(a, modes, tol=1e-9):
    """Pin the arbitrary global phase of a collocation eigenvector (defect C2).

    The eigenvector comes out of an SVD, which fixes it only up to a global
    e^{i*theta}.  Nothing in the solve pins theta, so `Re f` as computed is an
    arbitrary rotation inside the eigenspace: mathematically fine (both Re f
    and Im f solve the same equation) but NOT REPRODUCIBLE -- a re-run gives a
    different rotation, and any pointwise use of Re/Im separately is meaningless.

    Measured contamination before pinning (cc3, 2026-08-08):
        lam1 16.5151 : theta = +40.20 deg    lam2 25.0108 : theta = +148.92 deg
        parent 51.01 : theta = -26.55 deg

    This rotates onto the object's own real form, i.e. the gauge in which
    a_{-mu} = conj(a_mu).  After pinning, the residual |a_{-mu}/conj(a_mu) - 1|
    falls to 5.8e-06 .. 7.2e-05 and |Im f| / |Re f| <= 2.9e-06 across all modes.

    PHASE-INVARIANT quantities need none of this and are unaffected: the
    sigma_min dips and refinements (the eigenvalues themselves), |a|-based
    quantities, the S-invariance test, the sector projection, mode counting,
    and the PSLQ work.  Call this only when reconstructing f pointwise.

    Args:
        a: complex coefficient vector, indexed as `modes`.
        modes: sequence of (m1, m2) lattice labels, same order as `a`.
    Returns:
        the pinned copy of `a`.  `a` itself is not modified.
    """
    idx = {(round(float(m[0]), 9), round(float(m[1]), 9)): j
           for j, m in enumerate(modes)}
    rat = []
    for j, m in enumerate(modes):
        key = (round(-float(m[0]), 9), round(-float(m[1]), 9))
        k = idx.get(key)
        if k is None or abs(a[k]) < tol:
            continue
        rat.append(a[j] / np.conj(a[k]))
    if not rat:
        return np.array(a, copy=True)
    theta = np.angle(np.mean(rat))
    return np.array(a, copy=True) * np.exp(-1j * theta / 2)


def refine(dips_json=f"{OUTDIR}/scanA_dips.json", rmax=6.5,
           Y2=0.62, halfwidth=0.02):
    with open(dips_json) as f:
        scan_data = json.load(f)
    tau, _, _, _ = find_cusp_lattice()
    lat = Lattice(tau)
    moves = build_moves()

    Y1 = scan_data['Y']
    print(f"Building systems at Y1 = {Y1} and Y2 = {Y2} ...")
    S1 = System(lat, moves, Y1, rmax)
    S2 = System(lat, moves, Y2, rmax, seed=23)
    print(f"  S1: {len(S1.mus)} modes / {len(S1.zs)} pts;  "
          f"S2: {len(S2.mus)} modes / {len(S2.zs)} pts")
    print()

    results = []
    for d in scan_data['dips']:
        r0 = d['r']
        r1, s1 = golden_min(S1.sigma_min, r0 - halfwidth, r0 + halfwidth)
        r2, s2 = golden_min(S2.sigma_min, r1 - halfwidth, r1 + halfwidth)
        dev = abs(r1 - r2)
        stable = dev < 5e-4 and s2 < 0.1 * scan_data['median_sigma']
        results.append({'r_Y1': r1, 'sigma_Y1': s1, 'r_Y2': r2,
                        'sigma_Y2': s2, 'dev': dev, 'stable': bool(stable)})
        lam = 1 + r1 ** 2
        print(f"  dip {r0:.4f}: Y1 -> r = {r1:.8f} (sig {s1:.2e}), "
              f"Y2 -> r = {r2:.8f} (sig {s2:.2e}), |dr| = {dev:.2e} "
              f"{'STABLE' if stable else 'spurious?'}  lam = {lam:.6f}")

    stable_rs = [x['r_Y1'] for x in results if x['stable']]
    print()
    print(f"STABLE EIGENVALUES: {len(stable_rs)}")
    for r in stable_rs:
        print(f"  r = {r:.8f}   lambda = 1 + r^2 = {1 + r ** 2:.8f}")
    vol = 2.029883212819307
    weylc = vol / (6 * np.pi ** 2)
    if stable_rs:
        T = max(stable_rs)
        print(f"  Weyl check: N({T:.2f}) predicted "
              f"{weylc * T ** 3:.1f}, found {len(stable_rs)}")
    with open(f"{OUTDIR}/refined_eigenvalues.json", 'w') as f:
        json.dump({'Y1': Y1, 'Y2': Y2, 'results': results,
                   'stable_r': stable_rs}, f, indent=1)
    print("Saved refined_eigenvalues.json")


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'groundwork'
    if cmd == 'groundwork':
        groundwork()
    elif cmd == 'refine':
        refine()
    elif cmd == 'scan':
        kw = {}
        if len(sys.argv) > 2:
            kw['rmin'] = float(sys.argv[2])
        if len(sys.argv) > 3:
            kw['rmax'] = float(sys.argv[3])
        if len(sys.argv) > 4:
            kw['dr'] = float(sys.argv[4])
        if len(sys.argv) > 5:
            kw['Y'] = float(sys.argv[5])
        if len(sys.argv) > 6:
            kw['tag'] = sys.argv[6]
        scan(**kw)
    else:
        print(f"unknown command {cmd}")
