#!/usr/bin/env python3
"""Review 80, at the landing: main's plant on B1885's lock, made properly.

WHAT WAS WRONG.  In main's plants_agy002.py the plant "the note on the grid's 18 digits taken out of the verdict line"
looks for the words ", and 18 for the grid and the two checks made on it [...]".  Main's own mend of the same day had
changed that line to "the three checks made on it, A4, A5 and H5 [...]".  So the pattern found nothing, the file was
left as it was, and the kept row "the lock: passes" is the lock's answer on an unchanged arc.  The script does not ask
that a plant change its file.  Found by a reading on another family of model (its check of main's answers), and made
again here.
WHAT THIS DOES.  In a temporary copy of the arc's folder: (1) nothing planted; (2) main's pattern as it was written,
with a count of what it changed; (3) the note in fact taken out, from ", and 18 for the grid" to the bracket that
closes it.  The lock is run on each.
HOW IT COULD FAIL: (3) changing nothing stops the run; (1) not passing stops the run."""
import json, pathlib, re, shutil, subprocess, sys, tempfile
ROOT = pathlib.Path(__file__).resolve().parents[4]
ARC = next((ROOT / "frontier").glob("B1885_*"))
OLD = r", and 18 for the grid and the two checks made on it \[[^\]]*\]"


def run(change):
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d) / "root"; arc = root / "frontier" / ARC.name
        shutil.copytree(ARC, arc, ignore=shutil.ignore_patterns("__pycache__"))
        f = arc / "arc_verdict.json"; v = json.loads(f.read_text(encoding="utf-8")); before = v["claim_one_line"]
        if change: v["claim_one_line"] = change(before)
        f.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        tests = sorted(str(p) for p in (arc / "verification").glob("test_*.py"))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider"] + tests, capture_output=True, text=True, cwd=str(root))
        tail = [l for l in r.stdout.strip().split("\n") if l.strip()][-1]
        return len(before) - len(v["claim_one_line"]), "FAILS" if r.returncode else "passes", re.sub(r" in [0-9.]+s.*", "", tail)


def taken_out(c):
    i = c.index(", and 18 for the grid"); j = c.index("[", i); depth = 0
    for k in range(j, len(c)):
        depth += (c[k] == "[") - (c[k] == "]")
        if depth == 0: return c[:i] + c[k + 1:]
    raise RuntimeError("the note's bracket does not close")


rows = [("nothing planted", None), ("main's pattern as it was written", lambda c: re.sub(OLD, "", c)), ("the note in fact taken out", taken_out)]
out = []
for name, change in rows:
    removed, answer, tail = run(change)
    out.append({"plant": name, "characters taken out": removed, "the lock": answer, "tail": tail})
    print("%-34s characters taken out: %3d   the lock: %-6s (%s)" % (name, removed, answer, tail), flush=True)
assert out[0]["the lock"] == "passes", "the lock does not pass on the arc as it stands"
assert out[2]["characters taken out"] > 0, "the plant changed nothing"
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
