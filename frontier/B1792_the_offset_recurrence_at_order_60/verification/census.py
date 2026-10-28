"""B1792 census: the offset recurrence at order 60 (P-399; the SM seat's W164 prediction, sealed by main).  At B1749's 125 apex
points (loaded from B1749's sealed census module), on the twenty slope-2/5 flat lines of exact order 60 (b = k/60 with
gcd(k, 6) = 1), B1726's sealed compute() exactly as B1741 calls it (B1656's frame at B1667's end, both horocycles, the Higgs
DR, every sector in S and S~, the CKM for each (up, down) pair).  2 500 points.  No line of order 60 has been computed on the
record before this census.  Checkpointed (resumable).
    python3 -B census.py [--workers 8]      # writes census.jsonl, control.json; prints "census exit 0"
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "census.jsonl"
ORDERS = (60,)
ALPHA = Fr(2, 5)
_C = {}


def _load(name, rel):
    if name not in sys.modules:
        import importlib.util
        sp = importlib.util.spec_from_file_location(name, ROOT / rel)
        m = importlib.util.module_from_spec(sp); sys.modules[name] = m; sp.loader.exec_module(m)
    return sys.modules[name]


def _K():
    """B1726's sealed census module (its compute), under its own name"""
    return _load("b1726_census", "frontier/B1726_the_two_ingredients_replicated/verification/census.py")


def apexes():
    """B1749's 125 apex points, from B1749's sealed census module (its apexes(), unchanged)"""
    return _load("b1749_census", "frontier/B1749_the_six_at_fresh_apexes/verification/census.py").apexes()


def lines():
    """the twenty slope-2/5 lines of exact order 60, b = k/60 in increasing k (each is its own key under B1726's sign
    identification, since 2/5 < 3/5)"""
    out = []
    for k in range(60):
        b = Fr(k, 60)
        if math.lcm(ALPHA.denominator, b.denominator) == 60:
            key = min((ALPHA, b), ((-ALPHA) % 1, (-b) % 1)); assert key == (ALPHA, b); out.append(key)
    return out


def order(line):
    a, b = line
    return math.lcm(Fr(a).denominator, Fr(b).denominator)


def tasks():
    L = lines()
    return [(pi, p["Re_tau"], p["Im_tau"], k) for pi, p in enumerate(apexes()) for k in range(len(L))]


def point(t):
    pi, re, im, k = t
    a, b = lines()[k]
    r = _K().compute(re, im, a, b)
    r.update(apex=pi, words=apexes()[pi]["words"], line=k, alpha=str(a), b=str(b), order=order((a, b)), Re_tau=re, Im_tau=im)
    return r


def control():
    """C1: (i) B1741's stored best row reproduced by this instrument; (ii) B1755's stored rows on its four order-20 carriers
    (7/20, 1/4, 9/20, 3/20) at B1749's middle apex reproduced; (iii) B1724's T-law on (2/5, 1/60) at B1749's middle apex;
    (iv) twenty lines, every one of exact order 60"""
    K = _K(); L26 = K.lines()
    def dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    def row(path, pred):
        for l in path.read_text(encoding="utf-8").splitlines():
            r = json.loads(l)
            if pred(r): return r
    keys = lambda d: [k for k in d if k.startswith(("up|", "down|", "lep|", "ckm|"))]
    r41 = row(ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "census.jsonl",
              lambda r: r["line"] == 153 and abs(r["Re_tau"] - 3.4) < 1e-9 and abs(r["Im_tau"] - 2.993325909) < 1e-6)
    m41 = K.compute(3.4, r41["Im_tau"], *L26[153]); d1 = max(dev(m41[k], r41[k]) for k in keys(m41))
    p = apexes()[len(apexes()) // 2]; d2 = 0.0
    for bstr in ("7/20", "1/4", "9/20", "3/20"):
        r55 = row(ROOT / "frontier" / "B1755_the_six_on_the_lines_of_order_13_to_20" / "verification" / "census.jsonl",
                  lambda r: r["alpha"] == "2/5" and r["b"] == bstr and abs(r["Re_tau"] - p["Re_tau"]) < 1e-9 and abs(r["Im_tau"] - p["Im_tau"]) < 1e-9)
        m55 = K.compute(p["Re_tau"], p["Im_tau"], ALPHA, Fr(bstr)); d2 = max(d2, max(dev(m55[k], r55[k]) for k in keys(m55)))
    a, bb = ALPHA, Fr(1, 60)
    x = K.compute(p["Re_tau"], p["Im_tau"], a, bb); y = K.compute(p["Re_tau"] + 1, p["Im_tau"], a, (bb - a) % 1)
    d3 = max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in keys(x))
    L = lines()
    return {"against_B1741_best_row": d1, "against_B1755_order_20_carriers": d2, "T_covariance_order_60": d3,
            "lines": len(L), "every_order_60": all(order(l) == 60 for l in L), "apex_points": len(apexes())}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["apex"], r["line"]))
    todo = [t for t in tasks() if (t[0], t[3]) not in done]
    print("%d apex points x %d lines = %d points; %d done; %d to do" % (len(apexes()), len(lines()), len(lines()) * len(apexes()), len(done), len(todo)), flush=True)
    with open(OUT, "a", encoding="utf-8") as fh, Pool(nw) as P:
        for i, r in enumerate(P.imap_unordered(point, todo, chunksize=8)):
            fh.write(json.dumps(r) + "\n")
            if i % 500 == 0: fh.flush(); print("row", i, flush=True)
    c = control(); (HERE / "control.json").write_text(json.dumps(c, indent=1) + "\n")
    print("control written"); print("census exit 0")


if __name__ == "__main__":
    main()
