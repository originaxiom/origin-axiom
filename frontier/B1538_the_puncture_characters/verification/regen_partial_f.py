#!/usr/bin/env python3
"""B1538 -- the sealed partial Part F record, regenerated after the seat's container was replaced (2026-10-06; disclosed).

The partial record was the sealed Part F's first candidate: its header and 12,825 readings, sha-256 1e9c6e55... (the
addendum). Part F took its candidates in run_L.jsonl's row order. The original Part L wrote its first 7 rows on one worker, in
the sealed task order (largest chunks first), before the restart on two workers. So the first candidate is the first hit with
n >= 2 in those rows, taken in task order -- if one of the first 7 tasks has one (asserted; otherwise this script stops).

It reads that candidate by the sealed read_part_F, through the driver path of the addendum (run_f_scoped.py: a one-row
run_L.jsonl in a temporary directory), stops it once 12,826 lines are written, keeps exactly the first 12,826 lines, and
compares their sha-256 with the sealed one. Only on equality is the file written as run_F.jsonl.

    python3 regen_partial_f.py     (after Part L is regenerated)  ->  run_F.jsonl, regen_partial_f.json"""
import hashlib
import json
import multiprocessing as mp
import os
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEALED = "1e9c6e5550f2bb46453375cce8761e87ad6307a19d0ce25f1bb80f74602bcec7"
LINES = 12826


def first_candidate():
    sys.path.insert(0, str(HERE))
    import run as RUN
    F = RUN.F
    tasks = []
    for sw, lat, w, cid in RUN.population():
        C = F.Cover(F.State(sw), lat, w)
        m, _ = RUN.modulus(C)
        size = RUN.orbit_count(C, m) if m else 0
        nch = max(1, -(-size // RUN.CHUNK))
        tasks += [(size, (cid, i)) for i in range(nch)]
    order = [t for _, t in sorted(tasks, key=lambda x: -x[0])]
    rows = {}
    for line in (HERE / "run_L.jsonl").read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            rows[(r["cover"], r["chunk"])] = r
    for pos, key in enumerate(order[:7]):
        r = rows[key]
        if not r["read"]:
            continue
        for h in r["hits"]:
            if h["n"] >= 2:
                return pos, {"cover": r["cover"], "word": r["word"], "lattice": r["lattice"], "read": True, "hits": [h]}
    raise SystemExit("no candidate in the first seven tasks: the original first candidate cannot be identified")


def _worker(tmp, row):
    import contextlib
    import io
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1538_sealed_run_regen", HERE / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(HERE))
    spec.loader.exec_module(RUN)
    (Path(tmp) / "run_L.jsonl").write_text(json.dumps(row) + "\n")
    RUN.HERE = Path(tmp)
    with contextlib.redirect_stdout(io.StringIO()):
        RUN.read_part_F(True)


def main():
    pos, row = first_candidate()
    print(f"the first candidate: task {pos + 1}, cover {row['cover']}, hit {row['hits'][0]}", flush=True)
    tmp = tempfile.mkdtemp(prefix="b1538_partial_")
    out = Path(tmp) / "run_F.jsonl"
    p = mp.get_context("spawn").Process(target=_worker, args=(tmp, row))
    t0 = time.time()
    p.start()
    while True:
        time.sleep(2)
        n = out.read_bytes().count(b"\n") if out.exists() else 0
        if n >= LINES or not p.is_alive():
            break
    p.terminate()
    p.join()
    data = out.read_bytes()
    lines = data.split(b"\n")
    kept = b"\n".join(lines[:LINES]) + b"\n"
    digest = hashlib.sha256(kept).hexdigest()
    rec = {"first candidate (task, cover, hit)": [pos + 1, row["cover"], row["hits"][0]], "lines kept": LINES,
           "sha-256": digest, "the sealed partial record's sha-256": SEALED, "equal": digest == SEALED,
           "seconds": round(time.time() - t0, 1)}
    print(json.dumps(rec), flush=True)
    (HERE / "regen_partial_f.json").write_text(json.dumps(rec, indent=1) + "\n")
    if digest != SEALED:
        raise SystemExit("the regenerated partial record differs from the sealed one: not written")
    (HERE / "run_F.jsonl").write_bytes(kept)


if __name__ == "__main__":
    main()
