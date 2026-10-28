# W175 — THE RIDDLE's horn 1 off the mirror: the frame's own potential on the mirror-free line classes (the web seat's question 1). Where it holds Re τ, how firmly, which way it pushes the height, and how large J is there (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The web seat's relay of 2026-10-28** ("THE CLASS AND THE END", 422cd8ecd; this seat's relay §322).
  - Above Im τ = 1, a slope-2/5 line's T-orbit class meets a mirror-fixed point only if the line's order divides 10.
  - So W172's CP conservation at the counted line, an order-10 class, is the case where the class offers a
    CP-conserving state and the potential's single harmonic picks it.
  - On the mirror-free classes no such state exists in the band. Its question 1 to this seat is W172 on such a class.
- **For THE RIDDLE this is horn 1's escape route.** "What would break the riddle" (NOTE) names a forced selection off
  the CP-fixed loci.
  - On a mirror-free class the frame's own potential must put its X-minimum at a CP-violating state, since none other
    exists there.
  - The class is a counted choice, of horn 3's kind. Given the class, though, J at the potential's own minimum would be
    a number the frame fixes.
  - The mirror maps each class to its partner, so a mirror pair of classes holds a CP-conjugate pair of minima. Taken
    with its partner, the minimum is an orbit of two, the case the spontaneous-breaking clause admits.

## The class criterion (by hand; checked in C0)

- A potential moves a configuration along its line's T-orbit: (τ + 1, a, b) ~ (τ, a, b + a). With a = 2/5 the orbit is
  labelled by b mod 1/5, and the orbit coordinate X = Re τ runs over [0, 5) (W169).
- The mirror sends (τ, a, b) to (−τ̄, a, −b) (W172's lemma, in main's line convention). A point of the class is fixed
  when −X = X + k and −b ≡ b − 2k/5 mod 1 for some integer k. That needs b ≡ k/5 mod ½, which has a solution exactly
  when b ∈ (1/10)ℤ, that is, when the order lcm(5, denominator of b) divides 10.
- Above Im τ = 1 the only mirror lines are Re τ ∈ ½ℤ. Below it the extended group's other reflections enter, and the
  criterion does not cover them.

## The computation (fixed now)

- **The classes.** Slope 2/5, by b mod 1/5:
  - **the mirror-free classes of orders 15, 20, 25 and 30:** b = 1/15, 2/15 (15); 1/20, 3/20 (20); 1/25, 2/25, 3/25,
    4/25 (25); 1/30, 1/6 (30). That is ten classes in five mirror pairs: (1/15, 2/15), (1/20, 3/20), (1/25, 4/25),
    (2/25, 3/25) and (1/30, 1/6);
  - **the controls with a mirror point:** b = 1/10 (order 10, the counted class) and b = 0 (order 5).
- **The potential.** W172's kernel and content: W59's joint-parity kernel at s = 3, N = 48, W67's fields with the
  bosons' weight 1, ψ = (−a, b) for the class's representative line.
- **The heights.** Im τ = 1.5, 2.0, 2.5, 3.0 and 3.5.
- **The X-minimum** at each class and height: a grid of 1000 points on [0, 5), then a bounded refinement (W172's
  method). The X-amplitude, the X-curvature against the y-curvature, and ∂V/∂y at the minimum.
- **J at the minimum.** The frame's own point (`own_point`, B1726's instrument as this seat rebuilt it: L_max, readings
  (S̃, S)) at the class's representative line, Re τ = X*, at the height.
  - **A consistency check:** the same configuration read as the line b + 2j/5 at Re τ = X* − j, with j = ⌊X*⌋.
- **The mirror pairs.** Each pair's two X-profiles are compared, reflected (X ↦ c − X with the best c on the grid).
  J's sign is compared at the paired minima.
- **The two-dimensional read-out.** At each class, the least V over X ∈ [0, 5) and Im τ ∈ [1.2, 4], by a 200 × 57 grid
  and a bounded refinement. Its position: in the interior, or on the lower edge.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| C0 | **The criterion.** On every slope-2/5 line of order up to 60, a mirror-fixed point exists on the T-orbit above Im τ = 1 exactly when the order divides 10 (exact arithmetic) | 97% |
| C1 | **The pairs.** Each mirror pair's X-profiles agree reflected to 10⁻⁶ relative (the kernel's truncation), at every height | 90% |
| C2 | **CP is violated at the potential's own minimum** (decisive). On every mirror-free class at every height, \|J\| at the X-minimum exceeds 10⁻⁸; on the two controls it is below 10⁻¹² | 80% |
| C3 | **Weakly held, as W172.** On every class and at every height the X-amplitude is below 10⁻³ of \|V*\| | 85% |
| C4 | **The height is pushed down, as W169.** On every class and at every height, ∂V/∂y > 0 at the X-minimum | 80% |
| R | **Read-outs** (no predictions): X* per class and height, and its distance from B1786's carriers' rows (positions only); \|J\| and its sign per class; the consistency check; the paired minima's J signs; the two-dimensional least and its position; and \|J\| at the minima against the measured J, one number, counted as a look | — |

## What the outcomes mean (fixed now)

- **C2 holds.** The frame's own one-loop potential, on a mirror-free class, holds a CP-violating state, and J there is
  fixed by the class. That is horn 1's escape, of the kind THE RIDDLE named.
  - The class is a counted choice (horn 3), and the height is not held (C4).
  - The read-out against the measured J says whether the forced J has the right size.
  - The record's first CP-violating state chosen by the frame's own dynamics rather than by hand would be on record.
- **C2 fails** (J vanishes at some mirror-free minimum): an accidental zero, named with its class and height.
- **C3 fails:** the potential holds Re τ firmly on some class. That class's X* is then a sharper prediction.
- **C4 fails:** somewhere the potential holds the height in the band, which W169 did not find at the counted line.

## Weave or thread

- A frame result on stated classes. The potential is weave-type, the classes are counted choices, and the census covers
  every mirror-free class of orders 15–30 at slope 2/5. No class is hand-picked within that set.

## What stays out

- Other slopes, orders above 30, s = 4 and other contents (W172's variations), and the region below Im τ = 1.2.
- The six's comparison at the minima. Only J's size is compared, and the look is counted.

## Seen before the rule (disclosed)

- The web seat's relay: its criterion, its J values on the class of (2/5, 23/30) at Im τ 3.03 (−1.07 × 10⁻³ to
  +5.84 × 10⁻⁴ along the orbit, with a sign change), and its order-5 and order-10 zeros.
- W169 and W172's outputs at the counted class.
- The class list above was derived by hand from the criterion.
- Not computed: no potential on any mirror-free class, and no J at any minimum.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
