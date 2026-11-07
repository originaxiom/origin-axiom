"""AMENDMENT 2 of tauinst.py (after the sealed run, before any tau of k = 3 or 4 was computed): the only change is in
Mesh, where the horoball radius at each developed vertex no longer comes from the word-search lookup alone (it missed
vertices of k = 3 and 4 and stopped those members at "cusp point not found") but is carried across the fundamental
polyhedron's face pairings from the vertices the lookup finds; where both exist they agree to 1e-9 (asserted). On
k = 1, 2 and 5 the resulting mesh is bitwise identical to tauinst.py's.

The instrument for the level surface's own modulus (P-727), independent of main's Ford-domain meshers.

Parts, in order of use:
- geometry: SnapPy's developed ideal tetrahedra and face pairings, the cusp normalised (peripheral subgroup fixing
  infinity, maximal cusp at height 1), the fibration class chi from relator exponent sums, the cusp lattice
  (p1: chi = 0, the fibre's boundary; p2: chi = 1), and the Ford sphere set (a word search closed under products of
  floor-visible elements, checked against SnapPy's volume);
- harmonic time h (h(gx) = h(x) + chi(g), harmonic, h minus its linear part bounded in the cusp) by Hejhal
  collocation in the cusp's Fourier-Bessel expansion, at pulled-back points;
- a simplicial mesh of the truncated manifold, intrinsic so that glued faces carry the same nodes;
- the level surface {h = s mod 1} by marching tetrahedra with exact crossings (a node within max(1e-6, 1e-2 x the
  largest |delta h| on its mesh edges) of the level is snapped, so that no crossing falls within 1 % of an edge's end,
  then re-projected onto the exact level);
- 1-to-4 subdivisions, each new vertex projected onto the exact level along grad h (one projection per frame, edge and
  local copy: a frame whose faces are glued to each other holds the same surface edge at two places);
- the conformal modulus: the cusp hole capped by a cone, intrinsic Delaunay flips, cotangent Laplacian, tree-cotree
  cohomology basis, harmonic 1-forms, energy matrix E, tau = (-E12 + i sqrt(det E))/E22 (the root of the energy form,
  covariant under a change of the cycle basis) with the orientation from the integral of alpha ^ beta, reduced to the
  standard fundamental domain.
Nothing here reads a measured value."""
import itertools, time
from collections import Counter, deque
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import k1e
from numba import njit
import snappy
from snappy.snap.fundamental_polyhedron import FundamentalPolyhedronEngine, Infinity
from snappy.snap.t3mlite import simplex
from sympy import Matrix


def act3(A, w, z):
    """Act by A in SL(2,C) on the point (w, z) of upper half-space."""
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    cw_d = c * w + d
    den = np.abs(cw_d) ** 2 + np.abs(c) ** 2 * z * z
    return ((a * w + b) * np.conj(cw_d) + a * np.conj(c) * z * z) / den, z / den


