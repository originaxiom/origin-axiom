# W160 — the plan's stage 1, first part: the agy branch's line selection (B1761) and sector-blind norm (B1759) on this seat's own code. Is B1761's condition exact arithmetic at every τ, and is its cutoff an exponent law? (the rule, committed before the script)

The SM-derivation seat, 2026-10-27. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's word:** "i agree with you proposed plan" (2026-10-27). The plan is
  `THE_NINETEEN_PLAN_2026-10-27.md`; its stage 1 asks for third opinions, on own code, on the agy branch's kept leads
  before anything is built on them.
- **What B1761 claims** (the agy branch at 05e6caabf, its script and run file read).
  - Over 662 lines (B1726's 266 of order up to 12 and B1755's 396 of orders 13, 14, 15 and 20), at one probe point
    τ = 0.3145 + 3.0345i, a condition C1 leaves 10 lines.
  - **C1:** the up sector's i-channel residue is zero, its j-channel and the down sector's i-channel are not, and
    a ∉ {0, ½}.
  - A cutoff C2 (the up residue's invariant I < 0.05 and ‖R_jk‖/∣R_1∣ > 2) leaves the five lines (2/5, odd/10), the
    lines the six's census found.
- **What B1759 claims:** the channel kernel depends only on the summed twist. Since ∣q_L + q_R∣ = 3 in every sector,
  the puncture norms are the same in every sector.

## The hand work (data-free; done before this rule, disclosed)

- **The residues, in this seat's own formulas** (W85, W89): R_s = c_s θ_s(π ub) θ_s(π dl), with ub = (q_L + q_R)w and
  dl = (q_L − q_R)w, w = aτ + b. The units (1, i, j, k) go with the thetas (1, 2, 4, 3), and c = (−i, −1, −1, i).
  - Up: (q_L, q_R) = (1, −4), so ub = −3w and dl = 5w. Down: (1, 2), so ub = 3w and dl = −w. Leptons: (−3, 6), so
    ub = 3w and dl = −9w.
- **The zero law.** θ₂(πz) vanishes exactly at z ≡ ½ modulo ℤ + ℤτ.
  - So R_i^up = 0 if and only if 5w ≡ ½ or 3w ≡ ½, and R_i^down = 0 if and only if 3w ≡ ½ or w ≡ ½, at every τ.
  - 5w ≡ ½ means 5a ∈ ℤ and 5b ≡ ½: a ∈ {0, 1/5, …, 4/5} and b ∈ odd/10, the lines of order 10 (with (0, ½) of
    order 2).
  - C1 (B1761's clauses) is therefore 5w ≡ ½ with a ≠ 0. Up to sign that is the 10 lines (1/5, odd/10) and
    (2/5, odd/10), at every τ. Without the clause a ∉ {0, ½} it adds (0, 1/10) and (0, 3/10).
  - No line of order 13, 14, 15 or 20 can satisfy it.
- **The cutoff as an exponent law.** On a C1 line, R_i^up = 0, and the up residue's invariant over (i, j, k) is
  I = ∣R_j² + R_k²∣/(∣R_j∣² + ∣R_k∣²).
  - In θ₃(π ub) and θ₄(π ub) the two leading terms have opposite parity and sit at distances d = ‖3a‖ and 1 − d.
    So I = 2ε/(1 + ε²) with ε = exp(−π(1 − 2‖3a‖) Im τ), up to terms smaller by e^{−π Im τ}.
  - For a = 2/5, ε = e^{−(3/5)π Im τ}. For a = 1/5, ε = e^{−(1/5)π Im τ}. The 2/5 lines are nearer the null cone at
    every Im τ.
  - B1761's clause I < 0.05 admits the 1/5 lines too once 2ε/(1 + ε²) < 0.05 there, from Im τ ≈ 5.87 on.
- **Seen before the rule:** B1761's run file (10 survivors; I = 0.0063–0.0068 on the 2/5 lines and 0.2905–0.2910 on
  the 1/5 lines; ‖R_jk‖/∣R_1∣ = 12.1–12.6 and 1.85). The closed form gives 0.00656 and 0.2907 at the probe.
- **B1759, by hand:** the kernels K_s(z) = e^{2πiAz} θ_s(z + ub) θ₁′(0)/(θ_s(ub) θ₁(z)), A = Im ub/Im τ, depend on
  ub only. Under ub → −ub, z → −z they keep their modulus, and the cell is symmetric. So c_s(−3w) = c_s(3w): up's
  norms equal down's and the leptons' exactly. The sectors differ only through dl: 5w, −w and −9w.

## The objects

- **The lines:** B1726's 266 and B1755's 396, rebuilt by this seat's own enumeration (B1726's and B1755's rule:
  gcd(j, k, N) = 1, the key the smaller of (a, b) and (−a, −b) mod 1).
