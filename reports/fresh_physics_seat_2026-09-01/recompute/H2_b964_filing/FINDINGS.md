# H2 — B964 filing re-read (Ring R3, HELD item #23b)

**Date:** 2026-09-01 · **Seat:** fresh physics seat, reader cell · **Scope:** filing only. No mathematics re-examined; B964's content (adjoint VEV ⟹ unbroken group = stabilizer = centralizer ⟹ the measurement cascade is an adjoint Higgs mechanism) is taken as banked.

## Verdict: FILING-DEFECT

Label wrong under the house's own rule (PRACTICES B818 + Boundary rule 1); three of the four source arcs carry no pointer to the correction; one LAW_MAP row still carries the pre-B964 phrasing.

## What B964 corrects, and where those claims lived

Read in full: `frontier/B964_vev_correction/FINDINGS.md` (95 lines).

| # | withdrawn claim | where it was banked (B964 lines 11, 32, 76) |
|---|---|---|
| 1 | "the 27-VEV route provably stops one step short of the SM" (as a general statement) | B962 only |
| 2 | "the object does not supply a VEV" | B952, B959, B960; echoed in B962 |

Corrected statement (B964 lines 44-58): the object **supplies** the rank-preserving (adjoint) VEVs — that *is* the measurement cascade — and **lacks** only the rank-reducing 27 VEVs. B952's rank obstruction is unchanged and renamed.

## (1) Do the corrected arcs carry a dated addendum pointing at B964?

| arc | B964 pointer? | what the file still says |
|---|---|---|
| B962 `frontier/B962_vev_scout/FINDINGS.md` | **YES** — line 5 `## ⚠ PARTIALLY RETRACTED BY B964 (2026-08-08)`, title note line 3, inline strike-throughs lines 40 and 60 (added by B967) | correctly handled |
| B952 `frontier/B952_gut_ledger_rank/FINDINGS.md` | **NO** — zero occurrences of "B964" | lines 47-49: `Rank reduction requires a genuine breaking mechanism: a **Higgs VEV**, a **Wilson line / Hosotani flux**, or an **orbifold projection** — requirement #11 of the ledger, which the object does not supply.` |
| B959 `frontier/B959_nontoral_rank4/FINDINGS.md` | **NO** — zero occurrences; the arc's only addendum (`ADDENDUM_2026-08-20_RESCOPE_TO_TORAL.md`) concerns B1100's toral rescope, not B964 | line 88: `A Higgs-type mechanism remains unexcluded and remains unsupplied.` |
| B960 `frontier/B960_l136_adjoint/FINDINGS.md` | **NO** — zero occurrences | line 55: `A Higgs-type mechanism remains unexcluded — and remains unsupplied.` |

Why B967's retraction sweep missed B952/B959/B960: `docs/RETRACTED_PHRASES.md` row 1 registers the exact phrase `the object does not supply a VEV`. B952 says "which the object does not supply" (VEV two lines earlier); B959/B960 say "remains unsupplied". All three are **paraphrases** — B967's own declared blind spot ("a PARAPHRASE of a retracted claim passes silently"). B964 line 76 withdraws the claim "**everywhere it appears** (B952, B959, B960, B962)"; only B962 was ever marked.

Fair mitigation: in B952/B959/B960 the sentence is about *rank-reducing* mechanisms, so read carefully it is not false post-B964. But it uses "Higgs VEV"/"Higgs-type mechanism" bare — the exact habit B964 diagnosed (lines 80-83) — and a reader of those arcs gets no signal a correction exists.

## (2) Do the live surfaces reflect the corrected statement?

**`docs/LAW_MAP.md`** — mostly yes, one residual:
- line 230: `THE MEASUREMENT CASCADE *IS* AN ADJOINT HIGGS MECHANISM (B964)` — live, correct.
- lines 231-233: B962 rows carry `scoped by B964` / `SCOPED BY B964` / `B964's rule applied` — correct.
- line 269 (B952 row): `Reaching the SM needs rank REDUCTION — a Higgs VEV, a Wilson line/Hosotani flux, or an orbifold projection — which the object does not supply (L133).` — **pre-B964 wording**, bare "Higgs VEV", no B964 note. Same paraphrase-escape.

**`docs/THEOREM_REGISTRY.md`** — no pre/post defect:
- line 261 `T-RANK-OBSTRUCTION` (B952): no VEV clause; neutral.
- No registry row for B964's reframing itself; optional, see worklist.

**`docs/CLAIMS.md`** — **does not exist** in this tree (only `docs/THE_CLAIM.md`, which has no "B964", "supply a VEV" or "adjoint Higgs"). Nothing to correct.

**`docs/RETRACTIONS.md`** line 34 and **`docs/RETRACTED_PHRASES.md`** rows 1-2: carry the corrected statement, cite B964. Correct.

## (3) Is B964's verdict label a filing defect? Yes.

Two labels exist; they disagree with each other and with the convention:
- `frontier/B964_vev_correction/FINDINGS.md` line 91: `**Verdict: CORRECTION.**` — not a vocabulary value (`docs/PRACTICES.md` lines 97-100: PROVED / NEGATIVE / OPEN / RETRACTED).
- `frontier/B964_vev_correction/arc_verdict.json`: `"verdict": "RETRACTED"`, `"supersedes": null`. Propagates to generated `docs/views/VERDICT_LEDGER.md`, where B964 sits under `## RETRACTED (10)` at line 1167.

