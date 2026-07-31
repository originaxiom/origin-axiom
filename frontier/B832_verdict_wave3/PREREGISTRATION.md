# B832 — PREREGISTRATION: wave 3, with the calibration flaw fixed

cc banking seat, 2026-07-30. **Sealed before the fan-out launches.** Repository-instrument scope;
verdicts label what an arc *established*. Gate 5 absolute; nothing reaches `CLAIMS.md`.

## The frame, measured against the repository rather than a work list

B819's lesson — *a coverage number is only as good as its frame* — applied to this wave's own design:

| | |
|---|---|
| distinct arc ids in `frontier/` | **800** |
| already carrying an authored verdict | **617** |
| **unjudged (this wave's frame)** | **183** |
| of those, carrying a findings document (writable) | **138** |
| carrying none (a reader must return "no findings", never invent) | **45** |

## The fix this wave exists for

Wave 2's calibration block **exercised two of four verdict categories while licensing work that used
four** (B817 §3), and **2 of the 11 untested-category writes were wrong** (B818). `PRACTICES` now
requires the block be checked **before** the run.

**Checked, and it passes:** the 16-arc block draws **4 arcs from each of `PROVED`, `NEGATIVE`,
`OPEN`, `RETRACTED`**, selected by committed seed `20260730` from substantial arcs (≥ 2500 B)
already carrying that verdict. **Categories spanned before the run: all four.**

**Disclosure, because it changes what κ means.** The calibration arcs **already carry authored
verdicts**. Readers judge them **blind** — the existing verdicts are never shown — and are used by
this seat for exactly two purposes:

1. **to guarantee the block spans the vocabulary** (the point of the fix), and
2. **a secondary measure wave 2 could not compute: consistency against the established corpus.**

> **κ measures whether readers agree with each other. Consistency measures whether they agree with
> the corpus.** A panel can be perfectly self-consistent and uniformly drifted from the vocabulary;
> wave 2 had no way to see that. **Consistency is NOT accuracy against ground truth** — the banked
> verdicts are themselves reader-authored — and it must never be reported as such.

## Gates

- **Fleiss' κ ≥ 0.75** on the 16-arc block → write; below → **hold** (unchanged, sealed bar).
- **B815's reporting rule stands**: a pass whose bootstrap CI lower bound falls below the gate is
  reported **PASS (marginal)**, interval printed.
- **Consistency is reported, not gated.** It is a new measure with no sealed threshold, and
  inventing one now — after wave 2 — would be setting a bar to a number I can already estimate.
- **Writer safety, unchanged:** never overwrite an authored verdict; never write for an arc with no
  findings document (`FINDINGS.md` **or** `VERDICT.md`, per B826); readers return
  `OPEN` + "no findings" rather than invent. Held at a live 3.0 % fault rate in wave 2 with **zero**
  fabrications.
- **Audit** by B816's committed seed over the frame of what actually lands, drawn **after** the
  writes.

## Two-outcome

- **κ ≥ 0.75** → the ~138 writable verdicts are written; coverage rises from 617/800.
- **κ < 0.75** → **verdicts are HELD, not written, and not discarded.** A disagreeing panel writing
  138 verdicts would bake its disagreement into the ledger as knowledge.

## Pre-stated expectations

- **κ ≈ 0.75–0.90 — LOWER than wave 2's 0.9312.** Wave 2's block was accidentally two-category, and
  a 4-category judgement is strictly harder. **If κ comes out ≥ 0.93 I will have been wrong about
  why wave 2 scored so well**, and that must be reported rather than smoothed.
- **Consistency ≈ 0.75–0.90.** Below ~0.6 would indicate the panel is reading the vocabulary
  differently from the corpus and the write should be reconsidered even if κ passes.
- Coverage after: **≈ 755/800 (94 %)**, the residue being the 45 arcs with no findings document.

## What this wave does NOT do

No physics, no values, no new lexicon, no face attachment, no edges. Coverage is a precondition, not
the goal.
