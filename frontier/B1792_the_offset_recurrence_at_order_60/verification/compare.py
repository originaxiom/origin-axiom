"""B1792 comparison: B1741's sealed measure exactly, on this arc's census (the twenty slope-2/5 lines of exact order 60).
B1741's compare.py is loaded unchanged (as module 'b1741_compare'; its hash asserted) and only re-pointed: its census path to
this directory, its seeds to fresh ones (4501-4540: 160 000 random hierarchies), and its loader to the rows of one class or
line subset at a time.  Every feature, menu, sigma, random generator and chi-square is B1741's code.
THE PREDICTION (P-399; the SM seat's W164, sealed by main): the lines that carry the six -- a row with chi2_six (the seat's
menu) below 16.75 -- are exactly the +1/3 and +2/3 shifts of B1755's order-20 carriers (7/20, 1/4, 9/20, 3/20):
b = k/60 with k in {1, 7, 29, 35, 41, 47, 49, 55}.  Two decisive cells, named before the run and read apart:
  R_a: every one of the eight predicted lines carries the six;  R_b: none of the other twelve does.
Every other cell is a read-out, not a look.
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
C.SEEDS = list(range(4501, 4541))
APEXES = 125
TOTAL = 20
PREDICTED = {"1/60", "7/60", "29/60", "7/12", "41/60", "47/60", "49/60", "11/12"}
CLASSES = {"predicted": lambda r: r["b"] in PREDICTED, "other": lambda r: r["b"] not in PREDICTED, "all": lambda r: True}
COUNTS = {"predicted": 8, "other": 12, "all": 20}
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
    _use(cls="predicted"); A26 = C.arrays(C.B1726_CENSUS)
    ctrl["C2_chi2_six_seat_on_B1726"] = float(C.min_chi2(C.chi2_features("seat", False, C.B1726_CENSUS), A26["T6"][None, :])[0])
    plb = per_line_best()
    carriers = sorted(v["b"] for v in plb.values() if v["chi2_six_seat"] < 16.75)
    pred_carry = sorted(b for b in carriers if b in PREDICTED); other_carry = sorted(b for b in carriers if b not in PREDICTED)
    mirror = lambda b: str((Fr(3, 5) - Fr(b)) % 1)
    by_b = {v["b"]: v["chi2_six_seat"] for v in plb.values()}
    cells = {
        "R_a_DECISIVE_every_predicted_line_carries": len(pred_carry) == 8,
        "R_b_DECISIVE_no_other_line_carries": not other_carry,
        "readout_R_exact_recurrence": len(pred_carry) == 8 and not other_carry,
        "readout_predicted_specific_at_1pc": chi["predicted"]["six|seat"]["fraction_mean"] <= 0.01,
        "C1_control": ctrl["against_B1741_best_row"] < 1e-9 and ctrl["against_B1755_order_20_carriers"] < 1e-9 and ctrl["T_covariance_order_60"] < 1e-6 and ctrl["lines"] == 20 and ctrl["every_order_60"],
        "C2_control_chi2_reproduces_B1735": abs(ctrl["C2_chi2_six_seat_on_B1726"] - 3.0945633) < 1e-6,
    }
    out = {"apexes": APEXES, "counts": COUNTS, "predicted": sorted(PREDICTED), "seeds": S, "N": C.N, "chi2": chi, "best": best, "control": ctrl,
           "cells": cells, "carriers": carriers, "predicted_carrying": pred_carry, "other_carrying": other_carry,
           "readout_mirror_pairs": {b: [by_b[b], by_b[mirror(b)]] for b in sorted(by_b) if Fr(b) < Fr(mirror(b))},
           "readout_per_line": plb}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    for k, v in cells.items(): print(k, v)
    print("carriers", carriers)
    for name in CLASSES:
        for k in chi[name]: print("%-9s chi2 %-10s min %.2f, random as low %.5f (worst seed %.5f, hits %d)" % (name, k, chi[name][k]["min"], chi[name][k]["fraction_mean"], chi[name][k]["fraction_max"], chi[name][k]["hits"]))
    print("compare exit 0")


if __name__ == "__main__":
    main()
