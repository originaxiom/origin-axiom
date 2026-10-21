"""B1695 (P-243): one line, one tau, the unique section, against the six measured ratios; sealed before this runs.
For every grid point of the_grid.json and every discrete choice (Re tau in {0, 1/2}; the horocycle L_max or L_2; the up
sector's reading S, S~, conj S): chi2 = sum over the six log-ratios (m2/m3 and m1/m3 of up, down, leptons) of
(ln model - ln measured)^2 / sigma^2, sigma^2 = the data's relative errors in quadrature + B1637's 10% allowance squared;
and the largest factor by which any of the six misses.  G1 PASSES if the grid's minimum chi2 < 14.86 (chi2 with 4 degrees
of freedom at 99.5%, an allowance for the 12 discrete choices); G2 PASSES if some point puts all six within a factor 3.
A grid search: its minimum is an upper bound on the true minimum, and a FAIL is a statement about this grid.
    python3 -B compare.py      # writes comparison.json beside itself"""
import hashlib, json, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
ALLOW, CHI2_CUT, TOL = 0.10, 14.86, 3.0
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA
d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
def meas(a, b): return v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2)
TARGET = {("up", 0): meas("c", "t"), ("up", 1): meas("u", "t"), ("down", 0): meas("s", "b"), ("down", 1): meas("d", "b"),
          ("lep", 0): meas("mu", "tau"), ("lep", 1): meas("e", "tau")}
grid = json.loads((HERE / "the_grid.json").read_text(encoding="utf-8"))["grid"]
best = {}; tol_hits = []
for p in grid:
    for hor in ("L_max", "L_2"):
        for rd in ("S", "St", "conjS"):
            model = {"up": p["up|%s|%s" % (hor, rd)], "down": p["down|%s|S" % hor], "lep": p["lep|%s|S" % hor]}
            chi2 = 0.0; worst = 1.0; ok = True
            for (sec, k), (val, sig) in TARGET.items():
                m = model[sec][k]
                if not (m > 0): ok = False; break
                z = math.log(m / val); chi2 += (z / sig) ** 2; worst = max(worst, math.exp(abs(z)))
            if not ok: continue
            key = "Re%.1f|%s|%s" % (p["Re_tau"], hor, rd)
            if key not in best or chi2 < best[key]["chi2"]:
                best[key] = {"chi2": chi2, "worst_factor": worst, "alpha_96ths": p["j"], "Im_tau": p["Im_tau"],
                             "model": {s_: model[s_] for s_ in model}}
            if worst <= TOL: tol_hits.append({"combo": key, "alpha_96ths": p["j"], "Im_tau": p["Im_tau"], "worst_factor": worst, "chi2": chi2})
overall = min(best.values(), key=lambda r: r["chi2"])
by_worst = min(({"combo": k, **r} for k, r in best.items()), key=lambda r: r["worst_factor"])
out = {"data_sha256": SHA, "targets": {"%s|%s" % (k[0], ["m2/m3", "m1/m3"][k[1]]): {"value": t[0], "rel_sigma": t[1]} for k, t in TARGET.items()},
       "best_by_combo": best, "overall_min_chi2": overall, "G1_pass": overall["chi2"] < CHI2_CUT,
       "G2_points_within_factor_3": len(tol_hits), "G2_pass": len(tol_hits) > 0, "G2_examples": sorted(tol_hits, key=lambda r: r["worst_factor"])[:10],
       "smallest_worst_factor_among_chi2_minima": by_worst, "chi2_cut": CHI2_CUT, "tolerance": TOL}
if __name__ == "__main__":
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    print("G1", out["G1_pass"], "G2", out["G2_pass"])
