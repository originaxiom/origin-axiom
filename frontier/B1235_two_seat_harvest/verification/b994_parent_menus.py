# HARVESTED from fab5cloud's branch (reports/fresh_physics_seat_2026-09-01/sweeps/p2_parent_menus_from_b869.py @ 2ebdff8d), ROOT made repo-relative -- B1235 cell 5: B869's committed engine on B994's three parents.
#!/usr/bin/env python3
r"""Sweep follow-up for R3_REPORT P2 ("B994's parent menus exist in no committed file").

Before concluding an absence, the repo was swept (sweep_absence.sh pati.?salam|su\(6\).?x.?su\(2\)|su\(3\)\^3').
Result: no committed OUTPUT keys a menu by the parents SU(6)xSU(2), SU(3)^3 or Pati-Salam,
but committed CODE does generate them: B869's engine (`frontier/B869_false_positive_control/
false_positive_control.py`, on main) descends any su/so state via `all_descents`.  This script
runs that committed engine, unmodified, on the three parent states and prints the menus it
generates, so the P2 claim can be corrected from "no committed file" to "no committed output;
committed code generates them as follows".
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # frontier/B1235_*/verification -> repo root
SRC = os.path.join(ROOT, "frontier", "B869_false_positive_control", "false_positive_control.py")

spec = importlib.util.spec_from_file_location("fpc", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

menu, _ = m.e6_entry()
states = {r["option"]: r["state"] for r in menu if r["state"] is not None}
so10 = states["SO(10)xU(1)"]
ps = next(d for d in m.all_descents(*so10) if "Pati-Salam" in d[0])
states["Pati-Salam"] = (ps[1], ps[2], ps[3])

for name in ("SU(6)xSU(2)", "SU(3)^3", "Pati-Salam"):
    f, u, c = states[name]
    print(f"\n== B869 engine menu at parent {name} = {m.name_state(f, u)}  dim {m.dim_state(f, u)}")
    for desc, nf, nu, nc in m.all_descents(f, u, c):
        print(f"   {desc:34} -> {m.name_state(nf, nu):36} dim {m.dim_state(nf, nu):3}"
              f"  registerable={m.chiral(nf, nc)}")
    tr = []
    end = m.run_cascade(f, u, c, tr)
    print(f"   cascade (B861 rule) endpoint: {end}   path: {[t['at'] for t in tr]}")
