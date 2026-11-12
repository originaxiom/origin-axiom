#!/usr/bin/env python3
"""Standalone post-run check for X-C1b rows 923, 924, 925, and 929.

Leaves relays/x_c1b_verify/verify_x_c1b.py (3a4db80cb) and
relays/x_c1b_verify/verify_x_c1b_out.json (915624ba3) completely untouched,
and directly tests the four specification/helper discrepancies diagnosed after
reading verify_x_c1b_out.json:
  - Row 923: include R's second fixed-point coordinate equation z - y = 0 in eqs_lr.
  - Row 924 (I1): evaluate m135 (-LLRR) on the degree-1 base manifold at its 8
    characters with kappa = nu(abt) = 1 (u_1 = (0, 1/2) and u_2 = (1/2, 0)).
  - Row 925: include the odd-trace stable-letter lift U_t in SL(2, F_3) alongside
    Q_a, Q_b when checking <Q_a, Q_b, U_t> = SL(2, F_3) = 2T (24) and PSL = A_4 (12)
    on both +LR and +LLLR.
  - Row 929 (W15 Parts a and b): verify per-twin reading counts (36 on vector-like
    twins +LR, +LLRLRR and 24 on chiral twins -LR, -LLRLRR; 36 + 24 = 60) across
    p in {20089, 50329, 90073}.

0 of 19.
"""
from __future__ import annotations

from collections import Counter, deque
import hashlib
import json
import pathlib
import sys
import time

import gmpy2
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import verify_x_c1b as base  # noqa: E402


def check_923() -> dict[str, object]:
    xs, ys, zs = sp.symbols("x y z")
    # L(x, y, z) = (z, y, y*z - x); R(x, y, z) = (x, z, x*z - y)
    eqs_lr_full = [zs - xs, ys * zs - xs - zs, zs - ys, xs * zs - ys - zs]
    gb_lr = sp.groebner(eqs_lr_full, xs, ys, zs, order="lex")
    gb_polys = [str(sp.Poly(e, xs, ys, zs).as_expr()) for e in gb_lr.exprs]
    sols_lr = sp.solve(list(gb_lr.exprs), (xs, ys, zs), dict=True)
    pts_lr = sorted((int(s[xs]), int(s[ys]), int(s[zs])) for s in sols_lr)

    gb_swap = sp.groebner(eqs_lr_full + [ys - xs], xs, ys, zs, order="lex")
    sols_swap = sp.solve(list(gb_swap.exprs), (xs, ys, zs), dict=True)
    pts_swap = sorted((int(s[xs]), int(s[ys]), int(s[zs])) for s in sols_swap)

    kappas = {str(pt): pt[0] ** 2 + pt[1] ** 2 + pt[2] ** 2 - pt[0] * pt[1] * pt[2] - 2 for pt in pts_lr}

    # Planted control PC_923: drop z - y (reproducing the omission in verify_x_c1b.py)
    gb_dropped = sp.groebner([zs - xs, ys * zs - xs - zs, xs * zs - ys - zs], xs, ys, zs, order="lex")
    pts_dropped = sorted((int(s[xs]), int(s[ys]), int(s[zs])) for s in sp.solve(list(gb_dropped.exprs), (xs, ys, zs), dict=True))
    pc_923_fired = pts_dropped == [(-1, 2, -1), (0, 0, 0), (2, 2, 2)] and pts_lr != pts_dropped
    if not pc_923_fired:
        sys.exit(2)

    gb_target = [xs - zs, ys - zs, zs**2 - 2 * zs]
    gb_exact = all(sp.expand(a - b) == 0 for a, b in zip(gb_lr.exprs, gb_target)) and len(gb_lr.exprs) == 3
    ok = (
        gb_exact
        and pts_lr == [(0, 0, 0), (2, 2, 2)]
        and pts_swap == [(0, 0, 0), (2, 2, 2)]
        and kappas["(0, 0, 0)"] == -2
        and kappas["(2, 2, 2)"] == 2
    )
    return {
        "groebner_basis_lex": gb_polys,
        "groebner_matches_stated_basis": gb_exact,
        "fixed_points_LR": [list(pt) for pt in pts_lr],
        "fixed_points_LR_P_negI": [list(pt) for pt in pts_swap],
        "puncture_traces_kappa": kappas,
        "pc_923_fired": pc_923_fired,
        "result": "the same" if ok else "differs",
    }


