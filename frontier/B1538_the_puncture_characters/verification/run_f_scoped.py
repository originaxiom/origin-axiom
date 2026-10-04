#!/usr/bin/env python3
"""B1538 -- PART F' (PREREGISTRATION_ADDENDUM.md): the sealed Part F, unchanged, at the in-scope candidates, in parallel.

    python3 -u run_f_scoped.py --dry                     the hash check and the scope's aggregates (nothing read)
    python3 -u run_f_scoped.py --k13 [--record]          control K13 -> control_k13.json
    python3 -u run_f_scoped.py --workers k --record      ->  run_F_scoped.jsonl (resumable by whole candidates)

THE CANDIDATES are the sealed read_part_F's: every hit with n >= 2 in run_L.jsonl's read rows, in the record's order.
IN SCOPE (the addendum's section 2, fixed by structure before any Part F reading): every candidate of m004 and m003, and every
candidate of m136 and m135 whose planned readings (4 times the sealed smith_fourth_roots) are at most CAP, zero included.
They are read golden first, then silver by planned readings ascending; within each, in the record's order.
EACH CANDIDATE is read by the sealed run.py's own read_part_F, loaded by path and unchanged, in a fresh (spawned) process,
as the sealed Part F ran in its own process: the task writes a one-row run_L.jsonl (the candidate's Part L row, with that one
hit and the fields read_part_F reads) in a temporary directory, points the sealed module's HERE there, calls
read_part_F(True), and returns the run_F.jsonl it wrote there: the candidate's header row and its planned readings.
The driver appends each candidate's block to run_F_scoped.jsonl in the scope's order, checking only structure (the header,
the number of rows, their kind and candidate).  Nothing is read or printed from a reading.
CONTROL K13: the same path, on the sealed record's first candidate (out of scope), reproduces the first K13_LINES lines of
the sealed partial run_F.jsonl byte for byte; only sha-256 digests are compared.
Before anything, every line of ARTIFACT_HASHES.txt is checked; a single mismatch stops the driver."""
import contextlib
import hashlib
import importlib.util
import io
import json
import multiprocessing as mp
import os
import shutil
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
OUT = HERE / "run_F_scoped.jsonl"
GOLDEN = ("+LR", "-LR")
CAP = 1024
K13_LINES = 2000
# the scope's aggregates, sealed in the addendum's section 2 (the driver and the scoped read-out stop if they differ)
SEALED = {"candidates": 64422, "planned readings": 948832288, "in scope": 12152, "in scope, planned readings": 501792,
          "in scope, by state": {"m004": [8, 416], "m003": [42, 2688], "m136": [4923, 277504], "m135": [7179, 221184]},
          "out of scope": 52270, "out of scope, planned readings": 948330496}


def sealed_run():
    """the sealed run.py, loaded by path under its own name (it puts its own directory first on the path)"""
    alias = "b1538_run_sealed"
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / "run.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


def hash_mismatches():
    bad = []
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(None, 1)
            if hashlib.sha256((ARC / name).read_bytes()).hexdigest() != digest:
                bad.append(name)
    return bad


def candidates(RUN):
    """every candidate in the sealed order: its one-row Part L record, state, key, planned readings and scope"""
    covers, out = {}, []
    with open(HERE / "run_L.jsonl") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            if not r["read"]:
                continue
            for h in r["hits"]:
                if h["n"] < 2:
                    continue
                cid = r["cover"]
                if cid not in covers:
                    covers[cid] = RUN.F.Cover(RUN.F.State(r["word"]), tuple(r["lattice"]), int(cid.rsplit(".w", 1)[1]))
                planned = 4 * RUN.smith_fourth_roots(covers[cid], h["zeta"], h["m"])
                out.append({"row": {"cover": cid, "word": r["word"], "lattice": r["lattice"], "read": True, "hits": [h]},
                            "state": r["state"], "key": [cid, list(h["zeta"]), h["m"], list(h["s"])], "planned": planned,
                            "in scope": r["word"] in GOLDEN or planned <= CAP})
    return out


def scope_order(cands):
    """golden first, then silver by planned readings ascending; the record's order within each"""
    gold = [c for c in cands if c["in scope"] and c["row"]["word"] in GOLDEN]
    silver = [c for c in cands if c["in scope"] and c["row"]["word"] not in GOLDEN]
    return gold + sorted(silver, key=lambda c: c["planned"])          # sorted() is stable


def aggregates(cands):
    ins = [c for c in cands if c["in scope"]]
    by_state = {}
    for c in ins:
        s = by_state.setdefault(c["state"], [0, 0])
        s[0] += 1
        s[1] += c["planned"]
    return {"candidates": len(cands), "planned readings": sum(c["planned"] for c in cands), "in scope": len(ins),
            "in scope, planned readings": sum(c["planned"] for c in ins),
            "in scope, by state": {k: by_state.get(k, [0, 0]) for k in ("m004", "m003", "m136", "m135")},
            "out of scope": len(cands) - len(ins),
            "out of scope, planned readings": sum(c["planned"] for c in cands if not c["in scope"])}


def _read_into(tmp, row):
    """the sealed read_part_F on one candidate, its records in the directory tmp"""
    RUN = sealed_run()
    (Path(tmp) / "run_L.jsonl").write_text(json.dumps(row) + "\n")
    RUN.HERE = Path(tmp)
    with contextlib.redirect_stdout(io.StringIO()):
        RUN.read_part_F(True)


