# Memo 223 — THE_PRICE_IS_TWELVE.md

## 1. HEADLINE

"THE PRICE, ELABORATED — and it is TWELVE, not eleven." Occasion: owner asked "what arw the 11
irreducible inputs, elaborate." Banked per INDEX.md row 223: "1B, banked 2026-09-13."

## 2. CLAIMS

1. **Correction, first**: the bench had told the owner "11" twice (status answer + register
   R131), quoting `docs/THE_SM_VERDICT.md`'s stale "4+7=11". **Live count, recomputed: 4 axioms
   + 8 irreducible sources = 12**, over **18 rows outstanding** (was 4+10=14). Grade: computed,
   supersedes the bench's own prior answer.
2. Two independent surfaces (the ledger table and `IDENTIFICATION_BASELINE.json`) AGREE on the
   unearned set — so 14 (rows outstanding minus axioms) is not a parsing artifact. Grade:
   cross-checked.
3. **Four axioms** (C3 being-is-inexhaustible-description, C4 the once-punctured-torus carrier,
   C5 orientation-preserving monodromy, C18 the observer's closings) with priced alternatives (F2,
   F8 GEOMETRY-NECESSARY, F5 FRAGILE, whole-observer-side respectively). Grade: documentary,
   quoted from `docs/THE_END_TO_END_CHAIN.md`'s forcedness census (B1123: 39/43 links FORCED).
4. **Eight irreducible sources**, computed via B1266's own union-find re-run on the LIVE ledger
   (not cited from the 2026-09-06 result): (1) the listener map `u` = I-13+I-18+I-23+I-29 (four
   rows, one debt); (2) the fork I-10+I-11 (E₆(-14)/E₆(-26), rank-obstructed per B1265); (3) the
   closer's frame I-27+I-28+I-30 (B1296's singular-frame chiral spectrum, registered UNEARNED at
   creation); (4) I-6 (2T→ALE map, multiplicity paid but map unpaid); (5) I-7 (object's ℤ/3 ≡
   boundary CFT module group); (6) I-14 (B305 grading ℤ/3 ≡ Eisenstein unit, upgraded at B1264);
   (7) I-25 (principal sl₂ embedding, declared never varied, exact stake h¹=3=2chiral+1abelian);
   (8) I-26 (dim H¹ ≡ generation count, price restated geometric at B1290: needs χ(∂⁺M)≠0).
   Grade: each **UNEARNED**, computed by union-find over the rows' own earning text.
5. Five dated raises since 2026-09-06 moved the count: I-26 (B1259), I-27 (B1296), I-28 (B1298),
   I-30 (B1321), I-29 (B1306 C) — each "by hand and dated," per the ratchet's own rule (no silent
   absorption). Grade: documentary, dated.
6. **"12 irreducible inputs bought 0 of the SM's 19 free parameters."** Grade: computed ratio,
   stated plainly.
7. **INTERPRETIVE**: the count rose because the accounting got more honest, not because the
   theory got worse — 4 of 5 raises are pre-existing debts newly NAMED, not newly created; a hard
   block would "make the fastest path to green marking things earned." Grade: labelled
   INTERPRETIVE.
8. **Controls**: C1 (non-vacuity — ignoring reduction edges gives 14 sources not 8, so the
   reduction does real work) PASS; C2 (B1266's two traps — I-25/I-1 and I-10/I-11 — still live in
   the data) PASS; C3 (the I-10/I-11 two-cycle collapses to ONE source) PASS. Grade: all PASS.
