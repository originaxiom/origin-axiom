#!/usr/bin/env python3
"""W126 — the read-out on the physical spacetime (main's C10) for the ground-state universes (the script;
`W126_RULE.md` was committed and pushed before it).

On the Milne universe over a closed hyperbolic N the Lorentzian index of the E-twisted Dirac operator is -h(D_N^E)
(Bar-Strohmaier; the rule). On the Weeks and Meyerhoff manifolds the triplet's bundle restricts to C^{m1}, so the
index is -m1 h(D_N). This script computes h(D_N) by the spinor trace formula on W124's instrument (its enumeration and
unfolding identity, unchanged), carrying each element's lift to SL(2, C) for the manifold's unique spin structure.

    D0  the instrument (the spin signs, the frame, |tr|^2 against the O(3,1) trace, W124 reproduced)
    D1  Weyl for spinors      D2  positivity      D3, D4  S_1/2(0) < 1.9 on Weeks, Meyerhoff
    D5  the triplet's image group and its eigenvalue orders (exact)      D6  read-outs

    python3 -B the_physical_readout.py      # writes the_physical_readout.json and the_physical_readout_run.txt
"""
import contextlib
import gc
import io
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import snappy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_graviton_spectrum as GS  # noqa: E402

R, W, TGRID = GS.R, GS.W, GS.TGRID
out, log = {"arc": "W126", "rule": "W126_RULE.md"}, []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    log.append(s)


def mat(m, n):
    return np.array([[complex(m[i, j]) for j in range(n)] for i in range(n)])


# ---------------- the domain with words, and the spin lift ----------------
SIG = np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)


def phi(A):
    """SL(2, C) -> SO+(3,1) in signature (+,-,-,-): Lambda^mu_nu = tr(sigma_mu A sigma_nu A^dagger) / 2"""
    A = np.asarray(A)
    H = np.einsum("...ij,njk,...lk->...nil", A, SIG, A.conj())        # A sigma_nu A^dagger
    return 0.5 * np.einsum("mji,...nij->...mn", SIG, H).real


def lift(L4):
    """the inverse of phi, with a deterministic sign: the columns a1, a2 from H_0 +- H_3 and H_1 + i H_2, a1's
    largest component real and positive, then divided by sqrt(det) on the principal branch"""
    H = np.einsum("...mn,mij->...nij", L4, SIG)                          # H_nu = sum_mu Lambda^mu_nu sigma_mu
    P1 = (H[..., 0, :, :] + H[..., 3, :, :]) / 2
    K = (H[..., 1, :, :] + 1j * H[..., 2, :, :]) / 2
    d = np.stack([P1[..., 0, 0].real, P1[..., 1, 1].real], axis=-1)
    j = np.argmax(d, axis=-1)
    ar = np.arange(len(j))
    a1 = P1[ar, :, j] / np.sqrt(d[ar, j])[:, None]
    a2 = np.einsum("nji,nj->ni", K.conj(), a1) / np.einsum("ni,ni->n", a1.conj(), a1).real[:, None]
    A = np.stack([a1, a2], axis=-1)
    det = A[:, 0, 0] * A[:, 1, 1] - A[:, 0, 1] * A[:, 1, 0]
    return A / np.sqrt(det)[:, None, None]


def domain_with_lifts(name):
    M = snappy.Manifold(name)
    G = M.fundamental_group(simplify_presentation=False)
    gens, rels = G.generators(), G.relators()
    sols = []
    for signs in itertools.product((1, -1), repeat=len(gens)):
        sg = dict(zip(gens, signs))
        if all(np.abs(np.prod([sg[c.lower()] for c in r]) * mat(G.SL2C(r), 2) - np.eye(2)).max() < 1e-8
               for r in rels):
            sols.append(signs)
    D = M.dirichlet_domain(include_words=True)
    words = D.pairing_words()
    P = np.array([GS.to_np(m) for m in D.pairing_matrices()])
    sg = dict(zip(gens, sols[0])) if sols else None             # D0(a) asks for exactly one
    lifts = np.array([np.prod([sg[c.lower()] for c in w]) * mat(G.SL2C(w), 2) for w in words])
    A = phi(lifts)                                               # this script's convention
    K = np.vstack([np.kron(np.eye(4), b) - np.kron(a.T, np.eye(4)) for a, b in zip(A, P)])
    _, sv, vt = np.linalg.svd(K)
    C = vt[-1].reshape(4, 4).T                                   # P_i C = C phi(lift_i)
    conj_res = max(float(np.abs(C @ a - b @ C).max()) for a, b in zip(A, P)) / float(np.abs(C).max())
    _, P124, normals, info = GS.domain(name)
    info["out_radius"], info["volume"] = float(D.out_radius()), float(M.volume())
    same_domain = P124.shape == P.shape and float(np.abs(P124 - P).max()) < 1e-12
    e0 = np.array([1.0, 0, 0, 0])
    normals = P[:, :, 0] - e0
    info["spin sign solutions"] = [list(s) for s in sols]
    info["conjugation residual"] = conj_res
    info["the null space's next singular value"] = float(sv[-2])
    info["same domain as W124's"] = bool(same_domain)
    info["C"], info["Cinv"] = C, np.linalg.inv(C)
    return M, P, lifts, normals, info


