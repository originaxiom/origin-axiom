"""P-727 stage A (data-free): the conformal-modulus solver on a known case.

A Fuchsian once-punctured-torus group of known modulus tau0 (B1667's accessory machinery: tau0 -> Fricke traces, via
P-723's stage A) acts on the vertical half-plane over R. The solver must return tau0 from the surface and the group alone:
  1. the group: Jorgensen's normal form A, B from the traces (checked: traces, determinants, the commutator parabolic);
  2. the fundamental piece Q: the strip of the commutator's translation, above the upper envelope of the group's
     isometric circles (a graph t >= t_floor(u)), cut at t = T (the cusp is conformally a puncture);
  3. the mesh: on each paired arc, nodes and their exact images under the face pairing (so the pairing is node to node);
     the vertical sides paired by the translation; Delaunay inside;
  4. the energies: the cotangent Laplacian on the triangles' 3D Euclidean positions (2D Dirichlet energy is conformally
     invariant), minimised with h(gP) = h(P) + c(g) for the periods c = (1, 0) and (0, 1);
  5. tau: Im tau = 1/E22, Re tau = -E12/E22; the check det E = E11 E22 - E12^2 = 1.
"""
import sys, os, pathlib, cmath, math, time, itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def jorgensen(x, y, z):
    A = np.array([[x - y / z, x / z ** 2], [x, y / z]], dtype=complex)
    B = np.array([[y - x / z, -y / z ** 2], [-y, x / z]], dtype=complex)
    return A, B


def mob(M, w):
    return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])


def words(gens, depth):
    """All reduced words up to depth over gens (dict letter -> (matrix, period vector))."""
    inv = {k: k.swapcase() for k in gens}
    out = []
    frontier = [("", np.eye(2, dtype=complex), np.zeros(2))]
    for _ in range(depth):
        nxt = []
        for w, M, c in frontier:
            for k, (G, cg) in gens.items():
                if w and inv[k] == w[-1]:
                    continue
                nxt.append((w + k, M @ G, c + cg))
        out += nxt
        frontier = nxt
    return out


def solve_modulus(A, B, K_trans, T=None, n_arc=60, n_grid=(90, 60), depth=7, verbose=True):
    """The group <A, B> (real), cusp at infinity with [A,B] = translation by K_trans; returns tau and diagnostics."""
    k = abs(K_trans)
    gens = {"a": (A, np.array([1.0, 0.0])), "A": (np.linalg.inv(A), np.array([-1.0, 0.0])),
            "b": (B, np.array([0.0, 1.0])), "B": (np.linalg.inv(B), np.array([0.0, -1.0]))}
    els = words(gens, depth)
    circ = []
    seen = set()
    for w, M, c in els:
        cc = M[1, 0]
        if abs(cc) < 1e-10:
            continue
        ctr = (-M[1, 1] / cc).real; r = 1 / abs(cc)
        key = (round(ctr % k, 7), round(r, 7))
        if key in seen:
            continue
        seen.add(key)
        circ.append((ctr, r, M, c, w))
    # translates of each circle into a window around the strip [-k/2, k/2]
    Ktr = np.array([[1, K_trans.real], [0, 1]], dtype=complex)
    allc = []
    for ctr, r, M, c, w in circ:
        n0 = math.floor((ctr + k / 2) / k)
        for e in (-1, 0, 1):
            n = n0 + e
            # the isometric circle of M T_v has centre ctr - v; T_v = K^m with v = m * K_trans (period 0)
            v = n * K_trans.real
            Tv = np.array([[1, v], [0, 1]], dtype=complex)
            allc.append((ctr - v, r, M @ Tv, c, w))
    centers = np.array([q[0] for q in allc]); radii = np.array([q[1] for q in allc])

    def floor(u):
        u = np.atleast_1d(u)
        d = radii[None, :] ** 2 - (u[:, None] - centers[None, :]) ** 2
        h = np.sqrt(np.maximum(d, 0)); j = np.argmax(h, axis=1)
        return h[np.arange(len(u)), j], j

    uu = np.linspace(-k / 2, k / 2, 4001)
    tf, jf = floor(uu)
    # the faces: maximal runs of the same envelope circle
    faces = []
    start = 0
    for i in range(1, len(uu) + 1):
        if i == len(uu) or jf[i] != jf[start]:
            faces.append((jf[start], uu[start], uu[i - 1]))
            start = i
    if T is None:
        T = 6.0 * k
    if verbose:
        print(f"   circles {len(circ)}, envelope faces {len(faces)}: " +
              ", ".join(f"{allc[j][4]}[{a:+.3f},{b:+.3f}]" for j, a, b in faces), flush=True)
    return faces, allc, floor, T


