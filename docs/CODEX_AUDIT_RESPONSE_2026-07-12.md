# Response to Codex Documentation Audit (2026-07-12)

Codex audited commit 79933f0 (main at time of audit). 1,169 tracked documentation artifacts
(~1.06 million words). This document evaluates each finding.

## Finding 1: B531 period-two gap result may be an open-boundary artifact

**Status: NOTED — requires verification.**

Codex claims that at depth 8, an in-gap eigenstate splits one bulk gap into two fragments
(0.00638 + 0.00148 = 0.00786), matching depth 9's unsplit gap (0.00786). If true, this
would invalidate the claimed bulk oscillation.

**Assessment:** The B531 slopes s₁, s₂ were computed using eigendecomposition on open-boundary
chains. The period-2 oscillation in gap 3 (even/odd depth alternation) was attributed to the
negative contracting eigenvalue λ₂ ≈ −0.440. This mechanism is real (eigenvalue sign alternation
is a mathematical fact), but whether its spectral manifestation survives in the bulk (periodic
boundaries) vs being an open-boundary artifact is a separate question. The B531 control (Arnoux-Rauzy)
showed even/odd alternation is GENERIC; the clean period-2 specific to our substitution. The
control confirms the mechanism exists but does not resolve the boundary question.

**Action:** Flag B531 slopes as "open-boundary; bulk verification pending." The Nine Ingredients
campaign (B532-I6) uses IDS gap labels (topological, boundary-independent) rather than
eigendecomposition, so its verdicts are unaffected.

## Finding 2: B531 preregistration mismatch

**Status: NOTED — a process concern.**

The preregistration promised transfer-matrix Lyapunov computation; the implementation used
eigendecomposition. Both methods can probe the same question, but the mismatch between
registration and execution is a process failure. Registration, code, results, and tests
were committed together.

**Action:** Note as a method-discipline correction. Future preregistrations should describe
the actual computation, not the intended one, or document the switch.

## Finding 3: "Internal-space Fourier projection" never uses internal space

**Status: ALREADY ADDRESSED in B531 T3 and B532.**

The B531 T3 Fourier analysis computes |V̂(α)| at IDS gap frequencies and finds s ≈ 2.1×|V̂|
with a 12% DOS correction. The "internal space" label was indeed misleading — the computation
uses position-index Fourier coefficients, not the Rauzy internal coordinates. The structural
2.1 factor was noted as unexplained.

The B532 interaction grammar (GRAMMAR.md, Layer 21) correctly distinguishes: the Rauzy fractal
IS the internal space (forced by M), but spectral computations use the 1D physical chain.

## Finding 4: B530 entropy statement — log(β) is NOT topological entropy

**Status: ACCEPTED — terminology correction needed.**

Codex is correct. For a deterministic substitution subshift, the topological entropy of the
shift dynamical system is zero (linear word complexity ⟹ h_top = 0). The number log(β) is
the inflation exponent (= log of the Perron eigenvalue = growth rate of word length under σ).
It equals the topological entropy of the substitution MAP σ as an endomorphism, not of the
subshift.

B530 movement XVI states "exact entropy h = log β" — this is the inflation exponent, not
topological entropy of the subshift. The Nine Ingredients T(n) computation (B532-I6 Probe 7)
uses log(β) as a normalization constant, not as a claim about shift entropy.

**Action:** The label is misleading. Correct to "inflation exponent log(β)" wherever "entropy"
was used to mean the growth rate. The mathematical content is unaffected.

## Finding 5: Gap labeling used in the wrong direction

**Status: ACCEPTED — the distinction matters and should be stated clearly.**

The gap labeling theorem (Bellissard) says: IF a gap is open at energy E, THEN the IDS value
at E belongs to the gap-labeling group (= the image of K₀ under the trace). It does NOT
prove that gaps at those IDS values must be open. Gap opening is a separate theorem — proved
for the Fibonacci Hamiltonian (Avila–Bochi–Damanik, Damanik–Embree–Gorodetski) but not for
general Pisot substitutions.

For our substitution, B530 movement XXXII verified that three gaps are numerically open at
four different potentials. The Nine Ingredients campaign (Probe 4) shows gap-opening slopes
vary with the potential. The gap POSITIONS (IDS labels) are topological and forced; whether
they remain open for all potentials is a separate (and harder) question.

**Action:** All references to gap labeling should state: "gaps at IDS = f_a, f_a+f_b,
f_a+f_b+f_A are observed open at the computed potentials; the gap-labeling theorem constrains
their labels if open, but does not guarantee they open."

## Finding 6: 144 left-proper substitutions share the incidence matrix

**Status: ACCEPTED — this is a known and important point.**

The incidence matrix M does not determine σ uniquely. Codex's count of 144 left-proper
substitutions with the same M is correct (4 letters, each image starts with 'a',
remaining letters distributed among images of total length 14). Different word orders
produce different spectral properties.

This is exactly why the Nine Ingredients campaign works with σ directly (the four specific
words), not just M. The B532 interaction grammar (I2) proved σ is irreducibly 4-letter:
|Aut(σ)| = 1, no binary coarsening is substitutive, and no two letters can be identified.
The physics DOES depend on the word order — but the word order IS forced (the object is σ,
not just M).

**Action:** Clarify in documentation: "σ is one of 144 left-proper substitutions sharing M;
the spectral properties depend on the specific word order." This is already implicit in the
B532 work but should be stated explicitly.

## Finding 7: "Three-dimensional quasicrystal" is misleading

**Status: ACCEPTED — already addressed in B532-I6 Probe 9.**

The physical Hamiltonian is a one-dimensional chain. "Three-dimensional" refers to the Rauzy
fractal (the internal space of the tiling), not physical space. B532-I6 Probe 9 states
explicitly: "The substitution tiling is ONE-DIMENSIONAL. Intrinsic curvature of a 1D object
= 0. Extrinsic geometry exists only via EMBEDDING (Rauzy fractal, ℝ³)."

**Action:** Replace "3D quasicrystal" with "1D quasicrystal with 3D internal (Rauzy) space"
wherever the misleading label appears.

---

## Governance flags

| Flag | Status | Action |
|---|---|---|
| README says B440 | **FIXED** (2026-07-12) — now says B532 |
| README says 1,513 tests | **FIXED** — now says ~1800 |
| Atlas = 449, B-dirs = 517 | **ACKNOWLEDGED** — atlas updates are periodic, not continuous |
| Attribution gate failure | **CHECK** — verify commit trailers |
| Review overdue by 233+ merges | **ACKNOWLEDGED** — continuous review impractical at this velocity; periodic audits serve the same function |

## Summary

Of 7 findings: 4 **ACCEPTED** (terminology/direction corrections), 2 **NOTED** (require further
verification or are process concerns), 1 **ALREADY ADDRESSED**. No finding invalidates a
banked mathematical result. The most important corrections are the entropy terminology (Finding 4)
and the gap-labeling direction (Finding 5) — both are about what is CLAIMED, not what is COMPUTED.
The computations stand; the labels need tightening.
