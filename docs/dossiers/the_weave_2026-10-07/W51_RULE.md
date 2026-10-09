# W51 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **W50 found the state that breaks the weave's group:** the modulus τ. On the owner's ruled branch every value of τ
  breaks it, and at a generic value nothing survives on T but scalars. But at i and at ω the couplings in τ alone are
  degenerate, and nothing on record fixes τ.
- **The owner chose to look for what fixes τ** (2026-10-09). The question is whether a functional the weave itself
  supplies, with no free parameter, selects a value of τ, and which one.
- **The record so far.** Main's τ = ω is a tagged postulate (B1617). This seat's relay §38, corrected in §42: selecting
  τ needs a stated functional, and potentials built from the threads select i or ω depending on the kernel.

## Weave or thread?

- **W50's N6:** T is the representation of η²¹·(θ₄², θ₂², θ₃²) on the parities (½, 0), (0, ½), (½, ½).
- **One parity's quantity is not the weave's.** |θ_p/η|² is invariant only under that parity's stabilizer, not under
  the moves. The weave's quantities are the functions of all three parities at once that every move keeps: the
  symmetric functions.
- **So the candidates are fixed by THE WEAVE rule,** none hand-picked: the elementary symmetric functions of the three
  parity sectors' determinants, T's own norm, and the untwisted sector's determinant as the baseline.
- Weave-type.

## The candidates (each a real function of τ, invariant under SL(2, ℤ) and τ ↦ −τ̄, with no free parameter)

- **x_p = |θ_p(τ)/η(τ)|²** is the determinant of the Laplacian twisted by parity p's character: Kronecker's second limit
  formula, up to a universal constant. It is also the partition function of a Dirac fermion with that even spin
  structure.
- **e₁ = Σ_p x_p and e₂ = Σ_{p<q} x_p x_q:** the sum over the three sectors, and the second symmetric function.
- **e₃ = Π_p x_p:** the joint determinant of the three sectors, the weave's direct sum.
- **N_T = y^{−1/2} Σ_p |θ_p²/η³|²:** the invariant norm of T's canonical form at weight −½. It is also the partition
  function of two Dirac fermions and one non-compact boson in each sector. It equals D^{−1/2} Σ_p x_p².
- **P_T = Π_p y^{−1/2} |θ_p²/η³|²,** the joint norm. It equals 16 D^{−3/2}.
- **D = y |η|⁴:** the untwisted sector's determinant (the torus alone), the baseline.

## The facts by hand

1. **The joint determinant is flat.** e₃ = |θ₂θ₃θ₄|²/|η|⁶ = 4 at every τ, by Jacobi's identity θ₂θ₃θ₄ = 2η³. So the
   three parity sectors together do not select τ at all.
2. **The symmetric sums are minimized exactly at ω.**
   - AM–GM with e₃ = 4 gives e₁ ≥ 3·2^{2/3} ≈ 4.762203 and e₂ ≥ 3·2^{4/3} ≈ 7.559526.
   - Equality holds exactly where |θ₂| = |θ₃| = |θ₄|. That forces |λ| = |1 − λ| = 1 (λ = θ₂⁴/θ₃⁴), so λ = e^{±iπ/3}
     and j = 0: the orbit of ω.
   - At i: x₃ = 2 and x₂ = x₄ = √2, so e₁ = 2 + 2√2 ≈ 4.828427 and e₂ = 2 + 4√2 ≈ 7.656854.
3. **D is maximized at ω** (Osgood, Phillips and Sarnak: among flat tori of fixed area the hexagonal one maximizes the
   determinant). With η(i) = Γ(¼)/(2π^{3/4}) and |η(ω)| = 3^{1/8} Γ(⅓)^{3/2}/(2π): D(ω) ≈ 0.3558 and D(i) ≈ 0.3483.
4. **N_T and P_T are minimized at ω,** since N_T = D^{−1/2} Σ x_p² ≥ 3·2^{4/3}·D^{−1/2} and P_T = 16 D^{−3/2}.
   N_T(ω) ≈ 12.674 and N_T(i) ≈ 13.555; P_T(ω) ≈ 75.40 and P_T(i) ≈ 77.84.
5. **Every smooth invariant function is critical at i and at ω.** Their stabilizers rotate the tangent plane by π and
   by 2π/3.
6. **The boundary of the half fundamental domain** (x = 0, x = ½, and the arc |τ| = 1 between them) is fixed by
   anti-holomorphic symmetries. So a function's normal derivative vanishes there, and its critical points on the
   boundary are the critical points along each piece.
7. **Toward the cusp:** e₁, e₂, N_T and P_T grow without bound (x₃ and x₄ grow like |q|^{−1/12}), while D → 0.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **G1** | e₃ = 4 at every point of a grid over the fundamental domain, to 10⁻¹⁰. Jacobi's identity holds at the same points. | 97% |
| **G2** | e₁ and e₂ have exactly two critical points in the half fundamental domain: ω, the global minimum (3·2^{2/3}, 3·2^{4/3}), and i, a saddle (2 + 2√2, 2 + 4√2). Both grow without bound toward the cusp. | 80% |
| **G3** | D has exactly two critical points: ω, the global maximum, and i, a saddle. N_T and P_T have the same two, with ω their global minimum and i a saddle. The values match facts 3 and 4's closed forms to 10⁻⁸. | 80% |
| **G4** | No candidate has an extremum at a point other than i, ω or the cusp. | 80% |

**Extra read-outs (no prior).**
- The invariant norms y^k ‖Y_k(τ)‖² of W50's one-dimensional coupling spaces (O₊ and O₋ at k = 3, D and O₋ at k = 5,
  D at k = 7): their critical points and extrema over the fundamental domain.
- The values of every candidate at i, at ω and along the boundary.

**The reading, written before the run.**
- **If G1 to G4 hold, nothing canonical in the weave selects a generic τ.**
  - The weave's joint determinant over its three parities is flat, so the parity sectors together leave τ free.
  - Every other canonical candidate depends on τ only through symmetric sums and the untwisted η. Each is extremal
    only at ω (or i, as a saddle), or it runs to the cusp.
- **So a canonical selection gives one of two places.**
  - **ω**, if the principle minimizes the symmetric functionals. That gives main's tagged τ = ω a weave reading, and
    there W50's couplings are degenerate.
  - **The cusp**, if it maximizes a partition function. There the couplings become hierarchical in powers of q^{1/8},
    and the four-dimensional count depends on the cusp's end data (W45 to W48).
- **Either way, realistic flavour needs τ away from the fixed points**, a departure nothing canonical supplies:
  forced to choose, not forced which.
- **If a coupling norm (an extra read-out) is extremal at a generic point,** that point is a candidate the principle
  could force, if a coupling's strength is the thing it extremizes. The reading names that as a question, not a
  result.
- **If G2 to G4 fail** (a critical point away from i and ω), that point is a canonical candidate for τ, and the arc
  changes.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
