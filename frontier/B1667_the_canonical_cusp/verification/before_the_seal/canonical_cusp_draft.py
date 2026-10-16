"""P-185: the canonical end radius of the fibre's puncture (draft instrument; controls first).

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
import numpy as np
from itertools import product
from scipy.integrate import solve_ivp


# ---------------- theta functions and Weierstrass p for the lattice Z + tau Z ----------------
def thetas(v, tau, N=30):
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


# ---------------- the developing map near the puncture ----------------
def imB(lat, c, z0, g, lam, eps):
    """Im B from u(z) = -(i lam/2pi) log z + B + O(z^2), evaluated on the segment from z0 to z = eps (toward 0)."""
    zs = eps * z0 / abs(z0)
    a = transfer(lat, c, z0, zs, [1, 0])
    b = transfer(lat, c, z0, zs, [0, 1])
    w = b[0] / a[0]
    u = apply(g, w)
    return u.imag + (lam / (2 * np.pi)) * np.log(abs(zs))


def canonical(tau, c0=0.0, maxlen=8, eps=(0.02, 0.01), exact_c=None):
    if exact_c is None:
        c, res = solve_accessory(tau, c0)
    else:
        c, res = complex(exact_c), np.zeros(2)
    lat, z0, Aa, Ab = monodromy(tau, c)
    P0 = mobius_of(puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = normalise(Aa, Ab, P0)
    lam_r = abs(lam.real)
    mc = min_c(Ra, Rb, maxlen)
    h_max = 1.0 / mc
    ib = [imB(lat, c, z0, g, lam_r, e) for e in eps]
    L_max = (2 * np.pi / lam_r) * (h_max - ib[-1])
    L_2 = np.pi - (2 * np.pi / lam_r) * ib[-1]
    ta, tb, tab = traces(Aa, Ab)
    return dict(tau=tau, c=c, residual=float(np.max(np.abs(res))), traces=(ta, tb, tab),
                trP=np.trace(Aa @ Ab @ np.linalg.inv(Aa) @ np.linalg.inv(Ab)), trP0=np.trace(P0),
                lam=lam, realness=float(max(np.max(np.abs(Ra.imag)), np.max(np.abs(Rb.imag)))),
                cusp_area=lam_r * mc, h_max=h_max, imB=ib, L_max=L_max, L_2=L_2)


if __name__ == "__main__":
    for tau in (1j, np.exp(2j * np.pi / 3) + 1):     # tau = i and tau = omega + 1 ~ omega (the hexagonal lattice)
        r = canonical(tau)
        print(f"tau = {tau:.6f}")
        for k, v in r.items():
            if k != "tau":
                print(f"   {k}: {v}")


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
        rh = np.array([horocycle_radius(al, be, Lh, t, 0.999) for t in th], dtype=float)
        margin = min(margin, float(np.min(rmax - rh)))
        s_hi = np.log(rmax); s_lo = np.log(np.minimum(rh, rmax))
        s = 0.5 * (s_hi - s_lo)[:, None] * xs[None, :] + 0.5 * (s_hi + s_lo)[:, None]
        wsr = 0.5 * (s_hi - s_lo)[:, None] * ws[None, :]
        rr = np.exp(s); z = rr * np.exp(1j * th)[:, None]
        for r in (2, 3, 4):
            tot[r] += float(np.sum(wt[:, None] * wsr * np.abs(b1654.S_A(r, z, tau)) ** 2 * rr ** 2))
    return tot, margin


def canonical_lift(tau, Lh, al, be):
    N, margin = horoball_norms(tau, al, be, Lh)
    R = b1654.R_A(complex(tau))
    num = abs(sum(N[r] * R[r] ** 2 for r in (2, 3, 4)))
    den = sum(N[r] * abs(R[r]) ** 2 for r in (2, 3, 4))
    return num / den, N, margin


# ---------------- continuation from an exact symmetric root (the uniformising branch) ----------------
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
