# W171 — W73 per sector at N = 10, the counted line's order, in the weave reading: does any sector's surface Yukawa survive the stabiliser of the lines of order 10, in either reading of the twist? (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's list** (relays §304 and §312): W73 per sector at N = 10, the order of the counted line (2/5, ½).
  - W73 left one route to values in the surface frame: give the sectors different couplings, fixed before any data
    (W73, "What would make it a test").
  - It was parked on a choice of the line's order N (relay §115). Stage 2 (W167) counted the line, so N = 10.
- **Both readings' pieces exist** (the owner's ruling, relay §133):
  - the minimal reading: W91's twisted coupling vector V_s with W72's untwisted units;
  - the per-field reading: W92's dressed units, each field's units carrying its own charge, with R neutral.
- **Both closure laws are on record**, each checked at N = 9, 11 and 12 and never at 10:
  - the minimal reading's (chat1's law; W91, post hoc 2, with ψ = (a/N, −b/N) and the factor (Cτ + D)^{−½}):
    V_s returns around a line's stabiliser with exp(−2πi c (q_L² + q_R²)/N);
  - the per-field reading's (W92, post hoc; relay §133's correction): the Yukawa integrands return with
    exp(2πi ε c (q_L² + q_R² − q_H²)/N).
  - Here c = ⟨w, wγ⟩/N mod N for a line w (integers mod N) and an element γ with wγ ≡ εw, ε = ±1.

## The question, and the weave reading

- In the surface frame τ is integrated over. A line w of exact order N is kept by its stabiliser Γ_w ⊂ SL(2, ℤ), up
  to sign. Each sector's Yukawa integrand returns around γ ∈ Γ_w with a phase χ_s(γ), its closure character.
