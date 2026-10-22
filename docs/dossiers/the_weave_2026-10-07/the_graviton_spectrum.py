#!/usr/bin/env python3
"""W124 — the graviton spectrum of the ground-state universe (the script; `W124_RULE.md` was committed and pushed
before it).

- G1: the mode equation on the Milne cone, exact (sympy), for the TT family h = phi(z)(dx dy + dy dx) on the upper
  half-space.
- G0, G2-G7: for the Weeks manifold m003(-3,1) and the Meyerhoff manifold m004(5,1): the group enumerated breadth first
  from SnapPy's Dirichlet domain D (face pairings in O(3,1)); every element whose axis meets D, with l <= R, weighted
  by |axis cap D| (the unfolding identity); the trace formula in the scalar, coexact and TT sectors with the window
  h_T(t) = G(t - T) + G(t + T), G = exp(-t^2 / (2 w^2)), w = 4 / R.

    python3 -B the_graviton_spectrum.py      # writes the_graviton_spectrum.json and _run.txt beside itself
"""
import json
import math
import time
from pathlib import Path

import numpy as np
import snappy
import sympy as sp

HERE = Path(__file__).resolve().parent
out, log = {"arc": "W124", "rule": "W124_RULE.md"}, []
R = 6.0
W = 4.0 / R
TGRID = np.round(np.arange(0.0, 10.0 + 1e-9, 0.01), 2)
JL = np.diag([1.0, -1.0, -1.0, -1.0])
CS_WEEKS = [(27.8, 1), (32.9, 2), (43.0, 1), (59.7, 1), (66.3, 1), (67.6, 2), (69.7, 2), (84.4, 1), (90.5, 1),
            (93.9, 1), (97.8, 2), (106.9, 2), (109.4, 2), (116.6, 1), (118.3, 1), (127.3, 1), (132.8, 1),
            (137.7, 4), (145.2, 2), (149.6, 2), (160.0, 1), (163.8, 1), (175.5, 3), (186.0, 2), (190.9, 2),
            (192.6, 3), (194.1, 2), (209.5, 1), (215.3, 4), (221.8, 2), (226.9, 2), (229.6, 3), (241.6, 1),
            (247.6, 1), (250.3, 1), (253.6, 2), (256.4, 6), (261.2, 1), (264.3, 1), (268.8, 1), (276.2, 1),
            (280.6, 2)]          # Cornish and Spergel, arXiv math/9906017, Table III: (lambda, multiplicity)


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    log.append(s)


