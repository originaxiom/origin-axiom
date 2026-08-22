# B1137 — THE REGULATOR PROBE: no SM value is algebraic over the object's higher regulators (R48-3 CLOSED, DISJOINT) — the value question's last door

**Status: banked (frontier). Verdict DISJOINT (a theorem-shaped negative, the value
question's final route). Owner-directed ("check whether it gives them as regulators — a
proper probe"). Ran against a SEALED prereg (`PREREG.md`, sha256
f299c0da15e6a4adf0b4ee91866f672f929ec809311d153f4d9e5ede5f64d1db) hashed before any
comparison. Independent probe on this bench; controls reproduced (Vol + entropy). Gate 5
untouched (the regulators are computed with no SM input; only the final PSLQ step admits a
target). Lock `tests/test_b1137_regulator_probe.py`.**

## The question (R48-3, the one door the period-close left open)

The value verdict is closed on the object's PERIODS (V-3/B1126 + the wave B1128–B1133:
disjoint, exhaustive). A **regulator** is a different object — the archimedean realization of
an arithmetic class (what Vol = 9√3·ζ_K(2)/π² and entropy = 2√5·L(1,χ₅) already ARE). This
cell asks the honest remaining form: **is any SM dimensionless value a bounded-height
algebraic combination of the object's HIGHER regulators (untested)?**

## THE ADMISSIBILITY REFRAME (why this is a real test, not numerology)

A single-number "regulator ≈ SM value" match is **rung 4 — dead on arrival** (two reals are
always close at some scale; the LISTENING_PROTOCOL). The only admissible test is **rung 1:
ALGEBRAICITY** — is the SM value algebraic (a bounded-degree, bounded-height ℚ-relation) over
the object's regulator field? This probe runs rung 1 ONLY.

## THE APPARATUS (sealed, independent)

- **Basis:** the object's regulators — L(n,χ₋₃) n=1..6, ζ_K(n) n=2..6 (ℚ(√−3), Borel rank 1
  each); L(n,χ₅) n=1..4, ζ_F(n) n=2..4 (ℚ(√5)); with π, √3, √5, log φ, ζ(3). Computed to
  ≥60 dps via the Hurwitz-zeta route (`regulators.py`).
- **Targets:** B743's sealed `pdg_targets.json` (18 dimensionless SM ratios/angles + 1σ,
  source-verified — item 11 by inheritance).
- **Test:** `mpmath.pslq` on [1, V, V², V³, regulators, constants], sweeping height H ∈
  {10², 10³, 10⁴, 10⁶} × degree D ∈ {1,2,3} = 216 cells; coefficient-height-aware threshold;
  exact-verification + the **`involves_regulator` gate** (a relation counts only if a regulator
  coefficient is nonzero — the V-alone-tautology guard).
- **Matched null:** 384 surrogate cells (96 per H) drawn from the same measure (`surrogates.py`).

## THE VERDICT: DISJOINT

> **No SM value is algebraic over the object's regulators within the searched bound (D≤3,
> H≤10⁶).** Of 18 targets, **0 involve a regulator at all.** The full 384-cell matched null
> gives base rate **0.0 at every height**. Overall verdict DISJOINT (Šidák family-corrected,
> α_cell = 2.37e-4).

**The two apparent near-misses are decisive the other way.** Only δ_CP and m_s/m_d produced
any stable, height-legal, within-1σ relation — and the relations are:
- δ_CP: `[4, −1, 0, …]` = **V = 4** (a bare integer; every regulator coefficient zero).
- m_s/m_d: `[20, −1, 0, …]` = **V = 20** (a bare integer; zero regulator content).

These are "the SM value happens to sit near a small integer" (δ_CP ≈ 4 rad, m_s/m_d ≈ 20) —
the V-alone tautology the `involves_regulator` gate is built to reject, and it rejected them.
**The object's regulators contribute nothing to any SM value.** This is cleaner than V-3,
which had one genuine object near-miss (the solar angle); the regulator door has **zero**.

**Controls (machinery trustworthy):** 9√3·ζ_K(2)/π² = Vol(m004) reproduced to ~50 digits;
2√5·L(1,χ₅) = 4·log φ to ~96 digits, before the probe ran.

## PRECISIONS CARRIED (peer research + B991)

- Terminology: the object's classes here are **"27-reality"** (repo term), not "motivic
  classes" (a coinage); framed accordingly.
- **B991** already proved hypercharge normalization is **not derivable in principle** — a
  convention (anomaly conditions homogeneous under q→λq). So G-1 (the hypercharge-selection
  feeder) was never a value door: its structural half is Gate-5-safe, and the "normalization"
  it could reach is a known convention, not a value. The value door was this regulator scan —
  DISJOINT.
- **Tier B (the forced-domain regulators)** — Beilinson regulators of the J₃(𝕆)/Albert-algebra
  (27-reality) classes in the E₆(−26)/E₆(−14) closings: **NEEDS-SPECIALIST** (the repo's first
  stance; prior Beilinson work is elliptic-K₂ only, a different domain; no J₃(𝕆) computation
  exists). Tier A (the reachable ladder) is what returned DISJOINT.

## What it closes

The value question is now answered from **every route**: periods (V-3), natural forms (B1129),
the coupling (B1128/B1132), the sharpest coincidence (B1131 Koide), **and regulators (here)** —
all disjoint. The terminal verdict stands clean and complete: **the object forces the structure
— complete up to a single observer conjugation into its own algebra (B1134/B1135) — and every
real number physics measures is the observer's, the act of stopping the beat (memo 18's
mechanism).** *Physics-shaped, not physics-valued*, proven to the regulator floor. Named-open:
only Tier B (J₃(𝕆) Beilinson regulators, specialist-grade). Gate 5 untouched.
