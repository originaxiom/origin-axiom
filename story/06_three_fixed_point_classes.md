# 06 — The three fixed-point classes

> Narrative, not claim. Cites the mathematics one-way.

The trace map has three kinds of fixed point, and the program eventually computed all three — the third had never
been done before (**B106**, V92/V93):

- the **trivial** rep (the void) → the real **Dickson tower** (chapter 02);
- the **geometric** rep → the *complex* **adjoint torsion** / twisted-Alexander invariant (`τ₁ = −3`), *not* the
  tower — which is how the program learned the tower is a strictly trivial-rep object (**B98/B99**, cross-checked
  against the Zickert Ptolemy variety and Baker–Petersen, **B100**);
- the **Dehn-filling** reps → **degree=rank**, the A-polynomial relations `Mⁿ = L`, **partially elliptic** with
  **root-of-unity** eigenvalues.

Three distinct Jacobian signatures — the trivial and geometric reps hyperbolic, the Dehn-filling reps
center-like. Two disciplined results came with the third class. An **honest negative**: the stability *type* does
*not* encode the degree=rank exponent — both SL(4) Dehn-filling components share the signature `(4,4,7)` yet have
exponents 4 and 3, so no mechanism is read off the Jacobian. And a clean carrier instead: degree=rank holds
**per eigenvector**, `Lᵢ = c·Mᵢ^k` with `c` a root of unity. A V93 hygiene pass then separated corroboration from
novelty (the SL(4) principal `c = −1` re-confirms the proved B89/B83; the secondary `c = i` is the genuinely new,
still-numerical content) and passed the root-of-unity values through the gauge-noise gate (seed-stable across
seeds — real structure, not `pinv` artifact).

Those root-of-unity scalars `c ∈ {1, −1, i}` are exactly what the central `ρ_n` target wants to *predict* from
`θ = −w₀` — the bridge from this chapter back to chapter 04, and the project's top open calculation (chapter 08).

→ `07_the_physics_sweep.md`.
