"""Review 74: B1809:129 says that for the isotropic directions (R, t = -5/288) m2 vanishes only at L = infinity, with
m2/m3 = O(1/L) at the canonical end.  The web seat says this fails on order-4 lines (every sector) and order-12 lepton rows.
Main's check with B1821's evaluator (cm_zero_line.rows_at): within-sector m2/m3 only, nothing inter-sector, no phase."""
import sys, pathlib, json
sys.path.insert(0, sys.argv[1]); import cm_zero_line as Z
lines = {"order 4": [(0.25, 0.5), (0.5, 0.25), (0.25, 0.0), (0.0, 0.25), (0.75, 0.25)],
         "order 12": [(1/12, 0.0), (5/12, 1/12), (1/12, 5/12), (0.25, 1/3), (1/3, 0.25)],
         "order 5 (control)": [(0.2, 0.0), (0.0, 0.2), (0.2, 0.2)],
         "order 8 (control)": [(0.125, 0.0), (0.375, 0.25)]}
out = {}
for tau in (complex(0.13, 2.2), complex(0.3, 1.5)):
    for grp, ls in lines.items():
        for ln in ls:
            rows = [r for r in Z.rows_at(tau, ln) if r["direction"] in ("R", "t=-5/288")]
            for sec in ("up", "down", "lepton"):
                v = [r[sec][1] for r in rows]                     # m2/m3 over both radii and the eight readings
                out.setdefault(grp, {}).setdefault(sec, []).extend(v)
for grp, d in out.items():
    print("%-18s" % grp, "  ".join("%s m2/m3 max %.1e min %.1e" % (s, max(v), min(v)) for s, v in d.items()))
