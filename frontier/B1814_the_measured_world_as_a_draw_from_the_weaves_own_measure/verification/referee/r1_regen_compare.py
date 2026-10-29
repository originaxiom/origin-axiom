"""Referee R1: regenerate B1814's comparison.json by running the SEALED compare.py (the arc's file, sha-checked) as a module,
with HERE / CENSUS pointed at the scratch copy (run/), so nothing is written into the arc.  B1741's module is the real one
(loaded by compare.C() from the repo, sha asserted there).  Then compare the regenerated JSON with the committed one."""
import sys, json, hashlib, importlib.util, pathlib, time
REPO = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
ARC = REPO / "frontier/B1814_the_measured_world_as_a_draw_from_the_weaves_own_measure/verification"
RUN = pathlib.Path(__file__).resolve().parent / "run"
src = ARC / "compare.py"
assert hashlib.sha256(src.read_bytes()).hexdigest() == "022ec24f6f6db9606cdecf21d2fa98219c34d6cf46f0323e32d932baa21c3dea"
for f in ("census.jsonl", "control.json"):
    assert (RUN / f).read_bytes() == (ARC / f).read_bytes(), f
sp = importlib.util.spec_from_file_location("b1814_compare", src); m = importlib.util.module_from_spec(sp)
sys.modules["b1814_compare"] = m; sp.loader.exec_module(m)
m.HERE = RUN; m.CENSUS = RUN / "census.jsonl"
(RUN / "comparison.json").unlink(missing_ok=True)
t0 = time.time(); m.main(); print("main() %.0f s" % (time.time() - t0), flush=True)
new = json.loads((RUN / "comparison.json").read_text()); old = json.loads((ARC / "comparison.json").read_text())


def walk(a, b, path=""):
    bad = []
    if isinstance(a, dict):
        if set(a) != set(b): bad.append((path, "keys differ"))
        for k in a:
            if k in b: bad += walk(a[k], b[k], path + "/" + k)
    elif isinstance(a, list):
        if len(a) != len(b): bad.append((path, "len"))
        for i, (x, y) in enumerate(zip(a, b)): bad += walk(x, y, path + "[%d]" % i)
    elif a != b:
        bad.append((path, a, b))
    return bad


bad = walk(new, old)
print("byte-identical:", (RUN / "comparison.json").read_bytes() == (ARC / "comparison.json").read_bytes())
print("differences:", len(bad)); [print(x) for x in bad[:30]]
