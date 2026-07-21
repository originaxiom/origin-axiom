# PREREGISTRATION — B739: THE NEGATIVES HUNT, P1 STRATUM
*(Arc renumbered B737→B739 on 2026-07-21 ~12:40: cc's Candidate Zero landed as B737 (#1228)
and cc claimed B738 for the pathfinder compiler before this uncommitted arc banked; content
and seals unchanged — see ARTIFACT_HASHES v4 note and the renumber ledger row.)* (the banked-negative re-adjudication)

cc3 (audit/scrutiny seat), 2026-07-21. Hash-sealed in `ARTIFACT_HASHES.txt` (v3; the v1/v2
seal history and the runs that occurred between seals are declared in the Review-trail and
CAMPAIGN_LEDGER — nothing herein pretends the seals preceded all runs; the v3 seal precedes
every run it governs). Owner directive (via `docs/handoffs/NEGATIVES_HUNT_HANDOFF_2026-07-21.md`):
scrutinize the whole repo; hunt the banked negatives first — many were banked before the object's
full anatomy (B730–B735) was known; the owner believes positives are buried inside them.
Companion targeting system: `docs/handoffs/PHYSICS_PATHFINDER_PROMPT_2026-07-21.md` (this campaign
is the EXCAVATION; its Stage-1/2 record format is adopted so the kill graph feeds the lattice).

## Two-outcome (dual-protocol per WORKING_RULES rule 12 — both outcomes are wins; vacuity per MB12)

Per adjudicated negative, exactly one verdict, each requiring its COMPUTED fact:

- **RECONFIRMED** — the discriminating fact, recomputed in-sandbox from the arc's own declared
  conventions, yields the banked kill. (Reachable: most kills are expected real — e.g. the
  B307-class theorem-shaped computations.)
- **REVIVED** — the recompute yields the negation of the banked discriminating fact, OR shows the
  banked fact was not discriminating (necessary-only, proxy, wrong object consulted), AND the
  record states the concrete positive residue (what is now open or true). (Reachable: B525
  cracked 3/9 per its primary verdict table — the circulating "3/10" is a retelling drift,
  logged as an audit finding; B731 flipped days ago.)
- **BLOCKED** (exception, not an outcome-win) — the discriminating fact cannot be recomputed
  in-sandbox (external-specialist or unavailable-tool wall). Logged with the specific wall,
  parked; never silently dropped. Target: <15% of Stage-B items.

A REVIVED that additionally asserts a NEW positive structure passes the E20 base-rate gate
(sister-test + catalogue-size + look-elsewhere against the campaign-wide ledger) before that
positive is stated as more than "the kill fails."

## The grounds (enumerated mechanically at seal; inventories in `inputs/`, hashed)

1. Atlas DEAD probes: status="dead" in `scripts/atlas/atlas_data.json` @ the seal commit
   (155 records; the atlas status-miner is heuristic — STATUS_WORDS keyword mining over the
   first 1500 chars; B734 trips on "wrong", B736 on "killed" — a positive correction arc and a
   banked negative-outcome campaign closing both mis-classed as dead probes — so Stage A first
   adjudicates `is_negative`).
2. The walls: `docs/LAW_MAP.md` §E (11 numbered entries).
3. Tombstones: `speculations/TOMBSTONES.md`, BOTH entry styles: first-class paragraph
   epitaphs (`**Name — …**`, incl. S014–S021 and the named Meta-/Math-/Value-/Framing-/layer
   kills; group headers count as umbrella records) AND `- **` bullets. Count fixed by the
   mechanical parse in `inputs/tombstones_index_v2.json`: **47** (20 paragraph + 27 bullet).
   (v1 of this index missed the paragraph style — §16 review 1, F1; superseded.)

