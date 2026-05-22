# Origin Axiom — Claims Ledger

**This is the living source of truth for what the project claims.** It is governed by
`GOVERNANCE.md`. Every result must appear here with an ID, a status label, and an evidence
pointer. Prose elsewhere in the repo may not exceed the label of the claim it rests on.

**Status labels:** `proven` · `conditional` · `open` · `dead` (see `GOVERNANCE.md` §3).
**Evidence** points to the test that locks the claim. All thirteen `proven` claims are locked
by passing tests (39 passed, 1 optional SnapPy check skipped). P1–P10 were frozen at tag
`phaseA-foundation-freeze`; P11–P13 were added in the session-3 integration.

**Last updated:** 2026-05-22 · derived from `AUDIT_REPORT.md` §4; Phase A tests added;
P11–P13 added (exact-algebra results promoted from the session-3 review).

---

## Proven — exact, checkable, safe to build on

| ID | Claim | Evidence |
|---|---|---|
| P1 | `L=[[1,1],[0,1]]`, `R=[[1,0],[1,1]]` are primitive parabolic shears; `A=LR=[[2,1],[1,1]]` has trace 3, det 1, `χ_A=t²−3t+1`, eigenvalues `φ²`, `φ⁻²`. | `tests/test_algebra.py` ✓ |
| P2 | `A = P·Nτ²·P` and `Aⁿ = P·Nτ²ⁿ·P`, where `Nτ=[[0,1],[1,1]]` is the Fibonacci fusion-count matrix and `P` the basis swap. | `tests/test_fibonacci.py` ✓ |
| P3 | `L+R=[[2,1],[1,2]]` is exactly a normalized 1D zero-field Ising transfer matrix at `K=½log2`; correlation length `ξ=1/log3`. | `tests/test_ising.py` ✓ |
| P4 | `A=LR` is exactly a Zimm–Bragg helix-coil transfer matrix at `s=2`, `σ=½` (weakly cooperative). | `tests/test_zimm_bragg.py` ✓ |
| P5 | Word-ensemble thermodynamics: `Z_N^count=2ᴺ`, `Z_N^trace=Tr((L+R)ᴺ)=3ᴺ+1`; thresholds `β_c^count=log2`, `β_c^trace=log3`. | `tests/test_thermo.py` ✓ |
| P6 | `L` and `R` preserve only degenerate symmetric forms; `A` preserves the non-degenerate `G=[[-2,1],[1,2]]`, signature (1,1), det −5; null directions of `G` = `φ`-eigenvectors of `A`. **Phase-space, not spacetime.** | `tests/test_preserved_form.py` ✓ |
| P7 | The gluing identity `S_A = ext_{m,s}[S_L − F_R + ms]` holds exactly (Sympy-verified); model-level. | `tests/test_gluing.py` ✓ |
| P8 | `|det(Aⁿ−I)|` equals the torsion order of `H₁` of the mapping torus of `Aⁿ`; `(1/n)·log|det(Aⁿ−I)| → log(φ²)`. | `tests/test_torsion.py` ✓ |
| P9 | Figure-eight knot (4₁): `vol≈2.0299`, `H₁=ℤ`, `CS=0`, amphichiral. Sister m003: same volume, `CS=0.25`, `H₁=ℤ⊕ℤ/5`. | `tests/test_snapdata.py` ✓ |
| P10 | Five independent filters — trace-3 algebraic sieve, minimum hyperbolic volume, amphichirality, rank-2 categorifiability, Eisenstein triangulation — all select the figure-eight knot complement. | `tests/test_sieve.py` ✓ |
| P11 | `log(A)` decomposes exactly in the sl(2,ℝ) basis as `a·H + d·(E+F)` with `a = log(φ²)/√5`; the ratio `d/a = 2` exactly and the antisymmetric `(E−F)` coefficient is exactly `0`. Pure algebra (a closed form for `log A`); no physical interpretation. | `tests/test_sl2_decomposition.py` ✓ |
| P12 | The figure-eight gluing equation `z²(z−1)²=1` factors exactly as `(z²−z+1)(z²−z−1)` — an Eisenstein quadratic (discriminant −3) times a golden quadratic (discriminant 5). | `tests/test_gluing_equation.py` ✓ |
| P13 | The shape matrix of `log A`, `[[1,2],[2,−1]]`, and the preserved form `G` are isospectral (both det −5, eigenvalues ±√5). Elementary corollary of P11 + P6. | `tests/test_preserved_form.py` ✓ |

---

## Conditional — true only given assumptions that were chosen, not forced

| ID | Claim | Named assumption |
|---|---|---|
| C1 | `L` and `R` are *forced* as the primitive record moves. | Depends on the minimal record axioms A1–A6 (see V4 paper §2). Well-motivated; not laws of nature. |
| C2 | The Fibonacci `|F|²` probability matrix is reconstructed from `A`'s Perron eigenvector. | Requires an additional "Perron-switch / degeneracy" rule; plain MaxEnt gives ½,½. |
| C3 | Trace 3 is the unique torsion-free hyperbolic trace. | Holds only within once-punctured torus bundles with `SL(2,ℤ)` monodromy. |
| C4 | The `(disc 5)(disc −3)` state-integral factorization is unique to the figure-eight. | Verified for 11 census manifolds only — a census check, not a proof. |

---

## Open — research targets (Phase B / `frontier/`). NOT partial results.

| ID | Target |
|---|---|
| O1 | Physical spacetime emergence (beyond a phase-space form). |
| O2 | Derivation of 3+1 dimensions. |
| O3 | Einstein's field equations. |
| O4 | Matter / Standard Model content. |
| O5 | The cosmological constant. |
| O6 | The fine-structure constant. |
| O7 | Any empirical prediction outside toy/transfer models. |
| O8 | Fibonacci `F`-symbol amplitudes and `R`-symbol phases (i.e. genuine anyon physics). |
| O9 | Derivation of the marked cusp incidence data from the action alone. |

Handoff-document steps 3B → 6 ("path to Einstein") map onto O1–O5. The first concrete
frontier probe is whether the gluing identity `W = S_L − F_R + ms` maps onto the discrete
Chern–Simons flatness condition `F = 0` — a well-defined yes/no computation.

---

## Dead — falsified or shown circular. Permanent. See `docs/ARCHIVE.md`.

| ID | Killed claim | Why it died |
|---|---|---|
| D1 | `k ≈ 137` sets the cosmological constant. | Wrong Chern–Simons normalization; correct scaling gives no special `k`. |
| D2 | `Λ = Λ_Planck · φ⁻²ᴺ`. | Circular — `N` is defined by the answer it is meant to predict. |
| D3 | Dynamic dark energy `Λ(t)`. | Predicts `w ≈ −0.04`; ruled out at ~30σ by observation. |
| D4 | `|Z| = 1/φ` is a unique signature of the figure-eight. | Generic feature of level-5 `SU(2)` cyclotomic algebra. |
| D5 | Casimir energy depends on `φ`. | Leading-order Casimir energy is universal across cavity ratios. |
| D6 | Phonon zero-point stability is maximized at `φ`. | Coefficient of variation is flat across mass ratios. |
| D7 | The figure-eight cusp minimizes the Epstein zeta function. | The figure-eight cusp is rectangular, not equilateral. |
| D8 | Positive `L`, `R` satisfy the braid relation `LRL=RLR`. | Direct computation: `LRL ≠ RLR`. |
| D9 | The `φ^φ` axiom. | Tested computationally in early work; failed. |
| D10 | `θ*` extracted from CKM/PMNS observables is a *derivation*. | It is a one-parameter fit, not a derivation. |
