#!/usr/bin/env python3
"""W159 — the two-object route, tried again (the rule: W159_RULE.md, committed and pushed before this script).  It runs
once, from the repository root.

H_u = g_u DR and H_d = g_d DR: the record's own Higgs DR(tau) carried by the forced group on the qubit (W152's 24
elements, acting by S_h -> g S_h g^T), each image DR read at a modular image of tau and keeping DR's mixing; type II,
the seat's menu with c in {1, 3}, at W158's 38 strip rows (the census rows of B1749 and B1753 where the six pass with
the record's Higgs).  The couplings come from W158's basis couplings (linear in S_h).  The statistic is the least
chi2_nine over the 576 ordered pairs; it is priced by main's step-2 null and by random nines, seeds 1829-1848.  A
read-out scales the antipode's weight by lambda in {1.5, 2, 3, 4, 6}.

  K0  the group; the identity pair against the census; the images against DR at T- and S-images; the Takagi split
  K1  the nine below 21.67 at the strip
  K2  specificity at 1% under both nulls (decisive only if K1 holds)
  R   read-outs: the best pair, one Higgs, the record's pair, the least chi2_nine at each lambda, DR's invariant

    python3 -B docs/dossiers/the_weave_2026-10-07/the_higgs_orbit_pair.py
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
import traceback
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_two_special_higgs as W58      # noqa: E402  (W158: basis couplings, rows, pins; W157, W152 under it)
W57, W52, T8, T42 = W58.W57, W58.W52, W58.T8, W58.T42

REV = W58.REV
FILES, PIN = W58.FILES, W58.PIN
V49, V53 = W58.V49, W58.V53
OUT = HERE / "the_higgs_orbit_pair.json"
SEEDS = tuple(range(1829, 1849))
BAR6, BAR9 = 16.75, 21.67
LN3 = math.log(3)
LAMBDAS = (1.0, 1.5, 2.0, 3.0, 4.0, 6.0)
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ the group on directions
def lines(h):
    x, y, z = h
    return np.array([x, y - 1j * z, y + 1j * z])


def S_of(l):
    return np.array([[l[1], -l[0]], [-l[0], -l[2]]])


def lines_of_S(S):
    return np.array([-S[0, 1], S[0, 0], -S[1, 1]])


def xyz(l):
    return np.array([l[0], (l[1] + l[2]) / 2, (l[2] - l[1]) / 2j])


def act(g, h):
    return xyz(lines_of_S(g @ S_of(lines(h)) @ g.T))


def group():
    return [np.array([[complex(g[i][j]) for j in range(2)] for i in range(2)]) for g in W52.qubit_group()]


def as_np(m):
    return np.array([[complex(m[i][j]) for j in range(2)] for i in range(2)])


def invariant(h):
    return float(abs(np.sum(h * h)) / np.linalg.norm(h) ** 2)


def takagi(h):
    """S_h = c1 u1 u1^T + c2 u2 u2^T, u1 the top eigenvector of S S^H, u2 = j conj(u1); returns c1, c2, u1, u2"""
    S = S_of(lines(h))
    w, V = np.linalg.eigh(S @ np.conj(S.T))
    u1 = V[:, int(np.argmax(w))]
    u2 = np.array([-np.conj(u1[1]), np.conj(u1[0])])
    c1 = np.conj(u1) @ S @ np.conj(u1)
    c2 = np.conj(u2) @ S @ np.conj(u2)
    return c1, c2, u1, u2


def scaled(h, lam):
    c1, c2, u1, u2 = takagi(h)
    S = c1 * np.outer(u1, u1) + lam * c2 * np.outer(u2, u2)
    return xyz(lines_of_S(S))


# ============================================================================================ main
def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W159", "rule": "W159_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "machine": platform.machine()}
    try:
        run(root, out)
    except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
        out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


def run(root, out):
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    out["pins"] = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    W93, W89 = T8.own_modules(root)
    col = T8.L_column(files)
    L = T8.own_lines()
    G = group()
    ident = [i for i, g in enumerate(G) if abs(g[0, 1]) < 1e-12 and abs(g[1, 0]) < 1e-12
             and abs(g[0, 0] - g[1, 1]) < 1e-12]
    gT, gS = as_np(W52.G_T), as_np(W52.G_S)
    # the strip's rows, by W158's criterion
    rows_all, stored = [], {}
    for name, path in (("B1749", V49), ("B1753", V53)):
        rows = T8.census_rows(files[path + "/census.jsonl"])
        _arr, lab, best, _arg = W57.below_rows(rows, t6, sg)
        st = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
        for i in range(len(best)):
            if best[i] < BAR6:
                k, x, y, hor = lab[i]
                rows_all.append((name, k, x, y, hor))
                stored[(name, k, x, y)] = st[(k, x, y)]
    out["rows"] = len(rows_all)
    out["group order"] = len(G)
    out["identity elements"] = ident
    k0 = {"invariant spread max": 0.0, "identity pair against the census": {"up": 0.0, "down": 0.0, "lep": 0.0,
          "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}, "T-image against DR(tau + 1)": 0.0,
          "S-image against DR(-1/tau)": 0.0, "Takagi rebuild": 0.0, "I(lambda) formula": 0.0}
    cfgs = [(a, b, l, kk) for (a, b, l) in T8.SEAT for kk in (0.0, LN3)]
    feats = {lam: [] for lam in LAMBDAS}
    meta = []
    dr_info = []
    for ri, (name, k, x, y, hor) in enumerate(rows_all):
        tau = complex(x, y)
        B = W58.basis(W93, W89, col, L[k], x, y, hor)
        dr = np.array(T8.higgs_DR(tau))
        I0 = invariant(dr)
        imgs = [act(g, dr) for g in G]
        k0["invariant spread max"] = max(k0["invariant spread max"], max(abs(invariant(h) - I0) for h in imgs))
        # K0 (ii): the identity pair through the basis, against the stored census row
        own, Ys = {}, {}
        for sec in T8.SECTS:
            for rd in T8.RD:
                Ys[(sec, rd)] = W58.Y_of(B, sec, rd, dr)
                own[f"{sec}|{hor}|{rd}"] = T8.ratios(Ys[(sec, rd)])[0]
        for ru in T8.RD:
            for rdn in T8.RD:
                own[f"ckm|{hor}|{ru}|{rdn}"] = T8.ckm(Ys[("up", ru)], Ys[("down", rdn)])
        ref = {kk: v for kk, v in stored[(name, k, x, y)].items() if f"|{hor}|" in kk}
        dev = T8.compare_point(own, ref)
        d0 = k0["identity pair against the census"]
        for f in d0:
            d0[f] = d0[f] + dev[f] if f == "zero_pattern_mismatches" else max(d0[f], dev[f])
        # K0 (iii): the images are DR at modular images
        k0["T-image against DR(tau + 1)"] = max(k0["T-image against DR(tau + 1)"],
                                                W58.pdist(act(gT, dr), np.array(T8.higgs_DR(tau + 1))))
        k0["S-image against DR(-1/tau)"] = max(k0["S-image against DR(-1/tau)"],
                                               W58.pdist(act(gS, dr), np.array(T8.higgs_DR(-1 / tau))))
        # K0 (iv): the Takagi split and the scaled invariant
        c1, c2, u1, u2 = takagi(dr)
        S = S_of(lines(dr))
        reb = c1 * np.outer(u1, u1) + c2 * np.outer(u2, u2)
        k0["Takagi rebuild"] = max(k0["Takagi rebuild"], float(np.linalg.norm(reb - S) / np.linalg.norm(S)))
        r = abs(c2) / abs(c1)
        k0["I(lambda) formula"] = max(k0["I(lambda) formula"],
                                      abs(invariant(scaled(dr, 2.0)) - 4 * r / (1 + 4 * r * r)))
        sep = sorted({round(W58.fs_angle(dr, h), 3) for h in imgs})
        dr_info.append({"row": [name, k, x, y], "I(DR)": I0, "r": r, "separations from DR, degrees": sep[:4]})
        # the menu at this row, for each lambda
        for lam in LAMBDAS:
            base = dr if lam == 1.0 else scaled(dr, lam)
            hs = [act(g, base) for g in G]
            U = {}
            for gi, h in enumerate(hs):
                for rd in T8.RD:
                    for sec in T8.SECTS:
                        Ul, sv = W58.lefts(W58.Y_of(B, sec, rd, h))
                        U[(sec, rd, gi)] = (Ul, W58.flog([sv[1] / sv[0], sv[2] / sv[0]]) if sv[0] > 0
                                            else W58.flog([0, 0]))
            for iu in range(len(G)):
                for idn in range(len(G)):
                    for (a, b, l, kk) in cfgs:
                        ru, rdn, rl = T8.RD[a], T8.RD[b], T8.RD[l]
                        Uu, lu = U[("up", ru, iu)]
                        Ud, ld = U[("down", rdn, idn)]
                        _Ul, ll = U[("lep", rl, idn)]
                        v = W58.ckm_from(Uu, Ud)
                        f = np.concatenate([lu, ld, [ll[0] + kk, ll[1] - kk], W58.flog(v[:3])])
                        feats[lam].append(f / s9)
                        if lam == 1.0:
                            meta.append((ri, iu, idn, ru, rdn, rl, round(math.exp(kk)), v[3],
                                         W58.fs_angle(hs[iu], hs[idn])))
    out["K0"] = k0
    out["DR at the rows"] = dr_info
    X = np.array(feats[1.0])
    out["menu points"] = len(X)
    c2v = ((X - t9 / s9) ** 2).sum(1)
    i0 = int(np.argmin(c2v))
    m = meta[i0]
    six = float(((X[i0, :6] - t9[:6] / s9[:6]) ** 2).sum())
    out["K1"] = {"chi2_nine_min": float(c2v[i0]), "below 21.67": bool(c2v[i0] < BAR9),
                 "best": {"row": dr_info[m[0]]["row"], "g_u": m[1], "g_d": m[2], "readings": [m[3], m[4], m[5]],
                          "c": m[6], "J": m[7], "angle between H_u and H_d, degrees": m[8], "chi2_six part": six,
                          "CKM part": float(c2v[i0] - six),
                          "model over measured (nine)": np.exp(X[i0] * s9 - t9).tolist()}}
    one = [j for j, mm in enumerate(meta) if mm[1] == mm[2]]
    rec = [j for j, mm in enumerate(meta) if mm[1] in ident and mm[2] in ident]
    lam_min = {}
    for lam in LAMBDAS:
        Xl = np.array(feats[lam])
        lam_min[str(lam)] = float(((Xl - t9 / s9) ** 2).sum(1).min())
    out["R"] = {"one Higgs (g_u = g_d): chi2_nine min": float(c2v[one].min()),
                "the record's pair (identity, identity): chi2_nine min": float(c2v[rec].min()),
                "least chi2_nine at each lambda": lam_min}
    # the nulls, on the lambda = 1 menu
    tree = cKDTree(X)
    obs = float(c2v[i0])
    fa, fb = [], []
    for s in SEEDS:
        _six, nine = T8.own_draws(s, T8.NTARGET)
        N = np.array(nine)
        Ta = np.concatenate([np.tile(t6, (len(N), 1)), N[:, 6:9]], axis=1) / s9
        da = tree.query(Ta, k=1)[0] ** 2
        db = tree.query(N / s9, k=1)[0] ** 2
        fa.append(float(np.mean(da <= obs + 1e-9)))
        fb.append(float(np.mean(db <= obs + 1e-9)))
    out["K2"] = {"null (a), the data's six with random mixings: fraction_mean": float(np.mean(fa)),
                 "null (b), random nines: fraction_mean": float(np.mean(fb)), "per seed (a)": fa, "per seed (b)": fb}
    d0 = k0["identity pair against the census"]
    out["cells"] = {
        "K0": bool(all(out["pins"].values()) and len(G) == 24 and len(ident) == 1
                   and k0["invariant spread max"] < 1e-12
                   and max(d0["up"], d0["down"], d0["lep"], d0["ckm"]) < 1e-6 and d0["zero_pattern_mismatches"] == 0
                   and k0["T-image against DR(tau + 1)"] < 1e-10 and k0["S-image against DR(-1/tau)"] < 1e-10
                   and k0["Takagi rebuild"] < 1e-12 and k0["I(lambda) formula"] < 1e-12),
        "K1": out["K1"]["below 21.67"],
        "K2": bool(np.mean(fa) <= 0.01 and np.mean(fb) <= 0.01)}
    out["K2 decisive (K1 holds)"] = out["cells"]["K1"]


if __name__ == "__main__":
    main()