# ---------------- G1: the mode equation ----------------
def G1():
    tau, x, y, z, eps, a = sp.symbols("tau x y z epsilon a", positive=True)
    T = sp.Function("T")(tau)
    phi = z ** (a - 2)
    X3 = (x, y, z)
    g3 = sp.diag(1 / z ** 2, 1 / z ** 2, 1 / z ** 2)
    h3 = sp.zeros(3, 3)
    h3[0, 1] = h3[1, 0] = phi
    gi3 = g3.inv()
    Gam = [[[sum(gi3[i, l] * (sp.diff(g3[l, j], X3[k]) + sp.diff(g3[l, k], X3[j]) - sp.diff(g3[j, k], X3[l]))
                 for l in range(3)) / 2 for k in range(3)] for j in range(3)] for i in range(3)]
    # nabla_k h_ij, then nabla_l nabla_k h_ij, then the rough Laplacian -g^{kl} nabla_l nabla_k h_ij
    D1 = [[[sp.diff(h3[i, j], X3[k]) - sum(Gam[m][k][i] * h3[m, j] + Gam[m][k][j] * h3[i, m] for m in range(3))
            for k in range(3)] for j in range(3)] for i in range(3)]
    D2 = [[[[sp.diff(D1[i][j][k], X3[l]) - sum(Gam[m][l][i] * D1[m][j][k] + Gam[m][l][j] * D1[i][m][k]
                                               + Gam[m][l][k] * D1[i][j][m] for m in range(3))
             for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
    lap = sp.Matrix(3, 3, lambda i, j: sp.simplify(-sum(gi3[k, l] * D2[i][j][k][l]
                                                        for k in range(3) for l in range(3))))
    div = [sp.simplify(sum(gi3[k, i] * D1[i][j][k] for i in range(3) for k in range(3))) for j in range(3)]
    trace = sp.simplify(sum(gi3[i, j] * h3[i, j] for i in range(3) for j in range(3)))
    mu = sp.simplify(lap[0, 1] / phi)
    eigen = all(sp.simplify(lap[i, j] - mu * h3[i, j]) == 0 for i in range(3) for j in range(3))
    # the 4d metric and its Ricci tensor to first order in eps
    X4 = (tau, x, y, z)
    g4 = sp.diag(-1, tau ** 2 / z ** 2, tau ** 2 / z ** 2, tau ** 2 / z ** 2)
    g4[1, 2] = g4[2, 1] = eps * tau ** 2 * T * phi
    gi4 = g4.inv()
    G4 = [[[sum(gi4[i, l] * (sp.diff(g4[l, j], X4[k]) + sp.diff(g4[l, k], X4[j]) - sp.diff(g4[j, k], X4[l]))
                for l in range(4)) / 2 for k in range(4)] for j in range(4)] for i in range(4)]
    R1 = sp.zeros(4, 4)
    for b in range(4):
        for c in range(b, 4):
            e = sum(sp.diff(G4[q][b][c], X4[q]) - sp.diff(G4[q][b][q], X4[c])
                    + sum(G4[q][q][d] * G4[d][b][c] - G4[q][c][d] * G4[d][b][q] for d in range(4)) for q in range(4))
            R1[b, c] = R1[c, b] = sp.simplify(sp.diff(e, eps).subs(eps, 0))
    T0, T1, T2 = sp.symbols("T0 T1 T2")
    rxy = sp.expand(R1[1, 2].subs(sp.Derivative(T, (tau, 2)), T2).subs(sp.Derivative(T, tau), T1).subs(T, T0))
    c2, c1, c0 = (sp.simplify(rxy.coeff(s)) for s in (T2, T1, T0))
    others = [(i, j) for i in range(4) for j in range(i, 4) if (i, j) != (1, 2) and sp.simplify(R1[i, j]) != 0]
    ratio1, ratio0 = sp.simplify(c1 / c2), sp.simplify(c0 / c2)
    ok = (eigen and all(d == 0 for d in div) and trace == 0 and not others and c2 != 0
          and sp.simplify(ratio1 - 3 / tau) == 0 and sp.simplify(ratio0 - (mu - 2) / tau ** 2) == 0)
    return {"h traceless": trace == 0, "h divergence-free": all(d == 0 for d in div), "h an eigentensor": eigen,
            "mu(a)": str(mu), "Ric1_xy coefficients (T'', T', T)": [str(c2), str(c1), str(c0)],
            "T'/T'' ratio": str(ratio1), "T/T'' ratio": str(ratio0), "other Ric1 components non-zero": others,
            "holds": bool(ok)}


# ---------------- the enumeration ----------------
def to_np(m):
    return np.array([[float(m[i, j]) for j in range(4)] for i in range(4)])


def lor(u, v):
    return u[..., 0] * v[..., 0] - u[..., 1] * v[..., 1] - u[..., 2] * v[..., 2] - u[..., 3] * v[..., 3]


def keys_of(C):
    k = np.floor(C[:, 1:4, 0] / 0.05).astype(np.int64) + (1 << 20)
    return (k[:, 0] << 42) | (k[:, 1] << 21) | k[:, 2]


def member(sorted_keys, k):
    if not len(sorted_keys):
        return np.zeros(len(k), dtype=bool)
    i = np.minimum(np.searchsorted(sorted_keys, k), len(sorted_keys) - 1)
    return sorted_keys[i] == k


def domain(name):
    M = snappy.Manifold(name)
    D = M.dirichlet_domain()
    P = np.array([to_np(m) for m in D.pairing_matrices()])
    e0 = np.array([1.0, 0, 0, 0])
    lorentz = max(float(np.abs(p.T @ JL @ p - JL).max()) for p in P)
    centres = P[:, :, 0]
    normals = centres - e0                                   # D = {x : <x, n_i> >= 0}
    verts = []
    for v in D.vertex_list():
        v = np.array([float(c) for c in v])
        verts.append(np.concatenate([[1.0], v]) if len(v) == 3 else v)
    verts = np.array(verts)
    viol = float(min(0.0, min(float(lor(verts, n).min() / np.abs(verts).max()) for n in normals)))
    vh = verts / np.sqrt(np.maximum(lor(verts, verts), 1e-300))[:, None]
    vdist = float(np.arccosh(np.maximum(vh[:, 0], 1.0)).max())
    info = {"name": name, "volume": float(M.volume()), "homology": str(M.homology()), "faces": len(P),
            "in_radius": float(D.in_radius()), "out_radius": float(D.out_radius()),
            "O(3,1) defect": lorentz, "vertex inequality violation": viol, "max vertex distance": vdist}
    return M, P, normals, info


def enumerate_axes(P, normals, r_out):
    rho_bfs, rho_keep = R + 3 * r_out, R + 2 * r_out
    cb, ck, cR, s2out = math.cosh(rho_bfs), math.cosh(rho_keep), math.cosh(R), math.sinh(r_out) ** 2
    cur = np.eye(4)[None]
    cur_keys = keys_of(cur)
    prev_keys = np.array([], dtype=np.int64)
    radii = []
    keep_l, keep_c, keep_w = [], [], []
    visited, layers, empty_axes, bad = 1, 0, 0, 0
    kept_keys = []
    while len(cur):
        layers += 1
        # process the current layer
        c00 = cur[:, 0, 0]
        radii.append(np.arccosh(np.maximum(c00, 1.0)))
        sel = (c00 <= ck) & (c00 > 1.0 + 1e-9)
        G = cur[sel]
        if len(G):
            kept_keys.append(keys_of(G))
            tr = np.trace(G, axis1=1, axis2=2)
            tr2 = np.einsum("nij,nji->n", G, G)
            s_, q_ = tr / 2, (tr2 + 4) / 4
            dlt = np.sqrt(np.maximum(2 * q_ - s_ ** 2, 0.0))
            ca, cb_ = (s_ + dlt) / 2, (s_ - dlt) / 2              # cosh l, cos theta
            sh2 = (G[:, 0, 0] - ca) / np.maximum(ca - cb_, 1e-300)
            m = (ca <= cR) & (sh2 <= s2out * (1 + 1e-9) + 1e-12)
            G, ca, cb_ = G[m], ca[m], cb_[m]
            if len(G):
                ev, V = np.linalg.eig(G)
                imax, imin = np.argmax(np.abs(ev), axis=1), np.argmin(np.abs(ev), axis=1)
                ar = np.arange(len(G))
                vp = np.real(V[ar, :, imax])
                vm = np.real(V[ar, :, imin])
                vp *= np.sign(vp[:, :1])
                vm *= np.sign(vm[:, :1])
                pm = lor(vp, vm)
                vm = vm / (2 * pm)[:, None]
                al = np.stack([lor(vp, n) for n in normals], axis=1)
                be = np.stack([lor(vm, n) for n in normals], axis=1)
                with np.errstate(divide="ignore", invalid="ignore"):
                    ratio = -be / al
                lo = np.where(al > 1e-14, ratio, -np.inf).max(axis=1)
                hi = np.where(al < -1e-14, ratio, np.inf).min(axis=1)
                blocked = ((np.abs(al) <= 1e-14) & (be < 0)).any(axis=1)
                lo = np.maximum(lo, 0.0)
                bad += int((~blocked & (((lo <= 0) & (hi > 0)) | ~np.isfinite(hi))).sum())   # unbounded: none expected
                ok = (~blocked) & (hi > lo) & (lo > 0) & np.isfinite(hi)
                length = np.where(ok, 0.5 * np.log(np.where(ok, hi / np.where(lo > 0, lo, 1), 1)), 0.0)
                empty_axes += int((length <= 0).sum())
                pos = length > 0
                keep_l.append(np.arccosh(np.maximum(ca[pos], 1.0)))
                keep_c.append(cb_[pos])
                keep_w.append(length[pos])
        # expand to the next layer
        nxt_m, nxt_k = [], []
        for s0 in range(0, len(cur), 100000):
            chunk = cur[s0:s0 + 100000]
            C = np.einsum("nij,gjk->ngik", chunk, P).reshape(-1, 4, 4)
            C = C[C[:, 0, 0] <= cb]
            if not len(C):
                continue
            k = keys_of(C)
            new = ~member(prev_keys, k) & ~member(cur_keys, k)
            C, k = C[new], k[new]
            k, idx = np.unique(k, return_index=True)
            nxt_m.append(C[idx])
            nxt_k.append(k)
        if not nxt_m:
            break
        nk = np.concatenate(nxt_k)
        nm = np.concatenate(nxt_m)
        nk, idx = np.unique(nk, return_index=True)
        prev_keys, cur_keys, cur = cur_keys, nk, nm[idx]
        visited += len(cur)
    radii = np.concatenate(radii)
    allk = np.concatenate(kept_keys) if kept_keys else np.array([], dtype=np.int64)
    return {"ell": np.concatenate(keep_l), "cos": np.concatenate(keep_c), "w": np.concatenate(keep_w),
            "radii": radii, "visited": int(visited), "layers": layers, "empty axes": empty_axes,
            "unbounded flags": bad, "duplicate keys among kept": int(len(allk) - len(np.unique(allk)))}


# ---------------- the trace formula ----------------
def sectors(E, vol):
    ell, cs, wt = E["ell"], E["cos"], E["w"]
    th = np.arccos(np.clip(cs, -1, 1))
    den = 2 * (np.cosh(ell) - cs)
    weight = {0: np.ones_like(cs), 1: 2 * np.cos(th), 2: 2 * np.cos(2 * th)}
    pref = W / math.sqrt(2 * math.pi)
    geo = {m: np.zeros(len(TGRID)) for m in (0, 1, 2)}
    gau = pref * np.exp(-W ** 2 * ell ** 2 / 2) * wt / den
    for s0 in range(0, len(ell), 20000):
        cosT = np.cos(np.outer(TGRID, ell[s0:s0 + 20000]))
        for m in (0, 1, 2):
            geo[m] += cosT @ (2 * gau[s0:s0 + 20000] * weight[m][s0:s0 + 20000])
    c = 2 * W * math.sqrt(2 * math.pi)
    T2 = TGRID ** 2
    ident = {0: vol / (4 * math.pi ** 2) * c * (T2 + W ** 2), 1: vol / (2 * math.pi ** 2) * c * (T2 + W ** 2 + 1),
             2: vol / (2 * math.pi ** 2) * c * (T2 + W ** 2 + 4)}
    hT0 = 2 * np.exp(-T2 / (2 * W ** 2))                                   # h_T(0)
    hTi = 2 * np.exp(-(T2 - 1) / (2 * W ** 2)) * np.cos(TGRID / W ** 2)    # h_T(i), the constant mode
    S = {0: ident[0] + geo[0], 1: ident[1] + geo[1] + hT0, 2: ident[2] + geo[2]}
    return S, hTi, ident


def count(Sv):
    """N(T) = integral_0^T S / (w sqrt(2 pi)), trapezoid on the grid"""
    return np.concatenate([[0.0], np.cumsum((Sv[1:] + Sv[:-1]) / 2 * 0.01)]) / (W * math.sqrt(2 * math.pi))


def peaks(Sv, top=8.0, floor=0.3):
    res = []
    for i in range(1, len(TGRID) - 1):
        if TGRID[i] <= top and Sv[i] >= floor and Sv[i] >= Sv[i - 1] and Sv[i] > Sv[i + 1]:
            res.append([float(TGRID[i]), round(float(Sv[i]), 4)])
    return res


def first_cross(N, level=0.5):
    i = int(np.argmax(N >= level))
    return float(TGRID[i]) if N[i] >= level else None


def at(Sv, t):
    return float(Sv[int(round(t / 0.01))])


def main():
    t0 = time.time()
    out["parameters"] = {"R": R, "w": W, "grid": [0.0, 10.0, 0.01]}
    g1 = G1()
    out["G1"] = g1
    say("G1 mu(a) =", g1["mu(a)"], "| T'/T'' =", g1["T'/T'' ratio"], "| T/T'' =", g1["T/T'' ratio"],
        "| others", g1["other Ric1 components non-zero"], "->", g1["holds"], "(%.0f s)" % (time.time() - t0))

    res = {}
    for label, name in (("Weeks", "m003(-3,1)"), ("Meyerhoff", "m004(5,1)")):
        M, P, normals, info = domain(name)
        E = enumerate_axes(P, normals, info["out_radius"])
        vol = info["volume"]
        lat = {}
        for rho in (5.0, 6.0, 7.0):
            n = int((E["radii"] <= rho).sum())
            pred = math.pi * (math.sinh(2 * rho) - 2 * rho) / vol
            lat[str(rho)] = [n, round(pred, 1), round(n / pred, 4)]
        # the shortest geodesics: sum |axis cap D| against 2 x multiplicity x length (SnapPy, cutoff 1.5)
        short = []
        for g in M.length_spectrum(1.5):
            L0, mult = float(g["length"].real()), int(g["multiplicity"])
            sel = np.abs(E["ell"] - L0) < 1e-6
            short.append([round(L0, 8), mult, round(float(E["w"][sel].sum()), 8), round(2 * mult * L0, 8)])
        S, hTi, ident = sectors(E, vol)
        S0n = S[0] - hTi
        N0, N1, N2 = count(S0n), count(S[1]), count(S[2])
        res[label] = {"info": info, "visited": E["visited"], "layers": E["layers"], "kept axes": int(len(E["ell"])),
                      "empty axes": E["empty axes"], "unbounded flags": E["unbounded flags"],
                      "duplicate keys among kept": E["duplicate keys among kept"], "lattice counts": lat,
                      "shortest geodesics [l, mult, sum w, 2 mult l]": short,
                      "S0(0) and h0(i)": [at(S[0], 0.0), float(hTi[0])],
                      "S1 max on [0,1]": float(S[1][TGRID <= 1.0].max()), "S1(0)": at(S[1], 0.0),
                      "S1 min": float(S[1].min()), "S2 min": float(S[2].min()), "S2(0)": at(S[2], 0.0),
                      "scalar peaks": peaks(S0n), "coexact peaks": peaks(S[1]), "TT peaks": peaks(S[2]),
                      "N0 at 4,5,6,7,8": [round(float(N0[int(t * 100)]), 3) for t in (4, 5, 6, 7, 8)],
                      "N1 at 2,3,4,5,6,8": [round(float(N1[int(t * 100)]), 3) for t in (2, 3, 4, 5, 6, 8)],
                      "N2 at 2,3,4,5,6,8": [round(float(N2[int(t * 100)]), 3) for t in (2, 3, 4, 5, 6, 8)],
                      "N0 reaches 0.5 at": first_cross(N0), "N1 reaches 0.5 at": first_cross(N1),
                      "N2 reaches 0.5 at": first_cross(N2),
                      "Weyl TT at 8": vol / math.pi ** 2 * (8 ** 3 / 3 + 32),
                      "S on the grid": {"S0 minus constant": [round(float(v), 5) for v in S0n],
                                        "S1": [round(float(v), 5) for v in S[1]],
                                        "S2": [round(float(v), 5) for v in S[2]]}}
        r = res[label]
        say(label, info, "| visited", r["visited"], "| kept axes", r["kept axes"], "| lattice", lat,
            "| shortest", short[:4], "(%.0f s)" % (time.time() - t0))
        say(label, "S0(0) vs h0(i):", r["S0(0) and h0(i)"], "| S1 max[0,1] %.4f S1(0) %.4f S1 min %.4f | S2 min %.4f"
            % (r["S1 max on [0,1]"], r["S1(0)"], r["S1 min"], r["S2 min"]), "S2(0) %.4f" % r["S2(0)"])
        say(label, "TT peaks", r["TT peaks"], "| N2 reaches 0.5 at", r["N2 reaches 0.5 at"], "| N2(2..8)",
            r["N2 at 2,3,4,5,6,8"], "| Weyl at 8 %.2f" % r["Weyl TT at 8"])
        say(label, "scalar peaks", r["scalar peaks"], "| N0 reaches 0.5 at", r["N0 reaches 0.5 at"],
            "| coexact peaks", r["coexact peaks"])
        if label == "Weeks":
            rj = np.array([math.sqrt(l - 1) for l, _ in CS_WEEKS])
            mj = np.array([k for _, k in CS_WEEKS])
            Gf = lambda d: np.exp(-d ** 2 / (2 * W ** 2))
            Scs = sum(mm * (Gf(TGRID - r_) + Gf(TGRID + r_)) for r_, mm in zip(rj, mj))
            sel7 = TGRID <= 7.0
            r["Cornish-Spergel max |diff| on [0,7]"] = float(np.abs(S0n - Scs)[sel7].max())
            r["Cornish-Spergel diff at 4,5,6,7"] = [round(float((S0n - Scs)[int(t * 100)]), 4) for t in (4, 5, 6, 7)]
            say(label, "Cornish-Spergel max |diff| on [0,7]: %.4f" % r["Cornish-Spergel max |diff| on [0,7]"],
                r["Cornish-Spergel diff at 4,5,6,7"])
    out["manifolds"] = res
    wk, my = res["Weeks"], res["Meyerhoff"]
    g0 = all(v["info"]["vertex inequality violation"] > -1e-9 and v["info"]["max vertex distance"]
             <= v["info"]["out_radius"] + 1e-6 and v["duplicate keys among kept"] == 0
             and all(abs(x[2] - 1) <= 0.05 for x in v["lattice counts"].values()) for v in res.values())
    g2a = all(abs(v["S0(0) and h0(i)"][0] - v["S0(0) and h0(i)"][1]) <= 1e-3 * v["S0(0) and h0(i)"][1]
              for v in res.values())
    g2b = wk["Cornish-Spergel max |diff| on [0,7]"] <= 0.3
    g2c = my["N0 reaches 0.5 at"] is not None and 4.8 <= my["N0 reaches 0.5 at"] <= 5.6
    g3 = wk["S1 max on [0,1]"] <= 0.05 and my["S1(0)"] >= 1.0 and all(v["S1 min"] >= -0.05 for v in res.values())
    g4 = all(v["S2 min"] >= -0.05 for v in res.values())
    g5 = wk["N2 reaches 0.5 at"] is not None and 1.0 <= wk["N2 reaches 0.5 at"] <= 4.0
    g6 = all(abs(v["N2 at 2,3,4,5,6,8"][5] / v["Weyl TT at 8"] - 1) <= 0.25 for v in res.values())
    out["verdict"] = {"G0": bool(g0), "G1": g1["holds"], "G2": bool(g2a and g2b and g2c),
                      "G2 parts (a, b, c)": [bool(g2a), bool(g2b), bool(g2c)], "G3": bool(g3), "G4": bool(g4),
                      "G5": bool(g5), "G6": bool(g6)}
    say("verdict", out["verdict"], "(%.0f s)" % (time.time() - t0))
    (HERE / "the_graviton_spectrum.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    (HERE / "the_graviton_spectrum_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
