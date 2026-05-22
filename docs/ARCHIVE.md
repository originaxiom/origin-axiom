# Archive — Dead Ideas Register

Governed by `GOVERNANCE.md` §5. This file records every idea the project has **killed** and
*why*. Dead ideas are permanent: per the constitution, a `dead` claim never returns. A new
idea that resembles a dead one is a *new* claim with a new ID — and the burden is on it to
explain why it is not the dead one again.

This register exists so that retired ideas are never silently re-discovered. If you find
yourself excited by something below, re-read the "why it died" column first.

---

## Archive policy

- A claim becomes `dead` only with reproducing code/test showing the falsification or
  circularity. The demotion is logged in `PROGRESS_LOG.md`.
- Dead ideas are not deleted from history — they are evidence of the project's discipline.
- The corresponding `legacy/` artifacts that explored a dead idea stay in place, frozen.

---

## Dead claims

(IDs match `CLAIMS.md`.)

| ID | Idea | Why it died |
|---|---|---|
| D1 | `k ≈ 137` (≈ the fine-structure constant inverse) sets the cosmological constant via `Λ = exp(−V·k)/l_P²`. | The formula used the wrong Chern–Simons normalization. The correct Kashaev scaling `exp(−V·k/2π)` gives `k ≈ 866`, near no notable constant. The `137` match was a single-parameter coincidence — and other knots land equally near other "famous" numbers. Numerology. |
| D2 | `Λ = Λ_Planck · φ⁻²ᴺ` for an integer step count `N`. | Circular: `N` is obtained by taking the observed ratio and expressing it in base `φ`. It is a unit conversion of the answer, not a prediction of it. |
| D3 | Dynamic dark energy: `Λ` evolving as the self-referential iteration converges. | The dynamic version predicts equation-of-state `w ≈ −0.04`; observation pins `w ≈ −1`. Ruled out at roughly 30σ. |
| D4 | `|Z| = 1/φ` is a unique quantum-invariant signature of the figure-eight knot. | The value is a generic feature of level-5 `SU(2)` WRT theory — many trace-3, -7, -13, -17 matrices give it. Not a signature. |
| D5 | Casimir vacuum energy depends on `φ` through cavity geometry. | Leading-order Casimir energy is universal (`−1`) regardless of whether the cavity ratio is `φ`, `√2`, `π`, or rational. `φ` enters only exponentially-suppressed, invisible corrections. |
| D6 | The golden ratio maximizes phonon zero-point energy stability. | The coefficient of variation is flat (<2%) across all mass ratios; the most stable ratio is ≈1.2, not `φ`. |
| D7 | The figure-eight cusp minimizes the Epstein zeta function (an equilateral cusp). | Direct SnapPy data: the figure-eight cusp is **rectangular** (`τ = 3.464i`), not equilateral. The "combined bulk + cusp minimality" claim was based on a misread and is retracted. |
| D8 | The positive record shears `L`, `R` form a braid-group representation. | Direct computation: `LRL ≠ RLR`. A *signed* Dehn-twist pair can satisfy a braid relation, but that is a different (signed) layer — not the positive record-count layer. |
| D9 | The `φ^φ` axiom (an exponent-of-itself fundamental constant). | Tested computationally in the earliest era of the project (`00a_OriginAxiom`); it failed and was dropped. |
| D10 | `θ*` extracted from CKM/PMNS mixing data is a *derivation* of a fundamental angle. | It is a one-parameter fit to observed mixing angles. Without an independent derivation of `θ*`, it is curve-fitting — the same failure mode as D1. |

---

## Patterns behind the deaths

Three recurring failure modes — watch for them in any new work:

1. **Post-hoc constant matching** (D1, D2). A free parameter is tuned to an observation, then
   the tuned value is noticed to resemble a famous number. This is always numerology.
2. **Universality mistaken for specificity** (D4, D5, D6). A quantity is computed at `φ`,
   looks interesting, but turns out to behave the same for every input — `φ` was decorative.
3. **Definition or misread presented as discovery** (D7, D8). A property was asserted
   without checking the actual data, or a definitional identity was dressed as a surprise.

A new claim that cannot show it avoids all three does not reach `proven`.
