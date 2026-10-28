"""cross-checks: (1) on fresh seeds, B1741's direct min_chi2 (all rows, the seat menu) against the KD pipeline's all-lines
hits, per arc; (2) b1753_all's data per-line minima on the 48 five-ality lines against b1753_48's (the sealed census)."""
import sys, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import feat_null as FN
arc, seeds = sys.argv[1], [int(s) for s in sys.argv[2:]]
C = FN.C_for(arc); A = C.arrays(); F = C.chi2_features("seat", False)
obs = FN.SEALED["b1749"][1] if arc == "b1749" else FN.SEALED["b1753_48"][1]
Cp = FN._load_module("b1741_compare_plain", FN.FR / "B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")
k = np.load(HERE / ("kd_%s_5001_7500.npz" % arc)); hitseed = k["cand_seed"][k["plm"].min(0) <= obs + 1e-9]
tot_d = tot_k = 0
for s in seeds:
    d6, _ = Cp.draws(s); T = np.array(d6)
    hd = int((C.min_chi2(F, T) <= obs + 1e-9).sum()); hk = int((hitseed == s).sum())
    tot_d += hd; tot_k += hk
print("%s fresh seeds %s: direct min_chi2 hits %d, KD pipeline hits %d" % (arc, seeds if len(seeds) < 6 else "%d seeds" % len(seeds), tot_d, tot_k))
if arc == "b1753_all":
    a = np.load(HERE / "feat_b1753_all.npz")["data_line_min"]; b = np.load(HERE / "feat_b1753_48.npz")["data_line_min"]
    m = np.isfinite(b); print("five-ality lines: max |all - sealed48| data per-line min = %.3e over %d lines" % (np.abs(a[m] - b[m]).max(), m.sum()))
