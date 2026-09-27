#!/usr/bin/env python3
"""B1387 -- the harmonic cusp form of a cuspidal class, computed: a Hejhal-type linear solve on a cusped hyperbolic 3-manifold.

The object.  Let v be a cuspidal class (a homomorphism pi_1(M) -> Q vanishing on every peripheral subgroup; for cube~3.24 the line
H^1(M)^Isom of B1386).  Its L^2 harmonic representative is omega = dF for a harmonic function F on H^3 with F(g x) = F(x) + v(g).
In a chart where cusp c sits at infinity and its stabiliser acts by the translation lattice L_c (x in C, height t > 0),
    F = A_c + sum_{k in L_c^*, k != 0} c_k t K_1(2 pi |k| t) e^{2 pi i k.x}                                  (*)
on all of H^3 (the modes of a Gamma_c-periodic harmonic function; the t^2 mode is excluded by L^2, the growing Bessel mode by the cusp).
So the sign of omega_t = dF/dt at large height is minus the sign of the leading non-zero shell of (*): d+ = {leading shell < 0}.

The solve (after Hejhal).  The unknowns are the constants A_c (one fixed) and the c_k up to |k| sqrt(covol L_c) <= Kn.
- Sample points lie low in each chart, below the fundamental polyhedron's cusp regions.
- Each is pulled back into SnapPy's developed fundamental polyhedron (FundamentalPolyhedronEngine: the ideal vertices, the face
  pairings of the unsimplified presentation). The pull-back walks through the ideal tetrahedra and accumulates v over the face
  pairings crossed.
- It is re-expanded in the best chart among the four vertices of its tetrahedron, the chart of every polyhedron vertex being
  reached by a breadth-first search over the face pairings.
- Each sample gives one linear equation F_c(y) - F_c'(y*) = v(accumulated) - v(chart element); least squares.

Nothing about the member's symmetry is imposed. The rotation, the swap, the -I actions and the killed shells come out of the solve.
Usage: python3 harmonic_cusp_form.py"""
import itertools
import math
import random
import sys
import time
import warnings
from collections import deque
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
from scipy.special import k1
import snappy
from snappy.snap.fundamental_polyhedron import FundamentalPolyhedronEngine
from snappy.snap.t3mlite import simplex
from snappy.snap.kernel_structures import Infinity

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1386 = ROOT / "frontier" / "B1386_the_open_eisenstein_cusp" / "verification"
sys.path.insert(0, str(B1386))
import the_open_cusp as T                      # B1386: the member (covering path pinned by its signature), chi_grid, morse_chi

V = simplex.ZeroSubsimplices
FACES = simplex.TwoSubsimplices
OPP = {F: [v for v in V if not (v & F)][0] for F in FACES}
FACE_VERTS = {F: [v for v in V if (v & F) == v] for F in FACES}


# ------------------------------------------------------------------------------------------- Moebius geometry
def _mat(m):
    return np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])


def _sl2(A):
    return A / np.sqrt(np.linalg.det(A))


def act(A, P):
    """A in SL(2, C) acting on P = (w, h) in upper half-space"""
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    w, h = P
    q = c * w + d
    D = abs(q) ** 2 + abs(c) ** 2 * h * h
    return (((a * w + b) * np.conj(q) + a * np.conj(c) * h * h) / D, h / D)


def act_boundary(A, z):
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    if z is None:
        return None if abs(c) < 1e-300 else a / c
    den = c * z + d
    return None if abs(den) < 1e-300 else (a * z + b) / den


def _circumcircle(p, q, r):
    ax, ay, bx, by, cx, cy = p.real, p.imag, q.real, q.imag, r.real, r.imag
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    c0 = complex(ux, uy)
    return c0, abs(p - c0)


