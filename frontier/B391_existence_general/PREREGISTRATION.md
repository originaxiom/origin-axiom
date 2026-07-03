# B391 (W4) — PRE-REGISTRATION: the existence law at general N

**Committed before computation. Target: upgrade P63 from duel-verified to a general-N
statement with an explicit proved-vs-computational split. Time-box: 2 sessions.**

## The lemma list (what the general statement rests on)

- **L-A (CRT tensor theorem):** the level-N theta model tensor-factorizes over the prime
  powers of N with the banked multiplier convention. STATUS: proven cell-wise at N=15 for
  all pairs (P66/P67 work, 13/13); the general-N statement is the same construction —
  claimed as PROVED-BY-CONSTRUCTION at the model level (the operators are literal tensor
  products), with the level-15 verifications as its exact witnesses.
- **L-B (local classification, 3-side):** at q = 3^k the local model has a helicity DOUBLET
  iff k is odd, at exponents ±(ord/4) with ord = 4·3^(k−1) (the P59 Pisano order), phase
  90°; and an invariant line always (exponent 0). STATUS: census-verified k ≤ 4 (3,9,27,81);
  **this wave extends to k = 5 (q = 243) — REGISTERED PREDICTION: doublet EXISTS at
  exponents ±81 of ord 324, phase 90°.**
- **L-C (local classification, 5-side):** at q = 5^k doublets exist iff k is odd (phase 36°
  or 108° by the QR class of the multiplier mod 5), ord = 2·5^k; lines iff k is even.
  STATUS: census-verified k ≤ 3 (5, 25, 125); **this wave extends to k = 4 (q = 625) —
  REGISTERED PREDICTION: NO doublet; invariant line at exponent 0 of ord 1250.**
- **L-D (the assembly):** sector@N = (line at one factor) ⊗ (doublet at the other) — the
  banked v2 law (P63), predictive 9/9 at the duel.

## The verdicts this wave banks

Each prediction is two-outcome (a hit extends the classification's verified range to
k ≤ 5 / k ≤ 4 and the general statement's induction base; a miss KILLS the odd/even-power
law at the first untested rung — a major structural event). The general-N claim after this
wave: L-A proved-by-construction, L-B/L-C verified through the extended bases with the
INDUCTION STEP still computational-per-rung (named honestly as the remaining gap — a proof
of the local classification for all k needs the metaplectic local structure at wild
ramification, flagged for the specialist register if it resists one session's attempt).

Machinery: numpy F_p census (small primes p ≡ 1 mod 4q, overflow-checked), the
local_censuses.py logic ported to numpy; 2 primes cross-check. The 405-trap rule: q | p−1
verified explicitly. Locks from output JSON. Firewalled.
