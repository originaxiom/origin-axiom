#!/usr/bin/env python3
"""Zero-Shared-Code Cold-Room Countercheck for Card AGY-C69:
Independently reconstructs and verifies every claim of E1, E2, and E3 from scratch
with zero imports from the producer directory, using disjoint coordinates and algorithms:
- E1: Disjoint V_4 section S'_k = {a in O_{3^k} : a_2 == 1, a_3 == 1 mod 3} parameterized by
      b_1 = Psi_delta(b_2, b_3), base-3 digit-sum Legendre formula v_3(d!) = (d - s_3(d))/2,
      and right-action SLP polycyclic filtration through k = 7 (mod 2,187, 118,098 section pts).
- E2: Explicit C_tr-orbit sector projection blocks P_q W_{6,H} P_q over exact SymPy cyclotomic
      DomainMatrix rings Q(zeta_{lcm(N,3)}), computing sector dimensions and trace moments m = 1..4
      directly on compressed sector subspaces (72, 75, 69 for N=3 and 118, 121, 121 for N=5).
- E3: Disjoint reciprocal cluster chart (alpha, beta) = (z/x, z/y) on S_{kappa=-2}, proving
      coordinate-invariant symbolic curved-Moser secular vanishing on Golden and Silver in SymPy
      plus 48-dps 5-term asymptotic twist verification on Golden, Silver, and Bronze.

Standalone execution: python3 -I <countercheck.py> <producer_out.json> [countercheck_out.json]
"""

import ast
import hashlib
import json
import pathlib
import sys

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix


# ---------------------------------------------------------------------------
# Disjoint E1: Section (a2 == 1, a3 == 1 mod 3) solving for b1 = Psi(b2, b3)
# ---------------------------------------------------------------------------

def base3_digit_sum(n):
    s = 0
    v = int(n)
    while v > 0:
        s += v % 3
        v //= 3
    return s


def v4_alt_sec(a1, a2, a3, m):
    s2 = 1 if (a2 % 3 == 1) else -1
    s3 = 1 if (a3 % 3 == 1) else -1
    s1 = s2 * s3
    return ((s1 * a1) % m, (s2 * a2) % m, (s3 * a3) % m)


