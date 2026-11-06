"""P-727 stage B (data-free): the conformal modulus of the harmonic level surface Sigma_s = {phi = s} of a member.

Pipeline (each piece checked):
  1. phi on H^3 by B1846's collocation, anywhere by exact pullback;
  2. the fibre group F = <x, y> (chi = 0; [x, y] = the fibre's cusp translation along wf);
  3. the level surface as a graph v(u, t) over the strip (u along wf), tabulated by vectorised Newton continuation and
     interpolated; spot-checked by exact evaluation (phi(node) = s);
  4. F's isometric spheres (words in x, y; periods = exponent sums), the floor t_floor(u) where the surface first enters
     one, the face pairings g: floor -> floor (checked: images on the surface and on the floor);
  5. stage A's column mesh and cotangent energies on the surface's 3D positions -> tau; det E = 1 as the check;
  6. tau reduced to the standard fundamental domain (marking-free comparison).
usage: stage_b_modulus.py NAME s [res_arc res_lev]"""
import sys, os, math, cmath, time, json
import numpy as np
from scipy.interpolate import RectBivariateSpline
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from oa_harm import apply_m, chi_word
from stage_b_surface import setup, fibre_generators
from stage_a_control import UF, build_and_solve_cols


def reduce_tau(tau):
    for _ in range(200):
        tau = complex(tau.real - round(tau.real), tau.imag)
        if abs(tau) < 1 - 1e-12:
            tau = -1 / tau
        else:
            break
    return tau


class Surface:
    def __init__(self, G, H, wf, s, T=5.0, tlow=0.2, nu=161, nt=161):
        self.G, self.H, self.wf, self.s = G, H, wf, s
        self.L = abs(wf); self.e = wf / self.L; self.nu_ = 1j * self.e
        lat = G.lat
        g = lat.phi_lin(self.nu_) - lat.phi_lin(0)
        self.vs = s / g
        self.us = np.linspace(-self.L / 2, self.L / 2, nu)
        self.lts = np.linspace(math.log(T), math.log(tlow), nt)
        V = np.empty((nu, nt)); D = np.empty((nu, nt))
        v = np.full(nu, self.vs, dtype=float)
        for j, lt in enumerate(self.lts):
            t = math.exp(lt)
            for _ in range(25):
                f0 = self.phi_batch(self.us, v, t) - s
                f1 = self.phi_batch(self.us, v + 1e-6, t) - s
                d = (f1 - f0) / 1e-6
                step = np.clip(-f0 / d, -0.2, 0.2)
                v = v + step
                if np.max(np.abs(step)) < 1e-11:
                    break
            V[:, j] = v; D[:, j] = d
        self.V = V; self.dphi = D
        # periodic in u (the commutator translation): extend by one period on each side for the spline
        uu = np.r_[self.us[:-1] - self.L, self.us, self.us[1:] + self.L]
        VV = np.r_[V[:-1], V, V[1:]]
        self.spl = RectBivariateSpline(uu, self.lts[::-1], VV[:, ::-1], kx=3, ky=3)

    def phi_batch(self, us, vs, t):
        from fastpull import pullback_batch
        us = np.atleast_1d(np.asarray(us, dtype=float)); vs = np.atleast_1d(np.asarray(vs, dtype=float))
        Z = us * self.e + vs * self.nu_
        Tt = np.broadcast_to(np.asarray(t, dtype=float), Z.shape).copy()
        Zs, Ts, Cs = pullback_batch(self.G, Z, Tt)
        out = np.empty(len(Z))
        for k in range(0, len(Z), 4000):
            out[k:k + 4000] = self.H.phi(Zs[k:k + 4000], Ts[k:k + 4000])
        return out - Cs

    def v(self, u, t):
        u = np.mod(np.asarray(u) + self.L / 2, self.L) - self.L / 2
        return self.spl.ev(u, np.log(t))

    def point(self, u, t):
        return u * self.e + self.v(u, t) * self.nu_

    def coords(self, z):
        u = (z * np.conj(self.e)).real; v = (z * np.conj(self.nu_)).real
        return u, v


