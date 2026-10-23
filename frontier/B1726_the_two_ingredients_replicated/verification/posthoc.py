"""B1726, POST HOC (written after comparison.json was read once, after the outputs commit f1b7eb522; labelled; changes no
sealed cell; not covered by the seal).
A  the best six- and nine-rows recomputed at the census module's own precision (mpmath 40 digits, set by B1691's module)
   and at 15 digits
B  breadth: how many rows and points reach the seat menu's six within 2, 1.5, 1.3 and the nine within 2.5, and where
C  without the lepton factor: the seat's two readings with c = 1 only -- best six and the fraction as good (seed 1726)
D  the best six-row's grid neighbours (same line, Re tau, horocycle, configuration; Im tau +-0.1, +-0.2)
E  THE_BAR's Bonferroni over the four specificity cells, and the per-seed counts above 1%
F  the mixing at the best six-row (its own up and down readings)
    python3 -B posthoc.py        # writes posthoc.json beside itself"""
import sys, json, math, random, pathlib, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
V = HERE
sys.path.insert(0, str(V))
import compare as C
import census as K


def key_dev(x, y):
    d = 0.0
    for k in x:
        a, b = (x[k][:3], y[k][:3]) if k.startswith("ckm") else (x[k], y[k])
        for p, q in zip(a, b):
            if p > 1e-10 and q > 1e-10: d = max(d, abs(math.log(p / q)))
    return d


def stored(line, re_t, im_t):
    for l in (V / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["line"] == line and r["Re_tau"] == re_t and r["Im_tau"] == im_t: return r


def seat_row_errors(t, cs=(1, 3)):
    eu, ed, el, ek = C.errs(t)
    w = np.full(eu.shape[0], np.inf)
    for (a, b, l) in C.SEAT:
        for c in cs:
            x = np.maximum(np.maximum(eu[:, a], ed[:, b]), el[c][:, l])
            if ek is not None: x = np.maximum(x, ek[:, a, b])
            w = np.minimum(w, x)
    return w


def main():
    import mpmath as mp
    A = C.arrays(); cmp_ = json.loads((V / "comparison.json").read_text(encoding="utf-8")); out = {}
    # A
    resA = {}
    for name in ("best_six", "best_nine"):
        b = cmp_[name]["seat"]; a_, b_ = K.lines()[b["line"]]
        st = {k: v for k, v in stored(b["line"], b["Re_tau"], b["Im_tau"]).items() if "|" in k}
        K._modules(); mp.mp.dps = 40; hi = K.compute(b["Re_tau"], b["Im_tau"], a_, b_)
        mp.mp.dps = 15; lo = K.compute(b["Re_tau"], b["Im_tau"], a_, b_); mp.mp.dps = 40
        resA[name] = {"line": [str(a_), str(b_)], "order": int(np.lcm(a_.denominator, b_.denominator)),
                      "dps40_vs_stored": key_dev(hi, st), "dps15_vs_stored": key_dev(lo, st)}
    out["A_recompute"] = resA
    # B
    w6 = seat_row_errors(A["T6"]); w9 = seat_row_errors(A["T9"]); lab = A["lab"]
    def summ(w, thr):
        idx = np.where(w <= math.log(thr))[0]
        pts = {(lab[i][0], lab[i][1], lab[i][2]) for i in idx}
        return {"rows": int(len(idx)), "points": len(pts),
                "by_Re_tau": dict(sorted(collections.Counter(lab[i][1] for i in idx).items())),
                "by_order": dict(sorted(collections.Counter(int(np.lcm(K.lines()[lab[i][0]][0].denominator, K.lines()[lab[i][0]][1].denominator)) for i in idx).items())),
                "by_horocycle": dict(collections.Counter(lab[i][3] for i in idx)),
                "distinct_lines": len({lab[i][0] for i in idx}),
                "Im_tau_range": [min((lab[i][2] for i in idx), default=None), max((lab[i][2] for i in idx), default=None)]}
    out["B_breadth"] = {"six<=2": summ(w6, 2.0), "six<=1.5": summ(w6, 1.5), "six<=1.3": summ(w6, 1.3), "nine<=2.5": summ(w9, 2.5), "nine<=2": summ(w9, 2.0)}
    # C
    T6 = A["T6"]; w1 = seat_row_errors(T6, cs=(1,)); obs = float(np.min(w1)); i1 = int(np.argmin(w1))
    d6, _ = C.draws(1726)
    hits = sum(float(np.min(seat_row_errors(t, cs=(1,)))) <= obs + 1e-12 for t in d6)
    out["C_no_factor"] = {"best_six": math.exp(obs), "row": list(lab[i1]), "fraction_as_good_seed1726": hits / len(d6)}
    # D
    b = cmp_["best_six"]["seat"]; ai = {"S": 0, "St": 1}; (a, bb, l) = [ai[x] for x in b["readings"]]
    eu, ed, el, ek = C.errs(T6); c = 3 if b["lepton_factor"] == 3.0 else 1
    wcfg = np.maximum(np.maximum(eu[:, a], ed[:, bb]), el[c][:, l])
    nb = {}
    for i, L in enumerate(lab):
        if L[0] == b["line"] and L[1] == b["Re_tau"] and L[3] == b["horocycle"] and abs(L[2] - b["Im_tau"]) < 0.25:
            nb[str(L[2])] = math.exp(float(wcfg[i]))
    out["D_neighbours"] = dict(sorted(nb.items()))
    # E
    mean = cmp_["fraction_as_good_mean"]; per = cmp_["fraction_as_good_per_seed"]
    out["E_bar"] = {k: {"mean": mean[k], "bonferroni_4": min(1.0, 4 * mean[k]), "passes_0.01_after": 4 * mean[k] < 0.01,
                        "seeds_above_1pct": sum(per[s][k] > 0.01 for s in per)} for k in mean}
    # F
    i6 = [i for i, L in enumerate(lab) if L == (b["line"], b["Re_tau"], b["Im_tau"], b["horocycle"])][0]
    Vm = np.exp(A["K"][i6, a, bb]); Tc = np.exp(A["T9"][6:9])
    out["F_mixing_at_best_six"] = {"V_model": Vm.tolist(), "V_over_data": (Vm / Tc).tolist(), "J": float(A["J"][i6, a, bb])}
    json.dump(out, open(HERE / "posthoc.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
