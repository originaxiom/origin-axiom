"""P-727, R76-5 (data-free): the level surface's modulus meshed inside the FULL group's Ford domain D.

D's faces are the full group's isometric spheres (finite, volume-validated in B1846), so no face is missing at any height.
The surface in M is {phi = s mod 1} cut by D: the exact sheets phi = s + n inside the prism over the cusp cell. The grid
is doubly periodic in the lattice coordinates (n1, n2) -- the vertical walls disappear -- with phi unwrapped across the
w2 wall (phi(z + w_k) = phi(z) + c_k).

Every mesh vertex v (canonical position in the cell, sheet n_v) is lifted to the one sheet phi = s by T2^{-n_v}; an
identification by g (a lattice translate or a floor face pairing) between v (sheet n) and g v (sheet n + chi(g)) is the
fibre element f = T2^{-(n + chi(g))} g T2^{n}, whose period class comes from the cocycle cl(AB) = cl(A) + M^{chi(A)} cl(B)
(the monodromy M on H_1(F); fibre_faces.py). The harmonic functions with periods (1,0), (0,1) on the fibre generators
(x, y) then give tau by stage A's energies; det E = 1 is the check.
usage: stage_e_gamma.py NAME s N1 N2 NL"""
import sys, os, math, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from oa_harm import apply_m, chi_word
from stage_b_surface import setup, fibre_generators
from stage_b_modulus import reduce_tau
from fibre_faces import monodromy_from_relators, bfs_fibre

KUHN = [(0, 1, 3, 7), (0, 1, 5, 7), (0, 2, 3, 7), (0, 2, 6, 7), (0, 4, 5, 7), (0, 4, 6, 7)]


class Cocycle:
    """(chi, cl) of group elements; cl in the fibre letters' basis; M^h by integer powers."""
    def __init__(self, M):
        self.M = np.array(M, dtype=object)
        self.Mi = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=object)
        self.pw = {0: np.eye(2, dtype=object)}
    def P(self, h):
        if h not in self.pw:
            A = np.eye(2, dtype=object)
            for _ in range(abs(h)):
                A = A.dot(self.M if h > 0 else self.Mi)
            self.pw[h] = A
        return self.pw[h]
    def mul(self, A, B):
        return (A[0] + B[0], tuple(int(x) for x in np.array(A[1], dtype=object) + self.P(A[0]).dot(np.array(B[1], dtype=object))))
    def inv(self, A):
        v = -self.P(-A[0]).dot(np.array(A[1], dtype=object))
        return (-A[0], tuple(int(x) for x in v))
    def power(self, A, k):
        R = (0, (0, 0))
        B = A if k >= 0 else self.inv(A)
        for _ in range(abs(k)):
            R = self.mul(R, B)
        return R


