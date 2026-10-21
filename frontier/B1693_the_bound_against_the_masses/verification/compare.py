"""B1693 (P-241): B1692's bound against the measured masses, sealed before this runs (PREREGISTRATION.md).
Reads only B1637's hash-pinned transcription of Huang and Zhou 2021 (masses at M_Z, the full SM).
    python3 -B compare.py      # writes comparison.json beside itself"""
import hashlib, json, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
BOUND = 4.0                 # B1692: one covariant Higgs and a flat line split the sectors' m2/m3 by at most four
ALLOW = 0.10                # B1637's running allowance, per ratio, in quadrature with the data
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA, "the data file is not the pinned one"
d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
def ratio(a, b):
    r = v[a] / v[b]; rel = math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2); return r, rel
R = {"up": ratio("c", "t"), "down": ratio("s", "b"), "lepton": ratio("mu", "tau")}
def spread(keys):
    hi = max(keys, key=lambda k: R[k][0]); lo = min(keys, key=lambda k: R[k][0])
    S = R[hi][0] / R[lo][0]; sl = math.sqrt(R[hi][1] ** 2 + R[lo][1] ** 2)       # sigma of log S
    return {"pair": [hi, lo], "S": S, "lower_3sigma": S * math.exp(-3 * sl), "upper_3sigma": S * math.exp(3 * sl)}
T1 = spread(["up", "down", "lepton"]); T2 = spread(["down", "lepton"])
grade = lambda t: "EXCLUDED" if t["lower_3sigma"] > BOUND else "ALLOWED"
out = {"data_sha256": SHA, "ratios": {k: {"value": r, "rel_sigma_with_allowance": e} for k, (r, e) in R.items()},
       "T1_one_Higgs": dict(T1, grade=grade(T1)), "T2_down_lepton": dict(T2, grade=grade(T2)), "bound": BOUND, "allowance": ALLOW}
if __name__ == "__main__":
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1); print(json.dumps(out, indent=1))
