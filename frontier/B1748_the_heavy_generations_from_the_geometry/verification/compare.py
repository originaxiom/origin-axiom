"""B1748 comparison: the heavy generations from the geometry alone (P-362), against the data and against random targets.
Features per census row: log m_c/m_t, log m_s/m_b, log(c * m_mu/m_tau), log |V_cb| for the menu (the null line n or its
conjugate n-bar) x (c = 1 or 3), on one horocycle at a time (L_max is the stated rule; L_2 the comparison).  Statistics:
the coarse worst factor (max |log model - log target|) and chi2_heavy (sigma^2 = the data's relative error^2 + 0.10^2,
B1720's definition), each minimised over rows and menu; calibrated by the fraction of random targets reaching as low over the
same rows and menu -- B1741's generators exactly (random hierarchies' second-generation entries r2 for c/t, s/b, mu/tau; random
mixings' middle entry for V_cb), 20 seeds 1748-1767, 4 000 targets each.
    python3 -B compare.py [--workers 8]      # writes comparison.json (and prints the cells)
Importing computes nothing."""
import sys, json, math, random, hashlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
SEEDS = list(range(1748, 1768)); N = 4000; ALLOW = 0.10; LC3 = math.log(3.0)
MENU = [(rd, c) for rd in ("n", "nbar") for c in (1.0, 3.0)]
BAR4 = 13.277                                     # the 99th percentile of chi-square with four degrees of freedom
_A = {}


def targets():
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    d = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]; v, e = d["value"], d["sigma"]
    C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]; cv, cs = C["value"], C["sigma"]
    T = np.log(np.array([v["c"] / v["t"], v["s"] / v["b"], v["mu"] / v["tau"], cv[1][2]]))
    rel = [math.hypot(e["c"] / v["c"], e["t"] / v["t"]), math.hypot(e["s"] / v["s"], e["b"] / v["b"]), math.hypot(e["mu"] / v["mu"], e["tau"] / v["tau"]), cs[1][2] / cv[1][2]]
    return T, np.sqrt(np.array(rel) ** 2 + ALLOW ** 2)


def arrays():
    if not _A:
        rows = [json.loads(l) for l in (HERE / "census.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        rows.sort(key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
        assert len(rows) == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
        for hor in ("L_max", "L_2"):
            X = []
            for rd, c in MENU:
                f = np.log(np.maximum(np.array([r[f"{hor}|{rd}"] for r in rows], dtype=float), 1e-300))
                f[:, 2] += math.log(c); X.append(f)
            _A[hor] = np.array(X)                  # (menu, rows, 4)
        _A["lab"] = [(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows]; _A["n"] = len(rows)
    return _A


def best(hor, t, sg):
    X = arrays()[hor]; worst = np.max(np.abs(X - t), axis=2); chi = (((X - t) / sg) ** 2).sum(axis=2)
    iw = np.unravel_index(np.argmin(worst), worst.shape); ic = np.unravel_index(np.argmin(chi), chi.shape)
    return float(np.exp(worst[iw])), iw, float(chi[ic]), ic


def draws(seed):
    rng = random.Random(seed); out = []
    for _ in range(N):
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2: break
            tg.append(r2)
        while True:
            a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a: break
        out.append(np.log(np.array(tg + [b])))
    return np.array(out)


def one(seed):
    T, sg = targets(); D = draws(seed); out = {}
    for hor in ("L_max", "L_2"):
        w0, _, c0, _ = best(hor, T, sg); X = arrays()[hor]
        hw = hc = 0
        for t in D:
            hw += float(np.exp(np.min(np.max(np.abs(X - t), axis=2)))) <= w0 + 1e-12
            hc += float(np.min((((X - t) / sg) ** 2).sum(axis=2))) <= c0 + 1e-9
        out[hor] = (hw / N, hc / N)
    return seed, out


def describe(hor, idx):
    A = arrays(); m, i = idx; rd, c = MENU[m]; T, sg = targets(); f = A[hor][m, i]
    return {"line": A["lab"][i][0], "Re_tau": A["lab"][i][1], "Im_tau": A["lab"][i][2], "horocycle": hor, "null line": rd, "lepton_factor": c,
            "model/data (c/t, s/b, mu/tau, V_cb)": [round(float(x), 4) for x in np.exp(f - T)], "chi2_heavy": float((((f - T) / sg) ** 2).sum())}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    T, sg = targets(); A = arrays(); res = {"rows": A["n"], "seeds": SEEDS, "N": N, "bar_chi2_4": BAR4}
    for hor in ("L_max", "L_2"):
        w, iw, c, ic = best(hor, T, sg); res[hor] = {"best_worst_factor": w, "best_by_factor": describe(hor, iw), "min_chi2_heavy": c, "best_by_chi2": describe(hor, ic)}
        chi = (((A[hor] - T) / sg) ** 2).sum(axis=2); good = np.argwhere(chi < BAR4)
        res[hor]["rows_below_bar"] = int(len({int(i) for _, i in good}))
        res[hor]["below_bar_Im_tau"] = sorted({round(A["lab"][int(i)][2], 4) for _, i in good})[:40]
    with Pool(nw) as P: per = dict(P.map(one, SEEDS))
    for hor in ("L_max", "L_2"):
        fw = [per[s][hor][0] for s in SEEDS]; fc = [per[s][hor][1] for s in SEEDS]
        res[hor].update(fraction_factor_mean=float(np.mean(fw)), fraction_factor_max=float(np.max(fw)), fraction_chi2_mean=float(np.mean(fc)), fraction_chi2_max=float(np.max(fc)))
    ctrl = json.loads((HERE / "control.json").read_text(encoding="utf-8")); M, L = res["L_max"], res["L_2"]
    res["cells"] = {
        "R1_heavy_within_1.25_Lmax": M["best_worst_factor"] <= 1.25,
        "R2_coarse_specific_Lmax": M["fraction_factor_mean"] <= 0.01,
        "P1_chi2_heavy_below_bar_Lmax": M["min_chi2_heavy"] < BAR4,
        "P2_precision_specific_Lmax": M["fraction_chi2_mean"] <= 0.01,
        "L1_L2_misses_the_bar": L["min_chi2_heavy"] >= BAR4,
        "L2_Lmax_more_specific_than_L2": M["fraction_chi2_mean"] < L["fraction_chi2_mean"],
        "C1_control": ctrl["C1_B1741_apex_reproduced_rel"] < 2e-3 and ctrl["C2_T_covariance"] < 1e-9}
    (HERE / "comparison.json").write_text(json.dumps(res, indent=1) + "\n")
    for k, v in res["cells"].items(): print(k, v)
    for hor in ("L_max", "L_2"):
        r = res[hor]
        print("%-5s best worst factor %.3f; min chi2_heavy %.2f (bar %.2f), rows below the bar %d; random as good: factor %.4f (worst seed %.4f), chi2 %.4f (worst seed %.4f)" % (
            hor, r["best_worst_factor"], r["min_chi2_heavy"], BAR4, r["rows_below_bar"], r["fraction_factor_mean"], r["fraction_factor_max"], r["fraction_chi2_mean"], r["fraction_chi2_max"]))
        print("      best by chi2:", r["best_by_chi2"])


if __name__ == "__main__":
    main()
