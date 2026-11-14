"""B1937: main's comparison of agy-exp's X-EXACT-W (raw output at 48926341b, read by this script only; none of its numbers is
printed) with B1932's committed values. Tolerance fixed here before the run: per value, |d ln| <= 3 sqrt(e_m^2 + e_s^2
+ delta^2), e_m and e_s each code's stated relative error, delta = 5.4e-3 (the record's bound on the systematic: the
end above Im tau = 6, 5.4e-3; the grid interpolation, 4.6e-3). Prints only d ln / tolerance and z = d ln / sqrt(e_m^2 + e_s^2)."""
import json, subprocess, math, hashlib
ROOT = "/Users/dri/origin-axiom"
V = ROOT + "/frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json"
raw = open(V, "rb").read(); assert hashlib.sha256(raw).hexdigest().startswith("df1c9bee002ecf5e")
mine = json.loads(raw)
seat = json.loads(subprocess.run(["git", "-C", ROOT, "show", "48926341b:relays/x_exact_w_verify/verify_x_exact_w_out.json"], capture_output=True, text=True, check=True).stdout)
KEYS = ["up__2_over_3", "up__1_over_3", "down__2_over_3", "down__1_over_3", "mixing__1_2", "mixing__2_3", "mixing__1_3"]
assert mine["positions"] == ['up m2/m3', 'up m1/m3', 'down m2/m3', 'down m1/m3', '|V12|', '|V23|', '|V13|']
DELTA = 5.4e-3
c = seat["route2_ergodic_move_count"]["four_primary_combinations"]
worst = 0
for opt, comb in (("W-|a (move count)", "W_minus__exact_T90"), ("W+|a (move count)", "W_plus__exact_T90")):
    m = mine["options"][opt]; s = c[comb]["claimed_7_frame_code"]; se = c[comb]["claimed_7_frame_code_se"]
    row = []
    for i, k in enumerate(KEYS):
        dl = math.log(s[k]) - math.log(m["values"][i]); em = m["error"][i] / m["values"][i]; es = se[k] / s[k]
        tol = 3 * math.sqrt(em ** 2 + es ** 2 + DELTA ** 2); z = dl / math.sqrt(em ** 2 + es ** 2)
        row.append("%s: dln/tol %+.2f, z %+.1f" % (k, dl / tol, z)); worst = max(worst, abs(dl / tol))
    print(opt, "vs", comb); [print("   ", r) for r in row]
print("worst |d ln| / tolerance: %.2f -> %s" % (worst, "AGREE" if worst <= 1 else "DISAGREE"))
# the old weight as a control: it must differ from the exact-weight values by more than the jackknife alone (B1932: ~1 %)
for opt, comb in (("W-|a (move count)", "W_minus__old_small_cut"),):
    m = mine["options"][opt]; s = c[comb]["claimed_7_frame_code"]
    print("control (seat's old weight vs main's exact):", "max |d ln| %.4f" % max(abs(math.log(s[k]) - math.log(m["values"][i])) for i, k in enumerate(KEYS)))
# the discriminating fact: z (jackknife errors only) of the seat's exact-weight and old-weight values against main's exact
print("discrimination (z against the two codes' jackknife errors only; rms over the seven):")
for opt, w in (("W-|a (move count)", "W_minus"), ("W+|a (move count)", "W_plus")):
    m = mine["options"][opt]
    for tag in ("exact_T90", "old_small_cut"):
        s = c[w + "__" + tag]["claimed_7_frame_code"]; se = c[w + "__" + tag]["claimed_7_frame_code_se"]
        zs = [(math.log(s[k]) - math.log(m["values"][i])) / math.sqrt((m["error"][i] / m["values"][i]) ** 2 + (se[k] / s[k]) ** 2) for i, k in enumerate(KEYS)]
        tl = max(abs(math.log(s[k]) - math.log(m["values"][i])) / (3 * math.sqrt((m["error"][i] / m["values"][i]) ** 2 + (se[k] / s[k]) ** 2 + DELTA ** 2)) for i, k in enumerate(KEYS))
        print("   %s seat %-13s rms z %5.1f, max |z| %5.1f, max dln/tol %.2f" % (opt[:2], tag, math.sqrt(sum(z * z for z in zs) / 7), max(abs(z) for z in zs), tl))
# B1934's identity in the seat's read-out: lepton ratios equal the down ratios (printing only the relative difference)
for w in ("W_minus__exact_T90", "W_plus__exact_T90"):
    a = c[w]["all_12_outputs"]
    print("seat's lepton vs down,", w, "max rel diff %.1e" % max(abs(a["lepton__%s" % r] / a["down__%s" % r] - 1) for r in ("2_over_3", "1_over_3", "1_over_2")))