- **The weave reading** (the 2026-10-15 design's choice 2(a)): all 72 lines of order 10 together, the coupling made
  covariant under every move. Its pairing with the untwisted units and the Higgs's surface mode is the integral of
  the integrand's χ_s-invariant part.
  - If χ_s is not trivial on Γ_w, that part is zero. Change variables by γ on the cover where the integrand is single
    valued: the integral Y obeys Y = χ_s(γ) Y.
  - So **a sector's surface Yukawa is zero unless its character is trivial on the stabiliser**: a selection rule of
    the frame's own moves.
- **One line on its own curve** (a thread reading) gives the same zero. Its integrand is single valued only on the
  cover where χ_s is trivial, and the deck group's phases sum to zero. Here thread and weave agree.
- **By hand (reasoning, not computation; disclosed below).**
  - T¹⁰ fixes every line of order 10, with c = a² for the line (a, b). Conjugating it carries c = 1 to every line.
  - The sums are q_L² + q_R² = 17, 5 and 45 (minimal), and q_L² + q_R² − q_H² = 8, −4 and 36 (per field), for up,
    down and leptons. None is divisible by 10.
  - So every sector's character is non-trivial in both readings, and **the prediction is that every sector's surface
    Yukawa vanishes at N = 10, in both readings.**

## The computation (fixed now)

- **The lines.** The 36 lines of exact order 10 up to sign, in W91's integer convention (a, b) with w = (aτ + b)/10,
  ψ = (a/10, −b/10). chat1's convention, used by W92's code, is (l_a, l_b) = (b, a). The counted line, B1656's
  w = (2/5)τ + ½, is (4, 5).
- **The stabilising elements, per line:**
  - the conjugate g⁻¹T¹⁰g, with g ∈ SL(2, ℤ) whose first row is ≡ (a, b) mod 10 (exact; c computed, not assumed);
  - and, for the numerical cells, the element with least |C| among every SL(2, ℤ) matrix with entries in [−30, 30]
    that keeps the line up to sign with c prime to 10 (ties by least Σ|entries|, then lexicographic).
- **The objects.**
  - W91's generator, evaluated in factored form with exact exponents and phases. It is branch-free.
  - W92's dressed units and integrands, on W72's units, with the neutral R from analytic theta sums (W92's post hoc
    fix for mpmath's θ₂ nome branch).
  - The Standard Model's 6Y charges: Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3.
  - The minimal reading's pairs are (k_u, k_d) = (q_L + q_R, q_L − q_R) = (−3, 5), (3, −1) and (3, −9).
  - The reference pair (2, 4) has q_L² + q_R² = 10 ≡ 0, so its character is trivial. It reads the identity channel's
    untwisted multiplier, which W91's untwisted limit cannot (V₁ ≡ 0 there).

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **The instrument.** W91's generator against direct theta evaluation at six order-10 lines and three τ (\|Re τ\| < 1), all four channels and three sectors, to 10⁻⁴⁰. W92's dressing series against direct evaluation at N = 10, every charge the sectors use, three lines, two points, to 10⁻⁴⁰ | 95% |
| K1 | **The stabilisers, exact.** On all 36 lines, g⁻¹T¹⁰g keeps the line with c ≡ ±1 mod 10. So for every sector and both readings ε c Q ≢ 0 mod 10: no character is trivial. The [−30, 30] search finds an element with c prime to 10 on every line | 95% |
| K2 | **The minimal reading's law at N = 10, numerically.** On T¹⁰ at the 20 lines with a prime to 10, and on the searched element at the other 16 (the counted line among them), for all three sectors at two τ: the triplet's cycle products equal exp(−2πi c (q_L² + q_R²)/10)^{length} (W91 post hoc 2's method), and the identity channel's ratio to the reference equals exp(−2πi c (q_L² + q_R²)/10); τ-independent; to 10⁻³⁰. None equals 1 | 80% |
| K3 | **The per-field reading's law at N = 10, numerically.** W92's integrands on T¹⁰ at the 20 lines with a prime to 10 (τ = 0.1 + 1.1i), and on the first three threads L Rⁿ that fix lines of order 10 (W92's V3 points): the Y integrands return with exp(2πi ε c (q_L² + q_R² − q_H²)/10), and the K norms are closed, to 10⁻²⁵. Where c is prime to 10, none equals 1 | 80% |
| K4 | **The selection rule's consequence (decisive).** At the line (1, 0), the sum over j = 0..9 of each sector's integrands at τ + 10j vanishes, below 10⁻²⁵ of Σ_j \|·\|. This holds for W92's Y integrands (per field), and for each channel of V_s over its untwisted multiplier (minimal; the identity channel's read from the reference). The controls, all charges zero and the reference pair, give ten times the value. So **every sector's surface Yukawa at N = 10 is zero, in both readings** | 85% |
| R | **Read-outs** (no predictions). (i) The census over N = 2..16: each (N, sector, reading) survives iff its character is trivial on every line's stabiliser, with g⁻¹Tᴺg checked for c = 1 on every line of each order; the orders where all three sectors survive. (ii) The counted line's elements and characters. (iii) The measured phases' table | — |

## What the outcomes mean (fixed now)

- **K1 and K4 hold (the expected outcome).**
  - At the counted line's order the surface frame forbids every sector's Yukawa, in both readings of the twist. This
    is the frame's own selection rule, and it holds thread and weave alike.
  - **W73 per sector at N = 10 ends as an exclusion.** No normalisation (H-end) and no data are reached, because
    there is nothing to normalise. The parked arc closes.
- **K1 fails for some (sector, reading):** that pair's character is trivial at N = 10, and its surface Yukawa can be
  non-zero. It is computed under a new rule, with H-end, before any data are read.
- **K2 or K3 fails as worded, while the measured phase is still ≠ 1:** an instrument or convention slip, as in W91's U5
  and W92's V3. It is recorded, and read post hoc and labelled. The exclusion then rests on K1 and K4.
- **K4 fails:** the selection argument is wrong somewhere. It is recorded and diagnosed post hoc, and nothing is
  claimed.
- **The census** (a read-out) says which orders any sector's surface Yukawa survives at, in each reading. It is
  arithmetic on the characters, and it is not a test.

## Weave or thread

- **Weave.** The claim takes all 72 lines of order 10 at once, every sector, both readings, and the orbit under
  every move. Nothing is hand-picked.
- **Conditional on N = 10.** That is the counted line's order, and the line is a counted choice (stage 2). The census
  over N removes the condition, for survival only.
- **One line on its own curve** gives the same zero. That is a thread reading, and it is labelled so.

## What stays out

- H-end and the data, unless a sector survives (K1 fails).
- The fibre frame (B1656; W166–W170), where τ is fixed and not integrated. Nothing here touches it.
- Any regularisation or fundamental domain that is not covariant under the stabiliser. That would be a choice by
  hand, a thread choice.
- The 2026-10-15 design's naive orbit sums (one τ, each line's phase fixed by its representative). They are not
  covariant, so they are not the weave object. This rule replaces them.
- θ̄ and J. J = 0 in this frame anyway (W74).

## Looks (charter viii)

- None. No data are read.

## Pre-mortem

- **The likeliest failure is an instrument slip in K2 or K3.** W91's U5 and W92's V3 each failed as worded on a
  convention: the weight in the channel map, the line's sign, and mpmath's θ₂ nome branch. This rule uses W91 post hoc
  2's verified convention and W92 post hoc's analytic R.
- **The next likeliest is the reference trick** for the identity channel, if the reference's multiplier carries a
  factor the law does not.
- **The decisive content is χ ≠ 1.** It is exact (K1) and direct (K4), so a convention slip in K2 or K3 does not reach
  it.

## Seen before the rule (disclosed)

- **The two laws, their records and relay §133's sums** (8, −4 and 36).
- **Reasoning, not computation:**
  - that T¹⁰ keeps every line of order dividing 10 with c = a²;
  - that under T¹⁰ every channel of V_s at ψ = (1/10, 0) carries one relative phase, of modulus one;
  - the census arithmetic, that a sector survives at N iff N divides its sum (17, 5, 45 minimal; 8, −4, 36 per field).
- **Not computed:** nothing at N = 10. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- The script runs once. Its output is committed before it is read. The only checks before that are the exit, NaN,
  paths and warnings.
- Any later check is labelled post hoc.

0 of 19.
