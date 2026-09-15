# Reader r6 — memo 227 (outside_bench/memos/THE_CHAIN_RIGHT_NOW.md)

## 1. HEADLINE
"THE CHAIN RIGHT NOW: it completes as structure and hits a firewall." Banked 2026-09-13
(INDEX.md), occasioned by the owner's "how does the chain from minimal description to sm look
like? right now."

## 2. CLAIMS
1. The corpus's own census (`scripts/checks/forcedness_census.py`, run first per memo 154) PASSES
   at HEAD: 54 links total — 34 theorem, 8 no-go, 6 identity, 4 axiom, 1 census, 1 corollary — of
   which 50 are not axioms — grade: **PASS**, parsed from the checker's own output, not recalled.
2. Axioms sit at C3, C4, C5, C18 only; C6..C17 (the object through the two no-gos) contains not
   one declared choice — grade: PASS, same census.
3. The 15-row status reading (from `docs/THE_CHAIN_STATUS.md`): 6 derived (✅), 2 derived-but-
   generic (◐: row 3 ℚ(√−3)→2T→E₆; row 8 arena 252→2), 2 classical/literature (📖: arithmeticity,
   E₆ landing), 3 proved-unobtainable (🔒: hypercharge normalisation, all measured dimensionless
   values, scale), 3 absent (❌: three generations, Yukawas/masses/mixings, dynamics) — grade:
   parsed/counted from the status document, not independently re-derived here.
4. The document's own one-line reading, "verified present": "The chain does not thin out and stop
   — it completes as structure and hits a firewall" — grade: quoted-and-confirmed-present, not a
   new claim.
5. The two ◐ rows are named as the load-bearing weakness: row 3 "arriving does not confirm the
   earlier steps"; row 8 is "arena-generic: zero object tokens in the computation" — grade:
   interpretive reading of the status document, labelled as such.
6. The live cost (memo 223): 4 axioms + 8 irreducible sources = 12, over 18 rows outstanding,
   buying 0 of the SM's 19 free parameters — grade: parsed number, cited from memo 223.
