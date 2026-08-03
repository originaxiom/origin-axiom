# B874 — the measurement ladder: the coordinate census is a two-value cliff, and the full-measurement remnant is an su(3)-TYPE algebra — NOT the SM

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — exact ℚ-linear algebra on the banked B854 build, closing two questions
B866 carried forward.

## 1. The census — all 15 coordinate subtori of C, exact

| subtorus | Cent dim |
|---|---|
| ⟨x₈⟩, ⟨x₁₆⟩, ⟨x₈,x₁₆⟩ | **30** |
| every subtorus touching x₁₄ or x₂₂ (the other 12) | **12** |

A **two-value cliff**: the (8,16)-plane is the unique *soft* direction (every measurement inside
it resolves to 30 — the plane never resolves further than its own stratum), while **x₁₄ or x₂₂
alone already resolve to the full-measurement floor 12**. The three distinguished lines (46,
B866) live inside the soft plane. The observed centralizer ladder on coordinate data is
**78 → 46 → 30 → 12**, with no intermediate stratum.

**Consequence for step 2**: SU(5)×U(1)-sized centralizers (26) do NOT occur as coordinate-subtorus
centralizers. Whether a line-point + second-charge *joint* measurement produces one (which would
retire the step-2 ranking) remains open — it needs the cubic-field points, not this census.

## 2. Cent(C) — the full-measurement remnant, exactly over ℚ

**dim 12 = derived 8 ⊕ center 4**, brackets verified closed. The center **is C** (one line: C is
abelian and Cent(C) commutes with C by definition, so C ⊆ center; 4 = 4). The derived algebra's
intrinsic Killing form is **nondegenerate (rank 8)** ⟹ semisimple of dim 8 ⟹ **type A₂** —
the unique 8-dimensional semisimple Lie algebra. Signature **(4,4)** pins the real form:
**su(2,1)** (su(3): (0,8); sl(3,ℝ): (5,3); su(2,1): (4,4)).

> **Cent(C) = su(2,1) ⊕ C.** What survives every one of the object's 2T-charges is an
> su(3)-TYPE algebra plus the four measured charges themselves.

## 3. Verdicts

- **The "full measurement = SM" reading is DEAD**: the SM algebra needs derived 11 and center 1;
  the computed remnant has derived 8 and center 4. Stated plainly so it cannot drift into a
  claim.
- **What stands**: the remnant is A₂ — a color-sized algebra surviving total 2T-measurement, in
  the quasi-split real form su(2,1). This is a computed structure, recorded as such; **no
  dictionary to color is asserted** (the compact/quasi-split gap is exactly the layer-8 wall,
  B715/B868).
- The cliff shape — one soft plane carrying all the enhancement structure, every other direction
  maximally resolving — is the object's own; the (8,16)-plane's privileged role now has an
  exact, exhaustive census behind it rather than examples.

## 4. Carried forward

1. The joint measurement at the cubic-field points (line-point + x₁₄/x₂₂): does 26 appear, and
   is it su(5)⊕u(1)² — the step-2 retirement question.
2. The su(2,1) remnant's relation to the layer-8 real-form question — flagged only.

`tests/test_b874_ladder.py`
