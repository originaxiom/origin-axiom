"""B1667 -- THE CANONICAL CUSP (sealed instrument; one run).  Point P-185.

The fibre is the torus C/(Z + tau Z) with one puncture at z = 0. Its complete hyperbolic metric is the uniformisation:
the developing map w = y2/y1 of  y'' + (P(z)/4 + c) y = 0  (P = Weierstrass p), with the accessory parameter c = c(tau)
fixed by requiring real monodromy (a Fuchsian once-punctured torus group). Conjugate the monodromy into SL(2,R) with the
puncture's parabolic u -> u + lam fixing infinity and the surface in the upper half-plane. Near the puncture
u(z) = -(i lam / 2 pi) log z + B + O(z^2), so the horocycle Im u = h is |z| = exp(-(2 pi / lam)(h - Im B)) to leading order,
and the end radius L = log(1/eps) of B1654 is fixed by a canonical h:
  L_max(tau) = (2 pi / lam)(h_max - Im B),  h_max = 1/min|c_gamma|  (the maximal embedded cusp neighbourhood),
  L_2(tau)   = pi - (2 pi / lam) Im B        (the horocycle of length 2).
Both are invariant under the remaining real conjugations.
"""
import os
for _v in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")                    # the CPU rule: one BLAS thread per worker
import numpy as np
from itertools import product
from scipy.integrate import solve_ivp


# ---------------- theta functions and Weierstrass p for the lattice Z + tau Z ----------------
def thetas(v, tau, N=10):
    q = np.exp(1j * np.pi * tau)
    n = np.arange(N)
    t1 = 2 * np.sum((-1) ** n * q ** ((n + 0.5) ** 2) * np.sin((2 * n + 1) * v))
    t2 = 2 * np.sum(q ** ((n + 0.5) ** 2) * np.cos((2 * n + 1) * v))
    m = np.arange(1, N)
    t3 = 1 + 2 * np.sum(q ** (m ** 2) * np.cos(2 * m * v))
    t4 = 1 + 2 * np.sum((-1) ** m * q ** (m ** 2) * np.cos(2 * m * v))
    return t1, t2, t3, t4


class Lattice:
    def __init__(self, tau):
        self.tau = complex(tau)
        _, t2, t3, t4 = thetas(0.0, self.tau)
        self.t20, self.t30, self.t40 = t2, t3, t4
        self.e1 = (np.pi ** 2 / 3) * (t3 ** 4 + t4 ** 4)

    def wp(self, z):
        n = np.round(z.imag / self.tau.imag); z = z - n * self.tau      # P is doubly periodic: reduce to the central cell
        z = z - np.round(z.real)
        t1, t2, _, _ = thetas(np.pi * z, self.tau)
        return (np.pi * self.t30 * self.t40 * t2 / t1) ** 2 + self.e1


# ---------------- the ODE along a straight path ----------------
def transfer_path(lat, c, zf, dzf, y0, rtol=1e-12, atol=1e-14):
    """Continue the data y0 = (y, y') along z = zf(t), t in [0, 1], with dz/dt = dzf(t)."""
    def rhs(t, Y):
        z, d = zf(t), dzf(t)
        Q = 0.25 * lat.wp(z) + c
        return [d * Y[1], -d * Q * Y[0]]
    sol = solve_ivp(rhs, (0.0, 1.0), np.asarray(y0, dtype=complex), method="DOP853", rtol=rtol, atol=atol)
    assert sol.success, sol.message
    return sol.y[:, -1]


def transfer(lat, c, z_from, z_to, y0, rtol=1e-12, atol=1e-14):
    """Continue the solution with data y0 = (y, y') from z_from to z_to along the segment."""
    d = z_to - z_from
    return transfer_path(lat, c, lambda t: z_from + t * d, lambda t: d, y0, rtol, atol)


def fundamental_path(lat, c, zf, dzf):
    a = transfer_path(lat, c, zf, dzf, [1, 0]); b = transfer_path(lat, c, zf, dzf, [0, 1])
    return np.array([[a[0], b[0]], [a[1], b[1]]])


