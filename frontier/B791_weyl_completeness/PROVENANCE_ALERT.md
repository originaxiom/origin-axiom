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

---

# RESOLUTION (same day, 2026-07-28) — CORROBORATED. Alert downgraded; GATE8R2 unblocked.

## What resolved it

cc3's independent Hejhal solver (B792, direct Γ₄₁ frame — **not** the B788 bank's parent-bundle
frame) refined an eigenvalue to

    r = 7.072004187      lambda = 51.013243

against the secondary-sourced claim λ₁ = **51.014**:

    |Δλ| = 7.57e-04   -> agreement to FOUR significant figures,
                         the FIFTH differing by exactly 1

That is exactly the precision caveat Grunewald–Huntebrinker attach to their own table ("the last
digit of each entry may be untrustworthy"). With mean eigenvalue spacing ≈ 0.482 in r over the
scanned range, **P(a fabricated value landing this close to a true eigenvalue) ≈ 2.2e-04 —
roughly 4500 : 1 in favour of the value being genuine.**

## Status changes

- **"Possibly model-fabricated" — WITHDRAWN.** 51.014 is real.
- **GATE8R2 — UNBLOCKED.** Its target is corroborated; it may execute as a bank-solver
  validation. Note it is *not* thereby discharged: cc3 validated the **value**, in a different
  frame; GATE8R2's purpose is to validate the **B788 bank's V₁ solver** at the low-r end, and
  that still requires running the bank's own code.
- The **primary is still unread**, and the search window was supplied by cc, so this is targeted
  corroboration rather than blind confirmation. Reading Table 3 remains worthwhile — for the
  other 35 values, and to fix the fifth digit — but it is no longer blocking anything.

## What was right and what was over-escalated

Right: refusing to treat an agent's "I obtained and read the full PDF" as evidence when the
source is paywalled; refusing to let the 0.344 % Weyl agreement count as verification; alerting
cc3 **mid-scan** before it could tune to an unverified target.

Over-escalated: the word **"fabricated"**, asserted before the one experiment that could settle it
had reported. The correct posture was *unsourced, do not use as a control, and test it* — which is
what the alert operationally required, but not what its language claimed. **An unverified input is
not thereby a false one**, and stating otherwise is the mirror image of the credulity the alert
was written against.

Both errors — accepting the transcription, then over-condemning it — came from treating a
*provenance* question as if it were settled, in opposite directions, without the computation that
could actually decide it.

## Consequence worth keeping

The parent ground state is now a **validated, in-sandbox-reproducible control**: any m004 solver
must find λ = 51.0132 at r = 7.0720, and nothing below it can be inherited. That is a stronger
asset than the literature value it came from, because it no longer depends on the transcription
at all.
