"""B1944: the big run's look, read. It reads only the three committed outputs (sealed at a3d54c621 before anyone read
them) and the pinned data's sigmas, which the sealed script itself used, to express each row as frame over measured.
It computes nothing new and fits nothing.
    python3 -B read_the_look.py"""
import json, math, sys, hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B40 = next((ROOT / "frontier").glob("B1940_*")) / "verification"; B32 = next((ROOT / "frontier").glob("B1932_*")) / "verification"
SHAS = {B40 / "big_run_output_v3.json": "0441eb5c440be1bc721aa778adc27f8f0c6b8df47df94a48476ced752d3d6ef6",
        B40 / "big_run_windows_v3_output.json": "952f3fc48a53d35db18439b3483612fc3de829b2c4c3c7d217473147c3e557bc",
        B32 / "big_run_output.json": "667ff85fedb250f6e78b7a5ec76c0af86f814d7894a4f826f295f26496eb8bff"}
for f, h in SHAS.items():
    assert hashlib.sha256(f.read_bytes()).hexdigest() == h, f
sys.path.insert(0, str(B40)); import big_run_look_v3 as L
tl, sig = L.targets(L.DATA, L.CKMDATA)
v3 = json.loads((B40 / "big_run_output_v3.json").read_text()); w = json.loads((B40 / "big_run_windows_v3_output.json").read_text())
v1 = json.loads((B32 / "big_run_output.json").read_text())
names = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|"]
print("GOVERNING (version 3): %s; passing options: %s" % (v3["outcome_governing_seven"], v3["passing_options_none_preferred"]))
for o, e in v3["options"].items():
    f = [math.exp(p * s) for p, s in zip(e["pulls_nine"], sig)]
    print("%-20s chi2_7 %7.1f | worst factor (7) %7.1f | chi2_six %7.1f | chi2_nine %7.1f" % (o, e["chi2_seven"], e["worst_factor_seven"], e["chi2_six"], e["chi2_nine"]))
    print("   frame / measured: " + "  ".join("%s %.3g" % (n, x) for n, x in zip(names, f)))
cal = v3["calibration"]["by_statistic"]
print("calibration, fraction of random targets as good as the best option: chi2_7 %.4f, worst factor %.4f" % (cal["chi2_seven"]["fraction_as_good_as_the_best_option"], cal["worst_factor_seven"]["fraction_as_good_as_the_best_option"]))
print("windows companion (reported): " + "; ".join("%s: chi2_7 %.4f, worst factor %.4f" % (k, v["fraction_as_good"]["chi2_seven"], v["fraction_as_good"]["worst_factor_seven"]) for k, v in w["by_window"].items()))
print("VERSION 1 (reported): %s, best chi2_7 %.1f, calibration %.4f" % (v1["outcome"], v1["best_chi2_7"], v1["calibration"]["fraction_as_good_as_the_best_option"]))
