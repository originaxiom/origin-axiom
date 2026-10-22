"""B1726: the sealed cells of main's replication of the two-ingredient result, from census.jsonl (all 23 940 points
required).  Main's measure of fit (the worst factor max |ln(model/target)|, minimised over rows and the menu), main's
calibration priors (B1695's random hierarchies, B1713's random mixings), and for each menu the fraction of random targets
whose own best over the same rows and the same menu is at most the data's; the cells use the mean over seeds 1726-1745
(4 000 six-targets and 4 000 nine-targets each).  The menus (the lepton factor c multiplies m_mu/m_tau and divides
m_e/m_tau; the CKM comes from the configuration's up and down readings):
    seat   {(S~, S, S), (S~, S~, S~)} x c in {1, 3}       -- the four configurations the web seat compared
    cov    every (up, down, lepton) assignment of S or S~ (8) x c in {1, 3}
    free   the seat's two reading rules, c continuous     -- only m_mu m_e / m_tau^2 constrained
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
SEEDS = list(range(1726, 1746))
N = 4000
_A = {}


def arrays():
    if not _A:
        assert hashlib.sha256(DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
        assert hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
        v = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
        T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
        rows = [json.loads(l) for l in (HERE / "census.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        assert len(rows) == 23940 == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
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
    return _A


SEAT = ((1, 0, 0), (1, 1, 1))                                  # (up, down, lepton) reading indices: S~ = 1, S = 0
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
            "readings": [RD[a], RD[b], RD[l]], "lepton_factor": cc, "D": D, "J": float(A["J"][i, a, b]),
            "model_over_measured": np.exp(six - A["T6"]).tolist()}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    A = arrays()
    best6 = {m: describe(A["T6"], m) for m in ("seat", "cov", "free")}
    best9 = {m: describe(A["T9"], m) for m in ("seat", "cov", "free")}
    with Pool(nw) as P:
        per = dict(P.map(one, SEEDS))
    mean = {k: float(np.mean([per[s][k] for s in SEEDS])) for k in per[SEEDS[0]]}
    ctrl = json.loads((HERE / "control.json").read_text(encoding="utf-8"))
    cells = {
        "R1_six_within_2_seat": best6["seat"]["best_factor"] <= 2.0,
        "R2_six_specific_seat": mean["six|seat"] <= 0.01,
        "R3_six_specific_cov": mean["six|cov"] <= 0.01,
        "R4_six_specific_free": mean["six|free"] <= 0.01,
        "R5_nine_specific_seat": mean["nine|seat"] <= 0.01,
        "R6_J_within_3_at_best_nine_seat": abs(math.log(abs(best9["seat"]["J"]) / J_PDG)) <= math.log(3) if best9["seat"]["J"] != 0 else False,
        "R7_D_within_3_sigma_at_best_six_seat": abs(best6["seat"]["D"] - D_TARGET) <= 3 * D_SIGMA,
        "C1_control": ctrl["against_B1725"] < 1e-9 and ctrl["T_covariance"] < 1e-6,
    }
    out = {"points": 23940, "rows": len(A["lab"]), "seeds": SEEDS, "N": N, "J_PDG": J_PDG, "D_target": [D_TARGET, D_SIGMA],
           "best_six": best6, "best_nine": best9, "fraction_as_good_mean": mean, "fraction_as_good_per_seed": {str(s): per[s] for s in SEEDS},
           "control": ctrl, "cells": cells}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    for k, v in cells.items(): print(k, v)
    for k in sorted(mean): print("mean random as good %-10s %.4f" % (k, mean[k]))
    print("best six (seat): %.3f at %s" % (best6["seat"]["best_factor"], {k: best6["seat"][k] for k in ("line", "Re_tau", "Im_tau", "horocycle", "readings", "lepton_factor", "D")}))


if __name__ == "__main__":
    main()
