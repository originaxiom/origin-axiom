"""B1741 (P-347): tau from the thread rule, the line free, the census (no data).  At each of the 75 distinct apex points of
B1720's 121 thread classes (Im tau = Lagrange/2, as stored in the_thread_census.json), B1656's frame at B1667's canonical
end (both horocycles), the Higgs DR, on every one of B1713's 266 flat lines (orders 1-12 up to sign) -- not only the
thread's own -- every sector in S and S~ and the CKM for each (up, down) pair, through B1726's sealed compute().
19 950 points, 39 900 rows.  Checkpointed: each point is appended to census.jsonl; a rerun skips the points done.
    python3 -B census.py [--workers 8]      # writes census.jsonl and control.json beside itself
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "census.jsonl"
B1720 = ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification" / "the_thread_census.json"
_C = {}


def _K():
    if "K" not in _C:
        sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
        import census as K
        _C["K"] = K
    return _C["K"]


def apexes():
    """the distinct apex points of B1720's classes, with the classes at each (a mirror pair shares one)"""
    d = json.loads(B1720.read_text(encoding="utf-8")); out = {}
    for c in d["classes"]:
        key = (round(c["tau"][0], 9), round(c["tau"][1], 9)); out.setdefault(key, []).append(c["word"])
    return sorted(out.items(), key=lambda kv: (kv[0][1], kv[0][0]))


def tasks():
    return [(pi, re, im, k) for pi, ((re, im), _w) in enumerate(apexes()) for k in range(266)]


def point(t):
    pi, re, im, k = t
    a, b = _K().lines()[k]
    r = _K().compute(re, im, a, b); r.update(apex=pi, words=apexes()[pi][1], line=k, Re_tau=re, Im_tau=im)
    return r


def control():
    """C1: (i) the instrument reproduces B1726's stored row at (0.35 + 3.05i, its line 149) exactly; (ii) the frame's
    T-covariance at an apex: (3.4 + 2.993i, (2/5, 9/10)) against (0.4 + 2.993i, (2/5, 9/10) + 3 (0, 2/5)) = (2/5, 1/10)
    (b -> b + 3 alpha mod 1), every stored key, max |log| (B1724's law, the shift that maps an apex to the census frame)"""
    K = _K(); L = K.lines()
    rec = None
    for l in (ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["line"] == 149 and r["Re_tau"] == 0.35 and r["Im_tau"] == 3.05: rec = r; break
    mine = K.compute(0.35, 3.05, *L[149])
    def dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    d1 = max(dev(mine[k], rec[k]) for k in mine)
    im = [t for t in apexes() if abs(t[0][0] - 3.4) < 1e-9 and abs(t[0][1] - 2.993325909) < 1e-6][0][0][1]
    x = K.compute(3.4, im, Fr(2, 5), Fr(9, 10)); y = K.compute(0.4, im, Fr(2, 5), Fr(1, 10))
    d2 = max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in x)
    return {"against_B1726_row": d1, "T_covariance_at_an_apex": d2}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["apex"], r["line"]))
    todo = [t for t in tasks() if (t[0], t[3]) not in done]
    print(len(tasks()), "points;", len(done), "done;", len(todo), "to do", flush=True)
    with Pool(nw) as P, open(OUT, "a", encoding="utf-8") as f:
        for r in P.imap_unordered(point, todo, chunksize=8):
            f.write(json.dumps(r) + "\n"); f.flush()
    c = control(); json.dump(c, open(HERE / "control.json", "w"), indent=1)
    print("control:", c)


if __name__ == "__main__":
    main()
