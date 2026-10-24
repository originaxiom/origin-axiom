#!/usr/bin/env python3
"""W158 — the two-object route at the six's strip (the rule: W158_RULE.md, committed and pushed before this script).
It runs once, from the repository root.

H_u and H_d both on W152's 26 special lines (the squares of the 6 stabilizer, 8 F-type and 12 H-type magic states),
type II (the up sector's coupling from H_u, the down and lepton sectors' from H_d), each sector read as S_h or S~_h by
the seat's menu with c in {1, 3}, at every census row of B1749 and B1753 where the six pass the bar with the record's
Higgs.  The coupling is linear in S_h, so the script builds the three basis couplings per row and sector once (W138's
residues, norms and weighted M; W93's coupling).  The statistic is the least chi2_nine over the 676 ordered pairs; it is
priced by main's step-2 null (the data's six with random mixings) and by B1741's random nines, seeds 1809-1828.

  K0  the instrument: the 26 directions; basis couplings against direct ones; the record's DR against the census; the
      dictionary's basis against the frame's
  K1  the nine below 21.67 at the strip
  K2  specificity at 1% under both nulls (decisive only if K1 holds)
  R   read-outs: the best pair, the {stabilizer, H-type} subfamily, one Higgs on a special line, the record's DR

    python3 -B docs/dossiers/the_weave_2026-10-07/the_two_special_higgs.py
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

import mpmath as mp
import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_third_opinion_b1753 as W57    # noqa: E402  (W157: pins, rows below the bar; W156, W145 under it)
    import the_higgs_as_a_qubit as W52       # noqa: E402  (W152: the special states)
T8, T42 = W57.T8, W57.T42

REV = W57.REV
V49, V53 = W57.V49, W57.V53
FILES = (V49 + "/census.jsonl", V53 + "/census.jsonl", T8.HZ, T8.CKM, T8.COLUMN)
PIN = {V49 + "/census.jsonl": W57.PIN49[V49 + "/census.jsonl"], V53 + "/census.jsonl": W57.PIN[V53 + "/census.jsonl"]}
OUT = HERE / "the_two_special_higgs.json"
SEEDS = tuple(range(1809, 1829))
BAR6, BAR9 = 16.75, 21.67
LN3 = math.log(3)
UNIT = ("i", "j", "k")
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ the 26 directions
def directions():
    """h(psi) = to_xyz(Sym^2 psi) for W152's special states: (l1, l3, l7) = (-ab, a^2, -b^2), h = (l1, (l3 + l7)/2,
    (l7 - l3)/(2i)), the coefficients of the frame's units (CN_i, CN_j, CN_k)"""
    out = []
    for kind, bloch, st in W52.special_states():
        a, b = (complex(x.evalf(30)) for x in st)
        l1, l3, l7 = -a * b, a * a, -b * b
        h = np.array([l1, (l3 + l7) / 2, (l7 - l3) / 2j])
        out.append((kind, [str(x) for x in bloch], h / np.linalg.norm(h)))
    return out


def pdist(u, v):
    c = np.vdot(v, u) / np.vdot(v, v)
    return float(np.linalg.norm(u - c * v) / np.linalg.norm(u))


def fs_angle(u, v):
    x = abs(np.vdot(u, v)) / (np.linalg.norm(u) * np.linalg.norm(v))
    return float(math.degrees(math.acos(min(1.0, x))))


# ============================================================================================ a row's couplings
def basis(W93, W89, col, line, re_t, im_t, hor):
    """per sector: the basis couplings Y(CN_a) and Y(eps conj(CN_a) eps^T), a in (i, j, k)"""
    a, b = line
    tau = complex(re_t, im_t)
    out = {}
    for sec in T8.SECTS:
        R = T8.own_residues(W93, sec, a, b, tau)
        c = T8.own_norms(W89, W93, sec, a, b, tau, R)
        M = T8.weighted_M(W93, R, c, T8.L_at(col, im_t, hor))
        out[sec] = {"S": [W93.coupling_np(W93.CN[u], M) for u in UNIT],
                    "St": [W93.coupling_np(W93.EPSN @ np.conj(W93.CN[u]) @ W93.EPSN.T, M) for u in UNIT], "M": M}
    return out


def Y_of(B, sec, reading, h):
    if reading == "S":
        return sum(h[n] * B[sec]["S"][n] for n in range(3))
    return sum(np.conj(h[n]) * B[sec]["St"][n] for n in range(3))


def lefts(Y):
    U, sv, _ = np.linalg.svd(Y)
    return U[:, ::-1], sv


