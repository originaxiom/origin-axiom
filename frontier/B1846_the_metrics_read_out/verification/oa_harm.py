"""The harmonic generator of H^1(M; R) for a one-cusped SnapPy manifold with b1 = 1 (data-free).

Generalises B1295's Hejhal collocation (frontier/B1295_.../verification/harmonic_generator.py) from the Riley group of
m004 to any SnapPy holonomy:
  1. the holonomy from SnapPy, conjugated so the peripheral subgroup fixes infinity, scaled so the maximal cusp sits at
     height 1 (smallest |c| = 1) and rotated so the first peripheral translation is real positive;
  2. chi: the abelianisation onto Z (relator exponent sums), tracked exactly on words;
  3. the Ford domain's floor: every isometric sphere of radius >= r_min reached by a word BFS, closed under lattice
     translates of its centre (each move carries its exact chi);
  4. the pullback (z, t) -> its max-height translate, vectorised;
  5. the collocation for psi = phi - phi_lin as in B1295.
Integrity checks (the owner's rule): the Ford domain's Monte Carlo volume against SnapPy's; the generator relations
phi(g P) - phi(P) = chi(g) on every generator; a second collocation height.
"""
import itertools, math, warnings
warnings.filterwarnings("ignore")
import numpy as np
from scipy.special import k0, k1


def _mat(G, w):
    m = G.SL2C(w)
    return np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])


def _chi_vector(gens, rels):
    n = len(gens); E = []
    for r in rels:
        e = [0] * n
        for ch in r:
            e[gens.index(ch.lower())] += 1 if ch.islower() else -1
        E.append(e)
    E = np.array(E, dtype=float).reshape(-1, n)
    _, s, vt = np.linalg.svd(E)
    null = vt[int(np.sum(s > 1e-9)):]
    assert null.shape[0] == 1, "b1 must be 1"
    v = null[0] / np.max(np.abs(null[0]))
    vi = np.round(v).astype(int)
    assert np.allclose(v, vi, atol=1e-9) or np.allclose(-v, -vi, atol=1e-9)
    # primitive integer vector: divide by the gcd
    g = 0
    for x in vi:
        g = math.gcd(g, abs(int(x)))
    vi = vi // g
    assert np.all(E.astype(int) @ vi == 0)
    return {gens[i]: int(vi[i]) for i in range(n)}


def chi_word(chi, w):
    return sum(chi[ch] if ch.islower() else -chi[ch.lower()] for ch in w)


def apply_m(M, z, t):
    a, b = M[0]; c, d = M[1]
    w = c * z + d
    D = abs(w) ** 2 + abs(c) ** 2 * t * t
    return ((a * z + b) * np.conj(w) + a * np.conj(c) * t * t) / D, t / D


