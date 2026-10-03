"""B1527 -- THE CUSP DECIDES: the word states, their hyperbolic point in Ballas' frame, and type-one families.  Library; nothing
sealed is computed on import.

- word_group(sign, word): Gamma = F_2 x| <t> with t x t^-1 = phi(x) (phi as sm:B1523's route F builds it: phi_L: a -> ab,
  phi_R: b -> ba, the last letter first, then iota: a -> A, b -> B for the sign -); the cusp <l, t'>, l = abAB, t' = t for +
  and abt for - (phi fixes abAB exactly; iota sends it to ABab = (ab)^-1 abAB (ab)).
- hyperbolic_point(sign, word): the SL(2, C) holonomy located by sm:B1523's seeded route F (SnapPy's holonomy only seeds route
  F's 60-digit Newton on the trace map; the cusp shape must match SnapPy's), conjugated so the cusp fixes infinity, mapped to
  SO(3, 1) in Ballas' paraboloid frame (cusp_lib.hermitian_paraboloid): rho(gamma) = exp(X(E12 + E24) + Y(E13 + E34)) on the
  cusp, with (X, Y) the translation of gamma.
- solve_type_one(...): a representation of Gamma whose cusp lies in Ballas' slice with b = 0 (arXiv:1805.09274, (3.1) and
  Theorem 3.2: type one when a != 0):
      rho(gamma) = |det|^(-1/4) exp(X_gamma N_a + Y_gamma N_b),  N_a = E12 + a E22 + E24,  N_b = E13 + E34,
  for gamma = l, t', with a fixed and (A, B, T, X_l, Y_l, X_t, Y_t) unknown; Levenberg-Marquardt on the 66 residuals (the two
  bundle relations, the two cusp normal forms, det A = det B = 1), the Jacobian by complex-step differentiation (all maps are
  analytic), at the ambient mp.dps (40 in controls.py C5, 60 in run.py's polish)."""
import importlib.util
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import cusp_lib as L  # noqa: E402

_RF = ROOT / "frontier" / "B1523_the_flexible_states" / "verification"


def _load(name):
    spec = importlib.util.spec_from_file_location("b1523_" + name, _RF / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(_RF))
    spec.loader.exec_module(mod)
    return mod


# ============================================================================================ the groups
def automorphism(sign, word):
    img = {"a": "a", "b": "b"}
    for letter in reversed(word):
        step = {"a": "ab", "b": "b"} if letter == "L" else {"a": "a", "b": "ba"}
        img = {"a": L.substitute(img["a"], step), "b": L.substitute(img["b"], step)}
    if sign == "-":
        img = {g: L.substitute(img[g], {"a": "A", "b": "B"}) for g in "ab"}
    return img


def word_group(sign, word):
    img = automorphism(sign, word)
    rels = ["t" + g + "T" + L.inv_word(img[g]) for g in "ab"]
    return L.Group(["a", "b", "t"], rels, ("abAB", "t" if sign == "+" else "abt"), sign + word), img


def homology_matrix(img):
    """phi on H_1(F) = Z^2: column j holds the exponent sums of phi(gen_j)"""
    def ex(w, g):
        return w.count(g) - w.count(g.upper())
    return [[ex(img["a"], "a"), ex(img["b"], "a")], [ex(img["a"], "b"), ex(img["b"], "b")]]


def torsion_characters(img):
    """the characters of F that phi fixes, as (u_a, u_b) in (Q/Z)^2 with nu(a) = e^{2 pi i u_a}: nu o phi = nu on F means
    u (M - 1) = 0 mod 1 for the row vector u = (u_a, u_b) and M = homology_matrix (nu(phi(g_j)) = prod nu(g_i)^{M_ij})"""
    from fractions import Fraction as Fr
    M = homology_matrix(img)
    A = [[M[0][0] - 1, M[0][1]], [M[1][0], M[1][1] - 1]]
    D = abs(A[0][0] * A[1][1] - A[0][1] * A[1][0])
    out = set()
    for i in range(D):
        for j in range(D):
            u = (Fr(i, D), Fr(j, D))
            v0 = u[0] * A[0][0] + u[1] * A[1][0]
            v1 = u[0] * A[0][1] + u[1] * A[1][1]
            if v0.denominator == 1 and v1.denominator == 1:
                out.add(u)
    assert len(out) == D, (len(out), D)
    return sorted(out), D


# ============================================================================================ the hyperbolic point
def hyperbolic_sl2(sign, word):
    """(A, B, T) in SL(2, C) at mp.dps = 60, located by sm:B1523's seeded route F"""
    import snappy
    F = _load("route_f")
    R = _load("route_f_reach")
    S = _load("route_f_seeded")
    name = ("b++" if sign == "+" else "b+-") + word
    sh = complex(snappy.Manifold(name).cusp_info("shape")[0])

    def matches(z):
        if abs(abs(z.imag) - abs(sh.imag)) > 1e-9:
            return False
        return any(abs((z.real + e * sh.real) - round(z.real + e * sh.real)) < 1e-9 for e in (1, -1))
    steps = F.letters(sign, word)
    for p in S.seeds(sign, word):
        r = R.polish(steps, p)
        if r is None:
            continue
        A, B = F.rep_from_traces(*r)
        T, _ = F.monodromy_fast(steps, A, B)
        z, _ = F.cusp_shape(sign, A, B, T)
        if z is not None and matches(complex(z)):
            return A, B, T, sh
    raise RuntimeError("no matching hyperbolic fixed point for " + name)