def fibre_spheres(G, x, y, depth=int(os.environ.get('OA_FDEPTH', '8'))):
    """F's elements as (matrix, periods) from reduced words in x, y; their isometric spheres (centre, radius)."""
    gens = {"x": (G.wmat(x), np.array([1.0, 0.0])), "X": (np.linalg.inv(G.wmat(x)), np.array([-1.0, 0.0])),
            "y": (G.wmat(y), np.array([0.0, 1.0])), "Y": (np.linalg.inv(G.wmat(y)), np.array([0.0, -1.0]))}
    inv = {"x": "X", "X": "x", "y": "Y", "Y": "y"}
    out = []; seen = set()
    frontier = [("", np.eye(2, dtype=complex), np.zeros(2))]
    for _ in range(depth):
        nxt = []
        for w, M, c in frontier:
            for kk, (Gm, cg) in gens.items():
                if w and inv[kk] == w[-1]:
                    continue
                M2 = M @ Gm; c2 = c + cg
                if np.abs(M2).max() > float(os.environ.get('OA_FNORM', '300')):
                    continue
                nxt.append((w + kk, M2, c2))
                cc = M2[1, 0]
                if abs(cc) > 1e-9 and 1 / abs(cc) > float(os.environ.get('OA_FRMIN', '0.08')):
                    key = (round(abs(cc), 7), round((-M2[1, 1] / cc).real, 6), round((-M2[1, 1] / cc).imag, 6))
                    if key not in seen:
                        seen.add(key); out.append((w + kk, M2, c2))
        frontier = nxt
    return out