class Group:
    def __init__(self, name, rmin=0.06, depth=9, normcap=400.0):
        import snappy
        self.name = name
        M = snappy.Manifold(name)
        self.vol = float(M.volume())
        G = M.fundamental_group()
        self.gens = G.generators(); self.rels = G.relators()
        self.orig_words = list(G.original_generators())
        self.chi = _chi_vector(self.gens, self.rels)
        mw, lw = G.peripheral_curves()[0]
        self.mw, self.lw = mw, lw
        raw = {g: _mat(G, g) for g in self.gens}
        P = _mat(G, mw)
        a, b, c, d = P[0, 0], P[0, 1], P[1, 0], P[1, 1]
        assert abs(abs(a + d) - 2) < 1e-8, "meridian not parabolic"
        p = (a - d) / (2 * c)
        C = np.array([[0, 1], [-1, p]], dtype=complex); Ci = np.linalg.inv(C)
        conj = {g: C @ raw[g] @ Ci for g in self.gens}
        # the translations of the peripheral pair
        def trans(word):
            X = self.wmat(word, conj)
            assert abs(X[1, 0]) < 1e-7, ("not upper triangular", word, X)
            return X[0, 1] / X[1, 1]
        v1, v2 = trans(mw), trans(lw)
        # smallest |c| over a BFS, to place the maximal cusp at height 1
        cmin = min(abs(X[1, 0]) for X, _ in self._bfs(conj, depth=6, normcap=normcap) if abs(X[1, 0]) > 1e-8)
        s2 = cmin * np.conj(v1) / abs(v1)          # z -> s2 z ; c -> c / s2
        s = np.sqrt(s2)
        Dm = np.array([[s, 0], [0, 1 / s]], dtype=complex); Dmi = np.linalg.inv(Dm)
        self.H = {g: Dm @ conj[g] @ Dmi for g in self.gens}
        self.Fr = Dm @ C                      # SnapPy's SL2C frame -> this frame (a Mobius map; acts on H^3 by apply_m)
        self.Hfull = dict(self.H)
        for g in self.gens:
            self.Hfull[g.upper()] = np.linalg.inv(self.H[g])
        w1, w2 = s2 * v1, s2 * v2
        c1, c2 = chi_word(self.chi, mw), chi_word(self.chi, lw)
        if (np.conj(w1) * w2).imag < 0:            # orient the basis
            w2, c2 = -w2, -c2
        self.lat = Lattice(w1, w2, c1, c2)
        self.cmin_check = None
        self.moves = self._moves(rmin, depth, normcap)

    def wmat(self, w, mats=None):
        mats = mats if mats is not None else self.Hfull
        X = np.eye(2, dtype=complex)
        for ch in w:
            if mats is getattr(self, "Hfull", None):
                X = X @ mats[ch]
            else:
                X = X @ (mats[ch] if ch.islower() else np.linalg.inv(mats[ch.lower()]))
        return X

    def _bfs(self, mats, depth, normcap):
        """Word BFS over the generators and inverses; matrices as 4-tuples of Python complex; dedupe up to sign."""
        letters = []
        words = list(self.gens) + [w for w in getattr(self, "orig_words", []) if len(w) > 1]
        for w in words:
            X = np.eye(2, dtype=complex)
            for ch in w:
                X = X @ (mats[ch] if ch.islower() else np.linalg.inv(mats[ch.lower()]))
            Xi = np.linalg.inv(X); cw = chi_word(self.chi, w)
            letters.append((tuple(complex(v) for v in X.ravel()), cw))
            letters.append((tuple(complex(v) for v in Xi.ravel()), -cw))
        def key(m):
            a, b, c, d = m
            for v in (c, d, a, b):
                if abs(v) > 1e-9:
                    sg = 1 if (v.real > 1e-9 or (abs(v.real) <= 1e-9 and v.imag > 0)) else -1
                    break
            return tuple(int(round(sg * x * 1e6)) for v in m for x in (v.real, v.imag))
        I = (1 + 0j, 0j, 0j, 1 + 0j)
        seen = {key(I)}
        frontier = [(I, 0)]
        out = []
        for _ in range(depth):
            nxt = []
            for (a, b, c, d), cx in frontier:
                for (p, q, r, s_), cl in letters:
                    Y = (a * p + b * r, a * q + b * s_, c * p + d * r, c * q + d * s_)
                    if max(abs(Y[0]), abs(Y[1]), abs(Y[2]), abs(Y[3])) > normcap:
                        continue
                    k = key(Y)
                    if k in seen:
                        continue
                    seen.add(k)
                    nxt.append((Y, cx + cl))
            out.extend(nxt)
            frontier = nxt
        return [(np.array([[Y[0], Y[1]], [Y[2], Y[3]]]), cx) for Y, cx in out]

    def _moves(self, rmin, depth, normcap):
        lat = self.lat
        base = []
        for X, cx in self._bfs(self.H, depth, normcap):
            c = X[1, 0]
            if abs(c) < 1e-9 or 1 / abs(c) < rmin:
                continue
            base.append((X, cx))
        self.cmin_check = min(abs(X[1, 0]) for X, _ in base)
        spheres = {}
        for X, cx in base:
            c, d = X[1, 0], X[1, 1]
            ctr = -d / c
            n = np.round(lat.coords(ctr))
            for e1 in (-1, 0, 1):
                for e2 in (-1, 0, 1):
                    m1, m2 = int(n[0]) + e1, int(n[1]) + e2
                    v = m1 * lat.w1 + m2 * lat.w2
                    Tv = np.array([[1, v], [0, 1]], dtype=complex)
                    Y = X @ Tv                                    # centre ctr - v
                    cy = cx + m1 * lat.c1 + m2 * lat.c2
                    k = (round(abs(c), 7), round((ctr - v).real, 6), round((ctr - v).imag, 6))
                    if k not in spheres:
                        spheres[k] = (Y, cy)
        mv = list(spheres.values())
        self.MA = np.array([[Y[0, 0], Y[0, 1], Y[1, 0], Y[1, 1]] for Y, _ in mv])
        self.MC = np.array([cy for _, cy in mv])
        return mv

    def pullback(self, z, t, itmax=500):
        """(z,t) -> (z*, t*, chi(gamma)) with gamma P = P* of maximal height."""
        lat = self.lat
        z, chi = lat.reduce(z)
        a, b, c, d = self.MA.T
        for _ in range(itmax):
            w = c * z + d
            D = np.abs(w) ** 2 + np.abs(c) ** 2 * t * t
            tn = t / D
            j = int(np.argmax(tn))
            if tn[j] <= t * (1 + 1e-12):
                return z, t, chi
            zn = ((a[j] * z + b[j]) * np.conj(w[j]) + a[j] * np.conj(c[j]) * t * t) / D[j]
            z, t, chi = zn, tn[j], chi + int(self.MC[j])
            z, ch = lat.reduce(z); chi += ch
        raise RuntimeError("pullback did not terminate")

    def in_domain(self, z, t):
        a, b, c, d = self.MA.T
        D = np.abs(c * z + d) ** 2 + np.abs(c) ** 2 * t * t
        return np.all(D >= 1 - 1e-12)


