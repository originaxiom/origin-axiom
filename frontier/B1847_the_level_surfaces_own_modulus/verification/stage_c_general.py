"""P-727 stage C (data-free): the level surface's modulus where the surface folds (the excursion's tube level).

No graph assumption. The exact level {phi = s} (phi single-valued on H^3; this level is one sheet) is triangulated by
marching tetrahedra on a grid in (u, v, log t), periodic in u (the fibre's cusp translation, period 0 for both periods),
its vertices projected onto the exact level by Newton, the mesh clipped at the fibre group's Ford floor (the boundary
vertices projected onto the exact intersection with their sphere), and the face pairings imposed as constraints
(node-to-segment: a slave arc's vertex equals the master arc's interpolant at its exact image, plus the period), solved
by a sparse KKT system for the energies of the period classes (1,0), (0,1), (1,1). tau and det E = 1 as before.
Validation first: m004 (no fold) must reproduce the graph method; the excursion at s = 1/4 must agree with it there.
usage: stage_c_general.py NAME s NU NV NL"""
import sys, os, math, time, pickle
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from oa_harm import apply_m
from fastpull import pullback_batch
from stage_b_surface import setup, fibre_generators
from stage_b_modulus import fibre_spheres, reduce_tau

KUHN = [(0, 1, 3, 7), (0, 1, 5, 7), (0, 2, 3, 7), (0, 2, 6, 7), (0, 4, 5, 7), (0, 4, 6, 7)]   # cube corners as bits (iu, iv, il)