def run(name, s, n_arc=120, nlev=80, verbose=True):
    t0 = time.time()
    if name == "m004":
        G, H, info, wf = setup("m004", 6, 0.55, 900, 6)
    else:
        G, H, info, wf = setup(name, 12, 0.33, 9604, 7)
    x, y, Kt = fibre_generators(G, wf)
    import pickle
    tl = float(os.environ.get('OA_TLOW', '0.6')); nu_ = int(os.environ.get('OA_NU', '241')); nt_ = int(os.environ.get('OA_NT', '121'))
    cf = os.path.join(HERE, "cache", f"surf_{name}_{s:.4f}_{tl:.3f}_{nu_}_{nt_}.pkl")
    if os.path.exists(cf):
        S = pickle.load(open(cf, "rb")); S.G, S.H = G, H
    else:
        S = Surface(G, H, wf, s, tlow=tl, nu=nu_, nt=nt_)
        os.makedirs(os.path.dirname(cf), exist_ok=True)
        G_, H_ = S.G, S.H; S.G = S.H = None
        pickle.dump(S, open(cf, "wb")); S.G, S.H = G_, H_
    L = S.L
    # exact spot check of the tabulated surface
    if verbose:
        print(f"{name} s={s}: fibre group x={x}, y={y}, [x,y] = translation {Kt:.6f}; surface table t >= {math.exp(S.lts[-1]):.3f}, "
              f"min |dphi/dv| {np.min(np.abs(S.dphi)):.3e}; {time.time()-t0:.0f}s", flush=True)
    els = fibre_spheres(G, x, y)
    # sphere translates along wf (by the commutator, period 0) into a window around the strip
    sph = []
    for w, M, c in els:
        cc = M[1, 0]; ctr = -M[1, 1] / cc; r = 1 / abs(cc)
        uc, vc = S.coords(ctr)
        n0 = math.floor((uc + L / 2) / L)
        for e_ in (-1, 0, 1):
            n = n0 + e_
            Tv = np.array([[1, n * wf], [0, 1]], dtype=complex)
            M2 = M @ Tv
            sph.append((ctr - n * wf, r, M2, c, w))
    C = np.array([q[0] for q in sph]); Rr = np.array([q[1] for q in sph])
    cA = np.array([q[2][1, 0] for q in sph]); dA = np.array([q[2][1, 1] for q in sph])

    def depth_in(u, t):
        z = complex(S.point(u, t))
        pen = 1 - (np.abs(cA * z + dA) ** 2 + np.abs(cA) ** 2 * t * t)
        j = int(np.argmax(pen)); return pen[j], j

    def floor_of(u):
        lo, hi = 0.21, 1.2
        if depth_in(u, lo)[0] <= 0:
            return None, None
        for _ in range(60):
            mid = math.sqrt(lo * hi)
            if depth_in(u, mid)[0] > 0:
                lo = mid
            else:
                hi = mid
        return hi, depth_in(u, lo)[1]

    ug = np.linspace(-L / 2, L / 2, int(os.environ.get('OA_NFLOOR', '1601')))
    fl = [floor_of(u) for u in ug]
    if any(f[0] is None for f in fl):
        raise RuntimeError("the surface does not enter an F-sphere above t = 0.21 somewhere: extend the table down")
    tf = np.array([f[0] for f in fl]); jf = np.array([f[1] for f in fl])
    faces = []; st = 0
    for i in range(1, len(ug) + 1):
        if i == len(ug) or jf[i] != jf[st]:
            faces.append((jf[st], ug[st], ug[i - 1])); st = i
    if verbose:
        print(f"   F spheres {len(els)} (translates {len(sph)}); floor {tf.min():.4f}..{tf.max():.4f}; faces {len(faces)}: " +
              ", ".join(f"{sph[j][4]}[{a:+.3f},{b:+.3f}]" for j, a, b in faces[:12]) + (" ..." if len(faces) > 12 else ""), flush=True)
    from scipy.interpolate import interp1d
    floor_fn = interp1d(ug, tf, kind="linear")
    if tf.min() < math.exp(S.lts[-1]) * 1.05:
        raise RuntimeError("the floor reaches the bottom of the surface table: lower OA_TLOW")
    rng = np.random.default_rng(3)
    uu = rng.uniform(-L / 2, L / 2, 60)
    tt = np.array([float(floor_fn(u)) * math.exp(rng.uniform(0, math.log(4.0 / float(floor_fn(u))))) for u in uu])
    spot = max(abs(S.phi_batch([u], [float(S.v(u, t))], t)[0] - s) for u, t in zip(uu, tt))
    if verbose:
        print(f"   spline spot check on the domain (60 points, t >= floor): max |phi - s| {spot:.2e}", flush=True)

    def floor(uarr):
        uarr = np.atleast_1d(uarr)
        return floor_fn(np.clip(uarr, -L / 2, L / 2)), None

    # the pairing on floor points: exact Mobius action, then back to strip coordinates
    def pair(j, u):
        t = float(floor_fn(u)); z = complex(S.point(u, t))
        M = sph[j][2]
        z2, t2 = apply_m(M, z, t)
        u2, v2 = S.coords(z2)
        n = math.floor((u2 + L / 2) / L + 1e-12)
        u2r = u2 - n * L
        return u2r, t2, abs(v2 - float(S.v(u2r, t2))), abs(t2 - float(floor_fn(np.clip(u2r, -L / 2, L / 2))))

    # adapt stage A's builder: faces carry (centre, r, M, c, w); arcs are sampled on the surface's floor
    allc = []
    for j, a, b in faces:
        allc.append(sph[j])
    faces2 = [(i, a, b) for i, (j, a, b) in enumerate(faces)]
    worst_v, worst_t = 0.0, 0.0

    class Arc:            # make build_and_solve_cols' arc sampling use the surface floor and the 3D pairing
        pass
    import stage_a_control as SA
    orig_mob = SA.mob

    def mob_surface(M, w):
        # w = u + i t encodes a floor point; return the paired floor point as u' + i t'
        nonlocal worst_v, worst_t
        u, t = w.real, w.imag
        z = complex(S.point(u, t))
        z2, t2 = apply_m(M, z, t)
        u2, v2 = S.coords(z2)
        n = math.floor((u2 + L / 2) / L + 1e-12); u2r = u2 - n * L
        ev_ = abs(v2 - float(S.v(u2r, t2))); et_ = abs(t2 - float(floor_fn(np.clip(u2r, -L / 2, L / 2))))
        worst_v = max(worst_v, ev_); worst_t = max(worst_t, et_)
        import stage_b_modulus as SB
        SB.LAST = (ev_, et_)
        return complex(u2r + n * L, t2)
    SA.mob = mob_surface
    # arcs on the surface floor: stage A samples t = sqrt(r^2 - (u - ctr)^2); replace by the tabulated floor
    allc2 = []
    for (ctr, r, M, c, w) in allc:
        allc2.append((ctr, r, M, c, w))
    SA_math_sqrt = SA.math.sqrt
    def surf3d(u, t):
        z = S.point(u, t)
        return np.c_[np.real(z), np.imag(z), t]
    exact_floor = (lambda u: floor_of(u)[0]) if os.environ.get("OA_EXACT_FLOOR", "1") == "1" else (lambda u: float(floor_fn(u)))
    tau, info2 = build_cols_surface(faces2, allc2, floor_fn, 5.0, L, surf3d, n_arc, nlev, mob_surface, exact_floor)
    SA.mob = orig_mob
    import stage_b_modulus as SB
    if verbose:
        for key, (ev, et) in sorted(SB.FACE_ERR.items(), key=lambda kv: -kv[1][1])[:8]:
            print(f"      face {key[1]:>12s} [{key[2]:+.4f},{key[3]:+.4f}]: pairing off-surface {ev:.1e} off-floor {et:.1e}", flush=True)
    info2.update(spot=spot, pair_off_surface=worst_v, pair_off_floor=worst_t, floor_min=float(tf.min()), seconds=time.time() - t0)
    return tau, reduce_tau(tau), info2