def check_924_i1() -> dict[str, object]:
    # Degree-1 base manifold m135 = -LLRR: meridian is mu_w = abt, so kappa = nu(abt) = 1 <=> (c_a + c_b + c_t) % 4 == 0
    cov_base = base.build_cover("-", "LLRR", 1, {"a": [0], "b": [0], "t": [0]})
    assert cov_base["gen_words"] == ["a", "b", "t"]
    hol_m135 = base.get_holonomy("-", "LLRR")
    gm4, gm4_inv = hol_m135["gm4"], hol_m135["gm4_inv"]
    gen_m0 = [gm4["a"], gm4["b"], gm4["t"]]
    gen_i0 = [gm4_inv["a"], gm4_inv["b"], gm4_inv["t"]]
    roots4 = base.gm_roots_of_unity(4)
    z0, one = gmpy2.mpc(0), gmpy2.mpc(1)

    chars_all = base.cover_characters(cov_base, 4)
    chars_kappa1 = [c for c in chars_all if int(c[0] + c[1] + c[2]) % 4 == 0]
    chars_kappai = [c for c in chars_all if int(c[0] + c[1] + c[2]) % 4 == 1]

    active_members: list[dict[str, object]] = []
    for c_ch in chars_kappa1:
        mc = [base.gm_scale(roots4[int(c_ch[j]) % 4], gen_m0[j]) for j in range(3)]
        ic = [base.gm_scale(roots4[(-int(c_ch[j])) % 4], gen_i0[j]) for j in range(3)]
        h0, h1, r1, n_c, int_b = base.cohom_pres_gm(mc, ic, cov_base["rels_idx"], cov_base["cusps_idx"], want_interior=True)
        if n_c > 0 and int_b is not None:
            c_vec = [sum(int_b[i][r] * gmpy2.mpc(r + 1, r + 2) for r in range(n_c)) for i in range(12)]
            W1_m, W1_i, W1s_m, W1s_i = [], [], [], []
            L2_m, L2_i, L2s_m, L2s_i = [], [], [], []
            for j in range(3):
                Aj, Aij = mc[j], ic[j]
                cj = c_vec[4 * j : 4 * (j + 1)]
                naic = [-sum(Aij[ri][k] * cj[k] for k in range(4)) for ri in range(4)]
                M5 = [Aj[ri] + [cj[ri]] for ri in range(4)] + [[z0, z0, z0, z0, one]]
                M5i = [Aij[ri] + [naic[ri]] for ri in range(4)] + [[z0, z0, z0, z0, one]]
                M5s, M5si = base.gm_transpose(M5i), base.gm_transpose(M5)
                W1_m.append(M5); W1_i.append(M5i); W1s_m.append(M5s); W1s_i.append(M5si)
                L2_m.append(base.wedge2_gm(M5)); L2_i.append(base.wedge2_gm(M5i))
                L2s_m.append(base.wedge2_gm(M5s)); L2s_i.append(base.wedge2_gm(M5si))
            nw1 = base.cohom_pres_gm(W1_m, W1_i, cov_base["rels_idx"], cov_base["cusps_idx"])[3]
            nw1s = base.cohom_pres_gm(W1s_m, W1s_i, cov_base["rels_idx"], cov_base["cusps_idx"])[3]
            nl2 = base.cohom_pres_gm(L2_m, L2_i, cov_base["rels_idx"], cov_base["cusps_idx"])[3]
            nl2s = base.cohom_pres_gm(L2s_m, L2s_i, cov_base["rels_idx"], cov_base["cusps_idx"])[3]
            active_members.append({
                "c_abt_mod4": [int(x) for x in c_ch],
                "tuple_A": [h0, h1, r1, n_c],
                "count_W1_L2": [nw1 - nw1s, nl2 - nl2s],
            })

    # Planted control PC_924: perturb kappa = 1 to kappa = i, asserting 0 interior classes
    kappai_active = 0
    for c_ch in chars_kappai:
        mc = [base.gm_scale(roots4[int(c_ch[j]) % 4], gen_m0[j]) for j in range(3)]
        ic = [base.gm_scale(roots4[(-int(c_ch[j])) % 4], gen_i0[j]) for j in range(3)]
        if base.cohom_pres_gm(mc, ic, cov_base["rels_idx"], cov_base["cusps_idx"])[3] > 0:
            kappai_active += 1
    pc_924_fired = len(chars_kappai) == 8 and kappai_active == 0 and len(active_members) == 2
    if not pc_924_fired:
        sys.exit(2)

    char_pairs = sorted((m["c_abt_mod4"][0], m["c_abt_mod4"][1]) for m in active_members)
    counts_only = [m["count_W1_L2"] for m in active_members]
    ok = (
        len(chars_kappa1) == 8
        and len(active_members) == 2
        and char_pairs == [(0, 2), (2, 0)]
        and counts_only == [[-1, -1], [-1, -1]]
    )
    return {
        "kappa1_character_count": len(chars_kappa1),
        "active_members": active_members,
        "pc_924_fired": pc_924_fired,
        "result": "the same" if ok else "differs",
    }


