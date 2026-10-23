# W140 — the hypercharge line inside E₆: which flat lines the weave allows, and which of them keep m_e = m_d in the joint frame's extended matrices, against main's frame (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W139** found that no vev of the families' 27s splits leptons from down quarks. Its reading, labelled, said only a
  flat hypercharge line that breaks SU(5)'s relation can split them, and that the joint frame and main's frame then
  need the same ingredient. That reading mixes a weave question with a thread one.
- **The owner asked (2026-10-23)** whether this seat should compute the reading, and approved two parts:
  - the weave level: which lines on the shared fibre every move allows;
  - a census of every line of order ≤ 12, put in E₆'s hypercharge direction, deciding exactly which keep d and e
    degenerate in the joint frame. That is compared with main's frame.
- **Main's B1728** proved the mechanism in its own frame. On a flat line of order N, the frame sees each field's
  charge 6Y mod N, up to swap (a transpose) and sign (the torus's involution). So d = e iff N ∣ 4 or N ∣ 5, u = d iff
  N ∣ 6, and u = e iff N ∣ 2 or N ∣ 7. The "if" direction is proved; the converse is a census.

## The objects

- **The lines.** A flat U(1) line on the shared fibre is a point y of (ℚ/ℤ)², the holonomies around the fibre's two
  cycles; its order N is its exact order. The moves L = ((1, 1), (0, 1)) and R = ((1, 0), (1, 1)) act on y, and so does
  −I = (LR⁻¹L)².
- **The threads' lines.** A line is a thread's when that thread's monodromy fixes it. B1713's set is every line of
  order ≤ 12 up to sign.
- **The line in E₆'s hypercharge direction.** A field f gets the twist 6Y(f)·y, so on a line of exact order N its twist
  is labelled by q_f = 6Y(f) mod N.
  - **Light fields:** Q 1, u^c −4, d^c 2, L −3, e^c 6, H_u 3, H_d −3.
  - **The 27's extended entries** (W139's embedding): d 1 and D −2; the two antitriplets 2 and 2; the two Y = −½
    doublets −3 and −3; h_u⁺ 3 and e^c 6; the doublets' neutral vevs ∓3; the singlets 0.
  - The singlets S and ν^c stay untwisted, so E₆'s breaking vevs are constant. Hypercharge is the only U(1) that
    commutes with the Standard Model and leaves both singlets untwisted for every N. By hand: the other two Cartan
    directions twist S or ν^c.
- **The instrument: every twist-dependent coupling.** A frame whose couplings depend on the line only through the
  fields' twists has, in place of W139's λ_{ijk}, a coupling F(ℓ₁, ℓ₂, ℓ₃) of the three fields' labels
  ℓ = (family, q mod N). F is taken:
  - totally symmetric, as W is (main's swap is its transpose);
  - in a second variant, also invariant under negating every twist (main's sign).
  An identity that holds for every such F is forced by the twist arithmetic. A coincidence that fails for random F is
  not forced. Random complex F, at 30 digits.
- **The two models.**
  - **Light fields only** (main's frame's content): the 3 × 3 matrices M_u, M_d, M_e from F(Q, u^c, H_u),
    F(Q, d^c, H_d) and F(L, e^c, H_d), with one vev vector over the families' Higgs.
  - **E₆'s extended matrices:** W139's 6 × 6 charge −1/3 and charged-lepton matrices from N's monomials, each entry
    weighted by F of its three components' labels. Light masses are taken at hierarchical vevs (singlets 10⁴).

## Weave or thread

- **C1 is WEAVE:** every move at once, on the shared fibre.
- **C2 to C4 are a census of thread objects.** Every line of order ≤ 12 is taken, under B1713's rule, with none
  hand-picked, and the claims are about all of them at once. The quantity on each line is that line's, not the joint
  action's.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| C1 | **The weave's line.** For every N ≤ 12, the only point of (ℤ/N)² fixed by both L and R is 0, with or without −I. The orbits of ⟨L, R⟩ on (ℤ/N)² are exactly the sets of points of each exact order d ∣ N | 99% |
| C2 | **The threads' lines.** The lines of order ≤ 12, up to sign, number 266, B1713's count. Each line of order N is fixed by the hyperbolic thread LᴺRᴺ (trace N² + 2) | 98% |
| C3 | **The control: main's law from twist arithmetic alone.** In the light-fields model, for N = 1 … 12: in both variants of F, d = e exactly when N ∈ {1, 2, 4, 5} and u = d when N ∈ {1, 2, 3, 6}. u = e when N ∈ {1, 2, 7} with the sign symmetry (main's law), and N ∈ {1, 2} without it, so the order-7 coincidence is the sign's. Every other pair splits | 85% |
| C4 | **The joint frame.** In E₆'s extended matrices, for N = 1 … 12 and both variants of F, the three light down and lepton masses agree exactly when N ∈ {1, 5}. At N = 2 and 4 the 27's exotics split them where main's frame does not | 80% |
| C5 | the read-out. The census in lines up to sign: 22 of 266 keep d = e in main's frame and 13 in the joint frame; the six singular values at non-hierarchical vevs | — |

"Agree exactly" means |ln| of every light-mass ratio is below 10⁻²⁰ at all five random draws. "Split" means it exceeds
10⁻⁶ at every draw. An order that is neither fails its cell.

## What the outcomes mean (fixed now)

- **C1 holds.** The moves jointly allow only the trivial line. With W139, the weave's joint frame has D ≡ 1. Any split
  of leptons from down quarks needs a line fixed by one thread, so it is a thread choice, not forced by the principle.
  Since the moves act transitively on each order, the weave sees only a line's order, never the line.
- **C2 holds.** B1713's census set is exactly the threads' lines of order ≤ 12.
- **C3 holds.** Twist arithmetic with a generic coupling reproduces main's law (with the sign symmetry, as main's frame
  has it), so the model is a faithful instrument for what the twists force. **C3 fails:** the model is not faithful,
  and C4 is read only post hoc.
- **C4 holds.** The ingredient is the same but the protected set differs.
  - Inside E₆, only the five-ality lines (N ∣ 5) keep m_e = m_d, as SU(5)'s centre.
  - Main's mod-4 coincidence (Q ≡ L, d^c ≡ e^c, the Pati–Salam pairing) does not survive the 27's exotics.
  - W139's reading is corrected: both frames split d from e on most lines, but they protect different sets.
- **C4 gives {1, 2, 4, 5}.** The exotics do not matter, and W139's reading stands as written.
- **C4 gives any other set.** It is recorded as found.

## What stays out

- Data: no comparison with P-094's 10.58, and no new trial. That waits for parts 1 and 2, as agreed.
- τ, and any one frame's coupling function. B1656's functions are not rebuilt inside E₆; the generic F stands for every
  frame of this kind.
- Lines with components along the two other U(1)s that commute with the Standard Model.
- Orders above 12. The Higgs potential, and running.

## Seen before the rule (disclosed)

- **Read:**
  - main's B1728 FINDINGS, in full, for this rule;
  - W31's F4 argument (the moves force trivial hypercharge lines; argued there, not computed);
  - W138's C1, C3 and C4 (D_frame on orders 1, 2, 4, 5 and 10).
- **By hand:**
  - C1's fixed points;
  - C2's count, (528 − 4)/2 + 4 = 266;
  - C3's sets, from the twist pairs;
  - C4's set. Only the transposed correspondence fits the extended matrices' shapes. It needs N ∣ 5 on the light
    entries and on the exotics' entries: (−3, 3) against (−2, 2);
  - C5's 22 and 13;
  - the argument for pure hypercharge.
- **Not run:** nothing has been computed by a script.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