class Lattice:
    def __init__(self, w1, w2, c1, c2):
        self.w1, self.w2, self.c1, self.c2 = complex(w1), complex(w2), int(c1), int(c2)
        self.M = np.array([[self.w1.real, self.w2.real], [self.w1.imag, self.w2.imag]])
        self.Minv = np.linalg.inv(self.M)
        U = self.Minv
        self.u1 = complex(U[0, 0], U[0, 1]); self.u2 = complex(U[1, 0], U[1, 1])
        self.covol = abs(np.linalg.det(self.M))

    def coords(self, z):
        return self.Minv @ np.array([np.real(z), np.imag(z)])

    def phi_lin(self, z):
        n1, n2 = self.coords(z)
        return self.c1 * n1 + self.c2 * n2

    def reduce(self, z):
        n = np.round(self.coords(z))
        return z - (n[0] * self.w1 + n[1] * self.w2), -(int(n[0]) * self.c1 + int(n[1]) * self.c2)

    def modes(self, Rcut):
        N1 = int(Rcut * np.hypot(self.w1.real, self.w1.imag)) + 3
        N2 = int(Rcut * np.hypot(self.w2.real, self.w2.imag)) + 3
        out = []
        for m1 in range(-N1, N1 + 1):
            for m2 in range(-N2, N2 + 1):
                if (m1, m2) == (0, 0):
                    continue
                mu = m1 * self.u1 + m2 * self.u2
                if abs(mu) <= Rcut and (m1 > 0 or (m1 == 0 and m2 > 0)):
                    out.append((m1, m2, mu))
        return out


def design(lat, modes, Z, T):
    """Rows for psi at points (Z, T): psi = sum_{half} 2 Re(c_mu e^{2 pi i <mu,z>}) t K1(2 pi |mu| t)."""
    Z = np.asarray(Z); T = np.asarray(T)
    mus = np.array([m[2] for m in modes])
    th = 2 * np.pi * (np.outer(Z.real, mus.real) + np.outer(Z.imag, mus.imag))
    g = T[:, None] * k1(2 * np.pi * np.abs(mus)[None, :] * T[:, None])
    out = np.empty((len(Z), 2 * len(modes)))
    out[:, 0::2] = 2 * np.cos(th) * g
    out[:, 1::2] = -2 * np.sin(th) * g
    return out


