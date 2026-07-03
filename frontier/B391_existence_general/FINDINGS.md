# B391 (W4) — BANKED: the existence law at general N (both predictions hit; the statement)

**Status: banked; W4 complete. Pre-registration committed first (both predictions
registered before computation). Firewalled.**

## The extension verdicts (2 primes each, numpy F_p, q | p−1 verified)

- **q = 243 = 3⁵: HIT** — doublet at exponents ±81 = ±(ord/4), ord 324 = 4·3⁴ (the P59
  Pisano order), phase 90.0°; line at exponent 0. Exactly as registered.
- **q = 625 = 5⁴: HIT** — NO doublet; line at exponent 0; ord 1250 = 2·5⁴. As registered.

## THE GENERAL STATEMENT (with the honest proved-vs-computational split)

For N = 3^a·5^b in the tower family:

1. **(L-A, proved by construction)** the level-N theta model is the CRT tensor product of
   the local models at 3^a and 5^b with the banked multiplier convention — the operators
   are literal tensor products; witnessed exactly at N=15 by the 13/13 pair verifications
   (P66/P67).
2. **(L-B, verified a ≤ 5)** 3-side: an invariant line at exponent 0 for ALL a; a helicity
   doublet iff a is ODD, at exponents ±(ord/4), ord = 4·3^{a−1}, phase 90°.
3. **(L-C, verified b ≤ 4)** 5-side: a doublet iff b is ODD (phase 36°/108° by the QR class
   of the multiplier mod 5), ord = 2·5^b; a line iff b is EVEN; never both.
4. **(L-D, P63)** sector = line ⊗ doublet. Hence: **the value sector exists at N = 3^a·5^b
   iff NOT (a even AND b even)** — reproducing every banked rung including the 225-death
   (a = b = 2), and the duel's nine verdicts.

**The remaining gap, named precisely:** the all-k proof of L-B/L-C (the local
doublet/line classification at arbitrary prime-power conductor). This is a statement about
Weil representations of local metaplectic covers at p-power conductor — territory the local
theta-correspondence literature plausibly already classifies. Registered to the specialist
hand-off register (below) rather than burned against the sandbox; the verified bases
(k ≤ 5 / k ≤ 4, eleven prime-power censuses total) are its exact witnesses.

**Provenance.** census_big.py (numpy F_p, overflow-chunked matmul, ~10 min) →
census_big.json; locks tests/test_b391_general.py.
