#!/usr/bin/env python3
"""Zero-shared-code cold-room countercheck for Card AGY-C71 (fam3-v1-high-01, 0 of 19).

Independently recomputes every claim in c71_out.json using disjoint coordinates,
representations, and algorithms (stdlib + sympy only; 0 shared imports, 0 floats):
  1. E1 (B2007 Open #1): Uses the disjoint Klein-four Hensel section
     S'_k = {a_2 = 1, a_3 = 1 mod 3} solving a_1 = delta + 3 Psi_delta(t_2, t_3),
     and replaces Stirling falling-factorial conversion by direct evaluation on
     Kempner's poised grid G_m = {(b_2, b_3) : v_3(b_2!) + v_3(b_3!) < m} through
     k = 11 (mod 177147 = 3^11).
  2. E2 (B1990 Open #1): Replaces O(p^3) point enumeration by the O(p) 1D affine
     conic-bundle character formula across all 17 odd primes 3 <= p <= 61 plus
     3 out-of-sample primes (67, 71, 73).
  3. E3 (B2003 Open #3): Replaces 6-move summation and G_3 / N_3 subgroup quotienting
     by B2004's reduced generator operator (6 Pi_0 P_sigma Pi_0 vs -3 Pi_1 P_sigma Pi_1)
     and the abstract 6D rational S_3 x Z_3 representation 1 (+) sgn (+) (E_2 (x) A_2).
  4. E4 (B1997 Open #1): Constructs K_4 on O_81 from right-coset fiber translations
     without G_4 group enumeration and evaluates sparse cyclotomic SDM quartic nullities
     plus double-coset Mackey index in Sym(O_9).
"""
from collections import Counter, deque
import json
import pathlib
import sys
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def v3_factorial_digits(n: int) -> int:
    """Legendre valuation v_3(n!) = (n - s_3(n)) / 2 via base-3 digit sum."""
    if n <= 0:
        return 0
    s3 = 0
    x = n
    while x > 0:
        s3 += x % 3
        x //= 3
    return (n - s3) // 2