def main(name, s, N1, N2, NL, T=5.0, verbose=True):
    t0 = time.time()
    G, H, info, wf = setup(name, 12, 0.33, 9604, 7)
    lat = G.lat
    x, y, Kt = fibre_generators(G, wf)
    fib, cl_, sols, cls = monodromy_from_relators(G.gens, G.rels, G.chi)
    assert len(sols) == 1
    Mm = sols[0]; C = Cocycle(Mm)
    Bx = np.array([list(cls(x, Mm, C.Mi)), list(cls(y, Mm, C.Mi))], dtype=float).T
    Binv = np.linalg.inv(Bx)
    def period(el):                       # an element of F (chi = 0) -> its periods on (x, y)
        assert el[0] == 0, el
        pv = Binv @ np.array(el[1], dtype=float)
        assert np.allclose(pv, np.round(pv)), pv
        return np.round(pv)
    # the lattice translations as elements
    def word_el(w):
        return (chi_word(G.chi, w), tuple(int(v) for v in cls(w, Mm, C.Mi)))
    def trans_of(w):
        X = G.wmat(w); return X[0, 1] / X[1, 1]
    T1 = word_el(G.mw) if abs(trans_of(G.mw) - lat.w1) < 1e-7 else C.inv(word_el(G.mw))
    assert abs(abs(trans_of(G.mw)) - abs(lat.w1)) < 1e-7
    if abs(trans_of(G.lw) - lat.w2) < 1e-7:
        T2 = word_el(G.lw)
    else:
        assert abs(trans_of(G.lw) + lat.w2) < 1e-7; T2 = C.inv(word_el(G.lw))
    assert T1[0] == lat.c1 and T2[0] == lat.c2, (T1, T2, lat.c1, lat.c2)
    assert lat.c2 != 0, "this mesher lifts sheets by T2: needs chi(T2) != 0"
    def TK(k1, k2):
        return C.mul(C.power(T1, k1), C.power(T2, k2))
    def jump(n, K):
        """h(T_K v) - h(v) for a vertex on sheet n translated by the lattice vector K: periods of
        f = T2^{-(n + chi(T_K))} T_K T2^{n}, with sheets lifted by T2 (chi(T2) = c2 = +-1)."""
        TKel = TK(int(K[0]), int(K[1]))
        n_after = n + TKel[0]
        f = C.mul(C.mul(C.power(T2, -n_after // lat.c2), TKel), C.power(T2, n // lat.c2))
        return period(f)
    # the full group's spheres with (chi, cl), and their lattice translates near the cell
    tlo = float(os.environ.get("OA_TLO_E", "0.34"))
    raw, conflicts, nseen = bfs_fibre(G, Mm, fib, cl_, int(os.environ.get("OA_GDEPTH", "7")), 0.8 * tlo, keep_all=True)
    assert conflicts == 0
    sph = {}
    for X, chi_, clv in raw:
        cc = X[1, 0]; ctr = -X[1, 1] / cc
        k = np.round(lat.coords(ctr))
        for e1 in (-1, 0, 1):
            for e2 in (-1, 0, 1):
                m1, m2 = int(k[0]) + e1, int(k[1]) + e2
                v = m1 * lat.w1 + m2 * lat.w2
                Y = X @ np.array([[1, v], [0, 1]], dtype=complex)
                el = C.mul((chi_, clv), TK(m1, m2))
                key = (round(abs(cc), 7), round((ctr - v).real, 6), round((ctr - v).imag, 6))
                if key not in sph:
                    sph[key] = (Y, el)
    sph = list(sph.values())
    cA = np.array([q[0][1, 0] for q in sph]); dA = np.array([q[0][1, 1] for q in sph])
    if verbose:
        print(f"{name} s={s}: full-group spheres {len(raw)} (radius > {0.8*tlo:.2f}; translates {len(sph)}); M = {Mm.tolist()}; "
              f"T1 {T1}, T2 {T2}; {time.time()-t0:.0f}s", flush=True)
    # the doubly periodic grid; phi by the series (t >= Y everywhere on the grid)
    a1 = -0.5 + np.arange(N1) / N1; a2 = -0.5 + np.arange(N2) / N2
    ll = np.linspace(math.log(tlo), math.log(T), NL)
    A1, A2, LL = np.meshgrid(a1, a2, ll, indexing="ij")
    Z = A1.ravel() * lat.w1 + A2.ravel() * lat.w2
    PH = np.empty(Z.size)
    for k in range(0, Z.size, 4000):
        PH[k:k + 4000] = H.phi(Z[k:k + 4000], np.exp(LL.ravel()[k:k + 4000]))
    PH = PH.reshape(A1.shape) - s
    if verbose:
        print(f"   grid {N1}x{N2}x{NL}: phi in {time.time()-t0:.0f}s; range {PH.min():+.3f}..{PH.max():+.3f}", flush=True)
    # marching: vertices keyed by canonical position and sheet
    vid = {}; VP = []; VN = []; tris = []      # VP: canonical (u1, u2, lam); VN: sheet n
    def canon(U):
        k1 = math.floor(U[0] + 0.5); k2 = math.floor(U[1] + 0.5)
        return (U[0] - k1, U[1] - k2, U[2]), (k1, k2)
    def vert(Ua, fa, Ub, fb, n):
        lam = fa / (fa - fb)
        U = (Ua[0] + lam * (Ub[0] - Ua[0]), Ua[1] + lam * (Ub[1] - Ua[1]), Ua[2] + lam * (Ub[2] - Ua[2]))
        Cp, K = canon(U)
        nc = n - (K[0] * lat.c1 + K[1] * lat.c2)
        key = (round(Cp[0], 9), round(Cp[1], 9), round(Cp[2], 9), nc)
        if key not in vid:
            vid[key] = len(VP); VP.append(Cp); VN.append(nc)
        return vid[key], K
    for i in range(N1):
        for j in range(N2):
            for k in range(NL - 1):
                corners = []
                for b in range(8):
                    di, dj, dk = b & 1, (b >> 1) & 1, (b >> 2) & 1
                    ii, jj, kk = i + di, j + dj, k + dk
                    w1_, w2_ = ii // N1, jj // N2
                    f = PH[ii % N1, jj % N2, kk] + w1_ * lat.c1 + w2_ * lat.c2
                    U = (a1[ii % N1] + w1_, a2[jj % N2] + w2_, ll[kk])
                    corners.append((U, f))
                fs = [cf for _, cf in corners]
                for n in range(math.ceil(min(fs)), math.floor(max(fs)) + 1):
                    for tet in KUHN:
                        q = [corners[bb] for bb in tet]
                        vals = [cf - n for _, cf in q]
                        pos = [v > 0 for v in vals]
                        npos = sum(pos)
                        if npos in (0, 4):
                            continue
                        P_ = [(q[m][0], vals[m]) for m in range(4) if pos[m]]; N_ = [(q[m][0], vals[m]) for m in range(4) if not pos[m]]
                        if len(P_) == 1:
                            tris.append([vert(P_[0][0], P_[0][1], Uq, fq, n) for Uq, fq in N_])
                        elif len(N_) == 1:
                            tris.append([vert(N_[0][0], N_[0][1], Uq, fq, n) for Uq, fq in P_])
                        else:
                            (pa, fa), (pb, fb) = P_; (nc_, fc), (nd, fd) = N_
                            v1, v2, v3, v4 = vert(pa, fa, nc_, fc, n), vert(pa, fa, nd, fd, n), vert(pb, fb, nd, fd, n), vert(pb, fb, nc_, fc, n)
                            tris.append([v1, v2, v3]); tris.append([v1, v3, v4])
    VP = np.array(VP); VN = np.array(VN)
    if verbose:
        print(f"   marching: {len(VP)} vertices, {len(tris)} triangles, sheets {sorted(set(VN.tolist()))}; {time.time()-t0:.0f}s", flush=True)
    return dict(G=G, H=H, lat=lat, C=C, T1=T1, T2=T2, jump=jump, period=period, sph=sph, cA=cA, dA=dA,
                VP=VP, VN=VN, tris=tris, s=s, T=T, tlo=tlo, t0=t0)



def finish(D, verbose=True):
    """Clip at D's floor, pair the floor faces by their full-group elements, solve the three energies."""
    lat, C, jump, period, sph = D["lat"], D["C"], D["jump"], D["period"], D["sph"]
    G, H, s, T, t0 = D["G"], D["H"], D["s"], D["T"], D["t0"]
    cA, dA = D["cA"], D["dA"]
    VP = [tuple(v) for v in D["VP"]]; VN = list(D["VN"]); tris = D["tris"]
    cvec = np.array([lat.c1, lat.c2])
    def z_of(U):
        return U[0] * lat.w1 + U[1] * lat.w2
    def pen_at(Ps):
        Ps = np.atleast_2d(np.array(Ps, dtype=float))
        Z = Ps[:, 0] * lat.w1 + Ps[:, 1] * lat.w2; Tt = np.exp(Ps[:, 2])
        out = np.empty(len(Z)); J = np.empty(len(Z), int)
        for k in range(0, len(Z), 1000):
            pp = 1 - (np.abs(cA[None, :] * Z[k:k+1000, None] + dA[None, :]) ** 2 + np.abs(cA)[None, :] ** 2 * Tt[k:k+1000, None] ** 2)
            J[k:k+1000] = np.argmax(pp, 1); out[k:k+1000] = pp[np.arange(len(pp)), J[k:k+1000]]
        return out, J
    P0, _ = pen_at(VP)
    inside = list(P0 > 0)
    def canon(U):
        k1 = math.floor(U[0] + 0.5); k2 = math.floor(U[1] + 0.5)
        return (U[0] - k1, U[1] - k2, U[2]), (k1, k2)
    newv = {}; isfloor = [False] * len(VP)
    def frameU(v, K):
        P = VP[v]; return (P[0] + K[0], P[1] + K[1], P[2])
    def cut(a, Ka, b, Kb):
        Ua, Ub = frameU(a, Ka), frameU(b, Kb)
        lam = P0[a] / (P0[a] - P0[b])
        U = tuple(Ua[m] + lam * (Ub[m] - Ua[m]) for m in range(3))
        Cp, K = canon(U)
        n_frame = VN[a] + Ka[0] * lat.c1 + Ka[1] * lat.c2
        nc = n_frame - (K[0] * lat.c1 + K[1] * lat.c2)
        key = (round(Cp[0], 9), round(Cp[1], 9), round(Cp[2], 9), nc)
        if key not in newv:
            newv[key] = len(VP); VP.append(Cp); VN.append(nc); inside.append(False); isfloor.append(True)
        return (newv[key], K)
    out = []
    P0 = list(P0)
    for tr in tris:
        ins = [inside[v] for v, _ in tr]
        k = sum(ins)
        if k == 3:
            continue
        if k == 0:
            out.append(tr); continue
        o = [q for q, z in zip(tr, ins) if not z]; n_ = [q for q, z in zip(tr, ins) if z]
        if len(o) == 1:
            out.append([o[0], cut(o[0][0], o[0][1], n_[0][0], n_[0][1]), cut(o[0][0], o[0][1], n_[1][0], n_[1][1])])
        else:
            c1_ = cut(o[0][0], o[0][1], n_[0][0], n_[0][1]); c2_ = cut(o[1][0], o[1][1], n_[0][0], n_[0][1])
            out.append([o[0], o[1], c2_]); out.append([o[0], c2_, c1_])
        P0 += [0.0] * (len(VP) - len(P0))
    VPa = np.array(VP); VNa = np.array(VN); isfloor = np.array(isfloor)
    # keep the component that reaches the cusp top
    import scipy.sparse.csgraph as csg
    nv = len(VPa)
    I0 = np.array([[q[0] for q in tr] for tr in out])
    Ad = sp.coo_matrix((np.ones(3 * len(I0)), (np.r_[I0[:, 0], I0[:, 1], I0[:, 2]], np.r_[I0[:, 1], I0[:, 2], I0[:, 0]])), shape=(nv, nv))
    ncomp, labc = csg.connected_components(Ad, directed=False)
    top = np.where(VPa[:, 2] > math.log(T) - 1e-6)[0]
    keepc = set(labc[top])
    out = [tr for tr in out if labc[tr[0][0]] in keepc]
    used = sorted(set(q[0] for tr in out for q in tr))
    fl = np.array([v for v in used if isfloor[v]], dtype=int)
    # exact projection of the floor vertices onto {phi = s + n} and their sphere
    _, Jf = pen_at(VPa[fl])
    def F2(Pts, j, nlev):
        Z = Pts[:, 0] * lat.w1 + Pts[:, 1] * lat.w2; Tt = np.exp(Pts[:, 2])
        f1 = H.phi(Z, Tt) - (s + nlev)
        f2 = np.abs(cA[j] * Z + dA[j]) ** 2 + np.abs(cA[j]) ** 2 * Tt ** 2 - 1
        return np.stack([f1, f2], 1)
    Xf = VPa[fl].copy(); nf = VNa[fl]
    for _ in range(5):
        F0 = F2(Xf, Jf, nf); Jm = np.zeros((len(fl), 2, 3)); h = 1e-6
        for d_ in range(3):
            Xp = Xf.copy(); Xp[:, d_] += h; Jm[:, :, d_] = (F2(Xp, Jf, nf) - F0) / h
        JJt = np.einsum("nij,nkj->nik", Jm, Jm)
        Xf -= np.einsum("nji,nj->ni", Jm, np.linalg.solve(JJt + 1e-18 * np.eye(2), F0[..., None])[..., 0])
    proj = float(np.abs(F2(Xf, Jf, nf)).max())
    VPa[fl] = Xf
    # floor boundary edges (in the canonical cell, with their frame shifts)
    from collections import Counter
    ec = Counter(); eK = {}
    for tr in out:
        for (a, Ka), (b, Kb) in ((tr[0], tr[1]), (tr[1], tr[2]), (tr[2], tr[0])):
            key = (min(a, b), max(a, b)); ec[key] += 1
            dK = (Kb[0] - Ka[0], Kb[1] - Ka[1]) if a < b else (Ka[0] - Kb[0], Ka[1] - Kb[1])
            eK[key] = dK                      # shift of the larger-index vertex relative to the smaller, in a shared frame
    bedges = [e for e, n in ec.items() if n == 1 and isfloor[e[0]] and isfloor[e[1]]]
    stray = [e for e, n in ec.items() if n == 1 and not (isfloor[e[0]] and isfloor[e[1]]) and
             not (VPa[e[0], 2] > math.log(T) - 1e-6 and VPa[e[1], 2] > math.log(T) - 1e-6)]
    def X3(Ps):
        Ps = np.atleast_2d(Ps); Z = Ps[:, 0] * lat.w1 + Ps[:, 1] * lat.w2
        return np.c_[Z.real, Z.imag, np.exp(Ps[:, 2])]
    BE = np.array(bedges)
    # pairings: node-to-segment onto the nearest floor edge (with lattice translates), the period of the fibre element
    rows = []; worst = 0.0
    for idx, p in enumerate(fl):
        j = Jf[idx]; Y, el = sph[j]
        P = VPa[p]; z = P[0] * lat.w1 + P[1] * lat.w2; t = math.exp(P[2])
        z2, t2 = apply_m(Y, z, t)
        c2 = lat.coords(z2); Kq = (math.floor(c2[0] + 0.5), math.floor(c2[1] + 0.5))
        q = np.array([c2[0] - Kq[0], c2[1] - Kq[1], math.log(t2)])
        gq = C.mul(C.power(D["T1"], -Kq[0]), C.mul(C.power(D["T2"], -Kq[1]), el))
        n_p = int(VNa[p]); n_q = n_p + gq[0]
        f = C.mul(C.mul(C.power(D["T2"], -n_q // lat.c2), gq), C.power(D["T2"], n_p // lat.c2))
        cf = period(f)
        best = None
        for s1 in (-1, 0, 1):
            for s2 in (-1, 0, 1):
                A_ = VPa[BE[:, 0]] + np.array([s1, s2, 0]); B_ = VPa[BE[:, 1]] + np.array([s1, s2, 0]) + np.array([[eK[tuple(e)][0], eK[tuple(e)][1], 0] for e in BE])
                A3 = X3(A_); B3 = X3(B_); q3 = X3(q)[0]
                AB = B3 - A3; AQ = q3[None, :] - A3
                lamb = np.clip(np.sum(AQ * AB, 1) / np.maximum(np.sum(AB * AB, 1), 1e-300), 0, 1)
                dist = np.linalg.norm(A3 + lamb[:, None] * AB - q3[None, :], axis=1)
                k = int(np.argmin(dist))
                if best is None or dist[k] < best[0]:
                    best = (dist[k], k, lamb[k], (s1, s2))
        d0, k, lamb, (s1, s2) = best; worst = max(worst, d0)
        a, b = BE[k]; dK = eK[(min(a, b), max(a, b))]
        Ka = (s1, s2); Kb = (s1 + dK[0], s2 + dK[1])
        # h at the copies: h(T_K v) = h_v + jump(n_v, K)
        ja = jump(int(VNa[a]), Ka); jb = jump(int(VNa[b]), Kb)
        # slave rule: by the sphere centres of g and its inverse (canonical, lexicographic)
        cg = -Y[1, 1] / Y[1, 0]; cgi = Y[0, 0] / Y[1, 0]
        ka = tuple(np.round(lat.coords(cg) - np.floor(lat.coords(cg) + 0.5), 6)); kb = tuple(np.round(lat.coords(cgi) - np.floor(lat.coords(cgi) + 0.5), 6))
        tie = (ka == kb)
        slave = (ka < kb) if not tie else (tuple(np.round(P[:2], 9)) < tuple(np.round(q[:2], 9)))   # a face paired with its own translate: split by position
        rows.append((p, a, b, lamb, cf, ja, jb, slave, tie))
    cons = [r for r in rows if r[7]]
    # energies (cotangent on unwrapped frames; edge offsets from the frame shifts)
    W = {}; Doff = {}
    for tr in out:
        Ps = np.array([[VPa[v][0] + K[0], VPa[v][1] + K[1], VPa[v][2]] for v, K in tr])
        Q = X3(Ps); J_ = [jump(int(VNa[v]), K) for v, K in tr]
        for a_, b_, c_ in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            e1 = Q[a_] - Q[c_]; e2 = Q[b_] - Q[c_]
            cr = np.linalg.norm(np.cross(e1, e2))
            if cr < 1e-300:
                continue
            i_, j_ = tr[a_][0], tr[b_][0]
            key = (min(i_, j_), max(i_, j_))
            off = (J_[a_] - J_[b_]) if i_ < j_ else (J_[b_] - J_[a_])     # h(U_lo) - h(U_hi) = h_lo - h_hi + off
            W[key] = W.get(key, 0.0) + 0.5 * np.dot(e1, e2) / cr
            if key in Doff and np.abs(Doff[key] - off).max() > 1e-9:
                raise RuntimeError("inconsistent edge offsets (a seam bookkeeping error)")
            Doff[key] = off
    remap = -np.ones(len(VPa), int); remap[used] = np.arange(len(used)); n = len(used)
    I = np.array([remap[k[0]] for k in W]); Jx = np.array([remap[k[1]] for k in W]); w = np.array(list(W.values()))
    Do = np.array([Doff[k] for k in W])
    Lm = sp.coo_matrix((np.r_[w, w, -w, -w], (np.r_[I, Jx, I, Jx], np.r_[I, Jx, Jx, I])), shape=(n, n)).tocsr()
    m = len(cons) + 1
    ri, ci, vv = [], [], []
    for r_, (p, a, b, lamb, cf, ja, jb, _, _t) in enumerate(cons):
        ri += [r_, r_, r_]; ci += [remap[p], remap[a], remap[b]]; vv += [1.0, -(1 - lamb), -lamb]
    ri.append(m - 1); ci.append(0); vv.append(1.0)
    Cm = sp.coo_matrix((vv, (ri, ci)), shape=(m, n)).tocsr()
    K = sp.bmat([[2 * Lm, Cm.T], [Cm, None]]).tocsc(); lu = spla.splu(K)
    def E(pvec):
        dd = Do @ pvec
        # constraint: h_p = (1-l)(h_a + ja.p) + l (h_b + jb.p) - cf.p
        d = np.array([float((1 - r[3]) * np.dot(r[5], pvec) + r[3] * np.dot(r[6], pvec) - np.dot(r[4], pvec)) for r in cons] + [0.0])
        # energy with offsets: sum w (h_i - h_j + dd)^2 -> gradient 2L h + 2 B dd; solve KKT for min
        bvec = np.zeros(n); np.add.at(bvec, I, -w * dd * 2); np.add.at(bvec, Jx, w * dd * 2)
        sol = lu.solve(np.r_[bvec, d]); hh = sol[:n]
        return float(np.sum(w * (hh[I] - hh[Jx] + dd) ** 2)), float(np.abs(Cm @ hh - d).max())
    E11, r1 = E(np.array([1.0, 0.0])); E22, r2 = E(np.array([0.0, 1.0])); Ep, r3 = E(np.array([1.0, 1.0]))
    E12 = (Ep - E11 - E22) / 2
    tau = complex(-E12 / E22, 1 / E22)
    info = dict(vertices=n, triangles=len(out), floor=len(fl), proj=proj, pair_dist=worst, cons=len(cons), rows=len(rows),
                stray=len(stray), ties=sum(1 for r in rows if r[8]), detE=E11 * E22 - E12 ** 2, cres=max(r1, r2, r3), seconds=time.time() - t0)
    return tau, info

if __name__ == "__main__":
    name, s = sys.argv[1], float(sys.argv[2])
    N1, N2, NL = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    D = main(name, s, N1, N2, NL)
    tau, info = finish(D)
    tr = reduce_tau(tau)
    print(f"   tau {tau.real:+.6f}{tau.imag:+.6f}i  reduced {tr.real:+.6f}{tr.imag:+.6f}i  detE-1 {info['detE']-1:+.2e}  {info}", flush=True)
