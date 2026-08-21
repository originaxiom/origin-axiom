"""B1106 — the edge seal's genericity control (C-GEN), bite-controlled.

Convention pinned by the prereg (docs/EDGE_PREREG_SPEC.md §3): the Sturmian
letter b_n = floor((n+1)a + rho) - floor(na + rho) with rho = a; right hand =
(b_0 .. b_{N-1}); left hand read outward = (b_{-1}, b_{-2}, ...); the
reversal-closure identity is left_outward == reversed(right)  (B1095's banked
convention verbatim, tests/test_b1095_mirror_isospectral.py).

Positive control (must pass or every verdict below is void): the golden slope
1/phi^2 must reproduce the banked law -- closed at even Fibonacci index,
broken at exactly the two cut-adjacent letters at odd index.

The control: the strict silver analog 1/silver^2 = 3 - 2 sqrt2 at Pell
windows. Disclosure: the cousin slope 1 - 1/silver = 2 - sqrt2 mirrors the
golden alternation and is recorded as the known non-analog.

Writes b1106_gen_control.json. Exit 1 if the positive control fails.
"""
import json
import os
import sys
from math import floor, sqrt

PHI = (1 + sqrt(5)) / 2
GOLD = 2 - PHI            # 1/phi^2
SILV_STRICT = 3 - 2 * sqrt(2)   # 1/silver^2
SILV_COUSIN = 2 - sqrt(2)       # 1 - 1/silver (disclosed non-analog)

FIB = [233, 377, 610, 987, 1597, 2584, 4181]
FIB_IDX = {233: 13, 377: 14, 610: 15, 987: 16, 1597: 17, 2584: 18, 4181: 19}
PELL = [29, 70, 169, 408, 985, 2378, 5741]


def diffs(alpha, N):
    def b(n):
        return floor((n + 1) * alpha + alpha) - floor(n * alpha + alpha)
    r = [b(n) for n in range(N)]
    lo = [b(-n - 1) for n in range(N)]
    rr = r[::-1]
    return [i for i in range(N) if lo[i] != rr[i]]


def main():
    gold = {N: diffs(GOLD, N) for N in FIB}
    ok = all(
        (gold[N] == [] if FIB_IDX[N] % 2 == 0 else gold[N] == [0, 1])
        for N in FIB)
    silver = {N: diffs(SILV_STRICT, N) for N in PELL}
    cousin = {N: diffs(SILV_COUSIN, N) for N in PELL}
    silver_never_closes = all(len(v) > 0 for v in silver.values())
    out = {
        "positive_control_golden_law": ok,
        "golden": {str(N): v[:4] for N, v in gold.items()},
        "silver_strict_1_over_s2": {str(N): v[:4] for N, v in silver.items()},
        "silver_strict_never_closes": silver_never_closes,
        "silver_cousin_2_minus_sqrt2_disclosed": {
            str(N): v[:4] for N, v in cousin.items()},
        "verdict": ("C-GEN PASS: closure law golden-specific in the pinned "
                    "convention" if (ok and silver_never_closes) else "VOID/FAIL"),
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "b1106_gen_control.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"positive control (golden law): {ok}")
    print(f"silver strict never closes: {silver_never_closes}")
    print(out["verdict"])
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