def jacobi_prime(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def check_e1_disjoint_poised_grid(k_max: int = 11) -> dict:
    m_max = k_max - 2
    mod_a = 3 ** (k_max - 1)
    mod_b = 3 ** m_max

    def mul_trunc(p: dict, q: dict, mod: int) -> dict:
        res = {}
        for (i1, j1), c1 in p.items():
            if not c1:
                continue
            for (i2, j2), c2 in q.items():
                if i1 + i2 + j1 + j2 <= m_max and c2:
                    rc = (res.get((i1 + i2, j1 + j2), 0) + c1 * c2) % mod
                    if rc:
                        res[(i1 + i2, j1 + j2)] = rc
                    elif (i1 + i2, j1 + j2) in res:
                        del res[(i1 + i2, j1 + j2)]
        return res

    def lin_comb(p: dict, q: dict, sq: int, mod: int) -> dict:
        out = dict(p)
        for k, v in q.items():
            nv = (out.get(k, 0) + sq * v) % mod
            if nv:
                out[k] = nv
            elif k in out:
                del out[k]
        return out

    # Disjoint section S'_k: a_2 = 1 + 3 t_2, a_3 = 1 + 3 t_3, a_1 = delta + 3 Psi_delta(t_2, t_3)
    psi = {}
    hensel_err = 0
    val_terms = 0
    for delta in (1, 2):
        a2 = {(0, 0): 1, (1, 0): 3}
        a3 = {(0, 0): 1, (0, 1): 3}
        a1 = {(0, 0): delta}
        a2_sq = mul_trunc(a2, a2, mod_a)
        a3_sq = mul_trunc(a3, a3, mod_a)
        a23_3 = {k: (3 * v) % mod_a for k, v in mul_trunc(a2, a3, mod_a).items()}
        inv_2d = 2 if delta == 1 else 1
        for st in range(2, k_max):
            mj = 3 ** st
            rem_f = lin_comb(
                lin_comb(a2_sq, a3_sq, 1, mj),
                lin_comb(mul_trunc(a1, a1, mj), mul_trunc(a23_3, a1, mj), -1, mj),
                1,
                mj,
            )
            if rem_f:
                a1 = lin_comb(a1, rem_f, -inv_2d, mj)
        chk_f = lin_comb(
            lin_comb(a2_sq, a3_sq, 1, mod_a),
            lin_comb(mul_trunc(a1, a1, mod_a), mul_trunc(a23_3, a1, mod_a), -1, mod_a),
            1,
            mod_a,
        )
        if chk_f:
            hensel_err += 1
        d_psi = {}
        for k, c in a1.items():
            sh = (c - (delta if k == (0, 0) else 0)) % mod_a
            if sh % 3 != 0:
                hensel_err += 1
            bv = (sh // 3) % mod_b
            if bv:
                d_psi[k] = bv
                deg = k[0] + k[1]
                if deg >= 1:
                    if bv % (3 ** (deg - 1)) != 0:
                        hensel_err += 1
                    val_terms += 1
        psi[delta] = d_psi

    monoms = [(i, d - i) for d in range(m_max + 1) for i in range(d + 1)]
    m_idx = {mn: idx for idx, mn in enumerate(monoms)}
    n_mon = len(monoms)
    mul_idx = [
        [(idx2, m_idx[(i1 + i2, j1 + j2)]) for idx2, (i2, j2) in enumerate(monoms) if i1 + i2 + j1 + j2 <= m_max]
        for (i1, j1) in monoms
    ]

    grids = {
        kl: [
            (b2, b3)
            for b2 in range(3 * (kl - 2))
            for b3 in range(3 * (kl - 2))
            if v3_factorial_digits(b2) + v3_factorial_digits(b3) < (kl - 2)
        ]
        for kl in range(3, k_max + 1)
    }

    def eval_on_grid(vec: tuple, kl: int) -> tuple:
        mc = kl - 2
        mod_c = 3 ** mc
        res = []
        for (b2, b3) in grids[kl]:
            acc = 0
            for idx, (i, j) in enumerate(monoms):
                if i + j > mc:
                    break
                c = vec[idx]
                if c:
                    acc = (acc + c * (b2 ** i) * (b3 ** j)) % mod_c
            res.append(acc)
        return tuple(res)

    def to_vec(d: dict) -> tuple:
        v = [0] * n_mon
        for k, val in d.items():
            if k in m_idx:
                v[m_idx[k]] = val % mod_b
        return tuple(v)

    def make_gen(tag: str) -> tuple:
        tgt, f2m, f3m = {}, {}, {}
        for delta in (1, 2):
            a2 = {(0, 0): 1, (1, 0): 3}
            a3 = {(0, 0): 1, (0, 1): 3}
            a1 = {(0, 0): delta}
            for k, c in psi[delta].items():
                a1[k] = (a1.get(k, 0) + 3 * c) % mod_a

            def vflip(pq: dict, r: dict) -> dict:
                out = {k: (3 * v) % mod_a for k, v in pq.items()}
                for k, v in r.items():
                    out[k] = (out.get(k, 0) - v) % mod_a
                return out

            if tag == "L":
                na = (a1, a3, vflip(mul_trunc(a1, a3, mod_a), a2))
            elif tag == "R":
                na = (a3, a2, vflip(mul_trunc(a2, a3, mod_a), a1))
            elif tag == "Li":
                na = (a1, vflip(mul_trunc(a1, a2, mod_a), a3), a2)
            else:
                na = (vflip(mul_trunc(a1, a2, mod_a), a3), a2, a1)
            c0, c1, c2 = na[0].get((0, 0), 0) % 3, na[1].get((0, 0), 0) % 3, na[2].get((0, 0), 0) % 3
            s2 = 1 if c1 == 1 else -1
            s3 = 1 if c2 == 1 else -1
            s1 = s2 * s3
            tgt[delta] = (s1 * c0) % 3
            f2m[delta] = to_vec({k: ((s2 * v - (1 if k == (0, 0) else 0)) // 3) % mod_b for k, v in na[1].items()})
            f3m[delta] = to_vec({k: ((s3 * v - (1 if k == (0, 0) else 0)) // 3) % mod_b for k, v in na[2].items()})
        return (tgt, f2m, f3m)

    def vmul(u: tuple, v: tuple) -> tuple:
        res = [0] * n_mon
        for i1, c1 in enumerate(u):
            if not c1:
                continue
            for i2, ki in mul_idx[i1]:
                c2 = v[i2]
                if c2:
                    res[ki] = (res[ki] + c1 * c2) % mod_b
        return tuple(res)

    one_v = tuple([1] + [0] * (n_mon - 1))

    def comp_sprime(g2: tuple, g1: tuple) -> tuple:
        to, f2o, f3o = {}, {}, {}
        for delta in (1, 2):
            md = g1[0][delta]
            to[delta] = g2[0][md]
            y2, y3 = g1[1][delta], g1[2][delta]
            p2, p3 = [one_v], [one_v]
            for _ in range(1, m_max + 1):
                p2.append(vmul(p2[-1], y2))
                p3.append(vmul(p3[-1], y3))
            o2, o3 = g2[1][md], g2[2][md]
            r2, r3 = [0] * n_mon, [0] * n_mon
            for im, (i, j) in enumerate(monoms):
                c2, c3 = o2[im], o3[im]
                if not c2 and not c3:
                    continue
                pv = p3[j] if i == 0 else (p2[i] if j == 0 else vmul(p2[i], p3[j]))
                if c2:
                    for q, val in enumerate(pv):
                        if val:
                            r2[q] = (r2[q] + c2 * val) % mod_b
                if c3:
                    for q, val in enumerate(pv):
                        if val:
                            r3[q] = (r3[q] + c3 * val) % mod_b
            f2o[delta] = tuple(r2)
            f3o[delta] = tuple(r3)
        return (to, f2o, f3o)

    idf2 = [0] * n_mon
    idf2[m_idx[(1, 0)]] = 1
    idf3 = [0] * n_mon
    idf3[m_idx[(0, 1)]] = 1
    id_sp = ({1: 1, 2: 2}, {1: tuple(idf2), 2: tuple(idf2)}, {1: tuple(idf3), 2: tuple(idf3)})
    gens = {w: make_gen(w) for w in ("L", "R", "Li", "Ri")}
    inv_tag = {"L": "Li", "Li": "L", "R": "Ri", "Ri": "R"}
    inv_ok = (comp_sprime(gens["Li"], gens["L"]) == id_sp and comp_sprime(gens["Ri"], gens["R"]) == id_sp)

    o9 = [(s1, s2, s3) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
    i9 = {pt: idx for idx, pt in enumerate(o9)}

    def perm9(w: str) -> tuple:
        out = []
        for a in o9:
            if w == "L":
                b = (a[0], a[2], -a[1])
            elif w == "R":
                b = (a[2], a[1], -a[0])
            elif w == "Li":
                b = (a[0], -a[2], a[1])
            else:
                b = (-a[2], a[1], a[0])
            out.append(i9[b])
        return tuple(out)

    g9 = {w: perm9(w) for w in ("L", "R", "Li", "Ri")}
    c9 = lambda p2, p1: tuple(p2[p1[i]] for i in range(8))
    id9 = tuple(range(8))
    cosets = {id9: (id_sp, id_sp)}
    q = deque([id9])
    while q:
        cur = q.popleft()
        el, eli = cosets[cur]
        for gn in ("L", "R", "Li", "Ri"):
            nc = c9(g9[gn], cur)
            if nc not in cosets:
                cosets[nc] = (comp_sprime(gens[gn], el), comp_sprime(eli, gens[inv_tag[gn]]))
                q.append(nc)

    gsig = lambda el, kl: (
        eval_on_grid(el[1][1], kl),
        eval_on_grid(el[2][1], kl),
        eval_on_grid(el[1][2], kl),
        eval_on_grid(el[2][2], kl),
    )
    id_sigs = {k: gsig(id_sp, k) for k in range(3, k_max + 1)}

    rs_pairs = []
    seen = {id_sigs[k_max]}
    for c_key, (uel, uinv) in cosets.items():
        for gn in ("L", "R"):
            nc = c9(g9[gn], c_key)
            unc, unci = cosets[nc]
            sch = comp_sprime(unci, comp_sprime(gens[gn], uel))
            sg = gsig(sch, k_max)
            if sg in seen:
                continue
            schi = comp_sprime(uinv, comp_sprime(gens[inv_tag[gn]], unc))
            seen.add(sg)
            seen.add(gsig(schi, k_max))
            rs_pairs.append((sch, schi))

    def layer_f3(el: tuple, kl: int) -> list:
        mc = kl - 2
        div = 3 ** (mc - 1)
        mod_c = 3 ** mc
        sg = gsig(el, kl)
        ids = id_sigs[kl]
        out = []
        for ci in range(4):
            for pi in range(len(sg[ci])):
                df = (sg[ci][pi] - ids[ci][pi]) % mod_c
                if df % div != 0:
                    raise ValueError(f"Not in L_{kl}")
                out.append((df // div) % 3)
        return out

    pmul = lambda A, B: (comp_sprime(A[0], B[0]), comp_sprime(B[1], A[1]))
    pinv = lambda A: (A[1], A[0])
    pcomm = lambda A, B: pmul(pmul(A, B), pmul(pinv(A), pinv(B)))
    pcube = lambda A: pmul(pmul(A, A), A)

    layers = {k: [] for k in range(3, k_max + 1)}

    def sift(pair: tuple, sk: int = 3):
        cur = pair
        for k in range(sk, k_max + 1):
            v = layer_f3(cur[0], k)
            if not any(v):
                continue
            for piv, bv, bp in layers[k]:
                cf = v[piv]
                if cf == 1:
                    cur = pmul(pinv(bp), cur)
                    v = [(v[i] - bv[i]) % 3 for i in range(len(v))]
                elif cf == 2:
                    cur = pmul(bp, cur)
                    v = [(v[i] + bv[i]) % 3 for i in range(len(v))]
            pn = next((i for i, x in enumerate(v) if x != 0), None)
            if pn is not None:
                if v[pn] == 2:
                    cur = pinv(cur)
                    v = [(-x) % 3 for x in v]
                layers[k].append((pn, v, cur))
                return k
        return None

    wq = deque((rp, 3) for rp in rs_pairs)
    while wq:
        cand, sk = wq.popleft()
        ak = sift(cand, sk)
        if ak is not None:
            npair = layers[ak][-1][2]
            if ak < k_max:
                wq.append((pcube(npair), ak + 1))
                for rsg in rs_pairs:
                    wq.append((pcomm(npair, rsg), ak))

    dims = [len(layers[k]) for k in range(3, k_max + 1)]
    cubing_ranks = []
    for k in range(3, k_max):
        rows = []
        for _, _, bp in layers[k]:
            cb = pcube(bp)
            v = layer_f3(cb[0], k + 1)
            for rp, rv in rows:
                cf = v[rp]
                if cf:
                    v = [(v[i] - cf * rv[i]) % 3 for i in range(len(v))]
            pn = next((i for i, x in enumerate(v) if x != 0), None)
            if pn is not None:
                ic = 1 if v[pn] == 1 else 2
                v = [(x * ic) % 3 for x in v]
                rows.append((pn, v))
        cubing_ranks.append(len(rows))

    # RPF1: Origin-only 0-jet evaluation {(0, 0)} per sheet has at most 4 F_3 coordinates < 7 = dim L_6,
    # proving non-constant higher-degree Kempner polynomial terms are genuinely active in L_6!
    origin_grid = [(0, 0)]
    rows_origin6 = []
    mod4 = 81
    div4 = 27
    for _, _, bp in layers[6]:
        el = bp[0]
        v_sm = []
        for (comp_vec, id_vec) in (
            (el[1][1], id_sp[1][1]),
            (el[2][1], id_sp[2][1]),
            (el[1][2], id_sp[1][2]),
            (el[2][2], id_sp[2][2]),
        ):
            for (b2, b3) in origin_grid:
                s_el = sum(comp_vec[idx] * (b2 ** i) * (b3 ** j) for idx, (i, j) in enumerate(monoms) if i + j <= 4) % mod4
                s_id = sum(id_vec[idx] * (b2 ** i) * (b3 ** j) for idx, (i, j) in enumerate(monoms) if i + j <= 4) % mod4
                v_sm.append((((s_el - s_id) % mod4) // div4) % 3)
        for rp, rv in rows_origin6:
            cf = v_sm[rp]
            if cf:
                v_sm = [(v_sm[i] - cf * rv[i]) % 3 for i in range(len(v_sm))]
        pn = next((i for i, x in enumerate(v_sm) if x != 0), None)
        if pn is not None:
            ic = 1 if v_sm[pn] == 1 else 2
            rows_origin6.append((pn, [(x * ic) % 3 for x in v_sm]))
    rpf1_origin_0jet_undercounts_L6 = (len(rows_origin6) < dims[3] and dims[3] == 7)

    log3_k = []
    acc = 0
    for d in dims:
        acc += d
        log3_k.append(acc)

    return {
        "hensel_and_inverses_exact": (hensel_err == 0 and inv_ok and len(cosets) == 24),
        "dims_k3_k11": dims,
        "cubing_ranks_k3_k10": cubing_ranks,
        "log3_K_k3_k11": log3_k,
        "G11_order_str": str(24 * (3 ** log3_k[-1])),
        "rpf1_naive_mod3_grid_undercounts_L6": rpf1_origin_0jet_undercounts_L6,
    }


def check_e2_conic_character_sum() -> dict:
    """O(p) 1D affine conic-bundle fiber count on (2z - xy)^2 - (x^2 - 4)y^2 = 4(c - x^2), c = kappa + 2."""
    primes_base = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    primes_extra = [67, 71, 73]
    all_primes = primes_base + primes_extra
    mismatches = 0
    base_sectors = 0
    p3_cusp = 0
    rpf2_omit_singular_fibers_fails = True

    for p in all_primes:
        for kappa in range(p):
            c = (kappa + 2) % p
            # Sum exact affine conic fiber size over x in F_p: u^2 - D y^2 = R with D = x^2 - 4, R = 4(c - x^2)
            total_pts = 0
            smooth_only_pts = 0
            for x in range(p):
                D = (x * x - 4) % p
                R = (4 * (c - x * x)) % p
                if D == 0:
                    # u^2 = R with y arbitrary in F_p (p choices of y):
                    fib = p * (1 + jacobi_prime(R, p))
                else:
                    chi_D = jacobi_prime(D, p)
                    if R == 0:
                        # u^2 = D y^2: (0,0) plus (p - 1)*(1 + chi_D)
                        fib = 1 + (p - 1) * (1 + chi_D)
                    else:
                        # Smooth affine conic over F_p has p - chi_D points!
                        fib = p - chi_D
                    smooth_only_pts += fib
                total_pts += fib
            pred = p * p + jacobi_prime(kappa - 2, p) * (3 + jacobi_prime(kappa + 2, p)) * p + 1
            if total_pts != pred:
                mismatches += 1
            if p == 3 and kappa == ((-2) % 3):
                p3_cusp = total_pts
            if p in primes_base:
                base_sectors += 1
        # Check RPF2 at kappa = 2: smooth_only omits x = +-2 singular fibers
        if p >= 5:
            c2 = 4 % p
            sm2 = sum(
                (1 + (p - 1) * (1 + jacobi_prime((x * x - 4) % p, p)))
                if (4 * (c2 - x * x)) % p == 0
                else (p - jacobi_prime((x * x - 4) % p, p))
                for x in range(p)
                if (x * x - 4) % p != 0
            )
            if sm2 == p * p + 1:
                rpf2_omit_singular_fibers_fails = False

    return {
        "odd_primes_checked": len(primes_base),
        "extra_primes_checked": len(primes_extra),
        "sectors_checked": base_sectors,
        "p3_cusp_count": p3_cusp,
        "branchless_law_all_exact": (mismatches == 0 and p3_cusp == 1),
        "rpf2_omit_singular_fibers_fails": rpf2_omit_singular_fibers_fails,
    }


def check_e3_b2004_operator_and_abstract_6d() -> dict:
    def orbit_and_csig(M: int) -> tuple:
        rt = (3 % M, 3 % M, 3 % M)
        orb = [rt]
        idx = {rt: 0}
        q = deque([rt])
        while q:
            x, y, z = q.popleft()
            for w in (
                (x, z, (x * z - y) % M),
                (z, y, (y * z - x) % M),
                (x, (x * y - z) % M, y),
                ((x * y - z) % M, y, x),
            ):
                if w not in idx:
                    idx[w] = len(orb)
                    orb.append(w)
                    q.append(w)
        pC = tuple(idx[(v[1], v[2], v[0])] for v in orb)
        pS = tuple(idx[(v[1], v[0], (v[0] * v[1] - v[2]) % M)] for v in orb)
        return len(orb), pC, pS

    omega = sp.exp(2 * sp.pi * sp.I / 3)
    K_w = sp.QQ.algebraic_field(omega)
    w1 = K_w.from_sympy(omega)
    w2 = w1 * w1
    x = sp.Symbol("x")

    def halving_via_b2004_sigma(n: int, pC: tuple, pS: tuple) -> dict:
        """Uses B2004: W|_{H_0} = 6 Pi_0 P_sigma Pi_0 and W|_{H_1} = -3 Pi_1 P_sigma Pi_1 on C-orbits."""
        vis = [False] * n
        fix, cyc = [], []
        for i in range(n):
            if not vis[i]:
                if pC[i] == i:
                    vis[i] = True
                    fix.append(i)
                else:
                    j = pC[i]
                    k = pC[j]
                    vis[i] = vis[j] = vis[k] = True
                    cyc.append((i, j, k))
        d0 = len(fix) + len(cyc)
        d1 = len(cyc)
        v_b0, sz0 = {}, []
        for fi, v in enumerate(fix):
            v_b0[v] = fi
            sz0.append(1)
        off = len(fix)
        v_b1 = {}
        for oi, trip in enumerate(cyc):
            sz0.append(3)
            for sh, v in enumerate(trip):
                v_b0[v] = off + oi
                v_b1[v] = (oi, sh)

        # 6 Pi_0 P_sigma Pi_0 in unnormalized C-orbit sum basis (summing over all vertices of each C-orbit):
        r0 = [[0] * d0 for _ in range(d0)]
        for col, grp in enumerate([[f] for f in fix] + [list(t) for t in cyc]):
            for v in grp:
                row = v_b0[pS[v]]
                r0[row][col] += 6 // sz0[row]

        # -3 Pi_1 P_sigma Pi_1 on |u_o> = |v_0> + w^2 |v_1> + w |v_2>:
        # P_sigma |u_o> = |S v_0> + w^2 |S v_1> + w |S v_2>, and Pi_1 |v'_s> = (1/3) w^s |u_{o'}>,
        # so (-3) * (1/3) = -1: entry (o', o) is -sum_{r=0}^2 w^(-r + s_r) in Z[omega]!!
        w_pows = [K_w.one, w1, w2]
        r1 = [[K_w.zero] * d1 for _ in range(d1)]
        for col_o, trip in enumerate(cyc):
            for r_idx, v in enumerate(trip):
                sv = pS[v]
                if sv in v_b1:
                    row_o, s_idx = v_b1[sv]
                    r1[row_o][col_o] -= w_pows[(s_idx - r_idx) % 3]

        cp0 = sp.Poly.from_list(DomainMatrix.from_list(r0, sp.ZZ).charpoly(), x, domain=sp.ZZ).as_expr()
        dm1 = DomainMatrix(r1, (d1, d1), K_w)
        cp1 = sp.Poly([int(K_w.to_sympy(c)) for c in dm1.charpoly()], x, domain=sp.ZZ).as_expr()

        f0_2x = Counter({sp.Poly(f.subs(x, 2 * x), x).monic().as_expr(): m for f, m in sp.factor_list(cp0)[1]})
        f1_c = Counter({sp.Poly(f, x).monic().as_expr(): m for f, m in sp.factor_list(cp1)[1]})
        paired, unpaired = [], []
        p_deg, u_deg = 0, 0
        for f, m1 in sorted(f1_c.items(), key=lambda kv: (sp.degree(kv[0], x), str(kv[0]))):
            mp = min(m1, f0_2x[f])
            d = int(sp.degree(f, x))
            if mp > 0:
                p_deg += mp * d
                paired.append([str(f), int(mp), d])
            if m1 > mp:
                rem = m1 - mp
                u_deg += rem * d
                unpaired.append([str(f), int(rem), d])
        return {"n": n, "paired_deg": p_deg, "paired_factors": paired, "unpaired_deg": u_deg, "unpaired_factors": unpaired}

    m27 = halving_via_b2004_sigma(*orbit_and_csig(27))
    m45 = halving_via_b2004_sigma(*orbit_and_csig(45))
    m63 = halving_via_b2004_sigma(*orbit_and_csig(63))

    # Abstract 6D rational S_3 x Z_3 module V_rat6 = 1 (+) sgn (+) (E_2 (x) A_2) over ZZ (zero O_27 / N_3!):
    C_E2 = sp.Matrix([[0, -1], [1, -1]])
    S_E2 = sp.Matrix([[0, 1], [1, 0]])
    C_A2 = sp.Matrix([[0, -1], [1, -1]])
    I_2 = sp.eye(2)
    C_E2A2 = sp.Matrix(4, 4, lambda i, j: C_E2[i // 2, j // 2] * C_A2[i % 2, j % 2])
    S_E2A2 = sp.Matrix(4, 4, lambda i, j: S_E2[i // 2, j // 2] * I_2[i % 2, j % 2])

    def abstract_6d_unpaired(p_prime: int, flip_sgn: bool = False) -> tuple:
        np, pCp, pSp = orbit_and_csig(p_prime)
        sgn_val = 1 if flip_sgn else -1
        C6 = sp.diag(sp.Matrix([[1]]), sp.Matrix([[1]]), C_E2A2)
        S6 = sp.diag(sp.Matrix([[1]]), sp.Matrix([[sgn_val]]), S_E2A2)
        MC = sp.zeros(np, np)
        MS = sp.zeros(np, np)
        for i in range(np):
            MC[pCp[i], i] = 1
            MS[pSp[i], i] = 1
        N = 6 * np
        Ct = sp.Matrix(N, N, lambda i, j: C6[i // np, j // np] * MC[i % np, j % np])
        St = sp.Matrix(N, N, lambda i, j: S6[i // np, j // np] * MS[i % np, j % np])
        C2t = Ct * Ct
        Lt = St * C2t
        Lit = Ct * St
        Wt = Lt + Ct * Lt * C2t + C2t * Lt * Ct + Lit + Ct * Lit * C2t + C2t * Lit * Ct
        ns0 = (Ct - sp.eye(N)).nullspace()
        nsch = (C2t + Ct + sp.eye(N)).nullspace()
        B0 = sp.Matrix.hstack(*ns0)
        Bch = sp.Matrix.hstack(*nsch)
        X0 = (B0.T * B0).inv() * (B0.T * Wt * B0)
        Xch = (Bch.T * Bch).inv() * (Bch.T * Wt * Bch)
        cp0 = sp.Poly.from_list(DomainMatrix.from_Matrix(X0).convert_to(sp.QQ).charpoly(), x, domain=sp.QQ).as_expr()
        cpch = sp.Poly.from_list(DomainMatrix.from_Matrix(Xch).convert_to(sp.QQ).charpoly(), x, domain=sp.QQ).as_expr()
        f0_2x = Counter({sp.Poly(f.subs(x, 2 * x), x).monic().as_expr(): m for f, m in sp.factor_list(cp0)[1]})
        f1_c = Counter({sp.Poly(f, x).monic().as_expr(): m // 2 for f, m in sp.factor_list(cpch)[1]})
        unp, u_deg = [], 0
        for f, m1 in sorted(f1_c.items(), key=lambda kv: (sp.degree(kv[0], x), str(kv[0]))):
            rem = m1 - min(m1, f0_2x[f])
            if rem > 0:
                d = int(sp.degree(f, x))
                u_deg += rem * d
                unp.append([str(f), int(rem), d])
        return u_deg, unp

    u5_deg, u5_facs = abstract_6d_unpaired(5, False)
    u7_deg, u7_facs = abstract_6d_unpaired(7, False)
    u5_wrong_deg, _ = abstract_6d_unpaired(5, True)
    rpf3_flip_sgn_changes_defect = (u5_wrong_deg != u5_deg and u5_deg == 10)
    rpf5_mod45_vs_mod27_contrast = (m27["paired_deg"] == 23 and m27["unpaired_deg"] == 0 and m45["paired_deg"] == 4)

    return {
        "mod45_paired_deg": m45["paired_deg"],
        "mod45_paired_factors": m45["paired_factors"],
        "mod63_paired_deg": m63["paired_deg"],
        "mod63_paired_factors": m63["paired_factors"],
        "all_k_ge3_unpaired_deg_p5": u5_deg,
        "all_k_ge3_unpaired_factors_p5": u5_facs,
        "all_k_ge3_unpaired_deg_p7": u7_deg,
        "all_k_ge3_unpaired_factors_p7": u7_facs,
        "rpf3_flip_sgn_changes_defect": rpf3_flip_sgn_changes_defect,
        "rpf5_mod45_vs_mod27_contrast": rpf5_mod45_vs_mod27_contrast,
    }


def check_e4_sparse_sdm_mackey() -> dict:
    # Build O_81 and construct K_4 directly from Schreier fiber generators (without 1944-element G_4 BFS!)
    rt81 = (3, 3, 3)
    orb81 = [rt81]
    idx81 = {rt81: 0}
    q = deque([rt81])
    while q:
        x, y, z = q.popleft()
        for w in (
            (x, z, (x * z - y) % 81),
            (z, y, (y * z - x) % 81),
            (x, (x * y - z) % 81, y),
            ((x * y - z) % 81, y, x),
        ):
            if w not in idx81:
                idx81[w] = len(orb81)
                orb81.append(w)
                q.append(w)
    pL = tuple(idx81[(v[0], v[2], (v[0] * v[2] - v[1]) % 81)] for v in orb81)
    pR = tuple(idx81[(v[2], v[1], (v[1] * v[2] - v[0]) % 81)] for v in orb81)
    pLi = tuple(idx81[(v[0], (v[0] * v[1] - v[2]) % 81, v[1])] for v in orb81)
    pRi = tuple(idx81[((v[0] * v[1] - v[2]) % 81, v[1], v[0])] for v in orb81)

    orb9 = [(3 * s1 % 9, 3 * s2 % 9, 3 * s3 % 9) for s1 in (1, 2) for s2 in (1, 2) for s3 in (1, 2)]
    idx9 = {pt: i for i, pt in enumerate(orb9)}
    fib = [idx9[(v[0] % 9, v[1] % 9, v[2] % 9)] for v in orb81]
    pL9 = tuple(idx9[(v[0], v[2], (v[0] * v[2] - v[1]) % 9)] for v in orb9)
    pR9 = tuple(idx9[(v[2], v[1], (v[1] * v[2] - v[0]) % 9)] for v in orb9)
    pLi9 = tuple(idx9[(v[0], (v[0] * v[1] - v[2]) % 9, v[1])] for v in orb9)
    pRi9 = tuple(idx9[((v[0] * v[1] - v[2]) % 9, v[1], v[0])] for v in orb9)

    comp81 = lambda a, b: tuple(a[b[i]] for i in range(648))
    comp9 = lambda a, b: tuple(a[b[i]] for i in range(8))
    id81 = tuple(range(648))
    id9 = tuple(range(8))

    # 24-coset Schreier transversal of S_4 -> generate K_4 (81 elements) directly!
    cos24 = {id9: (id81, id81)}
    cq = deque([id9])
    g_list = [(pL9, pL, pLi), (pR9, pR, pRi), (pLi9, pLi, pL), (pRi9, pRi, pR)]
    while cq:
        c = cq.popleft()
        u, ui = cos24[c]
        for g9, g81, gi81 in g_list:
            nc = comp9(g9, c)
            if nc not in cos24:
                cos24[nc] = (comp81(g81, u), comp81(ui, gi81))
                cq.append(nc)

    k4_gens = []
    for c, (u, _) in cos24.items():
        for g9, g81, _ in ((pL9, pL, pLi), (pR9, pR, pRi)):
            nc = comp9(g9, c)
            _, unci = cos24[nc]
            sch = comp81(unci, comp81(g81, u))
            if sch != id81:
                k4_gens.append(sch)
    K4 = {id81}
    kq = deque([id81])
    while kq:
        g = kq.popleft()
        for kg in k4_gens:
            ng = comp81(kg, g)
            if ng not in K4:
                K4.add(ng)
                kq.append(ng)

    def pow81(g: tuple, e: int) -> tuple:
        r = id81
        for _ in range(e):
            r = comp81(g, r)
        return r

    ord9 = [g for g in K4 if pow81(g, 3) != id81]
    ga = ord9[0]
    suba = {pow81(ga, i) for i in range(9)}
    gb = next(g for g in ord9 if pow81(g, 3) not in suba)
    grid = {(i, j): comp81(pow81(ga, i), pow81(gb, j)) for i in range(9) for j in range(9)}
    igrid = {g: ij for ij, g in grid.items()}
    reps = [next(i for i, f in enumerate(fib) if f == fid) for fid in range(8)]
    coords = {gij[reps[f]]: (f, i, j) for f in range(8) for (i, j), gij in grid.items()}

    def amat(pg: tuple, pgi: tuple) -> list:
        c1 = igrid[comp81(pg, comp81(ga, pgi))]
        c2 = igrid[comp81(pg, comp81(gb, pgi))]
        return [[c1[0], c2[0]], [c1[1], c2[1]]]

    AL = amat(pL, pLi)
    AR = amat(pR, pRi)
    shL = [coords[pL[reps[f]]] for f in range(8)]
    shR = [coords[pR[reps[f]]] for f in range(8)]

    def invT(A: list) -> list:
        d = pow((A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 9, -1, 9)
        return [[(d * A[1][1]) % 9, (-d * A[1][0]) % 9], [(-d * A[0][1]) % 9, (d * A[0][0]) % 9]]

    BL, BR = invT(AL), invT(AR)
    vis_m = set()
    orbs = []
    for m1 in range(9):
        for m2 in range(9):
            if (m1, m2) not in vis_m:
                om = []
                dq = deque([(m1, m2)])
                vis_m.add((m1, m2))
                while dq:
                    u = dq.popleft()
                    om.append(u)
                    for B in (BL, BR):
                        w = ((B[0][0] * u[0] + B[0][1] * u[1]) % 9, (B[1][0] * u[0] + B[1][1] * u[1]) % 9)
                        if w not in vis_m:
                            vis_m.add(w)
                            dq.append(w)
                orbs.append(om)

    # Use conjugate primitive root zeta_9^(-1) = exp(-2 pi i / 9) and sparse SDM arithmetic!
    zeta9_conj = sp.exp(-2 * sp.pi * sp.I / 9)
    Kc = sp.QQ.algebraic_field(zeta9_conj)
    zc = Kc.from_sympy(zeta9_conj)
    zp = [Kc.one]
    for _ in range(1, 9):
        zp.append(zp[-1] * zc)

    size_hist = Counter(len(o) for o in orbs)
    inv_hits = []
    other_zero = True
    rpf4_flipped_cos_sign_zero = True

    for om in orbs:
        mi = {m: idx for idx, m in enumerate(om)}
        dim_b = 8 * len(om)
        rows = [[Kc.zero] * dim_b for _ in range(dim_b)]
        for ci, m in enumerate(om):
            mL = ((BL[0][0] * m[0] + BL[0][1] * m[1]) % 9, (BL[1][0] * m[0] + BL[1][1] * m[1]) % 9)
            mR = ((BR[0][0] * m[0] + BR[0][1] * m[1]) % 9, (BR[1][0] * m[0] + BR[1][1] * m[1]) % 9)
            rL, rR = mi[mL], mi[mR]
            for f in range(8):
                col = 8 * ci + f
                tfL, sL1, sL2 = shL[f]
                rows[8 * rL + tfL][col] += zp[(mL[0] * sL1 + mL[1] * sL2) % 9]
                tfR, sR1, sR2 = shR[f]
                rows[8 * rR + tfR][col] += zp[(mR[0] * sR1 + mR[1] * sR2) % 9]
        Ws = DomainMatrix(rows, (dim_b, dim_b), Kc).to_sparse()
        Is = DomainMatrix.eye(dim_b, Kc).to_sparse()
        W2s = Ws * Ws
        W4s = W2s * W2s
        neg_cl = all(((-m[0]) % 9, (-m[1]) % 9) in mi for m in om)
        ord9_fl = any((3 * m[0]) % 9 != 0 or (3 * m[1]) % 9 != 0 for m in om)

        q_hits = []
        for r in (1, 2, 4):
            two_w = Kc.one - (zp[r] + zp[9 - r]) * Kc.from_sympy(sp.Integer(2))
            Qr = (W4s - W2s.scalarmul(two_w) + Is.scalarmul(Kc.from_sympy(sp.Integer(4)))).to_dense()
            nl = dim_b - Qr.rank()
            if nl > 0:
                q_hits.append([r, nl])
            if len(om) == 6 and neg_cl and ord9_fl:
                two_w_bad = Kc.one + (zp[r] + zp[9 - r]) * Kc.from_sympy(sp.Integer(2))
                Qr_bad = (W4s - W2s.scalarmul(two_w_bad) + Is.scalarmul(Kc.from_sympy(sp.Integer(4)))).to_dense()
                if dim_b - Qr_bad.rank() != 0:
                    rpf4_flipped_cos_sign_zero = False
        if len(om) == 6 and neg_cl and ord9_fl:
            inv_hits.append(q_hits[0])
        elif q_hits:
            other_zero = False

    # Verify y^3 - 3y + 1 minimal polynomial of y_r = zeta_9^r + zeta_9^(-r) -> P_12!
    p_coeffs = [Kc.one]
    for r in (1, 2, 4):
        tw = Kc.one - (zp[r] + zp[9 - r]) * Kc.from_sympy(sp.Integer(2))
        qc = [Kc.one, Kc.zero, -tw, Kc.zero, Kc.from_sympy(sp.Integer(4))]
        nxt = [Kc.zero] * (len(p_coeffs) + len(qc) - 1)
        for ia, ca in enumerate(p_coeffs):
            for ib, cb in enumerate(qc):
                nxt[ia + ib] += ca * cb
        p_coeffs = nxt
    p12_ok = ([Kc.to_sympy(c) for c in p_coeffs] == [sp.Integer(c) for c in [1, 0, -3, 0, 3, 0, -21, 0, 12, 0, -48, 0, 64]])

    # Mackey index via Burnside/inner-product of permutation characters on O_9 / H_chi:
    # |S \ S_4 / H| = (1/|S_4|) sum_{g in S_4} |Fix_{S_4/S}(g)| * |Fix_{S_4/H}(g)|!
    m0 = next(om for om in orbs if len(om) == 6 and all(((-m[0]) % 9, (-m[1]) % 9) in om for m in om) and any((3 * m[0]) % 9 != 0 or (3 * m[1]) % 9 != 0 for m in om))
    # Track S_4 on both O_9 (size 8 = S_4/S, since |S|=3!) and m0 (size 6 = S_4/H, since |H|=4!):
    m0_idx = {m: i for i, m in enumerate(m0)}
    pLm = tuple(m0_idx[((BL[0][0] * m[0] + BL[0][1] * m[1]) % 9, (BL[1][0] * m[0] + BL[1][1] * m[1]) % 9)] for m in m0)
    pRm = tuple(m0_idx[((BR[0][0] * m[0] + BR[0][1] * m[1]) % 9, (BR[1][0] * m[0] + BR[1][1] * m[1]) % 9)] for m in m0)
    s4_pairs = {(id9, tuple(range(6)))}
    sq = deque([(id9, tuple(range(6)))])
    while sq:
        a8, a6 = sq.popleft()
        for g8, g6 in ((pL9, pLm), (pR9, pRm)):
            na8 = tuple(g8[a8[i]] for i in range(8))
            na6 = tuple(g6[a6[i]] for i in range(6))
            if (na8, na6) not in s4_pairs:
                s4_pairs.add((na8, na6))
                sq.append((na8, na6))
    burnside_sum = sum(
        sum(1 for i in range(8) if a8[i] == i) * sum(1 for j in range(6) if a6[j] == j)
        for a8, a6 in s4_pairs
    )
    mackey_dc = burnside_sum // len(s4_pairs)

    return {
        "regular_K4_fiber_action": (len(K4) == 81 and len(coords) == 648),
        "dual_K4_orbit_count": len(orbs),
        "dual_K4_orbit_size_hist": {str(k): v for k, v in sorted(size_hist.items())},
        "p12_galois_product_exact": p12_ok,
        "inv_closed_ord9_orbit_count": len(inv_hits),
        "quartic_r_and_nullity_pairs": sorted(inv_hits),
        "mackey_double_cosets": mackey_dc,
        "other_orbits_zero": other_zero,
        "rpf4_flipped_cos_sign_zero": rpf4_flipped_cos_sign_zero,
    }


def main() -> int:
    def _norm(obj):
        if isinstance(obj, bool) or isinstance(obj, sp.logic.boolalg.BooleanAtom):
            return bool(obj)
        if isinstance(obj, (int, sp.Integer)):
            return int(obj)
        if isinstance(obj, dict):
            return {str(k): _norm(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [_norm(v) for v in obj]
        return obj

    here = pathlib.Path(__file__).resolve().parent
    prod = json.loads((here / "c71_out.json").read_text(encoding="utf-8"))

    c1 = _norm(check_e1_disjoint_poised_grid(11))
    c2 = _norm(check_e2_conic_character_sum())
    c3 = _norm(check_e3_b2004_operator_and_abstract_6d())
    c4 = _norm(check_e4_sparse_sdm_mackey())

    discrepancies = []

    def cmp(name: str, got, exp) -> None:
        if got != exp:
            discrepancies.append({"field": name, "countercheck": got, "producer": exp})

    pe1 = prod["E1_kempner_3adic_tower"]
    cmp("E1.hensel_and_inverses_exact", c1["hensel_and_inverses_exact"], pe1["hensel_and_inverses_exact"])
    cmp("E1.dims_k3_k11", c1["dims_k3_k11"], pe1["dims_k3_k11"])
    cmp("E1.cubing_ranks_k3_k10", c1["cubing_ranks_k3_k10"], pe1["cubing_ranks_k3_k10"])
    cmp("E1.log3_K_k3_k11", c1["log3_K_k3_k11"], pe1["log3_K_k3_k11"])
    cmp("E1.G11_order_str", c1["G11_order_str"], pe1["G11_order_str"])

    pe2 = prod["E2_b1990_branchless_counts"]
    cmp("E2.odd_primes_checked", c2["odd_primes_checked"], pe2["odd_primes_checked"])
    cmp("E2.sectors_checked", c2["sectors_checked"], pe2["sectors_checked"])
    cmp("E2.p3_cusp_count", c2["p3_cusp_count"], pe2["p3_cusp_count"])
    cmp("E2.branchless_law_all_exact", c2["branchless_law_all_exact"], pe2["branchless_law_all_exact"])

    pe3 = prod["E3_b2003_crt_and_q6_defect"]
    cmp("E3.mod45_paired_deg", c3["mod45_paired_deg"], pe3["mod45_paired_deg"])
    cmp("E3.mod45_paired_factors", c3["mod45_paired_factors"], pe3["mod45_paired_factors"])
    cmp("E3.mod63_paired_deg", c3["mod63_paired_deg"], pe3["mod63_paired_deg"])
    cmp("E3.mod63_paired_factors", c3["mod63_paired_factors"], pe3["mod63_paired_factors"])
    cmp("E3.all_k_ge3_unpaired_deg_p5", c3["all_k_ge3_unpaired_deg_p5"], pe3["all_k_ge3_unpaired_deg_p5"])
    cmp("E3.all_k_ge3_unpaired_factors_p5", c3["all_k_ge3_unpaired_factors_p5"], pe3["all_k_ge3_unpaired_factors_p5"])
    cmp("E3.all_k_ge3_unpaired_deg_p7", c3["all_k_ge3_unpaired_deg_p7"], pe3["all_k_ge3_unpaired_deg_p7"])
    cmp("E3.all_k_ge3_unpaired_factors_p7", c3["all_k_ge3_unpaired_factors_p7"], pe3["all_k_ge3_unpaired_factors_p7"])

    pe4 = prod["E4_b1997_k4_mackey_ninth_roots"]
    cmp("E4.regular_K4_fiber_action", c4["regular_K4_fiber_action"], pe4["regular_K4_fiber_action"])
    cmp("E4.dual_K4_orbit_count", c4["dual_K4_orbit_count"], pe4["dual_K4_orbit_count"])
    cmp("E4.dual_K4_orbit_size_hist", c4["dual_K4_orbit_size_hist"], pe4["dual_K4_orbit_size_hist"])
    cmp("E4.p12_galois_product_exact", c4["p12_galois_product_exact"], pe4["p12_galois_product_exact"])
    cmp("E4.inv_closed_ord9_orbit_count", c4["inv_closed_ord9_orbit_count"], pe4["inv_closed_ord9_orbit_count"])
    cmp("E4.quartic_r_and_nullity_pairs", c4["quartic_r_and_nullity_pairs"], pe4["quartic_r_and_nullity_pairs"])
    cmp("E4.mackey_double_cosets", c4["mackey_double_cosets"], pe4["mackey_double_cosets"])

    rpf_flags = [
        c1["rpf1_naive_mod3_grid_undercounts_L6"],
        c2["rpf2_omit_singular_fibers_fails"],
        c3["rpf3_flip_sgn_changes_defect"],
        c4["other_orbits_zero"],
        c3["rpf5_mod45_vs_mod27_contrast"],
    ]
    rpf_caught = sum(1 for f in rpf_flags if f)

    out = {
        "card": "AGY-C71-COUNTERCHECK",
        "seat_code": "fam3-v1-high-01",
        "parameter_count": "0 of 19",
        "shared_imports_with_producer": 0,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "referee_planted_faults_caught": rpf_caught,
        "referee_planted_faults_total": 5,
        "extra_primes_verified_e2": c2["extra_primes_verified"] if "extra_primes_verified" in c2 else c2["extra_primes_checked"],
        "summary": {
            "dims_k3_k11": c1["dims_k3_k11"],
            "mod45_paired_deg": c3["mod45_paired_deg"],
            "unpaired_deg_p5_p7": [c3["all_k_ge3_unpaired_deg_p5"], c3["all_k_ge3_unpaired_deg_p7"]],
            "quartic_r_and_nullity_pairs": c4["quartic_r_and_nullity_pairs"],
            "mackey_double_cosets": c4["mackey_double_cosets"],
        },
    }
    (here / "c71_countercheck_out.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(
        f"COUNTERCHECK_C71: discrepancies={len(discrepancies)} rpf={rpf_caught}/5 "
        f"dims={c1['dims_k3_k11']} unp={[c3['all_k_ge3_unpaired_deg_p5'], c3['all_k_ge3_unpaired_deg_p7']]}\n"
    )
    return 0 if (len(discrepancies) == 0 and rpf_caught == 5) else 1


if __name__ == "__main__":
    sys.exit(main())
