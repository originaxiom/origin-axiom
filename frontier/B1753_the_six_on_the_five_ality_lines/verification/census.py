"""B1753 census: the six on the five-ality lines.  At the 223 distinct apex
points of the primitive thread words of length 13 (B1720's rule: Im tau = Lagrange/2; apex height in [2.0, 3.6]; none
among the classes B1741 (2-9), B1748 (10-11) or B1749 (12) used), on the 48 lines of B1713's 266 whose order is
divisible by 5 (orders 5 and 10: the lines on which the hypercharge twist 6Y w carries SU(5)'s centre, 6Y mod 5 being the
SU(5) multiplet label),
B1726's sealed compute() exactly as B1741 calls it (B1656's frame at B1667's end, both horocycles, the Higgs DR, every
sector in S and S~, the CKM for each (up, down) pair).  10 704 points.  Checkpointed (census.jsonl, resumable).
    python3 -B census.py [--workers 8]      # writes census.jsonl, control.json; prints "census exit 0"
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "census.jsonl"
HEIGHT = (2.0, 3.6)
_C = {}


def _K():
    """B1726's sealed census module (its compute and lines), loaded under its own name so this file's name cannot shadow it"""
    if "K" not in _C:
        import importlib.util
        if "b1726_census" not in sys.modules:
            sp = importlib.util.spec_from_file_location("b1726_census", ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.py")
            m = importlib.util.module_from_spec(sp); sys.modules["b1726_census"] = m; sp.loader.exec_module(m)
        _C["K"] = sys.modules["b1726_census"]
    return _C["K"]


def _TG():
    if "TG" not in _C:
        sys.path.insert(0, str(ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification"))
        import thread_geometry as TG
        _C["TG"] = TG
    return _C["TG"]


def apexes():
    """the fresh apex points: words of length 12 (B1720's necklaces), apex height in HEIGHT, distinct (Re tau mod 1, Im tau)
    to 9 digits, with the words at each"""
    if "pts" not in _C:
        TG = _TG(); pts = {}
        for w in TG.necklaces(13, 13):
            h = TG.lagrange(w) / 2
            if not (HEIGHT[0] <= h <= HEIGHT[1]): continue
            r, A = TG.representative(w, h); assert abs(r - h) < 1e-9, (w, r, h)
            a, b, c, d = A; xc = (a - d) / (2 * c); key = (round(xc % 1, 9), round(h, 9))
            pts.setdefault(key, {"Re_tau": round(xc % 1, 9), "Im_tau": h, "words": []})["words"].append(w)
        _C["pts"] = sorted(pts.values(), key=lambda p: (p["Im_tau"], p["Re_tau"]))
    return _C["pts"]


def five_lines():
    """the indices of B1713's lines whose order (the lcm of the denominators of alpha and b) is divisible by 5"""
    import math
    return [k for k, (a, b) in enumerate(_K().lines()) if math.lcm(Fr(a).denominator, Fr(b).denominator) % 5 == 0]


def tasks():
    return [(pi, p["Re_tau"], p["Im_tau"], k) for pi, p in enumerate(apexes()) for k in five_lines()]


def point(t):
    pi, re, im, k = t
    a, b = _K().lines()[k]
    r = _K().compute(re, im, a, b); r.update(apex=pi, words=apexes()[pi]["words"], line=k, Re_tau=re, Im_tau=im)
    return r


def control():
    """C1: (i) B1741's stored best row (line 153 at 3.4 + 2.993325909i) reproduced by this instrument, every stored key;
    (ii) B1726's stored row (line 149 at 0.35 + 3.05i), as B1741's C1 (i); (iii) B1724's T-law at a fresh apex (the middle
    one): (tau, (alpha, b)) against (tau + 1, (alpha, b - alpha mod 1)) on (2/5, 3/10), the CKM's moduli and every mass key"""
    K = _K(); L = K.lines()
    def dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    def row(path, line, re, im):
        for l in path.read_text(encoding="utf-8").splitlines():
            r = json.loads(l)
            if r["line"] == line and abs(r["Re_tau"] - re) < 1e-9 and abs(r["Im_tau"] - im) < 1e-6: return r
    keys = lambda d: [k for k in d if k.startswith(("up|", "down|", "lep|", "ckm|"))]
    r41 = row(ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "census.jsonl", 153, 3.4, 2.993325909)
    m41 = K.compute(3.4, r41["Im_tau"], *L[153]); d1 = max(dev(m41[k], r41[k]) for k in keys(m41))
    r26 = row(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.jsonl", 149, 0.35, 3.05)
    m26 = K.compute(0.35, 3.05, *L[149]); d2 = max(dev(m26[k], r26[k]) for k in keys(m26))
    p = apexes()[len(apexes()) // 2]; a, b = Fr(2, 5), Fr(3, 10)
    x = K.compute(p["Re_tau"], p["Im_tau"], a, b); y = K.compute(p["Re_tau"] + 1, p["Im_tau"], a, (b - a) % 1)
    d3 = max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in keys(x))
    return {"against_B1741_best_row": d1, "against_B1726_row": d2, "T_covariance_at_a_fresh_apex": d3, "apex_points": len(apexes()), "lines": len(five_lines())}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["apex"], r["line"]))
    todo = [t for t in tasks() if (t[0], t[3]) not in done]
    print("%d apex points x %d lines = %d points; %d done; %d to do" % (len(apexes()), len(five_lines()), len(five_lines()) * len(apexes()), len(done), len(todo)), flush=True)
    with open(OUT, "a", encoding="utf-8") as fh, Pool(nw) as P:
        for i, r in enumerate(P.imap_unordered(point, todo, chunksize=8)):
            fh.write(json.dumps(r) + "\n")
            if i % 5000 == 0: fh.flush(); print("row", i, flush=True)
    c = control(); (HERE / "control.json").write_text(json.dumps(c, indent=1) + "\n")
    print("control written"); print("census exit 0")


if __name__ == "__main__":
    main()