def solve(G, Y, Rcut, npts, seed, jitter=0.35):
    lat = G.lat
    modes = lat.modes(Rcut)
    rng = np.random.default_rng(seed)
    side = int(np.sqrt(npts))
    Zs, Ts, Zb, rhs, tst = [], [], [], [], []
    for i in range(side):
        for j in range(side):
            x = (i + 0.5 + jitter * rng.uniform(-1, 1)) / side - 0.5
            y = (j + 0.5 + jitter * rng.uniform(-1, 1)) / side - 0.5
            z0 = x * lat.w1 + y * lat.w2
            zs, ts, chi = G.pullback(z0, Y)
            if ts <= Y * (1 + 1e-9):
                continue
            Zs.append(zs); Ts.append(ts); Zb.append(z0)
            rhs.append(lat.phi_lin(z0) - lat.phi_lin(zs) + chi); tst.append(ts)
    V = design(lat, modes, Zs, Ts) - design(lat, modes, Zb, [Y] * len(Zb))
    r = np.array(rhs)
    sc = np.linalg.norm(V, axis=0); sc[sc == 0] = 1
    x, _, rank, sv = np.linalg.lstsq(V / sc, r, rcond=None)
    x = x / sc
    res = V @ x - r
    coef = np.array([complex(x[2 * j], x[2 * j + 1]) for j in range(len(modes))])
    return Harmonic(lat, modes, coef), dict(n_eq=len(r), n_unknown=2 * len(modes), rank=int(rank),
                                             sv_min=float(sv[-1]), sv_max=float(sv[0]),
                                             resid_rms=float(np.sqrt(np.mean(res ** 2))), resid_max=float(np.abs(res).max()),
                                             tstar_min=float(min(tst)), n_low=len(Zb))


class Harmonic:
    def __init__(self, lat, modes, coef):
        self.lat, self.modes, self.coef = lat, modes, coef
        self.mus = np.array([m[2] for m in modes])

    def psi(self, Z, T):
        Z = np.atleast_1d(np.asarray(Z, dtype=complex)); T = np.atleast_1d(np.asarray(T, dtype=float))
        th = 2 * np.pi * (np.outer(Z.real, self.mus.real) + np.outer(Z.imag, self.mus.imag))
        g = T[:, None] * k1(2 * np.pi * np.abs(self.mus)[None, :] * T[:, None])
        return np.sum(2 * np.real(self.coef[None, :] * np.exp(1j * th)) * g, axis=1)

    def phi(self, Z, T):
        Z = np.atleast_1d(np.asarray(Z, dtype=complex))
        lin = np.array([self.lat.phi_lin(z) for z in Z])
        return lin + self.psi(Z, T)

    def grad(self, Z, T):
        """Euclidean gradient (d/dx, d/dy, d/dt) of phi; the hyperbolic |d phi|^2 = t^2 |grad|^2."""
        Z = np.atleast_1d(np.asarray(Z, dtype=complex)); T = np.atleast_1d(np.asarray(T, dtype=float))
        lat = self.lat
        gl = lat.c1 * np.array([lat.Minv[0, 0], lat.Minv[0, 1]]) + lat.c2 * np.array([lat.Minv[1, 0], lat.Minv[1, 1]])
        a = 2 * np.pi * np.abs(self.mus)[None, :]
        th = 2 * np.pi * (np.outer(Z.real, self.mus.real) + np.outer(Z.imag, self.mus.imag))
        E = self.coef[None, :] * np.exp(1j * th)
        g = T[:, None] * k1(a * T[:, None])
        dg = -a * T[:, None] * k0(a * T[:, None])            # d/dt [t K1(a t)] = -a t K0(a t)
        dx = np.sum(2 * np.real(1j * 2 * np.pi * self.mus.real[None, :] * E) * g, axis=1) + gl[0]
        dy = np.sum(2 * np.real(1j * 2 * np.pi * self.mus.imag[None, :] * E) * g, axis=1) + gl[1]
        dt = np.sum(2 * np.real(E) * dg, axis=1)
        return dx, dy, dt
