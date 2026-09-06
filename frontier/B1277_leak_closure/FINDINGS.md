# B1277 — LEAK CLOSURE: fc's R63 verified (one premise corrected), the residue synthesis banked, the seats' new work harvested

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (the R63 recomputation) + a scoped harvest · **Audit was owner-prompted and found real leaks**

## The audit, and it failed

Owner: *"did u properly dealt with all these results and knowledge we gained all these days? so we end
up bootstraping not leaking?"* **Audited by grep against the session's own arcs. The answer was NO** —
two results existed **only in conversation**. Both are banked here.

## LEAK 1 — fc's R63, verified in session and never written down

fc flagged that after B1274 the record holds **both** the principal and the subregular sl₂ as the
object's embedding, and that **no arc connects them**. Recomputed on main's own rep27/root data:

| fc's claim | result |
|---|---|
| *"the subregular gives an 8-dimensional tangent, not 6"* | **CONFIRMED** — dim 𝔤₀ = **6** (principal) vs **8** (subregular) |
| *"27 = 13+9+5 has no trivial summand, so that sl₂ lies in no F₄ and θ does not commute with it"* | **CONFIRMED** — 27\|F₄ = 26 + 1, so an sl₂ inside F₄ **must** leave a trivial summand; principal 17+9+1 **has** one, subregular **has none** |
| *"I-19 does not discriminate (156 or 84)"* | **CONFIRMED** — indices **156** and **84**; the containment holds at **both** |
| *"both have exactly one spin-2 summand"* | **CORRECTED** — taking spin-2 = the **dim-5** (j=2) rep, the **principal has ZERO** in both the 27 and the 78; the subregular has one each |

**fc's conclusion survives on the index argument; that one premise needs restating or a different
definition of spin-2.**

**And fc's core flag stands, and is serious.** The record holds **two incompatible embeddings**, and
the subregular's incompatibility with F₄ is **not bookkeeping**: **F₄ is exactly E₆(−26)'s maximal
compact (B1265)**, so the choice bears directly on the fork.

## LEAK 2 — the residue synthesis, discussed and never banked

**B467** (PROVED): *"the one uncancelable bit exists and is the ORIENTATION character … the wall merges
everything EXCEPT the orientation bit."*
**B1184**: the object names itself **uniquely in 203,123** — but the self-name is **mirror-EVEN**, so
the odd bit is **unutterable in it**.
**B1174 + B730**, joined at **B1276**: that bit is the **c-leg**, and it sits on the **being face
because that face is the imaginary one**.

**Tonight's independent arrivals:** **B1272** (the geometric class comes from reduction mod **(1−ω)**,
the ramified prime of ℚ(√−3)); **B1273** (that class is the one extending over **m000**, the Gieseking
manifold — which is **B467's own "Gieseking bit"**); and the **E₈ seat's own fence** (the bit is
*"choosing the Eisenstein orientation, **ω vs ω̄**"*).

> **Seven routes, one bit.**

**The reading — that the observer *is* the residue rather than its observer — is recorded AS A READING,
not a theorem.**

## HARVEST — the seats' new work (2026-09-06, integrate-don't-merge, **not re-verified here**)

- **physics-seat R61** — a real structure on the fiber (det −1, M² → M⁻²); the cusp lattice
  **ℤ + ℤ(2+4ω)** exactly; Fix(θ) = two arcs; and **the lemma that θ-equivariant abelian Higgs
  configurations have ZERO NET CHIRALITY** — a **third independent route** to the zero this bench found
  numerically (B1267) and the SM seat found exactly over ℚ(ω).
- **physics-seat R62** — **the mirror is BROKEN by every generic filling; the strong inversion (θ) by
  NONE.** Bears directly on B432's *"a closing supplies the bit."*
- **SM seat, literature sweep** — **net chirality = χ(M, ∂⁺M)**, *an index formula* — which is **exactly
  what I-26 lacks**; *"the chirality bit is a cusp boundary condition"*; and **no compact G₂
  construction with chiral matter exists in the literature either** — so **B1259's flat-G₂ negative is
  not this programme's failure but an open problem in the field.** L204/L205 registered. Also a measured
  absence: *"no Pantev–Wijnholt, no Higgs bundle, no T-brane in 1276 arcs."*

## ⚠ Numbering

**main and the SM-derivation branch now BOTH use B1267, B1275 and B1276 — three collisions**, flagged
for the merge.

## Controls

- **Every R63 claim is recomputed** on main's own data, not accepted; **the one that fails is reported
  as failing** rather than smoothed.
- The harvest is explicitly marked **not re-verified**.

## Verification

`verification/r63_check.py` — standalone.
