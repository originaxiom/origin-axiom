# The read-out on the whole has a limit, the same at every point of order 5 — main's draft proof (2026-11-14; P-845)

*Main's draft, before any check; a seat's check is owed before it is banked. Standard ergodic theory applied to the
record's objects; each standard fact is cited, not re-proved.*

## Setting

- **Words.** w ∈ {L, R}ⁿ containing both letters. Its matrix M_w is hyperbolic. Its thread is the closed geodesic of
  γ_w = M_wᵀ, of length ℓ(w) = 2 log λ(w).
- **Points of order 5.** P₅ is the set of the 24 points (i/5, j/5) ≠ 0 of the torus. SL(2, ℤ) acts on P₅ through
  G = SL(2, F₅) by B1724's transport rules, transitively.
- **The frame.** F(τ, p) is the frame's outputs at the modulus τ and the line p, with an end that is covariant. Two
  ends qualify: B1921's invariant end held constant, and B1667's canonical end. Then F(gτ, g·p) = F(τ, p) for g in
  SL(2, ℤ) (B1724; B1921; for the canonical end, `audit/canonical_end/grid.py`'s check (3)). So F is a function on
  Y = SL(2, ℤ) \ (ℍ × P₅), the modular curve of level 5 with a marked point of order 5.
- **Allowed words.** w is allowed when M_w fixes the mark's class ±v (v = (1, 2)). Along an allowed word's thread the
  mark transported returns to itself, so A(w) = (1/ℓ) ∫ F along the lifted closed orbit is well defined (B1922).
- **The read-out.** R_n is the average of ∫F over the allowed words of length n, divided by the average of ℓ: the
  move-count measure, length-weighted (P-845).

## Claim

R_n → ∫ F̄ dμ as n → ∞, where:
- F̄(τ) = (1/24) Σ_{p ∈ P₅} F(τ, p), a function on the modular surface;
- μ is the flow-invariant probability measure that the uniform (Bernoulli ½, ½) measure on L/R sequences induces on
  the unit tangent bundle of the modular surface.

**Consequences.**
1. The limit exists.
2. It is the same for the mark, for its twin, and for every point of order 5. So the twin's fading (B1924) is a
   theorem, and the reading point is removed in the limit.
3. The limit can be computed without the constraint on words, as the ergodic average of F̄ along μ-typical geodesics.

## Proof (sketch; each step a standard result)

1. **Coding** (Series, 1985; the Farey tessellation). Oriented geodesics on the modular surface correspond to
   bi-infinite L/R cutting sequences, and closed geodesics to cyclic words. The shift is the first-return map to a
   cross-section, and the return time r(x) is the hyperbolic length between successive crossings, Hölder in x. The
   uniform measure ν on sequences gives, by suspension, the flow-invariant probability μ = (ν × dt)/E_ν r. Here
   E_ν r < ∞, since it is the Lyapunov exponent of the random product per letter. μ is singular with respect to
   Liouville, as B1868 found.
2. **Birkhoff sums over periodic points.** ∫_{γ_w} F = S_n f(w^∞) and ℓ(w) = S_n r(w^∞), where f(x) is the integral
   of F over the segment of one letter. For the full shift, the uniform measure on the periodic points of period n
   converges weak-* to ν. f is bounded, because the outputs are ratios of singular values and moduli of unitary
   entries, all in [0, 1]. f is continuous off a set where singular values coincide (needed: μ-null, see H1).
3. **The level-5 extension.** The holonomy of a word in G = SL(2, F₅) is a cocycle over the shift. The letters'
   images generate G, and G = 2I is perfect, so no homomorphism G → ℤ/d with d > 1 exists. Hence the skew product of
   the full shift by G is topologically mixing (the standard criterion for finite group extensions; Parry and
   Pollicott, Astérisque 187–188, ch. 8, the Chebotarev-type theorem for closed orbits).
   - So the holonomies of the words of length n equidistribute in G, jointly with the Birkhoff averages.
   - In particular, the allowed words have proportion |Stab(±v)|/|G| → 10/120 = 1/12.
   - Conditioned on that, the lifted Birkhoff average along the closed orbit through the mark's sheet converges to
     the integral of f against ν × (uniform on the G-orbit of the mark), and that orbit is all of P₅.
4. Dividing by the length, R_n → E_{ν × unif}[f]/E_ν[r] = ∫ F̄ dμ. ∎ (modulo H1 to H3)

## Hypotheses to check (owed before banking)

- **H1:** F is continuous μ-almost everywhere. The mixing moduli come from singular vectors and jump where singular
  values coincide. That set must be μ-null; μ is singular, so this is not automatic.
- **H2:** the weak-* convergence uses bounded F that is continuous μ-a.e. on a non-compact surface. Tightness holds
  because E_ν r < ∞. To check: the cusp excursions of μ-typical paths do not carry F's discontinuities.
- **H3:** the joint equidistribution in step 3 with length weights. To check: the weights ℓ(w) are Birkhoff sums of the
  Hölder r, which is covered by the same theorem.
- **The rate:** not claimed. B1924 sees the twin's difference fall below its errors by n = 16.

## The test the proof predicts (running: `fiber_grid.py`, then the ergodic average)

∫ F̄ dμ is computed from F̄ tabulated on a grid of the fundamental domain and averaged along many random geodesics. The
constraint is not needed, since F̄ is invariant. It must agree with B1924's read-outs at the mark and at the twin
(n = 22, the constant ends) within their sampling errors. A disagreement beyond the errors refutes the claim as stated,
or one of H1 to H3.

## Addendum (2026-11-14, morning): H2 and H3 argued (main; the seat's check still owed)

- **H2, tightness.** The base measures (uniform on the periodic points of period n) converge weak-* to ν on the compact
  shift space. The suspension is not compact, because the roof r is unbounded near L^∞ and R^∞. But r grows only like
  the logarithm of the length of the run of one letter at the crossing, and under ν, and under every ν_n for runs
  shorter than n, a run of length k has probability of order 2^(−k). So ν_n(r > t) is super-exponentially small in t,
  uniformly in n: r is uniformly integrable. Weak-* convergence of ν_n with a uniformly integrable roof gives weak-*
  convergence of the normalised orbit measures μ_n to μ (portmanteau). F is bounded and continuous off a μ-null set
  (H1), so ∫ F dμ_n → ∫ F dμ.
- **H3, the length weights and the constraint.** R_n weights each word by ℓ(w) = S_n r(w^∞), a Birkhoff sum of the same
  uniformly integrable r. The constraint keeps the words whose holonomy in G = SL(2, F₅) fixes the mark's class. The
  skew product of the full shift by the letters' images is transitive (they generate G) and mixing (G is perfect, so it
  has no cyclic quotient). Its periodic points with a prescribed holonomy class therefore equidistribute to ν × Haar,
  jointly with the Birkhoff sums: the finite-extension case of Parry and Pollicott's closed-orbit theorem, here for the
  full shift's periodic points.
- **The numerical face** (`h2_h3_check.py` → `h2_h3_check_run.txt`; 2 000 words at each n). The length per letter has
  mean 0.792 at n = 20, 50, 100 and 200, with spread 0.068, 0.043, 0.030 and 0.021, falling like 1/√n. The longest run
  grows like log₂ n (mean 4.7 at n = 20, 8.0 at n = 200). A run of 2 log₂ n + 4 or more occurs in 0.2 % of words or
  fewer.
- **So H1 to H3 are met as argued by main.** The verdict stays OPEN until agy-002's independent check of the sketch
  (M26) and its computation of B1924 (M23 to M25), as the rule of a second computation asks.

