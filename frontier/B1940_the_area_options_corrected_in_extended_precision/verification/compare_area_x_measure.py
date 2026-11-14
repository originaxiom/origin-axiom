"""The adapter for agy-exp's X-MEASURE (raw output sealed unread at 04293e826), written after that output arrived and
mechanical only: it maps the seat's names onto the seven positions and calls compare_area_second.compare, committed
before the output existed (c77335a08, the rule's A15). It prints none of the seat's numbers, only scaled differences.
Also, as a discriminating control: the seat's values against B1932's uncorrected area values (the corrected ones should
be nearer), and the seat's truncated-weight values against B1940's exact-weight ones."""
import json, math, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE))
import compare_area_second as C
seat = json.loads(subprocess.run(["git", "-C", str(ROOT), "show", "04293e826:relays/x_measure_verify/verify_x_measure_out.json"], capture_output=True, text=True, check=True).stdout)
K = ["up__2_over_3", "up__1_over_3", "down__2_over_3", "down__1_over_3", "mixing__1_2", "mixing__2_3", "mixing__1_3"]
comb = seat["area_measure_readout"]["four_primary_combinations"]
pick = lambda name, field: [comb[name][field][k] for k in K]
main = C.main_area_options()
old = json.loads((next((ROOT / "frontier").glob("B1932_*")) / "verification" / "BIG_RUN_VALUES.json").read_text())["options"]
worst = 0; allagree = True
for opt, name in (("W-|b (area)", "W_minus__exact_T90"), ("W+|b (area)", "W_plus__exact_T90")):
    mv, me = main[opt]; sv, se = pick(name, "claimed_7_frame_code"), pick(name, "claimed_7_frame_code_quad_err")
    r = C.compare(mv, me, sv, se); allagree &= r["agrees"]; worst = max(worst, r["worst"])
    print("%s vs %s: %s, worst |d ln|/tol %.2f; per position d ln/tol: %s" % (opt, name, "AGREE" if r["agrees"] else "DISAGREE", r["worst"], " ".join("%+.2f" % x["dln_over_tol"] for x in r["rows"])))
    ro = C.compare(old[opt]["values"], old[opt]["error"], sv, se)
    print("   control, against B1932's uncorrected file: worst |d ln|/tol %.2f (%s)" % (ro["worst"], "agree" if ro["agrees"] else "disagree"))
    rt = C.compare(mv, me, pick(name.replace("exact_T90", "old_small_cut"), "claimed_7_frame_code"), pick(name.replace("exact_T90", "old_small_cut"), "claimed_7_frame_code_quad_err"))
    print("   control, the seat's truncated weight against B1940's exact: worst |d ln|/tol %.2f" % rt["worst"])
print("THE AREA OPTIONS: %s (worst %.2f of the tolerance)" % ("AGREE" if allagree else "DISAGREE", worst))