# ------------------------------------------------------------------------------------------- the fundamental polyhedron
class Polyhedron:
    """SnapPy's developed fundamental polyhedron, conjugated by Phi(z) = 1/(z - z0) so that no ideal vertex is at infinity"""

    def __init__(self, M, seed=1):
        self.M = M
        E = FundamentalPolyhedronEngine.from_manifold_and_shapes(M, M.tetrahedra_shapes("rect"), normalize_matrices=True,
                                                                 match_kernel=True)
        mc = E.mcomplex
        rng = random.Random(seed)
        z0 = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3))
        self.Phi = _sl2(np.array([[0, 1], [1, -z0]], dtype=complex))
        Phinv = np.linalg.inv(self.Phi)
        self.ntet = len(mc.Tetrahedra)
        self.verts, self.cusp_of, self.vclass = [], [], []
        vid = {}
        for Tt in mc.Tetrahedra:
            d, cu, cl = {}, {}, {}
            for v in V:
                ip = Tt.Class[v].IdealPoint
                d[v] = act_boundary(self.Phi, None if ip == Infinity else complex(ip))
                cu[v] = Tt.Class[v].SubsimplexIndexInManifold
                cl[v] = vid.setdefault(id(Tt.Class[v]), len(vid))
            self.verts.append(d)
            self.cusp_of.append(cu)
            self.vclass.append(cl)
        self.nvert = len(vid)
        self.pairing = {}
        for g, prs in mc.Generators.items():
            for (inC, outC), perm in prs:
                self.pairing[(inC.Tetrahedron.Index, inC.Subsimplex)] = (g, outC.Tetrahedron.Index, outC.Subsimplex, perm)
        self.info, self.nbr, self.nbr_face = [], [], []
        for Tt in mc.Tetrahedra:
            inf, nb, nf = {}, {}, {}
            for F in FACES:
                g = Tt.GeneratorsInfo[F]
                inf[F] = g
                if g == 0:
                    nb[F], nf[F] = Tt.Neighbor[F].Index, Tt.Gluing[F].image(F)
                else:
                    _, s, fs, _ = self.pairing[(Tt.Index, F)]
                    nb[F], nf[F] = s, fs
            self.info.append(inf)
            self.nbr.append(nb)
            self.nbr_face.append(nf)
        self.gen = {g: self.Phi @ _sl2(_mat(m)) @ Phinv for g, m in mc.GeneratorMatrices.items() if g != 0}
        self.geninv = {g: np.linalg.inv(m) for g, m in self.gen.items()}
        self.circ = []
        for i in range(self.ntet):
            cc = {}
            for F in FACES:
                c0, R = _circumcircle(*[self.verts[i][v] for v in FACE_VERTS[F]])
                cc[F] = (c0, R, np.sign(abs(self.verts[i][OPP[F]] - c0) ** 2 - R * R))
            self.circ.append(cc)

    def outside(self, i, P):
        w, h = P
        out = []
        for F in FACES:
            c0, R, side = self.circ[i][F]
            val = abs(w - c0) ** 2 + h * h - R * R
            if np.sign(val) != side:
                out.append((abs(val), F))
        return out

    def walk(self, i, P, v, maxsteps=5000):
        """pull P back into the polyhedron; returns (tet, P*, acc, steps) with F(P) = F(P*) + acc"""
        rng = random.Random(7)
        acc, last = 0.0, None
        for step in range(maxsteps):
            bad = self.outside(i, P)
            if not bad:
                return i, P, acc, step
            bad.sort(reverse=True)
            cand = [F for _, F in bad if (i, F) != last] or [F for _, F in bad]
            F = cand[0] if rng.random() < 0.8 else rng.choice(cand)
            g = self.info[i][F]
            j, Fj = self.nbr[i][F], self.nbr_face[i][F]
            if g != 0:
                P = act(self.geninv[g], P)
                acc += v[g]
            last, i = (j, Fj), j
        raise RuntimeError("walk did not terminate")


def cuspidal_class(M):
    """the cuspidal line of the unsimplified presentation: v on the generators, vanishing on relators and peripheral words"""
    G = M.fundamental_group(simplify_presentation=False)
    n = G.num_generators()

    def vec(word):
        x = np.zeros(n)
        for g in word:
            x[abs(g) - 1] += 1 if g > 0 else -1
        return x
    A = np.array([vec(r) for r in G.relators(as_int_list=True)] +
                 [vec(w) for pair in G.peripheral_curves(as_int_list=True) for w in pair])
    _, s, vt = np.linalg.svd(A)
    null = vt[(s > 1e-8).sum():]
    x = null[0] / null[0][np.argmax(np.abs(null[0]))]
    v = {}
    for g in range(n):
        v[g + 1], v[-(g + 1)] = x[g], -x[g]
    return v, G, len(null)