# ---- from the instrument's geo part ----
def _chi_from_relators(ngen, relators):
    R = []
    for r in relators:
        row = [0] * ngen
        for ch in r:
            i = ord(ch.lower()) - ord('a')
            row[i] += 1 if ch.islower() else -1
        R.append(row)
    ns = Matrix(R).nullspace() if R else [Matrix([1] * ngen)]
    assert len(ns) == 1, "b1 != 1"
    fr = [Fraction(str(x)) for x in ns[0]]
    den = 1
    for x in fr: den = den * x.denominator // int(np.gcd(den, x.denominator))
    vi = [int(x * den) for x in fr]
    g0 = 0
    for x in vi: g0 = int(np.gcd(g0, abs(x)))
    return [x // g0 for x in vi]

def _to_np(m):
    A = np.array([[complex(m[0,0]), complex(m[0,1])], [complex(m[1,0]), complex(m[1,1])]])
    return A / np.sqrt(np.linalg.det(A))

class Geo:
    def __init__(self, name, wordlen=7, rmin=0.08, verbose=True):
        self.name = name
        M = snappy.Manifold(name)
        assert M.num_cusps() == 1
        self.M = M
        F = FundamentalPolyhedronEngine.from_manifold_and_shapes(M, M.tetrahedra_shapes('rect'),
                                                                normalize_matrices=True, match_kernel=False)
        mc = F.mcomplex
        self.mc = mc
        # face-pairing (unsimplified) generators
        self.nfp = len(mc.GeneratorMatrices) // 2
        fpm = {g: _to_np(m) for g, m in mc.GeneratorMatrices.items()}
        G0 = M.fundamental_group(simplify_presentation=False)
        chi0 = _chi_from_relators(self.nfp, G0.relators())
        # simplified presentation, matrices in the same frame
        G = M.fundamental_group()
        sm = F.matrices_for_presentation(G)
        self.sgens = G.generators()
        smats = [_to_np(m) for m in sm]
        chis = _chi_from_relators(len(self.sgens), G.relators())
        # fix the sign of chi consistently between the two presentations: compare on a common element
        # (express simplified generators' chi through the face pairings is not available; use the cusp instead below)
        self.tets = []
        for t in mc.Tetrahedra:
            pts = []
            for v in simplex.ZeroSubsimplices:
                p = t.Class[v].IdealPoint
                pts.append(None if (p == Infinity or str(p) == 'Infinity') else complex(p))
            self.tets.append(pts)
        # word search over the simplified generators
        letters = []
        for i, A in enumerate(smats):
            letters.append((A, chis[i]))
            letters.append((np.linalg.inv(A), -chis[i]))
        mats, chis_w, last = [np.eye(2, dtype=complex)[None]], [np.zeros(1, int)], [np.full(1, -1)]
        cur_m, cur_x, cur_l = mats[0], chis_w[0], last[0]
        for L in range(wordlen):
            nm, nx, nl = [], [], []
            for li, (A, x) in enumerate(letters):
                inv = li ^ 1
                keep = cur_l != inv
                nm.append(cur_m[keep] @ A); nx.append(cur_x[keep] + x); nl.append(np.full(keep.sum(), li))
            cur_m = np.concatenate(nm); cur_x = np.concatenate(nx); cur_l = np.concatenate(nl)
            # dedupe up to sign
            sgn = np.sign(cur_m[:, 0, 0].real + 1e-300)
            key = np.round((cur_m * sgn[:, None, None]).reshape(len(cur_m), 4), 7)
            kr = np.concatenate([key.real, key.imag], axis=1)
            _, idx = np.unique(kr, axis=0, return_index=True)
            cur_m, cur_x, cur_l = cur_m[idx], cur_x[idx], cur_l[idx]
            mats.append(cur_m); chis_w.append(cur_x); last.append(cur_l)
        allm = np.concatenate(mats); allx = np.concatenate(chis_w)
        # cusp normalisation: conjugate so the peripheral subgroup (SnapPy's meridian and longitude words) fixes infinity,
        # then scale so the maximal cusp sits at height 1
        mer, lon = G.peripheral_curves()[0]
        def wmat(w):
            A = np.eye(2, dtype=complex)
            for ch in w:
                i = ord(ch.lower()) - ord('a')
                A = A @ (smats[i] if ch.islower() else np.linalg.inv(smats[i]))
            return A
        def wchi(w):
            return sum((chis[ord(ch.lower()) - ord('a')] if ch.islower() else -chis[ord(ch.lower()) - ord('a')]) for ch in w)
        Am = wmat(mer)
        # fixed point of the parabolic Am: (a - d) / (2c) when c != 0, else infinity
        if abs(Am[1, 0]) > 1e-12:
            xi = (Am[0, 0] - Am[1, 1]) / (2 * Am[1, 0])
            Cj = np.array([[0, 1], [-1, xi]], dtype=complex)     # w -> 1/(xi - w)... sends xi to infinity
            Cj = Cj / np.sqrt(np.linalg.det(Cj))
        else:
            Cj = np.eye(2, dtype=complex)
        Cji = np.linalg.inv(Cj)
        allm = Cj @ allm @ Cji
        smats = [Cj @ A @ Cji for A in smats]
        fpm = {g: Cj @ A @ Cji for g, A in fpm.items()}
        def mobius(A, p):
            if p is None:
                return None if abs(A[1, 0]) < 1e-14 else A[0, 0] / A[1, 0]
            den = A[1, 0] * p + A[1, 1]
            return None if abs(den) < 1e-14 else (A[0, 0] * p + A[0, 1]) / den
        self.tets = [[mobius(Cj, p) for p in T] for T in self.tets]
        Am, Al = wmat(mer), wmat(lon)
        assert abs(Am[1, 0]) < 1e-9 and abs(Al[1, 0]) < 1e-9, (Am, Al)
        tm, tl = Am[0, 1] / Am[1, 1], Al[0, 1] / Al[1, 1]
        xm, xl = wchi(mer), wchi(lon)
        c = allm[:, 1, 0]
        cmin = np.abs(c[np.abs(c) > 1e-9]).min()
        lam = cmin
        self.lam = lam
        s = np.sqrt(lam)
        D, Di = np.diag([s, 1/s]), np.diag([1/s, s])
        allm = D @ allm @ Di
        self.smats = [D @ A @ Di for A in smats]
        self.schi = chis
        self.fpm = {g: D @ A @ Di for g, A in fpm.items()}
        self.tets = [[(None if p is None else lam * p) for p in T] for T in self.tets]
        tm, tl = tm * lam, tl * lam
        # lattice basis adapted to chi: p1 the primitive vector with chi = 0, p2 with chi = 1
        # (a m + b l) has chi = a xm + b xl
        g0 = int(np.gcd(xm, xl))
        a1, b1 = xl // g0, -xm // g0                       # chi(a1 m + b1 l) = 0, primitive
        p1 = a1 * tm + b1 * tl
        # find (a2, b2) with a2 xm + b2 xl = 1 and a1 b2 - a2 b1 = +-1
        best = None
        for a2 in range(-30, 31):
            for b2 in range(-30, 31):
                if a2 * xm + b2 * xl == 1 and abs(a1 * b2 - a2 * b1) == 1:
                    q = a2 * tm + b2 * tl
                    q = q - np.round((q * np.conj(p1)).real / abs(p1)**2) * p1
                    if best is None or abs(q) < abs(best) - 1e-12: best = q
        p2 = best
        self.p1, self.p2 = p1, p2
        self.mer, self.lon, self.chi_mer, self.chi_lon = mer, lon, xm, xl
        B = np.array([[p1.real, p2.real], [p1.imag, p2.imag]])
        self.B, self.Binv = B, np.linalg.inv(B)
        self.area = abs((np.conj(p1) * p2).imag)
        Mx = np.array([[p1.real, p1.imag], [p2.real, p2.imag]])
        nr, ni = np.linalg.solve(Mx, [0.0, 1.0])
        self.nu = nr + 1j * ni                     # l(w) = Re(conj(nu) w)
        Bi = np.linalg.inv(Mx)
        self.mu1 = Bi[0, 0] + 1j * Bi[1, 0]        # dual basis: Re(conj(mu_i) p_j) = delta_ij
        self.mu2 = Bi[0, 1] + 1j * Bi[1, 1]
        # chi on the face-pairing generators: fix the overall sign so that the cusp's chi-1 class agrees
        self.fchi = {g: (chi0[abs(g) - 1] if g > 0 else -chi0[abs(g) - 1]) for g in fpm}
        # sphere set, reduced modulo the lattice by right translation
        c = allm[:, 1, 0]; d = allm[:, 1, 1]
        ok = np.abs(c) > 1e-9
        allm, allx, c, d = allm[ok], allx[ok], c[ok], d[ok]
        r = 1 / np.abs(c)
        keep = r >= rmin
        allm, allx, c, d, r = allm[keep], allx[keep], c[keep], d[keep], r[keep]
        cen = -d / c
        cc = self.Binv @ np.vstack([cen.real, cen.imag])
        n1, n2 = np.floor(cc[0]), np.floor(cc[1])
        p = n1 * p1 + n2 * p2
        T = np.zeros((len(p), 2, 2), dtype=complex); T[:, 0, 0] = 1; T[:, 1, 1] = 1; T[:, 0, 1] = p
        allm = allm @ T
        allx = allx + n2.astype(int)
        cen = -allm[:, 1, 1] / allm[:, 1, 0]
        key = np.round(np.vstack([cen.real, cen.imag, r]).T, 7)
        _, idx = np.unique(key, axis=0, return_index=True)
        self.allcen = cen[idx].copy(); self.allr = r[idx].copy()
        self.sph_m = allm[idx]; self.sph_x = allx[idx]
        self.sph_c = cen[idx]; self.sph_r = r[idx]
        if verbose:
            print(f"{name}: tets {len(self.tets)}, face pairings {self.nfp}, simplified gens {len(self.sgens)}, "
                  f"lam {lam:.6f}, |p1| {abs(p1):.6f}, |p2| {abs(p2):.6f}, area {self.area:.6f}, spheres {len(self.sph_r)}")

    def floor(self, n=200, rcut=None, with_arg=False):
        """Floor height F(u, v) on an n x n grid over the parallelogram (cell centres), from every sphere and its
        lattice translates, updating only each disk's bounding box; optionally the index of the sphere achieving it."""
        us = (np.arange(n) + 0.5) / n
        U, V = np.meshgrid(us, us, indexing='ij')
        Fh = np.zeros((n, n)); Ah = -np.ones((n, n), dtype=int)
        hu = np.hypot(*self.Binv[0]); hv = np.hypot(*self.Binv[1])
        order = np.argsort(-self.sph_r)
        for k in order:
            r = self.sph_r[k]
            if rcut is not None and r < rcut: break
            cen = self.sph_c[k]
            cu, cv = self.Binv @ np.array([cen.real, cen.imag])
            du, dv = r * hu, r * hv
            for i in range(int(np.floor(cu - du)), int(np.floor(cu + du)) + 1):
                for j in range(int(np.floor(cv - dv)), int(np.floor(cv + dv)) + 1):
                    lo_u = max(0, int(np.floor((cu - du - i) * n))); hi_u = min(n, int(np.ceil((cu + du - i) * n)) + 1)
                    lo_v = max(0, int(np.floor((cv - dv - j) * n))); hi_v = min(n, int(np.ceil((cv + dv - j) * n)) + 1)
                    if lo_u >= hi_u or lo_v >= hi_v: continue
                    Uc = U[lo_u:hi_u, lo_v:hi_v] + i; Vc = V[lo_u:hi_u, lo_v:hi_v] + j
                    wx = Uc * self.p1.real + Vc * self.p2.real - cen.real
                    wy = Uc * self.p1.imag + Vc * self.p2.imag - cen.imag
                    hgt = np.sqrt(np.maximum(r * r - wx * wx - wy * wy, 0))
                    sub = Fh[lo_u:hi_u, lo_v:hi_v]
                    better = hgt > sub
                    sub[better] = hgt[better]
                    Ah[lo_u:hi_u, lo_v:hi_v][better] = k
        return (Fh, Ah) if with_arg else Fh

    def prune(self, n=300):
        """Drop spheres whose radius is below the floor's minimum (they are nowhere visible)."""
        Fh = self.floor(n)
        fmin = Fh.min()
        keep = self.sph_r >= fmin * (1 - 1e-6)
        self.sph_m, self.sph_x, self.sph_c, self.sph_r = self.sph_m[keep], self.sph_x[keep], self.sph_c[keep], self.sph_r[keep]
        return fmin

def complete_spheres(g, rounds=8, verbose=True, n=400):
    """Close the sphere set under products g T h of floor-visible elements (T a small lattice translation), until the
    Ford domain's volume matches SnapPy's and stops changing."""
    vol_ref = float(g.M.volume())
    hist = []
    for it in range(rounds):
        Fh, Ah = g.floor(n, with_arg=True)
        vol = (g.area / n ** 2) * np.sum(1.0 / (2 * np.maximum(Fh, 1e-300) ** 2)) if Fh.min() > 0 else np.inf
        hist.append(vol)
        if verbose: print(f"   sphere closure round {it}: spheres {len(g.sph_r)}, visible {len(np.unique(Ah[Ah >= 0]))}, floor min {Fh.min():.4f}, volume {vol:.6f} vs {vol_ref:.6f}", flush=True)
        if np.isfinite(vol) and abs(vol - vol_ref) < 2e-5 * vol_ref and it > 0 and abs(hist[-1] - hist[-2]) < 1e-7 * vol_ref:
            break
        vis = np.unique(Ah[Ah >= 0])
        Vm = g.sph_m[vis]; Vx = g.sph_x[vis]
        Vm = np.concatenate([Vm, np.linalg.inv(Vm)]); Vx = np.concatenate([Vx, -Vx])
        cands_m, cands_x = [], []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                p = i * g.p1 + j * g.p2
                T = np.array([[1, p], [0, 1]], dtype=complex)
                A = Vm @ T
                prod = np.einsum('aij,bjk->abik', A, Vm).reshape(-1, 2, 2)
                cands_m.append(prod); cands_x.append((Vx[:, None] + j + Vx[None, :]).reshape(-1))
        cm = np.concatenate(cands_m); cx = np.concatenate(cands_x)
        c = cm[:, 1, 0]
        ok = np.abs(c) > 1e-9
        cm, cx, c = cm[ok], cx[ok], c[ok]
        r = 1 / np.abs(c)
        fmin = Fh.min()
        keep = r >= max(fmin * 0.999, 0.05)
        cm, cx, r = cm[keep], cx[keep], r[keep]
        cen = -cm[:, 1, 1] / cm[:, 1, 0]
        cc = g.Binv @ np.vstack([cen.real, cen.imag])
        n1, n2 = np.floor(cc[0]), np.floor(cc[1])
        pp = n1 * g.p1 + n2 * g.p2
        T = np.zeros((len(pp), 2, 2), dtype=complex); T[:, 0, 0] = 1; T[:, 1, 1] = 1; T[:, 0, 1] = pp
        cm = cm @ T; cx = cx + n2.astype(int)
        cen = -cm[:, 1, 1] / cm[:, 1, 0]
        allm = np.concatenate([g.sph_m, cm]); allx = np.concatenate([g.sph_x, cx])
        allc = np.concatenate([g.sph_c, cen]); allr = np.concatenate([g.sph_r, r])
        key = np.round(np.vstack([allc.real, allc.imag, allr]).T, 7)
        _, idx = np.unique(key, axis=0, return_index=True)
        g.sph_m, g.sph_x, g.sph_c, g.sph_r = allm[idx], allx[idx], allc[idx], allr[idx]
        g.allcen = np.concatenate([g.allcen, cen]); g.allr = np.concatenate([g.allr, r])
        # keep the floor-visible spheres plus every sphere at least as large as the current floor minimum
        Fh2, Ah2 = g.floor(n, with_arg=True)
        vis2 = np.unique(Ah2[Ah2 >= 0])
        keep2 = np.zeros(len(g.sph_r), bool); keep2[vis2] = True
        if Fh2.min() > 0: keep2 |= g.sph_r >= Fh2.min() * 0.999
        g.sph_m, g.sph_x, g.sph_c, g.sph_r = g.sph_m[keep2], g.sph_x[keep2], g.sph_c[keep2], g.sph_r[keep2]
    return hist

# ---- from the instrument's hejhal part ----
class Harmonic:
    def __init__(self, g, R, Y, oversample=2.0, verbose=True):
        self.g = g
        self.R, self.Y = R, Y
        # modes: one of each +-mu pair
        mmax = int(np.ceil(R / min(abs(g.mu1), abs(g.mu2)) * 2)) + 2
        modes = []
        for m1 in range(-mmax, mmax + 1):
            for m2 in range(-mmax, mmax + 1):
                if (m1, m2) <= (0, 0) and not (m1 == 0 and m2 == 0) and (m1, m2) < (0, 0):
                    continue
                if m1 == 0 and m2 == 0: continue
                if (m1 < 0) or (m1 == 0 and m2 < 0): continue
                mu = m1 * g.mu1 + m2 * g.mu2
                if abs(mu) <= R: modes.append(mu)
        self.mu = np.array(modes)
        self.nm = len(self.mu)
        # sphere elements with their 9 translates
        S = []
        for A, x, cen, r in zip(g.sph_m, g.sph_x, g.sph_c, g.sph_r):
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    p = i * g.p1 + j * g.p2
                    T = np.array([[1, -p], [0, 1]], dtype=complex)
                    S.append((A @ T, x - j))
        self.Sm = np.array([s[0] for s in S]); self.Sx = np.array([s[1] for s in S])
        # collocation points: uniform grid over the parallelogram at height Y
        nunk = 2 * self.nm
        npts = int(oversample * nunk)
        n2 = int(np.ceil(np.sqrt(npts * abs(g.p2) / abs(g.p1))))
        n1 = int(np.ceil(npts / n2))
        u = (np.arange(n1) + 0.5) / n1; v = (np.arange(n2) + 0.5) / n2
        U, V = np.meshgrid(u, v, indexing='ij')
        w = (U * g.p1 + V * g.p2).ravel()
        z = np.full(w.shape, Y)
        ws, zs, xs = self.pullback(w, z)
        assert np.all(zs > Y * (1 + 1e-9)), "a collocation point was not pulled back"
        Aq = np.empty((len(w), nunk))
        for i in range(0, len(w), 2000):                  # by rows (memory); each row is computed on its own
            Aq[i:i + 2000] = self.basis(w[i:i + 2000], z[i:i + 2000]) - self.basis(ws[i:i + 2000], zs[i:i + 2000])
        rhs = self.lin(ws) - xs - self.lin(w)
        sol, res, rk, sv = np.linalg.lstsq(Aq, rhs, rcond=None)
        self.coef = sol
        self.resid = np.sqrt(np.mean((Aq @ sol - rhs) ** 2))
        self.cond = sv[0] / sv[-1]
        self.zmin_pulled = zs.min()
        if verbose:
            print(f"Hejhal: modes {self.nm} (unknowns {nunk}), points {len(w)}, Y {Y}, R {R}, rms residual {self.resid:.2e}, "
                  f"cond {self.cond:.2e}, min pulled height {zs.min():.4f}")

    def lin(self, w):
        return (np.conj(self.g.nu) * w).real

    def basis(self, w, z):
        ph = 2 * np.pi * (np.conj(self.mu)[None, :] * w[:, None]).real
        kk = 2 * np.pi * np.abs(self.mu)[None, :] * z[:, None]
        rad = z[:, None] * k1e(kk) * np.exp(-kk)
        return np.concatenate([rad * np.cos(ph), rad * np.sin(ph)], axis=1)

    def reduce(self, w):
        """Translate w into the fundamental parallelogram; return w', the chi of the translation applied."""
        g = self.g
        cu = g.Binv @ np.vstack([w.real, w.imag])
        n1, n2 = np.floor(cu[0]), np.floor(cu[1])
        return w - n1 * g.p1 - n2 * g.p2, -n2.astype(int)

    def pullback(self, w, z, maxit=200, chunk=8000):
        """Map (w, z) by gamma into the Ford domain; return (w*, z*, chi(gamma)). Pointwise, in chunks (memory)."""
        w = np.atleast_1d(np.asarray(w, dtype=complex)); z = np.atleast_1d(np.asarray(z, dtype=float))
        shp = np.broadcast(w, z).shape
        w = np.broadcast_to(w, shp).ravel(); z = np.broadcast_to(z, shp).ravel()
        W = np.empty(len(w), dtype=complex); Z = np.empty(len(w)); X = np.empty(len(w), dtype=int)
        for i in range(0, len(w), chunk):
            W[i:i + chunk], Z[i:i + chunk], X[i:i + chunk] = self._pullback1(w[i:i + chunk], z[i:i + chunk], maxit)
        return W.reshape(shp), Z.reshape(shp), X.reshape(shp)

    def _pullback1(self, w, z, maxit=200):
        w = np.array(w, dtype=complex).copy(); z = np.array(z, dtype=float).copy()
        x = np.zeros(w.shape, dtype=int)
        active = np.ones(w.shape, dtype=bool)
        for it in range(maxit):
            w2, dx = self.reduce(w)
            w = w2; x = x + dx
            idx = np.where(active)[0]
            if len(idx) == 0: break
            c = self.Sm[:, 1, 0][None, :]; d = self.Sm[:, 1, 1][None, :]
            den = np.abs(c * w[idx, None] + d) ** 2 + np.abs(c) ** 2 * z[idx, None] ** 2
            zz = z[idx, None] / den
            k = np.argmax(zz, axis=1)
            best = zz[np.arange(len(idx)), k]
            up = best > z[idx] * (1 + 1e-12)
            if not np.any(up):
                break
            ii = idx[up]; kk = k[up]
            A = self.Sm[kk]
            a, b, cc, dd = A[:, 0, 0], A[:, 0, 1], A[:, 1, 0], A[:, 1, 1]
            cw_d = cc * w[ii] + dd
            dn = np.abs(cw_d) ** 2 + np.abs(cc) ** 2 * z[ii] ** 2
            w[ii] = ((a * w[ii] + b) * np.conj(cw_d) + a * np.conj(cc) * z[ii] ** 2) / dn
            z[ii] = z[ii] / dn
            x[ii] = x[ii] + self.Sx[kk]
            active[:] = False; active[ii] = True
        else:
            raise RuntimeError("pullback did not converge")
        w, dx = self.reduce(w)
        return w, z, x + dx

    def eval_direct(self, w, z, chunk=3000):
        out = np.empty(len(w))
        a = self.coef[:self.nm]; b = self.coef[self.nm:]
        twopi = 2 * np.pi
        for i in range(0, len(w), chunk):
            ww = w[i:i + chunk]; zz = z[i:i + chunk]
            ph = twopi * (np.conj(self.mu)[None, :] * ww[:, None]).real
            kk = twopi * np.abs(self.mu)[None, :] * zz[:, None]
            rad = zz[:, None] * k1e(kk) * np.exp(-kk)
            out[i:i + chunk] = (rad * (np.cos(ph) * a[None, :] + np.sin(ph) * b[None, :])).sum(axis=1)
        return self.lin(w) + out

    def __call__(self, w, z):
        w = np.atleast_1d(np.asarray(w, dtype=complex)); z = np.atleast_1d(np.asarray(z, dtype=float))
        shp = np.broadcast(w, z).shape
        ws, zs, xs = self.pullback(w, z)
        return (self.eval_direct(ws.ravel(), zs.ravel()) - xs.ravel()).reshape(shp)

# ---- from the instrument's mesh3d part ----
def mink(X, Y):
    return -X[..., 0] * Y[..., 0] + X[..., 1] * Y[..., 1] + X[..., 2] * Y[..., 2] + X[..., 3] * Y[..., 3]

def normalize(X):
    return X / np.sqrt(-mink(X, X))[..., None]

def uhs_to_hyp(w, z):
    w = np.asarray(w); z = np.asarray(z)
    a2 = np.abs(w) ** 2 + z * z
    return np.stack([(a2 + 1) / (2 * z), w.real / z, w.imag / z, (a2 - 1) / (2 * z)], axis=-1)

def hyp_to_uhs(X):
    z = 1.0 / (X[..., 0] - X[..., 3])
    return (X[..., 1] + 1j * X[..., 2]) * z, z

def null_of(xi):
    if xi is None: return np.array([1.0, 0.0, 0.0, 1.0])
    A = abs(xi) ** 2
    return np.array([(A + 1) / 2, xi.real, xi.imag, (A - 1) / 2])

VERTS = [simplex.V0, simplex.V1, simplex.V2, simplex.V3]

FACES = [simplex.F0, simplex.F1, simplex.F2, simplex.F3]       # face i is opposite vertex i

class TruncTet:
    """Barycentric subdivision of one truncated ideal tetrahedron, refined r times (red refinement)."""
    def __init__(self, Ntil, H):
        self.N = Ntil                    # 4 normalised null vectors
        self.H = H
        self.X = []                      # node positions (hyperboloid)
        self.hor = []                    # index of the horosphere the node lies on, or -1
        self.fmask = []                  # bitmask of the hexagon faces (opposite vertex i -> bit i) containing the node
        self.T = []                      # simplices (4 node indices)
        self._build()

    def _add(self, X, hor, fmask):
        self.X.append(X); self.hor.append(hor); self.fmask.append(fmask)
        return len(self.X) - 1

    def proj_hor(self, Y, i):
        Ni = self.N[i]
        p = -mink(Y, Ni)
        s = (p * p * self.H * self.H - 1) / (2 * p)
        return normalize(Y + s * Ni)

    def _build(self):
        N, H = self.N, self.H
        q = lambda i, j: -mink(N[i], N[j])
        faces_of_vertex = lambda i: [f for f in range(4) if f != i]           # hexagon faces containing vertex i
        # truncation points: vertex i, edge towards j
        P = {}
        for i in range(4):
            for j in range(4):
                if i == j: continue
                X = (H / 2) * N[i] + (1 / (q(i, j) * H)) * N[j]
                fm = sum(1 << f for f in range(4) if f != i and f != j)       # faces containing edge ij
                P[(i, j)] = self._add(X, i, fm)
        # truncated ideal edge midpoints
        E = {}
        for i in range(4):
            for j in range(i + 1, 4):
                fm = sum(1 << f for f in range(4) if f != i and f != j)
                E[(i, j)] = self._add(normalize(N[i] + N[j]), -1, fm)
        # horocyclic arc midpoints: on face f (opposite vertex f), at vertex i, between edges ij and ik
        A = {}
        for f in range(4):
            vs = [v for v in range(4) if v != f]
            for i in vs:
                j, k = [v for v in vs if v != i]
                Y = normalize(self.X[P[(i, j)]] + self.X[P[(i, k)]])
                A[(f, i)] = self._add(self.proj_hor(Y, i), i, 1 << f)
        # cap centres (vertex i) and hexagon centres (face f)
        C = {}
        for i in range(4):
            js = [j for j in range(4) if j != i]
            Y = normalize(sum(self.X[P[(i, j)]] for j in js))
            C[i] = self._add(self.proj_hor(Y, i), i, 0)
        Fc = {}
        for f in range(4):
            vs = [v for v in range(4) if v != f]
            Fc[f] = self._add(normalize(sum(N[v] for v in vs)), -1, 1 << f)
        O = self._add(normalize(N[0] + N[1] + N[2] + N[3]), -1, 0)
        # simplices of the barycentric subdivision
        for f in range(4):                         # hexagons: edges are 3 truncated edges and 3 arcs
            vs = [v for v in range(4) if v != f]
            for a in range(3):
                for b in range(a + 1, 3):
                    i, j = vs[a], vs[b]
                    e = E[(min(i, j), max(i, j))]
                    for vtx in (P[(i, j)], P[(j, i)]):
                        self.T.append((O, Fc[f], e, vtx))
            for i in vs:
                j, k = [v for v in vs if v != i]
                arc = A[(f, i)]
                for vtx in (P[(i, j)], P[(i, k)]):
                    self.T.append((O, Fc[f], arc, vtx))
        for i in range(4):                         # caps: edges are the 3 arcs at vertex i
            fs = [f for f in range(4) if f != i]
            for f in fs:
                arc = A[(f, i)]
                vs = [v for v in range(4) if v != f and v != i]
                for j in vs:
                    self.T.append((O, C[i], arc, P[(i, j)]))
        self.X = np.array(self.X); self.hor = np.array(self.hor); self.fmask = np.array(self.fmask)
        self.T = np.array(self.T)

    def refine(self):
        X = list(self.X); hor = list(self.hor); fm = list(self.fmask)
        mid = {}
        def m(a, b):
            key = (a, b) if a < b else (b, a)
            if key in mid: return mid[key]
            Y = normalize(X[a] + X[b])
            hh = -1
            if hor[a] >= 0 and hor[a] == hor[b]:
                hh = hor[a]; Y = self.proj_hor(Y, hh)
            X.append(Y); hor.append(hh); fm.append(fm[a] & fm[b])
            mid[key] = len(X) - 1
            return mid[key]
        T2 = []
        for (x0, x1, x2, x3) in self.T:
            x01, x02, x03, x12, x13, x23 = m(x0, x1), m(x0, x2), m(x0, x3), m(x1, x2), m(x1, x3), m(x2, x3)
            T2 += [(x0, x01, x02, x03), (x01, x1, x12, x13), (x02, x12, x2, x23), (x03, x13, x23, x3),
                   (x01, x02, x03, x13), (x01, x02, x12, x13), (x02, x03, x13, x23), (x02, x12, x13, x23)]
        self.X = np.array(X); self.hor = np.array(hor); self.fmask = np.array(fm); self.T = np.array(T2)

def mobius_hyp(A):
    """The SO(3,1) matrix of A in SL2C acting on the hyperboloid model used here."""
    # act on a basis of Hermitian matrices: X <-> [[X0+X3, X1+iX2],[X1-iX2, X0-X3]] (det = -<X,X>)
    E = [np.array([[1, 0], [0, 1]]), np.array([[0, 1], [1, 0]]), np.array([[0, 1j], [-1j, 0]]), np.array([[1, 0], [0, -1]])]
    # the convention must match uhs_to_hyp; fix it numerically below
    Ah = A.conj().T
    Mt = np.zeros((4, 4))
    for c in range(4):
        Y = A @ E[c] @ Ah
        Mt[0, c] = ((Y[0, 0] + Y[1, 1]) / 2).real
        Mt[3, c] = ((Y[0, 0] - Y[1, 1]) / 2).real
        Mt[1, c] = ((Y[0, 1] + Y[1, 0]) / 2).real
        Mt[2, c] = ((Y[0, 1] - Y[1, 0]) / (2j)).real
    return Mt

class Mesh:
    def __init__(self, g, H, r, verbose=True):
        self.g = g; self.H = H
        mc = g.mc
        nt = len(g.tets)
        # normalised null vectors of every developed vertex
        Bi = g.Binv
        def cmod(xi):
            cu = Bi @ np.array([xi.real, xi.imag])
            return (cu[0] % 1.0, cu[1] % 1.0)
        cen_keys = {}
        for cen, rr in zip(g.allcen, g.allr):
            cen_keys.setdefault(tuple(np.round(cmod(cen), 6)), rr)
        # Amendment 2: the horoball radius (1/|c|) at every developed vertex. The word search can miss vertices whose
        # element is longer than it reaches (k = 3, 4), so the radii found by the lookup (and the vertices at
        # infinity) seed a propagation across the fundamental polyhedron's face pairings: fpm[k] carries the out-face's
        # vertices to the in-face's, and for A = [[a, b], [c, d]] taking x_b to x_a the radius is r_a = r_b / |c x_b + d|
        # (r_a = 1/|c| when x_b is infinity). A vertex reached twice, or both found and reached, must agree to 1e-9.
        tets_mc = list(mc.Tetrahedra)
        cls_pt = {}
        for ti, tt_ in enumerate(tets_mc):
            for vi, v in enumerate(simplex.ZeroSubsimplices):
                cls_pt.setdefault(tt_.Class[v].Index, g.tets[ti][vi])
        def lookup(xi):
            key = tuple(np.round(cmod(xi), 6))
            if key in cen_keys: return cen_keys[key]
            k2 = min(cen_keys, key=lambda k: min(abs(k[0] - key[0]) % 1, 1 - abs(k[0] - key[0]) % 1) + min(abs(k[1] - key[1]) % 1, 1 - abs(k[1] - key[1]) % 1))
            d2 = min(abs(k2[0] - key[0]) % 1, 1 - abs(k2[0] - key[0]) % 1) + min(abs(k2[1] - key[1]) % 1, 1 - abs(k2[1] - key[1]) % 1)
            return cen_keys[k2] if d2 < 1e-5 else None
        rad = {}
        for cl, x in cls_pt.items():
            if x is not None:
                r0 = lookup(x)
                if r0 is not None: rad[cl] = r0
        self.nlookup = len(rad)
        adj = {}
        for kk, lst in mc.Generators.items():
            if kk < 0: continue
            for (cin, cout), perm in lst:
                for v in simplex.ZeroSubsimplices:
                    if simplex.is_subset(v, cin.Subsimplex):
                        a_ = cin.Tetrahedron.Class[v].Index; b_ = cout.Tetrahedron.Class[perm.image(v)].Index
                        adj.setdefault(b_, []).append((a_, g.fpm[kk]))
                        adj.setdefault(a_, []).append((b_, g.fpm[-kk]))
        known = set(rad) | {cl for cl, x in cls_pt.items() if x is None}
        queue = deque(sorted(known))
        worst = 0.0
        while queue:
            xcl = queue.popleft(); xb = cls_pt[xcl]
            for ycl, A in adj.get(xcl, []):
                ya = cls_pt[ycl]
                if ya is None: continue
                r_new = 1 / abs(A[1, 0]) if xb is None else rad[xcl] / abs(A[1, 0] * xb + A[1, 1])
                if ycl in rad:
                    worst = max(worst, abs(rad[ycl] - r_new) / rad[ycl])
                else:
                    rad[ycl] = r_new; queue.append(ycl)
        assert all(x is None or cl in rad for cl, x in cls_pt.items()), "a developed vertex was not reached"
        assert worst < 1e-9, ("horoball radii disagree", worst)
        self.radius_agreement = worst
        self.Ntil = []
        for t in range(nt):
            Ns = []
            for vi, xi in enumerate(g.tets[t]):
                if xi is None:
                    Ns.append(null_of(None))
                else:
                    rr = rad[tets_mc[t].Class[simplex.ZeroSubsimplices[vi]].Index]      # radius 1/|c|
                    Ns.append(null_of(xi) * 2 / rr ** 2)
            self.Ntil.append(np.array(Ns))
        self.tt = [TruncTet(self.Ntil[t], H) for t in range(nt)]
        for _ in range(r):
            for T in self.tt: T.refine()
        # face pairings: (tet a, face Fa) -> (tet b, face Fb), with an SO(3,1) matrix taking a's frame to b's
        self.pairs = []
        for t in mc.Tetrahedra:
            for fi, F in enumerate(FACES):
                if t.Neighbor[F] is not None:
                    S = t.Neighbor[F]; perm = t.Gluing[F]
                    fj = FACES.index(perm.image(F))
                    if (t.Index, fi) < (S.Index, fj):
                        self.pairs.append((t.Index, fi, S.Index, fj, np.eye(4)))
        for k, lst in mc.Generators.items():
            if k < 0: continue
            for (ca, cb), perm in lst:
                ta, fa = ca.Tetrahedron.Index, FACES.index(ca.Subsimplex)
                tb, fb = cb.Tetrahedron.Index, FACES.index(cb.Subsimplex)
                # decide whether fpm[k] or its inverse maps face a onto face b (compare the null vectors as lines)
                best = None
                for A in (g.fpm[k], np.linalg.inv(g.fpm[k])):
                    Lm = mobius_hyp(A)
                    va = [i for i in range(4) if i != fa]; vb = [i for i in range(4) if i != fb]
                    img = [Lm @ self.Ntil[ta][i] for i in va]
                    err = 0
                    for v in img:
                        e = min(np.linalg.norm(np.cross(v[1:] / v[0], self.Ntil[tb][j][1:] / self.Ntil[tb][j][0])) +
                                abs(1 - (v[1:] / v[0]) @ (self.Ntil[tb][j][1:] / self.Ntil[tb][j][0])) for j in vb)
                        err += e
                    if best is None or err < best[0]: best = (err, Lm)
                assert best[0] < 1e-8, ("face pairing mismatch", k, best[0])
                self.pairs.append((ta, fa, tb, fb, best[1]))
        # merge nodes across glued faces
        offs = np.cumsum([0] + [len(T.X) for T in self.tt])
        self.offs = offs
        parent = np.arange(offs[-1])
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        from scipy.spatial import cKDTree
        maxd = 0
        for ta, fa, tb, fb, Lm in self.pairs:
            Ia = np.where((self.tt[ta].fmask >> fa) & 1)[0]
            Ib = np.where((self.tt[tb].fmask >> fb) & 1)[0]
            Xa = self.tt[ta].X[Ia] @ Lm.T
            Xb = self.tt[tb].X[Ib]
            assert len(Ia) == len(Ib), (ta, fa, tb, fb, len(Ia), len(Ib))
            tree = cKDTree(Xb)
            d, j = tree.query(Xa)
            maxd = max(maxd, d.max() / np.abs(Xb).max())
            assert len(set(j)) == len(j), "non-injective face match"
            for ia, jb in zip(Ia, j):
                ra, rb = find(offs[ta] + ia), find(offs[tb] + Ib[jb])
                if ra != rb: parent[max(ra, rb)] = min(ra, rb)
        self.gid = np.array([find(a) for a in range(offs[-1])])
        uniq = np.unique(self.gid)
        self.nglobal = len(uniq)
        if verbose:
            print(f"mesh: H {H}, refinement {r}, simplices {sum(len(T.T) for T in self.tt)}, local nodes {offs[-1]}, "
                  f"global nodes {self.nglobal}, face-match max relative distance {maxd:.1e}, pairs {len(self.pairs)}")

# ---- from the instrument's surface part ----
def geodesic_point(Xa, Xb, s):
    c = -mink(Xa, Xb)
    d = np.arccosh(np.maximum(c, 1.0))
    sd = np.sinh(d)
    small = d < 1e-12
    with np.errstate(invalid='ignore', divide='ignore'):
        A = np.where(small, 1 - s, np.sinh((1 - s) * d) / np.where(small, 1, sd))
        B = np.where(small, s, np.sinh(s * d) / np.where(small, 1, sd))
    return A[..., None] * Xa + B[..., None] * Xb

def node_values(Ms, Hf, chunk=20000):
    vals = []
    for T in Ms.tt:
        w, z = hyp_to_uhs(T.X)
        v = np.empty(len(w))
        for i in range(0, len(w), chunk):
            v[i:i + chunk] = Hf(w[i:i + chunk], z[i:i + chunk])
        vals.append(v)
    return vals

# ---- from the instrument's surf2 part ----
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

EIDX = {e: i for i, e in enumerate(EDGES)}

def _table():
    tab = {}
    for code in range(16):
        pos = [(code >> i) & 1 for i in range(4)]
        P = [i for i in range(4) if pos[i]]; Nn = [i for i in range(4) if not pos[i]]
        tris = []
        if len(P) in (1, 3):
            a = P[0] if len(P) == 1 else Nn[0]
            o = [i for i in range(4) if i != a]
            tris = [[(min(a, o[0]), max(a, o[0])), (min(a, o[1]), max(a, o[1])), (min(a, o[2]), max(a, o[2]))]]
        elif len(P) == 2:
            p0, p1 = P; n0, n1 = Nn
            e = lambda x, y: (min(x, y), max(x, y))
            tris = [[e(p0, n0), e(p0, n1), e(p1, n1)], [e(p0, n0), e(p1, n1), e(p1, n0)]]
        tab[code] = [[EIDX[x] for x in t] for t in tris]
    return tab

TABLE = _table()

# ---- from the instrument's surf3 part ----
class Surf:
    def __init__(self, Ms, Hf, s, vals=None, eps=1e-6, umin=1e-2):
        if vals is None: vals = node_values(Ms, Hf)
        # each global node's snapping threshold: max(eps, umin x the largest |delta h| on its mesh edges), so that no
        # crossing falls within umin of an edge's end (marching tetrahedra's needles, whose angles the lengths' rounding
        # decides, do not arise); the threshold is a property of the node, the same in every frame
        maxd = np.zeros(Ms.gid.max() + 1)
        for t, T in enumerate(Ms.tt):
            for (i, j) in EDGES:
                d = np.abs(vals[t][T.T[:, i]] - vals[t][T.T[:, j]])
                np.maximum.at(maxd, Ms.gid[Ms.offs[t] + T.T[:, i]], d)
                np.maximum.at(maxd, Ms.gid[Ms.offs[t] + T.T[:, j]], d)
        epsg = np.maximum(eps, umin * maxd)
        EPS = [epsg[Ms.gid[Ms.offs[t] + np.arange(len(vals[t]))]] for t in range(len(Ms.tt))]
        F_frame, F_simp, F_edges, F_n = [], [], [], []
        for t, T in enumerate(Ms.tt):
            hs = vals[t][T.T] - s
            ep = EPS[t][T.T]
            # integer levels n with some f = hs - n < -eps and some f >= -eps (eps per node)
            q = np.floor(hs + ep)
            lo = q.min(axis=1); hi = q.max(axis=1)
            cand = np.where(hi > lo)[0]
            assert np.all(hi[cand] - lo[cand] == 1), "a simplex spans two levels: refine"
            n = hi[cand]
            f = hs[cand] - n[:, None]
            code = ((f >= -ep[cand]).astype(int) * (1 << np.arange(4))).sum(axis=1)
            for c in range(1, 15):
                sel = np.where(code == c)[0]
                for tr in TABLE[c]:
                    F_frame.append(np.full(len(sel), t)); F_simp.append(cand[sel])
                    F_edges.append(np.tile(np.array(tr), (len(sel), 1))); F_n.append(n[sel])
        F_frame = np.concatenate(F_frame); F_simp = np.concatenate(F_simp)
        F_edges = np.concatenate(F_edges); F_n = np.concatenate(F_n)
        nF = len(F_frame)
        E = np.array(EDGES)
        simp = np.stack([Ms.tt[t].T[si] for t, si in zip(F_frame, F_simp)])
        la = simp[np.arange(nF)[:, None], E[F_edges, 0]]; lb = simp[np.arange(nF)[:, None], E[F_edges, 1]]
        offs = Ms.offs
        fa = np.stack([vals[t][la[i]] for i, t in enumerate(F_frame)]) - s - F_n[:, None]
        fb = np.stack([vals[t][lb[i]] for i, t in enumerate(F_frame)]) - s - F_n[:, None]
        ea = np.stack([EPS[t][la[i]] for i, t in enumerate(F_frame)]); eb = np.stack([EPS[t][lb[i]] for i, t in enumerate(F_frame)])
        # orient each edge so that 'p' is the non-negative end
        swap = fa < -ea
        lp = np.where(swap, lb, la); lq = np.where(swap, la, lb)
        fp = np.where(swap, fb, fa); fq = np.where(swap, fa, fb)
        snapped = np.abs(fp) < np.where(swap, eb, ea)
        gp = Ms.gid[offs[F_frame][:, None] + lp]; gq = Ms.gid[offs[F_frame][:, None] + lq]
        M1 = Ms.offs[-1] + 1
        keys = np.where(snapped, gp.astype(np.int64) * M1 + gp, np.minimum(gp, gq).astype(np.int64) * M1 + np.maximum(gp, gq))
        uk, first, vid = np.unique(keys.ravel(), return_index=True, return_inverse=True)
        vid = vid.reshape(nF, 3)
        nv = len(uk)
        fi = first // 3; fk = first % 3
        dt = F_frame[fi]; dlp = lp[fi, fk]; dlq = lq[fi, fk]; dn = F_n[fi]; dsnap = snapped[fi, fk]
        dgp = gp[fi, fk]
        # roots for non-snapped vertices: parameter u from p (u=0) to q (u=1)
        ns = np.where(~dsnap)[0]
        u = np.zeros(nv)
        if len(ns):
            Xa = np.stack([Ms.tt[t].X[i] for t, i in zip(dt[ns], dlp[ns])]); Xb = np.stack([Ms.tt[t].X[i] for t, i in zip(dt[ns], dlq[ns])])
            ga_ = np.array([vals[t][i] for t, i in zip(dt[ns], dlp[ns])]) - s - dn[ns]
            gb_ = np.array([vals[t][i] for t, i in zip(dt[ns], dlq[ns])]) - s - dn[ns]
            ua = np.zeros(len(ns)); ub = np.ones(len(ns)); side = np.zeros(len(ns), int)
            for it in range(100):
                uu = ua - ga_ * (ub - ua) / (gb_ - ga_)
                uu = np.where((uu <= ua) | (uu >= ub) | ~np.isfinite(uu), 0.5 * (ua + ub), uu)
                X = geodesic_point(Xa, Xb, uu); w, z = hyp_to_uhs(X)
                fu = Hf(w, z) - s - dn[ns]
                left = np.sign(fu) == np.sign(ga_)
                ga_new = np.where(left, fu, np.where(side == -1, ga_ * 0.5, ga_))
                gb_new = np.where(left, np.where(side == 1, gb_ * 0.5, gb_), fu)
                ua = np.where(left, uu, ua); ub = np.where(left, ub, uu)
                ga_, gb_ = ga_new, gb_new; side = np.where(left, 1, -1)
                if np.all((np.abs(fu) < 1e-14) | (ub - ua < 1e-15)): break
            u[ns] = np.where(np.abs(ga_) < np.abs(gb_), ua, ub)
            X = geodesic_point(Xa, Xb, u[ns]); w, z = hyp_to_uhs(X)
            self.res = np.abs(Hf(w, z) - s - dn[ns]).max()
        else:
            self.res = 0.0
        # per-triangle positions in the triangle's own frame
        P3 = np.empty((nF, 3, 4))
        for k in range(3):
            v = vid[:, k]
            XP = np.stack([Ms.tt[t].X[i] for t, i in zip(F_frame, lp[:, k])])
            XQ = np.stack([Ms.tt[t].X[i] for t, i in zip(F_frame, lq[:, k])])
            # the stored u runs from the defining copy's p; p is the non-negative end in every copy, so u carries over
            uu = np.where(snapped[:, k], 0.0, u[v])
            P3[:, k] = geodesic_point(XP, XQ, uu)
        # snapped vertices: move from the node onto the exact level along grad h (intrinsic, so frames agree)
        if snapped.any():
            kk, mm = np.where(snapped)
            Y, rres, tmax = project(Hf, P3[kk, mm], (s + F_n)[kk])
            P3[kk, mm] = Y
            self.snap_move = tmax
        else:
            self.snap_move = 0.0
        # orientation by the hyperboloid determinant against a positive vertex of the simplex
        simpX = np.stack([Ms.tt[t].X[sm] for t, sm in zip(F_frame, simp)])
        hsim = np.stack([vals[t][sm] for t, sm in zip(F_frame, simp)]) - s - F_n[:, None]
        esim = np.stack([EPS[t][sm] for t, sm in zip(F_frame, simp)])
        wpos = (hsim >= -esim) & (np.abs(hsim) >= esim)       # strictly positive vertices
        # every triangle's simplex has at least one negative vertex and one non-negative; use the negative side if
        # no strictly positive vertex exists
        haspos = wpos.any(axis=1)
        wneg = hsim < -esim
        Xpos = np.where(haspos[:, None], (simpX * wpos[:, :, None]).sum(1) / np.maximum(wpos.sum(1), 1)[:, None],
                        (simpX * wneg[:, :, None]).sum(1) / np.maximum(wneg.sum(1), 1)[:, None])
        sgn = np.where(haspos, 1.0, -1.0)
        dets = np.linalg.det(np.stack([P3[:, 0], P3[:, 1], P3[:, 2], Xpos], axis=1)) * sgn
        flip = dets < 0
        vid[flip] = vid[flip][:, [0, 2, 1]]; P3[flip] = P3[flip][:, [0, 2, 1]]
        # drop degenerate triangles (two equal vertices)
        good = (vid[:, 0] != vid[:, 1]) & (vid[:, 1] != vid[:, 2]) & (vid[:, 2] != vid[:, 0])
        vid, P3 = vid[good], P3[good]
        lev = (s + F_n)[good]
        self.frame = F_frame[good]
        u2, inv = np.unique(vid.ravel(), return_inverse=True)
        self.tri = inv.reshape(vid.shape); self.P3 = P3; self.nv = len(u2); self.level = lev
        self.nsnap = int(dsnap.sum())
        self.L = lengths(P3)

    def check(self):
        from collections import Counter
        he = Counter()
        for a, b, c in self.tri:
            he[(a, b)] += 1; he[(b, c)] += 1; he[(c, a)] += 1
        und = Counter()
        for (u, v), c in he.items(): und[(min(u, v), max(u, v))] += c
        bnd = sum(1 for v in und.values() if v == 1); nm = sum(1 for v in und.values() if v > 2)
        incons = sum(1 for (u, v), c in und.items() if c == 2 and he[(u, v)] != 1)
        chi = self.nv - len(und) + len(self.tri)
        adj = {}
        for (u, v), c in und.items():
            if c == 1:
                adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
        seen = set(); loops = 0
        for v0 in adj:
            if v0 in seen: continue
            loops += 1; stack = [v0]
            while stack:
                x = stack.pop()
                if x in seen: continue
                seen.add(x); stack += adj[x]
        return dict(chi=chi, boundary=bnd, loops=loops, nonmanifold=nm, inconsistent=incons, V=self.nv, F=len(self.tri))

# ---- from the instrument's subdiv part ----
def hgrad_dir(Hf, X):
    w, z = hyp_to_uhs(X)
    eps = 1e-6 * z
    gx = (Hf(w + eps, z) - Hf(w - eps, z)) / (2 * eps)
    gy = (Hf(w + 1j * eps, z) - Hf(w - 1j * eps, z)) / (2 * eps)
    gz = (Hf(w, z + eps) - Hf(w, z - eps)) / (2 * eps)
    # tangent vector in uhs coordinates (hyperbolic gradient direction = z^2 * Euclidean gradient, same direction)
    vx, vy, vz = gx, gy, gz
    nrm = np.sqrt(vx * vx + vy * vy + vz * vz)
    vx, vy, vz = vx / nrm, vy / nrm, vz / nrm
    t = 1e-6 * z
    Xp = uhs_to_hyp(w + t * (vx + 1j * vy), z + t * vz)
    Xm = uhs_to_hyp(w - t * (vx + 1j * vy), z - t * vz)
    dX = (Xp - Xm) / (2 * t[:, None])
    dX = dX + mink(dX, X)[:, None] * X           # project to the tangent space at X
    V = dX / np.sqrt(mink(dX, dX))[:, None]
    ghyp = z * np.sqrt(gx * gx + gy * gy + gz * gz)
    return V, ghyp

def project(Hf, X, level, iters=8):
    V, g = hgrad_dir(Hf, X)
    def at(t):
        Y = np.cosh(t)[:, None] * X + np.sinh(t)[:, None] * V
        w, z = hyp_to_uhs(Y)
        return Hf(w, z) - level, Y
    f0, _ = at(np.zeros(len(X)))
    t0 = np.zeros(len(X)); t1 = -f0 / g
    f1, Y = at(t1)
    for _ in range(iters):
        den = f1 - f0
        t2 = np.where(np.abs(den) > 1e-300, t1 - f1 * (t1 - t0) / np.where(np.abs(den) > 1e-300, den, 1), t1)
        t0, f0 = t1, f1
        t1 = t2
        f1, Y = at(t1)
        if np.all(np.abs(f1) < 1e-13): break
    return Y, np.abs(f1).max(), np.abs(t1).max()

def subdivide(tri, P3, levels_per_tri, Hf, frames=None):
    """tri: (F,3) vertex ids; P3: (F,3,4) positions in each triangle's frame; levels_per_tri: (F,) the level value
    (s + n) in that frame; frames: (F,) frame labels (positions are shared only within a frame). Each new vertex is
    projected once per (frame, edge). Returns refined tri, P3, levels, frames."""
    F = len(tri)
    nv = tri.max() + 1
    if frames is None: frames = np.zeros(F, dtype=np.int64)
    pairs = [(1, 2), (2, 0), (0, 1)]                 # midpoint m opposite vertex m
    A_ = np.concatenate([np.minimum(tri[:, i], tri[:, j]) for (i, j) in pairs])
    B_ = np.concatenate([np.maximum(tri[:, i], tri[:, j]) for (i, j) in pairs])
    Fr = np.concatenate([frames] * 3)
    Lv = np.concatenate([levels_per_tri] * 3)
    M = np.concatenate([normalize(P3[:, i] + P3[:, j]) for (i, j) in pairs])
    # one projection per (frame, edge, local copy): a frame whose faces are glued to each other holds the same surface
    # edge at two places, so the unprojected midpoint (rounded to 1e-8) is part of the key
    key = np.concatenate([np.stack([Fr.astype(np.int64), A_.astype(np.int64), B_.astype(np.int64)], 1),
                          np.round(M * 1e8).astype(np.int64)], axis=1)
    uk, first, inv = np.unique(key, axis=0, return_index=True, return_inverse=True)
    inv = inv.ravel()
    Y, res, tmax = project(Hf, M[first], Lv[first])
    mids_flat = Y[inv]
    mids = np.stack([mids_flat[:F], mids_flat[F:2 * F], mids_flat[2 * F:]], axis=1)
    ekey = A_.astype(np.int64) * (nv + 1) + B_
    uk2, inv2 = np.unique(ekey, return_inverse=True)
    newid = nv + inv2.reshape(3, F).T
    v0, v1, v2 = tri[:, 0], tri[:, 1], tri[:, 2]
    m0, m1, m2 = newid[:, 0], newid[:, 1], newid[:, 2]   # m0 on edge (1,2), m1 on (2,0), m2 on (0,1)
    T2 = np.concatenate([np.stack([v0, m2, m1], 1), np.stack([m2, v1, m0], 1),
                         np.stack([m1, m0, v2], 1), np.stack([m0, m1, m2], 1)])
    P0, P1, P2 = P3[:, 0], P3[:, 1], P3[:, 2]
    Q0, Q1, Q2 = mids[:, 0], mids[:, 1], mids[:, 2]
    PP = np.concatenate([np.stack([P0, Q2, Q1], 1), np.stack([Q2, P1, Q0], 1),
                         np.stack([Q1, Q0, P2], 1), np.stack([Q0, Q1, Q2], 1)])
    lev = np.concatenate([levels_per_tri] * 4)
    fr = np.concatenate([frames] * 4)
    u, inv3 = np.unique(T2.ravel(), return_inverse=True)
    return inv3.reshape(T2.shape), PP, lev, fr

def lengths(P3):
    L = np.zeros((len(P3), 3))
    W = []; Z = []
    for q in range(3):
        w_, z_ = hyp_to_uhs(P3[:, q]); W.append(w_); Z.append(z_)
    for m, (i, j) in enumerate([(1, 2), (2, 0), (0, 1)]):
        de = np.sqrt(np.abs(W[i] - W[j]) ** 2 + (Z[i] - Z[j]) ** 2)
        L[:, m] = 2 * np.arcsinh(de / (2 * np.sqrt(Z[i] * Z[j])))
    return L

# ---- from the instrument's flipnb part ----
@njit(cache=False)
def kahan_area(a, b, c):
    # sort a >= b >= c
    if a < b: a, b = b, a
    if b < c: b, c = c, b
    if a < b: a, b = b, a
    p = (a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c))
    if p < 0: p = 0.0
    return 0.25 * np.sqrt(p)

