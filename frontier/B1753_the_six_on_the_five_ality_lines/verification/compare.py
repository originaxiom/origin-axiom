"""B1753 comparison: B1741's sealed measure exactly, on this arc's fresh census (the five-ality lines).  B1741's compare.py is loaded unchanged
(as module 'b1741_compare') and only re-pointed: its census path to this directory, its seeds to fresh ones (1789-1808),
and its loader's row count to 10 704 (B1741's own loader asserts 19 950); every feature, menu, sigma, random generator,
chi-square and best-row description is B1741's code.  THE DECISIVE CELL, named before the run: P2 (the seat's menu, the
fraction of random hierarchies reaching as low a chi2_six, at most 0.1%).  P1 is its precondition; every other cell is a
read-out, not a look.
    python3 -B compare.py [--workers 8]      # writes comparison.json (and prints the cells)
Importing loads B1741's module and computes nothing."""
import sys, json, math, hashlib, pathlib, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SRC = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "compare.py"
SRC_SHA = "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"
if "b1741_compare" not in sys.modules:
    _spec = importlib.util.spec_from_file_location("b1741_compare", SRC)
    C = importlib.util.module_from_spec(_spec); sys.modules["b1741_compare"] = C; _spec.loader.exec_module(C)
C = sys.modules["b1741_compare"]
POINTS = 10704
C.HERE = HERE
C.SEEDS = list(range(1789, 1809))


def _load(path):
    """B1741's loader with one change: the row count asserted is 33 250 for this census (23 940 for B1726's, as B1741)"""
    assert hashlib.sha256(C.DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(C.CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; K = json.loads(C.CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    rows = [json.loads(l) for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]
    n = 23940 if pathlib.Path(path) == C.B1726_CENSUS else POINTS
    assert len(rows) == n == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    rows.sort(key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
    lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    U, Dn, E, Kk, Jm, lab = [], [], [], [], [], []
    for r in rows:
        for h in ("L_max", "L_2"):
            U.append([lg(r[f"up|{h}|{a}"]) for a in C.RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in C.RD])
            E.append([lg(r[f"lep|{h}|{a}"]) for a in C.RD])
            Kk.append([[lg(r[f"ckm|{h}|{a}|{b}"][:3]) for b in C.RD] for a in C.RD]); Jm.append([[r[f"ckm|{h}|{a}|{b}"][3] for b in C.RD] for a in C.RD])
            lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
    C._A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), K=np.array(Kk), J=np.array(Jm), lab=lab, T6=T6,
                T9=np.concatenate([T6, np.log(np.array([K[0][1], K[1][2], K[0][2]]))]))


C._load = _load


def main():
    from multiprocessing import Pool
    assert hashlib.sha256(SRC.read_bytes()).hexdigest() == SRC_SHA
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    A = C.arrays()
    best6 = {m: C.describe(A["T6"], m) for m in ("seat", "cov", "free")}
    best9 = {m: C.describe(A["T9"], m) for m in ("seat", "cov", "free")}
    with Pool(nw) as P:
        per = dict(P.map(C.one, C.SEEDS)); perc = dict(P.map(C.one_chi2, C.SEEDS))
    S = C.SEEDS
    mean = {k: float(np.mean([per[s][k] for s in S])) for k in per[S[0]]}
    chi = {k: {"min": perc[S[0]][k][0], "fraction_mean": float(np.mean([perc[s][k][1] for s in S])), "fraction_max": float(np.max([perc[s][k][1] for s in S]))} for k in perc[S[0]]}
    vud = C.vud_table()
    ctrl = json.loads((HERE / "control.json").read_text(encoding="utf-8"))
    A26 = C.arrays(C.B1726_CENSUS); ctrl["C2_chi2_six_seat_on_B1726"] = float(C.min_chi2(C.chi2_features("seat", False, C.B1726_CENSUS), A26["T6"][None, :])[0])
    cells = {
        "P2_DECISIVE_chi2_six_specific_seat_0.1pc": chi["six|seat"]["fraction_mean"] <= 0.001,
        "readout_P2_at_1pc": chi["six|seat"]["fraction_mean"] <= 0.01,
        "P1_chi2_six_below_16.75_seat": chi["six|seat"]["min"] < 16.75,
        "readout_R1_six_within_2_seat": best6["seat"]["best_factor"] <= 2.0,
        "readout_R2_six_specific_seat": mean["six|seat"] <= 0.01,
        "readout_R3_six_specific_cov": mean["six|cov"] <= 0.01,
        "readout_R4_six_specific_free": mean["six|free"] <= 0.01,
        "readout_R5_nine_specific_seat": mean["nine|seat"] <= 0.01,
        "readout_R7_D_within_3_sigma_at_best_six_seat": abs(best6["seat"]["D"] - C.D_TARGET) <= 3 * C.D_SIGMA,
        "readout_P2c_chi2_six_specific_cov": chi["six|cov"]["fraction_mean"] <= 0.01,
        "readout_P3_chi2_nine_below_21.67_seat": chi["nine|seat"]["min"] < 21.67,
        "readout_P4_chi2_nine_below_21.67_SM_reading": chi["nine|sm"]["min"] < 21.67,
        "C1_control": ctrl["against_B1741_best_row"] < 1e-9 and ctrl["against_B1726_row"] < 1e-9 and ctrl["T_covariance_at_a_fresh_apex"] < 1e-6,
        "C2_control_chi2_reproduces_B1735": abs(ctrl["C2_chi2_six_seat_on_B1726"] - 3.0945633) < 1e-6,
    }
    out = {"points": POINTS, "rows": len(A["lab"]), "seeds": S, "N": C.N, "J_PDG": C.J_PDG, "D_target": [C.D_TARGET, C.D_SIGMA],
           "best_six": best6, "best_nine": best9, "fraction_as_good_mean": mean, "fraction_as_good_per_seed": {str(s): per[s] for s in S},
           "chi2": chi, "chi2_per_seed": {str(s): perc[s] for s in S}, "Vud": vud, "control": ctrl, "cells": cells}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    for k, v in cells.items(): print(k, v)
    for k in sorted(mean): print("mean random as good %-10s %.4f" % (k, mean[k]))
    for k in chi: print("chi2 %-10s min %.2f, random as low %.4f (worst seed %.4f)" % (k, chi[k]["min"], chi[k]["fraction_mean"], chi[k]["fraction_max"]))


if __name__ == "__main__":
    main()
