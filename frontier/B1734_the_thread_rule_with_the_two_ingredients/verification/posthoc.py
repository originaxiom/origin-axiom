"""B1734, POST HOC (written after comparison.json was read once, after the outputs commit d9f1b02dc; labelled; changes no
sealed cell; not covered by the seal).
  A  breadth: rows within 2 (seat's menu) by order and thread; the best six on order-10 lines alone (where D != 9)
  B  the restriction's cost: the full thread rule -- every thread's own lines of EVERY order (B1720's 3 249 points),
     through the same instrument, readings and menus -- best six and the fraction of random hierarchies as good
     (seat's and covariant menus; 5 seeds, 1734-1738), against the sealed 190-point restriction
  C  THE_BAR's Bonferroni over the four specificity looks
    python3 -B posthoc.py [--workers 8]      # writes posthoc.json and allorders.json beside itself"""
import sys, json, math, collections, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import importlib.util
import compare as C
_K = {}


def Kmod():
    """this arc's census.py, loaded under a name other than "census" (that name is B1726's module, which it imports);
    loaded lazily so that spawned workers load it too"""
    if not _K:
        spec = importlib.util.spec_from_file_location("b1734_census", HERE / "census.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _K["m"] = m
    return _K["m"]


def _point(t): return Kmod().point(t)


def allorders_tasks():
    d = json.loads(Kmod().B1720.read_text(encoding="utf-8")); out = []
    for ci, c in enumerate(d["classes"]):
        for li, (a, b) in enumerate(c["lines"]):
            a, b = Fr(a), Fr(b); N = math.lcm(a.denominator, b.denominator)
            out.append((ci, li, c["word"], c["tau"][0], c["tau"][1], str(a), str(b), N))
    return out


def seat_best(eu, ed, el, ek, menu, cs=(1, 3)):
    w = None
    for (a, b, l) in (C.SEAT if menu == "seat" else C.COV):
        for c in cs:
            x = np.maximum(np.maximum(eu[:, a], ed[:, b]), el[c][:, l])
            if ek is not None: x = np.maximum(x, ek[:, a, b])
            w = x if w is None else np.minimum(w, x)
    return w


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    out = {}
    A = C.arrays(); lab = A["lab"]; eu, ed, el, ek = C.errs(A["T6"])
    w6 = seat_best(eu, ed, el, None, "seat")
    idx = np.where(w6 <= math.log(2))[0]
    out["A_within_2_rows"] = int(len(idx))
    out["A_within_2_by_order"] = dict(collections.Counter(int(lab[i][2]) for i in idx))
    out["A_within_2_threads"] = sorted({lab[i][0] for i in idx})
    o10 = [i for i in range(len(lab)) if lab[i][2] == 10]
    j = min(o10, key=lambda i: w6[i]); out["A_best_six_order10"] = {"factor": math.exp(float(w6[j])), "row": list(lab[j])}
    # B: the full thread rule
    T = allorders_tasks()
    with Pool(nw) as P:
        rows = P.map(_point, T, chunksize=8)
    json.dump({"points": len(T), "rows": rows}, open(HERE / "allorders.json", "w"))
    lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    U, Dn, E = [], [], []
    for r in rows:
        for h in ("L_max", "L_2"):
            U.append([lg(r[f"up|{h}|{a}"]) for a in C.RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in C.RD]); E.append([lg(r[f"lep|{h}|{a}"]) for a in C.RD])
    U, Dn, E = np.array(U), np.array(Dn), np.array(E)
    def errs6(t):
        eu = np.max(np.abs(U - t[0:2]), axis=2); ed = np.max(np.abs(Dn - t[2:4]), axis=2)
        dm, de = E[:, :, 0] - t[4], E[:, :, 1] - t[5]
        el = {1: np.maximum(np.abs(dm), np.abs(de)), 3: np.maximum(np.abs(dm + C.LC3), np.abs(de - C.LC3))}
        return eu, ed, el
    res = {}
    for menu in ("seat", "cov"):
        e0 = errs6(A["T6"]); obs = float(np.min(seat_best(*e0, None, menu)))
        fr = []
        for seed in range(1734, 1739):
            d6, _ = C.draws(seed); hits = 0
            for t in d6:
                hits += float(np.min(seat_best(*errs6(t), None, menu))) <= obs + 1e-12
            fr.append(hits / len(d6))
        res[menu] = {"best_six": math.exp(obs), "fraction_mean_5_seeds": float(np.mean(fr)), "per_seed": fr}
    out["B_full_thread_rule_all_orders"] = {"points": len(T), "rows": 2 * len(T), **res}
    cmp = json.loads((HERE / "comparison.json").read_text())
    m = cmp["fraction_as_good_mean"]
    out["C_bonferroni_4"] = {k: min(1.0, 4 * m[k]) for k in ("six|seat", "six|cov", "six|free", "nine|seat")}
    json.dump(out, open(HERE / "posthoc.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
