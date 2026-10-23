"""B1741 (P-347): the sealed cells of tau from the thread rule with the line free, from census.jsonl (all 19 950 points:
75 apex points x 266 lines, both horocycles).  Main's coarse measure (the worst factor) and its calibration (B1695's
random hierarchies, B1713's random mixings); the precision cells of P-341 (chi2 at B1720 compare.py's definition, the
minimum over the rows and the menu, and the fraction of the same random targets reaching as low).  Means over seeds
1741-1760, 4 000 six-targets and 4 000 nine-targets each.  The menus (c multiplies m_mu/m_tau and divides m_e/m_tau):
    seat   {(S~, S, S), (S~, S~, S~)} x c in {1, 3}
    cov    every (up, down, lepton) assignment of S or S~ (8) x c in {1, 3}
    free   the seat's two reading rules, c continuous
    sm     the Standard Model's reading alone, (S~, S, S) x c in {1, 3}
    python3 -B compare.py [--workers 8]      # writes comparison.json beside itself
Importing computes nothing."""
import sys, json, math, random, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
J_PDG = 3.08e-5          # PDG's CKM review (2024 edition), J = (3.08 +0.15 -0.13) x 10^-5; an external constant, disclosed
D_TARGET, D_SIGMA = 10.58, 0.11     # P-094: (y_mu y_d)/(y_s y_e), Antusch, Hinze and Saad, eq. 4.7
RD = ("S", "St")
LC3 = math.log(3)
SEEDS = list(range(1741, 1761))
N = 4000
_A = {}
_CACHE = {}
B1726_CENSUS = ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.jsonl"


def arrays(path=None):
    """this arc's census by default; another committed census (B1726's, for control C2) when a path is given"""
    if path is not None:
        if path not in _CACHE:
            saved = dict(_A); _A.clear(); _load(path); _CACHE[path] = dict(_A); _A.clear(); _A.update(saved)
        return _CACHE[path]
    if not _A: _load(HERE / "census.jsonl")
    return _A


def _load(path):
    if True:
        assert hashlib.sha256(DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
        assert hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
        v = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
        T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
        rows = [json.loads(l) for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]
        n = 23940 if pathlib.Path(path) == B1726_CENSUS else 19950
        assert len(rows) == n == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
        rows.sort(key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
        lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
        U, Dn, E, K, Jm, lab = [], [], [], [], [], []
        for r in rows:
            for h in ("L_max", "L_2"):
                U.append([lg(r[f"up|{h}|{a}"]) for a in RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in RD])
                E.append([lg(r[f"lep|{h}|{a}"]) for a in RD])
                K.append([[lg(r[f"ckm|{h}|{a}|{b}"][:3]) for b in RD] for a in RD]); Jm.append([[r[f"ckm|{h}|{a}|{b}"][3] for b in RD] for a in RD])
                lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
        _A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), K=np.array(K), J=np.array(Jm), lab=lab, T6=T6,
                  T9=np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))]))


SEAT = ((1, 0, 0), (1, 1, 1))                                  # (up, down, lepton) reading indices: S~ = 1, S = 0
SM = ((1, 0, 0),)
ALLOW = 0.10


def sigmas():
    d = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]; v, e = d["value"], d["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    s6 = np.array([math.sqrt((e[a] / v[a]) ** 2 + (e[b] / v[b]) ** 2 + ALLOW ** 2) for a, b in pr])
    C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]; cv, cs = C["value"], C["sigma"]
    s3 = np.sqrt(np.array([cs[0][1] / cv[0][1], cs[1][2] / cv[1][2], cs[0][2] / cv[0][2]]) ** 2 + ALLOW ** 2)
    return s6, np.concatenate([s6, s3])


def chi2_features(menu, nine, path=None):
    """per configuration (and fixed c): the rows' features divided by sigma, and the map of targets to the same coordinates;
    chi2 = |X - t|^2 is expanded so a block of targets is one matrix product.  c free: the leptons enter as their sum."""
    A = arrays(path); s6, s9 = sigmas(); sg = s9 if nine else s6; out = []
    cfgs = {"seat": SEAT, "cov": COV, "free": SEAT, "sm": SM}[menu]
    for (a, b, l) in cfgs:
        base = [A["U"][:, a] / sg[0:2], A["Dn"][:, b] / sg[2:4]]
        tail = [A["K"][:, a, b] / sg[6:9]] if nine else []
        if menu == "free":
            s45 = math.sqrt(sg[4] ** 2 + sg[5] ** 2)
            X = np.concatenate(base + [((A["E"][:, l, 0] + A["E"][:, l, 1]) / s45)[:, None]] + tail, axis=1)
            f = lambda T, s45=s45: np.concatenate([T[:, 0:4] / sg[0:4], ((T[:, 4] + T[:, 5]) / s45)[:, None]] + ([T[:, 6:9] / sg[6:9]] if nine else []), axis=1)
            out.append((X, f))
        else:
            for k in (0.0, LC3):
                X = np.concatenate(base + [((A["E"][:, l, 0] + k) / sg[4])[:, None], ((A["E"][:, l, 1] - k) / sg[5])[:, None]] + tail, axis=1)
                out.append((X, lambda T: T / sg))
    return out