House rule, `docs/PRACTICES.md`:
> line 115 (B818): "`RETRACTED` applies only when the arc withdraws **its own** headline. An arc that *establishes* that **another** arc's claim fails is doing positive work: label it by what **it** established (`PROVED` / `NEGATIVE`), and the retraction lands on the **target** arc's record. ... Mislabelling an auditor as RETRACTED makes the ledger say the audit is untrustworthy, which is the opposite of the truth."
> line 120 (Boundary rule 1): "a correction that also proves is PROVED. `RETRACTED` applies only when the withdrawal is the arc's **whole** content. If a new positive result supersedes an old one, the verdict is `PROVED` and the withdrawal is recorded in `supersedes`."

B964 withdraws claims of B952/B959/B960/B962 (not its own headline) and establishes a positive identification. Both rules give **`PROVED`**, `supersedes` populated, with the RETRACTED mark on the target arcs (which, per (1), only B962 carries). This is exactly the B818 failure: the ledger says "do not trust B964", and B964 holds the live truth.

### Proposed exact re-label (`arc_verdict.json`, live surface → dated in-place note)

```json
"verdict": "PROVED",
"supersedes": ["B962: '27-VEV route stops one step short' (as a general claim)", "B952/B959/B960/B962: 'the object does not supply a VEV'"],
"relabel_note": "2026-09-01: RETRACTED -> PROVED per PRACTICES B818 disambiguation and Boundary rule 1 (B964 withdraws OTHER arcs' claims and proves a positive reframing; withdrawal is neither its own headline nor its whole content). H2 filing re-read."
```
(`supersedes` is currently `null`; if the generator expects arc ids only, use `["B962"]` and keep claim-level detail in the note — check `scripts/views/generate.py` first.)

## Propagation worklist

| surface | line | current text | corrected text (house convention) |
|---|---|---|---|
| `frontier/B964_vev_correction/arc_verdict.json` | `"verdict"` | `"RETRACTED"`, `"supersedes": null` | `"PROVED"` + `supersedes` populated + dated in-place note (above) |
| `frontier/B964_vev_correction/FINDINGS.md` | 91 | `**Verdict: CORRECTION.**` | keep line; dated addendum beside: *"Addendum 2026-09-01 — ledger label: PROVED (B818 / Boundary rule 1). 'CORRECTION' is descriptive, not a vocabulary value; the four-value label lives in arc_verdict.json."* |
| `docs/views/VERDICT_LEDGER.md` | 1167 (under `## RETRACTED (10)`) | B964 listed as RETRACTED | regenerate via `scripts/views/generate.py` after the json edit — never hand-edit (file header) |
| `frontier/B952_gut_ledger_rank/FINDINGS.md` | 47-49 | `a **Higgs VEV**, a **Wilson line / Hosotani flux**, or an **orbifold projection** — requirement #11 of the ledger, which the object does not supply.` | dated addendum beside (`ADDENDUM_2026-09-01_B964.md`): *"Corrected by B964 (2026-08-08): the object DOES supply the adjoint (rank-preserving) VEVs — the cascade is an adjoint Higgs mechanism. What it lacks is the rank-reducing 27 VEV. Read 'Higgs VEV' here as '27 VEV'."* |
| `frontier/B959_nontoral_rank4/FINDINGS.md` | 88 | `A Higgs-type mechanism remains unexcluded and remains unsupplied.` | dated addendum beside (same text; note the existing 2026-08-20 addendum is unrelated) |
| `frontier/B960_l136_adjoint/FINDINGS.md` | 55 | `A Higgs-type mechanism remains unexcluded — and remains unsupplied.` | dated addendum beside (same text) |
| `docs/LAW_MAP.md` | 269 (B952 row) | `a Higgs VEV, a Wilson line/Hosotani flux, or an orbifold projection — which the object does not supply (L133)` | dated in-place note in the style of rows 231-233: `... a **rank-reducing (27)** Higgs VEV, a Wilson line/Hosotani flux, or an orbifold projection — which the object does not supply (L133). **[NB 2026-09-01, per B964: the object DOES supply the adjoint VEVs — the cascade is an adjoint Higgs mechanism; only the rank-reducing 27 half is missing.]**` |
| `docs/RETRACTED_PHRASES.md` | row 1 | phrase `the object does not supply a VEV` | optional: paraphrase rows `remains unsupplied` / `which the object does not supply` in VEV context — would need mention-cue exemptions (B967); judgement call |
| `docs/THEOREM_REGISTRY.md` | — | no B964 row | optional: `T-ADJOINT-HIGGS` row (unbroken group of an adjoint VEV = centralizer; cascade = adjoint Higgs; B964, cited standard) — registry-scope judgement, not a correctness defect |
| `docs/CLAIMS.md` | — | file does not exist | nothing to do |

## What is NOT wrong
- B964's content and LAW_MAP row 230 are live and correct.
- B962 was marked properly by B967 (banner, title note, inline strikes).
- `docs/RETRACTIONS.md` and `docs/RETRACTED_PHRASES.md` carry the corrected statement.
- THEOREM_REGISTRY's B952 row does not contain the withdrawn clause.

Nothing else was modified by this cell.
