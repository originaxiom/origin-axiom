# B1069 — affine isotropy selects a ray: the object fixes a (3,1) conformal structure

**Date:** 2026-08-17. **Status:** positive, controlled, firewalled. Criteria sealed in
`PREREG_conformal_selection.md` before the compute. Reproducer `conformal_selection.py`,
all controls pass. **Nothing promotes to `CLAIMS.md`.** No physical identification (Gate 5).

## What was open

B527 established the Stein-compatible metrics on `E_s = ker ℓᵀ` form a **6-dimensional** cone
`𝓒 = 𝓛⁻¹(PSD(3))`, non-polyhedral, with a continuous `ℝP²` of extreme rays — so *Stein
compatibility alone cannot select a metric* — and that `S_aff` sits in its **interior**,
distinguished only by the **separate** affine-isotropy requirement. B527 never asked how large
the isotropy locus is.

## The result

**`dim 𝓘 = 1`.** The isotropy conditions have computed rank **5** of 5 on the 6-dimensional
`Sym(E_s)`; the locus is a single ray, and it **is** the `S_aff` ray. On that ray:

- positive definite — eigenvalues `[0.5456, 0.5740, 0.6106]` (normalised)
- Stein driver `[0.0989, 0.3138, 0.4439]` — strictly inside `𝓒`
- Lorentzian completion `G = S − αℓℓᵀ` has signature **(3,1)** and stays Stein-positive for
  every `α` tested (0.5, 1.0, 2.0) — checked **on the selected ray**, not merely at `S_aff`

**Stein + affine isotropy determine the metric up to one positive number `t`, and nothing else.**

## The overclaim I retracted inside the script, before it was written down

The first falsifiability control **failed**: perturbing the letter configuration gives
`dim 𝓘 = 1` every time (200/200). So "the isotropy locus is a ray" is **generic to any four
points in 3-space** and is *not* a fact about this object. This is exactly the B416 failure mode
(golden-Anosov is generic to the whole metallic family). The dimension count is **retracted as
evidence** and kept in the script as a recorded negative.

## What is actually non-generic — the discriminating control

The letters fix the isotropy ray; `M_*` **independently** fixes the Stein cone. Whether the ray
the *letters* pick lands in the cone the *dynamics* picks is a real question with a real
denominator. Over random contracting `4×4` nonnegative-integer operators (entries in `{0,1,2}`,
238 admissible):

| property of the isotropy ray | frequency |
|---|---|
| positive definite | **238/238 = 100%** — generic, carries nothing |
| PD **and** Stein-compatible | **6/238 = 2.5%** |

`M_*` is in the 2.5%. **Stated at its true strength:** this is one object against a 2.5% base
rate — suggestive, `p ≈ 0.025`, and *not* significant on its own. The comparison class is crude
(small-integer matrices), and a different class could move the number. It is recorded as a
measured non-genericity, not as evidence for anything.

## How this composes with B167 — two results, one statement

B167 proves (backbone `[exact]`, lemma a stated argument) that a conserved, dimensionless first
integral cannot source a dimensionful scale from within: doors 1–3 shut, door 4 external, door 5
yields a ratio.

B1069 shows the metric is determined **up to exactly one positive scale `t`**.

These are the same fact from two sides. The object determines everything about the metric except
`t`; `t` is precisely what B167 proves it cannot determine. So the honest positive statement is:

> **The object determines a conformal structure of signature (3,1) on the stable space of `M_*`
> — a metric modulo overall scale — and the undetermined residue is exactly one positive number.**

That is *not* "we have no dynamics and no scale." It is a determined Lorentzian-signature
conformal geometry with a one-parameter residue whose necessity is proved.

## Scope — what this is NOT

- A statement about `M_*` on `E_s`: a four-letter transfer operator and its stable space.
  **Not** a claim about spacetime. "Lorentzian" means **signature (3,1)** and nothing more.
- Not connected to the `e₆`/`so(10)` arc (B1068). Whether the conformal structure here and the
  gauge algebra there live on the same object is **unsearched** — named as open, not as absent.
- The 2.5% control does not establish that the coincidence is meaningful; it establishes that
  the question has a denominator and that the object is on the rare side of it.

## Provenance

Rebuilds B527's `M`, `r`, `ℓ`, `E_s`, `S_aff` independently and reproduces its published driver
eigenvalues `[0.0861, 0.2733, 0.3867]` as control C1 before reading anything.
