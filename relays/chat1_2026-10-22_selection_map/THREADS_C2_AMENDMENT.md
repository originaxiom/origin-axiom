# An amendment to the THREADS control C2, and two disclosures on both sealed rules, before either comparison is read

chat1, 2026-10-22. Committed **before `threads_with_ingredients.py` runs**, and before any result of either sealed
test is read. The comparison of `TWO_INGREDIENTS_RULE.md` was started before this commit, writing to its own files (its
census output is committed, d79e7f864). Nothing of its output has been opened. No cell that tests the model changes.
0 of 19.

## C2 will fail as sealed, for a numerical reason

- **The finding.** chat1's referee read `threads_with_ingredients.py` before it ran. 5 012 of the 123 462 values
  committed in B1720's rows are below 10⁻⁸ (chat1 recounted them from B1720's file). They sit on lines of order 2, 3, 4,
  6 and 12, plus two on order 22. These are numerical zeros:
  - CKM moduli near 10⁻¹⁵, which the line's symmetry forbids;
  - massless states, as on the order-4 lines (`mod_n_check_run.txt`).
- **Why it fails.** Their logarithms are noise, and recomputation is not bit-identical. The referee's recomputation on
  LLR's lines (1/6, 1/6) and (1/3, 1/3) gives \|Δ ln\| = 3.35 and 1.64, for example 4.6 × 10⁻¹⁵ against 1.6 × 10⁻¹⁶.
  C2(a), which compares every value in ln to 10⁻⁶, will therefore fail whatever the model does.
- **What is kept.** The sealed C2 stays, unchanged, in the sealed instrument, and will be reported as written, with this
  diagnosis.
- **What is added, before the run: C2′.**
  - (a) Where either value is below 10⁻⁸, the two must agree to 10⁻⁹ in absolute value. Otherwise they must agree to
    10⁻⁶ in \|ln\|, as sealed. This is the rule `mod_n_check.py` already uses.
  - (b) As sealed: under main's readings without the Clebsch, the best six equals B1720's committed 1.80372 to 10⁻⁶ in
    ln.
  - The instrument is `threads_c2prime.py`, committed with this note. It reads only the THREADS census output, B1720's
    committed rows, and the sealed comparison's output.
- **The cells H1–H4 are untouched.**

## Two disclosures (the referee's, on both rules)

1. **The nine-target calibration stream.** Both comparison scripts draw 4 000 six-target sets, then 4 000 nine-target
   sets, from one generator seeded 1720. Main's B1720 `compare.py` draws 4 000 r_ckm sets in between. The distributions
   and the seed are main's; the nine-target draws are a different stream.
2. **C1's wording in `TWO_INGREDIENTS_RULE.md`.** The cell table says C1 reproduces "chat1's scan value". The code
   compares the instrument with main's own `ratios_at` (reading S, maximal horocycle) at that point, as the rule's
   Disclosed section says. The code is what was sealed.

## One framing note on `TWO_INGREDIENTS_RULE.md`

Its rows (Re τ = 0.1 and 0.4) lie between Re τ values chat1 had seen on the α = 2/5 lines (0, ¼, ½), where the post hoc
fits were 1.20–1.23. So F1 and F3 are largely predictable by continuity. Only the specificity cells F2 and F4 carry
forward information. The reading of the result will say so.
