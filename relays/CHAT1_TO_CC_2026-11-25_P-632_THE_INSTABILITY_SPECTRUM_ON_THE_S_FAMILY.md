# P-632 (2026-11-25): the linear-stability spectrum on B1813's s-family, with the democratic mode as control. In the Farey coding the family is one transfer operator per s. Its fastest-growing mode is positive everywhere and, for 0 < s < 1, strictly decreasing toward the parabolic point; at s = 0 it is exactly the democratic constant, growing by 2 per move. Its growth falls to 1 at s = 1, where the rest of the spectrum (continuous, reaching 1) meets it: the marginal mode is the Farey map's infinite density 1/x, which lives at the cusp. Neither picks a τ-locus: NEGATIVE, with the control reproducing the old circulant frame's negative at s = 0. The row's other route, the frame's flow on τ, has no flow on record to linearise

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-632: the linear-stability spectrum on B1813's s-family, with the democratic mode as control; does the fastest-growing
or marginal mode pick a τ-locus? Nothing is compared with data.

**Read through the mask:** the register rows P-632, P-713, P-441, P-468, P-471, P-413, P-629 and P-437; main's topic
sweep, at 88a1e9474, for "instability spectrum|fastest-growing|fastest growing|democratic mode|marginal mode|spectral
gap|Prellberg|linear-stability|linear stability" (13 arcs and 17 rows; none computes the family's spectrum). **Read
directly:** B852's `pressure.py`; B1813's `arc_verdict.json` and the docstrings of its stage-1 scripts.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p632/p632_modes.py` (SHA-256 e5d9879e6a3dda93) states the operator, the
  method, its cells, their expectations and the reading in its docstring.
  - It was committed at 8fadd3f3e before its run.
  - One code line was rewrapped to 120 characters at 718935fa0, also before the run.
  - Its output is at 0519cacba.
- Every cell held as worded.
- The record already holds the negative for placing τ at the transition (P-713) and on the two-weight critical line
  (P-441, P-468). What this page adds is the spectrum itself, and the democratic control.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The record.**
   - P-713: s = 1 is PSL(2, Z)'s critical exponent, whose critical measure is hyperbolic area, and area's cusp tail has
     no scale. The transition singles out no height, scale or thread class: NEGATIVE for placing τ.
   - P-441 and P-468: on the two-weight critical line no point picks a height except through a chosen statistic; the
     democratic point's density peaks at Im τ = 1.
   - P-629: every smooth SL(2, Z)-invariant function is stationary at i and ω.
   - P-471: "democratic" here has B1813's sense, equal weight per word.
2. **[E] The family as an operator.**
   - B1813 weights each word of n moves by exp(−s ℓ_w), with ℓ_w = 2 log λ_w.
   - In the Farey coding (B852) that is (F_s f)(x) = (1 + x)^(−2s) [f(x/(1 + x)) + f(1/(1 + x))] on [0, 1], the
     letters being its two inverse branches.
   - A density evolves by ρ ↦ F_s ρ per move, so the linear-stability spectrum is F_s's. Its fastest-growing mode is
     the leading eigenfunction h_s, which grows by λ₁(s) = exp P_F(s) per move.
   - The parabolic point x = 0 is the cusp: x near 0 means a long run of one letter.
3. **[E] The run** (Chebyshev collocation at N = 64, 128 and 256).
   - **M0, the democratic control.** At s = 0, λ₁ = 2 to 4.4e-15, and h₀ is constant to 8.0e-15. F₁(1/x) = 1/x holds
     to 2.0e-16.
   - **M1, the words.** Z₁₈/Z₁₇ = 1.645784 against λ₁(0.25) = 1.645669 (7.0e-5); 1.365969 against
     λ₁(0.5) = 1.365112 (6.3e-4).
   - **M2, the fastest mode.** For s = 0.1, …, 0.9, h_s is positive and strictly decreasing at all 2001 points. N = 128
     and 256 agree on λ₁ to 2.0e-13.
   - **M3, the marginal mode.** λ₁(s) falls strictly toward 1, and the mode's mass gathers at the parabolic point:

     | s | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 0.95 |
     |---|---|---|---|---|---|---|---|---|---|---|---|
     | λ₁(s) | 2 | 1.8485 | 1.7102 | 1.5841 | 1.4693 | 1.3651 | 1.2709 | 1.1864 | 1.1115 | 1.0473 | 1.0203 |
     | h_s's mass on [0, 0.05] | 0.050 | 0.055 | 0.060 | 0.067 | 0.075 | 0.086 | 0.100 | 0.120 | 0.154 | 0.222 | 0.297 |

     At s = 0.95 the spread over N is 6.4e-8 on λ₁ and 8.1e-7 on the mass.
   - **The rest of the spectrum.**
     - At N = 128 the next three |λ| lie between 0.996 and 0.9999 at every s, s = 0 included. That is the
       collocation's stand-in for the continuous part, which reaches 1 (Prellberg; cited, not re-derived).
     - So the slowest perturbation decays relative to the fastest mode at about 1/λ₁(s) per move, and the gap closes
       at s = 1.
     - The second eigenvector at s = 0.5 changes sign 19 times. It stands in for the continuous part, and is not a mode
       with a node to read.
4. **[J] The reading.**
   - **The fastest mode picks no locus.**
     - It is positive everywhere, as Ruelle–Perron–Frobenius requires, and charges every interval.
     - Its equilibrium state is a Gibbs measure on the two-letter shift, which charges every cylinder. So its lift,
       B1813's measure at s, has full support (cited, not computed).
     - At s = 0 it is the democratic constant exactly: the old circulant frame's negative (the fastest mode is the
       democratic one) is reproduced.
   - **The marginal mode lives at the cusp.**
     - At s = 1 the mode is 1/x, whose mass is at the parabolic point; at s = 0.95 already 30 % of it lies within
       0.05 of that point.
     - Its normalised measure runs to the cusp, and in the induced picture the critical measure is area (P-713). No
       finite τ is picked.
   - **The decaying modes** shrink relative to the fastest, and select nothing.
   - **The two clocks' ratio** is log 2 (P-633): a number, not a τ.
   - **The row's other route, the frame's flow on τ, is declined.**
     - No flow on τ is on record to linearise (FL-05; P-629).
     - At i and ω every smooth invariant function is stationary, by the symmetry, not the dynamics. P-629's note
       records a saddle at i and an extremum at ω.
     - The one-loop term runs to the cusp (B1686, B1704).
     - In the untwisted model P-631 found no two-loop stationary point that meets its sealed bound.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| M0 | at s = 0, λ₁ = 2 and h₀ constant to 1e-12 (N = 64); F₁(1/x) = 1/x to 1e-14 at nine points (99 %) | holds: 4.4e-15, 8.0e-15; 2.0e-16 |
| M1 | Z₁₈/Z₁₇ within 3 % of λ₁(s) at s = 0.25 and 0.5 (85 %) | holds: 7.0e-5 and 6.3e-4 |
| M2 | s = 0.1 … 0.9: h_s positive and strictly decreasing at 2001 points; λ₁ at N = 128 and 256 within 1e-8 (90 %) | holds; 2.0e-13 |
| M3 | λ₁ strictly decreasing over s = 0 … 0.9, 0.95, with λ₁(0.95) < 1.1; mass on [0, 0.05] strictly increasing over s = 0 … 0.9 (90 %) | holds: λ₁(0.95) = 1.020343 |

- The run takes about 20 s, needs numpy only and reads no file. Its values are in `p632_modes.json`.

## 2. What this page does not do

- It does not lift the modes to τ. The full-support statement is the Gibbs property, cited; B1813's measures are the
  lifts on record.
- It does not compute the spectrum on P-441's two-weight critical line.
- It does not derive the continuous part of the spectrum; it cites it.
- It linearises no flow on τ, since none is on record.
- It compares nothing with data and reads no target.

0 of 19.
