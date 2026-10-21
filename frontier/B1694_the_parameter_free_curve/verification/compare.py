"""B1694 (P-242): the parameter-free curve against the measured masses, sealed before this runs (PREREGISTRATION.md).
Reads the_curve.json (this arc) and B1637's hash-pinned transcription of Huang and Zhou 2021 (M_Z, the full SM).
For each curve and sector: F(r2) by log-log interpolation along the curve (Im tau increasing, r2 decreasing), rho =
r1_measured / F(r2_measured), sigma(log rho) from the data (r1's and r2's errors, r2's through the curve's slope) and
B1637's 10% allowance on each ratio; a sector PASSES a curve if the 3 sigma band of log rho meets [-log 3, log 3] (the
theory tolerance, a factor 3), FAILS otherwise; outside the curve's r2 range: OUT.
    python3 -B compare.py      # writes comparison.json beside itself"""
import hashlib, json, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
TOL, ALLOW = 3.0, 0.10
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA
d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
curves = json.loads((HERE / "the_curve.json").read_text(encoding="utf-8"))["curves"]
SECT = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
def rel(a, b): return math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2)
res = {}
for cname, pts in curves.items():
    lr2 = [math.log(p["m2/m3"]) for p in pts]; lr1 = [math.log(p["m1/m3"]) for p in pts]
    row = {}
    for sec, (f1, f2, f3) in SECT.items():
        r1, r2 = v[f1] / v[f3], v[f2] / v[f3]; x = math.log(r2)
        if not (min(lr2) <= x <= max(lr2)): row[sec] = {"grade": "OUT", "r2": r2}; continue
        k = next(i for i in range(len(lr2) - 1) if (lr2[i] - x) * (lr2[i + 1] - x) <= 0)
        slope = (lr1[k + 1] - lr1[k]) / (lr2[k + 1] - lr2[k]); F = math.exp(lr1[k] + slope * (x - lr2[k]))
        rho = r1 / F; sig = math.sqrt(rel(f1, f3) ** 2 + (slope * rel(f2, f3)) ** 2)
        lo, hi = math.log(rho) - 3 * sig, math.log(rho) + 3 * sig
        grade = "PASS" if (hi >= -math.log(TOL) and lo <= math.log(TOL)) else "FAIL"
        row[sec] = {"r1": r1, "r2": r2, "F(r2)": F, "rho": rho, "rho_3sigma": [math.exp(lo), math.exp(hi)], "local_slope": slope, "grade": grade}
    row["all_three_pass"] = all(row[sec]["grade"] == "PASS" for sec in SECT)
    res[cname] = row
out = {"data_sha256": SHA, "tolerance_factor": TOL, "allowance": ALLOW, "by_curve": res,
       "some_curve_passes_all_three": any(r["all_three_pass"] for r in res.values())}
if __name__ == "__main__":
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1); print(json.dumps(out, indent=1))
