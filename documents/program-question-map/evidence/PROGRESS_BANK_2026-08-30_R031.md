# Progress bank — 2026-08-30 — R031 sparse normalized toric trace

## Result

The normalized `dP6` dual trace used by the height-308 evaluator has exact
minimum support four:

```text
(1/4) * [012 + 023 + 034 + 045].
```

An exhaustive rational solve rejects all 20 one-entry, 190 two-entry and
1140 three-entry supports.  The four-entry trace is an exact dual cycle,
pairs with R027's marked top class as one, and differs from R027's cyclic
eight-entry trace by an explicit dual boundary.

Its signed shuffle product has 96 nonzero four-simplices, zero boundary and
unit pairing with the marked product generator.  This reduces the pending
residue contraction from 384 to 96 trace simplices without changing the
functional.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r031_sparse_toric_trace/sparse_toric_trace.py
```

## Boundary

No connecting entry is evaluated.  The remaining obligations are the frozen
`A_7/B_6/B_2` representatives, their common-frame determinant factor, the
direct `delta/f` trace contraction, and characteristic-zero/base-change
control for any modular nonvanishing or rank statement.