def main(name, s, NU, NV, NL, T=5.0, verbose=True):
    t0 = time.time()
    G, H, info, wf = (setup("m004", 6, 0.55, 900, 6) if name == "m004" else setup(name, 12, 0.33, 9604, 7))
    x, y, Kt = fibre_generators(G, wf)
    lat = G.lat; L = abs(wf); e = wf / L; nu = 1j * e
    g = lat.phi_lin(nu) - lat.phi_lin(0); W = abs(1 / g); vs = s / g
    els = fibre_spheres(G, x, y)
    sph = []
    for w, M, c in els:
        cc = M[1, 0]; ctr = -M[1, 1] / cc
        uc = (ctr * np.conj(e)).real
        n0 = math.floor((uc + L / 2) / L)
        for k_ in (-1, 0, 1):
            n = n0 + k_
            Tv = np.array([[1, n * wf], [0, 1]], dtype=complex)
            sph.append((M @ Tv, c, w))
    cA = np.array([q[0][1, 0] for q in sph]); dA = np.array([q[0][1, 1] for q in sph])

    def phi_xyz(U, V, Lm):
        Z = U * e + V * nu; Tt = np.exp(Lm)
        Zs, Ts, C = pullback_batch(G, Z, Tt)
        out = np.empty(len(Z))
        for k in range(0, len(Z), 4000):
            out[k:k + 4000] = H.phi(Zs[k:k + 4000], Ts[k:k + 4000])
        return out - C

    def pen(U, V, Lm):
        Z = U * e + V * nu; Tt = np.exp(Lm)
        P = np.empty(len(Z)); J = np.empty(len(Z), int)
        for k in range(0, len(Z), 2000):
            z = Z[k:k + 2000]; t = Tt[k:k + 2000]
            pp = 1 - (np.abs(cA[None, :] * z[:, None] + dA[None, :]) ** 2 + np.abs(cA)[None, :] ** 2 * t[:, None] ** 2)
            J[k:k + 2000] = np.argmax(pp, axis=1); P[k:k + 2000] = pp[np.arange(len(z)), J[k:k + 2000]]
        return P, J

    tlo = float(os.environ.get("OA_TLO_C", "0.33" if name != "m004" else "0.75"))
    us = -L / 2 + L * np.arange(NU) / NU
    WV = float(os.environ.get('OA_VWIN', '1.5'))
    vv = vs + np.linspace(-W * WV, W * WV, NV)
    ll = np.linspace(math.log(tlo), math.log(T), NL)
    UU, VV, LL = np.meshgrid(us, vv, ll, indexing="ij")
    F = phi_xyz(UU.ravel(), VV.ravel(), LL.ravel()).reshape(UU.shape) - s
    if verbose:
        print(f"{name} s={s}: grid {NU}x{NV}x{NL} phi in {time.time()-t0:.0f}s; v-window +-{WV*W:.3f} around {vs:.3f}", flush=True)
    # marching tetrahedra with shared edge vertices
    vid = {}; VX = []; tris = []
    def corner(i, j, k, b):
        return ((i + (b & 1)) % NU, j + ((b >> 1) & 1), k + ((b >> 2) & 1), (i + (b & 1)) // NU)    # last: wrapped?
    def vert(a, b):
        key = (min(a[:3], b[:3]), max(a[:3], b[:3]))
        if key in vid:
            return vid[key]
        fa, fb = F[a[:3]], F[b[:3]]
        lam = fa / (fa - fb)
        ua = us[a[0]] + a[3] * L; ub = us[b[0]] + b[3] * L
        p = (ua + lam * (ub - ua), vv[a[1]] + lam * (vv[b[1]] - vv[a[1]]), ll[a[2]] + lam * (ll[b[2]] - ll[a[2]]))
        vid[key] = len(VX); VX.append(p); return vid[key]
    for i in range(NU):
        for j in range(NV - 1):
            for k in range(NL - 1):
                cs = [corner(i, j, k, b) for b in range(8)]
                for tet in KUHN:
                    q = [cs[b] for b in tet]
                    sg = [F[c[:3]] > 0 for c in q]
                    npos = sum(sg)
                    if npos == 0 or npos == 4:
                        continue
                    P_ = [c for c, z in zip(q, sg) if z]; N_ = [c for c, z in zip(q, sg) if not z]
                    if len(P_) == 1:
                        tris.append([vert(P_[0], n) for n in N_])
                    elif len(N_) == 1:
                        tris.append([vert(N_[0], p) for p in P_])
                    else:
                        a, b = P_; c_, d = N_
                        v1, v2, v3, v4 = vert(a, c_), vert(a, d), vert(b, d), vert(b, c_)
                        tris.append([v1, v2, v3]); tris.append([v1, v3, v4])
    VX = np.array(VX); tris = np.array(tris)
    VX[:, 0] = np.mod(VX[:, 0] + L / 2, L) - L / 2
    # Newton projection onto the exact level
    for _ in range(3):
        h = 1e-6
        f0 = phi_xyz(VX[:, 0], VX[:, 1], VX[:, 2]) - s
        gu = (phi_xyz(VX[:, 0] + h, VX[:, 1], VX[:, 2]) - s - f0) / h
        gv = (phi_xyz(VX[:, 0], VX[:, 1] + h, VX[:, 2]) - s - f0) / h
        gl = (phi_xyz(VX[:, 0], VX[:, 1], VX[:, 2] + h) - s - f0) / h
        n2 = gu ** 2 + gv ** 2 + gl ** 2
        st = f0 / np.maximum(n2, 1e-300)
        VX[:, 0] -= st * gu; VX[:, 1] -= st * gv; VX[:, 2] -= st * gl
    res = np.abs(phi_xyz(VX[:, 0], VX[:, 1], VX[:, 2]) - s).max()
    if verbose:
        print(f"   marching: {len(VX)} vertices, {len(tris)} triangles; on the exact level to {res:.1e}; {time.time()-t0:.0f}s", flush=True)
    return dict(vlim=(vv[0], vv[-1]), llim=(ll[0], ll[-1]), G=G, H=H, L=L, e=e, nu=nu, VX=VX, tris=tris, sph=sph, cA=cA, dA=dA, pen=pen, phi=phi_xyz, s=s, T=T,
                x=x, y=y, t0=t0)



def solve_modulus_general(D, verbose=True):
    G, H, L, e, nu = D["G"], D["H"], D["L"], D["e"], D["nu"]
    VX, tris, sph, pen, phi, s = D["VX"].copy(), D["tris"], D["sph"], D["pen"], D["phi"], D["s"]
    t0 = D["t0"]
    # the window must contain the piece: no mesh vertex may sit on the v-walls
    near_wall = np.sum((VX[:, 1] - D["vlim"][0] < 1e-9) | (D["vlim"][1] - VX[:, 1] < 1e-9))
    P, J = pen(VX[:, 0], VX[:, 1], VX[:, 2])
    inside = P > 0
    # clip at the floor (pen = 0), sharing the new edge vertices
    newv = {}; NVX = [tuple(v) for v in VX]; lab = list(J); isfloor = [False] * len(VX)
    def cut(a, b):
        key = (min(a, b), max(a, b))
        if key in newv:
            return newv[key]
        lam = P[a] / (P[a] - P[b])
        pa, pb = np.array(NVX[a]), np.array(NVX[b])
        db = pb - pa; db[0] = (db[0] + L / 2) % L - L / 2       # periodic in u
        newv[key] = len(NVX); NVX.append(tuple(pa + lam * db)); lab.append(-1); isfloor.append(True)
        return newv[key]
    out = []
    for tr in tris:
        ins = [inside[v] for v in tr]
        k = sum(ins)
        if k == 3:
            continue
        if k == 0:
            out.append(list(tr)); continue
        o = [v for v, z in zip(tr, ins) if not z]; n_ = [v for v, z in zip(tr, ins) if z]
        if len(o) == 1:
            out.append([o[0], cut(o[0], n_[0]), cut(o[0], n_[1])])
        else:
            a1, a2 = cut(o[0], n_[0]), cut(o[1], n_[0])
            out.append([o[0], o[1], a2]); out.append([o[0], a2, a1])
    X = np.array(NVX); TR = np.array(out); isfloor = np.array(isfloor)
    X[:, 0] = np.mod(X[:, 0] + L / 2, L) - L / 2
    # the fundamental piece is connected and contains the cusp: keep the triangles connected to the top
    import scipy.sparse.csgraph as csg
    nv = len(X)
    Ad = sp.coo_matrix((np.ones(3 * len(TR)), (np.r_[TR[:, 0], TR[:, 1], TR[:, 2]], np.r_[TR[:, 1], TR[:, 2], TR[:, 0]])), shape=(nv, nv))
    ncomp, labc = csg.connected_components(Ad, directed=False)
    topv = np.where(X[:, 2] > math.log(D["T"]) - 1e-6)[0]
    keepc = set(labc[topv]) if len(topv) else set()
    keep_t = np.array([labc[tr[0]] in keepc for tr in TR])
    dropped = int((~keep_t).sum()); TR = TR[keep_t]
    fl = np.where(isfloor)[0]
    # exact projection of the floor vertices onto {phi = s} and their sphere (2 equations, minimal-norm Newton)
    _, Jf = pen(X[fl, 0], X[fl, 1], X[fl, 2])
    cA, dA = D["cA"], D["dA"]
    def sphere_res(idx, j):
        z = X[idx, 0] * e + X[idx, 1] * nu; t = np.exp(X[idx, 2])
        return np.abs(cA[j] * z + dA[j]) ** 2 + np.abs(cA[j]) ** 2 * t * t - 1
    for _ in range(4):
        h = 1e-6
        F1 = phi(X[fl, 0], X[fl, 1], X[fl, 2]) - s; F2 = sphere_res(fl, Jf)
        Jm = np.zeros((len(fl), 2, 3))
        for d_ in range(3):
            Xp = X[fl].copy(); Xp[:, d_] += h
            Jm[:, 0, d_] = (phi(Xp[:, 0], Xp[:, 1], Xp[:, 2]) - s - F1) / h
            z = Xp[:, 0] * e + Xp[:, 1] * nu; t = np.exp(Xp[:, 2])
            Jm[:, 1, d_] = (np.abs(cA[Jf] * z + dA[Jf]) ** 2 + np.abs(cA[Jf]) ** 2 * t * t - 1 - F2) / h
        Fv = np.stack([F1, F2], axis=1)
        JJt = np.einsum("nij,nkj->nik", Jm, Jm)
        step = np.einsum("nji,nj->ni", Jm, np.linalg.solve(JJt + 1e-18 * np.eye(2), Fv[..., None])[..., 0])
        X[fl] -= step
    X[:, 0] = np.mod(X[:, 0] + L / 2, L) - L / 2
    proj_res = max(np.abs(phi(X[fl, 0], X[fl, 1], X[fl, 2]) - s).max(), np.abs(sphere_res(fl, Jf)).max())
    # the floor boundary edges
    from collections import Counter
    ec = Counter()
    for tr in TR:
        for a, b in ((tr[0], tr[1]), (tr[1], tr[2]), (tr[2], tr[0])):
            ec[(min(a, b), max(a, b))] += 1
    bedges = [e_ for e_, n in ec.items() if n == 1 and isfloor[e_[0]] and isfloor[e_[1]]]
    other_b = [e_ for e_, n in ec.items() if n == 1 and not (isfloor[e_[0]] and isfloor[e_[1]])]
    top = math.log(D["T"]) - 1e-9
    stray = [e_ for e_ in other_b if not (X[e_[0], 2] > top - 1e-6 and X[e_[1], 2] > top - 1e-6)]
    stray_t = np.exp(np.array([X[e_[0], 2] for e_ in stray])) if stray else np.array([])
    lab_f = dict(zip(fl, Jf))
    def X3(idx_pts):
        z = idx_pts[:, 0] * e + idx_pts[:, 1] * nu
        return np.c_[z.real, z.imag, np.exp(idx_pts[:, 2])]
    # pairings: every floor vertex p on sphere j maps by its element to q; node-to-segment onto the nearest floor edge
    BE = np.array(bedges)
    A3 = X3(X[BE[:, 0]]); B3 = X3(X[BE[:, 1]])
    words = [q[2] for q in sph]
    rows = []; worst = 0.0
    for p in fl:
        j = lab_f[p]; M, c, w = sph[j]
        z = X[p, 0] * e + X[p, 1] * nu; t = math.exp(X[p, 2])
        z2, t2 = apply_m(M, z, t)
        u2 = (z2 * np.conj(e)).real; v2 = (z2 * np.conj(nu)).real
        u2 = (u2 + L / 2) % L - L / 2
        best = None
        for sh in (0.0, L, -L):
            q3 = np.array([(u2 + sh) * e.real + v2 * nu.real, (u2 + sh) * e.imag + v2 * nu.imag, t2])
            AB = B3 - A3; AQ = q3[None, :] - A3
            lamb = np.clip(np.sum(AQ * AB, 1) / np.maximum(np.sum(AB * AB, 1), 1e-300), 0, 1)
            dist = np.linalg.norm(A3 + lamb[:, None] * AB - q3[None, :], axis=1)
            k = int(np.argmin(dist))
            if best is None or dist[k] < best[0]:
                best = (dist[k], k, lamb[k])
        d0, k, lamb = best
        worst = max(worst, d0)
        rows.append((p, BE[k, 0], BE[k, 1], lamb, c, w))
    # master/slave by the pair's word order: the vertex is a slave iff its own word sorts before its image's word
    inv = lambda w_: "".join({"x": "X", "X": "x", "y": "Y", "Y": "y"}[ch] for ch in reversed(w_))
    cons = [r for r in rows if r[5] < inv(r[5])]
    return dict(X=X, TR=TR, cons=cons, proj_res=proj_res, pair_dist=worst, n_floor=len(fl), near_wall=int(near_wall),
                stray_boundary=len(stray), n_cons=len(cons), n_rows=len(rows), dropped_islands=dropped,
                stray_t=(float(stray_t.min()), float(stray_t.max())) if len(stray_t) else None,
                bottom=float(math.exp(D["llim"][0])))


def energies(D, R):
    X0, TR0, L, e, nu = R["X"], R["TR"], D["L"], D["e"], D["nu"]
    used = np.unique(TR0.ravel()); remap = -np.ones(len(X0), int); remap[used] = np.arange(len(used))
    X = X0[used]; TR = remap[TR0]
    cons_in = R["cons"]
    cons_m = [(remap[p], remap[a], remap[b], lamb, c, wd) for (p, a, b, lamb, c, wd) in cons_in]
    assert all(min(q[:3]) >= 0 for q in cons_m), "a constraint references a vertex outside the mesh"
    R = dict(R, cons=cons_m)
    n = len(X)
    W = {}
    for tr in TR:
        P_ = X[tr].copy()
        for m in (1, 2):
            P_[m, 0] = P_[0, 0] + ((P_[m, 0] - P_[0, 0] + L / 2) % L - L / 2)
        z = P_[:, 0] * e + P_[:, 1] * nu
        Q = np.c_[z.real, z.imag, np.exp(P_[:, 2])]
        for a_, b_, c_ in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            e1 = Q[a_] - Q[c_]; e2 = Q[b_] - Q[c_]
            cr = np.linalg.norm(np.cross(e1, e2))
            if cr < 1e-300:
                continue
            key = (min(tr[a_], tr[b_]), max(tr[a_], tr[b_])); W[key] = W.get(key, 0.0) + 0.5 * np.dot(e1, e2) / cr
    I = np.array([k[0] for k in W]); Jx = np.array([k[1] for k in W]); w = np.array(list(W.values()))
    Lm = sp.coo_matrix((np.r_[w, w, -w, -w], (np.r_[I, Jx, I, Jx], np.r_[I, Jx, Jx, I])), shape=(n, n)).tocsr()
    cons = R["cons"]
    m = len(cons) + 1
    ri, ci, vv = [], [], []
    for r_, (p, a, b, lamb, c, wd) in enumerate(cons):
        ri += [r_, r_, r_]; ci += [p, a, b]; vv += [1.0, -(1 - lamb), -lamb]
    ri.append(m - 1); ci.append(0); vv.append(1.0)                     # the gauge
    C = sp.coo_matrix((vv, (ri, ci)), shape=(m, n)).tocsr()
    K = sp.bmat([[2 * Lm, C.T], [C, None]]).tocsc()
    lu = spla.splu(K + sp.eye(K.shape[0]) * 0.0)
    def E(pvec):
        d = np.array([-float(np.dot(c, pvec)) for (_, _, _, _, c, _) in cons] + [0.0])
        sol = lu.solve(np.r_[np.zeros(n), d])
        h = sol[:n]
        return float(h @ (Lm @ h)), float(np.abs(C @ h - d).max())
    E11, r1 = E(np.array([1.0, 0.0])); E22, r2 = E(np.array([0.0, 1.0])); Ep, r3 = E(np.array([1.0, 1.0]))
    E12 = (Ep - E11 - E22) / 2
    tau = complex(-E12 / E22, 1 / E22)
    return tau, dict(detE=E11 * E22 - E12 ** 2, constraint_res=max(r1, r2, r3), vertices=n, triangles=len(TR),
                     negative_cot=int(np.sum(w < 0)))

if __name__ == "__main__":
    name, s = sys.argv[1], float(sys.argv[2])
    NU, NV, NL = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    D = main(name, s, NU, NV, NL)
    R = solve_modulus_general(D)
    print(f"   clip: {R['n_floor']} floor vertices projected to {R['proj_res']:.1e}; pairing images to the nearest floor edge "
          f"<= {R['pair_dist']:.1e}; constraints {R['n_cons']} of {R['n_rows']}; v-wall vertices {R['near_wall']}; "
          f"stray boundary edges {R['stray_boundary']} (heights {R['stray_t']}; grid bottom {R['bottom']:.3f}); islands dropped {R['dropped_islands']}; {time.time()-D['t0']:.0f}s", flush=True)
    tau, info = energies(D, R)
    tr = reduce_tau(tau)
    print(f"   tau {tau.real:+.6f}{tau.imag:+.6f}i  reduced {tr.real:+.6f}{tr.imag:+.6f}i  detE-1 {info['detE']-1:+.2e}  "
          f"constraint residual {info['constraint_res']:.1e}  {info}  {time.time()-D['t0']:.0f}s", flush=True)