# ------------------------------------------------------------------------------------------- charts
def _lattice_basis(vecs, tol=1e-7):
    vecs = [z for z in vecs if abs(z) > tol]

    def red(b1, b2):
        for _ in range(200):
            if abs(b1) > abs(b2):
                b1, b2 = b2, b1
            m = round(((b2 * b1.conjugate()).real) / abs(b1) ** 2)
            if m == 0:
                break
            b2 = b2 - m * b1
        return b1, b2
    b1 = min(vecs, key=abs)
    b2 = min([z for z in vecs if abs((z / b1).imag) > tol], key=abs)
    b1, b2 = red(b1, b2)
    for _ in range(20):
        changed = False
        for z in vecs:
            x = np.linalg.solve(np.array([[b1.real, b2.real], [b1.imag, b2.imag]]), [z.real, z.imag])
            if np.abs(x - np.round(x)).max() > 1e-6:
                cands = [b1, b2, z]
                n1 = min(cands, key=abs)
                b1, b2 = red(n1, min([q for q in cands if abs((q / n1).imag) > tol], key=abs))
                changed = True
        if not changed:
            break
    return (b1, -b2) if (b2 / b1).imag < 0 else (b1, b2)


class Charts:
    """a chart at every cusp (its base vertex sent to infinity) and, for every polyhedron vertex u, the element gamma_u carrying u to
    the base vertex of its cusp, with v(gamma_u); the parabolic loops give the lattice and are checked to carry v = 0"""

    def __init__(self, P, v):
        self.P = P
        edges = []
        for i in range(P.ntet):
            for F in FACES:
                g = P.info[i][F]
                if g:
                    _, s, _, perm = P.pairing[(i, F)]
                    for vv in FACE_VERTS[F]:
                        edges.append((P.vclass[s][perm.image(vv)], P.vclass[i][vv], g))     # gen[g] maps the first to the second
        self.cusp_of_vertex, pos, count = {}, {}, {}
        for i in range(P.ntet):
            for vv in V:
                u = P.vclass[i][vv]
                self.cusp_of_vertex[u], pos[u] = P.cusp_of[i][vv], P.verts[i][vv]
                count[u] = count.get(u, 0) + 1
        adj = {}
        for uS, uT, g in edges:
            adj.setdefault(uS, []).append((uT, g, +1))
            adj.setdefault(uT, []).append((uS, g, -1))
        self.gamma, self.vgam, self.base, self.A, self.Ainv, self.lat, self.parabolic_v = {}, {}, {}, {}, {}, {}, {}
        for c in range(P.M.num_cusps()):
            u0 = max((u for u, cc in self.cusp_of_vertex.items() if cc == c), key=lambda u: count[u])
            self.base[c] = u0
            A = np.array([[pos[u0], -1], [1, 0]], dtype=complex)
            self.A[c], self.Ainv[c] = A, np.linalg.inv(A)
            self.gamma[u0], self.vgam[u0] = np.eye(2, dtype=complex), 0.0
            lam, pv = [], []
            queue = deque([u0])
            while queue:
                u = queue.popleft()
                for w, g, sgn in adj.get(u, []):
                    if sgn == +1:
                        gw, vw = self.gamma[u] @ P.geninv[g], self.vgam[u] - v[g]
                    else:
                        gw, vw = self.gamma[u] @ P.gen[g], self.vgam[u] + v[g]
                    if w not in self.gamma:
                        self.gamma[w], self.vgam[w] = gw, vw
                        queue.append(w)
                    else:
                        p = gw @ np.linalg.inv(self.gamma[w])
                        if min(np.abs(p - np.eye(2)).max(), np.abs(p + np.eye(2)).max()) > 1e-8:
                            q = self.Ainv[c] @ p @ A
                            q = q / q[1, 1]
                            assert abs(q[1, 0]) < 1e-6 and abs(q[0, 0] - 1) < 1e-6, "a loop at the cusp is not a translation"
                            lam.append(q[0, 1])
                            pv.append(abs(vw - self.vgam[w]))
            self.lat[c] = _lattice_basis(lam)
            self.parabolic_v[c] = max(pv)

    def to_chart(self, c, u, Pt):
        return act(self.Ainv[c] @ self.gamma[u], Pt)