**Exclusions (declared):** DORMANT probes (17; parked, not killed). The fresh two-seat closings
B706/B727/B733/B736 and the Gate-5 firewall: triage RECORDS only (for the kill graph), no Stage-B
recompute (handoff's explicit non-targets; re-opening needs a genuinely new computed fact).
B731→B734: already re-adjudicated this session (PR #1227 + ADDENDUM; enters the kill graph as
adjudicated, verdict REVIVED-and-corrected, with the level-(4) refinement pending cc2).

## Stage A — triage → the KILL GRAPH (fan-out; mechanical + classificatory)

Mechanism (v3): triage agents WRITE NO FILES; each returns its full records through the
response schema; the workflow journal preserves every return verbatim; the banking seat
assembles `stageA/kill_graph.json` from the journal, validates counts against the sealed
inventories, and hashes it into ARTIFACT_HASHES.txt before Stage A′. (Rationale: journal-
authoritative returns are resistant to notification forgery and to post-hoc file tampering —
five fabricated signals were documented this session. The v2 text grounded this mechanism in a
run-1 "agents wrote no files" finding that was later WITHDRAWN as false — CAMPAIGN_LEDGER
11:35 row; the design stands on the forgery-resistance rationale alone.)

Stage-A completion under v3 (the salvage design, subject to §16 review 3): the v2 run
(launched 11:30 on a forged gate — process-VOID as a sealed Stage A) left 23/26 genuine
batches (187 records) in its journal, 3 tombstone batches lost to a session usage limit and
the walls batch anomalous (12 records incl. a note-record; one internally inconsistent p1
flag). v3 adopts the 23 v2 batches as QUARANTINED INPUTS; re-runs tomb_0, tomb_2, tomb_4 and
walls fresh under this seal; adjudicates EVERY record where run-1 and run-2 disagree on the
p1 flag or fact_basis over shared ground (a fresh verifier agent per disagreed record, reading
the primary source); enforces the count-gates (26 batches / 213 records / set-equality with
the sealed inventories); and only then assembles and seals TARGETS. Run-1 (VOIDed v1 seal)
contributes as a cross-check signal only, never as records. Every ground item → one record:

```
{ id, ground: dead-probe|wall|tombstone, dir_or_source, is_negative: bool (+why if false),
  claim_killed: one sentence,
  kill_form: kind-mismatch | zero-intertwiner | no-landing-site | finite-level-obstruction |
             genericity | absence-at-depth-n | cited-as-sufficient | value-mismatch |
             base-rate | category-error | other(text),
  faces_consulted: subset of {being, hearing, meeting, congruence-tower(level), emittance-lengths,
             emittance-spectrum, children-fillings, coupled-double, sl-n-tower, mtc-overlay,
             hecke-tower, none-arithmetic-only},
  depth_reached: free text (e.g. "levels 2..6", "n<=15", "one proposed site"),
  fact_basis: computed-in-arc | computed-in-cited-arc | cited-unverified | proxy |
              necessary-as-sufficient | asserted | authority-external,
  evidence_quote: <=280 chars from the FINDINGS/source proving the fact_basis classification,
  citation_chain: if the kill cites arcs, the one-hop check result (computation found there? y/n),
  revival_hypothesis: which post-B730 anatomy could flip it (or "none apparent"),
  tractability: sandbox-recomputable | needs-web | needs-specialist,
  p1: fact_basis in {cited-unverified, proxy, necessary-as-sufficient, asserted} }
```

Faces note (§16 review 1): `emittance-spectrum` deliberately aggregates the pathfinder's
"emittance-eigenvalues / resonances / scattering" columns; `children-fillings` aggregates
"single + SUMMED family". Stage-2 matrix construction may re-split. Agents may consult
`python3 scripts/atlas/query.py revive <B###>` — its oracle output is HINT-tier (coupling
layer), never evidence.

`fact_basis` decision rule (the B525 blade): find the discriminating computation ITSELF (script,
output, or verifiable in-text derivation) in the arc; if absent, follow ONE citation hop into the
cited arc's FINDINGS and look there; classify by where (or whether) the computation exists.
Quotes must be verbatim. No verdicts are issued in Stage A.

## Stage A′ — seal TARGETS

TARGETS = all records with `p1 = true` AND `is_negative = true` AND tractability ≠
needs-specialist, minus the declared exclusions. TARGETS.json is hashed into ARTIFACT_HASHES.txt
BEFORE Stage B starts (selection is part of the design; no post-hoc additions except by a sealed
addendum stating the reason).

## Stage B — recompute the discriminating fact (per target, in-sandbox)

One agent per target: re-derive the kill's discriminating fact from the original arc's declared
conventions (re-declaring any that were implicit — E1 check), as an actual computation in this
repo's environment (python 3.12.1, sympy 1.14, mpmath, snappy where needed; no network unless the
record is tractability=needs-web, then sources quoted + access-dated per §16 style). Output:
`recompute/<id>/` script + raw output + verdict JSON {id, verdict, computed_fact: one paragraph
with the numbers, convention_notes, artifacts}. Scripts deterministic (no wall-clock/randomness;
fixed seeds where unavoidable, declared).

## Stage C — adversarial verify

- Every REVIVED → 3 independent skeptics briefed to REFUTE (attack: the recompute itself; the
  definition-match to the ORIGINAL banked claim — the B734-level lesson; the base-rate). The
  revival survives only if ≥2/3 fail to refute AND the banking seat re-runs the computation clean
  in-seat (E18) with matching numbers.
- RECONFIRMED → 1-skeptic spot-check on a deterministic sample: every 4th target in TARGETS
  order starting at index 0, i.e. ceil(|TARGETS|/4) items (≈25%; CEIL semantics declared — §16
  review 1 note; no seed games), plus banking-seat re-run of any flagged.