- **The points:** τ ∈ {0.3145 + 3.0345i (B1761's probe), 0.13 + 1.07i, 0.05 + 2.05i, 0.85 + 3.45i, 0.5 + 6i}.
- **The residues:** this seat's own, at 60 digits (W85's theta series), and main's (B1656's functions, as sealed
  copies at origin/main, residues by contour) for the instrument check only.
- **The norms:** W89's polar quadrature.
- **No data.** No mass, mixing or census value is read.

## Weave or thread

**A frame result, data-free.** Every line of both lists is taken, and the claims are about all lines at once in the
frame B1656 with the record's hypercharges. C1 itself is a chosen condition. W160 does not make it forced; that is the
plan's stage 2. The lead was chosen by its author with the strip in view, so any later test built on it inherits that
look.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| L0 | **The instrument.** (i) The own enumeration reproduces both line lists exactly (266 and 396, in order). (ii) At the probe, on the 10 C1 lines and on every 33rd line of the 662 (all three sectors), main's residues and this seat's agree up to one factor per (line, sector): the ratio R_s(main)/R_s(own) varies across the nonzero channels by less than 10⁻⁷ relative, and a channel zero on own code (below 10⁻⁴⁰ of ∣R∣) is below 10⁻⁹ of ∣R∣ on main's | 85% |
| L1 | **The zero law, exact, at every point.** On own code at the first four points, over all 662 lines: R_i^up/∣R^up∣ < 10⁻⁴⁰ exactly on the lines with 5w ≡ ½ or 3w ≡ ½ and above 10⁻²⁵ on every other line; R_i^down likewise with 3w ≡ ½ or w ≡ ½ | 95% |
| L2 | **C1's survivors.** With B1761's clauses, exactly the 10 lines (1/5, odd/10) and (2/5, odd/10) at each of the first four points, none of them of order 13–20; without the clause a ∉ {0, ½}, 12 | 90% |
| L3 | **The cutoff as an exponent law.** (i) On the 10 lines, at the probe, at 0.85 + 3.45i and at 0.5 + 6i, I agrees with 2ε/(1 + ε²), ε = exp(−π(1 − 2‖3a‖) Im τ), within 10% relative. (ii) At all five points every 2/5 line has a smaller I than every 1/5 line | (i) 75%, (ii) 85% |
| L4 | **B1759, on own code.** At the probe, on the 10 lines, W89's norms satisfy c_s(−3w) = c_s(3w) for every unit s, to 10⁻⁸ relative | 95% |
| R | **Read-outs** (no prediction): the lines where R_i^up = 0 (the order-10 and order-6 sets, counted); ‖R_jk‖/∣R_1∣ on the 10 lines at each point; B1761's C1 + C2 survivors at each point, and the Im τ where the 1/5 lines first pass I < 0.05 (by bisection on own code; hand work says about 5.87); R_i^lep on the C1 lines | — |

## What the outcomes mean (fixed now)

- **L1 and L2 hold.** B1761's selection is exact arithmetic: C1 is 5w ≡ ½ with a ≠ 0, the same at every τ. The
  selection lives in two choices: that the up sector's i-channel vanishes, and that a ≠ 0. Stage 2 asks whether
  either is forced.
- **L3 holds.** B1761's cutoff is not a free number but an exponent law: among the C1 lines the up residue nearest
  the null cone is a = 2/5 at every τ. The data's α = 2/5 then reads as "C1, and the up residue nearest the cone",
  still two conditions to be derived. A fixed cutoff holds only below Im τ ≈ 5.87; an argmin holds at every τ.
- **L3 (i) fails, (ii) holds:** the ordering stands and the closed form is corrected before use.
- **L1 or L2 fails:** the hand work is wrong. The lines that break it are listed, and nothing is said about B1761
  until diagnosed.
- **L0 fails:** the own instrument and main's disagree. W85's and W89's agreement is re-examined before L1–L4 are
  read.
- **L4 holds.** B1759's identity is the record's own kernel formula (W87, W89), not a new theorem; its consequence
  that sectors split only through dl stands.

## What stays out

- Any data; B1761's Higgs probe (the inverse Gram) and B1762's recipes, which are W161; B1755's extension, which is
  W162; any claim that C1 is forced.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
