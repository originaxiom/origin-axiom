# Reader r7 — Memo 206 (`memos/WHO_CAN_HEAR_CHIRALITY.md`)

## 1. HEADLINE

"L78 ANSWERED, AND THE ROUTE COULD NEVER HAVE FAILED: who can hear chirality at level 2." No
explicit date line in the memo body itself; INDEX.md row 304 records it "banked 2026-09-12."
CELL 1 = A · CELL 2 = A · CELL 3 = A.

## 2. CLAIMS

1. L78 (`docs/OPEN_LEADS.md`, "OPEN — Round 2 first," ★★★★) was **already resolved** on the day
   it was registered: `frontier/B583_chiral_content/FINDINGS.md` §X3 (2026-07-14) states "L78
   resolves: the θ-odd amplitude is NOT reachable by Route A." Grade: documentary/pre-existing.
2. That level-2 rank-6 number had **no lock and no code** — `tests/test_b583_content.py` only
   tests the mechanism at level 1, in a 3×3 theater; the nine-primary claim stood in prose for
   two months. Grade: documentary gap-finding.
3. Stage rebuild from the Cartan matrix: `|W(E6)|=51840` exact; 3/9 integrable weights at
   levels 1/2; all gate checks (S symmetric/unitary, S² a 0/1 permutation, `(ST)^3=S^2`,
   Verlinde integral & non-negative, min quantum dim 1.0) pass to 1e-14 or better. Grade:
   control PASSED.
