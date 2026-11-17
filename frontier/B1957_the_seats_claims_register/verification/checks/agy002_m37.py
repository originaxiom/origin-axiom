"""B1957: agy-002's note M37 (A2-CANON-T90): its blind standalone values for the read-out on the whole, compared by main
with main's B1940 corrected file under the rule main committed before any seat's output existed (compare_area_second.py:
per value |d ln| <= 3 sqrt(e_main^2 + e_seat^2 + delta^2), delta = 5.4e-3).  The seat's sealed JSON is read as data; none
of its numbers is printed, only the differences.  No measured number is touched."""
import json, math, pathlib, subprocess, sys
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = next((ROOT / "frontier").glob("B1940_*")) / "verification"; sys.path.insert(0, str(V)); import compare_area_second as CA
seat = json.loads(subprocess.run(["git", "show", "origin/agy-002/verify:relays/a2_canon/verify_a2_canon_results.json"], capture_output=True, text=True, cwd=ROOT).stdout)["seven_values_summary"]
main = json.loads((V / "BIG_RUN_VALUES_v2.json").read_text())["options"]
if __name__ == "__main__":
    print("options in main's file:", sorted(main))
    for opt, world in (("W-|b (area)", "W_minus"), ("W+|b (area)", "W_plus")):
        mv, me = main[opt]["values"], main[opt]["error"]; me = me if isinstance(me, list) else [me] * 7
        for wt, lab in (("exact_T90", "the exact weight"), ("old_weight", "the truncated weight (the control)")):
            sv = seat["area_measure_exact_untruncated"][wt][world]["value_7"]; r = CA.compare(mv, me, sv, [0.0] * 7)
            print("%s, the seat's values with %s, its own error set to zero: agrees %s; worst |d ln| / tolerance %.3f; largest |d ln| %.5f" % (opt, lab, r["agrees"], r["worst"], max(abs(math.log(s / m)) for s, m in zip(sv, mv))))
    for opt, world in (("W-|a (move count)", "W_minus"), ("W+|a (move count)", "W_plus")):
        if opt not in main: continue
        mv, me = main[opt]["values"], main[opt]["error"]; me = me if isinstance(me, list) else [me] * 7
        sv, se = seat["move_count_measure"]["exact_T90"][world]["mean_7"], seat["move_count_measure"]["exact_T90"][world]["se_7"]; r = CA.compare(mv, me, sv, se)
        print("%s, the seat's sample of words with its own standard errors: agrees %s; worst |d ln| / tolerance %.3f; largest |d ln| %.5f" % (opt, r["agrees"], r["worst"], max(abs(math.log(s / m)) for s, m in zip(sv, mv))))
    old = json.loads((next((ROOT / "frontier").glob("B1932_*")) / "verification" / "BIG_RUN_VALUES.json").read_text())["options"]
    for opt, world in (("W-|b (area)", "W_minus"), ("W+|b (area)", "W_plus")):
        mv, me = old[opt]["values"], old[opt]["error"]; me = me if isinstance(me, list) else [me] * 7
        sv = seat["area_measure_exact_untruncated"]["exact_T90"][world]["value_7"]; r = CA.compare(mv, me, sv, [0.0] * 7)
        print("control: %s against B1932's uncorrected double-precision file: agrees %s; worst |d ln| / tolerance %.3f; largest |d ln| %.5f" % (opt, r["agrees"], r["worst"], max(abs(math.log(s_ / m)) for s_, m in zip(sv, mv))))
    import hashlib
    print("the two files' SHA-256 begin %s (B1940 v2) and %s (B1932): the note's 9ece85e1 and df1c9bee" % (hashlib.sha256((V / "BIG_RUN_VALUES_v2.json").read_bytes()).hexdigest()[:8], hashlib.sha256((next((ROOT / "frontier").glob("B1932_*")) / "verification" / "BIG_RUN_VALUES.json").read_bytes()).hexdigest()[:8]))