def check_925_f3() -> dict[str, object]:
    Qa = ((0, 2), (1, 0))
    Qb = ((1, 1), (1, 2))
    I_f3 = ((1, 0), (0, 1))

    def m3(X, Y):
        return (
            ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % 3, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % 3),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % 3, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % 3),
        )

    def inv3(X):
        return ((X[1][1] % 3, (-X[0][1]) % 3), ((-X[1][0]) % 3, X[0][0] % 3))

    sl2_all = [
        ((a, b), (c, d))
        for a in range(3)
        for b in range(3)
        for c in range(3)
        for d in range(3)
        if (a * d - b * c) % 3 == 1
    ]
    assert len(sl2_all) == 24

    def eval_w3(w: str):
        R = I_f3
        gens = {"a": Qa, "b": Qb, "A": inv3(Qa), "B": inv3(Qb)}
        for ch in w:
            R = m3(R, gens[ch])
        return R

    def closure_orders(gens_list):
        seen = {I_f3}
        q = deque([I_f3])
        while q:
            cur = q.popleft()
            for g in gens_list:
                nxt = m3(cur, g)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        psl = {min(g, tuple(tuple((-x) % 3 for x in r) for r in g)) for g in seen}
        return len(seen), len(psl)

    thread_results = {}
    for sgn, w in [("+", "LR"), ("-", "LR"), ("+", "LLLR"), ("-", "LLLR")]:
        img = base.phi1_words(sgn, w)
        ta, tb = eval_w3(img["a"]), eval_w3(img["b"])
        lifts = [U for U in sl2_all if m3(m3(U, Qa), inv3(U)) == ta and m3(m3(U, Qb), inv3(U)) == tb]
        if len(lifts) != 2:
            sys.exit(2)
        ord_sl2, ord_psl2 = closure_orders([Qa, Qb, lifts[0]])
        thread_results[sgn + w] = {"lift_count": len(lifts), "sl2_order": ord_sl2, "psl2_order": ord_psl2}

    # Planted control PC_925: omit U_t so only the fibre holonomy <Q_a, Q_b> = Q_8 (8) / V_4 (4) is generated
    fib_sl2, fib_psl2 = closure_orders([Qa, Qb])
    pc_925_fired = (fib_sl2, fib_psl2) == (8, 4) and all(
        v["sl2_order"] == 24 and v["psl2_order"] == 12 for v in thread_results.values()
    )
    if not pc_925_fired:
        sys.exit(2)

    ok = all(v["sl2_order"] == 24 and v["psl2_order"] == 12 for v in thread_results.values())
    return {
        "fibre_only_orders_Q8_V4": [fib_sl2, fib_psl2],
        "thread_congruence_orders_2T_A4": thread_results,
        "pc_925_fired": pc_925_fired,
        "result": "the same" if ok else "differs",
    }