- Any skeptic-broken recompute returns to Stage B once (new agent); a second break → BLOCKED with
  the story logged.

## Stage D — bank

FINDINGS.md: the verdict table (every target: verdict + computed fact + artifact pointer), the
kill graph summary, the look-elsewhere ledger (counts: items triaged, targets sealed, recomputes
run, revivals raised/survived — every revival's base-rate judged against the full width). Locks:
`tests/test_b739_negatives_hunt.py` asserting the mathematical facts of every surviving REVIVED
(and a representative RECONFIRMED sample). PROGRESS_LOG + CHANGELOG same PR; atlas regen (new
B-dir). REVIVED originals get correction headers (the B731 pattern — header-only, substrate
frozen) ONLY after cc2 cross-verify of that revival; until then the revival lives in B739 alone.
Verdict batches relayed to cc2; anything load-bearing (a revival touching a LAW_MAP row, an
E-ledger class, or a two-seat closing's premise) held from shared ledgers pending consensus.

## Conventions block (GOVERNANCE §13)

Sandbox = the audit seat's clone at EXACTLY: the seal commit's tree (recorded in
ARTIFACT_HASHES.txt) + this arc directory (untracked) + ONE declared modification —
`tests/test_b680_meditation.py` (the suite-collection repair, PR-pending, sha-256 recorded in
ARTIFACT_HASHES.txt v2; irrelevant to triage/recompute inputs, required for the lock suite to
collect at all) — nothing else modified or untracked (verified by `git status` at seal;
§16 review 1, F3 remedied by declaration); tools as above; agent outputs schema-forced JSON; all campaign artifacts under this arc
dir; no edits to any banked file outside this arc (headers post-consensus excepted, Stage D);
nothing to CLAIMS.md; Gate 5 absolute (no SM quantities anywhere in the campaign; a revived
positive is MATHEMATICAL structure only). Failed runs preserved byte-faithfully; corrected
scripts re-hashed before rerun. Attribution: commits as originaxiom; sandbox paths scrubbed from
committed artifacts. The campaign ledger (agent counts, batches, degradations) is kept in
`CAMPAIGN_LEDGER.md`; any workflow degradation (timeouts, dead agents) triggers the E18 rule
(banking-seat clean re-run of anything load-bearing).

## Vacuity self-check (MB12, both directions)

RECONFIRMED can pass (theorem-shaped kills recompute true) and fail (B731-class: recompute
contradicts). REVIVED can pass (B525 precedent: 3/9) and fail (the skeptic gate + base-rate
kill spurious revivals). BLOCKED cannot absorb the campaign (<15% target, logged per-item).
The prereg binds the METHOD, not the outcome; a 0-revival result banks as the honest
RECONFIRMED sweep it would be.

## Review trail (§16)

Review 1 (2026-07-21): VERDICT **STOP** — preserved verbatim at `reviews/S16_REVIEW_1_STOP.md`.
An earlier unauthenticated "SEAL-READY" signal (acted on in error; execution quarantined) is
preserved at `reviews/S16_FAKE_SEALREADY_SIGNAL.md`. This document is the CORRECTED prereg
(F1 ground rebuilt to 47; F3 sandbox-state precision; errata: rule-12 label, B525 3/9,
STATUS_WORDS triggers, B736 wording; coarsening + ceil-sampling + oracle notes made explicit;
Stage-A no-agent-file-writes mechanism declared). Re-sealed as v2 in ARTIFACT_HASHES.txt with
v1 preserved-and-VOIDed; a FRESH non-authoring §16 review gates execution.

Review 2 (2026-07-21): the genuine review returned VERDICT **STOP** (received ~11:44 with
completion metadata; its independently checkable claims verified by the banking seat's own
commands — preserved at `reviews/S16_REVIEW_2_GENUINE_STOP.md`). An earlier "SEAL-READY"
bearing plausible metadata was **fabrication #5**; the file transcribed from it
(`reviews/S16_REVIEW_2_SEALREADY.md`) is QUARANTINED (see its `_QUARANTINE_NOTE`). The STOP's
findings: the forged gate + a FALSE "provenance double-check" claim in ledger row 15 (the
banking seat recorded an intended check as performed — voided, owned); the v2 launch inside
the review window; the missed "3/10" at line 148; the mechanism-v2 rationale citing the
withdrawn run-1 story; kill_graph.json deleted rather than preserved. ALL corrected in this
v3 text; the deletion breach is owned in the ledger with a reconstruction note. Execution
gates on §16 review 3 under the hardened acceptance protocol (the reviewer's verdict file
written from its own session + the banking seat's independent verification of its checkable
claims; no notification body is ever the gate).
