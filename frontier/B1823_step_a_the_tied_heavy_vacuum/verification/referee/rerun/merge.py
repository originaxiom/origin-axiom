"""Merge step_a_v2_FGH.json's sections into step_a_v2.json (after section D has written it)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
main = json.loads((HERE / "step_a_v2.json").read_text()); fgh = json.loads((HERE / "step_a_v2_FGH.json").read_text())
for k in ("F", "G", "H"):
    if k in fgh:
        main[k] = fgh[k]
main["merge_note"] = "sections F, G, H computed by runner_FGH.py (the same functions) while D ran; merged by merge.py"
(HERE / "step_a_v2.json").write_text(json.dumps(main, indent=1, default=str), encoding="utf-8")
print("merged", [k for k in ("A", "B", "C", "D", "F", "G", "H") if k in main])
