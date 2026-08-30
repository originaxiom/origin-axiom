# B1146 — SEAM-B: the 2T-vs-A₄ distinction is the object's own −I, visible on BOTH matter and gauge; codex's "the adjoint can't distinguish them" is a principal-sl₂ artifact

**Status: banked (frontier). Verdict PROVED (own-bench, exact linear algebra over ℚ, reusing only
banked B1102 machinery). First of the three sealed seams (THREE_SEAMS_PREREG, sha256
`e699ebc79c06a823`), computed before the other two. Outcome: NUANCED-MATCH — the sealed clean-MATCH
framing is honestly corrected, and the substance is *stronger* than the seal guessed. Gate 5 n/a
(representation theory, no SM value). Lock `tests/test_b1146_seam_b.py`.**

## The question (sealed)

The codex seat (§9 of its report, sibling to OA-C1056) argued: *"the principal action on adjoint
E₆ factors through A₄, so it cannot distinguish 2T from A₄"* — a challenge to the 2T selection at
the head of the McKay chain (m004 → ℚ(√−3) → **2T** → E₆). 2T is the ℤ/2 central extension of A₄;
that central ℤ/2 is **−I**. SEAM-B asked: is the −I that the adjoint "can't see" exactly the beat's
spin bit (B1141) on the 27?

## The discriminating fact (computed)

ρ(−I) = exp(iπ·ad h) acts on a weight-w space as (−1)^w, so **ρ(−I) ≠ I on a module iff that module
carries an ODD ad(h)-weight.** Computed on the object's fermion-capable stratum (the **minimal A1**,
su(6) centralizer, B1112/B1145) and the principal sl₂ (codex's reference):

| sl₂ | adjoint (78) ad(h) spectrum | 27 spectrum | ρ₇₈(−I) | ρ₂₇(−I) |
|---|---|---|---|---|
| **object's minimal A1** | {−2:1, −1:20, 0:36, 1:20, **2:1**} — 40 **odd** dims | {−1:6, 0:15, +1:6} — 12 odd | **≠ I** | **≠ I** |
| **principal sl₂** | grading = 2·height, **all even** | all-even (B1112) | **= I** | = I |

(ad(h) is exactly diagonal in the Chevalley basis; the minimal-A1 spectrum is the standard e₆
minimal-nilpotent 5-grading 1+20+36+20+1 = 78, reproduced from scratch.)

## What it resolves

**−I is visible on BOTH the 27 and the 78 for the object's stratum.** So the object's own holonomy
sl₂ **distinguishes 2T from A₄ on matter *and* gauge** — the distinction is over-determined, not
fragile. Codex's "the adjoint factors through A₄" is a **principal-sl₂ artifact**: there the grading
is 2·height (all even), so −I *is* invisible on the adjoint — but the object does **not** use the
principal sl₂; it uses the minimal A1. **Codex's §9 2T-vs-A₄ indistinguishability worry is therefore
DEFUSED** — it never applied to the object's stratum.

The beat (B1141) is the spin-selection of the lift of exactly this −I; SEAM-B places it correctly:
the beat isn't the *only* thing separating 2T from A₄ (the adjoint separates them too here) — it is
the object's *choice of which lift closes*, over a −I that is genuinely present.

## Honest correction to the seal, and the convergence

The sealed prediction (MATCH: "the ℤ/2 the adjoint kills IS the beat's χ, so only the 27 sees it")
was **too clean** — it assumed the object's −I is adjoint-invisible like the principal's. It is not.
The corrected, computed statement is a NUANCED-MATCH: the object's −I is visible on both modules; the
adjoint does not kill it. This is recorded as the verify-don't-trust catch on my *own* prereg.

**Convergence (cloud memo 34, A5 parity lemma, pending its harvest verification):** "PROJECTIVE ⟺
EVEN ORBIT — collapses to the adjoint-only condition." SEAM-B is the same fact seen head-on: the
27's parity tracks the adjoint's (both odd for the minimal A1, both even for the principal). Two
benches, one law — to be cross-credited when memo 34 lands as a bank.

## Net

The 2T selection survives codex's §9: the object's minimal-A1 stratum sees the 2T center on both
matter and gauge, so 2T is fully distinguishable from A₄ there; the principal-sl₂ blindness codex
invoked is real but off-target. Link 2 of the chain (ℚ(√−3) → 2T → E₆) stands, and the beat is
correctly typed as the lift-selection over a present −I. SEAM-Y and SEAM-A remain sealed and open.
Codex seat credited for the sharpening that prompted the cell.