if __name__ == "__main__" and len(sys.argv) == 1:
    from pleated_stage_a import traces_of, markov
    for tau0 in (complex(0.23, 1.41), complex(-0.31, 1.07), complex(0.0, 1.0)):
        v, c, res = traces_of(tau0)
        x, y, z = [t.real for t in v]
        A, B = jorgensen(x, y, z)
        K = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        print(f"tau0 {tau0}: traces ({x:.8f}, {y:.8f}, {z:.8f}), Markov {markov(v).real:.2e}; tr A {np.trace(A).real:.8f} "
              f"tr B {np.trace(B).real:.8f} tr AB {np.trace(A @ B).real:.8f}; det {np.linalg.det(A).real:.12f} "
              f"{np.linalg.det(B).real:.12f}; [A,B] = {np.round(K, 9).tolist()}", flush=True)


# ------------------------------------------------------------------------------------------------ the mesh and the solve
class UF:
    """Union-find with integer period offsets: value(x) = value(root) + off(x)."""
    def __init__(self, n):
        self.p = list(range(n)); self.o = [np.zeros(2) for _ in range(n)]; self.bad = 0
    def find(self, x):
        if self.p[x] == x:
            return x, np.zeros(2)
        r, o = self.find(self.p[x]); self.p[x] = r; self.o[x] = self.o[x] + o; return r, self.o[x]
    def union(self, x, y, d):          # value(y) = value(x) + d
        rx, ox = self.find(x); ry, oy = self.find(y)
        if rx == ry:
            if np.abs((oy - ox) - d).max() > 1e-9:
                self.bad += 1
            return
        self.p[ry] = rx; self.o[ry] = ox + d - oy


