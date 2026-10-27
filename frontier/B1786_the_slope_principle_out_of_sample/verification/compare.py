"""B1786 comparison: B1741's sealed measure exactly, on this arc's census (the lines of order 25 and 30), class by class:
the slope 2/5 (30 lines), the slope 1/10 (20 lines; the principle predicts it fails although its second-generation exponents
equal the slope 2/5's, B1785), every other line (538), and all 588.  B1741's compare.py is loaded unchanged (as module
'b1741_compare'; its hash asserted) and only re-pointed: its census path to this directory, its seeds to fresh ones
(1829-1868: 160 000 random hierarchies), and its loader to the rows of one class at a time.  Every feature, menu, sigma,
random generator and chi-square is B1741's code.  THE DECISIVE CELL, named before the run (one composite prediction of the
principle -- five-ality alignment with the Higgs at the unit twist, which selects the slope 2/5 alone): D = on the lines of
slope 2/5 at most 0.1% of random hierarchies reach as low a chi2_six (the seat's menu), AND no line of any other slope has a
row below 16.75 (the seat's menu).  P1 is its precondition; every other cell is a read-out, not a look.
    python3 -B compare.py [--workers 8]      # writes comparison.json (and prints the cells)
Importing loads B1741's module and computes nothing."""
import sys, json, math, random, hashlib, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SRC = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "compare.py"
SRC_SHA = "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"
if "b1741_compare" not in sys.modules:
    _spec = importlib.util.spec_from_file_location("b1741_compare", SRC)
    C = importlib.util.module_from_spec(_spec); sys.modules["b1741_compare"] = C; _spec.loader.exec_module(C)
C = sys.modules["b1741_compare"]
C.HERE = HERE
C.SEEDS = list(range(1829, 1869))
APEXES = 125
TOTAL = 588
CLASSES = {"a2/5": lambda r: r["alpha"] == "2/5", "a1/10": lambda r: r["alpha"] == "1/10", "rest": lambda r: r["alpha"] not in ("2/5", "1/10"), "all": lambda r: True}
COUNTS = {"a2/5": 30, "a1/10": 20, "rest": 538, "all": 588}
_F = {"cls": None, "subset": None}
_ROWS = {}                                  # each census parsed once per process


def _base(path):
    """the census as compact arrays, built once per process: per row and horocycle the logs B1741's loader takes, with the
    row's line and order"""
    key = str(path)
    if key not in _ROWS:
        lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
        rows = []
        with open(path, encoding="utf-8") as fh:
            for l in fh:
                if not l.strip(): continue
                r = json.loads(l); rec = {"line": r["line"], "order": r.get("order"), "alpha": r.get("alpha"), "Re_tau": r["Re_tau"], "Im_tau": r["Im_tau"], "h": {}}
                for h in ("L_max", "L_2"):
                    rec["h"][h] = ([lg(r[f"up|{h}|{a}"]) for a in C.RD], [lg(r[f"down|{h}|{a}"]) for a in C.RD], [lg(r[f"lep|{h}|{a}"]) for a in C.RD],
                                   [[lg(r[f"ckm|{h}|{a}|{b}"][:3]) for b in C.RD] for a in C.RD], [[r[f"ckm|{h}|{a}|{b}"][3] for b in C.RD] for a in C.RD])
                rows.append(rec)
        _ROWS[key] = rows
    return _ROWS[key]


