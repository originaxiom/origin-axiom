# ACCEPTANCE CRITERIA — what "fixed" means for the 2026-11-10 audit

**From:** the advisor seat. **To:** cc. **Kind:** `propose:` — the owner rules on the bar; cc may `challenge:` any row
with evidence.

This file states, for each finding in `ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md`, the test the advisor seat will
apply at re-audit. A finding is accepted when its test passes on a fresh full clone of main. A test is objective
wherever one exists; where it needs judgement, the row says so.

## 0. The standard

1. **A fix to enforcement is accepted only when a planted violation turns it red.** The violation is committed in a
   scratch clone, the gate or lock is run on the clean tree at that commit, and it fails. "The code now looks right"
   is not acceptance.
2. **A fix to a claim is accepted only when every surface that carries the claim has changed.** The advisor will grep
   for the old statement across the tree, not only at the path named in the finding.
3. **A fix may not weaken a result that was sound.** Section 2 of the findings lists what held; a fix that changes one
   of those items needs its own reason.
4. **Nothing is closed by relabelling alone.** Moving a row to DONE, raising a baseline, adding a path to an exemption
   list or adding a cue word to a line does not meet any row below.
5. **The repository's own rules bind the fixes:** append-only logs, no moved or renamed banked paths, corrections
   dated where they apply, the original text kept.

## 1. Order of work (recommended)

1. **Enforcement first** (sections 3.1, 3.2 of the findings), so that the later corrections are themselves guarded.
2. **The weave discipline** (3.9), because it changes the verdict schema that later rows fill in.
3. **Errors and labels** (3.3, 3.4), then **propagation** (3.5).
4. **The value layer** (3.6) before any new seal.
5. **Governance** (3.7) at the owner's ruling.

## 2. The planted-violation suite

Each row is a mutation to commit in a scratch clone of main. Today every one of them passes the named gate. The fix
is accepted when the gate fails on it, and when the mutation is part of an automated test that the suite runs.

| # | Planted violation | Gate that must fail | Finding |
|---|---|---|---|
| PV1 | delete lines 200–400 of `PROGRESS_LOG.md`, commit | `append-only` | G1 |
| PV2 | replace `PROGRESS_LOG.md` with one line, commit | `append-only` | G1 |
| PV3 | append one sentence to `frontier/B1841_the_principled_ends_card/PREREGISTRATION.md`, commit | a seal gate | G2 |
| PV4 | delete a sealed pre-registration that the ledger covers, commit | a seal gate | G2 |
| PV5 | edit a sealed file and append a ledger row carrying the new digest, same commit | a seal gate | G2 |
| PV6 | hand-edit one generated row's sha8 in `docs/SEAL_LEDGER.md` | `seal-ledger-current` | G2 |
| PV7 | remove the generated rows of `docs/SEAL_LEDGER.md` and regenerate twice | the two runs agree, and neither reports "0 unrecorded" by reading the ledger itself | G3 |
| PV8 | add an arc whose seal file is named `PREREG.md`, first committed with its `FINDINGS.md` | `seal-order-unshown` | G4 |
| PV9 | run the gates on a `git archive` export (no `.git`) | every gate that needs git reports FAIL or SKIPPED, never "ok" | G5 |
| PV10 | delete `docs/IDENTIFICATION_BASELINE.json`, add three UNEARNED rows | `identification-register` | G5 |
| PV11 | delete `docs/RETRACTED_PHRASES.md` | `retraction-sweep` | G5 |
| PV12 | delete every `tests/test_b*.py` | `test-vacuity` | G5 |
| PV13 | empty `docs/LAW_MAP.md` and `docs/THEOREM_LEDGER.md` | `law-map-provenance`, `chain-locks` | G5 |
| PV14 | truncate one `arc_verdict.json` to invalid JSON | `arc-data` (and no gate skips it silently) | G14 |
| PV15 | run the gates with the clock set 30, 60 and 365 days after HEAD's commit date | the consistency gates give the same result as on the commit day | G6 |
| PV16 | point every entry of `tests/GATE_CONTROLS.json` at a skipped trivial test | `gate-controls` | G7 |
| PV17 | paste two phrases from rows of `docs/RETRACTED_PHRASES.md` added after 2026-10-07 into `README.md` | `retraction-sweep` | G8 |
| PV18 | a commit whose message carries a co-author trailer naming a vendor | `attribution` (if the practice stays as worded) | G9 |
| PV19 | raise one count in `docs/ATTRIBUTION_BASELINE.json` and add that many tokens, same commit | `attribution` | G9 |
| PV20 | a PROVEN row in `CLAIMS.md` that cites no lock | `claims` | G10 |
| PV21 | a banned phrase in a `.tex` file, and a capitalised variant in `README.md` | `framing` | G10 |
| PV22 | run the gates on a depth-50 clone | each history-dependent gate reports that the clone is shallow; none passes with "0 stale" | G13 |
| PV23 | a new NEGATIVE claim line worded "the object cannot …" on a one-thread arc, plus one old line reworded | `member-scope` | W1 |
| PV24 | a test function whose only assert is `assert 1 != 2` | `test-vacuity` | L7 |
| PV25 | a lock that reads a file matched by `.gitignore` | a gate | L4 |
| PV26 | a lock that asserts `stdout == committed transcript` where the transcript prints a float | a gate | L6 |
| PV27 | a test run that writes to a tracked file | the suite (tree must be unchanged after it) | L10 |

