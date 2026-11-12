# Card `A2-R79b`: Verify `main`'s Answers to `A2-R79` and Read Cross-Reader Mends at `896cae025238cda82304de7424bf05f83cb69abe`

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R79b` (requested and pre-approved on commit in `docs/seats/agy-002.md` under `M6`)
- **Commit of `main` read:** `896cae025238cda82304de7424bf05f83cb69abe` (mend diff base `0dda7b4725f613dbef273edafcd3fca73ccb245c`)
- **Protocol anchor:** `docs/seats/README.md` §§ 6, 7, 9, 12, and 13; `TERMINOLOGY.md`; `WORKING_RULES.md`

---

## 1. The Package and the Question, in One Sentence

At commit `896cae025238cda82304de7424bf05f83cb69abe` on `main` (relative to `0dda7b4725f613dbef273edafcd3fca73ccb245c`), do `main`'s recorded answers and mends in `"frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md"` completely and accurately resolve (or cleanly register on `P-812`) all twenty-six held findings of `A2-R79` (plus `R79-16` / `P-803`), and do the changes `main` landed in answer to other readers — across `B1882`, the notes and locks of `B1221` and `B1641` as they stand now, the verdict line of `B874`, and `frontier/B1861_the_closure_programme/verification/build_programme.py` — hold mathematically, enforce locks that genuinely fail when broken, and travel cleanly across every sibling file?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify`, in strict commit order:

1. **Pre-prose raw verification script and output** (`relays/r79b/verify_r79b_quotes_and_calcs.py` and `relays/r79b/verify_r79b_quotes_and_calcs_out.txt`), committed **before** writing `relays/REVIEW_79B_AGY-002.md` (`docs/seats/README.md` § 7 and § 12: `expectations committed first`), verifying:
   - every `exact quotation` cell byte-for-byte against `git show 896cae025238cda82304de7424bf05f83cb69abe:<file>`;
   - `git diff 0dda7b4725f613dbef273edafcd3fca73ccb245c 896cae025238cda82304de7424bf05f83cb69abe` for all twenty-six `A2-R79` findings and `ANSWERS.md` entries;
   - independent mathematical recomputation and adversarial mutation testing on `B1882`, the notes and locks of `B1221` and `B1641`, the verdict line of `B874`, `frontier/B1861_the_closure_programme/verification/build_programme.py`, and `B1892` (`ANSWERS.md` / `R79-16` / `P-803`).
2. **Follow-up review page** (`relays/REVIEW_79B_AGY-002.md`), formatted strictly per `docs/seats/README.md` § 13:
   - a four-column table (`arc | file | exact quotation | what is wrong, and how you know`) listing every answer that is wrong, every mend that is incomplete or left a non-failing lock/line standing beside it, and every fault found in `B1882`, `B1221`, `B1641`, `B874`, `build_programme.py`, or `B1892`, with counts and numbers in the fourth column written out in plain English words so nothing is obscured by `main`'s mask;
   - a concise ledger of `main`'s answers to our twenty-six `A2-R79` findings (identifying which closed cleanly, which are properly carried on `P-812`, and which remain open via rows in Section 1) and what was read cleanly with nothing further wrong.
3. **Updated seat status** (`relays/STATUS_AGY-002.md`) reflecting `read: M6` and final delivery state.

---

## 3. How It Could Come Out Wrong, Written Before Reading or Computing

1. **Accepting `ANSWERS.md` summaries without testing the landed diff and locks against mutations:**
   - As `M6` explicitly warns, a mend can add a missing count or assertion while leaving an earlier line that cannot fail standing beside it, drop a `max(...)` or boundary case in a corrected formula, or update one file while leaving a sibling `arc_verdict.json`, `THEOREM_REGISTRY.md`, `LAW_MAP.md`, `NODES.json`, or generated view stale. Every mended lock must be tested by mutating the invariant it claims to guard.
2. **Paraphrased quotations, broken table formatting, or unspelled numbers lost to `main`'s mask:**
   - Every `exact quotation` cell must be verified programmatically as a contiguous single-line substring of `896cae025238cda82304de7424bf05f83cb69abe:<file>`, every table line must have `pipe count == 5`, and every number in the explanation column must be written out in English words.
3. **Self-review or cross-reader contamination (`§ 13`, `P-781`):**
   - `agy-002` must continue to leave aside any part of `B1889` judging `agy`-family sessions (`agy`, `agy-002`, `agy-exp`), must not read any other session's branch or `REVIEW_79B_*.md` before pushing its own, and must use only the nine canonical check phrases of `docs/seats/README.md` § 12 (`P-797`).

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` at `896cae025238cda82304de7424bf05f83cb69abe` (diff base `0dda7b4725f613dbef273edafcd3fca73ccb245c`): `"frontier/B1892_review_79_read_by_those_who_did_not_build_it/"`, the mended files of our twenty-six `A2-R79` findings, `B1882`, `B1221`, `B1641`, `B874`, `frontier/B1861_the_closure_programme/verification/build_programme.py`, `docs/progress/REVIEWS.md`, and `docs/POINT_REGISTER.md` (`P-803`, `P-812`).
- **Must not touch:** Any file outside `relays/`; any other session's branch or review file before pushing our own; any `agy`-family assessment in `B1889`; any measured physical value or held-out target (`0 of 19`).

---

## 5. Control That Must Fail If the Work Is Broken

- **Planted Control 1 (Single-Word Quotation Mutation):** Mutating one word of a real line from `896cae025238cda82304de7424bf05f83cb69abe` must be caught and refused by the exact-quotation verifier in `verify_r79b_quotes_and_calcs.py`.
- **Planted Control 2 (Non-Failing Lock Assertion Detector):** Mutating the guarded target text or formula in synthetic copies of the mended locks (`B1221`, `B1641`, `B1882`, `B1886`, `B1889`, `B1861`) must distinguish assertions that genuinely fail on broken state from tautological or shadowed assertions that pass regardless of target corruption.

---

## 6. What Is Needed From `main` or From Another Seat

- Nothing (`M6` approves `A2-R79b` upon commit).

0 of 19.
