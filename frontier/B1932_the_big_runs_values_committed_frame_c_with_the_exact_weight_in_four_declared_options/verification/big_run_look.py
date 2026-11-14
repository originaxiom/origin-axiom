"""THE BIG RUN's comparison (main, drafted 2026-11-14 night; sealed by sha256 before it is run; its rule is
BIG_RUN_RULE.md). It reads the committed values (BIG_RUN_VALUES.json, pinned by sha256 below) and the two data files
pinned by B1720's compare.py, computes P-341's statistic on frame C's seven rows for each of the four declared options,
calibrates the best of the four against random targets, and writes big_run_output.json. Nothing is fitted; no option
is chosen after the output is read.
    python3 -B big_run_look.py"""
import hashlib, json, math, pathlib, random
import numpy as np
from scipy.stats import chi2
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
VALUES = HERE / "BIG_RUN_VALUES.json"
VALUES_SHA = "df1c9bee002ecf5eeb7f1f360e497a5c091bf092cdbaa499352ea3201d02b536"
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
CKMSHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
ALLOW = 0.10                     # P-341 / B1720 compare.py
OPTIONS = 4                      # two Higgs worlds x two measures, all committed with their values
BAR = float(chi2.ppf(1 - 0.01 / OPTIONS, 7))      # the 1 % tail of chi2(7) after the four options: 22.04
N_CAL, SEED = 4000, 20261115


def main():
    assert hashlib.sha256(VALUES.read_bytes()).hexdigest() == VALUES_SHA, "the values are not the committed ones"
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA and hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == CKMSHA
    d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
    meas = lambda a, b: (v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2))
    T = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b")]
    ck = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]
    for i, j in ((0, 1), (1, 2), (0, 2)):
        T.append((ck["value"][i][j], math.sqrt((ck["sigma"][i][j] / ck["value"][i][j]) ** 2 + ALLOW ** 2)))
    tl = np.log([t[0] for t in T]); sig = np.array([t[1] for t in T])
    V = json.loads(VALUES.read_text(encoding="utf-8"))
    out = {"bar": BAR, "options": {}}
    best = None
    for name, o in V["options"].items():
        m = np.log(np.array(o["values"])); pulls = (m - tl) / sig; c2 = float(np.sum(pulls ** 2))
        out["options"][name] = {"chi2_7": c2, "pulls": pulls.tolist(), "passes_bar": c2 < BAR}
        best = c2 if best is None else min(best, c2)
    M = np.array([np.log(np.array(o["values"])) for o in V["options"].values()])
    rng = random.Random(SEED); hits = 0; samples = []
    for _ in range(N_CAL):
        r = []
        for _s in range(2):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2:
                    break
            r += [r2, r1]
        while True:
            a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a:
                break
        r += [a, b, c]
        b2 = float(np.min(np.sum(((M - np.log(r)) / sig) ** 2, axis=1))); samples.append(b2); hits += b2 <= best + 1e-12
    out["calibration"] = {"N": N_CAL, "seed": SEED, "law": "B1720 compare.py's random targets (r_masses for two sectors, r_ckm)",
                          "fraction_as_good_as_the_best_option": hits / N_CAL, "median_best": float(np.median(samples))}
    out["best_chi2_7"] = best
    out["outcome"] = ("PASS" if best < BAR and hits / N_CAL < 0.01 else "FAIL")
    (HERE / "big_run_output.json").write_text(json.dumps(out, indent=1))
    print("written; sha256", hashlib.sha256((HERE / "big_run_output.json").read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