9. **Recommendation, not an action**: `docs/THE_SM_VERDICT.md` carries four stale strings
   ("4+7=11", "10 rows reduce to 7 irreducible", "11 = irreducible inputs", "14 = rows
   outstanding"); bringing them to 8/12/18 is "main's call," and the bench explicitly declines to
   edit `docs/` itself. Grade: recommendation.

## 3. CERTIFICATE

`outside_bench/certificates/the_price_is_twelve.py` and
`outside_bench/outputs/the_price_is_twelve.txt` both EXIST. No seal declared (structural read of
tracked files, rerunning B1266's own union-find live). Output tail:
```
C1: PASS
C2: PASS
C3: PASS
==============================================================================
 LIVE PRICE: 4 axioms + 8 irreducible sources = 12
             (18 rows outstanding) vs the SM's 19 free parameters
 verdict doc: 4 stale figure(s) struck for provenance, 0 still live
==============================================================================
```
"0 still live" here means: at the time this certificate was (re-)run, the 4 stale figures had
ALREADY been struck in `docs/THE_SM_VERDICT.md` — i.e. this output reflects the post-fix state
(see §4). It matches the memo's headline number (12) exactly.

## 4. ON MAIN ALREADY?

**(a) Already on main, with an explicit citation.** `docs/THE_SM_VERDICT.md:58-68` reads:
```
~~SPENDS 4 axioms + 10 UNEARNED identifications = 14 unpriced inputs ... 4 + 7 = 11~~
[NUMBERS SUPERSEDED IN PLACE 2026-09-13 — outside-bench memo 223, certificate
`outside_bench/certificates/the_price_is_twelve.py` ...]
LIVE: 4 axioms + 14 UNEARNED rows = 18 ROWS OUTSTANDING; 14 rows reduce to 8 IRREDUCIBLE
SOURCES, so the free-input count is 4 + 8 = 12. The ledger was raised five times after this
paragraph was written -- I-26 (B1259, 2026-09-06), I-27 (B1296, 2026-09-07), I-28 (B1298,
2026-09-08), I-30 (B1321, 2026-09-09), I-29 (B1306 C, 2026-09-09) ...
```
This is line-for-line the memo's own number and its own list of five raises, applied per
INDEX.md row 224 ("the owner-authorized FIX to `docs/THE_SM_VERDICT.md` — four stale figures
STRUCK IN PLACE, live figures stated"). The eight-source breakdown is also independently
documented on main at `frontier/B1266_the_source_of_input/FINDINGS.md` ("Live count: 11 rows →
8 sources; the irreducible price is 4 + 8 = 12") and `docs/CAMPAIGN_STATUS.md:~line near B1296`
("an eighth irreducible source, price 12"). The "18 rows outstanding" / "0 of 19 bought" figures
match too.

## 5. NEEDS COMPUTATION HERE

- **Claim 1/6 (the live count)**: DOCUMENTARY in the sense that it's a union-find over labeled
  text, but has a concrete recipe: run `frontier/B1266_the_source_of_input/verification/sources.py`
  (or `outside_bench/certificates/the_price_is_twelve.py`) against current
  `docs/IDENTIFICATION_BASELINE.json` and confirm `len(groups) == 8` and total unearned rows
  `== 14` (18 - 4 axioms). Expected: 8 sources, 12 total.
- **Claim 8, C1 (non-vacuity)**: recompute the union-find with the reduction edges (the rows'
  self-referential "paying X pays this" sentences) stripped out, and confirm the source count
  reverts to 14 (not 8) — i.e. the reduction is doing real collapsing work, not being vacuous.
- **Claim 8, C3**: confirm programmatically that I-10 and I-11's mutual reference forms exactly
  one 2-cycle in the dependency graph (not two independent edges) before collapsing to one source.

## 6. SUPERSESSION

The headline number (12) is not superseded — it is the number now standing on main. However the
memo's own text flags that its price may move again: "the ledger was raised five times... since
2026-09-06" (all captured before this memo), and nothing in INDEX.md rows 224-233 raises the
count further (row 224 "THE FIRST AXIOM" applies the fix; row 225's "Jorgensen" addendum
supersedes memo 224's *identification* of which theorem the owner meant, not the price; row 227
"THE CHAIN RIGHT NOW" quotes "the price, live (memo 223): 4 axioms + 8 irreducible sources = 12"
as still current). So as of the highest indexed memo (233), **12 still stands.**

## 7. GRADE PROPOSAL

**ALREADY-ON-MAIN.** The exact number, the five dated raises, and the four struck stale strings
are all now in `docs/THE_SM_VERDICT.md` with an explicit citation to this memo and certificate —
there is nothing left to bank; a verifier should re-run `the_price_is_twelve.py` periodically to
catch the next raise before it goes stale again.
