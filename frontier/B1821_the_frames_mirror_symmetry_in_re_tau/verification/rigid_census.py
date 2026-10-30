"""THE FINAL ATTACK, step 5.3 (data-free; audit room, 2026-10-29): B1810's thirteen declared Higgs directions (DR, a0, R,
t = -5/288, B1730's zero-free F_a at n = 1) on the six's 2/5 family (the ten lines (2/5, k/10)) over B1726's tau grid (Re tau
0.05, 0.2, 0.35, 0.55, 0.7, 0.85; Im tau 2.05 ... 3.45), B1667's two radii, the eight readings.  The evaluator is
p449/cm_zero_line.py's rows_at (checked against B1810's committed table to 2.6e-6).  Rows are stored compactly; nothing is
compared with a measured value -- the output is committed unread to the seal's design and read only by the sealed test."""
# B1821 (2026-10-30): committed from the audit room as the census's instrument; the only change is the import path, set to this folder.
import json, os, sys, pathlib, itertools
from fractions import Fraction as F
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cm_zero_line as Z
OUT = HERE / "rigid_census.jsonl"
RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85)
IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
DIRS = Z.DIRS


def task(arg):
    k, re, im = arg
    try:
        rows = Z.rows_at(complex(re, im), (F(2, 5), F(k, 10)))
    except Exception as ex:
        return {"line": [2 / 5, k / 10], "tau": [re, im], "error": repr(ex)[:200]}
    comp = [[DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"],
             r["up"], r["down"], r["lepton"], r["V"], r["J"], r["V defined"]] for r in rows]
    return {"line": ["2/5", "%d/10" % k], "tau": [re, im], "rows": comp}


if __name__ == "__main__":
    jobs = [(k, re, im) for k in range(10) for re in RE for im in IM]
    done = set()
    if OUT.exists():
        for l in OUT.read_text().splitlines():
            r = json.loads(l); done.add((r["line"][1], r["tau"][0], r["tau"][1]))
    jobs = [j for j in jobs if ("%d/10" % j[0], j[1], j[2]) not in done]
    print("jobs", len(jobs), flush=True)
    with Pool(int(os.environ.get("RC_WORKERS", "8"))) as P, open(OUT, "a") as fh:
        for n, row in enumerate(P.imap_unordered(task, jobs, chunksize=1)):
            fh.write(json.dumps(row) + "\n"); fh.flush()
            if n % 100 == 0: print(n, flush=True)
    print("done", flush=True)
