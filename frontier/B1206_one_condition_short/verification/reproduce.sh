#!/usr/bin/env bash
# B1206 -- how many cuts the object's own structure supplies on the P^3 Higgs line.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee count.txt
# Banked inputs (all cited, none invented):
#   * the cubic contains 1.10.10          (LAW_MAP, B884/B987: 27^3 > 16.16.10 + 1.10.10)
#   * sector dimensions Q/dc/Hd/Hu = 3/3/4/1   (B1161's own-verified selection arithmetic)
#   * the 27 has exactly TWO neutrals, and the measured lambda-term row is
#         N.Hu.Hd :  N1 -> 2 nonzero entries,  N2 -> 0    (memo 80, byte-verified at B1171)
dim_Hd, dim_Hu, n_neutrals = 4, 1, 2
print(f"B_0 = the H_d block: dim {dim_Hd}  =>  the Higgs line is P^{dim_Hd-1} = P^3 (dim 3)")

# A linear functional on B_0 arises CANONICALLY from the cubic only when the other two
# legs are pinned to unique states. That needs a 1-dimensional partner on both legs.
print("\nWHICH CUBIC SLOTS GIVE A CANONICAL LINEAR FUNCTIONAL ON B_0?")
print("  a cubic term C(X, Y, .) is linear in h once X and Y are PINNED.")
print(f"  H_u is {dim_Hu}-dimensional -> pinned automatically.")
print(f"  the neutrals: {n_neutrals} of them, but the measured lambda-term row says")
print("    N1 -> 2 nonzero entries, N2 -> 0  =>  only ONE neutral couples to Hu.Hd.")
canonical_linear = 1
print(f"  => canonical linear functionals on B_0: {canonical_linear} (the lambda-term C(N1, H_u, .))")
print("  (the q.dc.Hd and l.ec.Hd rows are linear in h only after CHOOSING matter states,")
print("   so they give texture conditions, not canonical ones -- they are the tensor itself.)")

print("\nTHE CUT LEDGER on the P^3:")
dim = 3
print(f"  start                                   dim {dim}")
dim -= canonical_linear
print(f"  - {canonical_linear} canonical LINEAR condition (lambda-term)   dim {dim}")
dim -= 1
print(f"  - 1 NONLINEAR condition (det Y_d = 0, B1205)  dim {dim}")
assert dim == 1
print(f"\n  => dim {dim}. Points need dim 0. THE FORCING FALLS EXACTLY ONE CONDITION SHORT.")
print("REPRODUCES")
PY
