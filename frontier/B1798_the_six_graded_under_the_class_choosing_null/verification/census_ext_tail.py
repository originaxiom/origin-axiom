"""companion to census_ext.py: the same tasks and the same point() (B1753's own), taken from the END of the task list,
written to b1753_all266/census_ext_tail.jsonl; skips tasks already in either file at start.  Stopped by hand when the two
files together cover every task; the loader deduplicates (compute() is deterministic; duplicates are checked equal).
    python3 -B census_ext_tail.py --workers 2"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import census_ext as E
OUT = E.OUT.parent / "census_ext_tail.jsonl"


def point(t):
    return E.point(t)


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    for p in (E.OUT, OUT):
        if p.exists():
            for l in p.read_text(encoding="utf-8").splitlines():
                try: r = json.loads(l)
                except json.JSONDecodeError: continue
                done.add((r["apex"], r["line"]))
    todo = [t for t in reversed(E.tasks()) if (t[0], t[3]) not in done]
    print("tail: %d to do (from the end)" % len(todo), flush=True)
    with open(OUT, "a", encoding="utf-8") as fh, Pool(nw) as P:
        for i, r in enumerate(P.imap(point, todo, chunksize=4)):
            fh.write(json.dumps(r) + "\n"); fh.flush()
    print("tail exit 0")


if __name__ == "__main__":
    main()
