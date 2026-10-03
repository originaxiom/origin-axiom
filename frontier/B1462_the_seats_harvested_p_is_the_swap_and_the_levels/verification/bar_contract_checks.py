#!/usr/bin/env python3
"""B1462 -- two of sm:B1524's null-contract numbers, re-derived (the rest of B1524 is read, not re-derived):
 (1) the scan law: the chance that n exchangeable picks from a census of N with K carriers include a carrier is
     1 - C(N-K, n)/C(N, n), and B1518's 1 - (1 - K/N)^n understates it (strictly, for 1 < n <= N-K, K >= 1);
 (2) the Sidak counterexample at the gate: two picks in one stratum of 399 with 2 carriers -- exact size 0.0100125 > 0.01,
     Sidak's 1 - (1 - 2/399)^2 = 0.00999 < 0.01 passes; Bonferroni 2 * 2/399 = 0.01003 does not."""
import sys, json, pathlib
from fractions import Fraction as F
from math import comb
HERE = pathlib.Path(__file__).resolve().parent
def exact_scan(N, K, n): return 1 - F(comb(N - K, n), comb(N, n))
def binom_scan(N, K, n): return 1 - (1 - F(K, N)) ** n
def main():
    out = {}
    under = all(exact_scan(N, K, n) > binom_scan(N, K, n) for N in range(5, 60) for K in range(1, N) for n in range(2, N - K + 1))
    equal_at_one = all(exact_scan(N, K, 1) == binom_scan(N, K, 1) for N in range(5, 60) for K in range(1, N))
    out["binomial_understates_for_n_ge_2"] = under; out["agree_at_n_1"] = equal_at_one
    ex = exact_scan(399, 2, 2); sidak = 1 - (1 - F(2, 399)) ** 2; bonf = min(F(1), 2 * F(2, 399))
    out["sidak_example"] = dict(exact=float(ex), sidak=float(sidak), bonferroni=float(bonf), exact_gt_gate=ex > F(1, 100), sidak_passes=sidak < F(1, 100), bonferroni_passes=bonf < F(1, 100))
    out["m369_scan_p"] = dict(exact=float(exact_scan(536, 87, 24)), binomial=float(binom_scan(536, 87, 24)))     # B1524's 0.9871 vs 0.9857
    ok = under and equal_at_one and ex > F(1, 100) and sidak < F(1, 100) and not (bonf < F(1, 100)) and abs(out["m369_scan_p"]["exact"] - 0.9871) < 5e-4 and abs(out["m369_scan_p"]["binomial"] - 0.9857) < 5e-4
    out["verdict"] = "PASS" if ok else "FAIL"
    json.dump(out, open(HERE / "bar_contract_checks.json", "w"), indent=1)
    print(json.dumps(out, indent=1)); print("VERDICT bar-contract-checks: %s" % out["verdict"]); return 0 if ok else 1
if __name__ == "__main__":
    sys.exit(main())