def sl2_word(w, M):
    X = mp.eye(2)
    for c in w:
        X = X * (M[c] if c.islower() else mp.inverse(M[c.lower()]))
    return X


def to_cusp_frame(A, B, T, sign, theta=0):
    """conjugate (A, B, T) so the cusp fixes infinity, then rotate the translations by e^{i theta}"""
    M = {"a": A, "b": B, "t": T}
    l = sl2_word("abAB", M)
    s = 1 if mp.re(l[0, 0] + l[1, 1]) > 0 else -1
    N = l - s * mp.eye(2)
    if abs(N[0, 0]) + abs(N[0, 1]) >= abs(N[1, 0]) + abs(N[1, 1]):
        u, v = N[0, 1], -N[0, 0]
    else:
        u, v = -N[1, 1], N[1, 0]
    nrm = mp.sqrt(abs(u) ** 2 + abs(v) ** 2)
    u, v = u / nrm, v / nrm
    Sm = mp.matrix([[u, -mp.conj(v)], [v, mp.conj(u)]])           # columns: the fixed vector, then its orthogonal
    Rm = mp.matrix([[mp.expjpi(theta / (2 * mp.pi)), 0], [0, mp.expjpi(-theta / (2 * mp.pi))]])
    C = Sm * mp.inverse(Rm)
    Ci = mp.inverse(C)
    return {g: Ci * M[g] * C for g in "abt"}


def paraboloid_module(M2):
    return L.Module({g: L.hermitian_paraboloid(M2[g]) for g in "abt"})


def translation(P):
    """(X, Y) of a type-0 normal form matrix exp(X(E12 + E24) + Y(E13 + E34))"""
    return mp.re(P[0, 1]), mp.re(P[0, 2])


# ============================================================================================ the type-one slice
def slice_matrix(X, Y, a):
    """Ballas' slice with b = 0, SL-normalised: |det|^(-1/4) exp(X N_a + Y N_b)"""
    N = mp.matrix(4, 4)
    N[0, 1], N[1, 1], N[1, 3] = X, a * X, X
    N[0, 2], N[2, 3] = Y, Y
    return mp.expm(N) * mp.exp(-a * X / 4)


def pack(mod, XY):
    u = []
    for g in "abt":
        for i in range(4):
            for j in range(4):
                u.append(mod.M[g][i, j])
    return mp.matrix(u + list(XY))


def unpack(u):
    mats = {}
    k = 0
    for g in "abt":
        Mg = mp.matrix(4, 4)
        for i in range(4):
            for j in range(4):
                Mg[i, j] = u[k]
                k += 1
        mats[g] = Mg
    return mats, [u[k], u[k + 1], u[k + 2], u[k + 3]]


def _word(mats, w, inv):
    X = mp.eye(4)
    for c in w:
        X = X * (mats[c] if c.islower() else inv[c.lower()])
    return X


def residual(u, a, G, img):
    mats, (Xl, Yl, Xt, Yt) = unpack(u)
    inv = {g: mp.inverse(mats[g]) for g in mats}
    out = []
    for g in "ab":
        R = mats["t"] * mats[g] - _word(mats, img[g], inv) * mats["t"]
        out += [R[i, j] for i in range(4) for j in range(4)]
    for w, (X, Y) in ((G.cusp[0], (Xl, Yl)), (G.cusp[1], (Xt, Yt))):
        R = _word(mats, w, inv) - slice_matrix(X, Y, a)
        out += [R[i, j] for i in range(4) for j in range(4)]
    out += [mp.det(mats["a"]) - 1, mp.det(mats["b"]) - 1]
    return mp.matrix(out)


def jacobian(u, a, G, img, h=None):
    """complex-step: every map is analytic in the real unknowns"""
    h = h or mp.mpf(10) ** (-(mp.mp.dps - 5))
    n = len(u)
    cols = []
    for k in range(n):
        v = mp.matrix([mp.mpc(x) for x in u])
        v[k] += 1j * h
        cols.append([mp.im(x) / h for x in residual(v, a, G, img)])
    m = len(cols[0])
    J = mp.matrix(m, n)
    for k in range(n):
        for i in range(m):
            J[i, k] = cols[k][i]
    return J


def solve_type_one(u0, a, G, img, tol=None, maxit=60, lam0=None):
    """Levenberg-Marquardt from u0; returns (u, |F|, iterations, history)"""
    tol = tol or mp.mpf(10) ** (-(mp.mp.dps - 12))
    u = mp.matrix([mp.re(x) for x in u0])
    F = residual(u, a, G, img)
    f = mp.norm(F)
    lam = lam0 if lam0 is not None else mp.mpf(10) ** -6
    hist = [f]
    for it in range(maxit):
        if f < tol:
            return u, f, it, hist
        J = jacobian(u, a, G, img)
        JT = J.T
        Hm = JT * J
        g = JT * mp.matrix([mp.re(x) for x in F])
        while True:
            Am = Hm + lam * mp.eye(Hm.rows)
            try:
                d = mp.lu_solve(Am, -g)
            except ZeroDivisionError:
                lam *= 10
                continue
            un = u + d
            Fn = residual(un, a, G, img)
            fn = mp.norm(Fn)
            if fn < f:
                u, F, f = un, Fn, fn
                lam = max(lam / 10, mp.mpf(10) ** -30)
                break
            lam *= 10
            if lam > mp.mpf(10) ** 10:
                return u, f, it, hist
        hist.append(f)
    return u, f, maxit, hist


def eig_sorted(M):
    ev = mp.eig(M)[0]
    return sorted(ev, key=lambda z: (mp.re(z), mp.im(z)))
