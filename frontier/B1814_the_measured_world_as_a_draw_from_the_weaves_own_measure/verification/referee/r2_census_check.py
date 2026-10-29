"""Referee R2: the committed census.jsonl is the sealed census.py's output.  (a) tasks() regenerated (deterministic seeds)
against every row's task fields; (b) the frame (B1740's compute via census.point) recomputed on a random subsample of
rows, every key compared exactly; (c) row-level sanity: arms, indices, caps, warnings.  The sealed census.py is imported
from the arc read-only (only tasks()/point() are called; main() never)."""
import sys, json, math, random, hashlib, importlib.util, pathlib, time
from multiprocessing import Pool
REPO = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
ARC = REPO / "frontier/B1814_the_measured_world_as_a_draw_from_the_weaves_own_measure/verification"
src = ARC / "census.py"
assert hashlib.sha256(src.read_bytes()).hexdigest() == "6d95b183ec55cbae55a1394704a135ea53b9c3695e5db18654614d47b3349788"
sp = importlib.util.spec_from_file_location("b1814_census", src); C = importlib.util.module_from_spec(sp)
sys.modules["b1814_census"] = C; sp.loader.exec_module(C)
NSUB = int(sys.argv[1]) if len(sys.argv) > 1 else 40


def recompute(row):
    t = {k: row[k] for k in ("arm", "i", "word", "trace", "ell", "u", "gamma", "line_thread", "order", "n_lines", "Re_tau", "Im_tau", "alpha", "b")}
    r = C.point(t); diffs = []
    for k in row:
        if k not in r: diffs.append((k, "missing")); continue
        if json.loads(json.dumps(r[k])) != row[k]: diffs.append((k, row[k] if not isinstance(row[k], list) else row[k][:2], r[k] if not isinstance(r[k], list) else r[k][:2]))
    for k in r:
        if k not in row: diffs.append((k, "extra"))
    return row["arm"], row["i"], diffs


if __name__ == "__main__":
    rows = [json.loads(l) for l in (ARC / "census.jsonl").read_text().splitlines() if l.strip()]
    print("rows", len(rows), "unique (arm,i)", len({(r["arm"], r["i"]) for r in rows}))
    t0 = time.time(); T = C.tasks(); print("tasks() %.1f s" % (time.time() - t0))
    byk = {(r["arm"], r["i"]): r for r in rows}; mism = 0
    for t in T:
        r = byk[(t["arm"], t["i"])]
        for k, v in t.items():
            if json.loads(json.dumps(v)) != r[k]: mism += 1; print("task mismatch", t["arm"], t["i"], k, v, r[k]) if mism < 10 else None
    print("task-field mismatches:", mism)
    for arm in ("A0", "A1"):
        rs = [r for r in rows if r["arm"] == arm]
        cap = [r for r in rs if r["Im_tau"] > C.YCAP]
        print(arm, "capped", len(cap), "capped rows lacking frame keys", sum("up|L_2|S" not in r for r in cap),
              "uncapped rows with frame keys", sum("up|L_2|S" in r for r in rs if r["Im_tau"] <= C.YCAP),
              "warned", sum(bool(r.get("warnings")) for r in rs),
              "order>12", sum(r["order"] > 12 for r in rs), "Im<1", sum(r["Im_tau"] < 1 for r in rs))
    rng = random.Random(4242)
    sub = [r for r in rows if r["Im_tau"] <= C.YCAP]; sub = rng.sample(sub, NSUB)
    t0 = time.time()
    with Pool(3) as P: out = P.map(recompute, sub, chunksize=1)
    nd = sum(1 for a, i, d in out if d)
    print("recomputed %d rows in %.0f s; rows with any difference: %d" % (len(sub), time.time() - t0, nd))
    for a, i, d in out:
        if d: print(a, i, d[:4])
