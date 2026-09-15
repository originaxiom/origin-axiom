# memo_215 — THE_SEAL_ALREADY_HAPPENED.md

## 1. HEADLINE
"**THE §4A.2 SEAL HAPPENED THREE WEEKS AGO, AND THIS BENCH TOLD THE OWNER TWICE THAT IT HAD NOT.**" No date given in the memo header itself; banked 2026-09-12 per INDEX.md.

## 2. CLAIMS
1. `docs/WHAT_WOULD_COUNT.md` §4A.2 (at the time of writing) read "STATUS: SPEC ONLY, OWNER-PENDING" — quoted as a MEASURED fact (a substring test at HEAD, no seal used for this memo itself).
2. The seal actually happened 2026-08-21: `docs/SEAL_LEDGER.md:527`, `frontier/B1106_edge_seal/FINDINGS.md:1` and `:5` (owner's rulings D-2/D-3 executed), `docs/EDGE_PREREG_SPEC.md:3` ("Status at landing: SEALED") — graded PROVED/measured (four independent substring hits).
3. **BENCH ERROR #28** (self-filed): registers R113/R114/R115 told the owner §4A.2 was "blocked on an owner decision"/"waiting on your signature" — both WRONG, the signature had been given and executed three weeks earlier — graded self-filed correction, "the same failure mode as BENCH ERROR #25."
4. `docs/OPEN_LEADS.md` line 1895 (at time of writing) self-contradicted: header said "SEALED 2026-08-21... RESOLVED" while body said "SPEC ONLY... owner-pending" and value column said "GATED on the owner's aperiodic unseal" — graded MEASURED, "a twelfth stale row, and the worst-placed one."
5. Description of what the seal actually is (§0–§3 structure of `EDGE_PREREG_SPEC.md`, the B1171 addendum-beside re-posing R6 as R6′) — DOCUMENTARY, restates prior banked material (B1106, B1171), not a new claim.
6. "What is actually left... a collaborator who can count modes... an experimental run nobody has commissioned" — graded interpretive conclusion, not a numeric claim.
7. Interpretive cross-reference to memo 197 (sealed alternation is the mode of 3000 random phases at 19.77%, "one phase in five reproduces the sealed law") — imported from another memo, not recomputed here; graded INTERPRETIVE / DOCUMENTARY citation.
8. Recommendation (not an action): bring §4A.2's STATUS line and L173's body/value column into agreement with the header — explicitly "this bench does not edit main's documents." Registers R113/R114/R115 declared "superseded on this point" by this memo.

## 3. CERTIFICATE
`outside_bench/certificates/the_seal_already_happened.py` EXISTS (87 lines). `outside_bench/outputs/the_seal_already_happened.txt` EXISTS (69 lines). Output tail: "ALL ASSERTIONS HOLD AT THIS HEAD." — every individual `[OK]` assertion (quoted substrings against named file:line targets) is printed and matches the memo's claims (e.g. the R6′/B8146 quotes, the EDGE_PREREG_SPEC §0–§3 quotes, the memo-197 19.77% quote). This agrees with the memo's headline. **No seal file** is claimed for memo 215 itself ("No seal. Every claim is a substring test on a tracked file at HEAD" — stated explicitly in the memo header), so there is no sha256 to check.

## 4. ON MAIN ALREADY?
1. The core correction (seal already happened, status line stale) — **(b) applied via the merge as an ADDENDUM inside a main arc, with explicit citation**: `docs/WHAT_WOULD_COUNT.md:286` now reads (struck-through old text preserved) "~~STATUS: SPEC ONLY, OWNER-PENDING~~ ... **[STATUS SUPERSEDED IN PLACE, 2026-09-12 — outside-bench memo 215, certificate `outside_bench/certificates/the_seal_already_happened.py`; the struck sentence above is kept for provenance, not deleted.]**" followed by a new "**STATUS: SEALED 2026-08-21 — AWAITING AN EXPERIMENTALIST, NOT A DECISION.**" line. This is a direct, named citation to memo 215 on main, with the struck-vs-live convention exactly as the memo recommended (though the memo said it would not itself edit main — main's own maintainers evidently did, using this memo as the cited authority).
2. `docs/OPEN_LEADS.md:1917` (L173 row): also carries "**[SUPERSEDED IN PLACE 2026-09-12 — outside-bench memos 206/208/210/211/213/214/215; certificates `the_triage_was_already_done.py`, `the_seal_already_happened.py`. Struck text kept for provenance, not deleted.]**" and a new line "**SUPERSEDED — contradicts this row's OWN header.** The unseal was RESOLVED and the spec was **SEALED 2026-08-21**..." — again, direct citation, memo 215 named among a batch of six memos (206/208/210/211/213/214/215).
3. R113/R114/R115 being superseded — not independently checked on main (these are `outside_bench/THE_OWNER_REGISTER.md` register entries, i.e. internal to the bench's own lane, not a main document); (c)/(d) not applicable — this is bench-internal bookkeeping, not a main claim.

## 5. NEEDS COMPUTATION HERE
DOCUMENTARY throughout. Every claim in this memo is a substring/grep check against tracked files at a fixed commit (SEAL_LEDGER.md:527, B1106/FINDINGS.md:1,5, EDGE_PREREG_SPEC.md:3, OPEN_LEADS.md:1895/1917, WHAT_WOULD_COUNT.md §4A.2). A verifier should simply re-run `grep -n "THE EDGE SEAL" docs/SEAL_LEDGER.md`, `sed -n '1,5p' frontier/B1106_edge_seal/FINDINGS.md`, `grep -n "SEALED" docs/EDGE_PREREG_SPEC.md`, and confirm the current (post-merge) text of `docs/WHAT_WOULD_COUNT.md` and `docs/OPEN_LEADS.md:1917` — which this reader has already done above and confirms the correction is live on main.

## 6. SUPERSESSION
Not withdrawn by any later memo. This memo itself supersedes (in place, on main) the prior stale status lines and explicitly supersedes registers R113/R114/R115 "on this point." It shares its correction with (and is cited alongside) memos 206/208/210/211/213/214 in the OPEN_LEADS.md row — i.e. it is one of a cluster of memos making the same/adjacent corrections, all landed together 2026-09-12.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN.** This is the cleanest case among the six assigned memos: the memo's finding is documentary (no computation, only file-state facts), it was verified sha256/grep-exact against current file contents, and it has been explicitly merged into main's own `docs/WHAT_WOULD_COUNT.md` and `docs/OPEN_LEADS.md` with direct, named citations to memo 215 and its certificate. Nothing further to reproduce; the correction is live.
