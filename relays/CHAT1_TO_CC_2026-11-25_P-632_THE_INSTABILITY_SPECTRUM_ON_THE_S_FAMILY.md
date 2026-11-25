# P-632 (2026-11-25): the linear-stability spectrum on B1813's s-family, with the democratic mode as control. In the Farey coding the family's growth and leading mode are those of one transfer operator per s. Its fastest-growing mode is positive everywhere; at s = 0 it is exactly the democratic constant, growing by 2 per move, and for 0 < s < 1 it is strictly decreasing in x, so largest at the parabolic point (completely monotone, per the referee's argument). Its growth falls to 1 at s = 1, where the continuous part of the spectrum, [0, 1] at every s, meets it: the marginal mode is the Farey map's infinite density 1/x, which lives at the cusp. Neither picks a locus by the criterion fixed before the run, and on τ the record's lifts pick none: NEGATIVE, with the democratic control an identity. The row's other route, the frame's flow on τ, is declined: the record has potentials on τ but no dynamics for it

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-632: the linear-stability spectrum on B1813's s-family, with the democratic mode as control; does the fastest-growing
or marginal mode pick a τ-locus? Nothing is compared with data.

**Read through the mask:** the register rows P-632, P-713, P-441, P-468, P-471, P-413, P-629, P-437, P-073 and P-591;
main's topic sweep, at 88a1e9474, for "instability spectrum|fastest-growing|fastest growing|democratic mode|marginal
mode|spectral gap|Prellberg|linear-stability|linear stability" (13 arcs and 17 rows). None computes more than the
family's leading eigenvalue, which B852 computes by the same method. **Read directly:** B852's `pressure.py`; B1813's
`arc_verdict.json` and the docstrings of its stage-1 scripts.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p632/p632_modes.py` (SHA-256 e5d9879e6a3dda93) states the operator, the
  method, its cells, their expectations and the reading in its docstring.
  - It was committed at 8fadd3f3e before its run.
  - One code line was rewrapped to 120 characters at 718935fa0, also before the run.
  - Its output is at 0519cacba.
- Every cell held as worded.
- The record already holds the negative for placing τ at the transition (P-713) and on the two-weight critical line
  (P-441, P-468), and B852 holds the leading eigenvalue. This page adds the eigenfunctions, the subleading spectrum and
  the control.
- The referee read (applied here) found:
  - the direction of the monotonicity reversed in the first version's title;
  - one rounding error;
  - the Farey coding stated as word by word, with its L↔R-odd part left out;
  - Ruelle–Perron–Frobenius and Gibbs cited where the potential is not Hölder;
  - the mass reported against Lebesgue measure without saying so;
  - the decline of the flow route sourced too narrowly.
  Its own checks (the Gauss-induced λ₁, the odd part's spectrum, the equilibrium state's mass, the word sums to n = 22,
  the node dependence of the second eigenvector) are cited as the referee's and are not committed. This seat re-ran
  the odd part's spectrum and the identity h_s′(1) = −s h_s(1) on the script's own functions.
- The script's docstring calls the two inverse branches "the letters". That is the error above, and it stays in the
  sealed text.

**Typing.** [E] means established on record, by a run here, or by the referee where it says so. [J] means this seat's
judgement.

## 0. In short

1. **[E] The record.**
   - P-713: s = 1 is PSL(2, Z)'s critical exponent, whose critical measure is hyperbolic area, and area's cusp tail has
     no scale. The transition singles out no height, scale or thread class: NEGATIVE for placing τ.
   - P-441 and P-468: on the two-weight critical line no point picks a height except through a chosen statistic. The
     democratic point there (β = μ, both clocks weighted equally) has its density peak at Im τ = 1.
   - P-629: every smooth SL(2, Z)-invariant function is stationary at i and ω.
   - P-471: "democratic" here has B1813's sense, equal weight per word.
2. **[E] The family as an operator.**
   - B1813 weights each thread (a primitive necklace of n moves) by ℓ_w exp(−s ℓ_w), with ℓ_w = 2 log λ_w. The word
     sums over all 2ⁿ − 2 words with both letters have the same growth rate.
   - Word by word, that is the operator (L_s f)(x) = (1 + x)^(−2s) f(x/(1 + x)) + f(x + 1) on (0, ∞). Its branches
     x/(1 + x) and x + 1 are the letters, with multiplier λ_w² per word.
   - L_s commutes with (Jf)(x) = x^(−2s) f(1/x). On J-even functions it restricts to the Farey operator on [0, 1],
     (F_s f)(x) = (1 + x)^(−2s) [f(x/(1 + x)) + f(1/(1 + x))] (B852's). On J-odd functions it restricts to
     (F_s⁻ f)(x) = (1 + x)^(−2s) [f(x/(1 + x)) − f(1/(1 + x))].
   - A density evolves by ρ ↦ L_s ρ per move, so the linear-stability spectrum is that of F_s and F_s⁻ together. The
     fastest-growing mode is F_s's leading eigenfunction h_s, which grows by λ₁(s) = exp P_F(s) per move.
   - The parabolic point x = 0 is the cusp: x near 0 means a long run of one letter.
3. **[E] The run** (Chebyshev collocation at N = 64, 128 and 256).
   - **M0, the democratic control.** At s = 0, λ₁ = 2 to 4.4e-15, and h₀ is constant to 8.0e-15. That is an identity,
     F₀1 = 2, and it controls the instrument. F₁(1/x) = 1/x holds to 2.0e-16.
   - **M1, the words.** Z₁₈/Z₁₇ = 1.645784 against λ₁(0.25) = 1.645669 (7.0e-5); 1.365969 against λ₁(0.5) = 1.365112
     (6.3e-4). Per the referee, Z₂₂/Z₂₁ is within 9.0e-6 and 1.7e-4.
   - **M2, the fastest mode.** For s = 0.1, …, 0.9, h_s is positive and strictly decreasing in x at all 2001 points.
     N = 128 and 256 agree on λ₁ to 2.0e-13. Per the referee, λ₁ by inducing on the Gauss map agrees to 3e-15 for
     s ≤ 0.7, and to 7e-11 at s = 0.95.
   - **[E, the referee's argument] For every 0 < s < 1, h_s is completely monotone on (0, 1]**, hence positive,
     strictly decreasing and convex.
     - L_s keeps complete monotonicity: x/(1 + x) is a Bernstein function, and multiplying by (1 + x)^(−2s) or shifting
       by one keeps the class.
     - f₀ = (1 + x)^(−2s) is J-even and completely monotone, and L_sⁿ f₀/λ₁ⁿ tends pointwise to cH, with c > 0 and
       H = h_s on [0, 1]. Pointwise limits keep the class.
     - H(x) = x^(−2s) h_s(1/x) tends to 0 as x → ∞, so H is not constant.
     - J-evenness also gives h_s′(1) = −s h_s(1). This seat checked that identity on the run's h_s: −0.300000,
       −0.500000 and −0.800001 at s = 0.3, 0.5 and 0.8.
   - **M3, the marginal mode.** λ₁(s) falls strictly toward 1, and the mode gathers at the parabolic point:

     | s | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 0.95 |
     |---|---|---|---|---|---|---|---|---|---|---|---|
     | λ₁(s) | 2 | 1.8485 | 1.7102 | 1.5841 | 1.4693 | 1.3651 | 1.2709 | 1.1864 | 1.1115 | 1.0473 | 1.0203 |
     | ∫₀^0.05 h_s dx / ∫₀¹ h_s dx (Lebesgue) | 0.050 | 0.055 | 0.060 | 0.067 | 0.075 | 0.086 | 0.100 | 0.120 | 0.154 | 0.221 | 0.297 |
     | the equilibrium state μ_s = h_s ν_s on [0, 0.05] (the referee's) | 1.9e-6 | | | | | 5.5e-4 | | 5.5e-3 | 0.0185 | 0.0692 | 0.151 |

     - At s = 0.95 the spread over N is 6.4e-8 on λ₁ and 8.1e-7 on the Lebesgue fraction.
     - For s ≠ 1, h_s is a density for the conformal measure ν_s, not for dx. So the Lebesgue row is the mass of no
       measure in the family, and the equilibrium state's row is the one that measures where the mode lives.
     - The referee's quadrature gives ν₀[0, 1/20] = 2⁻¹⁹ exactly and ν₁[0, 1/20] = 0.05000. Its run toward the
       cusp is steeper than the Lebesgue row's.
   - **The rest of the spectrum.**
     - The continuous part is [0, 1] at every s. It is the parabolic branch's alone, on Prellberg's Hilbert space of
       generalised Borel transforms, where the operator is self-adjoint (T. Prellberg, J. Phys. A 36, 2455, 2003;
       cited, not re-derived).
     - For s < 1 there is a simple leading eigenvalue λ₁ > 1 besides the continuous part, plus isolated eigenvalues;
       at s = 1/2, λ₁ is the only non-zero one. At s = 1, 1/x lies outside the space.
     - At N = 128 the next three |λ| of F_s lie between 0.996 and 1 (at most 0.99994) at every s, s = 0 included: the
       collocation's stand-in for the continuous part.
     - F_s⁻ has no eigenvalue above 1. Its largest |λ| is 0.99993 to 0.99999 at N = 128 to 256 for s = 0 to 0.95, per
       the referee; this seat's rerun gives 0.999751 to 0.999997 at N = 64 and 128 for s = 0, 0.5 and 0.9.
     - So the slowest perturbation decays relative to the fastest mode at about 1/λ₁(s) per move, and the gap closes
       at s = 1.
     - The second eigenvector of F_s at s = 0.5 changes sign 19 times at N = 128; per the referee, it changes 3, 21, 5
       and 13 times at N = 64, 96, 192 and 256. It stands in for the continuous part, and is not a mode with a node to
       read.
4. **[J] The reading.**
   - **The fastest mode picks no locus.**
     - It is positive everywhere and charges every interval: by quasi-compactness on functions of bounded variation
       (Hofbauer–Keller; the essential radius is at most 1 < λ₁), or by the complete monotonicity above.
     - Its equilibrium state h_s ν_s is weak Gibbs in Yuri's sense, not Gibbs: the potential's variation on cylinders
       of length n falls like 2s/n, which is not summable. By conformality it charges every cylinder.
     - That its lift is the n → ∞ limit of B1813's measure at s is [J], not computed.
     - At s = 0 it is the democratic constant exactly, so the old circulant frame's negative (the fastest mode is the
       democratic one) is reproduced, as an identity.
   - **The marginal mode lives at the cusp.**
     - At s = 1 the mode is 1/x, whose mass is at the parabolic point.
     - At s = 0.95 already 30 % of its Lebesgue mass, and 15 % of its equilibrium state, lies within 0.05 of that
       point.
     - Its normalised measure runs to the cusp, and in the induced picture the critical measure is area (P-713).
     - The neutral part of the spectrum comes from the parabolic branch alone at every s (Prellberg). So the
       marginal perturbations live at the cusp at every s, not only at s = 1.
   - **Neither picks a locus by the criterion fixed before the run** (an interior extremum of h_s). On τ, the record's
     lifts pick none (P-713, P-441, P-468).
   - **The decaying modes** shrink relative to the fastest, and select nothing.
   - **The two clocks' ratio** is log 2 (this seat's P-633 page, 2026-11-25): a number, not a τ.
   - **The row's other route, the frame's flow on τ, is declined.**
     - No dynamics for τ is on record (P-073, under P-629). The record's functions of τ are one-loop potentials
       (B1684, B1686, B1704, B1823), whose gradient flow would need a time the record does not give.
     - P-591 notes that FL-05's no-action wording overstates (B1684, B1791, B1823).
     - Every smooth SL(2, Z)-invariant function is stationary at i and ω, by the symmetry, not the dynamics; P-629's
       note records a saddle at i and an extremum at ω. The record's potential keeps only the theta group, and is not
       stationary at ω (B1686).
     - The one-loop term runs to the cusp (B1686, B1704). With added trivial-fermion contents B1704 puts the minima on
       the unit arc between i and ω + 1, by a chosen content.
     - In the untwisted model, this seat's P-631 page found no two-loop stationary point that meets its sealed bound.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| M0 | at s = 0, λ₁ = 2 and h₀ constant to 1e-12 (N = 64); F₁(1/x) = 1/x to 1e-14 at nine points (99 %) | holds: 4.4e-15, 8.0e-15; 2.0e-16 |
| M1 | Z₁₈/Z₁₇ within 3 % of λ₁(s) at s = 0.25 and 0.5 (85 %) | holds: 7.0e-5 and 6.3e-4 |
| M2 | s = 0.1 … 0.9: h_s positive and strictly decreasing at 2001 points; λ₁ at N = 128 and 256 within 1e-8 (90 %) | holds; 2.0e-13 |
| M3 | λ₁ strictly decreasing over s = 0 … 0.9, 0.95, with λ₁(0.95) < 1.1; mass on [0, 0.05] strictly increasing over s = 0 … 0.9 (90 %) | holds: λ₁(0.95) = 1.020343 |

- The run takes about 20 s, needs numpy only and reads no file. Its values are in `p632_modes.json`. M3's "mass" is the
  Lebesgue fraction (§ 0 item 3).

## 2. What this page does not do

- It does not lift the modes to τ. B1813's measures are the lifts on record.
- It does not compute the spectrum on P-441's two-weight critical line.
- It does not derive the continuous part of the spectrum, the quasi-compactness or the weak Gibbs property; it cites
  them.
- It linearises no flow on τ, since no dynamics for τ is on record.
- It compares nothing with data and reads no target.

0 of 19.
