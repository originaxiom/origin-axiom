# B1535 (pre-seal design note) — Theorem C's prediction for sm:B1532, written before sm:B1532's read-out

sm (the SM-derivation seat), 2026-10-04, written at 02:30Z.
- sm:B1532's route T finished at 02:25:28Z, and route L finished before it.
- `terms_T.jsonl` and `terms_L.jsonl` have not been opened, and `read_out.py` has not run.
- This note is committed and pushed before either happens, so the prediction below is blind.

## The theorem (B1535 §3, to be sealed with its controls)

**Theorem C (the cap).** Take:
- N, a finite cover of a complete finite-volume hyperbolic 3-manifold, with ρ its four;
- ν, a finite-order character of π₁N;
- any class c ∈ H¹(N; ν⁵ ⊗ ρ).

Then sm:B1515's frame W₁ = [[ν ⊗ ρ, c·ν⁻⁴], [0, ν⁻⁴]] satisfies two bounds.
- **The Λ² side:** I(Λ²W₁) = −dim(im δ¹ ∩ K) ∈ [−n(ν³ ⊗ ρ), 0].
  - δ¹ is the connecting map H¹(N; Λ²V*) → H²(N; (V ⊗ L)*) of (Λ²W₁)*.
  - K is the interior part of H²(N; (V ⊗ L)*), of dimension n((V ⊗ L)*) = n(ν³ ⊗ ρ).
- **The W side:** I(W₁) ≥ −b0 − n(ν⁴), with b0 = [ν⁴ = 1].

The proof uses five ingredients:
- sm:B1527's Lemma E, assembled from the two long exact sequences, on N and on the cusps;
- sm:B1515's Lemma 2 (unitary pieces have index 0) and Lemma T (the torus table at every parabolic cusp);
- Garland–Raghunathan, PH¹(Γ; so(3, 1)) = 0 for non-uniform lattices, as stated in Monroe, arXiv:2604.22004, §6.1 [21].
  - It gives sm:B1515's Lemma 3: the Higgs bulk ν²Λ²ρ has no interior class.
  - It gives the rigidity Λ_A ∩ π_A = 0, at every cusp, on N and on the finite cover ker ν².
- The connecting map δ¹ of Λ²W₁ vanishes identically. Its boundary composite is a sum of torus cups, all zero by the torus
  table (t1 = 5), and H²(N; Λ²V) injects into the boundary because there are no interior classes.

The two sides read the same in the other stacking order (W₂* = W₁(ν̄, c′)). So in either order a count (∓g, ∓g) needs both
n(ν³ ⊗ ρ) ≥ g and b0 + n(ν⁴) ≥ g.

Checked so far: a smoke test at m135's non-simple member u₁ against sm:B1534's banked terms, every identity holding. The full
control on all 144 banked terms (`verification/control_k1.py`) is running.

## The prediction for sm:B1532 (M₂–M₆, λ = 1, every finite abelian cover, pulled-back members, every class read)

Each term is T(ν, χ, c) = (I(W₁ ⊗ χ), I(Λ²W₁ ⊗ χ)) on M_n, with χ contributing, so χ is trivial on the cusp. Its Λ² piece has
quotient ν⁻³χ ⊗ ρ, and ν⁻³χ is again a λ = 1 character of M_n.

The supplies on the levels, from sm:B1515 §3, banked:
- **The four on M₁–M₅.** The twisted geometric four has no interior class at any λ = 1 character: n(ζ ⊗ ρ) = 0.
- **The four on M₆.** It has interior classes at 28 characters: n = 1 at 24 of order 8 (four deck orbits) and n = 2 at the 4 of
  order 5. Everywhere else on M₆, n = 0.
- **The line.** n(ζ) = 0 for every finite-order character of a once-punctured-torus bundle (B1535's Lemma W). The levels are
  such bundles.

A slip is disclosed here: a first draft of this note asserted from memory that every λ = 1 character of M₁–M₆ is simple. Checking
sm:B1515's banked table before the commit corrected it. It goes to ERROR_LEDGER at B1535's bank.

The prediction:
1. **The Λ² terms are capped by the four's supply.** −n(ν⁻³χ ⊗ ρ) ≤ T_Λ ≤ 0 at every member, twist and class sm:B1532 read, in
   both routes.
   - **On M₂–M₅ every Λ² term is 0.**
   - On M₆ a Λ² term can be non-zero only where ν⁻³χ is one of the 28 characters. There it lies in {0, −1} (order 8) or in
     {0, −1, −2} (order 5).
2. **The W terms are bounded below.** Every W term is ≥ −1, and −1 occurs only at χ = ν⁴, where L ⊗ χ is trivial (b0 = 1).
3. **Hence at most one generation**, in either order, at every count of every cover.
   - On a cover with deck characters B the cap reads g ≤ min(b0 + Σ_χ n(ν⁴χ), Σ_χ n(ν⁻³χ ⊗ ρ)) = min([ν⁴ ∈ B], ·) ≤ 1.
   - **No count is a three**, and sm:B1532 is NEGATIVE on three generations within its scope.
   - On M₂–M₅ no count is generation-shaped at all, since every Λ² sum is 0.
   - On M₆ a (−1, −1) is not excluded by the cap: it needs ν⁴ ∈ B and a twist in B that carries a 5̄′.

If sm:B1532 reads a term outside these bounds, either Theorem C's proof or an instrument has a bug. The term is then re-read in
both routes before anything is banked, under sm:B1532's own adjudication rule (its §9).
