"""THE FINAL ATTACK, Step B's refined census: a second worker set on the remaining lines (data-free; 2026-10-30, main).
The first run (rigid_census_refined.py) takes the menu in order; this one takes it in REVERSE, with a copy of the first
run's line function (its grid, evaluator, rounding and gzip settings imported from it) that differs only in its temporary
suffix, so the two never write the same temporary file (checked: the copy's records equal the first run's file on sample
points). A line already finished (its file exists) is skipped; a line both happen to compute is
written twice with identical bytes (the computation and the gzip stream are deterministic) by an atomic os.replace. Its
log has the first run's format, and the manifest tool reads both logs.
    RC_WORKERS=6 nice -n 10 python3 -I rigid_census_refined_tail.py"""
import gzip, json, os, sys, pathlib
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rigid_census_refined as RC


def line_task(m):
    N, a, b = m
    name = "N%02d_%d-%d_%d-%d" % (N, a.numerator, a.denominator, b.numerator, b.denominator)
    path = RC.OUTDIR / (name + ".jsonl.gz")
    if path.exists(): return name, "skipped"
    recs = []
    for re, im in RC.GRID:
        assert abs(re) < 1
        try:
            rows = RC.Z.rows_at(complex(re, im), (a, b))
            comp = [[RC.DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"],
                     RC.r8(r["up"]), RC.r8(r["down"]), RC.r8(r["lepton"]), RC.r8(r["V"]), RC.r8(r["J"]), r["V defined"]] for r in rows]
            assert len(comp) == 208, len(comp)
            recs.append({"line": [str(a), str(b)], "order": N, "tau": [re, im], "rows": comp})
        except Exception as ex:
            recs.append({"line": [str(a), str(b)], "order": N, "tau": [re, im], "error": repr(ex)[:200]})
    if path.exists(): return name, "skipped"                       # finished by the first run meanwhile
    tmp = path.with_suffix(".tmpb")
    with open(tmp, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as fh:
        for r in recs: fh.write((json.dumps(r) + "\n").encode("utf-8"))
    os.replace(tmp, path)
    return name, "%d configurations, %d errors" % (len(recs), sum(1 for r in recs if "error" in r))


if __name__ == "__main__":
    todo = [m for m in reversed(RC.MENU)]
    print("tail run: %d lines in reverse" % len(todo), flush=True)
    with Pool(int(os.environ.get("RC_WORKERS", "6"))) as P:
        for n, (name, what) in enumerate(P.imap_unordered(line_task, todo, chunksize=1)):
            print(n, name, what, flush=True)
    print("done", flush=True)
