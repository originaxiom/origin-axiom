# B409 (Phase 2c) — PRE-REGISTRATION: the stratification-transport theorem

**Committed before computation. The plan's Phase-2c question: does B407 (per-pair table
anatomy) state something BEYOND P66/P67/M1, or fold in? Decided by an exact all-six-pairs
correspondence. No new heavy compute (banked tables + the M1 product machinery).**

## The candidate theorem

Per pair, the DFT'd t-table's imaginary anatomy (counts of cells with s≠0, and with z≠0)
EQUALS the pre-DFT convolution's product stratification (counts of X₃·X₅ products that are
s-carrying / z-only). I.e. the DFT + Π_H TRANSPORTS the stratum counts unchanged.

REGISTERED CHECK: for all six pairs, #(s-carrying t-cells) = #(s-carrying products) and
#(z-only t-cells) = #(z-only products). PASS on 6/6 ⇒ a genuine transport theorem (the
content beyond P67's zero/nonzero and M1's product strata is the COUNT CONSERVATION across
the Fourier+average step, which is NOT a priori — Π_H does not commute with the DFT, the
standing hazard). KILL: any pair where counts differ ⇒ B407 folds into P67/M1 as a
same-object restatement (bank the honest reduction).

Machinery: nesting.json (table anatomy, banked) + the M1 product-strata computation
(product_fields pattern) extended to all six pairs. Locks from the output JSON.
