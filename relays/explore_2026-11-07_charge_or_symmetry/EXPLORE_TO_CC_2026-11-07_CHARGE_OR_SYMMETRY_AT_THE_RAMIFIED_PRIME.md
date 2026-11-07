# EXPLORE → CC: CHARGE OR SYMMETRY AT THE RAMIFIED PRIME (P-738) (2026-11-07)

**From:** the explore seat. **To:** main (cc).

**For:** the owner's "yes" to the P-738 test.

**Kind:** data-free; no frame value, no data, no held-out quantity.
- Pre-registered at 4b0f638d8, pushed before the run.
- Output committed unread at f272c392b, then read.

## The question

At S = {5} the two readings of "invisible at level 5" select different departures:
- the charge reading, E ≡ ±I mod 5, selects (6), at depth 3.618 (P-737; B1855's proof is cited, its rebuild P-741);
- the symmetry reading, E ∈ ±⟨LR⟩ mod 5, selects (2,1,1,1,2), at depth 1.625.

They differ by exactly a golden phase, E ≡ ±(LR)^a with a ≢ 0 mod 5.

Does the object's own level-5 structure decide between them?

## Results (charge_or_symmetry_out.txt)

The tests use the object's own level-5 quantization: B355's Weil representation of the quantized golden cat map, with
R = T and L = S T⁻¹ S⁻¹, ρ(T) = diag e(3x²/5), and ρ(S) the discrete Fourier transform on C⁵. Parity splits C⁵ into an
even sector (dimension 3) and an odd sector (dimension 2).

- **HG TRUE.**
  - H = ±⟨LR⟩ mod 5 has order 10 and is conjugate in SL(2, F₅) to ±{[[1, b], [0, 1]]}, the image of ±Γ₁(5).
  - LR has order 5 in PSL(2, F₅).
  - So the object's own tick closes on X_H ≅ X₁(5) every tick, and on X(5) only every 5 ticks.
  - The symmetry reading is closure on X_H. The charge reading is closure on X(5).
- **HQ0 TRUE.** ρ is projective: all 120 elements are reached, 121 repeated arrivals are checked, and none clashes. ρ(S)²
  and ρ(−I) are both proportional to the parity.
- **HQ1 TRUE: the charge reading is gauge invisibility.**
  - ρ(E) is a scalar on C⁵ only for E = I.
  - On each parity sector, ρ(E) is a scalar exactly for E = ±I.
- **HQ2 TRUE: the symmetry reading is the commutant.** The E with ρ(E)ρ(LR)ρ(E)⁻¹ ∝ ρ(LR) are exactly ±⟨LR⟩.
- **HQ3 TRUE: the tick is a ℤ/5 clock in every sector.**

  | sector | eigenvalue angles of ρ(LR) (turns) | what it is |
  |---|---|---|
  | even (dimension 3) | 0, 0.4, 0.6 | an icosahedral rotation by 4π/5 |
  | odd (dimension 2) | 0.1, 0.9 | |

  - In each sector the eigenvalues are pairwise distinct, and every ratio is a primitive 5th root of unity.
  - ρ((LR)^a) is a scalar on a sector only for a ∈ {0, 5}.
  - **Second check, by character tables (exact):**
    - the even trace is 1 − φ = (1 − √5)/2, A₅'s 3-dimensional character on a 5-cycle;
    - the odd trace is 2 cos 36° = φ, the value the record found at level 45 (CLAIMS E17, tr ρ(A₁) = φ).
- **HQ4 TRUE.**
  - **(6):** E ≡ I, a scalar on C⁵ and on both sectors. It is invisible on every state.
  - **(2,1,1,1,2):** E ≡ LR, a golden phase of a = 1. It is not a scalar on C⁵ or on either sector. It acts as a phase
    on every eigenvector of ρ(LR), so it is invisible only on quasi-energy eigenstates.

## The reading

**In the object's own level-5 quantization:**
- the charge reading is exactly the gauge sense of "invisible": a scalar on every state;
- the symmetry reading is invisible only on stationary (quasi-energy) states;
- the golden tick is a ℤ/5 clock in every sector, in the even sector literally an icosahedral rotation by 4π/5;
- so the line-invisible departure (2,1,1,1,2) is observable on any superposition of quasi-energy states.

So the symmetry reading needs a superselection rule forbidding superpositions of the object's level-5 quasi-energy states,
which stops the ℤ/5 clock. Standard quantum mechanics has no such rule. Under it, the charge reading is the invisible
one, and it gives the run of 6 at depth 3.618.

**Geometry and quantum point opposite ways, as pre-registered:**
- the tick's own closure curve is X_H ≅ X₁(5), the symmetry side;
- the quantum state space carries the full SL(2, F₅) action, faithful up to ±I on each sector, the X(5) side.

The quantum side is what decides "invisible".

**Conditional on two things:**
1. the level-5 Weil representation is the physical state space at level 5 (P-721's object-native level; LAW_MAP's
   "measurement is passage through the finite");
2. standard quantum mechanics: superpositions of quasi-energy states are physical.

## What remains for the deep candidate (P-717)

- the read-out at the apex;
- minimization against a sum;
- the premise that the history departs at all;
- the hand;
- conditions 1 and 2 above.

**Speculation (tagged):** the level-5 quantum clock is the quantized tick itself. Whether it is "followed" is close to
P-438's "followed against counted", and to the record's clock rows (B1815: the clock CHOSEN). A data-free test: does the
record's own minimal sector (P56, the two-state sector with quasi-energy ±108°) contain superpositions that the dynamics
runs as a clock?

## Suggested rows (main's to assign)

- **P-738:** answered as conditional. Under standard quantum mechanics on the object's level-5 quantization, the charge
  reading is the invisible one, and the symmetry reading needs a quasi-energy superselection rule.
- **P-717:** a dated note naming conditions 1 and 2 as the level-5 premise's grounds.

0 of 19.
