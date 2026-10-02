#!/usr/bin/env python3
"""The second-order test of branch_obstruction.py at all six branch points (both signs of Z), with the sector and
the sign of the meridian that B1446 found there."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import branch_obstruction as bo
from mpmath import mp, mpf, mpc, polyroots, nstr
mp.dps = 60
rec = json.load(open(HERE.parents[1] / "B1446_the_parabolic_points_and_the_branch_points" / "verification" / "branch_points.json"))["numeric"]["points"]
roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300); out = []
for p in rec:
    ur = mpc(eval(p["u"].replace("j", "j"))) if "j" in p["u"] else mpf(p["u"])
    u = min(roots, key=lambda r: abs(r - ur)); zs = p["Z_sign"]; z = p["zero_sectors"][0]; a = tuple(z["a"]); ts = z["meridian_sign"]
    try:
        r = bo.analyse(u, a, zsign=zs, tsign=ts, quiet=True)
        row = dict(u=nstr(u, 12), Z_sign=zs, a=list(a), meridian_sign=ts, h1=r["h1"], h2=r["h2"], classes=[r["classes_upper"], r["classes_lower"]],
                   second_order_norm=r.get("both", {}).get("norm_of_second_order_term"), distance_from_image=r.get("both", {}).get("distance_from_image"))
    except AssertionError as ex: row = dict(u=nstr(u, 12), Z_sign=zs, a=list(a), meridian_sign=ts, error=str(ex)[:80])
    out.append(row); print(row, flush=True)
json.dump(out, open(HERE / "all_branch_points.json", "w"), indent=1)