def build_cols_surface(faces, allc, floor_fn, T, k, surface3d, n_arc, nlev, pairmap, exact_floor=None):
    """stage A's column mesh with the floor and pairing supplied by the surface."""
    import stage_a_control as SA
    fl, links = [], []
    import stage_b_modulus as SB
    SB.FACE_ERR = {}
    for j, a, b in faces:
        ctr, r, M, c, w = allc[j]
        nn = max(3, int(n_arc * (b - a) / k) + 2)
        for u in np.linspace(a, b, nn):
            t = exact_floor(u) if exact_floor is not None else float(floor_fn(u))
            SB.LAST = (0.0, 0.0)
            q = pairmap(M, complex(u, t))
            ev, et = SB.LAST
            fe = SB.FACE_ERR.setdefault((j, w, round(a, 4), round(b, 4)), [0.0, 0.0])
            fe[0] = max(fe[0], ev); fe[1] = max(fe[1], et)
            n = math.floor((q.real + k / 2) / k + 1e-12)
            fl.append((u, t)); fl.append((q.real - n * k, q.imag))
            links.append((len(fl) - 2, len(fl) - 1, c.copy()))
    fl.append((-k / 2, float(floor_fn(-k / 2)))); fl.append((k / 2, float(floor_fn(k / 2))))

    class FakeFloor:
        def __call__(self, uarr):
            return np.array([float(floor_fn(np.clip(x, -k / 2, k / 2))) for x in np.atleast_1d(uarr)]), None
    # reuse the stage A builder by handing it pre-sampled floor nodes
    return cols_from_nodes(fl, links, FakeFloor(), T, k, surface3d, nlev, node_t=np.array([p[1] for p in fl]))


