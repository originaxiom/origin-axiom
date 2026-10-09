# B1634 — PREREGISTRATION: THE SM SEAT'S W50 ON MAIN, AND W45'S MULTIPLIER FROM THE THETA CONSTANTS

cc (main), 2026-10-09, after S111. **Sealed before `w50_on_main.py` runs.** No data. 0 of 19.

**Why it matters.** The SM seat's W50 says three things. On the owner's ruled branch (the weave ⟨L, R⟩, with even ticks
and positivity) the inner automorphisms by a and by b are not moves. So at a generic τ the weave leaves only scalars on
T, and couplings in τ alone are vector-valued modular forms with generic mixing. And T is exactly the representation of
η²¹·(θ₂², θ₃², θ₄²). If so, main's T-TAU-ONLY-PERMUTATION and the residual groups of B1617, B1618 and B1630 hold only in
the frame where the inner automorphisms act. Separately, the classical theta constants would supply the multiplier on
which B1632 found W45's χ_{3/2} = 0 to depend. The owner's audit rule asks main to verify such load-bearing claims itself.

## Seen first

`VERDICT topic-sweep /inner automorphism|ruled branch|theta constant|metaplectic|braid/: 7 of 1405 arcs on main match (NEGATIVE 4, PROVED 3)` — the
SM seat's relay §54–§55 and its W49–W50 @ `3e7c0eec6`; B1617, B1618, B1620's inner cell and T-TAU-ONLY-PERMUTATION,
B1630, B1632. **Literature:** B₃ → SL(2, ℤ) with kernel ⟨Δ⁴⟩; Aut⁺(F₂) → SL(2, ℤ) with kernel Inn(F₂); the Jacobi theta
transformation laws (θ₂, θ₃, θ₄ under τ + 1 and −1/τ) and η's.

## Disclosed

- Not blind: W50's claims were read before the seal. Main writes its own code: word enumeration, lifts, the theta laws
  checked numerically, and the equivalence test.
- V1 enumerates words to length 10 (the seat went to 12), for time.
- The equivalence test looks for M with M ρ_θ M⁻¹ equal to the lifts up to scalars (α, β) at 48th roots of unity.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **V1** | every reduced word of length ≤ 10 with H₁ = I acts as the identity or as conj(c^{±1}) (c = a b⁻¹ a⁻¹ b); none as conj(a^{±1}) or conj(b^{±1}) | 92% |
| **V2** | their lifts on T are all scalars | 92% |
| **V3** | the classical laws check numerically; ρ_θ is equivalent up to scalars to the lifts for at least one identification, with θ₃² going to the clock's line (−, −) | 75% |
| **V4** | χ_{3/2}(ρ_θ) = 0 and χ_{23/2}(ρ_θ) ≥ 1 (η²¹θ² is a form there) | 75% |

**The reading, written before the run (the cells can only lower it).**
- **If V1 and V2 hold,** W50's premise is verified on main. On the ruled branch the inner automorphisms are not
  symmetries, T-TAU-ONLY-PERMUTATION holds only where they act, and couplings in τ alone are vector-valued modular forms.
- **If V3 and V4 hold,** the classical theta constants fix W45's multiplier, and χ_{3/2} = 0 is verified independently of
  W41. The cusp unit's payoff (±3 given Λ and the unit) then rests on verified mathematics, and on the ruled branch the
  flavour numbers are values at τ of modular forms built from the theta constants.

## Instruments

`verification/w50_on_main.py`; hashes in `ARTIFACT_HASHES.txt`.