def min_chi2(F, T, block=400):
    best = np.full(len(T), np.inf)
    for X, f in F:
        x2 = (X ** 2).sum(1)
        for s0 in range(0, len(T), block):
            t = f(T[s0:s0 + block]); c = x2[:, None] - 2 * X @ t.T + (t ** 2).sum(1)[None, :]
            best[s0:s0 + block] = np.minimum(best[s0:s0 + block], c.min(0))
    return best


def one_chi2(seed):
    A = arrays(); d6, d9 = draws(seed); out = {}
    for name, T, ds, nine, menus in (("six", A["T6"], np.array(d6), False, ("seat", "cov", "free")), ("nine", A["T9"], np.array(d9), True, ("seat", "sm"))):  # the same menus as B1740
        for m in menus:
            F = chi2_features(m, nine); obs = float(min_chi2(F, T[None, :])[0])
            out["%s|%s" % (name, m)] = (obs, float(np.mean(min_chi2(F, ds) <= obs + 1e-9)))
    return seed, out


def vud_table():
    A = arrays(); out = {}
    for a in (0, 1):
        for b in (0, 1):
            k = np.exp(A["K"][:, a, b]); v = np.sqrt(np.clip(1 - k[:, 0] ** 2 - k[:, 2] ** 2, 0, None))
            out["up %s / down %s" % (RD[a], RD[b])] = {"median": float(np.median(v)), "q10": float(np.quantile(v, 0.1)), "q90": float(np.quantile(v, 0.9)), "fraction_above_0.9": float(np.mean(v > 0.9))}
    return out
COV = tuple((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))


def errs(t):
    A = arrays()
    eu = np.max(np.abs(A["U"] - t[0:2]), axis=2); ed = np.max(np.abs(A["Dn"] - t[2:4]), axis=2)
    dm, de = A["E"][:, :, 0] - t[4], A["E"][:, :, 1] - t[5]
    el = {1: np.maximum(np.abs(dm), np.abs(de)), 3: np.maximum(np.abs(dm + LC3), np.abs(de - LC3)), "free": np.abs(dm + de) / 2}
    ek = np.max(np.abs(A["K"] - t[6:9]), axis=3) if len(t) == 9 else None
    return eu, ed, el, ek


def best_over(t, menu, E=None):
    """(the best worst factor as a log, the row, the configuration) over the menu; E = errs(t) if already computed"""
    eu, ed, el, ek = E if E is not None else errs(t)
    cfgs = [(r, c) for r in (SEAT if menu in ("seat", "free") else COV) for c in (("free",) if menu == "free" else (1, 3))]
    best = (math.inf, None, None)
    for (a, b, l), c in cfgs:
        w = np.maximum(np.maximum(eu[:, a], ed[:, b]), el[c][:, l])
        if ek is not None: w = np.maximum(w, ek[:, a, b])
        i = int(np.argmin(w))
        if w[i] < best[0]: best = (float(w[i]), i, ((a, b, l), c))
    return best


def draws(seed):
    rng = random.Random(seed)
    def r_masses():
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2: break
            tg += [r2, r1]
        return tg
    def r_ckm():
        while True:
            a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a: return [a, b, c]
    d6 = [np.log(np.array(r_masses())) for _ in range(N)]
    d9 = [np.log(np.array(r_masses() + r_ckm())) for _ in range(N)]
    return d6, d9


def one(seed):
    A = arrays(); d6, d9 = draws(seed); out = {}
    for name, T, ds in (("six", A["T6"], d6), ("nine", A["T9"], d9)):
        ET = errs(T); obs = {m: best_over(T, m, ET)[0] for m in ("seat", "cov", "free")}
        hits = {m: 0 for m in obs}
        for t in ds:
            Et = errs(t)
            for m in obs: hits[m] += best_over(t, m, Et)[0] <= obs[m] + 1e-12
        for m in obs: out["%s|%s" % (name, m)] = hits[m] / len(ds)
    return seed, out


