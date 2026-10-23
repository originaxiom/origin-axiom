# W143 — P-345 on this seat's W133: which zero-free Higgs lines GENESIS PF1-W admits that are led at the cusp by the non-null eigenline, both sign families computed on own code, and W133's open multiplicities (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1739** found the censuses' Higgs nearly null (h·h = η⁶/4). Under the Standard Model's reading the light up
  and down states are then nearly orthogonal, which is why the nine fail.
- **P-345 (a)** asks for a Higgs led at the cusp by ρ(T)'s non-null eigenline e_i (the θ₂-type component), which no
  Higgs on record is. It asks whether GENESIS PF1-W (the web seat's reading), H-cov or any zero-free condition admits
  one, and whether it keeps the six's hierarchy.
- **Main sealed B1740** on F₋₂ = η⁵(θ₂⁻², θ₄⁻², iθ₃⁻²) for the second question; it is running, and no expectation is
  stated here.
- **The first question is this seat's.**
  - W133 found that PF1-W, read on the families' joint coupling, keeps exactly dim h zero-free lines in each twisted
    space, three in each of the two three-generation spaces h(12, 1) and h(20, 1).
  - It identified one sign family of theta-power lines on its own code. The other sign was found by the web seat and
    proved complete by main (B1730), and is not yet computed here.
  - W133 also left open which of its unassigned multiplicities each new line carries.
- **The owner said "continue"** to this as the next step (2026-10-23).

## The objects

- **The family.** F_a = η^{3−a}(εθ₂^a, εθ₄^a, iθ₃^a), with a ≡ 2 (mod 4) and ε = i^{(a+2)/2}. So ε = −1 for a ≡ 2
  (mod 8) and ε = +1 for a ≡ 6 (mod 8). Its twist is r ≡ 2a (mod 24).
- **On the lines** l₁ = x, l₃ = y − iz, l₇ = y + iz of a vector (x, y, z), N′ = l₁(l₃² − l₇²) = −4i·xyz. That is the
  same for both signs, so tF_a solves W133's system exactly when 2^{a+2}t³ = 1, as W133's post hoc found for ε = −1.
- **W133's four spaces** h(r, n) and their Gröbner systems, from its committed code (`the_zero_free_higgs.py`,
  `…posthoc.py`, `…posthoc3.py`): exact membership by coordinates, and the multiplicity of each solution line by its
  characteristic polynomial's squarefree factors.
- **The leading behaviour at the cusp.** In x = q^{1/8}, each component's valuation and leading coefficient: θ₂^a
  starts at x^a, and θ₃^a, θ₄^a at x⁰. A Higgs is led by the non-null eigenline when its least-valuation part is
  proportional to e₁ = (1, 0, 0), whose square is 1. It is led by a null line when that part is (0, ε, i), whose square
  is ε² − 1 = 0.
- **The range:** a ∈ [−30, 42], as W133's post hoc.

## Weave or thread

**WEAVE-type, as W133:** the weave's own surface, every allowed twist, end data n ∈ {0, 1}, the moves' joint
representation, and claims about every zero-free section at once.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| H1 | **Membership, both signs, exact.** The F_a in each space are exactly: h(4, 0) {2}; h(4, 1) {2, 26, −10, 14}; h(12, 1) {−6, 18, 6}; h(20, 1) {10, −2, 22}. Each member's cube-root multiple solves W133's system, and each space's count equals its number of lines (1, 4, 3, 3), so the family is every zero-free line, as B1730 proved | 90% |
| H2 | **W133's open multiplicities.** In h(12, 1), F₆ carries 4. In h(4, 1), F₋₁₀ and F₁₄ carry 6 and 8 between them. In h(20, 1), F₋₂ and F₂₂ carry 1 and 4 between them. Which way round is a read-out | 85% |
| H3 | **The leading behaviour, exact.** Every member with a < 0 is led at the cusp by the θ₂ component alone: the non-null eigenline. Every member with a > 0 is led by (0, ε, i): null. So the non-null-led lines are F₋₁₀ in h(4, 1), F₋₆ in h(12, 1) and F₋₂ in h(20, 1): exactly one in each three-generation space | 95% |
| H4 | a read-out: W127's index in each space (from W133's committed record), and B1740's F₋₂ identified with the h(20, 1) member a = −2, ε = +1 | — |

## What the outcomes mean (fixed now)

- **H1 and H3 hold.** P-345 (a)'s first question is answered yes, on this seat's own code. GENESIS PF1-W, the web
  seat's reading read on the families' joint coupling, admits exactly one Higgs line led by the non-null eigenline in
  each three-generation twisted space: F₋₆ (r = 12) and F₋₂ (r = 20).
  - B1740 tests F₋₂.
  - F₋₆ is the other PF1-W candidate, and nothing on record tests it.
  - Whether either keeps the six's hierarchy is B1740's question, and a sibling test's for F₋₆. That is proposed to
    main, with no expectation stated here.
  - PF1-W does not choose between the two twists or among the three lines of a space, as W133 found. "Led by the
    non-null eigenline" is P-345's added condition, not PF1-W's.
- **H2 holds.** W133's open item is closed: every multiplicity has its line.
- **H1 fails:** the membership differs from what the web seat and main recorded. The difference is the finding,
  diagnosed before anything else is said.
- **H3 fails:** some member's leading part is neither e₁ nor (0, ε, i). It is recorded as found.

## What stays out

- Data and the hierarchy, which are B1740's. Couplings not diagonal in the parity basis. End data n ≥ 2. H-cov.

## Seen before the rule (disclosed)

- **Read:**
  - W133's NOTE section with its dated correction;
  - W133's post-hoc code (`theta_power_lines`, `coords`, `mult_matrix`) and its posthoc3 JSON (the ε = −1
    multiplicities);
  - B1740's seal message;
  - P-345;
  - B1739's commit message.
- **By hand:**
  - N′ = −4i·xyz for both signs, so the same scaling;
  - the leading exponents (a for θ₂^a, 0 for θ₃^a and θ₄^a);
  - the null and non-null squares;
  - the expected members, from W133's record and its correction;
  - the multiplicities by elimination.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
