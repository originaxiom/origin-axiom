# B877 — S1 REVIEW PASSED: the First Measurement Theorem ACCEPTED at banking grade — the charge-measurement/triality story is now a two-seat theorem

cc banking seat, 2026-08-03, late night. Review of the solo seat's FIRST MEASUREMENT THEOREM
(`REVIEWED_DOCUMENT.md`, their authorship; prepared by them to banking grade for this review).
Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched — the physics reading stays inside
their §5 fence, and this review keeps it there.

## 1. The verdict

**ACCEPTED.** Every clause is sound, every load-bearing certificate reproduces on this seat's
build, and clauses A–E were independently verified here before the theorem arrived (B866, B872,
B874, B875). The exact instruments the theorem adds on top of this seat's numerics all ran green
here (`rerun_output.txt`).

## 2. Clause map — their certificate × this seat's independent leg

| clause | their certificate | this seat's independent leg |
|---|---|---|
| A (12/30/46 + the three lines) | pencil theorem det₃₆ = c·μ¹², det₁₂ = c·μ⁴ **exact /ℚ** (levi6 — rerun green); restriction-of-scalars ℚ-nullities 36 = 12×3, 12 = 4×3 (fmt_phase2b — rerun green) | B866 (48×48 interpolation), B872 `cubic_modp_check` (mod-p radical), B874 census; roots cross-check: their μ-roots ≡ this seat's 13×-scaled values, digit for digit |
| B (types; intersections; span) | the **squeeze** (mod-p rank as a LOWER bound + reductivity + dim exact + the classification table) — the valid direction; K_i∩K_j = z(Π) **by identity, no computation** | core (30, 28, 2) at this seat's own primes (B875); K-type (46/45/1) B866 addendum; intersections/span numerically (B875) |
| C (the tiling) | rank–nullity + semisimplicity of ad(x_j), j-independence a priori | B875 skeleton + sector dims |
| D (the law) | **the weight-line lemma** — 48 = 16·3 forces the cyclic law **a priori**; dim ≥ 16 by mod-p lower bound; [Vᵢ,Vᵢ] ⊆ core by **sum-freeness** via the one-prime lemma (fmt_combined — rerun green: 16-element multisets sum-free at all 3 roots × both primes) | B875: the law at ~1e-24 in oblique coordinates |
| E (matter = foreign sectors) | (C) + the standard D₅⊕u(1) branching pinned by (B) | B872: 16⊕16̄ on two legs (exact/ℤ fork-node orbits; certified numerics) |

## 3. Logic review (the part scripts cannot do)

- **The weight-line lemma is correct**: nonzero Π-weights total 48; each annihilator line
  carries 16; 16·3 = 48 exhausts them. A sum of nonzero weights from two distinct lines cannot
  vanish (it would lie on both lines) and cannot return to either parent line — so it lands on
  the third line or is no weight at all: [Vᵢ,Vⱼ] ⊆ V_k **a priori**. The only computational
  content in D is the lower bound and the sum-freeness — both certified.
- **The one-prime lemma is applied in the valid direction**: a single good prime where every
  candidate identity a+b−c reduces to nonzero proves each is nonzero over ℚ̄. Two primes used.
- **The type squeezes use mod-p only as lower bounds** (rank_p ≤ rank_ℚ) — the direction that
  cannot lie — closed by exact dimensions and reductivity (I2). No float enters any clause.
- Imports I1–I3, I5 are textbook; each is used exactly where pinned.

## 4. Review notes (recorded, none blocking)

1. **Manifest gap**: §3 cites `levi2.py` (core type, exact ℚ) — absent from the handoff. Not
   blocking: the same squeeze pattern closes the core type exactly (dim 30 exact from the
   ℚ-block structure; derived ≥ 28 from this seat's own mod-p; center ≥ 2 since Π is central;
   reductivity ⟹ (28, 2); I3 ⟹ D₄). Request the script for the record on the next pass.
2. **Normalization**: their ρ is this build's native parameter (B872's mod-p certificate,
   µ = 1/13 vs the banked B866 form); their real roots match this seat's working values
   exactly. No trap survives.
3. This seat's B875 numerics documented the **nearly-parallel-sectors projector trap**; the
   theorem's weight/mod-p methods are immune to it. Both facts now in the record.

## 5. What is now banked, and what is not

- **Banked by this review**: clauses A–E as a two-seat theorem — the object's superselection
  torus stratifies e₆ by charge measurement; the first breaking is the centralizer of any one
  of exactly three Galois-conjugate distinguished charges; the enhanced centralizers tile e₆
  over the triality core with the cyclic law; each breaking's coset is the 16⊕16̄ made of the
  two foreign sectors.
- **NOT banked**: the generation reading. Their §5 fence is kept verbatim: the triple is a
  candidate for O3, S₃-unlabelable, and **the decisive test is THE DESCENT** (B876, running
  at review time). The held Stage-2 shot remains owner-gated.

`tests/test_b877_fmt_review.py`