def build_and_solve(faces, allc, floor, T, k, K_trans, surface3d, n_arc=80, nu=70, nt=50, verbose=True, xform=None):
    pts = []                      # (u, t)
    def add(u, t):
        pts.append((u, t)); return len(pts) - 1
    links = []                    # (i, j, d): value(j) = value(i) + d
    # arcs: every face sampled; every sample mapped by its element into the strip
    for j, a, b in faces:
        ctr, r, M, c, w = allc[j]
        us = np.linspace(a, b, max(4, int(n_arc * (b - a) / k) + 2))
        for u in us:
            t = math.sqrt(max(r * r - (u - ctr) ** 2, 0.0))
            i = add(u, t)
            q = mob(M, complex(u, t))
            n = math.floor((q.real + k / 2) / k + 1e-12)
            qu = q.real - n * k
            jj = add(qu, q.imag)
            links.append((i, jj, c.copy()))
    # vertical sides, paired by the translation (period 0)
    t0 = float(floor(np.array([-k / 2]))[0][0])
    ts = np.exp(np.linspace(math.log(max(t0, 1e-6)), math.log(T), nt))
    for t in ts:
        i = add(-k / 2, t); j = add(k / 2, t); links.append((i, j, np.zeros(2)))
    # top edge and interior grid (log-spaced in t above the floor)
    for u in np.linspace(-k / 2, k / 2, nu)[1:-1]:
        f = float(floor(np.array([u]))[0][0])
        for e in np.linspace(0, 1, nt)[1:]:
            t = math.exp(math.log(f) + e * (math.log(T) - math.log(f)))
            add(u, t)
    P = np.array(pts)
    # validation: every mapped arc node lies on the envelope
    on = [abs(P[j, 1] - float(floor(np.array([P[j, 0]]))[0][0])) for _, j, _ in links[: -nt]]
    # merge coincident nodes
    uf = UF(len(P))
    for i, j, d in links:
        uf.union(i, j, d)
    from scipy.spatial import cKDTree
    tree = cKDTree(np.c_[P[:, 0], np.log(P[:, 1])])
    for i, j in tree.query_pairs(1e-9):
        uf.union(i, j, np.zeros(2))
    # triangulate in (u, log t); keep triangles whose centroid is inside Q
    tri = Delaunay(np.c_[P[:, 0], np.log(P[:, 1])])
    S = tri.simplices
    cu = P[S, 0].mean(1); ct = np.exp(np.log(P[S, 1]).mean(1))
    keep = (ct > floor(cu)[0] * (1 + 1e-9)) & (np.abs(cu) <= k / 2)
    S = S[keep]
    X3 = surface3d(P[:, 0], P[:, 1])
    if xform is not None:
        X3 = xform(X3)                        # a conformal map of R^3: the energies, hence tau, must not change
    # cotangent weights on the 3D triangles
    W = {}
    for tr in S:
        for a_, b_, c_ in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            i, j, m = tr[a_], tr[b_], tr[c_]
            e1 = X3[i] - X3[m]; e2 = X3[j] - X3[m]
            cot = np.dot(e1, e2) / max(np.linalg.norm(np.cross(e1, e2)), 1e-300)
            key = (min(i, j), max(i, j)); W[key] = W.get(key, 0.0) + 0.5 * cot
    roots = {}; cls = np.empty(len(P), int); off = np.zeros((len(P), 2))
    for x in range(len(P)):
        r, o = uf.find(x); cls[x] = roots.setdefault(r, len(roots)); off[x] = o
    n = len(roots)
    I = np.array([e[0] for e in W]); J = np.array([e[1] for e in W]); w = np.array(list(W.values()))
    ci, cj = cls[I], cls[J]
    D = off[I] - off[J]                          # h_I - h_J = H_ci - H_cj + D . p
    def energy(pvec):
        dd = D @ pvec
        L = sp.coo_matrix((np.r_[w, w, -w, -w], (np.r_[ci, cj, ci, cj], np.r_[ci, cj, cj, ci])), shape=(n, n)).tocsr()
        rhs = np.zeros(n); np.add.at(rhs, ci, -w * dd); np.add.at(rhs, cj, w * dd)
        L = L + sp.eye(n) * 1e-12
        H = spla.spsolve(L.tocsc(), rhs)
        diff = H[ci] - H[cj] + dd
        return float(np.sum(w * diff ** 2))
    E11 = energy(np.array([1.0, 0.0])); E22 = energy(np.array([0.0, 1.0])); Ep = energy(np.array([1.0, 1.0]))
    E12 = (Ep - E11 - E22) / 2
    tau = complex(-E12 / E22, 1 / E22)
    info = dict(nodes=len(P), classes=n, triangles=len(S), pairing_on_envelope_max=float(max(on)) if on else 0.0,
                inconsistent_cycles=uf.bad, detE=E11 * E22 - E12 ** 2, negative_cot=int(np.sum(w < 0)))
    return tau, info


def inversion(c=(0.3, 0.7, -0.6), R=1.3):
    c = np.array(c)
    def f(X):
        D = X - c
        return c + R * R * D / np.sum(D * D, axis=1)[:, None]
    return f


