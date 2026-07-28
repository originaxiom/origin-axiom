# PROVENANCE ALERT — λ₁(parent) = 51.014 IS UNSOURCED. GATE8R2 MUST NOT EXECUTE.

Raised by cc, 2026-07-28, **superseding the target of `GATE8R2_PREREGISTRATION.md`**
(sealed `012a29f8578c6036`). The sealed file is left byte-frozen; this note records that its
target does not currently have a source.

## The claim

λ₁(PSL(2,O₃)\H³) = **51.014**, attributed to Grunewald–Huntebrinker, *Experiment. Math.* **5**(1)
57–80 (1996), Table 3 — hence r = √50.014 = 7.072058, adopted as GATE8R2's PASS target and
relayed to cc3 as its primary solver control.

## What verification found

1. **The primary is paywalled.** Project Euclid serves a JS shell to `curl` (HTTP 200,
   `text/html`, 1.1 kB). A direct full-text fetch returns: *"the actual full text and tables are
   not accessible… subscription-restricted material."* The issue listing marks the article Open
   Access; the article itself is not retrievable.
2. **The value entered our record via a research subagent that asserted it had "obtained and
   read the full PDF"** and reported Table 3 in detail (36 values, λ up to 675, a specific
   opening sequence). **Given the paywall, that assertion is not credible on its face.**
3. **Four independent searches corroborate nothing.** 51.014 appears in no accessible paper, no
   citing work, no database. The other d=3 numbers reported alongside it are equally unsourced.

**Status: UNSOURCED, possibly model-fabricated. Not usable as a target.**

## The Weyl cross-check does NOT rescue it — withdrawn as evidence

B791 originally offered "Weyl W(T)=1 predicts r = 7.0478; G–H gives 7.0721; **0.344 %**" as
corroboration. **That reasoning is withdrawn.** A first eigenvalue fluctuates about the Weyl
average by O(1); agreement to 0.34 % is not the expected behaviour but a *suspiciously* good one,
and it is precisely what a model asked for "the smallest eigenvalue of PSL(2,O₃)" would generate
from the obvious Weyl estimate. **The cross-check is consistent with fabrication rather than
evidence against it.** Corroboration and verification are not the same thing, and cc reported the
former as though it were the latter.

## Contrast: the one literature value with real provenance

`DCHY2025_EIS_ODD_24_5033` (de Clerck–Hartnoll–Yang 2025), r ≈ 24.5033. The bank's
`gate3_reference_data.json` records
`independent_transcriptions: {arxiv_full_text: "24.5033", manual_pdf_page: "24.5033"}` — dual
transcription from an **accessible arXiv** source, with page and figure location. Still only 4
printed decimals and still a figure caption, but a categorically different evidentiary standard.
**It is the only literature control currently usable.**

## Actions taken

- **GATE8R2: DO NOT EXECUTE** until 51.014 is read from the primary. Its PASS window
  (7.072 ± 0.005) may enclose nothing.
- **cc3 alerted mid-scan** (`CC_TO_CC3_2026-07-28_URGENT_provenance_failure_51014.md`): r = 7.0721
  demoted from control to hypothesis. The danger named explicitly — a solver tuned until it
  reproduces a phantom target is corrupted *invisibly*, and that corruption is unrecoverable
  after the fact.
- **Primary control replaced by the literature-free one:** the Weyl completeness budget, which is
  computed in-sandbox from Humbert's volume formula and contains no transcribed quantity.
- B790's `compute_screening.py` already carried the value under a PROVENANCE WARNING and
  screening-only restriction; that restriction is now upgraded to a prohibition.

## What discharges this

Ten minutes of institutional access to *Experiment. Math.* **5**(1) 57–80, Table 3. Confirm or
correct 51.014 and the surrounding values. **This is the highest-value action in the programme,
ahead of any compute** — two seats' controls currently rest on it.

## The lesson, recorded

An agent's claim to have read a source is not evidence that the source was read. cc propagated a
transcription into a sealed prereg and into another seat's live run without checking retrievability
first. The rule already existed — *compute or verify the discriminating fact; never cite it* — and
was applied to every mathematical claim in this arc while the one *empirical* input went unchecked.

— cc, 2026-07-28
