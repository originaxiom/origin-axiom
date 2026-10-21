#!/usr/bin/env python3
"""POST HOC, not a cell: main's B1693 (S162, opened at 8b99c7876) read at the frame's scale with W119's one-loop factors.

Arithmetic on two committed outputs, after both were read:
- B1693's central ratios at M_Z, from main's S162 commit message: the leptons' m_mu/m_tau is 15.98 times the up
  quarks' m_c/m_t (T1), and the down-lepton pair is 3.14 (T2); B1692's bound is 4;
- W119's factors F = DR(M_Z)/DR(Lambda) per sector at each of its 24 scan points (the_beyond_tree_level.json).

At one loop m1/m2 does not run (W119's rule), so (m2/m3)(Lambda) = F * (m2/m3)(M_Z), and a ratio of two sectors' m2/m3
moves by the ratio of their F. No new physics input; no threshold or two-loop terms.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "the_beyond_tree_level.json").read_text(encoding="utf-8"))
T1_MZ, T2_MZ, BOUND = 15.98, 3.14, 4.0
rows = []
for p in d["points"]:
    F = p["F"]
    rows.append({"model": p["model"], "tan beta": p["tan beta"], "Lambda": p["Lambda"],
                 "T1 at Lambda (leptons over up)": T1_MZ * F["leptons"] / F["up"],
                 "T2 at Lambda (leptons over down)": T2_MZ * F["leptons"] / F["down"]})
t1 = [r["T1 at Lambda (leptons over up)"] for r in rows]
t2 = [r["T2 at Lambda (leptons over down)"] for r in rows]
out = {"status": "post hoc arithmetic, not a cell", "inputs": {"T1 at M_Z": T1_MZ, "T2 at M_Z": T2_MZ, "bound": BOUND},
       "T1 range at Lambda": [min(t1), max(t1)], "T2 range at Lambda": [min(t2), max(t2)],
       "T1 above the bound at every point": all(x > BOUND for x in t1),
       "T2 within the bound at every point": all(1 / BOUND <= x <= BOUND for x in t2), "points": rows}
(HERE / "the_b1693_at_the_frame_scale.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "points"}, indent=1))
