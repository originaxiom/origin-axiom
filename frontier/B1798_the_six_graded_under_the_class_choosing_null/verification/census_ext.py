"""R71-1 draft: B1753's 223 apexes on the 218 lines of B1713's 266 that B1753's census does not hold (orders not divisible
by 5), with B1726's sealed compute() exactly as B1753's census.py calls it (B1753's census.py imported unchanged under its
own module name; its apexes() and _K() reused).  No data is read here.  Checkpointed, resumable.
    python3 -B census_ext.py --workers 10      -> b1753_all266/census_ext.jsonl
    python3 -B census_ext.py --verify 24       -> recompute 24 committed 48-line rows, print the max deviation"""
import sys, json, math, random, pathlib, importlib.util
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V53 = ROOT / "frontier/B1753_the_six_on_the_five_ality_lines/verification"
OUT = pathlib.Path(__file__).resolve().parent / "b1753_all266" / "census_ext.jsonl"
if "b1753_census" not in sys.modules:
    _sp = importlib.util.spec_from_file_location("b1753_census", V53 / "census.py")
    _m = importlib.util.module_from_spec(_sp); sys.modules["b1753_census"] = _m; _sp.loader.exec_module(_m)
B53 = sys.modules["b1753_census"]


def other_lines():
    five = set(B53.five_lines())
    return [k for k in range(266) if k not in five]


def tasks():
    return [(pi, p["Re_tau"], p["Im_tau"], k) for pi, p in enumerate(B53.apexes()) for k in other_lines()]


def point(t):
    return B53.point(t)          # B1753's own point(): compute(re, im, *lines()[k]) + the same labels


def verify(n):
    rows = [json.loads(l) for l in (V53 / "census.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    rng = random.Random(7101); pick = rng.sample(rows, n)
    worst = 0.0
    for r in pick:
        m = B53.point((r["apex"], r["Re_tau"], r["Im_tau"], r["line"]))
        for k, v in r.items():
            if k.startswith(("up|", "down|", "lep|", "ckm|")):
                for x, y in zip(v, m[k]):
                    worst = max(worst, abs(x - y))
    print("verified %d committed rows; max |stored - recomputed| = %.3e" % (n, worst))


def main():
    from multiprocessing import Pool
    if "--verify" in sys.argv:
        verify(int(sys.argv[sys.argv.index("--verify") + 1])); return
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    OUT.parent.mkdir(exist_ok=True)
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip():
                try: r = json.loads(l)
                except json.JSONDecodeError: continue
                done.add((r["apex"], r["line"]))
    todo = [t for t in tasks() if (t[0], t[3]) not in done]
    print("%d apexes x %d other lines = %d; %d done; %d to do" % (len(B53.apexes()), len(other_lines()), len(tasks()), len(done), len(todo)), flush=True)
    with open(OUT, "a", encoding="utf-8") as fh, Pool(nw) as P:
        for i, r in enumerate(P.imap_unordered(point, todo, chunksize=8)):
            fh.write(json.dumps(r) + "\n")
            if i % 2000 == 0: fh.flush(); print("row", i, flush=True)
    print("census_ext exit 0")


if __name__ == "__main__":
    main()