def run_control(tau0, res=(80, 70, 50), T_mult=6.0, verbose=True, xform=None):
    from pleated_stage_a import traces_of
    v, _, _ = traces_of(tau0)
    x, y, z = [t.real for t in v]
    A, B = jorgensen(x, y, z)
    K = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    Kt = complex(mob(K, 0.0))                 # the translation of the commutator
    faces, allc, floor, T = solve_modulus(A, B, Kt, T=T_mult * abs(Kt), verbose=verbose)
    surf = lambda u, t: np.c_[u, np.zeros_like(u), t]
    tau, info = build_and_solve(faces, allc, floor, T, abs(Kt), Kt, surf, n_arc=res[0], nu=res[1], nt=res[2], xform=xform)
    return tau, info, (x, y, z)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "solve":
    for tau0 in (complex(0.23, 1.41), complex(-0.31, 1.07)):
        for res in ((60, 50, 40), (120, 100, 80)):
            t0 = time.time()
            tau, info, tr = run_control(tau0, res=res, verbose=(res[0] == 60))
            print(f"tau0 {tau0}  res {res}: tau {tau.real:+.6f}{tau.imag:+.6f}i  (mirror {-tau.real:+.6f})  |err| "
                  f"{min(abs(tau - tau0), abs(complex(-tau.real, tau.imag) - tau0)):.2e}  {info}  {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "curved":
    tau0 = complex(0.23, 1.41)
    for xf, name in ((None, "flat"), (inversion(), "inverted (curved)")):
        tau, info, tr = run_control(tau0, res=(120, 100, 80), verbose=False, xform=xf)
        print(f"{name}: tau {tau.real:+.6f}{tau.imag:+.6f}i  detE {info['detE']:.6f}  negative cot {info['negative_cot']}", flush=True)


def build_and_solve_cols(faces, allc, floor, T, k, surface3d, n_arc=80, nlev=60, xform=None, uniq=1e-10):
    """A structured, hole-free mesh: a column at every floor node (arc samples and their exact images, plus the strip's
    edges); in each column the same log-spaced levels from the floor to T; adjacent columns joined level by level."""
    fl = []                       # floor nodes (u, t) and links between them
    links = []
    for j, a, b in faces:
        ctr, r, M, c, w = allc[j]
        nn = max(3, int(n_arc * (b - a) / k) + 2)
        for u in np.linspace(a, b, nn):
            t = math.sqrt(max(r * r - (u - ctr) ** 2, 0.0))
            q = mob(M, complex(u, t))
            n = math.floor((q.real + k / 2) / k + 1e-12)
            fl.append((u, t)); fl.append((q.real - n * k, q.imag))
            links.append((len(fl) - 2, len(fl) - 1, c.copy()))
    fl.append((-k / 2, float(floor(np.array([-k / 2]))[0][0]))); fl.append((k / 2, float(floor(np.array([k / 2]))[0][0])))
    U = np.array([p[0] for p in fl])
    order = np.argsort(U)
    cols = []                     # unique column positions
    colof = np.empty(len(fl), int)
    for idx in order:
        if cols and abs(U[idx] - cols[-1]) < uniq:
            colof[idx] = len(cols) - 1
        else:
            cols.append(U[idx]); colof[idx] = len(cols) - 1
    cols = np.array(cols)
    ncol = len(cols)
    fcol, _ = floor(cols)
    eta = np.linspace(0, 1, nlev)
    tt = np.exp(np.log(fcol)[:, None] + eta[None, :] * (np.log(T) - np.log(fcol))[:, None])   # ncol x nlev
    node = lambda ci, m: ci * nlev + m
    Pu = np.repeat(cols, nlev); Pt = tt.ravel()
    uf = UF(ncol * nlev)
    for i, j, d in links:          # the face pairings act on floor nodes (level 0)
        uf.union(node(colof[i], 0), node(colof[j], 0), d)
    for m in range(nlev):          # the strip's edges, paired by the translation (period 0)
        uf.union(node(0, m), node(ncol - 1, m), np.zeros(2))
    S = []
    for ci in range(ncol - 1):
        for m in range(nlev - 1):
            a0, a1, b0, b1 = node(ci, m), node(ci, m + 1), node(ci + 1, m), node(ci + 1, m + 1)
            S.append((a0, b0, b1)); S.append((a0, b1, a1))
    S = np.array(S)
    X3 = surface3d(Pu, Pt)
    if xform is not None:
        X3 = xform(X3)
    W = {}
    for tr in S:
        for a_, b_, c_ in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            i, j, m = tr[a_], tr[b_], tr[c_]
            e1 = X3[i] - X3[m]; e2 = X3[j] - X3[m]
            cr = np.linalg.norm(np.cross(e1, e2))
            if cr < 1e-300:
                continue
            key = (min(i, j), max(i, j)); W[key] = W.get(key, 0.0) + 0.5 * np.dot(e1, e2) / cr
    roots = {}; cls = np.empty(ncol * nlev, int); off = np.zeros((ncol * nlev, 2))
    for x in range(ncol * nlev):
        r, o = uf.find(x); cls[x] = roots.setdefault(r, len(roots)); off[x] = o
    n = len(roots)
    I = np.array([e[0] for e in W]); J = np.array([e[1] for e in W]); w = np.array(list(W.values()))
    ci_, cj_ = cls[I], cls[J]; D = off[I] - off[J]
    def energy(pvec):
        dd = D @ pvec
        L = sp.coo_matrix((np.r_[w, w, -w, -w], (np.r_[ci_, cj_, ci_, cj_], np.r_[ci_, cj_, cj_, ci_])), shape=(n, n)).tocsr()
        rhs = np.zeros(n); np.add.at(rhs, ci_, -w * dd); np.add.at(rhs, cj_, w * dd)
        H = spla.spsolve((L + sp.eye(n) * 1e-12).tocsc(), rhs)
        return float(np.sum(w * (H[ci_] - H[cj_] + dd) ** 2))
    E11 = energy(np.array([1.0, 0.0])); E22 = energy(np.array([0.0, 1.0])); E12 = (energy(np.array([1.0, 1.0])) - E11 - E22) / 2
    tau = complex(-E12 / E22, 1 / E22)
    return tau, dict(columns=ncol, levels=nlev, classes=n, inconsistent_cycles=uf.bad, detE=E11 * E22 - E12 ** 2,
                     negative_cot=int(np.sum(w < 0)))


_TR = {}
def traces_cached(tau0):
    import json
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "traces_cache.json")
    try:
        cache = json.load(open(f))
    except Exception:
        cache = {}
    key = f"{tau0.real:.6f},{tau0.imag:.6f}"
    if key not in cache:
        from pleated_stage_a import traces_of
        v, _, _ = traces_of(tau0)
        cache[key] = [t.real for t in v] + [max(abs(t.imag) for t in v)]
        json.dump(cache, open(f, "w"))
    return cache[key]


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "cols":
    for tau0 in (complex(0.23, 1.41), complex(-0.31, 1.07)):
        x, y, z, im = traces_cached(tau0)
        A, B = jorgensen(x, y, z)
        K = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B); Kt = complex(mob(K, 0.0))
        faces, allc, floor, T = solve_modulus(A, B, Kt, T=6 * abs(Kt), verbose=False)
        surf = lambda u, t: np.c_[u, np.zeros_like(u), t]
        for n_arc, nlev in ((60, 40), (120, 80), (240, 160)):
            for xf, nm in ((None, "flat"), (inversion(), "curved")):
                t1 = time.time()
                tau, info = build_and_solve_cols(faces, allc, floor, T, abs(Kt), surf, n_arc=n_arc, nlev=nlev, xform=xf)
                print(f"tau0 {tau0} {nm:6s} arc {n_arc:3d} lev {nlev:3d}: tau {tau.real:+.7f}{tau.imag:+.7f}i |err| {abs(tau - tau0):.2e} "
                      f"detE-1 {info['detE']-1:+.2e} cols {info['columns']} bad {info['inconsistent_cycles']} {time.time()-t1:.0f}s", flush=True)
