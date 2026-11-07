# CHARGE OR SYMMETRY AT THE RAMIFIED PRIME (P-738) — pre-registration (the explore seat, 2026-11-07)

**For:** the owner's "yes" (2026-11-07) to the P-738 test.
- P-737 is settled (B1855). At S = {5}, least action under the charge reading (E ≡ ±I mod 5) selects the run of 6,
  depth 3.618. The proof for all defects is cited, not yet rebuilt on main (P-741).
- Under the symmetry reading (E ∈ ±⟨LR⟩ mod 5), least action selects (2,1,1,1,2), depth 1.625.
- The two readings differ by exactly a golden phase E ≡ ±(LR)^a, a ≢ 0 mod 5: a level-5 tick count.

**The question:** does the object's own level-5 structure decide between them?

**Kind:** data-free; finite-group and representation arithmetic only; no frame value, no data, no held-out quantity.
**Written before** `charge_or_symmetry_check.py` is run. Its output is committed unread, then read.

## Seen first (swept 2026-11-07 over main's docs)

**On record:**
- the quantized golden cat map and its level tower (B376, P59);
- the Weil representation at N = 3, 5, 15 (B355), with main's level-5 convention R = T, L = S T⁻¹ S⁻¹ and the odd
  subspace span{δ₁ − δ₄, δ₂ − δ₃} (P-738's row; Theorem 150's check);
- the order-5 line classes as the cusps of X₁(5) (B1845);
- T as a symmetry of the frame's outputs (S301);
- P-738's own test (X(5) against X₁(5));
- P-454 (the Weil filter).

**Not found:**
- the two readings as gauge (scalar) against symmetry (commutant) in the level-5 Weil representation;
- the golden tick as a ℤ/5 clock in each of its sectors.

## The two structures, both object-native at 5

- **(G) Geometry.**
  - H = ±⟨LR mod 5⟩, of order 10, is the object's own level-5 group.
  - The object's tick closes on X_H every tick, and on X(5) only every 5 ticks.
  - Rung departures close on X(5). Line departures close on X_H.
- **(Q) Quantum.** ρ is the level-5 Weil representation, built as B355 does, on C⁵ with δ_x for x ∈ ℤ/5:
  - ρ(T) δ_x = e(3x²/5) δ_x, where 3 = 2⁻¹ mod 5;
  - ρ(S) is the discrete Fourier transform;
  - R = T and L = S T⁻¹ S⁻¹;
  - it is projective, extended to all of SL(2, F₅) by words and checked for consistency up to scalars;
  - parity P = ρ(−I) (up to phase) splits C⁵ into the even sector (dimension 3) and the odd sector (dimension 2).

## Hypotheses, before computing

- **HG (exact):**
  - H = ±⟨LR⟩ mod 5 has order 10 and is conjugate in SL(2, F₅) to ±{[[1, b], [0, 1]]}, the image of ±Γ₁(5);
  - LR has order 5 in PSL(2, F₅).
- **HQ0:** ρ is a projective representation. Every element reached by two words gives proportional matrices, and
  ρ(S)² ∝ P.
- **HQ1 (the charge reading is quantum invisibility):**
  - ρ(E) is a scalar on C⁵ exactly when E = I;
  - on each parity sector, ρ(E) is a scalar exactly when E = ±I.
- **HQ2 (the symmetry reading is the commutant):** ρ(E)ρ(LR)ρ(E)⁻¹ ∝ ρ(LR) exactly when E ∈ ±⟨LR⟩.
- **HQ3 (the tick is a ℤ/5 clock in every sector):**
  - on each sector, the eigenvalues of ρ(LR) are pairwise distinct;
  - every ratio of two of them is a primitive 5th root of unity;
  - hence ρ((LR)^a) is a scalar on a sector exactly when a ≡ 0 mod 5.
- **HQ4 (the two candidates):**
  - ρ(E) for (6) is a scalar on C⁵;
  - ρ(E) for (2,1,1,1,2) is proportional to ρ(LR)^a with a ≢ 0 mod 5, so it is non-scalar on both sectors, and acts as
    a phase on each eigenvector of ρ(LR).

**Priors:**
- HG, HQ0, HQ1 and HQ2 are near certain, being standard.
- HQ3 is likely: the even sector should be A₅'s icosahedral rotation representation, with the tick as a rotation of
  order 5, and the odd sector a binary-icosahedral representation.

## What follows either way

- **If HQ1–HQ4 hold:**
  - in the object's own level-5 quantization, "invisible" in the gauge sense (a scalar on every state of a sector) is
    exactly the charge reading;
  - the symmetry reading is invisible only on quasi-energy eigenstates;
  - the golden tick is a ℤ/5 clock in every sector, so a phase shift by a ≢ 0 is observable on any superposition of
    quasi-energy states;
  - so the symmetry reading needs a superselection rule forbidding quasi-energy superpositions at level 5, a rule
    standard quantum mechanics does not have;
  - and the charge reading, which gives the run of 6 at depth 3.618, is the one consistent with standard quantum
    mechanics on the object's level-5 quantization.
  - **It stays conditional on** the level-5 Weil representation being the physical state space: P-721's
    object-native level, and LAW_MAP's "measurement is passage through the finite".
- **If HQ3 fails in some sector,** where the tick's eigenvalues coincide, the two readings coincide in that sector.
  The sector is reported, along with whether it is the record's odd sector of Theorem 150.
- **Geometry (HG) and quantum (HQ) may point opposite ways:** X_H, where the tick closes, against the full SL(2, F₅)
  action of ρ. That is reported as found.

0 of 19.
