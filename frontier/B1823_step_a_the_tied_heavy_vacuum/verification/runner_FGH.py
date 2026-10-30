"""Runs step_a_v2.py's sections F, G, H while section D runs (which owns step_a_v2.json): output step_a_v2_FGH.json,
merged into step_a_v2.json by merge.py after D finishes.  Same functions, same environment record."""
import sys, json, time, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step_a_v2 as S
OUT = HERE / "step_a_v2_FGH.json"
res = json.loads(OUT.read_text()) if OUT.exists() else {}
res["environment"] = S.env()
for key in (sys.argv[1:] or ["F", "G", "H"]):
    t0 = time.time(); print("== section", key, flush=True)
    r = S.SECTIONS[key](); r["seconds"] = round(time.time() - t0, 1); res[key] = r
    OUT.write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    print("== section %s done in %.0fs" % (key, r["seconds"]), flush=True)