def read_candidate(task):
    idx, row = task
    tmp = tempfile.mkdtemp(prefix="b1538f_")
    try:
        t0 = time.time()
        _read_into(tmp, row)
        p = Path(tmp) / "run_F.jsonl"
        return idx, (p.read_text() if p.exists() else ""), time.time() - t0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def block_ok(text, cand):
    """structure only: one header for this candidate, then exactly its planned rows, each a reading of this candidate"""
    rows = [json.loads(x) for x in text.splitlines()]
    if not rows or rows[0].get("kind") != "candidate":
        return False
    head = rows[0]
    key = [head["cover"], head["chi"]["zeta"], head["chi"]["m"], head["chi"]["s"]]
    return (key == cand["key"] and len(rows) == 1 + head["planned"] and text.endswith("\n")
            and all(r.get("kind") == "reading" and [r["cover"], r["chi"]["zeta"], r["chi"]["m"], r["chi"]["s"]] == key
                    for r in rows[1:]))


def resume(scope):
    """the number of whole candidate blocks already in OUT, in the scope's order; an incomplete tail is cut"""
    if not OUT.exists():
        return 0
    lines = OUT.read_text().splitlines(keepends=True)
    pos, k = 0, 0
    while pos < len(lines) and k < len(scope):
        head = json.loads(lines[pos]) if lines[pos].endswith("\n") else None
        if head is None or head.get("kind") != "candidate":
            break
        end = pos + 1 + head["planned"]
        if end > len(lines) or not block_ok("".join(lines[pos:end]), scope[k]):
            break
        pos, k = end, k + 1
    keep = "".join(lines[:pos])
    if len(keep.encode()) != OUT.stat().st_size:
        print(f"resume: cutting an incomplete tail ({len(lines) - pos} lines)", flush=True)
        OUT.write_text(keep)
    return k


def control_k13(first, record):
    """K13: the driver's path reproduces the sealed partial record's first K13_LINES lines (only digests compared)"""
    sealed_lines = (HERE / "run_F.jsonl").read_bytes().split(b"\n")
    assert len(sealed_lines) > K13_LINES
    want = hashlib.sha256(b"\n".join(sealed_lines[:K13_LINES]) + b"\n").hexdigest()
    tmp = tempfile.mkdtemp(prefix="b1538k13_")
    p = Path(tmp) / "run_F.jsonl"
    ctx = mp.get_context("spawn")
    proc = ctx.Process(target=_read_into, args=(tmp, first["row"]))
    t0 = time.time()
    proc.start()
    try:
        while True:
            time.sleep(2)
            if p.exists() and p.read_bytes().count(b"\n") >= K13_LINES:
                break
            if not proc.is_alive():
                break
    finally:
        if proc.is_alive():
            proc.terminate()                                   # this process only, by its own PID
        proc.join()
    got_lines = p.read_bytes().split(b"\n") if p.exists() else []
    got = hashlib.sha256(b"\n".join(got_lines[:K13_LINES]) + b"\n").hexdigest() if len(got_lines) > K13_LINES else None
    shutil.rmtree(tmp, ignore_errors=True)
    res = {"control": "K13", "what": "the driver's path (a one-row run_L.jsonl in a temporary directory, the sealed "
           "run.py's HERE pointed there, read_part_F(True) in a spawned process) on the sealed record's first candidate",
           "lines compared": K13_LINES, "sha-256 of the sealed partial's first lines": want,
           "sha-256 of the driver's first lines": got, "identical": got == want, "seconds": round(time.time() - t0, 1)}
    print(json.dumps(res, indent=1), flush=True)
    if record:
        (HERE / "control_k13.json").write_text(json.dumps({k: v for k, v in res.items() if k != "seconds"}, indent=1) + "\n")
    return res


def main():
    args = sys.argv[1:]
    bad = hash_mismatches()
    if bad:
        print(f"hash mismatch, nothing read: {bad}", flush=True)
        sys.exit(2)
    RUN = sealed_run()
    cands = candidates(RUN)
    agg = aggregates(cands)
    print(json.dumps(agg), flush=True)
    if agg != SEALED:
        print("the scope's aggregates differ from the addendum's: nothing read", flush=True)
        sys.exit(3)
    scope = scope_order(cands)
    if "--dry" in args:
        return
    if "--k13" in args:
        control_k13(cands[0], "--record" in args)
        return
    if "--record" not in args:
        print("nothing written (pass --record)", flush=True)
        return
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    done = resume(scope)
    total = sum(c["planned"] for c in scope)
    read = sum(c["planned"] for c in scope[:done])
    print(f"B1538 Part F': {len(scope)} candidates, {total} planned readings; {done} candidates done; {workers} workers",
          flush=True)
    t0 = time.time()
    ctx = mp.get_context("spawn")
    with ctx.Pool(workers) as pool:
        tasks = [(i, scope[i]["row"]) for i in range(done, len(scope))]
        for idx, text, sec in pool.imap(read_candidate, tasks):
            if not block_ok(text, scope[idx]):
                print(f"candidate {idx + 1}: its block is not the sealed shape; stopped", flush=True)
                sys.exit(4)
            with open(OUT, "a") as f:
                f.write(text)
                f.flush()
                os.fsync(f.fileno())
            read += scope[idx]["planned"]
            print(f"{idx + 1}/{len(scope)} candidates, {read}/{total} readings ({sec:.1f} s; total {time.time() - t0:.0f} s)",
                  flush=True)
    print("Part F' done", flush=True)


if __name__ == "__main__":
    main()
