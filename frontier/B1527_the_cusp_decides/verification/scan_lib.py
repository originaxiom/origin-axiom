"""B1527 -- THE CUSP DECIDES: the fast scan (float64).  Library; nothing sealed is computed on import.

A representation rho of the bundle group Gamma = <a, b, t | t x t^-1 = phi(x)> (family_lib.word_group) whose cusp <l, t'> lies in
Ballas' slice (arXiv:1805.09274, (3.1)), SL-normalised:
    rho(gamma) = |det|^(-1/4) exp(X_gamma N_a + Y_gamma N_b),   N_a = E12 + a E22 + E24,   N_b = E13 + b E33 + E34,
for gamma = l, t'.  Type one when exactly one of a, b is non-zero, type two when both are (Ballas Thm 3.2).
- `a` is fixed (it fixes the slice's scale, (a, b, x, y) ~ (a/s, b/s, s x, s y)); `b` is fixed at 0 (the type-one solver) or free
  (the generalized-cusp solver).
- Unknowns: A, B, T (48 entries), X_l, Y_l, X_t, Y_t, and b when free.  Residuals (66): T g - phi(g) T for g = a, b; the two cusp
  words minus their slice matrices; det A - 1, det B - 1.
- Levenberg-Marquardt; the Jacobian by complex-step differentiation (every map is analytic in the real unknowns, so the
  derivative is exact to rounding).
- The slice matrix in closed form (upper triangular; divided differences of exp): with al = a X, be = b Y,
      exp = [[1, X f1(al), Y f1(be), X^2 f2(al) + Y^2 f2(be)], [0, e^al, 0, X f1(al)], [0, 0, e^be, Y f1(be)], [0, 0, 0, 1]],
  f1(z) = (e^z - 1)/z, f2(z) = (e^z - 1 - z)/z^2 (series near 0); checked against scipy's expm by `selftest()`.
The scan seeds from the hyperbolic point in the cusp frame rotated by theta (family_lib.to_cusp_frame), so it can find a
solution near any frame; which frames it finds is the outcome.  Solutions are polished afterwards at high precision by
family_lib (mpmath); this module only finds them."""
import numpy as np

H_STEP = 1e-30


# ============================================================================================ the slice
def _f1(z):
    z = np.asarray(z, dtype=complex)
    out = np.empty_like(z)
    small = np.abs(z) < 1e-3
    zs = z[small]
    out[small] = 1 + zs / 2 + zs ** 2 / 6 + zs ** 3 / 24 + zs ** 4 / 120 + zs ** 5 / 720
    zl = z[~small]
    out[~small] = np.expm1(zl) / zl
    return out


def _f2(z):
    z = np.asarray(z, dtype=complex)
    out = np.empty_like(z)
    small = np.abs(z) < 1e-2
    zs = z[small]
    out[small] = 0.5 + zs / 6 + zs ** 2 / 24 + zs ** 3 / 120 + zs ** 4 / 720 + zs ** 5 / 5040 + zs ** 6 / 40320
    zl = z[~small]
    out[~small] = (np.expm1(zl) - zl) / zl ** 2
    return out


def slice_matrix(X, Y, a, b):
    """|det|^(-1/4) exp(X N_a + Y N_b), analytic in (X, Y, a, b) (complex arguments allowed, for the complex step)"""
    al, be = a * X, b * Y
    f1a, f1b = _f1(np.array([al]))[0], _f1(np.array([be]))[0]
    f2a, f2b = _f2(np.array([al]))[0], _f2(np.array([be]))[0]
    E = np.zeros((4, 4), dtype=complex)
    E[0, 0] = 1
    E[0, 1] = X * f1a
    E[0, 2] = Y * f1b
    E[0, 3] = X * X * f2a + Y * Y * f2b
    E[1, 1] = np.exp(al)
    E[1, 3] = X * f1a
    E[2, 2] = np.exp(be)
    E[2, 3] = Y * f1b
    E[3, 3] = 1
    return E * np.exp(-(al + be) / 4)


def selftest():
    """the closed form against mpmath's expm at 40 digits: the largest error relative to the matrix's largest entry"""
    import mpmath as mp
    rng = np.random.default_rng(5)
    worst = 0.0
    with mp.workdps(40):
        for _ in range(50):
            X, Y, a, b = rng.normal(size=4) * np.array([1.5, 1.5, 0.7, 0.7])
            if rng.random() < 0.3:
                a *= 1e-6
            N = mp.matrix(4, 4)
            N[0, 1], N[1, 1], N[1, 3] = X, a * X, X
            N[0, 2], N[2, 2], N[2, 3] = Y, b * Y, Y
            ref = mp.expm(N) * mp.exp(-(a * X + b * Y) / 4)
            R = np.array([[complex(ref[i, j]) for j in range(4)] for i in range(4)])
            worst = max(worst, np.abs(slice_matrix(X, Y, a, b) - R).max() / np.abs(R).max())
    return worst


# ============================================================================================ words
class Words:
    """the group's words compiled to index lists into (A, B, T, A^-1, B^-1, T^-1)"""
    IDX = {"a": 0, "b": 1, "t": 2, "A": 3, "B": 4, "T": 5}

    def __init__(self, G, img):
        self.phi = [[self.IDX[c] for c in img[g]] for g in "ab"]
        self.cusp = [[self.IDX[c] for c in w] for w in G.cusp]

    @staticmethod
    def evaluate(idx, mats):
        X = np.eye(4, dtype=complex)
        for i in idx:
            X = X @ mats[i]
        return X


# ============================================================================================ the system
def n_unknowns(b_free):
    return 52 + (1 if b_free else 0)


