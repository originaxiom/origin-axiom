# Reader r3 — memo 193 (THE_GUARD_THAT_CAUSED_THE_DAMAGE)

## 1. HEADLINE
"TWELVE RED TESTS ON A CLEAN MAIN, ALL TWELVE CLOSED — and the two causes are both
instruments damaging what they were written to protect." **2026-09-09.**

## 2. CLAIMS
1. `test_no_hardcoded_paths.py` (a textual guard) cannot see that the absolute-path
   cleanup replaced checkout prefixes with the documentation placeholder `"<repo>/"`,
   which is a dead path in code; **26 committed scripts** stopped working (B657×4,
   B663×1, B670×5, B673×1, B677×1, B771×5, B775×3, B787×2, B1306 sliceC×3). — **VERIFIED, repaired**
2. B1306 slice C's three re-derivations (C5, C2, C7) and B771 cell W3-084 **re-run
   green and rewrite committed outputs byte-identically** after the fix. — **VERIFIED BY RUNNING**
3. `.gitignore`'s LaTeX-intermediate rules (`*.out`,`*.log`,`*.jsonl`) matched at every
   depth and deleted evidence for **5 locks** (P3 manifest, B646 ORIGINALS_MANIFEST,
   B1062, B1063, B1137); the P3 manifest's own failure message told the reader to run
   `build_manifest.py`, which on a clone **deletes 20+ real entries**. — **VERIFIED, repaired** (negations added; before==after exactly after dropping only absent path-shaped entries)
4. Three B1062 logs regenerated from their own scripts, every pinned string
   reproducing exactly. — **VERIFIED**
5. B565 `test_snappy_gate` failure: SnapPy 3.3.2 returns the *other* SL(2,C) lift
   (χ(a)=−1, χ(b)=+1); representation unchanged. Gate rewritten to require **exactly
   one** of the four sign characters to reproduce all three pinned traces — **stronger, not weaker**. — **FIXED / VERIFIED**
6. B511/D3.3 failure (`0.0 > 0.8`) is loxodromic-overflow NaN (by step 79), not a
   claim failure; fixed by projecting to SU(2) each step; **the claim reproduces**:
   classical 0.895 > 0.8, wild 0.048 < 0.15, all three mixes concentrating. — **VERIFIED, reproduces**
7. B616: the lock has **never passed** — script prints "3 of 390" against a pinned
   "2 of 378"; checked by running the script in a worktree at the landing commit
   `d6eac1ed`, which also prints 3 of 390. Re-pinned to "3 of 390"; verdict
   STILL-AMBIGUOUS unchanged. — **VERIFIED, re-pinned**
8. One fragility flagged and **deliberately not patched**: B616's family cut
   `0 < val` is decided by the sign of rounding noise on 14 exact zeros between
   2e−32 and 7e−16 (main's call to re-pin, not this bench's). — **flagged, unresolved by design**
9. `test_no_email_addresses_or_reviewer_placeholders` fired on ordinary English
   ("a reviewer-facing verification package"); regex narrowed to identifier shapes. — **FIXED**
10. B1137: real grid recomputed (216 cells, 837s); `aggregate.py` returns
    `overall verdict = DISJOINT`, all 18 targets NONE — reproducing the banked claim.
    Null grid regeneration in progress; aggregate not to be re-run until it exists. — **VERIFIED, reproduces (partial — null grid pending)**
11. **ADDENDUM 1:** codex seat's 7 red tests are 2 preserved receipts, not defects —
    (a) a sympy structural-equality false negative on an algebraically-zero
    connection-matrix difference, already sealed by the seat's own test as a
    "preserved receipt"; (b) six failures are one fact (`geometry()`'s deliberate
    `ValueError`, sealed `HOLONOMY_EQUIVARIANCE_FAILURE.txt`). A geometric bridge
    (`is_isometric_to(..., return_isometries=True)`) supplies the missing interface;
    10/10 of the target tests pass on it. **Not pushed to their branch** — filed as a capability. — **withdrawn-as-defect / new capability found**
12. **ADDENDUM 2:** codex lands R24 (boundary charge = sign(q)·k) and R25
    (compensating wall, net index −k); R25's own text: *"for k=3 this is a mirror
    sector, not a mirror-free completion"* — self-priced against its own interest. — **landed, self-priced (not a full win)**
13. A second, independent seat (`paper-verification-ufp0zn`) found the identical
    `<repo>` placeholder defect in `c_e8_types.py`, same day, no contact — confirming
    the defect class is real. — **CORROBORATED independently**
14. The paper (`papers/P3_THE_PAPER/main.tex`) still carried the **retracted**
    family-wide amphichirality sentence (B1181→B1235); corrected to 112
    members / 38 amphichiral / 74 chiral; rebuilt and handed to the owner. — **FIXED**