def describe(t, menu):
    A = arrays(); w, i, ((a, b, l), c) = best_over(t, menu)
    row = A["lab"][i]
    six = np.concatenate([A["U"][i, a], A["Dn"][i, b], A["E"][i, l]])
    cc = 3.0 if c == 3 else (1.0 if c == 1 else math.exp(((A["T6"][4] - six[4]) - (A["T6"][5] - six[5])) / 2))
    six = six + np.array([0, 0, 0, 0, math.log(cc), -math.log(cc)])
    D = math.exp(six[4] + six[3] - six[2] - six[5])                 # (m_mu m_d)/(m_s m_e) from the logs of the six
    return {"best_factor": math.exp(w), "line": row[0], "Re_tau": row[1], "Im_tau": row[2], "horocycle": row[3],
            "Vud": float(math.sqrt(max(0.0, 1 - math.exp(2 * A["K"][i, a, b][0]) - math.exp(2 * A["K"][i, a, b][2])))),
            "readings": [RD[a], RD[b], RD[l]], "lepton_factor": cc, "D": D, "J": float(A["J"][i, a, b]),
            "model_over_measured": np.exp(six - A["T6"]).tolist()}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    A = arrays()
    best6 = {m: describe(A["T6"], m) for m in ("seat", "cov", "free")}
    best9 = {m: describe(A["T9"], m) for m in ("seat", "cov", "free")}
    with Pool(nw) as P:
        per = dict(P.map(one, SEEDS)); perc = dict(P.map(one_chi2, SEEDS))
    mean = {k: float(np.mean([per[s][k] for s in SEEDS])) for k in per[SEEDS[0]]}
    chi = {k: {"min": perc[SEEDS[0]][k][0], "fraction_mean": float(np.mean([perc[s][k][1] for s in SEEDS])), "fraction_max": float(np.max([perc[s][k][1] for s in SEEDS]))} for k in perc[SEEDS[0]]}
    vud = vud_table()
    ctrl = json.loads((HERE / "control.json").read_text(encoding="utf-8"))
    A26 = arrays(B1726_CENSUS); ctrl["C2_chi2_six_seat_on_B1726"] = float(min_chi2(chi2_features("seat", False, B1726_CENSUS), A26["T6"][None, :])[0])
    cells = {
        "R1_six_within_2_seat": best6["seat"]["best_factor"] <= 2.0,
        "R2_six_specific_seat": mean["six|seat"] <= 0.01,
        "R3_six_specific_cov": mean["six|cov"] <= 0.01,
        "R4_six_specific_free": mean["six|free"] <= 0.01,
        "R5_nine_specific_seat": mean["nine|seat"] <= 0.01,
        "R6_J_within_3_at_best_nine_seat": abs(math.log(abs(best9["seat"]["J"]) / J_PDG)) <= math.log(3) if best9["seat"]["J"] != 0 else False,
        "R7_D_within_3_sigma_at_best_six_seat": abs(best6["seat"]["D"] - D_TARGET) <= 3 * D_SIGMA,
        "P1_chi2_six_below_16.75_seat": chi["six|seat"]["min"] < 16.75,
        "P2_chi2_six_specific_seat": chi["six|seat"]["fraction_mean"] <= 0.01,
        "P3_chi2_nine_below_21.67_seat": chi["nine|seat"]["min"] < 21.67,
        "P4_chi2_nine_below_21.67_SM_reading": chi["nine|sm"]["min"] < 21.67,
        "P2c_chi2_six_specific_cov": chi["six|cov"]["fraction_mean"] <= 0.01,
        "C1_control": ctrl["against_B1726_row"] < 1e-9 and ctrl["T_covariance_at_an_apex"] < 1e-6,
        "C2_control_chi2_reproduces_B1735": abs(ctrl["C2_chi2_six_seat_on_B1726"] - 3.0945633) < 1e-6,
    }
    out = {"points": 19950, "rows": len(A["lab"]), "seeds": SEEDS, "N": N, "J_PDG": J_PDG, "D_target": [D_TARGET, D_SIGMA],
           "best_six": best6, "best_nine": best9, "fraction_as_good_mean": mean, "fraction_as_good_per_seed": {str(s): per[s] for s in SEEDS},
           "chi2": chi, "chi2_per_seed": {str(s): perc[s] for s in SEEDS}, "Vud": vud, "control": ctrl, "cells": cells}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    for k, v in cells.items(): print(k, v)
    for k in sorted(mean): print("mean random as good %-10s %.4f" % (k, mean[k]))
    for k in chi: print("chi2 %-10s min %.2f, random as low %.4f (worst seed %.4f)" % (k, chi[k]["min"], chi[k]["fraction_mean"], chi[k]["fraction_max"]))
    for k in vud: print("|V_ud| %-16s median %.3f, above 0.9 %.3f" % (k, vud[k]["median"], vud[k]["fraction_above_0.9"]))
    print("best six (seat): %.3f at %s" % (best6["seat"]["best_factor"], {k: best6["seat"][k] for k in ("line", "Re_tau", "Im_tau", "horocycle", "readings", "lepton_factor", "D")}))


if __name__ == "__main__":
    main()
