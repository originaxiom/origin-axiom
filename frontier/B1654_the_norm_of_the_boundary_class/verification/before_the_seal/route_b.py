"""C1 exploration (main, unsealed): route B for c_r(tau), independent of route A's quadrature and theta code.
c_r = int_P (|S|^2 - 1/|z|^2 - 2 Re(s1 z/zbar)) dA + 2 Re(s1 * int e^{2i th} rmax^2/2 dth) + int log rmax dth,
P = {x + t tau : x, t in [-1/2, 1/2]}, product Gauss-Legendre in (x, t) split at x = 0 and t = 0; mpmath jtheta."""
import mpmath as mp
mp.mp.dps = 20
def make(tau):
    q = mp.exp(1j*mp.pi*tau); th1p = mp.jtheta(1, 0, q, 1)*mp.pi
    t0 = {r: mp.jtheta(r, 0, q) for r in (2, 3, 4)}
    S = lambda r, z: mp.jtheta(r, mp.pi*z, q)*th1p/(t0[r]*mp.jtheta(1, mp.pi*z, q))
    return q, th1p, t0, S
def s1_of(S, r):
    # S_r = 1/z + s1 z + ...: s1 = lim (S - 1/z)/z, from a symmetric small-circle average (a_1 coefficient)
    rho = mp.mpf('0.02'); N = 64
    return mp.fsum(S(r, rho*mp.expjpi(2*mp.mpf(k)/N))*mp.expjpi(-2*mp.mpf(k)/N) for k in range(N))/(N*rho)
def rmax(th, tau):
    d = mp.expj(th); y1 = mp.im(d)/mp.im(tau); x1 = mp.re(d) - y1*mp.re(tau)
    return mp.mpf(1)/2/max(abs(x1), abs(y1))
def c_r(r, tau, n=40):
    q, th1p, t0, S = make(tau); s1 = s1_of(S, r)
    xs, ws = zip(*[(x, w) for x, w in zip(*gl(n))])
    tot = mp.mpf(0)
    for (xa, xb) in [(-0.5, 0.0), (0.0, 0.5)]:
        for (ta, tb) in [(-0.5, 0.0), (0.0, 0.5)]:
            for xi, wi in zip(xs, ws):
                x = (xb-xa)/2*xi + (xb+xa)/2
                for tj, wj in zip(xs, ws):
                    t = (tb-ta)/2*tj + (tb+ta)/2
                    z = x + t*tau
                    f = abs(S(r, z))**2 - 1/abs(z)**2 - 2*mp.re(s1*z/mp.conj(z))
                    tot += wi*wj*(xb-xa)/2*(tb-ta)/2*f
    tot *= mp.im(tau)                                   # dA = Im(tau) dx dt
    # the vertex directions of P as breakpoints for the angular integrals
    verts = [(sx*0.5 + sy*0.5*tau) for sx in (1, -1) for sy in (1, -1)]
    br = sorted([mp.arg(v) % (2*mp.pi) for v in verts]); br.append(br[0] + 2*mp.pi)
    I_log = mp.fsum(mp.quad(lambda th: mp.log(rmax(th, tau)), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_e2 = mp.fsum(mp.quad(lambda th: mp.expj(2*th)*rmax(th, tau)**2/2, [a, b]) for a, b in zip(br[:-1], br[1:]))
    return tot + 2*mp.re(s1*I_e2) + I_log, s1
_GL = {}
def gl(n):
    if n not in _GL:
        import numpy as np
        x, w = np.polynomial.legendre.leggauss(n); _GL[n] = ([mp.mpf(float(a)) for a in x], [mp.mpf(float(b)) for b in w])
    return _GL[n]
if __name__ == "__main__":
    import sys, numpy as np, end_data_defect as A
    sys.path.insert(0, '.')
    def cA(r, tau, rho=0.05):
        tot, _ = A.c_r(r, tau, rho); s1 = A.laurent(r, tau, 1); s3 = A.laurent(r, tau, 3)
        return tot + abs(s1)**2*np.pi*rho**4/2 + abs(s3)**2*np.pi*rho**8/4
    w = complex(np.exp(2j*np.pi/3))
    for name, tau in [("omega", w), ("i", 1j), ("0.13+1.07i", 0.13+1.07j)]:
        for r in (2, 3, 4):
            for n in (24, 40):
                cb, s1 = c_r(r, mp.mpc(tau), n)
                print(f"{name} r={r} n={n}: route B {mp.nstr(cb, 14)}  route A {cA(r, tau):.12f}  diff {abs(float(cb) - cA(r, tau)):.1e}")
