# B1509 — predictions committed before the direct verification run

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Status of this file:** written and pushed before
`verification/extension_index.py` exists. Its git hash is the order of record.

**The question** is lead 1 of B1508, "the join on the projective vacuum". The audit lane (codex's second lane) has a finite-energy
harmonic vacuum family on m004's convex-projective deformation, which is vector-like (R42–R56). Its matter H¹ classes appear only
at the exceptional points: a central twist μ ∈ μ₄ of Ballas' representation ρ_q, at q = 17 ± 12√2 for μ = −1 and at
q = 7 ± 4√3 for μ = ±i. There h¹(4 ⊗ μ) = h¹(4̄ ⊗ μ⁻¹) = 1.

Does the minimal non-split extension of that vacuum carry main's index? The extension is the rank-five analogue of the audit
lane's R40, W = V + L, transplanted from main's m010 witness onto the harmonic family.

## What was run before this file, and what it showed

`verification/control_exceptional.py` (record `control_exceptional_run.txt`) was meant as a pre-seal reproduction of the lane's
exceptional points. It reproduces them exactly:
- the relator holds;
- the longitude has characteristic polynomial (X − q)³(X − q⁻³);
- h¹ = 1 for the defining 4 and for the dual at the six pairs (q, μ);
- h¹ = 0 at the generic samples q = 1/3, 2, 5, 17 for all four central twists.

It also printed the full two-variable twisted Alexander numerator:

    D(q, s) = −(s − 1)⁴ · Q(q, s),   Q = −q s⁴ + 8q s³ + (q² − 16q + 1) s² + 8q s − q.

That went beyond the control's stated scope, which was not to read any multiplicity in the twist variable (ERROR_LEDGER, rule
slip). Q is palindromic in s: Q = s²·P(s + 1/s), with P(x) = −q x² + 8q x + q² − 14q + 1. Checked symbolically. The outcome below
therefore follows from theorems T1–T3 together with that printed polynomial. This arc is banked as decided at design time, as
B1500, B1502 and B1504 were. The direct run that follows is a verification of the predictions, not a blind test.

## The theorems (proofs in FINDINGS)

- **T1 (the matter is boundary-acyclic).** For q > 0, q ≠ 1, the longitude acts on 4, 4̄ and 6 = Λ²4 with eigenvalues among q,
  q⁻³, q², q⁻², q³, q⁻¹ — never 1. Every character of H₁(m004) = ℤ is trivial on the null-homologous longitude. So each such sector,
  twisted by any character, has H*(T; V) = 0. Then H*(M; V) = H*(M, ∂M; V), every end condition gives the same space, and
  h¹(V) = h¹(V*): the sector is vector-like in every count (the defining and dual case is R44's acyclicity).
- **T2 (the extension's index).** Let A have H⁰(A) = H⁰(A*) = 0, an acyclic boundary torus and h¹(A) = 1 with generator c. Let
  W₁ = [[A, c], [0, 1]] (rank five). Then I(W₁) = −r₁ ∈ {0, −1}, and I(W₁) = −1 iff e ∪ c = 0 in H²(M; A), where e generates
  H¹(M; ℂ).
  - The reason: on T the extension splits, H*(T; W₁) = H*(T; 1), and the restriction factors through H¹(M; 1).
  - With the opposite order, W₂ = (W₁[A*])*, so I(W₂) = −I(W₁[A*]) ∈ {0, +1}.
  - Λ²W₁ is boundary-acyclic by T1, so I(Λ²W₁) = 0.
  - Only central twists can fire. For a non-central μ, the line μ⁻⁴ needed for det = 1 is non-trivial on the meridian, so the
    boundary is acyclic and I = 0.
- **T3 (when e ∪ c vanishes).** m004 fibres over the circle with fibre F, a once-punctured torus, and monodromy acting on
  H¹(F; A) ≅ ℂ⁴. By the Wang sequence (with H⁰(F; A) = 0), H¹(M; A) = ker(T − 1) and H²(M; A) = coker(T − 1), and e ∪ is the
  natural map ker → coker. So e ∪ c = 0 iff eigenvalue 1 of T has a Jordan block of size ≥ 2. With h¹ = 1 that holds iff μ is a
  root of multiplicity ≥ 2 of the twisted Alexander polynomial in s.
  - By the palindromic form, s = −1 is a ramification point of s ↦ s + 1/s. So at q = 17 ± 12√2, where P(−2) = 0 and
    P′(−2) = 12q ≠ 0, the root s = −1 is double.
  - At s = ±i the map is unramified (P′(0) = 8q ≠ 0), so the roots are simple.

## The predictions (to be checked by the direct run, exact and over three primes)

| | prediction | basis |
|---|---|---|
| D1 | I(W₁) = −1 at (q, μ) = (17 ± 12√2, −1) | T2 + T3 (double root) |
| D2 | I(W₁) = 0 at (7 ± 4√3, +i) and (7 ± 4√3, −i) | T2 + T3 (simple roots) |
| D3 | I(W₂) = +1 at (17 ± 12√2, −1); 0 at the four ±i pairs | T2 for A* (Δ_{A*}(s) ≐ Δ_A(1/s), so the same multiplicities) |
| D4 | I(Λ²W₁) = I(Λ²W₂) = 0 at all six pairs | T1 |
| D5 | the formal SU(5)′ content of W₁ at the μ = −1 points: N(10′) = −I(W₁) = 1, N(5̄′) = −I(Λ²W₁) = 0. One 10 without a 5̄ is SU(5)³-anomalous, so the bulk count alone is not a consistent spectrum; an end contribution (inflow) is required | D1, D4 + E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅ |
| D6 | the extension class lies in the (4, 1₅) component of the (4, 16) of E₈ ⊃ SU(4) × Spin(10): the SU(5)′-singlet part of the light 16. The extension breaks Spin(10) to SU(5)′ and is F-flat but not polystable, so it needs a source (R41) or the 16̄ partner | representation theory (checked in the run: the off-diagonal block has U(1)_T charge 5) |

If the direct run disagrees with D1–D4, then T2 or T3 is wrong, and the arc reports that. 0 of 19.