## 3. Locks

| Finding | Accepted when |
|---|---|
| L1, L2 | Every lock declares a tier (RECOMPUTE / RERUN / TRANSCRIPT) and a gate checks the declaration against the file's content. Re-running `tools/lock_census.py` and `tools/lock_map.py` gives **zero** PROVED arcs in the dependency closure of any frame that is to be read against data whose locks are all TRANSCRIPT. For the rest of the record the count may only fall, as a named list. |
| L3 | Every `[THEOREM]` link of `docs/THEOREM_LEDGER.md` has a RECOMPUTE lock, and `chain-locks` reads the tier. |
| L4, L5, L6 | The named locks pass on a fresh clone, and each fails when the number it guards is changed in the script's output. |
| L7 | The 11 named tests are rewritten or removed; PV24 fails. |
| L8 | B892, B952 and B866 each contain the script that computes their headline, and their lock runs it. |
| L9 | The core suite fails, not skips, when SnapPy is absent — or the skip is counted and printed in the suite's summary. |
| L10 | PV27. |

**The mutation rule for the value chain:** for every arc in the closure named in L1, the advisor will change one
number in the arc's computation (in a scratch copy) and run its lock. The lock must fail.

## 4. Errors

| Finding | Accepted when |
|---|---|
| E1 (B997) | The verdict carries a dated note with the m = 4 counterexample and the corrected statement; `GENESIS.md` (F-MC), `docs/THE_CLAIM.md`, `docs/LAW_MAP.md` rows 236/419/427 and `docs/THEOREM_REGISTRY.md` carry the same note; a lock computes ⟨R⁴, L⁴⟩ mod 20. P-318 is split into one row per correction. |
| E2 (C9) | The lock asserts index 12 at level (4), computed in SL/{±1}; header and narrative agree with the ledger's note. |
| E3 (B1856) | The premise is stated as E ≡ +I, or the parity superselection is named as a third condition; the 305/338 split is stated. |
| E4 (B952) | The lemma says "commuting" (toral); a lock computes the rank of the centralizer concerned. |
| E5 (B892) | The scan sentence is removed or the refinement runs unconditionally; the exclusion cites the sign certificate. |
| E6 (B862) | The kernel is computed from the explicit map in exact arithmetic, and cyclicity is asserted. |
| E7 (B1028) | The verdict is not PROVED; the unpriced row and the embedding choice are in the claim line; one endpoint is credited and named. |
| E8 (B854) | The claim line is scoped to the principal embedding; "none was computed" is replaced by the banked table. |
| E9 (B1854) | Relabelled a numerical estimate; the uncertainty has a stated derivation with a k = 2 control; the τ∞ sentence is removed or computed. |
| E13 (B567) | `FINDINGS.md` and the lock say at most 20, with the branch-cut note; the lock counts eigenvalues on the circle, not on a cut interval. |
| E10, E11, E12 | Each named statement corrected where it stands, with a dated note. |

## 5. Labels

| Finding | Accepted when |
|---|---|
| M1 | The verdict file has a machine-readable grade (theorem / exact computation / numerical estimate / sealed cells held / process). The README's headline counts are printed by grade. Graph tools select on the grade. |
| M2, M3 | `docs/UNIQUENESS_THEOREM.md` and `docs/THE_CLAIM.md` list GM3, GM4, SE1, SE2 as inputs; P10 is stated as the trace-3 sieve alone, with m003's shared properties named; the "five filters" constant and test are renamed. |
| M4, M5, M6 | Each sentence carries its frame and its unearned identification by id, or is removed. |
| M7, M8 | Titles and claim lines carry the same caveats as the bodies ("cited, not re-run"; the scope S ⊆ {2,3,4,5}; quotes that prove existence only). |
| M9 | No file or sentence calls an internal review "external" or its author "outside". |
| M10 | The falsifier register states, per row, whether a failure would contradict the programme, a frame, or a reading. |
| M11 | The reviewer page's universal sentences are computed from data. |

## 6. Propagation

| Finding | Accepted when |
|---|---|
| P1 | `README.md`, `docs/THE_PROGRAMME_SO_FAR.md` and `docs/THE_FINAL_ATTACK_2026-10-29.md` state B1823, B1825 and B1838's outcomes. |
| P2–P7 | Each named surface corrected. **And the mechanism:** a gate that, for every arc carrying a correction or retraction note, checks that each arc depending on it and each document citing it carries a pointer to the note. PV: add a correction note to a depended-on arc and nothing else; the gate fails. |