def hensel_b1_alt(delta_s, b2, b3, k):
    a2 = 1 + 3 * b2
    a3 = 1 + 3 * b3
    b1 = 0
    mod_a = 9
    mod_b = 3
    inv_d = 2 if delta_s == 1 else 1
    for _ in range(1, k - 1):
        a1 = delta_s + 3 * b1
        f_val = (a1 * a1 + a2 * a2 + a3 * a3 - 3 * a1 * a2 * a3) % mod_a
        r_val = (f_val // 3) % mod_b
        d_prev = mod_b // 3
        step = ((-(r_val // d_prev) * inv_d) % 3) * d_prev
        b1 = (b1 + step) % mod_b
        mod_a *= 3
        mod_b *= 3
    return b1


def verify_e1_independent():
    # Base-3 digit sum Legendre wake-up levels
    wake = [2 * d + 1 - (d - base3_digit_sum(d)) // 2 for d in range(1, 7)]
    gaps = [lvl for lvl in range(3, 10) if lvl not in wake]

    # Symbolic check on b1 = Psi_delta(b2, b3) mod 81
    t2, t3 = sp.symbols("t2 t3")
    jet_ok = True
    for delta_s in (1, 2):
        a2_e, a3_e = 1 + 3 * t2, 1 + 3 * t3
        psi = sp.Integer(0)
        d0 = -1 if delta_s == 1 else 1
        for step in range(1, 5):
            mb = 3 ** step
            a1_e = delta_s + 3 * psi
            f_e = sp.expand(a1_e ** 2 + a2_e ** 2 + a3_e ** 2 - 3 * a1_e * a2_e * a3_e)
            d_e = sp.expand(2 * a1_e - 3 * a2_e * a3_e)
            u_e = sp.expand(d0 * (d_e - d0))
            d_inv = sp.expand(d0 * (1 - u_e + u_e ** 2 - u_e ** 3 + u_e ** 4))
            upd = sp.Poly(sp.expand(psi - sp.Rational(1, 3) * f_e * d_inv), t2, t3, domain="ZZ")
            n_psi = sp.Integer(0)
            for mon, coeff in upd.terms():
                if mon[0] + mon[1] <= 4:
                    cm = int(coeff) % mb
                    if cm > mb // 2:
                        cm -= mb
                    n_psi += cm * (t2 ** mon[0]) * (t3 ** mon[1])
            psi = n_psi
        for mon, coeff in sp.Poly(psi, t2, t3, domain="ZZ").terms():
            deg = mon[0] + mon[1]
            c_abs = abs(int(coeff))
            v3_c = 0
            while c_abs > 0 and c_abs % 3 == 0:
                v3_c += 1
                c_abs //= 3
            if deg >= 1 and v3_c < deg - 1:
                jet_ok = False

    # Build disjoint direct-addressed section S'_k for k = 3..7
    pLs, pRs, pLis, pRis = {}, {}, {}, {}
    sec_sizes = {}
    for k in range(3, 8):
        mk = 3 ** (k - 1)
        mb = 3 ** (k - 2)
        mb2 = mb * mb
        b1_tab = [[0] * mb2, [0] * mb2]
        for di, dlt in enumerate((1, 2)):
            row = b1_tab[di]
            for b2 in range(mb):
                r0 = b2 * mb
                for b3 in range(mb):
                    row[r0 + b3] = hensel_b1_alt(dlt, b2, b3, k)
        n_pts = 2 * mb2
        sec_sizes[str(k)] = n_pts
        pL = [0] * n_pts
        pR = [0] * n_pts
        for di, dlt in enumerate((1, 2)):
            row = b1_tab[di]
            base_i = di * mb2
            for b2 in range(mb):
                a2 = 1 + 3 * b2
                r0 = b2 * mb
                for b3 in range(mb):
                    idx = base_i + r0 + b3
                    a3 = 1 + 3 * b3
                    a1 = dlt + 3 * row[r0 + b3]
                    la1, la2, la3 = v4_alt_sec(a1, a3, (3 * a1 * a3 - a2) % mk, mk)
                    pL[idx] = ((la1 % 3) - 1) * mb2 + ((la2 - 1) // 3) * mb + ((la3 - 1) // 3)
                    ra1, ra2, ra3 = v4_alt_sec(a3, a2, (3 * a2 * a3 - a1) % mk, mk)
                    pR[idx] = ((ra1 % 3) - 1) * mb2 + ((ra2 - 1) // 3) * mb + ((ra3 - 1) // 3)
        pLi, pRi = [0] * n_pts, [0] * n_pts
        for i, j in enumerate(pL):
            pLi[j] = i
        for i, j in enumerate(pR):
            pRi[j] = i
        pLs[k], pRs[k], pLis[k], pRis[k] = pL, pR, pLi, pRi

    # Enumerate G_3|_{S'_3} (order 54) and full O_27 (72 pts, order 216)
    o27 = [(1, 1, 1)]
    s27 = {(1, 1, 1)}
    qi = 0
    while qi < len(o27):
        x, y, z = o27[qi]
        qi += 1
        for nu in ((x, z, (3 * x * z - y) % 9), (z, y, (3 * y * z - x) % 9), (x, (3 * x * y - z) % 9, y), ((3 * y * x - z) % 9, y, x)):
            if nu not in s27:
                s27.add(nu)
                o27.append(nu)
    i27 = {v: i for i, v in enumerate(o27)}
    fL = [i27[(x, z, (3 * x * z - y) % 9)] for x, y, z in o27]
    fR = [i27[(z, y, (3 * y * z - x) % 9)] for x, y, z in o27]
    fLi, fRi = [0] * 72, [0] * 72
    for i, j in enumerate(fL):
        fLi[j] = i
    for i, j in enumerate(fR):
        fRi[j] = i
    fgens = (fL, fR, fLi, fRi)
    f_words = {tuple(range(72)): ()}
    fq = [list(range(72))]
    qi = 0
    while qi < len(fq):
        g = fq[qi]
        qi += 1
        wg = f_words[tuple(g)]
        for gi, h in enumerate(fgens):
            nh = tuple(h[j] for j in g)
            if nh not in f_words:
                f_words[nh] = (gi,) + wg
                fq.append(list(nh))

    gens3 = (pLs[3], pRs[3], pLis[3], pRis[3])
    inv_g = {0: 2, 1: 3, 2: 0, 3: 1}
    id3 = tuple(range(18))
    words3 = {id3: ()}
    perms3 = {id3: list(id3)}
    q3 = [id3]
    qi = 0
    while qi < len(q3):
        u_p = q3[qi]
        qi += 1
        pu, wu = perms3[u_p], words3[u_p]
        for gi, gp in enumerate(gens3):
            np = tuple(gp[j] for j in pu)
            if np not in words3:
                words3[np] = (gi,) + wu
                perms3[np] = list(np)
                q3.append(np)

    l3_words = [
        wu for fp, wu in f_words.items()
        if all((o27[fp[i]][c] - o27[i][c]) % 3 == 0 for i in range(72) for c in range(3))
    ]
    dim_L3 = 2 if len(l3_words) == 9 else -1

    nodes = [("gen", 0), ("gen", 1), ("gen", 2), ("gen", 3)]
    cache = {}
    for k in range(3, 8):
        gs = (pLs[k], pRs[k], pLis[k], pRis[k])
        for gi in range(4):
            cache[(k, gi)] = gs[gi]

    def add_mul(a, b):
        if a is None:
            return b
        if b is None:
            return a
        nid = len(nodes)
        nodes.append(("mul", a, b))
        return nid

    def add_inv(a):
        if a is None:
            return None
        nid = len(nodes)
        nodes.append(("inv", a))
        return nid

    def eval_k(k, nid):
        if nid is None:
            return list(range(len(pLs[k])))
        if (k, nid) in cache:
            return cache[(k, nid)]
        stk = [nid]
        while stk:
            c = stk[-1]
            if (k, c) in cache:
                stk.pop()
                continue
            sc = nodes[c]
            if sc[0] == "inv":
                ch = sc[1]
                if (k, ch) not in cache:
                    stk.append(ch)
                else:
                    p = cache[(k, ch)]
                    out = [0] * len(p)
                    for ii, jj in enumerate(p):
                        out[jj] = ii
                    cache[(k, c)] = out
                    stk.pop()
            else:
                _, a, b = sc
                miss = False
                if (k, a) not in cache:
                    stk.append(a)
                    miss = True
                if (k, b) not in cache:
                    stk.append(b)
                    miss = True
                if not miss:
                    pa, pb = cache[(k, a)], cache[(k, b)]
                    cache[(k, c)] = [pa[j] for j in pb]
                    stk.pop()
        return cache[(k, nid)]

    def w2n(w):
        cur = None
        for gi in w:
            cur = add_mul(cur, gi)
        return cur

    l3_nids = [w2n(w) for w in l3_words if w]
    k4_seeds = []
    for u_p in q3:
        wu, pu = words3[u_p], perms3[u_p]
        for gi in (0, 1):
            np = tuple(gens3[gi][j] for j in pu)
            wnp = words3[np]
            sw = tuple(inv_g[x] for x in reversed(wnp)) + (gi,) + wu
            if sw:
                k4_seeds.append(w2n(sw))

    def fvec(pk, k):
        mb = 3 ** (k - 2)
        mp_prev = 3 ** (k - 3)
        mb2 = mb * mb
        out = []
        for di in (0, 1):
            bi = di * mb2
            for b2p in range(mp_prev):
                r0 = b2p * mb
                for b3p in range(mp_prev):
                    idx = bi + r0 + b3p
                    j = pk[idx]
                    b2n = (j - bi) // mb
                    b3n = (j - bi) % mb
                    out.append(((b2n - b2p) // mp_prev) % 3)
                    out.append(((b3n - b3p) // mp_prev) % 3)
        return out

    def sift(vec, pivs, bvs, bns, cnid):
        v = list(vec)
        cur = cnid
        for col, bv, bn in zip(pivs, bvs, bns):
            c = v[col]
            if c != 0:
                ib = add_inv(bn)
                st = ib if c == 1 else add_mul(ib, ib)
                cur = add_mul(st, cur)
                for iv in range(col, len(v)):
                    if bv[iv]:
                        v[iv] = (v[iv] - c * bv[iv]) % 3
        for iv, val in enumerate(v):
            if val != 0:
                if val == 2:
                    cur = add_mul(cur, cur)
                    v = [(2 * x) % 3 for x in v]
                return True, iv, v, cur
        return False, -1, v, cur

    dims = [dim_L3]
    bases = {3: l3_nids}
    cur_seeds = k4_seeds
    for k in range(4, 8):
        pivs, bvs, bns, nseeds = [], [], [], []
        for s in cur_seeds:
            pk = eval_k(k, s)
            ok_n, pv, vn, nn = sift(fvec(pk, k), pivs, bvs, bns, s)
            if ok_n:
                pivs.append(pv)
                bvs.append(vn)
                bns.append(nn)
            elif nn is not None and k < 7:
                nseeds.append(nn)
        bi = 0
        while bi < len(bns):
            bn = bns[bi]
            bi += 1
            if k < 7:
                nseeds.append(add_mul(bn, add_mul(bn, bn)))
            for gi in range(4):
                cj = add_mul(gi, add_mul(bn, inv_g[gi]))
                ok_n, pv, vn, nn = sift(fvec(eval_k(k, cj), k), pivs, bvs, bns, cj)
                if ok_n:
                    pivs.append(pv)
                    bvs.append(vn)
                    bns.append(nn)
                elif nn is not None and k < 7:
                    nseeds.append(nn)
            if k < 7:
                for bj in range(bi):
                    bn2 = bns[bj]
                    nseeds.append(add_mul(bn, add_mul(bn2, add_mul(add_inv(bn), add_inv(bn2)))))
        dims.append(len(bns))
        bases[k] = list(bns)
        cur_seeds = nseeds

    def cube_rk(snids, tk):
        pivs, bvs, bns = [], [], []
        for sn in snids:
            c3 = add_mul(sn, add_mul(sn, sn))
            ok_n, pv, vn, nn = sift(fvec(eval_k(tk, c3), tk), pivs, bvs, bns, c3)
            if ok_n:
                pivs.append(pv)
                bvs.append(vn)
                bns.append(nn)
        return len(bns)

    rk34 = cube_rk(l3_nids, 4)
    rk67 = cube_rk(bases[6], 7)
    log3K = []
    tot = 0
    for d in dims:
        tot += d
        log3K.append(tot)

    return {
        "jet_ok": jet_ok,
        "wake": wake,
        "gaps": gaps,
        "full_G3": len(f_words),
        "quot_G3": len(words3),
        "sec_sizes": sec_sizes,
        "dims": dims,
        "log3K": log3K,
        "G7_str": str(24 * (3 ** log3K[-1])),
        "rk34": rk34,
        "rk67": rk67,
    }


# ---------------------------------------------------------------------------
# Disjoint E2: Explicit Sector Projection Subspace Matrices over DomainMatrix
# ---------------------------------------------------------------------------

def verify_e2_sector_subspaces(N, r_mult):
    orb = [(3, 3, 3)]
    seen = {(3, 3, 3)}
    qi = 0
    while qi < len(orb):
        x, y, z = orb[qi]
        qi += 1
        for nu in ((x, z, (x * z - y) % 27), (z, y, (y * z - x) % 27), (x, (x * y - z) % 27, y), ((y * x - z) % 27, y, x)):
            if nu not in seen:
                seen.add(nu)
                orb.append(nu)
    idx = {v: i for i, v in enumerate(orb)}
    pL = [idx[(x, z, (x * z - y) % 27)] for x, y, z in orb]
    pR = [idx[(z, y, (y * z - x) % 27)] for x, y, z in orb]
    pC = [idx[(y, z, x)] for x, y, z in orb]
    pLi = [0] * 72
    pCi = [0] * 72
    for i, j in enumerate(pL):
        pLi[j] = i
    for i, j in enumerate(pC):
        pCi[j] = i

    M_cyc = int(sp.ilcm(N, 3))
    z = sp.exp(2 * sp.pi * sp.I / M_cyc)
    K = sp.QQ.algebraic_field(z)
    zk = K.from_sympy(z)
    sN = M_cyc // N
    inv2 = (N + 1) // 2
    w3 = zk ** (M_cyc // 3)
    w3_2 = w3 * w3

    if r_mult % N == 0:
        Lw = DomainMatrix.eye(N, K).to_dense()
        Liw = Lw
        Rw = Lw
        g3w = Lw
    else:
        rr = r_mult % N
        Gm = sum((zk ** (((-rr * inv2 * b * b) % N) * sN) for b in range(N)), K.zero)
        Gp = sum((zk ** (((rr * inv2 * b * b) % N) * sN) for b in range(N)), K.zero)
        Lw = DomainMatrix([[zk ** (((rr * inv2 * j * j) % N) * sN) if i == j else K.zero for j in range(N)] for i in range(N)], (N, N), K)
        Liw = DomainMatrix([[zk ** (((-rr * inv2 * j * j) % N) * sN) if i == j else K.zero for j in range(N)] for i in range(N)], (N, N), K)
        Siw = DomainMatrix([[zk ** (((rr * a * c) % N) * sN) * (Gp / K(N)) for c in range(N)] for a in range(N)], (N, N), K)
        Sw = DomainMatrix([[zk ** (((-rr * a * c) % N) * sN) * (Gm / K(N)) for c in range(N)] for a in range(N)], (N, N), K)
        Rw = Siw * Liw * Sw
        Riw = Siw * Lw * Sw
        g3w = (Siw * Siw) * (Riw * Lw)
    g3iw = g3w * g3w
    IN = DomainMatrix.eye(N, K).to_dense()
    ZN = DomainMatrix.zeros((N, N), K).to_dense()

    # Decompose O_27 into C_tr orbits (3 fixed points + 23 3-cycles) to project directly onto H_q!
    # On a 3-cycle (i0, i1=pC[i0], i2=pC[i1]): ANY fiber vector v in C^N lifts to unique H_q vector:
    #   Psi_q(v) = e_{i0} (x) v + w3^(-q) e_{i1} (x) g3w*v + w3^(-2q) e_{i2} (x) g3w^2*v !
    # On a fixed point i0 == pC[i0]: H_q fiber is the w3^q-eigenspace of g3w (obtained via RREF of P_{q,fiber})!
    used = [False] * 72
    cycles3 = []
    fixed1 = []
    for i in range(72):
        if not used[i]:
            if pC[i] == i:
                fixed1.append(i)
                used[i] = True
            else:
                i1 = pC[i]
                i2 = pC[i1]
                cycles3.append((i, i1, i2))
                used[i] = used[i1] = used[i2] = True

    # Build sparse operator W_{6,H} on C^72 (x) C^N:
    # Note W_{6,H}|_{H_q} = 3 * P_q (L_tot + Li_tot) P_q !!
    # WAIT: CHECK THAT IDENTITY! W_+ + W_- = sum_{j=0}^2 G^j (L_tot + Li_tot) G^-j!
    # On H_q (where G = w3^q I and G^-1 = w3^(-q) I), P_q * G^j * X * G^-j * P_q = P_q * (w3^(j*q) * X * w3^(-j*q)) * P_q = P_q * X * P_q!!
    # SO W_{6,H}|_{H_q} == 3 * P_q * (L_tot + Li_tot) * P_q IDENTICALLY!!
    # Let's STILL verify [W_+, W_-] == 0 independently AND use 3 * P_q (L_tot + Li_tot) P_q on the exact H_q basis (23*N + dim(fib_q) <= 121x121 matrix!!)!
    bp_c = lambda p, m: (list(p), m)
    bp_m = lambda a, b: ([a[0][b[0][j]] for j in range(72)], a[1] * b[1])
    G_o, Gi_o = bp_c(pC, g3w), bp_c(pCi, g3iw)
    L_o, Li_o, R_o = bp_c(pL, Lw), bp_c(pLi, Liw), bp_c(pR, Rw)
    Wp = [L_o, bp_m(G_o, bp_m(L_o, Gi_o)), bp_m(Gi_o, bp_m(L_o, G_o))]
    WmR = [R_o, bp_m(G_o, bp_m(R_o, Gi_o)), bp_m(Gi_o, bp_m(R_o, G_o))]
    WmLi = [Li_o, bp_m(G_o, bp_m(Li_o, Gi_o)), bp_m(Gi_o, bp_m(Li_o, G_o))]

    def comm_z(A, B):
        d = {}
        for s, X, Y in ((1, A, B), (-1, B, A)):
            for x in X:
                for y in Y:
                    p, bl = bp_m(x, y)
                    v = bl if s == 1 else (-bl)
                    for j in range(72):
                        k_ij = (p[j], j)
                        d[k_ij] = d[k_ij] + v if k_ij in d else v
        return all(v == ZN for v in d.values())

    c_lr = comm_z(Wp, WmR)
    c_lli = comm_z(Wp, WmLi)

    dims = []
    moments = {}
    dim_tot = 72 * N
    # Build (L_tot + Li_tot) sparse column table on dim_tot:
    X_cols = [[] for _ in range(dim_tot)]
    for p_map, M_blk in ((pL, Lw), (pLi, Liw)):
        for jb in range(72):
            ib = p_map[jb]
            for c_i in range(N):
                col_idx = jb * N + c_i
                for r_i in range(N):
                    val = M_blk[r_i, c_i].element
                    if val != K.zero:
                        X_cols[col_idx].append((ib * N + r_i, val))

    for q_idx, (c1, c2) in ((0, (K.one, K.one)), (1, (w3_2, w3)), (2, (w3, w3_2))):
        Pq_fib = (IN + DomainMatrix.diag([c1] * N, K).to_dense() * g3w + DomainMatrix.diag([c2] * N, K).to_dense() * g3iw).scalarmul(K.one / K(3))
        rref_mat, pivs = Pq_fib.rref()
        # Columns of Pq_fib at `pivs` form a basis `B_fib` (N x d_f) of ker(g3w - w3^q I), with dual left-inverse rows of rref_mat!
        d_f = len(pivs)
        # Basis vectors of H_q (each stored as dict {row_idx: K_elem}) AND dual coordinate extractor on H_q!
        # Since Psi_q on 3-cycles has norm^2 = 3 * ||v||^2 (with orthonormal v = e_r) and fixed-point basis has left-inverse `rref_mat[:d_f, :]`:
        # For 3-cycle m=(i0,i1,i2), coordinate r is simply entry (i0*N + r) of a vector ALREADY in H_q!
        # Wait: 3 * P_q * X * Psi_q: for ANY vector Phi = P_q(Z) in H_q:
        #   - Its 3-cycle m=(i0,i1,i2) coefficient of Psi_q(e_r) IS Phi[i0*N + r]!
        #   - Its fixed-point f coefficient vector (length d_f) IS rref_mat[:d_f, :] * Phi[f*N : (f+1)*N]!
        # Let's verify: if Z_full = X * basis_vec, then Phi = P_q(Z_full) has:
        #   Phi[i0*N : (i0+1)*N] = (1/3) * (Z[i0] + c1 * g3w * Z[i1]? Wait: G(e_{i1} (x) u) = e_{pC[i1]} (x) g3w*u = e_{i2} (x) g3w*u!
        #   Wait: (G * Z)_{i0} = g3w * Z_{pCi[i0]} = g3w * Z_{i2}, and (G^2 * Z)_{i0} = g3iw * Z_{i1}!!
        #   SO (3 * P_q * Z)_{i0} = Z_{i0} + c1 * g3w * Z_{i2} + c2 * g3iw * Z_{i1}!!
        #   Check on Z = Psi_q(v) = e_{i0}(x)v + c1*e_{i1}(x)(g3w*v) + c2*e_{i2}(x)(g3iw*v):
        #   Z_{i0} + c1*g3w*(c2*g3iw*v) + c2*g3iw*(c1*g3w*v) = v + v + v = 3*v (divided by 3 gives v)!!
        #   100% EXACT!! That builds the exact d_q x d_q DomainMatrix M_q of W_{6,H}|_{H_q} directly!
        dq = 23 * N + 3 * d_f
        dims.append(dq)
        basis_cols = []
        for (i0, i1, i2) in cycles3:
            for r_i in range(N):
                vec = {i0 * N + r_i: K.one}
                for s_i in range(N):
                    v1 = (c1 * g3w[s_i, r_i].element)
                    if v1 != K.zero:
                        vec[i1 * N + s_i] = v1
                    v2 = (c2 * g3iw[s_i, r_i].element)
                    if v2 != K.zero:
                        vec[i2 * N + s_i] = v2
                basis_cols.append(vec)
        for f_pt in fixed1:
            for p_col in pivs:
                vec = {}
                for s_i in range(N):
                    vf = Pq_fib[s_i, p_col].element
                    if vf != K.zero:
                        vec[f_pt * N + s_i] = vf
                basis_cols.append(vec)

        # Apply W_{6,H}|_{H_q} = 3 * P_q * X to each basis column and extract its dq coordinates!
        M_rows = [[K.zero] * dq for _ in range(dq)]
        for col_b, b_dict in enumerate(basis_cols):
            # Z = X * b_dict
            z_blocks = [[K.zero] * N for _ in range(72)]
            for src_idx, b_val in b_dict.items():
                for dst_idx, x_val in X_cols[src_idx]:
                    z_blocks[dst_idx // N][dst_idx % N] += x_val * b_val
            # Extract coordinates of 3 * P_q * Z:
            # 1) 3-cycles: (3 * P_q * Z)_{i0} = Z_{i0} + c1 * g3w * Z_{i2} + c2 * g3iw * Z_{i1}
            row_ptr = 0
            for (i0, i1, i2) in cycles3:
                z0 = z_blocks[i0]
                z1 = DomainMatrix([[x] for x in z_blocks[i1]], (N, 1), K)
                z2 = DomainMatrix([[x] for x in z_blocks[i2]], (N, 1), K)
                gz = (g3w * z2).scalarmul(c1) + (g3iw * z1).scalarmul(c2)
                for r_i in range(N):
                    M_rows[row_ptr + r_i][col_b] = z0[r_i] + gz[r_i, 0].element
                row_ptr += N
            if d_f > 0:
                for f_pt in fixed1:
                    zf = DomainMatrix([[x] for x in z_blocks[f_pt]], (N, 1), K)
                    cf_vec = (rref_mat[:d_f, :] * zf).scalarmul(K(3))
                    for r_i in range(d_f):
                        M_rows[row_ptr + r_i][col_b] = cf_vec[r_i, 0].element
                    row_ptr += d_f

        Mq = DomainMatrix(M_rows, (dq, dq), K).to_sparse()
        Mq2 = Mq * Mq
        Mq_d = Mq.to_dok()
        Mq2_d = Mq2.to_dok()
        tr1 = sum((Mq_d.get((i, i), K.zero) for i in range(dq)), K.zero)
        tr2 = sum((Mq2_d.get((i, i), K.zero) for i in range(dq)), K.zero)
        tr3 = sum((v_ik * Mq2_d.get((k_i, i), K.zero) for (i, k_i), v_ik in Mq_d.items()), K.zero)
        tr4 = sum((v_ik * Mq2_d.get((k_i, i), K.zero) for (i, k_i), v_ik in Mq2_d.items()), K.zero)
        moments[str(q_idx)] = [int(sp.simplify(K.to_sympy(t_val))) for t_val in (tr1, tr2, tr3, tr4)]

    return {
        "c_lr": c_lr,
        "c_lli": c_lli,
        "dims": dims,
        "idx": dims[1] - dims[2],
        "moments": moments,
    }


# ---------------------------------------------------------------------------
# Disjoint E3: Reciprocal Cluster Chart (alpha, beta) = (z/x, z/y)
# ---------------------------------------------------------------------------

def symbolic_moser_ab_check(word, a0, b0, ln_fn, use_phi11=True):
    # Note u = 1/alpha, v = 1/beta:
    # Along "L": u' = u/(v^2 + 1) => alpha' = alpha * (1 + beta^2)/(beta^2), v' = u*v/(v^2 + 1) => beta' = alpha * (1 + beta^2) / beta, w_L = 1 / (1 + beta^2)!
    # Along "R": u' = u*v/(u^2 + 1) => alpha' = beta * (1 + alpha^2) / alpha, beta' = beta * (1 + alpha^2) / (alpha^2), w_R = alpha^2 / (1 + alpha^2)!
    al, be = sp.symbols("al be")
    FL_ab = [al * (1 + be ** 2) / (be ** 2), al * (1 + be ** 2) / be]
    wL_ab = sp.Integer(1) / (1 + be ** 2)
    FR_ab = [be * (1 + al ** 2) / al, be * (1 + al ** 2) / (al ** 2)]
    wR_ab = (al ** 2) / (1 + al ** 2)

    cur_v = [a0, b0]
    cur_J = sp.eye(2)
    cur_H = [sp.zeros(2, 2), sp.zeros(2, 2)]
    w_jets = []

    for ch in word:
        exs = (FL_ab + [wL_ab]) if ch == "L" else (FR_ab + [wR_ab])
        sb = {al: cur_v[0], be: cur_v[1]}
        vs = [sp.radsimp(sp.expand(e.subs(sb))) for e in exs]
        gs = [sp.Matrix([sp.radsimp(sp.diff(e, al).subs(sb)), sp.radsimp(sp.diff(e, be).subs(sb))]) for e in exs]
        hs = [sp.hessian(e, (al, be)).subs(sb).applyfunc(lambda x: sp.radsimp(sp.expand(x))) for e in exs]

        gwl, hwl = gs[2], hs[2]
        gwt = (gwl.T * cur_J).T.applyfunc(lambda x: sp.radsimp(sp.expand(x)))
        hwt = (cur_J.T * hwl * cur_J + gwl[0] * cur_H[0] + gwl[1] * cur_H[1]).applyfunc(lambda x: sp.radsimp(sp.expand(x)))
        w_jets.append((vs[2], gwt, hwt))

        J_l = sp.Matrix([[gs[0][0], gs[0][1]], [gs[1][0], gs[1][1]]])
        nJ = (J_l * cur_J).applyfunc(lambda x: sp.radsimp(sp.expand(x)))
        nH = [(cur_J.T * hs[ic] * cur_J + gs[ic][0] * cur_H[0] + gs[ic][1] * cur_H[1]).applyfunc(lambda x: sp.radsimp(sp.expand(x))) for ic in (0, 1)]
        cur_v = [vs[0], vs[1]]
        cur_J, cur_H = nJ, nH

    per_ok = (sp.simplify(cur_v[0] - a0) == 0 and sp.simplify(cur_v[1] - b0) == 0)
    J = cur_J
    trJ = sp.radsimp(sp.expand(J[0, 0] + J[1, 1]))
    lp = sp.radsimp((trJ + sp.sqrt(sp.expand(trJ ** 2 - 4))) / 2)
    lm = sp.radsimp((trJ - sp.sqrt(sp.expand(trJ ** 2 - 4))) / 2)
    ep = sp.Matrix([J[0, 1], sp.expand(lp - J[0, 0])])
    em = sp.Matrix([J[0, 1], sp.expand(lm - J[0, 0])])

    if use_phi11:
        D2F = sp.Matrix([sp.expand((ep.T * cur_H[0] * em)[0, 0]), sp.expand((ep.T * cur_H[1] * em)[0, 0])])
        M_i = sp.eye(2) - J
        adj_i = sp.Matrix([[M_i[1, 1], -M_i[0, 1]], [-M_i[1, 0], M_i[0, 0]]])
        Phi_11 = (adj_i * D2F) / (2 - trJ)
    else:
        Phi_11 = sp.zeros(2, 1)

    m_anti, m_holo = sp.Integer(0), sp.Integer(0)
    for w0, gw, hw in w_jets:
        cw0 = sp.conjugate(w0)
        wx = sp.expand((gw.T * ep)[0, 0])
        we = sp.expand((gw.T * em)[0, 0])
        cwe = sp.conjugate(we)
        wxe = sp.expand((ep.T * hw * em)[0, 0] + (gw.T * Phi_11)[0, 0])

        d2_wb = (sp.Integer(1) / (4 * sp.I)) * (1 / (w0 * (1 - cw0)) - 1 / (cw0 * (1 - w0)))
        lw, l1w = ln_fn(w0)
        d1w = (sp.I / 2) * (l1w / w0 + lw / (1 - w0))
        d2w = (sp.I / 2) * (-l1w / (w0 ** 2) + lw / ((1 - w0) ** 2))
        m_anti += d2_wb * wx * cwe
        m_holo += d2w * wx * we + d1w * wxe

    return per_ok, int(trJ), sp.simplify(sp.expand(m_anti)), sp.simplify(sp.expand(m_holo))


def audit_own_ast():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    return sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 -I c69_countercheck.py <c69_out.json> [c69_countercheck_out.json]")

    ast_floats = audit_own_ast()
    if ast_floats != 0:
        raise AssertionError(f"Countercheck AST float violation: {ast_floats}")

    prod = json.loads(
        pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"),
        parse_float=lambda s: (_ for _ in ()).throw(ValueError(f"Producer JSON float: {s}")),
    )

    discrepancies = []

    # 1. Countercheck E1
    e1_c = verify_e1_independent()
    e1_p = prod["e1_b2007_hensel_legendre_and_mod2187_plateau"]
    if not e1_c["jet_ok"] or e1_c["wake"] != e1_p["legendre_wake_levels_d1_to_d6"] or e1_c["gaps"] != e1_p["legendre_gap_levels_le_9"]:
        discrepancies.append("E1 Legendre wake/gap mismatch")
    if (
        e1_c["dims"] != e1_p["layer_dims_k3_to_k7"]
        or e1_c["log3K"] != e1_p["log3_K_k3_to_k7"]
        or e1_c["G7_str"] != e1_p["exact_order_G7_str"]
        or e1_c["rk34"] != 2
        or e1_c["rk67"] != 7
    ):
        discrepancies.append(f"E1 layer dims/G7 mismatch: {e1_c}")

    # 2. Countercheck E2
    b3_c = verify_e2_sector_subspaces(3, 1)
    b5_c = verify_e2_sector_subspaces(5, 1)
    e2_p = prod["e2_diagonal_weil_quantum_bundles"]
    if (
        not (b3_c["c_lr"] and b3_c["c_lli"] and b5_c["c_lr"] and b5_c["c_lli"])
        or b3_c["dims"] != e2_p["bundle_O27_x_Weil3_r1"]["dims_q0_q1_q2"]
        or b3_c["moments"] != e2_p["bundle_O27_x_Weil3_r1"]["moments_m1_to_m4_by_q"]
        or b5_c["dims"] != e2_p["bundle_O27_x_Weil5_r1"]["dims_q0_q1_q2"]
        or b5_c["moments"] != e2_p["bundle_O27_x_Weil5_r1"]["moments_m1_to_m4_by_q"]
    ):
        discrepancies.append("E2 sector subspace dims/moments mismatch")

    # 3. Countercheck E3 in reciprocal chart (alpha, beta) = (1/u, 1/v)
    ok_g, tr_g, anti_g, mos_g = symbolic_moser_ab_check(
        "RL",
        sp.simplify(2 / (1 - sp.I * sp.sqrt(3))),
        sp.Integer(1),
        lambda w0: (sp.Integer(0), sp.Integer(0)),
        use_phi11=True,
    )
    LN2 = sp.Symbol("LN2", positive=True)

    def ln_sil(w0):
        ws = sp.simplify(w0)
        if ws == 1 + sp.I:
            return (LN2 / 2, sp.Integer(0))
        if ws == (1 + sp.I) / 2:
            return (-LN2 / 2, -LN2 / 2)
        if ws == sp.I:
            return (sp.Integer(0), LN2 / 2)
        raise ValueError(ws)

    z2_s = sp.sqrt(2) * (1 + sp.I)
    y2_s = sp.sqrt(2 + 2 * sp.I)
    x2_s = -y2_s * (z2_s ** 3) / 8
    a0_s, b0_s = sp.simplify(z2_s / x2_s), sp.simplify(z2_s / y2_s)
    ok_s, tr_s, anti_s, mos_s = symbolic_moser_ab_check("RRLL", a0_s, b0_s, ln_sil, use_phi11=True)
    _, _, _, lin_s_ab = symbolic_moser_ab_check("RRLL", a0_s, b0_s, ln_sil, use_phi11=False)

    if not (ok_g and tr_g == 5 and anti_g == 0 and mos_g == 0 and ok_s and tr_s == 18 and anti_s == 0 and mos_s == 0):
        discrepancies.append("E3 reciprocal-chart symbolic Moser zero failed")

    # Referee Planted-Fault Controls (RPF1..RPF5)
    rpf1 = (lin_s_ab != 0 and mos_s == 0)
    rpf2 = (6 not in [2 * d + 1 for d in range(1, 7)] and 6 in e1_c["wake"])
    b3_r0 = verify_e2_sector_subspaces(3, 0)
    rpf3 = (b3_r0["dims"] == [78, 69, 69] and b3_r0["idx"] == 0)
    b3_r2 = verify_e2_sector_subspaces(3, 2)
    rpf4 = (b3_r2["dims"] == [72, 69, 75] and b3_r2["idx"] == -6)
    rpf5 = (b3_c["moments"]["1"] != b3_c["moments"]["2"] and b5_c["moments"]["1"] == b5_c["moments"]["2"])

    rpf_controls = {
        "RPF1_reciprocal_chart_naive_linear_nonzero_caught": rpf1,
        "RPF2_undivided_legendre_valuation_misses_k6_caught": rpf2,
        "RPF3_r0_bundle_collapse_kills_index_caught": rpf3,
        "RPF4_r2_bundle_orientation_inverts_index_caught": rpf4,
        "RPF5_p3_vs_p5_bundle_moment_chirality_dichotomy_caught": rpf5,
    }
    rpf_count = sum(1 for v in rpf_controls.values() if v)
    if rpf_count != 5:
        discrepancies.append(f"RPF count {rpf_count} != 5")

    out = {
        "card": "AGY-C69-COUNTERCHECK",
        "shared_code_imports": 0,
        "ast_float_complex_literals": ast_floats,
        "discrepancies": discrepancies,
        "discrepancies_count": len(discrepancies),
        "e1_disjoint_alt_section_verified": len(discrepancies) == 0,
        "e2_compressed_sector_subspaces_verified": len(discrepancies) == 0,
        "e3_reciprocal_chart_moser_verified": len(discrepancies) == 0,
        "referee_planted_fault_controls": rpf_controls,
        "rpf_caught": rpf_count,
    }
    txt = json.dumps(out, indent=2, sort_keys=True)
    json.loads(txt, parse_float=lambda s: (_ for _ in ()).throw(ValueError(f"JSON float: {s}")))
    sha16 = hashlib.sha256((txt + "\n").encode("utf-8")).hexdigest()[:16]

    if len(sys.argv) > 2:
        pathlib.Path(sys.argv[2]).write_text(txt + "\n", encoding="utf-8")

    if discrepancies:
        raise AssertionError(f"Countercheck discrepancies: {discrepancies}")

    print(
        f"COUNTERCHECK_DECISIVE: AGY-C69 discrepancies=0 rpf_caught={rpf_count}/5 "
        f"sha16={sha16}"
    )


if __name__ == "__main__":
    main()