# ------------------------------------------------------------------------------------------- the solve
class Solver:
    def __init__(self, P, C, v, Kn):
        self.P, self.C, self.v = P, C, v
        self.nc = P.M.num_cusps()
        self.cols, col = {}, 0
        for c in range(1, self.nc):
            self.cols[(c, "A")] = col
            col += 1
        self.modes, self.s, self.first = {}, {}, {}
        for c in range(self.nc):
            b1, b2 = C.lat[c]
            G = np.array([[abs(b1) ** 2, (b1 * b2.conjugate()).real], [(b1 * b2.conjugate()).real, abs(b2) ** 2]])
            Gi = np.linalg.inv(G)
            s = math.sqrt(abs((b1.conjugate() * b2).imag))
            self.s[c] = s
            nmax = int(Kn / s * max(abs(b1), abs(b2)) * 2) + 2
            ks = []
            for m in range(-nmax, nmax + 1):
                for n in range(-nmax, nmax + 1):
                    if (m > 0 or (m == 0 and n > 0)):
                        kk = math.sqrt(np.array([m, n]) @ Gi @ np.array([m, n]))
                        if kk * s <= Kn:
                            ks.append((kk, m, n))
            ks.sort()
            self.modes[c] = (np.array([k[1] for k in ks]), np.array([k[2] for k in ks]), np.array([k[0] for k in ks]))
            self.first[c] = col
            col += 2 * len(ks)
        self.ncol = col

    def row(self, c, y, sign=1.0, out=None):
        out = np.zeros(self.ncol) if out is None else out
        w, h = y
        b1, b2 = self.C.lat[c]
        st = np.linalg.solve(np.array([[b1.real, b2.real], [b1.imag, b2.imag]]), [w.real, w.imag])
        mm, nn, kk = self.modes[c]
        th = 2 * np.pi * (mm * st[0] + nn * st[1])
        amp = 2 * h * k1(2 * np.pi * kk * h)
        idx = self.first[c] + 2 * np.arange(len(mm))
        out[idx] += sign * amp * np.cos(th)
        out[idx + 1] -= sign * amp * np.sin(th)
        if c:
            out[self.cols[(c, "A")]] += sign
        return out

    def best_chart(self, i, Pt):
        best = None
        for vv in V:
            u = self.P.vclass[i][vv]
            c = self.C.cusp_of_vertex[u]
            y = self.C.to_chart(c, u, Pt)
            if best is None or y[1] / self.s[c] > best[0]:
                best = (y[1] / self.s[c], c, u, y)
        return best

    def equations(self, c, tau, Q, rng):
        b1, b2 = self.C.lat[c]
        i0 = next(i for i in range(self.P.ntet) for vv in V if self.P.vclass[i][vv] == self.C.base[c])
        rows, rhs, taus = [], [], []
        for a in range(Q):
            for b in range(Q):
                y = (((a + 0.5 + rng.uniform(-0.3, 0.3)) / Q) * b1 + ((b + 0.5 + rng.uniform(-0.3, 0.3)) / Q) * b2, tau * self.s[c])
                i, Ps, acc, _ = self.P.walk(i0, act(self.C.A[c], y), self.v)
                tb, cb, ub, yb = self.best_chart(i, Ps)
                r = self.row(c, y)
                self.row(cb, yb, -1.0, r)
                val = acc - self.C.vgam[ub]
                if np.abs(r).max() < 1e-12 and abs(val) < 1e-12:
                    continue
                rows.append(r)
                rhs.append(val)
                taus.append(tb)
        return rows, rhs, taus

    def coefficient(self, x, c, j):
        return complex(x[self.first[c] + 2 * j], x[self.first[c] + 2 * j + 1])

    def shells(self, x, c, nshell):
        mm, nn, kk = self.modes[c]
        out = []
        for j in range(len(kk)):
            entry = ((int(mm[j]), int(nn[j])), self.coefficient(x, c, j))
            if out and abs(kk[j] - out[-1][0]) < 1e-7 * kk[j]:
                out[-1][1].append(entry)
            elif len(out) < nshell:
                out.append([kk[j], [entry]])
            else:
                break
        return [(kn * self.s[c], coefs) for kn, coefs in out]


def build(M, Kn, seed=1):
    P = Polyhedron(M, seed=seed)
    v, G, dim = cuspidal_class(M)
    assert dim == 1, "the cuspidal line"
    C = Charts(P, v)
    return P, v, G, C, Solver(P, C, v, Kn)