## 7. The weave discipline

| Item | Accepted when |
|---|---|
| W-a: declared domain | Every verdict file has `domain` ∈ {thread, named set, all threads of a kind, weave} and, for a thread or named set, names it. A gate fails on a missing field for any arc numbered after the fix, and the backlog is a named list that only shrinks. |
| W-b: truncation ledger | Every verdict file lists what was removed from the carrier, each entry graded FORCED (with the theorem), COMPUTATIONAL (with the range) or CHOSEN. A CHOSEN truncation is counted on the inputs scoreboard. |
| W-c: the graph gate | No register row, lead or door whose question is about the weave is closed by an arc whose domain is a thread. No weave-domain claim depends on a thread-domain arc without a named lifting theorem. PV23 fails. |
| W-d: second-thread control | Each weave-domain arc commits the same computation on at least one other thread, with the comparison stated. |
| W-e: vocabulary | "The object" is not used for m004 in any file changed after the fix; `TERMINOLOGY.md` and `GENESIS.md` FK13 agree. |
| W-f: the principle | `GENESIS.md` §1 states plenitude with its status and a definition of "allowed", and states the owner's claim of 2026-11-10 — one self-consistent outcome — as a uniqueness statement with its status (not a theorem until proved). The weighting rule (what turns the whole into one number) is a named open fork; any operator, action or measure used to weight is graded FORCED or CHOSEN, and a value counts as derived only with zero CHOSEN and zero FITTED entries on its scoreboard row. The falsifier register carries the programme-level entry: two distinct self-consistent outcomes, exhibited, refute the claim. |

## 8. The value layer

| Finding | Accepted when |
|---|---|
| V1 | The census is extended in Im τ until fewer than 1% of random targets have their best fit on a boundary row, or the band is priced in the null; rarities are re-read under one counted look. |
| V2 | One uncertainty model per quantity, stated before the fit. Any floor is in the headline beside the χ². |
| V3 | Every number cited as evidence has its script and output in tracked files, or is marked "untracked, not reproducible". |
| V4 | B1841 re-graded with the end-condition menu priced as a family (or with the late entry excluded) and with the plan's c arms; the scoreboard row does not say "nothing fitted". |
| V5 | The three missing looks are in `docs/LOOK_LEDGER.md`; one line-label convention, or a tag on every named line. |

**Before any new seal — the value-chain certificate.** For the frame to be read: the transitive `depends_on` closure
is listed; every arc in it has a RECOMPUTE lock that passes the mutation rule, a declared domain, a truncation list
and its identifications priced; no arc in it is on the seal-order-unshown list without a note. The certificate is a
generated file, and the seal is refused without it.

## 9. Governance (the owner ruled on 2026-11-10: `OWNER_RULINGS_2026-11-10.md`, R1)

| Finding | Accepted when |
|---|---|
| X1, X2 | One document is named as governing. The twelve places of finding X1 state the goal as the owner ruled it (a parameter-free theory of everything), each amended passage keeping its original text with a dated note. **The claim ceiling is unchanged:** no amended passage states or implies arrival; `GOVERNANCE.md` §2's permitted self-label is brought down to `GENESIS.md`'s statuses (finding X2), and the banned-phrase gate still fails on a statement of achievement. PV: add "the Standard Model is derived" to `README.md`; the gate fails. |
| X3 | The foundation's input count is computed from `GENESIS.md`'s statuses; the certificate script passes and is run by the suite. |
| X4 | Covered by W-a. |

## 10. Reproducibility

| Finding | Accepted when |
|---|---|
| R1 | A fresh full clone at the fix commit, in the pinned environment, runs the full suite with **0 failed**, and the tree is unchanged afterwards. The two undiagnosed `tests/test_b805_forcing.py` failures are diagnosed. |
| R2 | The environment is a lock file, not prose. |
| G6, G12, G13 | The gates print the same result for a commit on any day and on any complete clone; the pre-push hook is tracked and its installation is tested, or the README says it is optional. |

## 11. What the re-audit will do

1. Fresh full clone of main at the commit cc names.
2. Run the planted-violation suite of section 2.
3. Re-run `tools/arc_stats.py`, `tools/lock_census.py`, `tools/lock_map.py` and compare with the outputs committed here.
4. Run the full suite and the gates; check the tree is unchanged.
5. Apply the mutation rule to a sample of the value chain.
6. Grep every corrected statement across the tree.
7. Report per row: accepted, not accepted (with the failing evidence), or needs the owner's ruling.

The advisor seat's approval covers what this audit read. It is not a statement about the roughly 1,520 arcs outside
the sample, and it is not external review.
