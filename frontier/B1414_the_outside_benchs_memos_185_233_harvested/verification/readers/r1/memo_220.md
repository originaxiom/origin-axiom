# Reader r1 — Memo 220 (THE_RESIDUAL_IS_DISCHARGED.md)

## 1. HEADLINE
"L72'S UNIQUENESS RESIDUAL IS DISCHARGED, AND THE OBVIOUS ROUTE WOULD HAVE BEEN WRONG."
No CELL grades given (a literature-verification memo, not a computation cell); described as
"No seal." Date **2026-09-13** (banked per INDEX.md).

## 2. CLAIMS
1. RSW §5.3.6 fusion rules (`α²=1+β, αβ=α+β, β²=1+α+β`) computed from Verlinde on the
   rebuilt E₆ level-2 stage are **IDENTICAL** to the quoted source. Grade: **CHECK 1 PASS**.
2. RSW Theorem 3.2(3) quantum dimensions (`d₁=2.246979604…`, `d₂=2cos(π/7)=1.801937736…`)
   match this bench's centraliser dims **1, 1.801937736, 2.246979604** to every printed digit.
   Grade: **CHECK 2 PASS**.
3. RSW's representative has twists `h=0,1/7,5/7`; the bench's are `h=0,2/7,6/7`; **complex
   conjugation maps one exactly onto the other**, consistent with memo 211 CELL 3 (`k′=1`
   matched at 1.1e−15, `k′=6` rejected at 8.4e−2/8.7e−1). Grade: **CHECK 3 PASS**.
4. RSW §5.4 verbatim: "all unitary MTCs are the one listed... and those from the two
   symmetries S→−S and complex conjugate" — an **unconditional, complete realization
   classification** for this fusion rule. Grade: **CHECK 4 PASS — the discharge**.
5. **The residual is DISCHARGED**: "constructed + verified, not classified" → **classified**,
   against a complete list, not a uniqueness heuristic.
6. Interpretive claim: the "obvious route" (citing RSW's own conjecture, §2, "modular data
   determines the MTC") **would have been WRONG** — that conjecture is stated by RSW
   themselves as unproven ("very likely") and is **false in general** (Mignard–Schauenburg,
   smallest counterexample rank 49). Grade: **DOCUMENTARY / methodological**.
7. RSW Table 3 lists `(E₆,k), k=1,2` at ranks 3 and 9 — matching what memos 206/211
   independently rebuilt from the Cartan matrix, "neither consulted for the other." Grade:
   **free confirmation, DOCUMENTARY**.
8. Scope: RSW classify **unitary** MTCs; unitarity of the ambient E₆ level-2 WZW category is
   **cited, not proved here**. Discharge is about F-symbol uniqueness-up-to-gauge only; "memo
   218 already showed no reported number depends on them." Grade: **explicit fence**.
9. **Memo 219 §5 is SUPERSEDED ON THIS POINT** (its "still not discharged... unreachable"
   verdict); its egress-block measurement itself stands unchanged.

## 3. CERTIFICATE
- `certificates/l72_residual_discharged.py` — **EXISTS**.
- `outputs/l72_residual_discharged.txt` — **EXISTS**. Tail: "ALL FOUR CHECKS PASS," matching
  the headline exactly (checks 1–4 all reported passing, including the RSW-conjecture caveat
  language reproduced near-verbatim).
- No seal — the memo itself states this explicitly ("No seal: verifies a computed object
  against statements read verbatim..."), consistent with the file listing (no
  `L72...PREREG` or similar seal file was found under `outside_bench/seals/` for this memo).

## 4. ON MAIN ALREADY?
- **(b) applied via the merge as an ADDENDUM inside a main arc, but INCOMPLETE / STALE**:
  `docs/OPEN_LEADS.md:531`, the L72 row, already carries a **2026-09-12** "SUPERSEDED IN
  PLACE" strike-and-note citing outside-bench memos 206/208/210/211/213/214/215, ending with
  the residual exactly as memo 220 frames it: *"Phase 3 is WALLED/EXTERNAL... Residual
  'uniqueness-up-to-gauge... not classified': memo 211 closed the Galois ambiguity... 
  classification still needs the rank ≤ 4 classification from the literature."* Memo 220
  (2026-09-13, one day later) is precisely the answer to that last sentence, but **the
  OPEN_LEADS.md row has not been updated past 2026-09-12** — no citation to memo 220, RSW, or
  arXiv:0712.1377 was found there or anywhere else on main.
- **(c) NOT on main**: grep for `0712.1377`, `Rowell.Stong.Wang`/`Rowell-Stong-Wang` across
  `frontier/` and `docs/` (excluding `outside_bench/`) returns **zero hits**. The RSW paper's
  content (fusion rules, Table 3, §5.4's classification sentence, the §2 conjecture caveat)
  is not cited anywhere on main.
- No contradiction with main; memo 220 is a strict continuation/closure of the exact residual
  main's own L72 row already names as outstanding.

## 5. NEEDS COMPUTATION HERE
1. Claims 1–3 (fusion rules, quantum dims, twists) are internal reproductions of memos
   206/211's own rebuilt E₆-level-2 Verlinde data — a verifier should re-run the Verlinde
   formula on the E₆ level-2 Cartan data (as memo 206/211 built it) and confirm the same
   fusion rules and dims to the same digit precision; this is DOCUMENTARY with respect to
   memo 220 itself (it is a literature-comparison, not a new derivation) but the underlying
   Verlinde computation is a discriminating fact: recompute S,T for the rank-3 centraliser
   and confirm `d₁,d₂` to 9 significant figures.
2. Claim 4 (RSW §5.4 sentence): DOCUMENTARY — verify the quoted sentence appears verbatim on
   the supplied PDF (arXiv:0712.1377v4) at §5.4, and that §2's conjecture caveat and the
   Mignard–Schauenburg rank-49 counterexample citation are both real and correctly
   characterized (i.e. RSW's own words really do call it "very likely," not proven).
3. Claim 7 (Table 3 listing `(E₆,k) k=1,2` at ranks 3,9): DOCUMENTARY — confirm Table 3 in the
   PDF lists these two entries at these two ranks.

## 6. SUPERSESSION
Memo 220 **supersedes memo 219 §5 in place** (memo 219's "unreachable, not discharged"
verdict on this specific residual), per its own §6 and per the addendum-1 pointer recorded in
INDEX.md's row for 220 ("addendum 1 to memos/PARI_ARRIVES_AND_THE_LITERATURE_WALL.md").
No later memo (through 224, the last of r1's assignment) or owner-register entry retracts
memo 220 itself. On main, `docs/OPEN_LEADS.md:531`'s L72 row is now **stale relative to memo
220** and is the concrete next-update target.

## 7. GRADE PROPOSAL
**REGISTER**, with a specific, actionable follow-up: this is a documentary literature-
verification memo (no new arithmetic invariant computed; CHECKS 1–3 reproduce prior bench
results and CHECK 4 quotes a paper). It should be **applied as the missing update to
`docs/OPEN_LEADS.md:531`'s L72 row** — the row already anticipates exactly this closure and
currently understates the state of the art by one day. This is the single most actionable
finding among r1's five memos: a concrete, low-cost doc edit that closes an open row main
itself flagged as pending literature.
