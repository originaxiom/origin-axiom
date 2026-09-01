# R04 — recomputation of B863 (termination) + B994 (rule variation) over B861's menus

**Cell:** `reports/fresh_physics_seat_2026-09-01/recompute/R04_termination/` · **Date:** 2026-09-01
**Verdict: MATCH** (every banked number reproduced blind; one convention note under E23; one
provenance note on B994; one vacuity-shaped note on B994's headline clause, stated as a note,
not a verdict).

## Blind-first ledger

**Read BEFORE computing** (claim statement + menu content only):
- `frontier/B861_fused_cascade/FINDINGS.md`
- `frontier/B863_termination/FINDINGS.md`
- `frontier/B994_rule_variation/FINDINGS.md`

**Read AFTER my numbers were on disk** (`r04_blind_recompute.py` + `r04_blind_output.txt`):
- `frontier/B863_termination/termination.py`, `frontier/B861_fused_cascade/fused_cascade.py`
- `frontier/B863_termination/results.json`, `frontier/B994_rule_variation/results.json`,
  `frontier/B861_fused_cascade/results.json`
- `frontier/B994_rule_variation/arc_verdict.json`, `frontier/B863_termination/arc_verdict.json`
- `tests/test_b863_termination.py`, `tests/test_b861_fused_cascade.py`

My implementation is independent: own atom table (rep name → dim, conjugate), own branchings of
the 27 (each verified to sum to dim 27/15), own multiset-chirality test, exact integer/Fraction
arithmetic throughout, no measured SM values anywhere (Gate 5 clean).

## What I recomputed and what the bank says

**Registerability per option** (mine → banked, all agree):

| step | option (alg dim) | mine | banked |
|---|---|---|---|
| 1 | SO(10)×U(1) (46) | chiral ✓ | ✓ |
| 1 | SU(6)×SU(2) (38) | chiral ✓ | ✓ |
| 1 | Sp(8) (36) — 27 = traceless Λ²8, self-dual | vector-like ✗ | ✗ |
| 1 | SU(3)³ (24) | chiral ✓ | ✓ |
| 2 | SU(5)×U(1) (25) | chiral ✓ | ✓ |
| 2 | Pati-Salam (21) | chiral ✓ | ✓ |
| 3 | SU(4)×U(1) (16) — {6,4,4̄,1,…} self-conjugate | vector-like ✗ | ✗ |
| 3 | SM (12) — (3,2) unpaired | chiral ✓ | ✓ |

**B863 termination** (mine → banked, all agree): SM control chiral **YES**; descents
(a) su(2)→u(1): su(3)-content **{3:2, 3̄:2, 1:3}** vector-like (my multiset equals the banked
one exactly); (b) su(3)→su(2)×u(1) regular: my multiset {(2,2):1,(1,2):2,(2,1):2,(1,1):3} =
theirs, all self-conjugate, vector-like; (b′) principal su(3)₁→su(2)₄: my multiset
{(t3,2):1,(t3,1):2,(1,2):1,(1,1):1} = theirs, real/pseudoreal only, vector-like — and I
independently verified the conformal-embedding credentials: embedding index **4** (T(spin 1)/T(spin ½)
= 2/(1/2)), c(su(3)₁) = 8/4 = **2** = c(su(2)₄) = 12/6; (c) abelianization: trivially vector-like.
I additionally ran all four descents on the **full 27-content** at SM level (not just the 15-state
generation): all vector-like there too. → **SM terminal: reproduced.**

**B994 enumeration** (mine → banked, all agree): registerable options per step **[3, 2, 1]**;
selection-function chains = **6**; the six chains are exactly the banked six; endpoints =
{SM} only; max-dim and first-listed → **SO(10)×U(1) → SU(5)×U(1) → SM** (the banked B861 path);
min-dim and last-listed → **SU(3)³ → Pati-Salam → SM**. `sm_chain_share` = 1/6 ✓.

The repo's own locks (`test_b861_fused_cascade.py`, `test_b863_termination.py`) pass as
committed: 14 passed.

## E23 convention note (resolved — this is a MATCH, not a discrepancy)

B861's script tests the **16 alone** at step 2 and the **10+5̄ generation** at step 3; my blind
run used the **full 27-content** at every step (B861's FINDINGS §3 words: "the generation — the
27's matter content"). The verdicts agree at every option, and this is provable, not lucky:
`r04_postdiff_crosscheck.py` shows every difference multiset (the 27-content minus the arc's
slice) is **self-conjugate**, and adding a self-conjugate multiset never changes the chirality
verdict (conjugation is additive; Counter addition is cancellative). I also ran the arcs' exact
slice-objects through my instrument: same four verdicts.

## Controls (the instrument can find the excluded thing when planted)

- **C1** planted chiral content {3,1} under su(3) → instrument says chiral (True). ✓
- **C2** planted vector-like 5⊕5̄⊕1⊕1 at SM level → instrument kills it (False). ✓
- **C2b** 27-content minus the 10 (5⊕5̄⊕5̄⊕singlets) → correctly still chiral (net 5̄). A first
  draft of this control expected vector-like — my own error, the instrument was right.
- **C3** planted an extra registerable step-3 option → enumeration jumps to 12 chains and the
  endpoint set becomes {SM, FAKE-X}: the uniqueness claim **can fail** and the instrument sees it. ✓
- **C4** conjugation table is an involution and dim-preserving on every atom. ✓
- Positive control for termination = the SM itself passing (banked and reproduced).

## Notes for the bank

1. **Provenance gap on B994:** `frontier/B994_rule_variation/` contains FINDINGS.md,
   arc_verdict.json, and results.json but **no script**, and there is no `tests/test_b994_*` lock;
   a repo-wide grep finds no committed code producing that results.json. My independent
   re-enumeration reproduces every field of it exactly, so the numbers are right — but this
   PROVED arc's computation is otherwise unwitnessed by committed code.
2. **Vacuity-shaped note on B994's headline (not a VACUITY verdict):** "all six chains end at
   the SM" is combinatorially forced the moment the per-step registerable counts are [3,2,1]
   with the SM as step 3's sole survivor — the enumeration clause itself could not have found a
   non-SM endpoint. The falsifiable content lives in the **registerability classifications**
   (Sp(8) ✗, SU(4)×U(1) ✗), which I recomputed independently and whose failure modes control C3
   demonstrates. B994's own FINDINGS already concedes this ("the menu structure forces the
   endpoint"), so this is a sharpening, not a catch.
3. **Inherited fence, stated not resolved:** menu completeness (B873's P5 gate) is an input.
   Everything above is conditional on B861's menus being the complete list of registerable-eligible
   descents; a missing chain would break both the termination and the six-chain count silently.
   Likewise B861's flagged unresolved SU(3)₉ special embedding (dim 8; cannot move any winner)
   and B863's own "not exhaustive over exotic conformal embeddings" carve-out carry through.

## Files in this cell

- `r04_blind_recompute.py` — the blind recomputation (exact arithmetic, dimension-checked branchings)
- `r04_blind_output.txt` — its output, written before any arc script was opened
- `r04_postdiff_crosscheck.py` / `r04_postdiff_output.txt` — arcs' exact objects under my
  instrument + the self-conjugate-addition reconciliation lemma