def solve(M, Kn=10.0, tau=0.10, seed=1, sample_seed=1, test_taus=(0.06, 0.09)):
    t0 = time.time()
    P, v, G, C, S = build(M, Kn, seed)
    rng = random.Random(sample_seed)
    rows, rhs, taus = [], [], []
    for c in range(S.nc):
        Q = int(math.ceil(math.sqrt(1.6 * 2 * len(S.modes[c][0])))) + 2
        r, b, t = S.equations(c, tau, Q, rng)
        rows += r
        rhs += b
        taus += t
    A, b = np.array(rows), np.array(rhs)
    x, _, rank, sv = np.linalg.lstsq(A, b, rcond=None)
    res = A @ x - b
    test = []
    for c in range(S.nc):
        for tt in test_taus:
            r, bb, _ = S.equations(c, tt, 12, random.Random(1000 + 17 * c))
            test += list(np.array(r) @ x - np.array(bb))
    stats = {"unknowns": S.ncol, "equations": len(b), "full rank": rank == S.ncol, "condition": float(sv[0] / sv[-1]),
             "fit residual rms": float(np.sqrt(np.mean(res ** 2))), "test residual rms": float(np.sqrt(np.mean(np.square(test)))),
             "lowest pulled-back height": float(min(taus)), "seconds": round(time.time() - t0, 1),
             "v on the parabolics (max)": max(C.parabolic_v.values())}
    return S, x, stats


# ------------------------------------------------------------------------------------------- reading the modes
def bispectrum(coefs):
    """arg of c_{K1} c_{K2} c_{K3} over a sum-zero triple of the shell (+-); chi({lead > 0}) = sign cos of it on a rotation orbit (L1)"""
    ks = [np.array(k) for k, _ in coefs]
    cs = [z for _, z in coefs]
    for signs in itertools.product((1, -1), repeat=3):
        if np.all(sum(sg * k for sg, k in zip(signs, ks)) == 0):
            prod = 1
            for sg, z in zip(signs, cs):
                prod *= z if sg == 1 else np.conj(z)
            return prod
    return None


def chi_plus(coefs):
    """chi(d+) for d+ = {omega_t > 0} = {leading shell of F < 0}: Morse count (grid where the shell is one direction)"""
    terms = []
    for (m, n), z in coefs:
        terms += [(-z, (m, n)), (-np.conj(z), (-m, -n))]
    K = np.array([k for _, k in terms], dtype=float)
    if np.linalg.matrix_rank(K) == 1:
        return T.chi_grid(T.grid_values(terms, 240) > 0), None
    chi, complete, gap, _ = T.morse_chi(terms)
    assert complete
    return chi, gap


def analyse(S, x):
    """the leading non-vanishing shell at every cusp, its invariants, and the index N = -sum chi(d+) (v is cusp-fixed on all cusps)"""
    rows = {}
    for c in range(S.nc):
        sh = S.shells(x, c, 6)
        scale = max(abs(z) for _, coefs in sh for _, z in coefs)
        lead = next(i for i, (_, coefs) in enumerate(sh) if max(abs(z) for _, z in coefs) > 1e-2 * scale)
        kn, coefs = sh[lead]
        chi, gap = chi_plus(coefs)
        b = bispectrum(coefs) if len(coefs) == 3 else None
        rows[c] = {"killed shells before the leading one (max |c| s)": [float(max(abs(z) for _, z in sh[i][1]) * S.s[c]) for i in range(lead)],
                   "leading shell |k| sqrt(covol)": round(float(kn), 4), "vectors": len(coefs) * 2,
                   "|c| sqrt(covol)": [round(abs(z) * S.s[c], 5) for _, z in coefs],
                   "cos of the triple phase": None if b is None else round(math.cos(math.atan2(b.imag, b.real)), 5),
                   "chi(d+)": chi, "critical gap": None if gap is None else round(gap, 3)}
    N = -sum(r["chi(d+)"] for r in rows.values())
    return rows, N


def member():
    M = T.covering_path()
    assert M.triangulation_isosig(decorated=True) == T.ISOSIG
    return M


if __name__ == "__main__":
    M = member()
    print("=== B1387: the harmonic cusp form of v+ on cube~3.24 (B1386's member), computed ===", flush=True)
    for Kn, tau, seed, ss in ((6, 0.10, 1, 1), (10, 0.10, 1, 1), (14, 0.10, 1, 1), (12, 0.08, 3, 9), (14, 0.09, 2, 3)):
        S, x, st = solve(M, Kn, tau, seed, ss)
        rows, N = analyse(S, x)
        print("Kn %d, sample height %.2f, chart seed %d, sample seed %d: %s" % (Kn, tau, seed, ss, st), flush=True)
        for c, r in rows.items():
            print("   cusp %d: %s" % (c, r), flush=True)
        print("   -> N(v+) = -(chi_0 + chi_1 + chi_2 + chi_3) = %+d" % N, flush=True)
    print("DONE")