def ckm_from(Uu, Ud):
    V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]


def flog(x):
    return np.log(np.maximum(np.asarray(x, dtype=float), 1e-300))


# ============================================================================================ K0
def K0_directions(dirs):
    kinds = {}
    for k, _b, _h in dirs:
        kinds[k] = kinds.get(k, 0) + 1
    null = max(abs(np.sum(h * h)) for _k, _b, h in dirs)
    dmin = min(pdist(dirs[i][2], dirs[j][2]) for i in range(len(dirs)) for j in range(len(dirs)) if i < j)
    return {"by kind": kinds, "max |h.h|": null, "least projective distance between two": dmin}


def theta_R(tau):
    """R(tau) as W138's higgs_DR builds it, and to_xyz(Sym^2(Theta_2(2 tau), Theta_3(2 tau))), both by direct sums"""
    with mp.workdps(30):
        t = mp.mpc(tau.real, tau.imag)
        e = lambda m: mp.exp(1j * mp.pi * t * m)
        h = [mp.mpf(2 * n + 1) / 2 for n in range(-12, 12)]
        th2 = mp.fsum(e(x * x) for x in h)
        th3 = mp.fsum(e(n * n) for n in range(-12, 13))
        th4 = mp.fsum((-1) ** n * e(n * n) for n in range(-12, 13))
        R = np.array([complex(-th2 / (th3 * th4)), complex(-th4 / (th2 * th3)), complex(1j * th3 / (th2 * th4))])
        eps = mp.fsum(mp.exp(2j * mp.pi * t * x * x) for x in h)
        the = mp.fsum(mp.exp(2j * mp.pi * t * n * n) for n in range(-12, 13))
        a, b = complex(eps), complex(the)
        l1, l3, l7 = -a * b, a * a, -b * b
        hq = np.array([l1, (l3 + l7) / 2, (l7 - l3) / 2j])
    return R, hq


