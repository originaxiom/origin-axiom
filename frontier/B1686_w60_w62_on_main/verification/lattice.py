"""Main's own lattice for P-222 (the SM seat's W60 and W62 checked on main), written from W60_RULE.md and W62_RULE.md, not
from the seat's scripts.

The triangular lattice: sites at Z^2 + (1/3, 2/3) in the basis (1, omega), unit spacing, six neighbours +-(1,0), +-(0,1),
+-(1,1); the isotropic six-point Laplacian (H u)(x) = (2/3) sum_y (u(x) - U_xy u(y)). A torus is the quotient by a
sublattice Lambda with integer basis v1, v2 (coefficients of 1 and omega); the puncture z = 0 is the centroid of the
triangle (-2/3, -1/3), (1/3, -1/3), (1/3, 2/3). The flat connection: with (s, t) the coordinates in the basis (v1, v2),
a link crossing the cut s = 0 (the line through v2) in the +s direction carries G1 = R(a) e^{2 pi i phi1}, one crossing
t = 0 (the line through v1) in the +t direction carries G2 = R(b) e^{2 pi i phi2}; a link crossing both carries the
product in the order crossed (the convention is fixed by the plaquette check: exactly one triangle, the puncture's,
has holonomy -1). R = the quaternion units (rank 2: R(a) = i, R(b) = j) or 1 (rank 1). The cuts are shifted by EPS so
no site lies on one."""
import numpy as np
import scipy.sparse as sp

OMEGA = complex(-0.5, np.sqrt(3) / 2)
EPS = 1e-7
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
DELTAS = ((1, 0), (0, 1), (1, 1))


class Torus:
    def __init__(self, v1, v2):
        self.v1, self.v2 = np.array(v1, float), np.array(v2, float)
        self.M = np.column_stack([self.v1, self.v2]); self.Minv = np.linalg.inv(self.M)
        self.n = int(round(abs(np.linalg.det(self.M))))
        self.shape = (v2[0] + v2[1] * OMEGA) / (v1[0] + v1[1] * OMEGA)
        corners = np.array([[0, 0], self.v1, self.v2, self.v1 + self.v2])
        lo, hi = np.floor(corners.min(0)) - 2, np.ceil(corners.max(0)) + 2
        P, Q = np.meshgrid(np.arange(lo[0], hi[0] + 1) + 1 / 3, np.arange(lo[1], hi[1] + 1) + 2 / 3, indexing="ij")
        pts = np.column_stack([P.ravel(), Q.ravel()])
        st = pts @ self.Minv.T - EPS
        keep = np.all((st >= 0) & (st < 1), axis=1)
        self.sites = pts[keep]
        assert len(self.sites) == self.n, (len(self.sites), self.n)
        self.index = {self._key(p): k for k, p in enumerate(self.sites)}

    @staticmethod
    def _key(p):
        return (int(round(3 * p[0])), int(round(3 * p[1])))

    def reduce(self, p):
        st = self.Minv @ p - EPS
        return p - self.M @ np.floor(st)

    def links(self, R1, R2):
        """every forward link (x, y, the list of crossings in order): a crossing is (which cut, direction)"""
        out = []
        for k, x in enumerate(self.sites):
            sx = self.Minv @ x - EPS
            for d in DELTAS:
                y = x + np.array(d, float); sy = self.Minv @ y - EPS
                cr = []
                for ax in (0, 1):
                    a, b = sx[ax], sy[ax]
                    for m in range(int(np.floor(min(a, b))) + 1, int(np.floor(max(a, b))) + 1):
                        lam = (m - a) / (b - a)
                        cr.append((lam, ax, 1 if b > a else -1))
                cr.sort()
                out.append((k, self.index[self._key(self.reduce(y))], [(ax, sg) for _, ax, sg in cr]))
        return out

    def operator(self, phi=(0.0, 0.0), rank=2, order="first-left"):
        R = (QI, QJ) if rank == 2 else (np.eye(1, dtype=complex), np.eye(1, dtype=complex))
        G = [R[0] * np.exp(2j * np.pi * phi[0]), R[1] * np.exp(2j * np.pi * phi[1])]
        Ginv = [np.linalg.inv(g) for g in G]
        r = rank; rows, cols, vals = [], [], []
        diag = np.zeros(self.n * r)
        self.U = {}
        for x, y, cr in self.links(None, None):
            U = np.eye(r, dtype=complex)
            mats = [G[ax] if sg > 0 else Ginv[ax] for ax, sg in cr]
            if order == "first-right": mats = mats[::-1]
            for m in mats: U = U @ m
            self.U[(x, y)] = U
            diag[x * r:(x + 1) * r] += 2 / 3; diag[y * r:(y + 1) * r] += 2 / 3
            for a in range(r):
                for b in range(r):
                    if U[a, b] != 0:
                        rows.append(x * r + a); cols.append(y * r + b); vals.append(-(2 / 3) * U[a, b])
                        rows.append(y * r + b); cols.append(x * r + a); vals.append(-(2 / 3) * np.conj(U[a, b]))
        H = sp.coo_matrix((vals, (rows, cols)), shape=(self.n * r, self.n * r)).tocsr()
        return (H + sp.diags(diag)).tocsc()

    def plaquettes(self, r):
        """the holonomy of every triangle (up and down), from the links of the last operator() call"""
        def link(x, y):
            if (x, y) in self.U: return self.U[(x, y)]
            return np.linalg.inv(self.U[(y, x)])
        nbr = {}
        for (x, y) in self.U:
            nbr.setdefault(x, {})
        idx = lambda p: self.index[self._key(self.reduce(p))]
        res = []
        for k, x in enumerate(self.sites):
            a, b, c, d = k, idx(x + np.array([1., 0])), idx(x + np.array([1., 1])), idx(x + np.array([0., 1]))
            for tri in ((a, b, c), (a, c, d)):
                Hh = link(tri[0], tri[1]) @ link(tri[1], tri[2]) @ link(tri[2], tri[0])
                res.append((tri, Hh))
        return res


