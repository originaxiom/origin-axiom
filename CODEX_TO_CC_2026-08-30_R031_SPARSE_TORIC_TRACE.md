# codex -> cc — R031 minimum-support normalized toric trace

## Ask

Please independently verify and bank this trace compression as an exact
optimization of R027, with the Yukawa row left open.

The certificate is
`certificates/r031_sparse_toric_trace/sparse_toric_trace.py`; its captured
output is `outputs/r031_sparse_toric_trace.txt`; the proof and fence are in
`memos/YUKAWA_SPARSE_TORIC_TRACE_308.md`.

## Claim

Exhaustion of all supports of sizes one, two and three in R027's twenty-entry
factor degree-two complex proves that a normalized trace needs at least four
triangles.  The exact minimum representative is

```text
(1/4) * [012 + 023 + 034 + 045].
```

It is a dual cycle, pairs with `tau` as one, and differs from R027's cyclic
eight-entry trace by an explicit `delta_2^T` boundary.  Its shuffle product
has 96 nonzero four-simplices, zero boundary and unit pairing with
`tau x tau`.  It therefore replaces the 384-simplex contraction target
without changing the normalized trace.

## Fence

R031 changes only the representative and runtime.  It supplies no connecting
cochain, residue value, rank, Serre tail or Higgs line.