def puncture_loop(lat, c, z0, eps):
    """The data-transfer of the loop: z0 -> zs (on the ray toward 0) -> once round |z| = |zs| -> back to z0."""
    zs = eps * z0 / abs(z0)
    T1 = fundamental(lat, c, z0, zs)
    T2 = fundamental_path(lat, c, lambda t: zs * np.exp(2j * np.pi * t), lambda t: 2j * np.pi * zs * np.exp(2j * np.pi * t))
    T3 = fundamental(lat, c, zs, z0)
    return T3 @ T2 @ T1


def fundamental(lat, c, z_from, z_to):
    """T with columns = the continued data of the two standard solutions (initial data e1, e2 at z_from)."""
    a = transfer(lat, c, z_from, z_to, [1, 0])
    b = transfer(lat, c, z_from, z_to, [0, 1])
    return np.array([[a[0], b[0]], [a[1], b[1]]])


def mobius_of(T):
    """The Mobius matrix by which w = y2/y1 transforms when the solutions are continued by T."""
    A = np.array([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
    return A / np.sqrt(np.linalg.det(A))


def monodromy(tau, c, z0=None):
    lat = Lattice(tau)
    if z0 is None:
        z0 = 0.5 + 0.5 * lat.tau
    Ta = fundamental(lat, c, z0, z0 + 1)
    Tb = fundamental(lat, c, z0, z0 + lat.tau)
    return lat, z0, mobius_of(Ta), mobius_of(Tb)


def traces(Aa, Ab):
    return np.trace(Aa), np.trace(Ab), np.trace(Aa @ Ab)


# ---------------- the accessory parameter ----------------
def solve_accessory(tau, c0=0.0, tol=1e-12, maxit=40):
    """Newton on c (complex) for Im tr A_a = Im tr A_b = 0."""
    def F(c):
        _, _, Aa, Ab = monodromy(tau, c)
        ta, tb, _ = traces(Aa, Ab)
        return np.array([ta.imag, tb.imag])
    c = complex(c0)
    for _ in range(maxit):
        f = F(c)
        if np.max(np.abs(f)) < tol:
            return c, f
        h = 1e-6
        J = np.column_stack([(F(c + h) - f) / h, (F(c + 1j * h) - f) / h])
        dx = np.linalg.solve(J, -f)
        c = c + dx[0] + 1j * dx[1]
    return c, F(c)


# ---------------- normalisation into SL(2,R) with the cusp at infinity ----------------
def apply(M, w):
    return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])


def fixed_points(M):
    a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    disc = np.sqrt((a - d) ** 2 + 4 * b * cc)
    return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)


def normalise(Aa, Ab, P, w_base=0.0):
    fp = fixed_points(P)
    p = 0.5 * (fp[0] + fp[1])                       # the parabolic's double fixed point
    f1, f2 = fixed_points(Aa)
    # the Mobius map g sending (p, f1, f2) to (inf, 0, 1): the invariant circle goes to R
    g = np.array([[1.0, -f1], [1.0, -p]], dtype=complex)
    s = apply(g, f2)
    g = np.array([[1.0 / s, -f1 / s], [1.0, -p]], dtype=complex)
    g = g / np.sqrt(np.linalg.det(g))
    if apply(g, w_base).imag < 0:                    # put the surface in the upper half-plane
        g = np.array([[1j, 0], [0, -1j]]) @ g        # u -> -u
    conj = lambda M: g @ M @ np.linalg.inv(g)
    Ra, Rb, RP = conj(Aa), conj(Ab), conj(P)
    RP = RP / RP[0, 0]
    lam = RP[0, 1]
    return g, Ra, Rb, RP, lam


def min_c(Ra, Rb, maxlen=8):
    gens = [Ra, Rb, np.linalg.inv(Ra), np.linalg.inv(Rb)]
    inv = {0: 2, 1: 3, 2: 0, 3: 1}
    best = np.inf
    frontier = [(np.eye(2, dtype=complex), -1)]
    for _ in range(maxlen):
        nxt = []
        for M, last in frontier:
            for k in range(4):
                if last >= 0 and inv[k] == last:
                    continue
                N = M @ gens[k]
                if abs(N[1, 0]) > 1e-9 * max(1.0, abs(N[0, 0])):
                    best = min(best, abs(N[1, 0]))
                nxt.append((N, k))
        frontier = nxt
    return best


