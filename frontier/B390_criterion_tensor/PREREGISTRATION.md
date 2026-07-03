# B390 (W3.iii) — PRE-REGISTRATION: the bright/dark criterion via the tensor split

**Committed before computation. The route: by the tensor identity (B386/P66 pattern,
convention (u₃,u₅) = (2,2)), each pair's Par-table is C = C₃·C₅ cell-wise, so its DFT
t-table is the CONVOLUTION of the two local spectra: t = t₃ ⋆ t₅. The s-component (√−15 =
√−3·√5) of any cell is assembled from (√−3-content of the 3-side spectrum) × (√5-content of
the 5-side spectrum) under convolution + Π_H bookkeeping (handled exactly in-engine, never
by hand — the standing hazard).**

## Registered gates and criterion

- **G1 (tensor gate per pair):** C = C₃·C₅ holds cell-wise at (2,2) for ALL 12 banked pairs
  (it is proven only for (1,2) so far). KILL: any pair fails (then the criterion route dies
  here and the failure pattern is the finding).
- **G2 (the reconstruction gate):** the banked s-darkness verdicts (7 bright / 5 dark) are
  reproduced from the LOCAL DATA ALONE: compute t = t₃ ⋆ t₅ exactly from the local tables,
  project Π_H, read the s-table; 12/12 must match the banked classification.
- **THE CRITERION (the deliverable):** the per-pair attribution — for each dark pair, WHICH
  mechanism kills the s-channel:
    (D-a) the 5-side spectrum has no √5-content (predicted for seeds ≡ 0 mod 5);
    (D-b) the 3-side spectrum has no √−3-content;
    (D-c) both sides have content but the CONVOLUTION cancels (the subtle class — predicted
          for the riddle-adjacent pairs (1,3), (1,4)).
  Stated arithmetically per class, with the (1,3)-vs-(3,4) resolution exhibited.
- **OUT-OF-SAMPLE (registered before computing it):** pair (2,5) — the criterion predicts
  its class from local data alone (registered prediction: DARK by (D-a), seed 5 kills the
  5-side); then the full exact Par-table + DFT + s-check verifies. KILL: prediction wrong.

Machinery: the B386 local-model code (tensor_gate.local_partrace_table) at each pair's
(m₁,m₂); exact ζ₆₀ engine; locks from output JSONs. Time-box: this session + one more (W3
ends at session 3). Firewalled.