@njit(cache=False)
def cot_opp(hl, h):
    k = 3 * (h // 3)
    hn = k + (h - k + 1) % 3; hp = k + (h - k + 2) % 3
    a = hl[h]; b = hl[hn]; c = hl[hp]
    A = kahan_area(a, b, c)
    if A < 1e-300: A = 1e-300
    return (b * b + c * c - a * a) / (4.0 * A)

@njit(cache=False)
def flip_delaunay(hv0, hv1, hl, twin, tri, maxflips):
    nh = hl.shape[0]
    stack = np.empty(4 * nh + 16, dtype=np.int64)
    top = 0
    for h in range(nh):
        stack[top] = h; top += 1
    instack = np.ones(nh, dtype=np.bool_)
    flips = 0
    while top > 0 and flips < maxflips:
        top -= 1; h = stack[top]; instack[h] = False
        t = twin[h]
        if t < 0: continue
        if cot_opp(hl, h) + cot_opp(hl, t) >= -1e-12: continue
        k1 = h // 3; k2 = t // 3
        hn = 3 * k1 + (h - 3 * k1 + 1) % 3; hp = 3 * k1 + (h - 3 * k1 + 2) % 3
        tn = 3 * k2 + (t - 3 * k2 + 1) % 3; tp = 3 * k2 + (t - 3 * k2 + 2) % 3
        a = hv0[h]; b = hv1[h]; c = hv1[hn]; d = hv1[tn]
        lab = hl[h]; lbc = hl[hn]; lca = hl[hp]; lad = hl[tn]; ldb = hl[tp]
        # planar layout: a = (0,0), b = (lab,0); c above, d below
        A1 = kahan_area(lab, lbc, lca); A2 = kahan_area(lab, lad, ldb)
        cy = 2 * A1 / lab; dy = -2 * A2 / lab
        cx = (lab * lab + lca * lca - lbc * lbc) / (2 * lab)
        dx = (lab * lab + lad * lad - ldb * ldb) / (2 * lab)
        lcd = np.sqrt((cx - dx) ** 2 + (cy - dy) ** 2)
        An1 = kahan_area(lcd, lca, lad); An2 = kahan_area(lcd, ldb, lbc)
        if An1 < 1e-15 * lcd * lcd or An2 < 1e-15 * lcd * lcd or An1 + An2 < 0.999999 * (A1 + A2):
            continue
        l_bc = hl[hn]; tw_bc = twin[hn]
        l_ca = hl[hp]; tw_ca = twin[hp]
        l_ad = hl[tn]; tw_ad = twin[tn]
        l_db = hl[tp]; tw_db = twin[tp]
        e0 = 3 * k1; e1 = 3 * k1 + 1; e2 = 3 * k1 + 2
        f0 = 3 * k2; f1 = 3 * k2 + 1; f2 = 3 * k2 + 2
        hv0[e0] = d; hv1[e0] = c; hl[e0] = lcd; twin[e0] = f0
        hv0[e1] = c; hv1[e1] = a; hl[e1] = l_ca; twin[e1] = tw_ca
        hv0[e2] = a; hv1[e2] = d; hl[e2] = l_ad; twin[e2] = tw_ad
        hv0[f0] = c; hv1[f0] = d; hl[f0] = lcd; twin[f0] = e0
        hv0[f1] = d; hv1[f1] = b; hl[f1] = l_db; twin[f1] = tw_db
        hv0[f2] = b; hv1[f2] = c; hl[f2] = l_bc; twin[f2] = tw_bc
        if tw_ca >= 0: twin[tw_ca] = e1
        if tw_ad >= 0: twin[tw_ad] = e2
        if tw_db >= 0: twin[tw_db] = f1
        if tw_bc >= 0: twin[tw_bc] = f2
        tri[k1, 0] = d; tri[k1, 1] = c; tri[k1, 2] = a
        tri[k2, 0] = c; tri[k2, 1] = d; tri[k2, 2] = b
        flips += 1
        for hh in (e1, e2, f1, f2):
            if not instack[hh]:
                stack[top] = hh; top += 1; instack[hh] = True
    return flips

@njit(cache=False)
def all_cots(hl):
    out = np.empty(hl.shape[0])
    for h in range(hl.shape[0]):
        out[h] = cot_opp(hl, h)
    return out

# ---- from the instrument's conformal part ----
class HalfedgeMesh:
    def __init__(self, tri, L):
        """tri: (F,3) oriented triangles; L[k, m]: length of the edge opposite vertex m of triangle k."""
        self.tri = tri.copy()
        F = len(tri)
        # halfedge h = 3k + m goes from tri[k][m] to tri[k][(m+1)%3]; its length is L[k, (m+2)%3]
        self.hv0 = tri.reshape(-1)
        self.hv1 = tri[:, [1, 2, 0]].reshape(-1)
        self.hl = L[:, [2, 0, 1]].reshape(-1).copy()
        self.twin = -np.ones(3 * F, dtype=int)
        d = {}
        for h in range(3 * F):
            d[(self.hv0[h], self.hv1[h])] = h
        for h in range(3 * F):
            t = d.get((self.hv1[h], self.hv0[h]))
            if t is not None: self.twin[h] = t
        # make twin lengths consistent (average)
        for h in range(3 * F):
            t = self.twin[h]
            if t > h:
                m = 0.5 * (self.hl[h] + self.hl[t]); self.hl[h] = m; self.hl[t] = m
        self.nv = tri.max() + 1


def modulus(tri, L, verbose=False):
    # cap the boundary with a cone
    Hm = HalfedgeMesh(tri, L)
    bnd = np.where(Hm.twin < 0)[0]
    nloops = 0
    if len(bnd):
        per = Hm.hl[bnd].sum()
        rho = per / (2 * np.pi)
        cvert = Hm.nv
        newtri = [tuple(t) for t in tri]; newL = [tuple(l) for l in L]
        for h in bnd:
            u, v = Hm.hv0[h], Hm.hv1[h]
            newtri.append((v, u, cvert))
            # opposite-vertex lengths: opposite v: |u c| = rho; opposite u: |v c| = rho; opposite c: |uv|
            newL.append((rho, rho, Hm.hl[h]))
        tri = np.array(newtri); L = np.array(newL)
        Hm = HalfedgeMesh(tri, L)
    assert np.all(Hm.twin >= 0), "not closed after capping"
    V = Hm.nv; F = len(Hm.tri); E = len(Hm.hl) // 2
    chi = V - E + F
    flips = flip_delaunay(Hm.hv0, Hm.hv1, Hm.hl, Hm.twin, Hm.tri, 10 ** 8)
    # edges
    eid = -np.ones(len(Hm.hl), dtype=int)
    edges = []
    for h in range(len(Hm.hl)):
        if eid[h] < 0:
            eid[h] = len(edges); eid[Hm.twin[h]] = len(edges)
            edges.append(h)
    edges = np.array(edges)
    a = Hm.hv0[edges]; b = Hm.hv1[edges]
    hsign = np.where(edges[eid] == np.arange(len(Hm.hl)), 1.0, -1.0)
    cots = all_cots(Hm.hl)
    w = 0.5 * (cots[edges] + cots[Hm.twin[edges]])
    # tree (primal BFS) and cotree (dual BFS avoiding tree edges)
    adj = [[] for _ in range(V)]
    for e, h in enumerate(edges):
        adj[a[e]].append((b[e], e)); adj[b[e]].append((a[e], e))
    intree = np.zeros(len(edges), bool); parent_e = -np.ones(V, int); seen = np.zeros(V, bool)
    q = deque([0]); seen[0] = True
    while q:
        x = q.popleft()
        for y, e in adj[x]:
            if not seen[y]:
                seen[y] = True; intree[e] = True; parent_e[y] = e; q.append(y)
    # dual: faces adjacent across non-tree edges
    face_of = np.arange(len(Hm.hl)) // 3
    incot = np.zeros(len(edges), bool); fseen = np.zeros(F, bool); fparent = -np.ones(F, int)
    q = deque([0]); fseen[0] = True
    while q:
        f = q.popleft()
        for m in range(3):
            h = 3 * f + m; e = eid[h]
            if intree[e]: continue
            g2 = face_of[Hm.twin[h]]
            if not fseen[g2]:
                fseen[g2] = True; incot[e] = True; fparent[g2] = h; q.append(g2)
    left = np.where(~intree & ~incot)[0]
    assert len(left) == 2 - chi + 0 and len(left) == 2, (chi, len(left))
    # cocycles from the dual cycles through the leftover edges
    def path_to_root_faces(f):
        hs = []
        while fparent[f] >= 0:
            h = fparent[f]; hs.append(h); f = face_of[Hm.twin[h]]
        return hs           # halfedges h with face_of[twin[h]] the parent side ... crossing from parent into child
    zetas = []
    for e in left:
        h = edges[e]
        z = np.zeros(len(edges))
        def add(hh, sgn):
            z[eid[hh]] += sgn * hsign[hh]
        f1, f2 = face_of[h], face_of[Hm.twin[h]]
        f = f1
        while fparent[f] >= 0:                 # up from f1: cross child -> parent through hh (hh in the parent)
            hh = fparent[f]; add(hh, 1.0); f = face_of[hh]
        f = f2
        while fparent[f] >= 0:                 # down to f2: reverse of f2's upward path
            hh = fparent[f]; add(hh, -1.0); f = face_of[hh]
        add(h, 1.0)                            # cross from f2 into f1 through h
        zetas.append(z)
    # closedness check
    for z in zetas:
        cl = np.zeros(F)
        np.add.at(cl, face_of, z[eid] * hsign)
        assert np.abs(cl).max() < 1e-9, "cocycle not closed"
    # primal cycles through the leftover edges (tree paths)
    def tree_path(x):
        es = []
        while parent_e[x] >= 0:
            e = parent_e[x]; es.append(e); x = a[e] if b[e] == x else b[e]
        return es
    cycles = []
    for e in left:
        # cycle: a[e] -> b[e] along e, then b[e] -> root -> a[e] along the tree
        coef = np.zeros(len(edges)); coef[e] += 1
        x = b[e]
        while parent_e[x] >= 0:
            ee = parent_e[x]; y = a[ee] if b[ee] == x else b[ee]
            coef[ee] += 1 if a[ee] == x else -1; x = y
        x = a[e]; path = []
        while parent_e[x] >= 0:
            ee = parent_e[x]; y = a[ee] if b[ee] == x else b[ee]
            coef[ee] -= 1 if a[ee] == x else -1; x = y
        cycles.append(coef)
    P = np.array([[cyc @ z for z in zetas] for cyc in cycles])      # P[i, j] = period of zeta_j on cycle i
    # harmonic forms
    W = sp.diags(w)
    D = sp.csr_matrix((np.concatenate([-np.ones(len(edges)), np.ones(len(edges))]),
                       (np.concatenate([np.arange(len(edges))] * 2), np.concatenate([a, b]))), shape=(len(edges), V))
    Lap = (D.T @ W @ D).tocsr()
    Lr = Lap[1:, 1:].tocsc()
    solve = spla.factorized(Lr)
    omegas = []
    for z in zetas:
        rhs = -(D.T @ (w * z))
        u = np.zeros(V); u[1:] = solve(rhs[1:])
        omegas.append(z + D @ u)
    Om = np.array(omegas).T                       # edges x 2
    # forms with periods (1,0) and (0,1) on (cycle 1, cycle 2)
    C = Om @ np.linalg.inv(P.T)                   # columns alpha, beta: cycles @ C = I
    Em = C.T @ (w[:, None] * C)
    # orientation: cup product of alpha and beta over the oriented triangles
    # orientation: integral of alpha ^ beta with the piecewise-constant forms on each laid-out triangle
    h0 = 3 * np.arange(F); h1 = h0 + 1; h2 = h0 + 2
    l01 = Hm.hl[h0]; l12 = Hm.hl[h1]; l20 = Hm.hl[h2]
    x2 = (l01 ** 2 + l20 ** 2 - l12 ** 2) / (2 * l01)
    # vectorised Kahan area
    s3 = np.sort(np.stack([l01, l12, l20], 1), axis=1)[:, ::-1]
    aa, bb, cc = s3[:, 0], s3[:, 1], s3[:, 2]
    Ar = 0.25 * np.sqrt(np.maximum((aa + (bb + cc)) * (cc - (aa - bb)) * (cc + (aa - bb)) * (aa + (bb - cc)), 0))
    y2 = 2 * Ar / l01
    def comp(col):
        a01 = C[eid[h0], col] * hsign[h0]; a20 = C[eid[h2], col] * hsign[h2]
        pp = a01 / l01; qq = (-a20 - pp * x2) / y2
        return pp, qq
    pa, qa = comp(0); pb, qb = comp(1)
    cup = float(np.sum(Ar * (pa * qb - qa * pb)))
    det = np.linalg.det(Em)
    # tau is the root in the upper half-plane of the energy form E22 t^2 + 2 E12 t + E11: covariant under a change of
    # the cycle basis (E -> A E A^T moves the root by A's Moebius map); (-E12 + i)/E22 agrees only when det E = 1
    tau = (-Em[0, 1] + 1j * np.sqrt(det)) / Em[1, 1]
    if cup < 0: tau = -np.conj(tau)
    tr = reduce_tau(tau)
    if verbose:
        print(f"   modulus: V {V} F {F} chi {chi} flips {flips}, min weight {w.min():.2e}, cup {cup:+.6f}, det E {det:.6f}, "
              f"tau {tau:.6f} reduced {tr:.6f}")
    return tr, det, cup, dict(V=V, F=F, flips=flips, Em=Em, tau=tau, cup=cup, P=P)

def reduce_tau(t):
    for _ in range(1000):
        t = t - np.round(t.real)
        if abs(t) < 1 - 1e-14: t = -1 / t
        else: break
    return t

# ---- from the instrument's pipeline part ----
def word_matrix(g, w):
    A = np.eye(2, dtype=complex)
    for ch in w:
        i = ord(ch.lower()) - ord('a')
        A = A @ (g.smats[i] if ch.islower() else np.linalg.inv(g.smats[i]))
    return A

def word_chi(g, w):
    return sum((g.schi[ord(ch.lower()) - ord('a')] if ch.islower() else -g.schi[ord(ch.lower()) - ord('a')]) for ch in w)

def systole(g, maxlen=6):
    letters = [chr(ord('a') + i) for i in range(len(g.sgens))] + [chr(ord('A') + i) for i in range(len(g.sgens))]
    best = None
    for L in range(1, maxlen + 1):
        for w in itertools.product(letters, repeat=L):
            if any(w[i] == w[i + 1].swapcase() for i in range(L - 1)): continue
            if L > 1 and w[0] == w[-1].swapcase(): continue
            A = word_matrix(g, w)
            Lc = 2 * np.arccosh(np.trace(A) / 2 + 0j)
            if Lc.real < 0: Lc = -Lc
            if Lc.real < 1e-6: continue
            if best is None or Lc.real < best[0].real - 1e-9:
                best = (Lc, ''.join(w), A)
    return best

def axis_points(A, n=200, span=3.0):
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    disc = np.sqrt((d - a) ** 2 + 4 * b * c)
    x1 = ((a - d) + disc) / (2 * c); x2 = ((a - d) - disc) / (2 * c)
    m = (x1 + x2) / 2; r = abs(x1 - x2) / 2
    t = np.linspace(-span, span, n)
    u = (x1 - m) / r
    return m + r * np.tanh(t) * u, r / np.cosh(t)

def core_gradient(H, w, z):
    eps = 1e-6 * z
    gx = (H(w + eps, z) - H(w - eps, z)) / (2 * eps)
    gy = (H(w + 1j * eps, z) - H(w - 1j * eps, z)) / (2 * eps)
    gz = (H(w, z + eps) - H(w, z - eps)) / (2 * eps)
    return z * np.sqrt(gx ** 2 + gy ** 2 + gz ** 2)

def ford_volume(g, n=500):
    Fh = g.floor(n)
    return (g.area / n ** 2) * np.sum(1.0 / (2 * Fh ** 2)), Fh.min()

def face_check(H, n=3000, seed=2):
    g = H.g
    rng = np.random.default_rng(seed)
    w = rng.uniform(0, 1, n) * g.p1 + rng.uniform(0, 1, n) * g.p2
    r = 1 / np.abs(H.Sm[:, 1, 0]); cen = -H.Sm[:, 1, 1] / H.Sm[:, 1, 0]
    d2 = r[None, :] ** 2 - np.abs(w[:, None] - cen[None, :]) ** 2
    hgt = np.sqrt(np.maximum(d2, 0))
    k = np.argmax(hgt, axis=1); z = hgt[np.arange(n), k]
    A = H.Sm[k]
    a, b, c, d = A[:, 0, 0], A[:, 0, 1], A[:, 1, 0], A[:, 1, 1]
    cw_d = c * w + d
    den = np.abs(cw_d) ** 2 + np.abs(c) ** 2 * z * z
    w2 = ((a * w + b) * np.conj(cw_d) + a * np.conj(c) * z * z) / den; z2 = z / den
    lhs = H.eval_direct(w2, z2) - H.eval_direct(w, z) - H.Sx[k]
    return np.abs(lhs).max()

def surface_series(Ms, H, s, vals, nsub, log=print):
    S = Surf(Ms, H, s, vals)
    ck = S.check()
    out = dict(level=s, check=ck, snapped=S.nsnap, residual=S.res, series=[])
    log(f"    level {s}: {ck}, snapped {S.nsnap}, residual {S.res:.1e}")
    tri, P3, lev, fr = S.tri, S.P3, S.level, S.frame
    for n in range(nsub + 1):
        L = lengths(P3)
        tr, det, cup, info = modulus(tri, L)
        out['series'].append(dict(n=n, F=len(tri), detE=det, cup=cup, tau=complex(tr)))
        log(f"      n={n}: F {len(tri)} det E - 1 {det - 1:+.2e} cup {cup:+.4f} reduced tau {tr.real:+.7f} {tr.imag:+.7f}i")
        if n < nsub:
            tri, P3, lev, fr = subdivide(tri, P3, lev, H, fr)
    return out