# ============================================================================================ main
def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W158", "rule": "W158_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
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
    dirs = directions()
    out["K0 (i)"] = K0_directions(dirs)
    # the strip's rows, by the criterion
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
    rng = np.random.default_rng(158)
    k0ii, k0iii, k0iv, dr_near = 0.0, {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0,
                                         "zero_pattern_mismatches": 0}, 0.0, []
    feats, meta = [], []
    cfgs = [(a, b, l, k) for (a, b, l) in T8.SEAT for k in (0.0, LN3)]
    for (name, k, x, y, hor) in rows_all:
        B = basis(W93, W89, col, L[k], x, y, hor)
        tau = complex(x, y)
        # K0 (ii): basis against direct, three random h
        for _ in range(3):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            S = sum(h[n] * W93.CN[UNIT[n]] for n in range(3))
            for sec in T8.SECTS:
                for rd, Sd in (("S", S), ("St", W93.EPSN @ np.conj(S) @ W93.EPSN.T)):
                    Yd = W93.coupling_np(Sd, B[sec]["M"])
                    k0ii = max(k0ii, float(np.linalg.norm(Y_of(B, sec, rd, h) - Yd) / np.linalg.norm(Yd)))
        # K0 (iii): the record's DR through the basis, against the stored census row
        hdr = np.array(T8.higgs_DR(tau))
        own = {}
        Ys = {}
        for sec in T8.SECTS:
            for rd in T8.RD:
                Ys[(sec, rd)] = Y_of(B, sec, rd, hdr)
                own[f"{sec}|{hor}|{rd}"] = T8.ratios(Ys[(sec, rd)])[0]
        for ru in T8.RD:
            for rdn in T8.RD:
                own[f"ckm|{hor}|{ru}|{rdn}"] = T8.ckm(Ys[("up", ru)], Ys[("down", rdn)])
        ref = {kk: v for kk, v in stored[(name, k, x, y)].items() if f"|{hor}|" in kk}
        dev = T8.compare_point(own, ref)
        for f in k0iii:
            k0iii[f] = k0iii[f] + dev[f] if f == "zero_pattern_mismatches" else max(k0iii[f], dev[f])
        # K0 (iv): the dictionary's basis
        R, hq = theta_R(tau)
        k0iv = max(k0iv, pdist(R, hq))
        # read-out: the record's DR against the 26
        ang = [(fs_angle(hdr, d[2]), d[0], d[1]) for d in dirs]
        a_min = min(ang)
        dr_near.append({"row": [name, k, x, y], "nearest special line": [a_min[1], a_min[2]],
                        "Fubini-Study angle, degrees": a_min[0]})
        # the menu at this row
        U = {}
        for i, (_kd, _bl, h) in enumerate(dirs):
            for rd in T8.RD:
                for sec in T8.SECTS:
                    Y = Y_of(B, sec, rd, h)
                    Ul, sv = lefts(Y)
                    U[(sec, rd, i)] = (Ul, flog([sv[1] / sv[0], sv[2] / sv[0]]) if sv[0] > 0 else flog([0, 0]))
        for iu in range(len(dirs)):
            for idn in range(len(dirs)):
                for (a, b, l, kk) in cfgs:
                    ru, rdn, rl = T8.RD[a], T8.RD[b], T8.RD[l]
                    Uu, lu = U[("up", ru, iu)]
                    Ud, ld = U[("down", rdn, idn)]
                    _Ul, ll = U[("lep", rl, idn)]
                    v = ckm_from(Uu, Ud)
                    f = np.concatenate([lu, ld, [ll[0] + kk, ll[1] - kk], flog(v[:3])])
                    feats.append(f / s9)
                    meta.append((len(dr_near) - 1, iu, idn, ru, rdn, rl, round(math.exp(kk)), v[3]))
    out["K0 (ii) basis against direct, max relative"] = k0ii
    out["K0 (iii) the record's DR against the census"] = k0iii
    out["K0 (iv) dictionary basis, max projective distance"] = k0iv
    X = np.array(feats)
    out["menu points"] = len(X)
    c2 = ((X - t9 / s9) ** 2).sum(1)
    i0 = int(np.argmin(c2))
    m = meta[i0]
    six = ((X[i0, :6] - t9[:6] / s9[:6]) ** 2).sum()
    out["K1"] = {"chi2_nine_min": float(c2[i0]), "below 21.67": bool(c2[i0] < BAR9),
                 "best": {"row": dr_near[m[0]]["row"], "H_u": [dirs[m[1]][0], dirs[m[1]][1]],
                          "H_d": [dirs[m[2]][0], dirs[m[2]][1]], "readings": [m[3], m[4], m[5]], "c": m[6],
                          "chi2_six part": float(six), "CKM part": float(c2[i0] - six), "J": m[7],
                          "model over measured (nine)": np.exp(X[i0] * s9 - t9).tolist()}}
    kinds = [d[0] for d in dirs]
    sub = [j for j, mm in enumerate(meta) if {kinds[mm[1]], kinds[mm[2]]} == {"stabilizer", "H"}]
    one = [j for j, mm in enumerate(meta) if mm[1] == mm[2]]
    out["R"] = {"{stabilizer, H-type} pairs, either order: chi2_nine min": float(c2[sub].min()),
                "one Higgs on a special line (H_u = H_d): chi2_nine min": float(c2[one].min()),
                "the record's DR at the rows": dr_near}
    # the nulls
    tree = cKDTree(X)
    obs = float(c2[i0])
    fa, fb = [], []
    for s in SEEDS:
        _six, nine = T8.own_draws(s, T8.NTARGET)
        N = np.array(nine)
        Ta = np.concatenate([np.tile(t6, (len(N), 1)), N[:, 6:9]], axis=1) / s9
        Tb = N / s9
        da = tree.query(Ta, k=1)[0] ** 2
        db = tree.query(Tb, k=1)[0] ** 2
        fa.append(float(np.mean(da <= obs + 1e-9)))
        fb.append(float(np.mean(db <= obs + 1e-9)))
    out["K2"] = {"null (a), the data's six with random mixings: fraction_mean": float(np.mean(fa)),
                 "null (b), random nines: fraction_mean": float(np.mean(fb)), "per seed (a)": fa, "per seed (b)": fb}
    k0 = out["K0 (i)"]
    out["cells"] = {
        "K0": bool(all(out["pins"].values()) and k0["by kind"] == {"stabilizer": 6, "F": 8, "H": 12}
                   and k0["max |h.h|"] < 1e-14 and k0["least projective distance between two"] > 1e-6
                   and k0ii < 1e-12 and max(k0iii["up"], k0iii["down"], k0iii["lep"], k0iii["ckm"]) < 1e-6
                   and k0iii["zero_pattern_mismatches"] == 0 and k0iv < 1e-10),
        "K1": out["K1"]["below 21.67"],
        "K2": bool(np.mean(fa) <= 0.01 and np.mean(fb) <= 0.01)}
    out["K2 decisive (K1 holds)"] = out["cells"]["K1"]


if __name__ == "__main__":
    main()
