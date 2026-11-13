"""P-783: is the golden state the lowest twin-odd state on the level-5 curve, and is it simple?

The twin-odd states are the Maass cusp forms on Gamma0(5) with the quadratic character chi(d) = (d/5) (B1885 transforms
with it; P-776's twin exchange is the character's sign). They fall in four classes: parity under the mirror z -> -conj(z)
(sine or cosine series) and sign eps = +-1 under the Fricke involution W5: z -> -1/(5z). The golden state (B1885) is in the
class (sine, eps = -1) at R0 = pi/(2 ln phi).

METHOD (Hejhal's, main's own code): f(z) = sum_{n=1..M} c(n) sqrt(y) K_{iR}(2 pi n y) cs(2 pi n x), cs = sin or cos. Points
z_m = x_m + iY on a horocycle below the fundamental domain are pulled back: z = g z0 with z0 in PSL2(Z)'s domain, g = gamma
sigma_j with gamma in Gamma0(5) and sigma_j one of the six coset representatives; f(z) = chi(gamma) f(sigma_j z0); when
sigma_j sends z0 toward the cusp 0, W5 brings it back up: f(w) = eps f(W5 w). The relation f(z_m) = (the expansion at the
pulled-back point) is a linear system V(R) c = 0 (M x M, after a discrete Fourier transform on the horocycle). An
eigenvalue R makes V(R) singular: its least singular value falls to rounding.
CONTROL: the golden state must appear at R0 in its class. A cusp-form ansatz has no constant term, so the continuous
spectrum (the mirror-even classes) cannot give a false minimum.
No data; no value of the modulus on record is read; no point is compared with anything."""
import numpy as np, json, pathlib, sys, math
HERE = pathlib.Path(__file__).resolve().parent

# ---- K_{iR}(x) = int_0^inf exp(-x cosh t) cos(R t) dt, vectorised (Gauss-Legendre on [0, T])
_GL_N = 400
_gx, _gw = np.polynomial.legendre.leggauss(_GL_N)
def KiR(R, x):
    x = np.asarray(x, dtype=float)
    T = np.arccosh(np.maximum(60.0 / np.maximum(x, 1e-300), 1.0)) + 2.0
    t = 0.5 * T[..., None] * (_gx + 1); w = 0.5 * T[..., None] * _gw
    return np.sum(w * np.exp(-x[..., None] * np.cosh(t)) * np.cos(R * t), -1)

# ---- reduction to PSL2(Z)'s fundamental domain, tracking the matrix
def reduce(z):
    a, b, c, d = 1, 0, 0, 1                         # z_original = g z_current, g = [[a,b],[c,d]]
    for _ in range(1000):
        n = math.floor(z.real + 0.5)
        if n != 0:
            z -= n; a, b, c, d = a, b + a * n, c, d + c * n           # g <- g T^n
        if abs(z) < 1 - 1e-15:
            z = -1 / z; a, b, c, d = b, -a, d, -c                     # g <- g S^-1, S = [[0,-1],[1,0]]
        else:
            return z, (a, b, c, d)
    raise RuntimeError("reduce did not end")

def legendre5(d):
    r = d % 5
    return 0 if r == 0 else (1 if r in (1, 4) else -1)

REPS = [(1, 0, 0, 1)] + [(0, -1, 1, k) for k in range(5)]          # I and S T^k:  S T^k = [[0,-1],[1,k]]
def mul(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return (a * e + b * gg, a * f + b * hh, c * e + d * gg, c * f + d * hh)
def inv(g):
    a, b, c, d = g; return (d, -b, -c, a)
def act(g, z):
    a, b, c, d = g; return (a * z + b) / (c * z + d)

def pullback(z, eps):
    """(the point where the expansion at infinity is evaluated, the factor): f(z) = factor * f(point)"""
    z0, g = reduce(complex(z))
    for s in REPS:
        gam = mul(g, inv(s))
        if gam[2] % 5 == 0:
            fac = legendre5(gam[3])
            w = act(s, z0)
            if s == (1, 0, 0, 1):
                return w, fac
            w2 = -1 / (5 * w)                                   # W5 w, high in the half-plane
            return w2, fac * eps
    raise RuntimeError("no coset")

def V_matrix(R, M, Y, Q, parity, eps):
    cs = np.sin if parity == "sin" else np.cos
    xm = (np.arange(1, Q + 1) - 0.5) / (2 * Q)                  # (0, 1/2): the mirror halves the period
    pts, fac = [], []
    for x in xm:
        w, f = pullback(complex(x, Y), eps); pts.append(w); fac.append(f)
    pts = np.array(pts); fac = np.array(fac, dtype=float)
    n = np.arange(1, M + 1)
    ys, xs = pts.imag, pts.real
    Kp = np.array([KiR(R, 2 * np.pi * k * ys) for k in n])            # M x Q
    B = fac[None, :] * np.sqrt(ys)[None, :] * Kp * cs(2 * np.pi * n[:, None] * xs[None, :])   # l x m: f(z_m) = sum_l c_l B[l,m]
    W = (4.0 / (2 * Q)) * cs(2 * np.pi * n[:, None] * xm[None, :])      # discrete transform over the half period
    KY = np.sqrt(Y) * KiR(R, 2 * np.pi * n * Y)
    V = np.diag(KY) - W @ B.T                                       # row n: c_n sqrt(Y) K(2 pi n Y) - sum_m W[n,m] f(z_m)
    # scale each column l by 1/(sqrt(Y) K(2 pi l Y)) so the rows are comparable
    return V / KY[None, :]

def least_singular(R, M=34, Y=0.12, Q=60, parity="sin", eps=-1, k=1):
    s = np.linalg.svd(V_matrix(R, M, Y, Q, parity, eps), compute_uv=False)
    return s[-k:][::-1] / s[0]

if __name__ == "__main__":
    import mpmath as mp
    # the Bessel function against mpmath
    errs = []
    for R in (0.7, 2.1, 3.3):
        for x in (0.8, 2.5, 7.0, 20.0):
            ref = float(mp.re(mp.besselk(mp.mpc(0, R), x)))
            errs.append(abs(KiR(R, np.array([x]))[0] - ref) / max(abs(ref), 1e-300))
    print("K_iR against mpmath: max rel", max(errs))
    R0 = math.pi / (2 * math.log((1 + math.sqrt(5)) / 2))
    print("R0 =", R0)
    for par, ep in (("sin", -1), ("sin", 1), ("cos", -1), ("cos", 1)):
        vals = [least_singular(R0 + dr, parity=par, eps=ep)[0] for dr in (-0.05, -0.01, 0.0, 0.01, 0.05)]
        print(par, ep, ["%.2e" % v for v in vals])