4. Corroborations: `h(27)` at level 1 = 2/3 exactly (= B569's proved value); `h(78)` at level 2
   = 6/7 = h∨/(k+h∨). `C := S²` **is** the E6 diagram flip (1↔6, 3↔5) as a permutation on the
   nine primaries' Weyl dimensions. Grade: computed exactly, asserted as a gate.
5. **CELL 1 = A**: B583 X3's level-2 rank 6 reproduces (1111 slopes vs its 719, θ-odd
   projection 2.14e-14, an order of magnitude tighter than the original 4e-13); level-1 control
   returns rank 2 (B580 Q1's banked number); rank stable across 39/287/1111 slopes (control C4).
   Grade: OUTCOME A, reproduced.
6. **CELL 2 = A**: `C=S²` is central in the SL(2,Z) image and fixes the vacuum
   (`e0C=e0` to ~3e-15, `[C,S]=[C,T]≈0`) ⇒ Route A's "positive outcome" (rank > θ-even dim) was
   **algebraically excluded from the start**, in any modular tensor category. So L78 as
   registered failed MB12 (couldn't both pass and fail). Grade: OUTCOME A, interpretive/critical
   of the lead's own design.
7. **CELL 3 = A (new)**: "THE REACH LAW" — a primary observer hears chirality (θ-odd reach > 0)
   iff it is not self-conjugate under `C`, and if it hears any of it, it hears **all** of it
   (reach 0 for the three self-conjugate primaries {1,78,650}; reach 3-of-3 for all six
   `C`-paired primaries, max|proj|=0.6870). Pure chiral seeds `(e_i−e_{C(i)})/√2` give span rank
   exactly 3 (entirely inside θ-odd), leakage into θ-even = −9.1e-13. Control C3 (MB12
   transversality) confirms the instrument can report nonzero. Grade: OUTCOME A, computed not
   cited.
8. What is **not** settled: this computes reachability, not the amplitude value B580's Q3 asks
   for; and the "legitimacy" of a non-vacuum `27`-observer (WHAT_WOULD_COUNT §4A.1's "inserted
   closing" question) is explicitly left open. Grade: negative/scope statement.
9. **BENCH ERROR #25**: a previous turn wrongly named L78 "the highest-graded still-open lead"
   without reading the arc it pointed to; register R113 item 1 is superseded by this memo.
   Grade: self-correction filed at point of occurrence.
10. Two in-run defects caught before banking: nine primaries first printed under wrong labels
    (numbers right, labels from another arc's ordering); a Weyl-dimension pairing bug
    (`μ·Cα` instead of `μ·α`) that crashed loudly (`ZeroDivisionError`) rather than silently
    returning wrong numbers. Grade: caught-in-run, not a live defect.

## 3. CERTIFICATE

- `certificates/l78_route_a.py` — EXISTS. `outputs/l78_route_a.txt` — EXISTS; tail matches the
  memo's CELL 3 table verbatim (span ranks, θ-odd reach, singular values 47.138095, Frobenius²
  6666.000000 = captured = predicted, leakage −9.095e-13) and ends "DONE -- outcomes above;
  interpretation lives in the memo, not here."
- `seals/L78_ROUTE_A_PREREG.md` — EXISTS; **sha256 recomputed and matches exactly**:
  `bff5ed36d85880c5a667c54086aa28f88d0fd182f8ef2a9e517c59a2bf355edf`, committed/pushed before
  the certificate, as claimed.
- No ADDENDUM changed this seal (none present in the memo file).

## 4. ON MAIN ALREADY?

- **(b) Applied via the merge as an update inside `docs/OPEN_LEADS.md`.** L78's row
  (`docs/OPEN_LEADS.md:552`) now reads: struck original text, then "[SUPERSEDED IN PLACE
  2026-09-12 — outside-bench memos 206/208/210/211/213/214/215; certificates
  `the_triage_was_already_done.py`, `the_seal_already_happened.py`...]" followed by
  "**RESOLVED** — B666 cell T: ... B583's level-2 rank 6 had no lock and no code until memo 206
  reproduced it (1111 slopes vs its 719, θ-odd projection 2.1e−14), which also showed Route A's
  positive outcome was never available (C = S² is central and fixes the vacuum), and added the
  reach law..." — this is a verbatim, specific citation of memo 206's own findings (claim 5, 6,
  7), confirmed by direct file read at that line.
- `frontier/B583_chiral_content/FINDINGS.md` §X3 (2026-07-14) is quoted accurately by the memo;
  I did not independently re-derive it but its existence as the pre-registration source for
  claim 1 is corroborated by the OPEN_LEADS citation above.
- No `frontier/B*` arc directory appears to exist specifically titled for memo 206's own
  computation (e.g. no `frontier/B6xx_reach_law` or similar) — the harvesting into main took the
  form of a documentation update to `docs/OPEN_LEADS.md`, not a new frontier arc. Grep for
  "reach law", "WHO_CAN_HEAR", "hears chirality" outside `outside_bench/` finds only the
  `docs/OPEN_LEADS.md` hit above.

## 5. NEEDS COMPUTATION HERE

- Claim 5 (rank-6 reproduction): NEEDS COMPUTATION — a verifier should independently rebuild the
  `S`/`T` matrices from the E6 Cartan matrix and Kac–Peterson formula at k=1,2 and recompute the
  vacuum-seeded filling-covector rank at level 2 over an independent slope set (e.g. Q=45).
  Expected: rank exactly 6, θ-odd projection ~1e-14.
- Claim 6 (Route A structurally excluded): NEEDS COMPUTATION but is really an algebraic
  identity — verify `[S²,S]=0` and `S²·e0=e0` symbolically/exactly (not just numerically) for
  the E6 level-1/2 modular data; this is checkable exactly since `S` has closed-form
  root-of-unity entries.
- Claim 7 (reach law): NEEDS COMPUTATION — recompute θ-odd reach for a non-`C`-paired primary
  seed vs. a `C`-paired one and confirm the 0-or-3 dichotomy holds for at least one additional
  slope set not already tried (39, 287, 1111 were used; try e.g. 719 to match B583's own
  original set exactly).
- Claim 4 (`C` = diagram flip): DOCUMENTARY/gate-asserted but exactly checkable — recompute the
  36 positive roots' Weyl-dimension formula and confirm the permutation `[0,5,3,2,4,1,8,7,6]`
  equals the (1↔6,3↔5) diagram flip.

## 6. SUPERSESSION

- Not superseded — this memo IS itself the superseding event for L78's prior "OPEN" status
  (register R113 item 1 explicitly named superseded by this memo, per claim 9 and confirmed on
  main at `docs/OPEN_LEADS.md:552`).
- No later memo or arc contradicts memo 206's own findings; it is cited by name in the
  OPEN_LEADS supersession bracket alongside memos 208/210/211/213/214/215 as part of one
  batched 2026-09-12 write-back.

## 7. GRADE PROPOSAL

**ALREADY-ON-MAIN.** The memo's central claims (L78 resolved, rank-6 reproduced, Route-A
structurally excluded, the reach law) are already written back into `docs/OPEN_LEADS.md:552`
verbatim-in-substance, with explicit citation to memo 206. The underlying computation (CELL
1–3, seal-verified) is sound and independently reproducible cheaply, but there is no additional
banking action needed beyond what the merge already did — a verifier's remaining job is simply
to spot-check the numbers (§5), not to establish novelty or write-back.