def _load(path):
    """B1741's loader with one change: only the rows of the current class (or of a given line subset) are kept, and their
    count is asserted (125 apexes x the class's lines); the arithmetic on each row is B1741's"""
    assert hashlib.sha256(C.DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(C.CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; K = json.loads(C.CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    rows = _base(path)
    if pathlib.Path(path) == C.B1726_CENSUS:
        n = 23940
    else:
        assert len(rows) == APEXES * TOTAL == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
        if _F["subset"] is not None:
            rows = [r for r in rows if r["line"] in _F["subset"]]; n = APEXES * len(_F["subset"])
        else:
            rows = [r for r in rows if CLASSES[_F["cls"]](r)]; n = APEXES * COUNTS[_F["cls"]]
    assert len(rows) == n == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    rows = sorted(rows, key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
    U, Dn, E, Kk, Jm, lab = [], [], [], [], [], []
    for r in rows:
        for h in ("L_max", "L_2"):
            u, d, e, k, j = r["h"][h]
            U.append(u); Dn.append(d); E.append(e); Kk.append(k); Jm.append(j)
            lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
    C._A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), K=np.array(Kk), J=np.array(Jm), lab=lab, T6=T6,
                T9=np.concatenate([T6, np.log(np.array([K[0][1], K[1][2], K[0][2]]))]))


C._load = _load


def _use(cls=None, subset=None):
    key = (cls, tuple(sorted(subset)) if subset else None)
    if _F.get("key") != key:
        _F.update(cls=cls, subset=set(subset) if subset else None, key=key); C._A.clear()


def one_class(task):
    """(class, seed) -> B1741's one_chi2 on that class's rows"""
    name, seed = task
    _use(cls=name)
    return name, seed, C.one_chi2(seed)[1]


def lines_of(path):
    L = {}
    for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l); L[r["line"]] = (r["alpha"], r["b"], r["order"])
    return L


def subset_minima(n_subsets=200, seed=1786):
    """read-out (the random-subset control): the observed chi2_six (seat) minimum on random sets of 30 of the 588 lines
    (the size of the slope-2/5 class), against the class's own"""
    L = lines_of(HERE / "census.jsonl"); ids = sorted(L); rng = random.Random(seed); out = []
    for _ in range(n_subsets):
        s = rng.sample(ids, COUNTS["a2/5"]); _use(subset=s); A = C.arrays()
        out.append(float(C.min_chi2(C.chi2_features("seat", False), A["T6"][None, :])[0]))
    return out


def per_line_best():
    """read-out: the chi2_six (seat) minimum on each line, with its alpha, b and order"""
    L = lines_of(HERE / "census.jsonl"); res = {}
    for k in sorted(L):
        _use(subset=[k]); A = C.arrays()
        res[k] = {"alpha": L[k][0], "b": L[k][1], "order": L[k][2], "chi2_six_seat": float(C.min_chi2(C.chi2_features("seat", False), A["T6"][None, :])[0])}
    return res


def main():
    from multiprocessing import Pool
    assert hashlib.sha256(SRC.read_bytes()).hexdigest() == SRC_SHA
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    S = C.SEEDS
    with Pool(nw) as P:
        res = P.map(one_class, [(name, s) for name in CLASSES for s in S])
    chi = {}
    for name in CLASSES:
        per = {s: o for (nm, s, o) in res if nm == name}
        chi[name] = {k: {"min": per[S[0]][k][0], "fraction_mean": float(np.mean([per[s][k][1] for s in S])),
                         "fraction_max": float(np.max([per[s][k][1] for s in S])),
                         "hits": int(round(sum(per[s][k][1] * C.N for s in S)))} for k in per[S[0]]}
    best = {}
    for name in CLASSES:
        _use(cls=name); A = C.arrays()
        best[name] = {m: C.describe(A["T6"], m) for m in ("seat",)}
    ctrl = json.loads((HERE / "control.json").read_text(encoding="utf-8"))
    _use(cls="a2/5"); A26 = C.arrays(C.B1726_CENSUS)
    ctrl["C2_chi2_six_seat_on_B1726"] = float(C.min_chi2(C.chi2_features("seat", False, C.B1726_CENSUS), A26["T6"][None, :])[0])
    six = lambda name: chi[name]["six|seat"]
    six = lambda name: chi[name]["six|seat"]
    plb = per_line_best()
    other_below = sorted((v["chi2_six_seat"], v["alpha"], v["b"]) for v in plb.values() if v["alpha"] != "2/5" and v["chi2_six_seat"] < 16.75)
    cells = {
        "D_DECISIVE_slope_two_fifths_specific_at_0.1pc_and_no_other_slope_below_16.75": six("a2/5")["fraction_mean"] <= 0.001 and not other_below,
        "P1_chi2_six_below_16.75_on_slope_two_fifths": six("a2/5")["min"] < 16.75,
        "readout_slope_two_fifths_specific_at_1pc": six("a2/5")["fraction_mean"] <= 0.01,
        "readout_slope_one_tenth_below_16.75": six("a1/10")["min"] < 16.75,
        "readout_rest_specific_at_1pc": six("rest")["fraction_mean"] <= 0.01,
        "readout_nine_below_21.67_on_slope_two_fifths": chi["a2/5"]["nine|seat"]["min"] < 21.67,
        "C1_control": ctrl["against_B1741_best_row"] < 1e-9 and ctrl["against_B1749_best_row"] < 1e-9 and ctrl["T_covariance_order_25"] < 1e-6 and ctrl["line_counts"] == {"25": 300, "30": 288} and ctrl["every_order_exact"],
        "C2_control_chi2_reproduces_B1735": abs(ctrl["C2_chi2_six_seat_on_B1726"] - 3.0945633) < 1e-6,
    }
    sub = subset_minima()
    out = {"apexes": APEXES, "counts": COUNTS, "seeds": S, "N": C.N, "chi2": chi, "best": best, "control": ctrl, "cells": cells,
           "readout_random_30_line_subsets_chi2_six_seat": {"class_two_fifths": six("a2/5")["min"], "subsets": sub,
               "fraction_of_subsets_as_low": float(np.mean([x <= six("a2/5")["min"] + 1e-9 for x in sub]))},
           "other_slopes_below_16.75": other_below,
           "readout_per_line": plb}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    for k, v in cells.items(): print(k, v)
    for name in CLASSES:
        for k in chi[name]: print("%-6s chi2 %-10s min %.2f, random as low %.5f (worst seed %.5f, hits %d)" % (name, k, chi[name][k]["min"], chi[name][k]["fraction_mean"], chi[name][k]["fraction_max"], chi[name][k]["hits"]))
    print("compare exit 0")


if __name__ == "__main__":
    main()