def cols_from_nodes(fl, links, floor, T, k, surface3d, nlev, uniq=1e-10, node_t=None):
    import scipy.sparse as sp
    import scipy.sparse.linalg as spla
    U = np.array([p[0] for p in fl]); order = np.argsort(U)
    cols = []; colof = np.empty(len(fl), int)
    for idx in order:
        if cols and abs(U[idx] - cols[-1]) < uniq:
            colof[idx] = len(cols) - 1
        else:
            cols.append(U[idx]); colof[idx] = len(cols) - 1
    cols = np.array(cols); ncol = len(cols)
    fcol, _ = floor(cols)
    if node_t is not None:                       # each column starts at its own floor node's exact height
        fcol = np.array(fcol, dtype=float)
        for idx in range(len(fl)):
            fcol[colof[idx]] = node_t[idx]
    eta = np.linspace(0, 1, nlev)
    tt = np.exp(np.log(fcol)[:, None] + eta[None, :] * (np.log(T) - np.log(fcol))[:, None])
    node = lambda ci, m: ci * nlev + m
    Pu = np.repeat(cols, nlev); Pt = tt.ravel()
    uf = UF(ncol * nlev)
    for i, j, d in links:
        uf.union(node(colof[i], 0), node(colof[j], 0), d)
    for m in range(nlev):
        uf.union(node(0, m), node(ncol - 1, m), np.zeros(2))
    Sx = []
    for ci in range(ncol - 1):
        for m in range(nlev - 1):
            a0, a1, b0, b1 = node(ci, m), node(ci, m + 1), node(ci + 1, m), node(ci + 1, m + 1)
            Sx.append((a0, b0, b1)); Sx.append((a0, b1, a1))
    Sx = np.array(Sx)
    X3 = surface3d(Pu, Pt)
    e1 = X3[Sx[:, 0]]; e2 = X3[Sx[:, 1]]; e3 = X3[Sx[:, 2]]
    W = {}
    for (ia, ib, ic) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        A_ = X3[Sx[:, ia]] - X3[Sx[:, ic]]; B_ = X3[Sx[:, ib]] - X3[Sx[:, ic]]
        cr = np.linalg.norm(np.cross(A_, B_), axis=1)
        cot = np.where(cr > 1e-300, np.sum(A_ * B_, axis=1) / np.maximum(cr, 1e-300), 0.0)
        for (i, j, cv) in zip(Sx[:, ia], Sx[:, ib], cot):
            key = (min(i, j), max(i, j)); W[key] = W.get(key, 0.0) + 0.5 * cv
    roots = {}; cls = np.empty(ncol * nlev, int); off = np.zeros((ncol * nlev, 2))
    for xx in range(ncol * nlev):
        r, o = uf.find(xx); cls[xx] = roots.setdefault(r, len(roots)); off[xx] = o
    n = len(roots)
    I = np.array([e[0] for e in W]); J = np.array([e[1] for e in W]); w = np.array(list(W.values()))
    ci_, cj_ = cls[I], cls[J]; D = off[I] - off[J]
    def energy(pvec):
        dd = D @ pvec
        Lm = sp.coo_matrix((np.r_[w, w, -w, -w], (np.r_[ci_, cj_, ci_, cj_], np.r_[ci_, cj_, cj_, ci_])), shape=(n, n)).tocsr()
        rhs = np.zeros(n); np.add.at(rhs, ci_, -w * dd); np.add.at(rhs, cj_, w * dd)
        Hh = spla.spsolve((Lm + sp.eye(n) * 1e-12).tocsc(), rhs)
        return float(np.sum(w * (Hh[ci_] - Hh[cj_] + dd) ** 2))
    E11 = energy(np.array([1.0, 0.0])); E22 = energy(np.array([0.0, 1.0])); E12 = (energy(np.array([1.0, 1.0])) - E11 - E22) / 2
    tau = complex(-E12 / E22, 1 / E22)
    return tau, dict(columns=ncol, levels=nlev, classes=n, inconsistent_cycles=uf.bad, detE=E11 * E22 - E12 ** 2,
                     negative_cot=int(np.sum(w < 0)))


if __name__ == "__main__":
    name = sys.argv[1]; s = float(sys.argv[2])
    res = [(int(sys.argv[3]), int(sys.argv[4]))] if len(sys.argv) > 4 else [(60, 40), (120, 80)]
    for n_arc, nlev in res:
        tau, tr, info = run(name, s, n_arc, nlev, verbose=(n_arc == res[0][0]))
        print(f"   res ({n_arc},{nlev}): tau {tau.real:+.6f}{tau.imag:+.6f}i  reduced {tr.real:+.6f}{tr.imag:+.6f}i  "
              f"detE-1 {info['detE']-1:+.2e}  bad cycles {info['inconsistent_cycles']}  pairing off-surface {info['pair_off_surface']:.1e} "
              f"off-floor {info['pair_off_floor']:.1e}  {info['seconds']:.0f}s", flush=True)
