# B933 () — the spinor-Hejhal design lands, and the probe already sees the Dirac spectrum of m004

**Status: DRAFT — exploratory numerics (double precision), NOT sealed, NOT
banked. Verdicts wait on the sealed run designed in `DESIGN.md` §10.**

**Date:** 2026-08-06 · **Seat:** computation agent (cc bench) ·
**Authorization:** the B921-harvested Cell-3 spin fork (ρ₁ non-Lie under
both conventions ⟹ discrete Dirac spectrum, unconditional).

## What this arc delivers

1. **The complete design** (`DESIGN.md`) for the Dirac/spinor-Hejhal
   computation on m004 with spin structure ρ₁ = (A,B): the operator in the
   horospherical trivialization (D = −i[t σ·∂ − σ₃], derived three
   independent ways), the shifted-lattice cusp modes
   e^{2πi⟨μ,z⟩} t^{3/2}(K_{iλ−1/2}, −ie^{iθ_μ}K_{iλ+1/2}) with
   μ ∈ Λ* + u₂/2, the SU(2)-twisted vector collocation identity, the
   element-by-element adaptation of B922's certified scalar protocol, the
   validation-gate battery, the honest anchor statement, the cost table,
   and the two-outcome sealed criterion.

2. **A successful feasibility probe** (~20 min of compute, `probe.py` +
   `results.json`): the operator assembled, all gates passed, and a rough
   first spectrum obtained.

## The probe's numbers (double precision, two-Y/two-seed/two-wordset stable)

- **First eigenvalue bracket: |λ₁| = 2.97455058 ± 1e−6** (three independent
  instruments agree to 8 digits; multiplicity 2 with a 9-order σ-gap).
- Distinct positive values found in |λ| ≤ 7: 2.97455058, 4.32782242,
  4.72904955, 5.67720879, 6.00516263, 6.63387901, 6.92096493 — and their
  exact negatives (pairing to 3e−13).
- **A kernel candidate at λ = 0 of dimension exactly 2** (σ₁ = σ₂ ≈ 1e−12,
  σ₃ ≈ 0.53; |λ| < 1e−8). Exactness is deliberately left open (obligation
  O2).
- Weyl screen: 30 states (with the observed doubling) vs ~22.7 leading-term
  expected at Λ = 6.92 — right ballpark; screen only.

## What the probe taught the design (the paid lessons)

- **The conjugate-twist lesson (gate G2b).** The spinor automorphy twist in
  the coordinate trivialization is the elementwise CONJUGATE of the Iwasawa
  SU(2) factor (R_geom = C·Ad(k)·C, C = diag(1,−1,1)). With the unconjugated
  twist, every standard gate still passes (operator identity, SU(2),
  cocycle, peripheral ±I, assembly) yet the collocation system is
  inconsistent: a completely flat σ ≈ 0.5 landscape with zero dips over
  |λ| ≤ 7 — observed, diagnosed by a new frame-rotation gate, fixed, and the
  spectrum appeared. G2b is mandatory in the sealed protocol; the failure is
  preserved in `results.json`.
- **Exact spectral symmetry is a theorem here**: J = σ₂∘conj anticommutes
  with D, preserves the ρ₁-twisted automorphy and the shifted lattice ⟹
  spec(D) = −spec(D) exactly, and ker D is even-dimensional (J² = −1). The
  probe's ±3e−13 pairing and dim-2 kernel match both consequences. This
  gives the sealed run an enforceable shape gate — partial compensation for
  the missing external anchor.
- **An instrument-level Kramers-type doubling**: the ENTIRE singular
  spectrum is doubled at every λ. Mechanism open (obligation O1); blocks
  multiplicity language, not eigenvalue claims.

## Honest boundaries

- Double precision throughout; nothing here is certified; the sealed run's
  criterion (DESIGN §10) is where a verdict can first exist.
- **No external anchor exists**: no prior computed Dirac eigenvalue on any
  hyperbolic 3-manifold was found (arXiv API, 3 targeted queries + 1
  must-pass control; Bär 2000 and the Bolte–Stiepan surface trace formula
  are analytic, not numerical). The sweep is arXiv-only and must be
  completed (O3) before any "first" sentence banks. Validation is
  internal-only and the banked FINDINGS must say so.
- The golden-search resolution floor (6e−9) masks the true two-Y agreement;
  the 8-digit statement rests on the three-instrument cross-check.
- ρ₂'s spectral type stays convention-dependent (O4); this arc computes ρ₁
  only.

## Cost forward (from B922's 58.1 h / 25-digit scalar anchor)

Sealed 10-digit first-window table: 1–3 days. Sealed 25-digit λ₁:
100–180 h (2–3× scalar; extrapolation). PSLQ rung on λ₁: hours.

## Files

`DESIGN.md` · `probe.py` · `results.json` · `validate_out.json` ·
`scan_results.npz` · `scan_dips.json` · `refined.json`