# ---------------- the local solution at the puncture (Frobenius) ----------------
def wp_laurent(lat, nmax=60):
    """p(z) = 1/z^2 + sum_{n>=1} a_n z^{2n}, from g2, g3 (e1, e2, e3 by theta constants, periods 1 and tau)."""
    t2, t3, t4 = lat.t20, lat.t30, lat.t40
    k = np.pi ** 2 / 3
    e1, e2, e3 = k * (t3 ** 4 + t4 ** 4), k * (t2 ** 4 - t4 ** 4), -k * (t2 ** 4 + t3 ** 4)
    g2, g3 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2), 4 * e1 * e2 * e3
    a = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, nmax + 1):
        a[n] = 3.0 / ((2 * n + 3) * (n - 2)) * sum(a[m] * a[n - 1 - m] for m in range(1, n - 1))
    return a


def frobenius(lat, c, M=120):
    """alpha_m, beta_m with y1 = z^{1/2} sum alpha_m z^m, y2 = y1 log z + z^{1/2} sum beta_m z^m (beta_0 = 0)."""
    a = wp_laurent(lat, M // 2 + 2)
    Q = np.zeros(M + 1, dtype=complex); Q[0] = c
    for n in range(1, M // 2 + 1):
        if 2 * n <= M:
            Q[2 * n] = a[n] / 4
    al = np.zeros(M + 1, dtype=complex); be = np.zeros(M + 1, dtype=complex); al[0] = 1.0
    for m in range(1, M + 1):
        sa = sum(Q[j] * al[m - 2 - j] for j in range(0, m - 1))
        al[m] = -sa / m ** 2
        sb = sum(Q[j] * be[m - 2 - j] for j in range(0, m - 1))
        be[m] = -(2 * m * al[m] + sb) / m ** 2
    return al, be


def g_local(al, be, z):
    zp = z ** np.arange(len(al))
    return np.dot(be, zp) / np.dot(al, zp)


def local_B(lat, c, z0, g, lam, al, be, eps=0.05):
    """Im B in u(z) = -(i lam/2pi)(log z + g(z)) + B, matched exactly at z_s on the ray (no O(z^2) neglect)."""
    zs = eps * z0 / abs(z0)
    a = transfer(lat, c, z0, zs, [1, 0]); b = transfer(lat, c, z0, zs, [0, 1])
    u = apply(g, b[0] / a[0])
    return u.imag + (lam / (2 * np.pi)) * (np.log(abs(zs)) + g_local(al, be, zs).real)


def horocycle_radius(al, be, Lh, theta, r_hi):
    """r(theta) solving log(1/r) - Re g(r e^{i theta}) = Lh (the horoball is r < r(theta)); bisection in log r."""
    lo, hi = np.log(1e-12), np.log(r_hi)
    f = lambda s: -s - g_local(al, be, np.exp(s + 1j * theta)).real - Lh
    if f(hi) > 0:
        return None                                   # the horocycle does not close inside r_hi on this ray
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return np.exp(0.5 * (lo + hi))


# ---------------- the channel norms outside the canonical horoball (B1654's profiles and quadrature) ----------------
import importlib.util, pathlib as _pl
_B1654 = sorted(_pl.Path(__file__).resolve().parents[3].glob("frontier/B1654_*/verification/the_norm_of_the_boundary_class.py"))[0]
_spec = importlib.util.spec_from_file_location("b1654", _B1654); b1654 = importlib.util.module_from_spec(_spec)
_src = _B1654.read_text()
_src = _src[:_src.index("# ---------------------------------------------------------------- route B")]   # route A and helpers only
_src = _src.replace("def thetas(z, tau):", "K = 40\ndef thetas(z, tau):", 1)
exec(compile(_src, str(_B1654), "exec"), b1654.__dict__)


def voronoi(tau):
    """The Dirichlet cell of 0 for Z + tau Z: (vertex angles with wrap, rmax(theta)) from the six neighbours' bisectors."""
    tau = complex(tau)
    assert abs(tau.real) <= 0.5 + 1e-12 and abs(tau) >= 1 - 1e-12, f"voronoi() needs a reduced tau, got {tau}"
    V = [1, -1, tau, -tau, tau - 1, 1 - tau, tau + 1, -tau - 1]
    def rmax(th):
        th = np.asarray(th, dtype=float); e = np.exp(1j * th)
        best = np.full(th.shape, np.inf)
        for v in V:
            den = (e * np.conj(v)).real
            val = np.where(den > 1e-14, (abs(v) ** 2 / 2) / np.where(den > 1e-14, den, 1.0), np.inf)
            best = np.minimum(best, val)
        return best
    # vertices: intersections of bisectors that lie on the cell boundary
    verts = []
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            a, b = V[i], V[j]
            A = np.array([[a.real, a.imag], [b.real, b.imag]])
            if abs(np.linalg.det(A)) < 1e-12:
                continue
            x = np.linalg.solve(A, [abs(a) ** 2 / 2, abs(b) ** 2 / 2]); z = x[0] + 1j * x[1]
            th = np.angle(z)
            if abs(abs(z) - rmax(np.array([th]))[0]) < 1e-9:
                verts.append(float(np.mod(th, 2 * np.pi)))
    br = sorted(set(round(v, 12) for v in verts))
    return br + [br[0] + 2 * np.pi], rmax


def horoball_norms(tau, al, be, Lh, nth=96, ns=64):
    """N_r = int over the Dirichlet cell minus the horoball {log(1/r) - Re g > Lh} of |S_r|^2 dA, r = 2, 3, 4 (B1654's S_r).
    Also returns the embedding margin min_theta (rmax(theta) - r_h(theta)) (>= 0 iff the horoball stays in the cell)."""
    from numpy.polynomial.legendre import leggauss
    tau = complex(tau)
    br, rmaxf = voronoi(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns)
    tot = {2: 0.0, 3: 0.0, 4: 0.0}; margin = np.inf
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a); wt = 0.5 * (b - a) * wg
        rmax = rmaxf(th)
        rh = [horocycle_radius(al, be, Lh, t, min(0.95, 1.1 * rm)) for t, rm in zip(th, rmax)]
        if any(v is None for v in rh):
            raise RuntimeError(f"the horocycle does not close inside the cell at tau = {tau}")
        rh = np.array(rh, dtype=float)
        margin = min(margin, float(np.min(rmax - rh)))
        s_hi = np.log(rmax); s_lo = np.log(np.minimum(rh, rmax))
        s = 0.5 * (s_hi - s_lo)[:, None] * xs[None, :] + 0.5 * (s_hi + s_lo)[:, None]
        wsr = 0.5 * (s_hi - s_lo)[:, None] * ws[None, :]
        rr = np.exp(s); z = rr * np.exp(1j * th)[:, None]
        for r in (2, 3, 4):
            tot[r] += float(np.sum(wt[:, None] * wsr * np.abs(b1654.S_A(r, z, tau)) ** 2 * rr ** 2))
    return tot, margin


def canonical_lift(tau, Lh, al, be, nth=96, ns=64):
    N, margin = horoball_norms(tau, al, be, Lh, nth, ns)
    R = b1654.R_A(complex(tau))
    num = abs(sum(N[r] * R[r] ** 2 for r in (2, 3, 4)))
    den = sum(N[r] * abs(R[r]) ** 2 for r in (2, 3, 4))
    return num / den, N, margin


def track(tau_target, start=(1j, 0.0), step=0.04):
    """Follow the uniformising accessory parameter from a symmetric point (where c = 0 exactly) to tau_target:
    first off the symmetric locus by a small step in Re tau, then along Re tau, then along Im tau."""
    t0, c = complex(start[0]), complex(start[1])
    tgt = complex(tau_target)
    nudge = 0.03 if tgt.real >= t0.real else -0.03
    waypoints = [t0 + nudge, complex(tgt.real, t0.imag), tgt]
    cur = t0
    for wpnt in waypoints:
        n = max(1, int(np.ceil(abs(wpnt - cur) / step)))
        for k in range(1, n + 1):
            tau_k = cur + (wpnt - cur) * k / n
            c, res = solve_accessory(tau_k, c)
            if np.max(np.abs(res)) > 1e-9:
                raise RuntimeError(f"continuation lost at tau = {tau_k}: residual {np.max(np.abs(res)):.1e}")
        cur = wpnt
    return c


def uniformisation_check(tau, c, g, npts=7):
    """Im u > 0 at sample points of the cell (the developing image of the uniformisation lies in H)."""
    lat = Lattice(tau); z0 = 0.5 + 0.5 * lat.tau
    worst = np.inf
    for i in range(npts):
        for j in range(npts):
            z = (i + 0.5) / npts * 1.0 + (j + 0.5) / npts * lat.tau - 0.5 * (1 + lat.tau) + 1e-3
            if abs(z) < 0.08:
                continue
            a = transfer(lat, c, z0, z0 + z, [1, 0]); b = transfer(lat, c, z0, z0 + z, [0, 1])
            worst = min(worst, apply(g, b[0] / a[0]).imag)
    return worst


# ================================================================ THE RUN (cells as sealed in PREREGISTRATION.md)
import json, time, pathlib, traceback
from multiprocessing import Pool

HERE = pathlib.Path(__file__).resolve().parent
OMEGA6 = np.exp(1j * np.pi / 3)                      # the hexagonal lattice Z + e^{i pi/3} Z, the point tau = omega + 1
L_MAX_ETA, L_2_ETA = 0.69208004049, 2.78647514288    # the eta^4 closed form at omega (disclosed control)
XS = (0.05, 0.15, 0.25, 0.35, 0.45)
YS = (0.95, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0)
YS_EXT = (3.25, 3.5, 3.75, 4.0)                      # column 0.25 only: the cusp of moduli
DS = (0.02, 0.05, 0.1, 0.2)                          # the ray omega6 + d e^{2 pi i/3} into the domain


def point(tau, c, fine=False):
    tau = complex(tau); c = complex(c)
    lat, z0, Aa, Ab = monodromy(tau, c)
    P0 = mobius_of(puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = normalise(Aa, Ab, P0)
    lam_signed = float(lam.real); lam = abs(lam.real)
    mc8 = min_c(Ra, Rb, 8); mc6 = min_c(Ra, Rb, 6)
    al, be = frobenius(lat, c)
    ib = [float(local_B(lat, c, z0, g, lam, al, be, e)) for e in (0.1, 0.05)]
    h_max = 1.0 / mc8
    L_max = (2 * np.pi / lam) * (h_max - ib[1]); L_2 = np.pi - (2 * np.pi / lam) * ib[1]
    rho_max, N_max, m_max = canonical_lift(tau, L_max, al, be)
    rho_2, N_2, m_2 = canonical_lift(tau, L_2, al, be)
    x, y, z = (abs(t) for t in traces(Aa, Ab))
    R = b1654.R_A(tau); cr = {k: b1654.cA(k, tau, 1e-4) for k in (2, 3, 4)}
    f = abs(sum(cr[k] * R[k] ** 2 for k in (2, 3, 4))) / b1654.nR2(R)
    out = dict(tau=[tau.real, tau.imag], c=[c.real, c.imag], traces=[x, y, z],
               markov=float(abs(x * x + y * y + z * z - x * y * z) / (x * y * z)), trP0=[np.trace(P0).real, np.trace(P0).imag],
               realness=float(max(np.max(np.abs(Ra.imag)), np.max(np.abs(Rb.imag)))), lam=lam, lam_signed=lam_signed, minc6=float(mc6),
               minc8=float(mc8), cusp_area=float(lam * mc8), imB=ib, L_max=float(L_max), L_2=float(L_2),
               uniformisation=float(uniformisation_check(tau, c, g, npts=4)), margin_max=m_max, margin_2=m_2,
               rho_max=float(rho_max), rho_2=float(rho_2), N_max=N_max, N_2=N_2, f=float(f))
    if fine:
        out["rho_2_fine"] = float(canonical_lift(tau, L_2, al, be, nth=144, ns=96)[0])
    return out


def newton_walk(tau_from, c, tau_to, step=0.04):
    n = max(1, int(np.ceil(abs(tau_to - tau_from) / step)))
    for k in range(1, n + 1):
        tk = tau_from + (tau_to - tau_from) * k / n
        c, res = solve_accessory(tk, c)
        if np.max(np.abs(res)) > 1e-9:
            raise RuntimeError(f"continuation lost at tau = {tk}: residual {np.max(np.abs(res)):.1e}")
    return c, float(np.max(np.abs(res)))


def chain(task):
    kind, arg = task
    out = []
    try:
        if kind == "controls":
            for tau in (1j, OMEGA6):
                r = point(tau, 0.0); r["residual"] = 0.0; r["where"] = "control"; out.append(r)
        elif kind == "column":
            x = arg
            ys = [y for y in YS if abs(complex(x, y)) >= 1.03] + (list(YS_EXT) if abs(x - 0.25) < 1e-9 else [])
            tau = complex(x, ys[0]); c = track(tau)
            c, res = solve_accessory(tau, c)
            for k, y in enumerate(ys):
                if k:
                    c, res = newton_walk(tau, c, complex(x, y))
                    tau = complex(x, y)
                r = point(tau, c, fine=(abs(x - 0.25) < 1e-9 and y >= 2.0)); r["residual"] = float(np.max(np.abs(res)))
                r["where"] = "grid"; out.append(r)
        elif kind == "omega":
            direction = np.exp(2j * np.pi / 3); tau, c = OMEGA6, 0.0
            for d in DS:
                tgt = OMEGA6 + d * direction
                c, res = newton_walk(tau, c, tgt, step=0.005); tau = tgt
                r = point(tau, c); r["residual"] = res; r["where"] = f"omega ray d={d}"; r["d"] = d; out.append(r)
    except Exception:
        out.append({"failure": traceback.format_exc(), "task": [kind, str(arg)]})
    return out


def main():
    t0 = time.time()
    LOG = []
    def say(*a):
        line = " ".join(str(x) for x in a); print(line, flush=True); LOG.append(line)
    tasks = [("controls", None)] + [("column", x) for x in XS] + [("omega", None)]
    with Pool(processes=7) as pool:
        results = pool.map(chain, tasks)
    pts = [r for rs in results for r in rs]
    fails = [r for r in pts if "failure" in r]
    pts = [r for r in pts if "failure" not in r]
    OUT = {"points": pts, "failures": fails}
    def dump():
        (HERE / "the_canonical_cusp.json").write_text(json.dumps(OUT, indent=1, default=lambda o: str(o)))
        (HERE / "the_canonical_cusp_run.txt").write_text("\n".join(LOG) + "\n")
    say(f"B1667 THE CANONICAL CUSP: {len(pts)} points, {len(fails)} failed tasks, {time.time() - t0:.0f} s")
    for r in fails:
        say("FAILED TASK", r["task"]); say(r["failure"])
    for r in pts:
        tau = complex(*r["tau"])
        say(f"  {r['where']:>18}  tau={tau.real:.3f}{tau.imag:+.3f}i  c={complex(*r['c']):.6f}  |tr|=({r['traces'][0]:.6f},{r['traces'][1]:.6f},{r['traces'][2]:.6f})"
            f"  area={r['cusp_area']:.6f}  L_max={r['L_max']:.6f}  L_2={r['L_2']:.6f}  rho_max={r['rho_max']:.4e}  rho_2={r['rho_2']:.4e}"
            f"  f={r['f']:.4e}  Im u_min={r['uniformisation']:.3e}  margins=({r['margin_max']:.2e},{r['margin_2']:.2e})")
    dump()

    grid = [r for r in pts if r["where"] == "grid"]
    ctrl = {round(complex(*r["tau"]).imag, 6): r for r in pts if r["where"] == "control"}
    ray = sorted([r for r in pts if r["where"].startswith("omega ray")], key=lambda r: r["d"])
    allp = grid + ray
    # ---------------- L0, the gate
    g = {}
    g["no failed task, every point present"] = (len(fails) == 0 and len(grid) == sum(
        len([y for y in YS if abs(complex(x, y)) >= 1.03]) + (len(YS_EXT) if abs(x - 0.25) < 1e-9 else 0) for x in XS)
        and len(ray) == len(DS) and len(ctrl) == 2)
    g["Newton residual <= 1e-9"] = all(r["residual"] <= 1e-9 for r in allp)
    g["|traces| > 2 and Markov <= 1e-8"] = all(min(r["traces"]) > 2 and r["markov"] <= 1e-8 for r in allp + list(ctrl.values()))
    g["tr P0 = -2 to 1e-7"] = all(abs(complex(*r["trP0"]) + 2) <= 1e-7 for r in allp + list(ctrl.values()))
    g["realness <= 1e-7"] = all(r["realness"] <= 1e-7 for r in allp + list(ctrl.values()))
    g["orientation: lam > 0 (the cusp's translation, signed)"] = all(r["lam_signed"] > 0 for r in allp + list(ctrl.values()))
    g["uniformisation: Im u > 0 on the sample"] = all(r["uniformisation"] > 0 for r in allp + list(ctrl.values()))
    g["Im B stable across matching radii to 1e-7"] = all(abs(r["imB"][0] - r["imB"][1]) <= 1e-7 for r in allp + list(ctrl.values()))
    g["min|c| at word length 6 = at 8 (1e-9)"] = all(abs(r["minc6"] - r["minc8"]) <= 1e-9 for r in allp + list(ctrl.values()))
    g["maximal horoball touches the cell: -1e-6 <= margin <= 2e-3"] = all(-1e-6 <= r["margin_max"] <= 2e-3 for r in allp + list(ctrl.values()))
    g["length-2 horocycle embedded: margin > 0"] = all(r["margin_2"] > 0 for r in allp + list(ctrl.values()))
    fine = [r for r in grid if "rho_2_fine" in r]
    g["quadrature: rho_2 at 144x96 vs 96x64 within 1e-3 (column 0.25, Im tau >= 2)"] = (len(fine) == 9 and all(
        abs(r["rho_2_fine"] / r["rho_2"] - 1) <= 1e-3 for r in fine))
    ci, co = ctrl.get(1.0), ctrl.get(round(OMEGA6.imag, 6))
    g["control i: traces (2 sqrt2, 2 sqrt2, 4), area 4 sqrt2 (1e-8)"] = (ci is not None and max(abs(a - b) for a, b in zip(
        sorted(ci["traces"]), sorted([2 * 2 ** .5, 2 * 2 ** .5, 4.0]))) <= 1e-8 and abs(ci["cusp_area"] - 4 * 2 ** .5) <= 1e-8)
    g["control omega: traces (3, 3, 6), area 6 (1e-8)"] = (co is not None and max(abs(a - b) for a, b in zip(
        sorted(co["traces"]), [3.0, 3.0, 6.0])) <= 1e-8 and abs(co["cusp_area"] - 6) <= 1e-8)
    g["control omega: L_max, L_2 = the eta^4 values (1e-6)"] = (co is not None and abs(co["L_max"] - L_MAX_ETA) <= 1e-6
        and abs(co["L_2"] - L_2_ETA) <= 1e-6)
    g["control omega: rho_can = 0 for both cuts (1e-10)"] = co is not None and co["rho_max"] <= 1e-10 and co["rho_2"] <= 1e-10
    OUT["L0"] = g; L0 = all(g.values())
    say(""); say("L0, the gate:", "HOLDS" if L0 else "FAILS")
    for k, v in g.items():
        say(f"   {'ok  ' if v else 'FAIL'} {k}")
    dump()
    if not L0:
        say("L0 failed: nothing after it is read as a result."); OUT["verdict_by_rule"] = "OPEN (gate)"; dump(); return
    # ---------------- T1
    T1 = all(0.2 < r["L_max"] < 2.0 and 1.5 < r["L_2"] < 4.5 for r in allp)
    OUT["T1"] = dict(holds=T1, L_max_range=[min(r["L_max"] for r in allp), max(r["L_max"] for r in allp)],
                     L_2_range=[min(r["L_2"] for r in allp), max(r["L_2"] for r in allp)])
    say(""); say("T1, the canonical radius is of order one (0.2 < L_max < 2, 1.5 < L_2 < 4.5 everywhere):", "HOLDS" if T1 else "FAILS",
        OUT["T1"]["L_max_range"], OUT["T1"]["L_2_range"])
    # ---------------- T2
    bulk = [r for r in grid if r["tau"][1] <= 1.5 + 1e-9 and abs(complex(*r["tau"]) - OMEGA6) >= 0.15]
    T2 = len(bulk) > 0 and all(r["rho_2"] >= 5e-3 and r["rho_max"] >= 5e-2 for r in bulk)
    OUT["T2"] = dict(holds=T2, n=len(bulk), rho_2_min=min(r["rho_2"] for r in bulk), rho_max_min=min(r["rho_max"] for r in bulk))
    say("T2, no hierarchy from the canonical cut in the bulk (rho_2 >= 5e-3, rho_max >= 5e-2):", "HOLDS" if T2 else "FAILS", OUT["T2"])
    # ---------------- T3
    d3 = [r for r in ray if r["d"] in (0.02, 0.05, 0.1)]
    sl3 = float(np.polyfit(np.log([r["d"] for r in d3]), np.log([r["rho_2"] for r in d3]), 1)[0])
    T3 = 0.75 <= sl3 <= 1.25
    OUT["T3"] = dict(holds=T3, slope=sl3, rho_2=[(r["d"], r["rho_2"]) for r in ray])
    say("T3, the zero at omega is simple (log-log slope of rho_2 in d over 0.02, 0.05, 0.1 in [0.75, 1.25]):", "HOLDS" if T3 else "FAILS", sl3)
    # ---------------- T4
    col = sorted([r for r in grid if abs(r["tau"][0] - 0.25) < 1e-9 and r["tau"][1] >= 2.0 - 1e-9 and
                  any(abs(r["tau"][1] - y) < 1e-9 for y in (2.0, 2.5, 3.0, 3.5, 4.0))], key=lambda r: r["tau"][1])
    sl4 = float(np.polyfit([r["tau"][1] for r in col], np.log([r["rho_2"] for r in col]), 1)[0])
    L2_35 = [r["L_2"] for r in col if abs(r["tau"][1] - 3.5) < 1e-9][0]; L2_40 = [r["L_2"] for r in col if abs(r["tau"][1] - 4.0) < 1e-9][0]
    T4 = (-3.6 <= sl4 <= -2.2) and abs(L2_40 - L2_35) < 0.05
    OUT["T4"] = dict(holds=T4, slope=sl4, L2_35=L2_35, L2_40=L2_40)
    say("T4, toward the cusp of moduli (slope of ln rho_2 in Im tau in [-3.6, -2.2]; |L_2(4) - L_2(3.5)| < 0.05):", "HOLDS" if T4 else "FAILS",
        sl4, L2_35, L2_40)
    # ---------------- read-outs (no criterion)
    c25 = sorted([r for r in grid if abs(r["tau"][0] - 0.25) < 1e-9], key=lambda r: r["tau"][1])
    OUT["readout"] = dict(
        column_025=[(r["tau"][1], r["L_max"], r["L_2"], r["rho_max"], r["rho_2"], r["f"]) for r in c25],
        leading_order_ratio=[(r["tau"], r["rho_2"] / (r["f"] / (2 * np.pi * r["L_2"])) if r["f"] > 0 else None) for r in grid],
        cusp_area_range=[min(r["cusp_area"] for r in allp), max(r["cusp_area"] for r in allp)])
    say(""); say("read-out, column Re tau = 0.25 (Im tau, L_max, L_2, rho_max, rho_2, f):")
    for row in OUT["readout"]["column_025"]:
        say("   " + "  ".join(f"{v:.6g}" for v in row))
    say("read-out, cusp area range:", OUT["readout"]["cusp_area_range"])
    OUT["verdict_by_rule"] = "PROVED" if (T1 and T2 and T3 and T4) else "NEGATIVE as sealed (a cell fails)"
    say(""); say("verdict by the rule:", OUT["verdict_by_rule"], f"({time.time() - t0:.0f} s)")
    dump()


if __name__ == "__main__":
    main()