7. **Currency finding**: `docs/THE_CHAIN_STATUS.md` (adopted 2026-09-12, header claims "it lives
   on main") is **NOT on origin/main** as of the memo's writing — it existed only on
   `<remote>/paper-verification-ufp0zn` — grade: reported as an observation, not a defect, per the
   memo's own framing.

## 3. CERTIFICATE
- `certificates/the_chain_right_now.py` exists; `outputs/the_chain_right_now.txt` exists (both
  confirmed). The memo states no seal is used, since every number is parsed from a tracked file or
  produced by the corpus's own checker.
- Output tail: "54 links, 50 forced, axioms at C3/C4/C5/C18, C6..C17 axiom-free : True / the
  15-row status table is on a BRANCH, not on main : True / the cost: 4 axioms + 8 irreducible
  sources = 12, buying 0 of 19" — **AGREES** with the memo's headline and §1–4 verbatim.
- **Independently re-ran** `scripts/checks/forcedness_census.py` fresh on the current repo HEAD
  (2026-09-16, commit `3857877d`, well after this memo's 2026-09-13 banking date) as part of this
  review: it printed **the identical numbers** — "54 links... THEOREM 34, NO-GO 8, IDENTITY 6,
  AXIOM 4, CENSUS 1, COROLLARY 1... FORCED (non-axiom): 50 of 54... axioms at: [3, 4, 5, 18]...
  axioms in C6..C17: NONE... PASS." Claim 1–2 are **reproduced live, unchanged**, despite several
  more B-arcs (up through B1409+) having landed on main since this memo was banked — the census
  target (`docs/THEOREM_LEDGER.md`'s 54-link chain) has not grown in link count in the interim.

## 4. ON MAIN ALREADY?
- Claims 1–2 (54 links, 50 forced, axioms at C3/C4/C5/C18): **(a) already on main** — this is
  exactly `docs/THEOREM_LEDGER.md` read through the corpus's own committed checker
  (`scripts/checks/forcedness_census.py`, confirmed present and runnable on main HEAD). Not a new
  claim; a correct read-out of an existing main artifact.
- Claim 7 (the currency finding — **THIS IS NOW STALE, contradicted by main's current state**):
  **(c)→now effectively superseded by main's own subsequent history.** `docs/THE_CHAIN_STATUS.md`
  **does exist and is tracked on main today.** `git log --follow --diff-filter=A` shows it was
  added by commit `4d1cbb6b`, "B1339 the chain status ADOPTED..." dated 2026-09-12, and
  `git merge-base --is-ancestor 4d1cbb6b HEAD` confirms it **is an ancestor of the current HEAD**
  (`3857877d`, 2026-09-15). So the file that memo 227 (banked 2026-09-13) says "is NOT on
  origin/main... it exists only on `<remote>/paper-verification-ufp0zn`" **has since landed on
  main** — most likely via the 2026-09-15 consolidation referenced elsewhere in the record. This
  is not a contradiction of memo 227 at the time it was written (the owner register itself,
  `THE_OWNER_REGISTER.md:5148`, independently confirms the same "it does not [live on main]"
  reading as of that session), but a reader today should treat claim 7 as **resolved / no longer
  actionable**: the status document's own header claim ("it lives on main") is now simply true.
- Claims 3–6 (the 15-row table's content itself, and memo 223's cost accounting): by extension now
  **(a) on main**, since the document carrying them (`docs/THE_CHAIN_STATUS.md`) is on main. Not
  independently re-verified row-by-row against frontier arcs in this review (that would be a
  separate, larger audit); flagged here only as "the container is now present," not "every row is
  independently confirmed."

## 5. NEEDS COMPUTATION HERE
- Claims 1–2: DOCUMENTARY relative to a re-run, but trivially and cheaply reproducible — run
  `python3 scripts/checks/forcedness_census.py` (already done in this review; confirmed PASS with
  identical numbers). No further computation needed; this is as verified as a claim can get.
- Claim 6 (memo 223's cost: 4 axioms + 8 irreducible sources = 12, buying 0 of 19): DOCUMENTARY —
  re-derive by reading `docs/THE_CHAIN_STATUS.md`'s own §3 cost accounting and confirming the
  arithmetic 4+8=12 and the "0 of 19" count against the 15-row table's ❌/🔒 rows; a bookkeeping
  check, not a mathematical computation.
- Claim 3 (the two ◐ rows' genericity — row 3 and row 8): this is the one number-shaped
  discriminating fact worth independent recomputation — re-run whatever computation established
  "arena → content: 252 → 2" (row 8) with the object's own tokens stripped out, to confirm it
  really is "arena-generic" (i.e., that a generic rank-3-abelian-plus-15-plet arena, not just this
  object's, produces the same 252→2 reduction). If a verifier wants one thing to actually compute
  here, it is this.

## 6. SUPERSESSION
No later outside-bench memo revisits "THE_CHAIN_RIGHT_NOW" or memo 227 by name (INDEX rows
228–233 and owner register scanned; the one register hit at `THE_OWNER_REGISTER.md:4574`,
"Answer: memo 227, read out of the record rather than recalled," and the line at 5148 both *cite*
it as a correct diagnosis at the time, not a retraction). The memo is **effectively superseded by
main's own subsequent state** on its one currency claim (§4 above): `docs/THE_CHAIN_STATUS.md` has
since landed on main, closing the gap the memo flagged.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** (claims 1–2, and now claim 7's underlying document too) with one **REGISTER**
note: this memo's real service was a correct, cheap, honest snapshot of the chain's shape and a
currency catch (the status document's "it lives on main" claim was false when checked) — and that
catch has since been resolved by main's own progress, so nothing further needs to change on main
because of this memo. Worth a one-line note in the record (e.g. in `docs/THE_CHAIN_STATUS.md`'s
own currency block or `docs/CAMPAIGN_STATUS.md`) that the outside bench independently confirmed
the 54-link/50-forced count reproduces on a later HEAD, since that is a positive piece of
cross-lane verification that costs nothing to record.
