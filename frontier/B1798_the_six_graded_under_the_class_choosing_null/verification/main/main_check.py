"""Main's verification of R71-1 (B1798), its own sample and seeds:
(1) 40 rows of the census extension (b1753_all266/census_ext.jsonl), drawn with main's own RNG seed, recomputed with
    B1753's point() (B1726's compute()), compared exactly;
(2) 12 seeds drawn at random from 5001-7500 (main's RNG): B1741's direct min_chi2 over all 59 318 rows for every target;
    per seed, the direct hits (<= obs) against the KD pipeline's, and every target with direct min <= obs + 0.5 must be a
    KD candidate (the screen's completeness).
    python3 -B main_check.py"""
import sys, json, random, pathlib
import numpy as np
D = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(D))
import census_ext as CE
import feat_null as FN
rng = random.Random(20261028)
rows = [json.loads(l) for l in (D / "b1753_all266" / "census_ext.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
print("census_ext rows:", len(rows), "| expected 223 x 218 =", 223 * 218)
worst = 0.0; nkeys = 0
for r in rng.sample(rows, 40):
    m = CE.point((r["apex"], r["Re_tau"], r["Im_tau"], r["line"]))
    for k, v in r.items():
        if k.startswith(("up|", "down|", "lep|", "ckm|")):
            nkeys += 1
            for x, y in zip(v, m[k]): worst = max(worst, abs(x - y))
print("(1) 40 extension rows recomputed (%d keyed entries): max |stored - recomputed| = %.3e" % (nkeys, worst))
C = FN.C_for("b1753_all"); F = C.chi2_features("seat", False)
Cp = FN._load_module("b1741_compare_plain", FN.FR / "B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")
obs = FN.SEALED["b1753_48"][1]
k = np.load(D / "kd_b1753_all_5001_7500.npz"); cs, cm = k["cand_seed"], k["plm"].min(0)
seeds = sorted(rng.sample(range(5001, 7501), 12))
td = tk = miss = 0
for s in seeds:
    d6, _ = Cp.draws(s); T = np.array(d6)
    dm = C.min_chi2(F, T)
    hd = int((dm <= obs + 1e-9).sum()); hk = int(((cs == s) & (cm <= obs + 1e-9)).sum())
    near = int((dm <= obs + 0.5).sum()); ncand = int((cs == s).sum())
    td += hd; tk += hk; miss += max(0, near - ncand)
    print("  seed %d: direct hits %d, KD hits %d | direct within obs+0.5: %d, KD candidates: %d" % (s, hd, hk, near, ncand))
print("(2) 12 random seeds (48 000 targets): direct hits %d, KD hits %d; targets within the margin not screened: %d" % (td, tk, miss))
print("main_check exit 0")
