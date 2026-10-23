"""B1734 (P-312): the thread rule with the two ingredients, the census (no data).  For each of B1720's 121 thread classes
whose own fixed lines (B1733: the Smith rule) include lines of order 5 or 10, B1656's frame at B1667's canonical end
(both horocycles), the Higgs DR, at the thread's apex tau (B1720's, Im tau = Lagrange/2) and on each such line -- both
members of every order-5 pair {v, 2v}, so the bit is counted (B1733) -- every sector in S and S~ and the CKM for each
(up, down) pair, through B1726's sealed compute().  190 points (49 classes; 98 order-5, 92 order-10 lines).
    python3 -B census.py [--workers 8]      # writes census.json and control.json beside itself
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1720 = ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification" / "the_thread_census.json"


def _K():
    sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
    import census as K
    return K


def tasks():
    d = json.loads(B1720.read_text(encoding="utf-8")); out = []
    for ci, c in enumerate(d["classes"]):
        for li, (a, b) in enumerate(c["lines"]):
            a, b = Fr(a), Fr(b); N = math.lcm(a.denominator, b.denominator)
            if N in (5, 10): out.append((ci, li, c["word"], c["tau"][0], c["tau"][1], str(a), str(b), N))
    return out


def point(t):
    ci, li, w, re_t, im_t, a, b, N = t
    r = _K().compute(re_t, im_t, Fr(a), Fr(b)); r.update(cls=ci, line=li, word=w, Re_tau=re_t, Im_tau=im_t, a=a, b=b, order=N)
    return r


def control():
    """C1: the instrument reproduces B1720's stored rows (reading S for every sector, both horocycles) at its first three
    order-5/10 points to 1e-9 in log; and B1726's census control (against B1725's verified census, T-covariance)"""
    d = json.loads(B1720.read_text(encoding="utf-8")); rows = {(r["class"], r["line"]): r for r in d["rows"]}
    worst = 0.0
    for t in tasks()[:3]:
        mine = point(t); st = rows[(t[0], t[1])]
        for k in ("up|L_max|S", "down|L_max|S", "lep|L_max|S", "up|L_2|S", "down|L_2|S", "lep|L_2|S"):
            for p, q in zip(mine[k], st[k]):
                if p > 1e-10 and q > 1e-10: worst = max(worst, abs(math.log(p / q)))
    return {"against_B1720": worst, **{("B1726_" + k): v for k, v in _K().control().items()}}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    T = tasks()
    with Pool(nw) as P:
        rows = P.map(point, T, chunksize=4)
    json.dump({"points": len(T), "rows": rows}, open(HERE / "census.json", "w"))
    c = control(); json.dump(c, open(HERE / "control.json", "w"), indent=1)
    print(len(T), "points;", "control:", c)


if __name__ == "__main__":
    main()
