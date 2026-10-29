# W177 — the frame's kernel norms in closed form: the twisted norms c_s that W89 computes by quadrature, as an exact series, with their cusp limit and first correction (the rule, committed before the script)

The SM-derivation seat, 2026-10-29, at the owner's "all u reccomend" (this seat's item 4: W174's S0 settled exactly).
Committed and pushed before the script that reads it exists. Nothing here is a result.

## Why

- **W174's S0 failed.** On 46 of 179 resolved lines the six's exponents had not converged by Im τ = 6.
- **What the exponents depend on.** A read-only map of W174's construction (this seat's, before this rule; disclosed
  below) found the following:
  - The largest mass's exponent follows exactly from a min-plus count.
  - The two mass ratios do not, because the record's objects cancel at leading order: Σ_s R_s² ≡ 0, and the Higgs
    vector DR is null at leading order.
  - So the ratios are set by second-order terms. Among them is the first correction to the kernel norms c_s
    (W89's `norm`, a 100 × 60 polar quadrature in double precision), and that correction is not on record.
- **The exact exponents therefore need the norms exactly.** This arc gives them. W178, under its own rule, then reads
  the six's exponents.

## The derivation (by hand, before any check)

**Conventions.** These are W89's: Jacobi θ_s(z|τ) with argument πz and nome e^{iπτ}; θ₁′(0) = dθ₁/dz at 0. The shift
ū is reduced to the centred cell, ū = α + βτ with α, β ∈ [−½, ½), and A = Im ū / Im τ = β. The kernel is

  K_s(z) = e^{2πiAz} θ_s(z + ū) θ₁′(0) / (θ_s(ū) θ₁(z)),

and c_s = lim_{ε→0} [∫_{cell ∖ B_ε(0)} |K_s|² dA + 2π ln ε]. Write τ = x + iy, Q = e^{2πiτ}, X = e^{2πiz}.

1. **The Kronecker function.** F(z, w) = θ₁′(0) θ₁(z + w) / (θ₁(z) θ₁(w)) = −2πi Σ_{n∈ℤ} X^n / (1 − W Q^n), with
   W = e^{2πiw}, for 0 < Im z < Im τ and w off the lattice.
   - Both sides have the same multipliers (1 under z → z + 1, e^{−2πiw} under z → z + τ).
   - Both have the same simple pole at z = 0 with residue 1.
   - Both have the same poles in w.
   - The leading terms as Q → 0 agree: −2πi[1/(1 − W) + X/(1 − X)] = π cot πz + π cot πw.
2. **Each kernel is a twisted Kronecker function.** θ₂(z) = θ₁(z + ½), θ₄(z) = −i e^{iπz} e^{iπτ/4} θ₁(z + τ/2) and
   θ₃(z) = θ₄(z + ½). So K_s(z) = e^{2πiλ_s z} F(z, w_s), with:

| s | w_s | σ_s | λ_s = A + σ_s/2 |
| --- | --- | --- | --- |
| 1 | ū | 0 | A |
| 2 | ū + ½ | 0 | A |
| 3 | ū + ½ + τ/2 | 1 | A + ½ |
| 4 | ū + τ/2 | 1 | A + ½ |

   In every case λ_s y = Im w_s, so the pole at z = τ also has residue of modulus 1.
3. **Parseval.** Take the fundamental domain {0 ≤ Re z < 1, 0 ≤ Im z < y}. At height t, for 0 < t < y,
   ∫₀¹ |K_s|² d(Re z) = 4π² e^{−4πλt} Σ_n e^{−4πnt} / |1 − W Q^n|². All frequencies share the shift λ, so no cross
   terms survive.
4. **The regularisation.** Excising strips t < δ and t > y − δ in place of discs changes the regularised integral by
   2π ln 2. Each corner holds half a pole: ∫_{t>δ, |z|<T} |z|^{−2} = π ln(T/δ) − π ln 2. Integrate each term in t.
   Rewrite the upper-limit terms with n = −m, using |1 − W Q^{−m}|² = |W|² |Q|^{−2m} |1 − W^{−1} Q^m|² and
   λy = Im w. Then use Σ_{k≥0} e^{−εk}/(k + μ) = −ln ε − ψ(μ) − γ + o(1).
5. **The result (the closed series).** For λ ∉ ℤ, let λ₊ = λ − ⌊λ⌋ and λ₋ = 1 − λ₊. Then

  c_s = −2π ln 2π − 2πγ − π[ψ(λ₊) + ψ(λ₋)] + π(S₊ + S₋),

  with
  - S₊ = Σ_{n+λ>0} (|1 − WQ^n|^{−2} − 1)/(n + λ) + Σ_{n+λ<0} |1 − WQ^n|^{−2}/(n + λ);
  - S₋ the same with λ → −λ and W → W^{−1}.

  Both sums converge geometrically. For λ ∈ ℤ the term with n + λ = 0 is excluded from S₊ and S₋, ψ(λ±) is replaced
  by ψ(1), and 4π²y / |1 − W Q^{−λ}|² is added.
6. **The cusp limit and the first correction.** With ū's (α, β) held fixed as y → ∞, S± → 0, giving
   - c^∞ = −2π ln 2π − 2πγ − π[ψ(λ₊) + ψ(1 − λ₊)];
   - c − c^∞ = 2π[Re(W Q^{n₀})/λ₊ + Re(W^{−1} Q^{m₀})/λ₋] + O(e^{−4πy min(λ₊, λ₋)}), where n₀ and m₀ are the least
     integers with n₀ + λ > 0 and m₀ − λ > 0.
   - The first correction is of size e^{−2πy min(λ₊, λ₋)}, and it carries Re τ through the phases.
7. **The untwisted check.** For ū = 0 and s = 2, 3, 4 the series must equal W87's closed form
   −2π ln((π/2)|θ_s(0)|²) exactly. For s = 2, λ = 0 and W = −1, which gives π²y − 2π ln 2π plus exponentially
   small terms, as W87's θ₂ form does.

## The computation (fixed now)

- **Precision.** mpmath at 40 digits for the series and the identities. W89's `norm`, unchanged, is the quadrature
  route.
- **The grid for N2–N4.**
  - All four s.
  - The three sectors' ū = (q_L + q_R)w, which is ±3w in every sector, so one ū per line and sign.
  - w = aτ + b on 20 lines: the ten slope-2/5 lines (2/5, k/10) and the ten (2/11, k/11), k ≠ 9.
  - x ∈ {1/8, 3/8}.
  - y ∈ {2, 4, 6} for N2; y ∈ {4, 6, 8, 12, 16, 24} for N3.
  - Points where θ_s(ū) vanishes or the record's residue cut applies are skipped and counted.
- **N0 and N1.** 200 random points each, seeded: z with 0 < Im z < Im τ, w and ū off the lattice, Im τ ∈ [0.8, 6].

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| N0 | **The expansion.** F(z, w) = −2πi Σ_n X^n/(1 − WQ^n) at all 200 points, to 10⁻²⁵ | 97% |
| N1 | **The kernels.** K_s(z) = e^{2πiλ_s z} F(z, w_s) with the table above, all four s, at all 200 points, to 10⁻²⁵ | 90% |
| N2 | **Two routes.** The closed series and W89's quadrature agree within 10⁻⁷ at every grid point with y ≤ 6 | 85% |
| N3 | **The first correction.** After subtracting c^∞ and the leading correction of step 6, the remainder is at most 10·max(e^{−4πyλ₊}/λ₊, e^{−4πyλ₋}/λ₋) at every N3 point | 80% |
| N4 | **W87's closed form.** For ū = 0 and s = 2, 3, 4 at y ∈ {1, 2, 4, 8} and x ∈ {0, 1/8, 3/8}, the series equals −2π ln((π/2)|θ_s(0)|²) to 10⁻²⁵ | 90% |
| R | **Read-outs** (no predictions): per grid point, c from both routes, their difference, c^∞, λ±, the leading correction; the largest quadrature error by y and by min(λ±); the time per norm on each route | — |

## What the outcomes mean (fixed now)

- **N0, N1 and N4 hold.** The derivation is right, and the norms are exact closed series. Their cusp limit and first
  correction are explicit, which is what W178 needs.
- **N2 holds.** W89's quadrature is confirmed to 10⁻⁷ where the record used it.
- **N2 fails at some points.** The quadrature, not the series, is then the suspect, and its error is read out. A
  failure where the series disagrees with both W87 and the quadrature would mean the derivation is wrong; N4 decides
  which.
- **N3 fails.** The leading-correction formula is wrong in its form or its constant, and W178 must use the series
  itself, not its truncation.

## Weave or thread

- **neither (an instrument).** The quantity is the frame's kernel norm on the shared fibre, at every τ and every shift.
  It is a closed form for what W89 computes, not a claim about threads or about the weave's joint action.

## What stays out

- The six and their exponents (W178).
- Any data comparison.
- Every other norm on record (W87's untwisted closed form enters only as a check).

## Seen before the rule (disclosed)

- **A read-only map of W174's construction, made in scratch by an agent of this seat before this rule.** It found the
  following.
  - c^∞ depends only on β′ = ‖α_s + 3a‖, with values −0.3382, 4.4732 and −2.7273 at β′ = 0.2, 0.3 and 1/22 from W89's
    quadrature at large y.
  - A digamma formula fits those values. It is the same as step 6's c^∞ when λ₊ = ½ ± β′.
  - The corrections decay at measured rates near π(1 − 2β′) per unit y.
  - It probed the six at large y on five lines with mixed precision: convergence to (0.3, 0.8, 0.2, 0.55, 0.2, 0.55)
    on two slope-2/5 lines and to (3/8, 7/8, 1/8, 1/2, 1/8, 5/8) on (3/8, 1/2), and drift on (2/11, 5/11) and (1/6, 0)
    at y = 20.
  - These numbers bear on W178, not on this rule's cells, and are disclosed again there.
- W87's closed form for the untwisted norms (on record).
- The derivation above was done by hand. No comparison of this rule's series with the quadrature, with W87, or with
  F's definition has been run.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