def lowest(H, K, sigma=-0.5):
    """the K lowest eigenvalues of the Hermitian H, through its real symmetric form [[Re H, -Im H], [Im H, Re H]] (every
    eigenvalue twice): scipy's shift-invert on the complex Hermitian H loses accuracy (3e-7 against a dense solve on a
    1176-dimensional torus), the real form agrees to 1e-14"""
    from scipy.sparse.linalg import eigsh
    if np.iscomplexobj(H.data) and np.abs(H.imag).max() > 0:
        R = sp.bmat([[H.real, -H.imag], [H.imag, H.real]]).tocsc()
        w = np.sort(eigsh(R, k=2 * K, sigma=sigma, which="LM", return_eigenvectors=False))
        return w[0::2]
    w = eigsh(H.real if np.iscomplexobj(H.data) else H, k=K, sigma=sigma, which="LM", return_eigenvectors=False)
    return np.sort(np.real(w))


def lattice_spectrum_abelian(N1, N2, phi, n_lowest=None, v1=None, v2=None):
    """the closed-form spectrum of the rank-1 operator on the torus spanned by v1 = (N1, 0), v2 = (0, N2) (W60's tori):
    (4/3)[3 - cos 2 pi k1 - cos 2 pi k2 - cos 2 pi (k1 + k2)], k = (m + phi)/N"""
    m1, m2 = np.meshgrid(np.arange(N1), np.arange(N2), indexing="ij")
    k1, k2 = (m1 + phi[0]) / N1, (m2 + phi[1]) / N2
    lam = (4 / 3) * (3 - np.cos(2 * np.pi * k1) - np.cos(2 * np.pi * k2) - np.cos(2 * np.pi * (k1 + k2)))
    lam = np.sort(lam.ravel())
    return lam[:n_lowest] if n_lowest else lam


def lattice_spectrum_abelian_general(T, phi):
    """the closed-form spectrum of the rank-1 operator on any sublattice torus: plane waves e^{2 pi i k.x} with
    k in the dual of Lambda shifted by phi, k = M^{-T}(m + phi), m over Z^2 / (the dual of Z^2), n of them"""
    MinvT = T.Minv.T
    # the n characters: k = M^{-T} (m + phi) modulo Z^2 (the dual of the site lattice Z^2)
    ks = set(); out = []
    span = int(np.ceil(np.abs(T.M).sum())) + 2
    for m1 in range(-span, span + 1):
        for m2 in range(-span, span + 1):
            k = MinvT @ np.array([m1 + phi[0], m2 + phi[1]])
            key = tuple(np.round(np.mod(k, 1.0) * 1e9).astype(np.int64) % 1000000000)
            if key in ks: continue
            ks.add(key)
            out.append((4 / 3) * (3 - np.cos(2 * np.pi * k[0]) - np.cos(2 * np.pi * k[1]) - np.cos(2 * np.pi * (k[0] + k[1]))))
            if len(out) == T.n: return np.sort(out)
    raise RuntimeError("not all characters found")
