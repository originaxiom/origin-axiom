"""chat1, 2026-10-28: B1740's F_-2 floors per sector and reading, after the relay's read-only referee (audit_checks.py's
part D read reading S only, while the Standard Model's reading takes the up sector in S~). Post hoc, labelled; read from
B1740's committed census; the measured ratios are read for the comparison. Committed before its one run.
Run:  python3 -B b1740_floor.py <main_checkout>"""
import sys, json, math, pathlib
import numpy as np
MAIN = pathlib.Path(sys.argv[1]).resolve()
rows = [json.loads(l) for l in (MAIN / "frontier/B1740_the_non_null_higgs_under_the_standard_models_reading/verification/census.jsonl").read_text().splitlines() if l.strip()]
v = json.loads((MAIN / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text())["masses_GeV"]["value"]
meas = {"up": v["c"] / v["t"], "down": v["s"] / v["b"], "lep": v["mu"] / v["tau"]}
I = np.array([r["Im_tau"] for r in rows for h in ("L_max", "L_2")]); ims = sorted(set(I.tolist()))
print("B1740's F_-2 census: %d rows at two horocycles" % len(rows))
for s in ("up", "down", "lep"):
    for rd in ("S", "St"):
        x = np.array([r["%s|%s|%s" % (s, h, rd)][0] for r in rows for h in ("L_max", "L_2")])
        print("  %-4s reading %-2s: least m2/m3 %.3f (%.0f times the measured %.2e); from %.3f at Im tau %.2f to %.3f at %.2f"
              % (s, rd, x.min(), x.min() / meas[s], meas[s], x[I == ims[0]].min(), ims[0], x[I == ims[-1]].min(), ims[-1]))
print("b1740_floor exit 0")