def unpack(u, b_free, b_fixed=0.0):
    A = u[0:16].reshape(4, 4)
    B = u[16:32].reshape(4, 4)
    T = u[32:48].reshape(4, 4)
    Xl, Yl, Xt, Yt = u[48], u[49], u[50], u[51]
    b = u[52] if b_free else b_fixed
    return A, B, T, (Xl, Yl, Xt, Yt), b


def pack(A, B, T, XY, b=None):
    parts = [np.asarray(A, dtype=complex).ravel(), np.asarray(B, dtype=complex).ravel(), np.asarray(T, dtype=complex).ravel(),
             np.asarray(XY, dtype=complex)]
    if b is not None:
        parts.append(np.array([b], dtype=complex))
    return np.concatenate(parts)


def residual(u, a, W, b_free, b_fixed=0.0):
    A, B, T, (Xl, Yl, Xt, Yt), b = unpack(u, b_free, b_fixed)
    mats = [A, B, T, np.linalg.inv(A), np.linalg.inv(B), np.linalg.inv(T)]
    out = []
    for g, idx in zip((A, B), W.phi):
        out.append((T @ g - Words.evaluate(idx, mats) @ T).ravel())
    for idx, (X, Y) in zip(W.cusp, ((Xl, Yl), (Xt, Yt))):
        out.append((Words.evaluate(idx, mats) - slice_matrix(X, Y, a, b)).ravel())
    out.append(np.array([np.linalg.det(A) - 1, np.linalg.det(B) - 1]))
    return np.concatenate(out)


def jacobian(u, a, W, b_free, b_fixed=0.0):
    n = len(u)
    cols = []
    for k in range(n):
        v = np.array(u, dtype=complex)
        v[k] += 1j * H_STEP
        cols.append(residual(v, a, W, b_free, b_fixed).imag / H_STEP)
    return np.array(cols).T


def solve(u0, a, W, b_free, b_fixed=0.0, tol=1e-12, maxit=80, lam0=1e-6):
    """Levenberg-Marquardt from u0 (real); returns (u, |F|, iterations)"""
    u = np.array(np.real(u0), dtype=float)
    F = residual(u, a, W, b_free, b_fixed).real
    f = np.linalg.norm(F)
    lam = lam0
    for it in range(maxit):
        if f < tol:
            return u, f, it
        J = jacobian(u, a, W, b_free, b_fixed)
        H = J.T @ J
        g = J.T @ F
        d_scale = np.diag(H).copy()
        d_scale[d_scale < 1e-12] = 1e-12
        while True:
            try:
                d = np.linalg.solve(H + lam * np.diag(d_scale), -g)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            un = u + d
            Fn = residual(un, a, W, b_free, b_fixed).real
            fn = np.linalg.norm(Fn)
            if np.isfinite(fn) and fn < f:
                u, F, f = un, Fn, fn
                lam = max(lam / 10, 1e-15)
                break
            lam *= 10
            if lam > 1e12:
                return u, f, it
    return u, f, maxit


# ============================================================================================ reading a solution
def frame_reading(u, b_free, b_fixed=0.0):
    """the slice data of a solution: the translations, the angle of l in the slice frame, b"""
    A, B, T, (Xl, Yl, Xt, Yt), b = unpack(np.asarray(u, dtype=complex), b_free, b_fixed)
    zl, zt = complex(Xl.real, Yl.real), complex(Xt.real, Yt.real)
    return {"zl": zl, "zt": zt, "shape": zt / zl, "angle_l": np.degrees(np.angle(zl)), "b": float(np.real(b))}


def line_angle_from_l(direction, zl, orient):
    """the angle of the line through `direction` (a complex number) measured from l, mod 180, in the orientation `orient` = +-1
    (the one that gives the computed cusp shape the sign of SnapPy's imaginary part, the convention of sm:B1523's slope box)"""
    return float(np.degrees(orient * np.angle(direction / zl)) % 180.0)


# ============================================================================================ seeds at the hyperbolic point
def hyperbolic_seed(sign, word, theta, cache=None):
    """(G, img, W, u0, orient): the hyperbolic point of the word state in the cusp frame rotated by theta (radians), as the
    starting point of the solver (its cusp is type 0: a = b = 0, so u0 solves the system only at a = 0)"""
    import mpmath as mp
    import family_lib as FL
    G, img = FL.word_group(sign, word)
    key = (sign, word)
    if cache is not None and key in cache:
        A2, B2, T2, sh = cache[key]
    else:
        A2, B2, T2, sh = FL.hyperbolic_sl2(sign, word)
        if cache is not None:
            cache[key] = (A2, B2, T2, sh)
    M2 = FL.to_cusp_frame(A2, B2, T2, sign, theta)
    mod = FL.paraboloid_module(M2)
    mats = {g: np.array([[complex(mod.M[g][i, j]) for j in range(4)] for i in range(4)]) for g in "abt"}
    W = Words(G, img)
    allm = [mats["a"], mats["b"], mats["t"], np.linalg.inv(mats["a"]), np.linalg.inv(mats["b"]), np.linalg.inv(mats["t"])]
    Pl = Words.evaluate(W.cusp[0], allm)
    Pt = Words.evaluate(W.cusp[1], allm)
    XY = [Pl[0, 1].real, Pl[0, 2].real, Pt[0, 1].real, Pt[0, 2].real]
    u0 = pack(mats["a"], mats["b"], mats["t"], XY)
    zl, zt = complex(XY[0], XY[1]), complex(XY[2], XY[3])
    orient = 1 if np.sign((zt / zl).imag) == np.sign(sh.imag) else -1
    return G, img, W, u0.real, orient
