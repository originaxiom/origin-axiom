#!/usr/bin/env python3
"""P-512, POST HOC (labelled; written after p512_check's output was read): the slopes C6 did not grade because B1817's R2
had not converged by its criterion. For each such slope with no tie, does R2 move toward the multiplicity prediction
between Im tau 8, 10 and 12, in all four series (two offsets, two readings)? Grades nothing.

    python3 -B p512_posthoc_unconverged.py --main <checkout of main at 5e5e75ac4>
"""
import argparse, json, pathlib, subprocess
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--main", required=True)
ROOT = pathlib.Path(ap.parse_args().main).resolve()
assert subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.startswith("5e5e75ac4")
out = json.loads((HERE / "p512_check_out.json").read_text(encoding="utf-8"))
rows = [json.loads(l) for l in (ROOT / "frontier/B1817_the_frames_own_lepton_down_factor_at_the_cusp/verification/a1_cusp_map.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
idx = {(r["nc"], r["alpha"], r["b"], r["Im"]): r for r in rows if "error" not in r}
counts = {"approaching": 0, "not approaching": 0}
lines = []
for rec in out["cells"]["C6"]["not_graded"]:
    if rec["why"] == "tie" or "pred_S" not in rec:
        continue
    pred = {"S": float(F(rec["pred_S"])), "St": float(F(rec["pred_St"]))}
    series = {}
    for bb in (0.137, 0.311):
        for rn in ("S", "St"):
            vals = [idx[(rec["nc"], rec["alpha"], bb, y)]["L_max|%s" % rn]["R2"] for y in (8.0, 10.0, 12.0)]
            series[(bb, rn)] = vals
    def dist(v, rn):
        return abs(v / pred[rn] - 1)
    appr = all(dist(v[2], rn) < dist(v[1], rn) < dist(v[0], rn) for (bb, rn), v in series.items())
    counts["approaching" if appr else "not approaching"] += 1
    lines.append("N_c %d alpha %-6s pred S %-4s St %-4s | S @0.137: %s | St @0.137: %s | %s" % (
        rec["nc"], rec["alpha"], rec["pred_S"], rec["pred_St"],
        " -> ".join("%.4f" % v for v in series[(0.137, "S")]), " -> ".join("%.4f" % v for v in series[(0.137, "St")]),
        "approaching in all four series" if appr else "NOT approaching in all four"))
text = "\n".join(["P-512 post hoc (labelled): the unconverged, untied slopes of C6, R2 at Im tau 8 -> 10 -> 12 (L_max)"] + lines +
                 ["counts: %s" % counts])
print(text)
(HERE / "p512_posthoc_unconverged_out.txt").write_text(text + "\n", encoding="utf-8")