## 3. CERTIFICATE
`outside_bench/certificates/dead_placeholder_paths.py` exists.
`outside_bench/outputs/dead_placeholder_paths_out.txt` exists (not named in the
INDEX row's citation column, but present and dated with the other certs).
Its final lines: *"CELL 1 live '<repo>/' path literals remaining: 0 -> B ...
CELL 2 ... 26; ... 0 -> B ... CELL 3 ... B ... ALL CONTROLS PASSED. VERDICT: CELL 1
= B, CELL 2 = B, CELL 3 = B — no dead placeholder path remains."* This **agrees**
with the memo's headline. No seal is named for memo 193; sha256 check N/A.

## 4. ON MAIN ALREADY?
- Claim 1/repair: **(a) already on main.** `frontier/B1306_the_older_debt/verification/sliceC/c_e8_types.py:5` now carries `"<repo>/"` only inside a comment explaining it is a dead-path placeholder — the live literal is gone (confirmed by direct read).
- Claim 3/repair (.gitignore negations): **(a) already on main.** `.gitignore:25-26` (`!frontier/*/verification/*.out`, `!frontier/*/verification/*/*.out`), `:30-32` (B646/B1062/B1063 `.log` negations), `:99,102` (`.jsonl` negations).
- Claim 3 (manifest-stale message is a trap): **(a) already on main.** `tests/test_p3_verification_package.py:55-61` — the comment states exactly this reasoning and the assertion compares `_drop_absent_paths(b) == a` rather than trusting the builder blindly.
- Claim 5 (B565 gate strengthened): **(a) already on main.** `tests/test_b565_realform.py:50-83` — "find every sign character that works, and require exactly one."
- Claim 7/8 (B616 re-pin + fragility): **(a) already on main, and refined further.** `tests/test_b616_heldout.py:3-7` re-pins to "3 of 390 pairs" dated 2026-09-09 (matches memo exactly); a **later** comment at `:37-38` dated 2026-09-15 adds a platform-dependent-pin note (macOS bench prints "2 of 378") — main has moved on from this memo without contradicting it.
- Claim 14 (paper correction): **(a) already on main.** `papers/P3_THE_PAPER/main.tex:1058-1063` — "38 of the family's 112 members are amphichiral, not all... 38 are amphichiral and 74 are chiral. The earlier 'all members are amphichiral'..." matches the addendum's correction verbatim in substance.
- Claim 9 (regex fix), claim 2 (byte-identical re-runs), claim 10 (B1137 DISJOINT re-run), claim 11 (geometric-bridge capability filed but not pushed to the other seat's branch), claim 6 (B511 SU(2) projection fix): not independently re-checked byte-for-byte here (would require running scripts, out of the 2-minute budget), but the certificate output already reproduces the CELL 1-3 = B/B/B verdict and the surrounding repaired files (`.gitignore`, `test_b565_realform.py`, `test_p3_verification_package.py`, `test_b616_heldout.py`) are consistently in the repaired state on main — **(a) already on main, by the state of the files**, not independently re-run by this reader.

## 5. NEEDS COMPUTATION HERE
- Claim 2 (byte-identical re-run): re-run `frontier/B1306_the_older_debt/verification/sliceC/c_e8_types.py`, `c_geodir_h1.py`, `c_tits_lift.py` and diff their committed JSON outputs against HEAD — expect zero diff.
- Claim 6 (B511/D3.3): re-run the SU(2)-projected random-walk script for 60 steps and confirm no NaN and classical mix ≈ 0.895 (> 0.8 threshold).
- Claim 10 (B1137): re-run `frontier/B1137_regulator_probe`'s `aggregate.py` on the committed real grid and confirm `overall verdict = DISJOINT`.
- Claim 11 (geometric bridge): on `m202`, run `Q.is_isometric_to(K, return_isometries=True)` in SnapPy and confirm 12 isometries returned versus `Q.isomorphisms_to(K)` returning 0 — DOCUMENTARY otherwise (a capability claim, not a value).

## 6. SUPERSESSION
Not superseded. This memo's repairs are visibly still standing on main and one of
them (B616's pin) was extended by a later, unrelated main commit (2026-09-15
platform-dependent-pin note) without contradiction. No later outside-bench memo in
`INDEX.md` retracts memo 193.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** — every spot-checked repair (guard fix, `.gitignore` negations,
B565 gate, B616 re-pin, paper correction) is present in the current tree with a
verifiable file:line citation; the memo is an infrastructure-hygiene sweep whose
product is the repaired files themselves, already merged, not a standalone
computation awaiting a bank.
