"""B1732, POST HOC (written after comparison.json was read once, after the outputs commit 5f5db8108; labelled; changes no
sealed cell; not covered by the seal).
  A  R6's base rate: over every row and every seat-menu CKM pair (up S~ with down S or S~), the fraction whose |J| lies
     within a factor 3 of PDG's 3.08e-5; and among rows whose nine fit within 4.5
  B  where the six (seat's menu) come within 2: rows, points, line orders
  C  B1726 against B1732 at the same rows: the best six under each menu, side by side
    python3 -B posthoc.py      # writes posthoc.json beside itself"""
import sys, json, math, collections, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compare as C, census as K


def main():
    A = C.arrays(); lab = A["lab"]; out = {}
    J = np.abs(A["J"]); win = np.abs(np.log(np.maximum(J, 1e-300) / C.J_PDG)) <= math.log(3)
    seat_pairs = [(1, 0), (1, 1)]
    w = np.concatenate([win[:, a, b] for a, b in seat_pairs])
    eu, ed, el, ek = C.errs(A["T9"])
    nine = np.concatenate([np.maximum.reduce([eu[:, a], ed[:, b], np.minimum(el[1][:, b], el[3][:, b]), ek[:, a, b]]) for a, b in seat_pairs])
    out["A_J_within_3_all_rows"] = float(w.mean())
    out["A_J_within_3_rows_nine_within_4.5"] = float(w[nine <= math.log(4.5)].mean()) if (nine <= math.log(4.5)).any() else None
    out["A_rows_nine_within_4.5"] = int((nine <= math.log(4.5)).sum())
    eu6, ed6, el6, _ = C.errs(A["T6"]); best = np.full(len(lab), np.inf)
    for (a, b, l) in C.SEAT:
        for c in (1, 3): best = np.minimum(best, np.maximum(np.maximum(eu6[:, a], ed6[:, b]), el6[c][:, l]))
    idx = np.where(best <= math.log(2))[0]
    order = lambda k: math.lcm(K.lines()[k][0].denominator, K.lines()[k][1].denominator)
    out["B_six_within_2_rows"] = int(len(idx)); out["B_six_within_2_points"] = len({lab[i][:3] for i in idx})
    out["B_by_order"] = dict(sorted(collections.Counter(order(lab[i][0]) for i in idx).items()))
    b26 = json.loads((HERE.parents[1] / "B1726_the_two_ingredients_replicated" / "verification" / "comparison.json").read_text())
    b32 = json.loads((HERE / "comparison.json").read_text())
    out["C_best_six"] = {m: {"B1726_DR": round(b26["best_six"][m]["best_factor"], 3), "B1732_F6": round(b32["best_six"][m]["best_factor"], 3)} for m in ("seat", "cov", "free")}
    out["C_fraction_as_good"] = {k: {"B1726_DR": b26["fraction_as_good_mean"][k], "B1732_F6": b32["fraction_as_good_mean"][k]} for k in b32["fraction_as_good_mean"]}
    json.dump(out, open(HERE / "posthoc.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