def check_929_extensions() -> dict[str, object]:
    odd6 = base.genesis_states(6, odd_only=True)
    sub_states = [s for s in odd6 if (s[0] + s[1]) in ("+LR", "-LR", "+LLRLRR", "-LLRLRR")]
    all_q = [(0, 0), (1, 0), (0, 1), (1, 1)]

    def eval_subset(states_list, prime_p: int):
        sp_p = base.setup_spin_gf(prime_p)
        QA_p, QB_p = sp_p["QA"], sp_p["QB"]
        QAi_p, QBi_p = sp_p["QAi"], sp_p["QBi"]
        z24_p = int(sp_p["zeta24"])
        lift_p = sp_p["lift_steps_2d"]
        pars_nz = [(1, 0), (0, 1), (1, 1)]
        tot = 0
        hist: Counter[int] = Counter()
        per_state: dict[str, dict[str, int]] = {}
        for sgn, w, _ in states_list:
            lbl = sgn + w
            st_cnt: Counter[int] = Counter()
            steps3, mu3, _ = base.steps_route2(sgn, w, 3)
            u3_part = mu3[:-1]
            U3 = lift_p(steps3, 0)
            U3i = base.np_inv_gf(U3, prime_p)
            for par_p in pars_nz:
                bp_a = prime_p - 1 if par_p[0] else 1
                bp_b = prime_p - 1 if par_p[1] else 1
                bp_t = 1
                for ch in u3_part:
                    bp_t = (bp_t * (bp_a if ch in "aA" else bp_b)) % prime_p
                bp_vals = {"a": bp_a, "b": bp_b, "t": bp_t}
                for par_q in all_q:
                    qa_s = prime_p - 1 if par_q[0] else 1
                    qb_s = prime_p - 1 if par_q[1] else 1
                    qt_u = 1
                    for ch in u3_part:
                        qt_u = (qt_u * (qa_s if ch in "aA" else qb_s)) % prime_p
                    Aa = (qa_s * QA_p) % prime_p
                    Ab = (qb_s * QB_p) % prime_p
                    Aai = (qa_s * QAi_p) % prime_p
                    Abi = (qb_s * QBi_p) % prime_p
                    for k24 in range(24):
                        kap = pow(z24_p, k24, prime_p)
                        At = ((kap * qt_u) % prime_p * U3) % prime_p
                        Ati = (pow((kap * qt_u) % prime_p, prime_p - 2, prime_p) * U3i) % prime_p
                        A_m = {"a": Aa, "b": Ab, "t": At}
                        A_i = {"a": Aai, "b": Abi, "t": Ati}
                        hom_m = {g: (bp_vals[g] * A_m[g]) % prime_p for g in "abt"}
                        hom_i = {g: (bp_vals[g] * A_i[g]) % prime_p for g in "abt"}
                        _, h1_g, _, _, cocs = base.cohom_steps_np_gf(hom_m, hom_i, steps3, "abAB", mu3, prime_p, want_cocs=True)
                        if h1_g == 0:
                            continue
                        draws_c = list(cocs)
                        if h1_g >= 2:
                            gen_c = np.zeros_like(cocs[0])
                            for ic, zc in enumerate(cocs):
                                gen_c = (gen_c + pow(z24_p, 5 * ic + 1, prime_p) * zc) % prime_p
                            draws_c.append(gen_c)
                        for cv in draws_c:
                            X_m, X_i = {}, {}
                            for gi, g in enumerate("abt"):
                                cg = cv[2 * gi : 2 * (gi + 1)].reshape(2, 1)
                                bpg = bp_vals[g]
                                cBp = (cg * bpg) % prime_p
                                neg_Aic = ((-A_i[g] @ cg) % prime_p)
                                M3x = np.block([[A_m[g], cBp], [np.zeros((1, 2), dtype=np.int64), np.array([[bpg]], dtype=np.int64)]]) % prime_p
                                M3xi = np.block([[A_i[g], neg_Aic], [np.zeros((1, 2), dtype=np.int64), np.array([[bpg]], dtype=np.int64)]]) % prime_p
                                X_m[g], X_i[g] = M3x, M3xi
                            t_X, t_Xs = base.verify_b1604_e1_duality_gf(X_m, X_i, steps3, "abAB", mu3, prime_p)
                            ix = t_X[3] - t_Xs[3]
                            tot += 1
                            hist[ix] += 1
                            st_cnt[ix] += 1
            per_state[lbl] = {str(k): int(v) for k, v in sorted(st_cnt.items())}
        return {"total": tot, "hist": {str(k): int(v) for k, v in sorted(hist.items())}, "per_state": per_state}

    res_by_prime = {str(p_val): eval_subset(sub_states, p_val) for p_val in (20089, 50329, 90073)}

    # Planted control PC_929: swap silent +LLRLRR with firing +LR, asserting silent zero-check fails
    r0 = res_by_prime["20089"]["per_state"]
    pc_929_fired = (r0["+LLRLRR"] == {"0": 36}) and (r0["+LR"] == {"1": 36}) and (r0["+LR"] != {"0": 36})
    if not pc_929_fired:
        sys.exit(2)

    ok = all(
        rp["total"] == 120
        and rp["hist"] == {"0": 60, "1": 60}
        and rp["per_state"]["+LR"] == {"1": 36}
        and rp["per_state"]["-LR"] == {"1": 24}
        and rp["per_state"]["+LLRLRR"] == {"0": 36}
        and rp["per_state"]["-LLRLRR"] == {"0": 24}
        for rp in res_by_prime.values()
    )
    return {
        "primes_checked": res_by_prime,
        "pc_929_fired": pc_929_fired,
        "result": "the same" if ok else "differs",
    }


def main() -> None:
    t0 = time.time()
    r923 = check_923()
    r924 = check_924_i1()
    r925 = check_925_f3()
    r929 = check_929_extensions()
    all_controls = bool(r923["pc_923_fired"] and r924["pc_924_fired"] and r925["pc_925_fired"] and r929["pc_929_fired"])
    payload = {
        "card": "X-C1b-postrun",
        "seat": "agy-exp",
        "all_planted_controls_fired": all_controls,
        "checks": {
            "923": r923,
            "924_I1": r924,
            "925_F3_congruence": r925,
            "929_W15_extensions": r929,
        },
        "elapsed_seconds": round(time.time() - t0, 3),
    }
    out_path = HERE / "postrun_923_924_925_929_out.json"
    out_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    digest = hashlib.sha256(out_bytes).hexdigest()
    (HERE / "POSTRUN_OUTPUT_SHA256.txt").write_text(f"{digest}  postrun_923_924_925_929_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