def enumerate_axes_lifted(P, lifts, normals, r_out, Cj, Cjinv):
    """W124's enumerate_axes, unchanged, with each element's spin lift carried as one sign: the lift of an element
    with O(3,1) matrix X is sign * lift(Cjinv X Cj); a child's sign is read from its parent's lift times the pairing's
    lift (the sign's agreement is recorded)"""
    hol = lambda X: lift(np.einsum("ij,njk,kl->nil", Cjinv, X, Cj))
    worst = [0.0]
    rho_bfs, rho_keep = R + 3 * r_out, R + 2 * r_out
    cb, ck, cR, s2out = math.cosh(rho_bfs), math.cosh(rho_keep), math.cosh(R), math.sinh(r_out) ** 2
    cur = np.eye(4)[None]
    cur_s = np.ones(1, dtype=np.int8)
    cur_keys = GS.keys_of(cur)
    prev_keys = np.array([], dtype=np.int64)
    radii = []
    keep_l, keep_c, keep_w, keep_t = [], [], [], []
    visited, layers, empty_axes, bad = 1, 0, 0, 0
    kept_keys = []
    while len(cur):
        layers += 1
        c00 = cur[:, 0, 0]
        radii.append(np.arccosh(np.maximum(c00, 1.0)))
        sel = (c00 <= ck) & (c00 > 1.0 + 1e-9)
        G, Gs = cur[sel], cur_s[sel]
        if len(G):
            kept_keys.append(GS.keys_of(G))
            tr = np.trace(G, axis1=1, axis2=2)
            tr2 = np.einsum("nij,nji->n", G, G)
            s_, q_ = tr / 2, (tr2 + 4) / 4
            dlt = np.sqrt(np.maximum(2 * q_ - s_ ** 2, 0.0))
            ca, cb_ = (s_ + dlt) / 2, (s_ - dlt) / 2
            sh2 = (G[:, 0, 0] - ca) / np.maximum(ca - cb_, 1e-300)
            m = (ca <= cR) & (sh2 <= s2out * (1 + 1e-9) + 1e-12)
            G, Gs, ca, cb_ = G[m], Gs[m], ca[m], cb_[m]
            if len(G):
                ev, V = np.linalg.eig(G)
                imax, imin = np.argmax(np.abs(ev), axis=1), np.argmin(np.abs(ev), axis=1)
                ar = np.arange(len(G))
                vp = np.real(V[ar, :, imax])
                vm = np.real(V[ar, :, imin])
                vp *= np.sign(vp[:, :1])
                vm *= np.sign(vm[:, :1])
                pm = GS.lor(vp, vm)
                vm = vm / (2 * pm)[:, None]
                al = np.stack([GS.lor(vp, n) for n in normals], axis=1)
                be = np.stack([GS.lor(vm, n) for n in normals], axis=1)
                with np.errstate(divide="ignore", invalid="ignore"):
                    ratio = -be / al
                lo = np.where(al > 1e-14, ratio, -np.inf).max(axis=1)
                hi = np.where(al < -1e-14, ratio, np.inf).min(axis=1)
                blocked = ((np.abs(al) <= 1e-14) & (be < 0)).any(axis=1)
                lo = np.maximum(lo, 0.0)
                bad += int((~blocked & (((lo <= 0) & (hi > 0)) | ~np.isfinite(hi))).sum())
                ok = (~blocked) & (hi > lo) & (lo > 0) & np.isfinite(hi)
                length = np.where(ok, 0.5 * np.log(np.where(ok, hi / np.where(lo > 0, lo, 1), 1)), 0.0)
                empty_axes += int((length <= 0).sum())
                pos = length > 0
                keep_l.append(np.arccosh(np.maximum(ca[pos], 1.0)))
                keep_c.append(cb_[pos])
                keep_w.append(length[pos])
                keep_t.append(Gs[pos].astype(float) * np.trace(hol(G[pos]), axis1=1, axis2=2))
        nxt_m, nxt_s, nxt_k = [], [], []
        ng = len(P)
        for s0 in range(0, len(cur), 50000):
            chunk, chunk_s = cur[s0:s0 + 50000], cur_s[s0:s0 + 50000]
            C = np.einsum("nij,gjk->ngik", chunk, P).reshape(-1, 4, 4)
            f = np.nonzero(C[:, 0, 0] <= cb)[0]                 # the lifts are formed for survivors only
            C = C[f]
            if not len(C):
                continue
            k = GS.keys_of(C)
            new = ~GS.member(prev_keys, k) & ~GS.member(cur_keys, k)
            C, k, f = C[new], k[new], f[new]
            k, idx = np.unique(k, return_index=True)
            f = f[idx]
            Ck = C[idx]
            truth = chunk_s[f // ng].astype(float)[:, None, None] * np.einsum(
                "nij,njk->nik", hol(chunk[f // ng]), lifts[f % ng])
            Lc = hol(Ck)
            kk = np.argmax(np.abs(Lc).reshape(len(Lc), 4), axis=1)
            ratio = truth.reshape(len(Lc), 4)[np.arange(len(Lc)), kk] / Lc.reshape(len(Lc), 4)[np.arange(len(Lc)), kk]
            sgn = np.where(ratio.real >= 0, 1, -1).astype(np.int8)
            worst[0] = max(worst[0], float(np.abs(truth - sgn[:, None, None] * Lc).max()) if len(Lc) else 0.0)
            nxt_m.append(Ck)
            nxt_s.append(sgn)
            nxt_k.append(k)
            del C
        if not nxt_m:
            break
        nk = np.concatenate(nxt_k)
        nm = np.concatenate(nxt_m)
        ns = np.concatenate(nxt_s)
        nk, idx = np.unique(nk, return_index=True)
        prev_keys, cur_keys, cur, cur_s = cur_keys, nk, nm[idx], ns[idx]
        visited += len(cur)
    radii = np.concatenate(radii)
    allk = np.concatenate(kept_keys) if kept_keys else np.array([], dtype=np.int64)
    return {"ell": np.concatenate(keep_l), "cos": np.concatenate(keep_c), "w": np.concatenate(keep_w),
            "trace": np.concatenate(keep_t), "sign agreement (max |lift - sign * canonical|)": worst[0],
            "radii": radii, "visited": int(visited), "layers": layers,
            "empty axes": empty_axes, "unbounded flags": bad,
            "duplicate keys among kept": int(len(allk) - len(np.unique(allk)))}


# ---------------- the spinor sector ----------------
def spinor_sector(E, vol):
    ell, cs, wt, tr = E["ell"], E["cos"], E["w"], E["trace"]
    half = np.arccosh(tr / 2)                                  # (l + i theta~)/2, Re >= 0
    num = 2 * np.cos(half.imag)                                 # 2 cos(theta~/2), the spin structure's sign
    den = 2 * (np.cosh(ell) - cs)
    pref = W / math.sqrt(2 * math.pi)
    gau = pref * np.exp(-W ** 2 * ell ** 2 / 2) * wt / den
    geo = np.zeros(len(TGRID))
    for s0 in range(0, len(ell), 20000):
        cosT = np.cos(np.outer(TGRID, ell[s0:s0 + 20000]))
        geo += cosT @ (2 * gau[s0:s0 + 20000] * num[s0:s0 + 20000])
    c = 2 * W * math.sqrt(2 * math.pi)
    ident = vol / (2 * math.pi ** 2) * c * (TGRID ** 2 + W ** 2 + 0.25)
    o31 = 2 * np.cosh(ell) + 2 * cs                             # the O(3,1) trace; |tr of the lift|^2 should equal it
    checks = {"max | |tr|^2 - O(3,1) trace | / trace": float(np.max(np.abs(np.abs(tr) ** 2 - o31) / o31)),
              "max |2 Re(half) - l|": float(np.max(np.abs(2 * half.real - ell))),
              "max |cos(2 Im(half)) - cos(theta)|": float(np.max(np.abs(np.cos(2 * half.imag) - cs)))}
    return ident + geo, ident, checks


def lowest_bound(S, eps):
    G = lambda x: np.exp(-x ** 2 / (2 * W ** 2))
    for nu in np.arange(0.0, 4.0, 0.005):
        if np.all(G(TGRID - nu) + G(TGRID + nu) <= S + eps):
            return round(float(nu), 3)
    return None


# ---------------- the triplet's image group (exact) ----------------
def triplet_group():
    """rho = (e^{i pi/4} P, e^{i pi/4} L^-1) has every element of the form zeta8^k Q with Q a signed permutation
    matrix: elements are kept exactly as (k mod 8, Q), normalized so that Q's first non-zero entry is positive.
    The eigenvalues of zeta8^k Q are exact: a cycle of length c with sign product s gives the c-th roots of s."""
    from fractions import Fraction
    Pm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    Lm = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])

    def norm(k, Q):
        f = Q.flatten()
        if f[np.nonzero(f)[0][0]] < 0:
            return (k + 4) % 8, -Q
        return k % 8, Q

    def key(e):
        return (e[0], tuple(e[1].flatten()))

    def mul(a, b):
        return norm(a[0] + b[0], a[1] @ b[1])

    S_, T_ = norm(1, Pm), norm(1, Lm.T)
    gens = [S_, T_, norm(-1, Pm.T), norm(-1, Lm)]
    w8 = np.exp(1j * np.pi / 4)
    import the_higgs_route as HR                              # W123's matrices, for the identification
    ident = max(float(np.abs(w8 ** S_[0] * S_[1] - HR.rS).max()), float(np.abs(w8 ** T_[0] * T_[1] - HR.rT).max()))
    e = norm(0, np.eye(3, dtype=int))
    seen, frontier = {key(e): e}, [e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if key(y) not in seen:
                    seen[key(y)] = y
                    nxt.append(y)
        frontier = nxt

    def angles(x):
        k, Q = x
        perm = [int(np.nonzero(Q[:, j])[0][0]) for j in range(3)]       # column j goes to row perm[j]
        sign = [int(Q[perm[j], j]) for j in range(3)]
        done, out_ = set(), []
        for j0 in range(3):
            if j0 in done:
                continue
            cyc, j = [], j0
            while j not in done:
                done.add(j)
                cyc.append(j)
                j = perm[j]
            c, s = len(cyc), int(np.prod([sign[j] for j in cyc]))
            for t in range(c):
                out_.append((Fraction(t, c) + (Fraction(1, 2 * c) if s < 0 else 0) + Fraction(k, 8)) % 1)
        return out_

    orders = sorted({a.denominator for x in seen.values() for a in angles(x)})
    Linv = T_
    Lr = mul(mul(S_, norm(-1, Lm)), norm(-1, Pm.T))                   # L = S T^-1 S^-1
    lifts = {}
    for name, X in (("+LR", mul(Lr, Linv)), ("-LR", mul(mul(S_, S_), mul(Lr, Linv)))):
        for sgn, Y in (("+", X), ("-", norm(X[0] + 4, X[1]))):
            ang = angles(Y)
            lifts[f"{name} lift {sgn}"] = {"eigenvalue angles / 2pi": sorted(str(a) for a in ang),
                                          "m1": sum(1 for a in ang if a == 0)}
    return {"order": len(seen), "identified with W123's rho to": ident, "eigenvalue orders": orders,
            "any order divisible by 5": any(o % 5 == 0 for o in orders), "lifts of +-LR": lifts}


def main():
    t0 = time.time()
    tg = triplet_group()
    out["D5"] = tg
    say("D5 the triplet's image group: order", tg["order"],
        "| identified to %.1e" % tg["identified with W123's rho to"], "| eigenvalue orders", tg["eigenvalue orders"],
        "| any of order divisible by 5:", tg["any order divisible by 5"])
    for k, v in tg["lifts of +-LR"].items():
        say("   ", k, v)
    w124 = json.loads((HERE / "the_graviton_spectrum.json").read_text(encoding="utf-8"))["manifolds"]
    res = {}
    for label, name in (("Weeks", "m003(-3,1)"), ("Meyerhoff", "m004(5,1)")):
        M, P, lifts, normals, info = domain_with_lifts(name)
        say(label, "spin sign solutions", info["spin sign solutions"], "| conjugation residual %.1e" %
            info["conjugation residual"], "| same domain as W124's", info["same domain as W124's"])
        E = enumerate_axes_lifted(P, lifts, normals, info["out_radius"], info.pop("C"), info.pop("Cinv"))
        vol = info["volume"]
        S12, ident, chk = spinor_sector(E, vol)
        S, _, _ = GS.sectors(E, vol)
        N12 = GS.count(S12)
        s2_dev = float(np.max(np.abs(np.round(S[2], 5) - np.array(w124[label]["S on the grid"]["S2"]))))
        weyl = vol / math.pi ** 2 * (8 ** 3 / 3 + 8 / 4)
        r = {"info": info, "visited": E["visited"], "kept axes": int(len(E["ell"])),
             "W124 visited, kept axes": [w124[label]["visited"], w124[label]["kept axes"]],
             "max |S2 rounded - W124's stored S2|": s2_dev, "lift checks": chk,
             "duplicate keys among kept": E["duplicate keys among kept"], "unbounded flags": E["unbounded flags"],
             "sign agreement (max |lift - sign * canonical|)": E["sign agreement (max |lift - sign * canonical|)"],
             "S_1/2(0)": GS.at(S12, 0.0), "S_1/2 min": float(S12.min()),
             "S_1/2 min location": float(TGRID[int(np.argmin(S12))]),
             "N_1/2(8)": float(N12[800]), "Weyl at 8": weyl,
             "N_1/2 at 1,2,3,4,6,8": [round(float(N12[int(t * 100)]), 3) for t in (1, 2, 3, 4, 6, 8)],
             "peaks": GS.peaks(S12), "lowest |lambda_D| bound at eps 0, 0.01, 0.02":
             [lowest_bound(S12, e) for e in (0.0, 0.01, 0.02)],
             "S_1/2 on the grid": [round(float(v), 5) for v in S12]}
        res[label] = r
        del E, S, S12
        gc.collect()
        say(label, "visited", r["visited"], "kept", r["kept axes"], "(W124:", r["W124 visited, kept axes"], ")",
            "| S2 dev %.1e" % s2_dev, "| lift checks", {k: "%.1e" % v for k, v in chk.items()},
            "(%.0f s)" % (time.time() - t0))
        say(label, "S_1/2(0) %.4f | S_1/2 min %.4f at %.2f | N_1/2(8) %.2f vs Weyl %.2f" % (
            r["S_1/2(0)"], r["S_1/2 min"], r["S_1/2 min location"], r["N_1/2(8)"], weyl),
            "| peaks", r["peaks"], "| lowest |lambda| bound", r["lowest |lambda_D| bound at eps 0, 0.01, 0.02"])
    out["manifolds"] = res
    d0 = all(len(v["info"]["spin sign solutions"]) == 1 and v["info"]["conjugation residual"] < 1e-10
             and v["lift checks"]["max | |tr|^2 - O(3,1) trace | / trace"] < 1e-8
             and v["sign agreement (max |lift - sign * canonical|)"] < 1e-6
             and v["visited"] == v["W124 visited, kept axes"][0] and v["kept axes"] == v["W124 visited, kept axes"][1]
             and v["max |S2 rounded - W124's stored S2|"] <= 6e-6 for v in res.values())
    d1 = all(abs(v["N_1/2(8)"] - v["Weyl at 8"]) <= 0.25 * v["Weyl at 8"] for v in res.values())
    d2 = all(v["S_1/2 min"] >= -0.05 for v in res.values())
    d3 = res["Weeks"]["S_1/2(0)"] < 1.9
    d4 = res["Meyerhoff"]["S_1/2(0)"] < 1.9
    d5 = tg["identified with W123's rho to"] < 1e-12 and not tg["any order divisible by 5"]
    out["verdict"] = {"D0": bool(d0), "D1": bool(d1), "D2": bool(d2), "D3": bool(d3), "D4": bool(d4), "D5": bool(d5)}
    say("verdict", out["verdict"], "(%.0f s)" % (time.time() - t0))
    (HERE / "the_physical_readout.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    (HERE / "the_physical_readout_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
