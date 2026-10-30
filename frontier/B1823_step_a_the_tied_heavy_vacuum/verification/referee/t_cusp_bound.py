"""Is the interior vacuum below everything the cusp can offer?  As Im tau -> infinity every singlet (a cusp form) -> 0, so
each copy tends to F(0) [neutral] + F(sigma_-^2 -> 0) + F(b_i^2): the cusp's infimum is at least n (2 F(0) + F(u*)), reached
only if every b_i^2 can be tuned to u* there.  An interior minimum below that bound cannot be undercut by a runaway."""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "rerun"))
import numpy as np
from search import u_star
from model import Ffun
D = json.loads((HERE.parent / "step_a_v2.json").read_text())["D"]["configs"]
rows = []
for r in D:
    us = u_star(r["mu2"], r["m02"])
    bound = r["n"] * (2 * Ffun(0.0, r["mu2"], r["m02"]) + Ffun(us, r["mu2"], r["m02"]))
    best = r["best"]["V"] if "best" in r else None
    rw = r.get("runaway", {}).get("V")
    rows.append(dict(menu=r["menu"], tnorm=r["tnorm"], n=r["n"], mu2=r["mu2"], m02=r["m02"], lv=r["lv"], V_interior=best,
                     cusp_bound=float(bound), interior_below_cusp_bound=bool(best is not None and best < bound), runaway_found_V=rw))
bad = [x for x in rows if x["V_interior"] is not None and not x["interior_below_cusp_bound"]]
print("configs:", len(rows), " interior vacuum NOT below the cusp's lower bound:", len(bad))
for x in bad:
    print("  ", x)
(HERE / "t_cusp_bound.json").write_text(json.dumps(dict(rows=rows, n_not_below=len(bad), not_below=bad), indent=1))
