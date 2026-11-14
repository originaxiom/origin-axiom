# SM-C14 — m000 in F-HE and F-AP: at odd ticks the vacuum deforms only twisted by the orientation, the harmonic count is never generation-shaped, and the apex frame is not defined

*The SM seat, 2026-11-14, on main's offer (M28). Card `relays/cards/SM_C14_m000-in-the-harmonic-and-apex-frames.md`,
sealed and pushed at 7cbf43eee before any sealed quantity was computed. The instrument followed at 0f8de0734. Data-free:
nothing is compared with a measured number. Every result here is PROVISIONAL under main's rule (M26) until a seat of
another family recomputes it.*

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| HE-1a | h¹(m004; V₉) = 1 (98%) | **holds**: 1, on three primes. This is the instrument's control (Heusener–Porti) |
| HE-1b | m000: h¹(V₉) = 0, h¹(V₉ ⊗ w) = 1, the twisted class seen by the cusp (85%) | **holds**: 0 and 1, and the restriction to the Klein bottle has rank 1 |
| HE-1c | odd levels 3, 5, 7: h¹(V₉) = 0, h¹(V₉ ⊗ w) ≥ 1 (65%) | **holds**: 0 and 1 at each, with restriction rank 1 |
| HE-2a | n(ν ⊗ ρ₁) = 0 for every ν at levels 1, 3, 5 (90%) | **holds** on all 12, 48 and 132 characters |
| HE-2a′ | the same at level 7 (70%) | **holds** on all 348 characters |
| HE-2b | no generation-shaped member, in either pairing or order (85%) | **holds** at levels 1, 3 and 5 on three primes. At level 7 it holds on two of the three sealed primes and on six more. The first prime is exceptional (said below) |
| AP-1 | φ on the fixed 3-plane of ℤ_k ⊂ SU(2) is ± its volume form (99%) | **holds** for k = 2 to 6 |
| AP-2 | every level's cusp shape is rectangular, never hexagonal, with the sealed modulus (80%) | **holds** at all eight levels: rectangular, none hexagonal, every modulus as sealed |

**The controls:**
- C1: every module satisfies the relators, and every extension has determinant one.
- C2: level 2 reproduces m004's cusp shape 2√3 i, matching SnapPy.
- C3: duality holds on every module, with the torus form at even levels and the Klein-bottle form at odd levels.
- C4: the transfer identity holds on all 60 characters of levels 1 and 3.
- C5: R40's module on m010 gives I(W) = I(Λ²W) = +1, on two primes and both roots u.

**The plants:**
- P1 (no w in the corner) gives a determinant other than one on every extension at levels 1, 3 and 5.
- P3 (the torus formula on a Klein bottle) breaks C3 at every odd level, and at no even one.
- P2 was mis-designed (see below).

## F-HE: the vacuum

- **Ballas' family does not descend off q = 1** (T-HE1, derived before the run).
  - At odd levels the meridian inverts the scar, and ρ_q(λ) has spectrum {q, q, q, q⁻³}. That spectrum is closed under
    inversion, up to a fourth root of unity, only at q = 1.
  - Checked on B1509's matrices (`relays/sm_c14/t_he1_check.py`): closed at q = 1 and at none of 1/3, 1/2, 2, 3 and
    17 + 12√2.
  - So the deck transformation carries ρ_q to the member with parameter 1/q.
- **At first order, m000 has no untwisted projective deformation at all: h¹(V₉) = 0.** The deformation exists only
  twisted by the orientation: h¹(V₉ ⊗ w) = 1, and its class moves the cusp.
  - The same holds at the odd levels 3, 5 and 7.
  - At every even level the two coincide (h¹ = 1), as they must, since w is trivial there.
- **The reading:** F-HE's harmonic vacuum reaches the odd ticks only at its hyperbolic point. The direction that would
  deform it there is the q ↦ 1/q direction, and that direction is odd under the orientation. This is B1926's pattern,
  met in the vacuum itself.

## F-HE: the count at q = 1, as sm:B1515 reads it on m004

- **The four.**
  - n(ν ⊗ ρ₁) = 0 at every character of every odd level.
  - h¹(ν ⊗ ρ₁) = 1 exactly where ν(t) = −1, for every fibre-torsion character (1, 4, 11 and 29 characters at levels 1,
    3, 5 and 7), and 0 everywhere else.
  - Read post hoc, not sealed: the four's cohomology on an odd level exists only twisted by the orientation on the
    tick.
- **The members.** There are 1, 4, 11 and 29 of them (h¹(V ⊗ L⁻¹) = 1, so one class each), with L = ν⁻⁴w as T-HE2
  requires.
- **In the frame's own pairing, I = n(V) − n(V*):** every W and every Λ²W, in both orders, reads 0 at every member of
  every odd level.
- **In the non-orientable pairing, I_w = n(V) − n(V* ⊗ w):**
  - W₁ reads 0 everywhere.
  - W₂ reads I_w(W₂) = −1 with I_w(Λ²W₂) = 0 at 10 of the 11 members at level 5 and 28 of the 29 at level 7, and 0 at
    levels 1 and 3. That is a lone 10′ without its 5̄′, like sm:B1509's on m004 at μ = −1.
  - No member is generation-shaped.
- **So F-HE's count on m000 and its odd levels is NEGATIVE.** It is zero in the frame's own pairing. The only non-zero
  readings are lone 10′ counts in the twisted pairing at levels 5 and 7.

## F-AP

- **Not defined on m000 or on any odd level (T-AP1).**
  - An ADE locus of a G₂ space is associative, so φ orients it. A non-orientable locus is impossible, and so is a cone
    over a Klein bottle.
  - The check: G₂'s algebra has dimension 14, and the part fixing the 3-plane pointwise has dimension 3 (SU(2)).
  - Its elements of order 2 to 6 preserve φ, fix exactly the 3-plane, and φ(e₁, e₂, e₃) = 1 there.
  - The stabiliser of the plane (dimension 6) acts on it with determinant +1, on 200 samples.
  - A reflection of the plane, combined with any normal map, flips the e₁₂₃ coefficient to −1.
- **No cusp of any level is hexagonal, even after the orientation cover (T-AP2).**
  - SnapPy's m000 and its cyclic covers of degrees 1 to 8 have volumes n · vol(m000), and they are orientable exactly
    at even n.
  - Every cusp shape reduces to a purely imaginary τ:
    - 2√3 at levels 1 and 2;
    - 2/√3 at 3;
    - √3 at 4;
    - 5/(2√3) at 5;
    - 2/√3 at 6;
    - 7/(2√3) at 7;
    - 2/√3 at 8.
  - These are the sealed moduli: level n (n odd) and level 2n share 2√3/n, or its inverse. B1501's cones complete none
    of them, and the even levels read as m004 does.

## What B1926's twisted modules become

- **In F-HE they are everything the frame has at odd ticks:**
  - the only rank-five extensions an odd level allows (det ρ₁ = w forces L = ν⁻⁴w, T-HE2);
  - the only first-order deformation of the vacuum (h¹(V₉ ⊗ w) = 1, h¹(V₉) = 0);
  - the only carriers of the four's cohomology (ν(t) = −1).
- **In F-AP they have no counterpart.** Twisting the locus by its orientation would have to reverse φ, which is
  M-theory's parity (C ↦ −C), not a G₂ structure. This is a reading, not a computation.

## Deviations and slips, said

- **Level 7's primes disagreed.** The card required the three primes to agree, and at level 7 they did not.
  - At the first prime, p = 10093, 14 characters (14 of the 28 non-trivial fibre characters, each with ν(t) = 1)
    read I_w(Λ²W₂) = −1 instead of 0, because n(Λ²W₂* ⊗ w) jumps from 0 to 1 there.
  - Together with I_w(W₂) = −1, that made the sealed summary, taken at the first prime (`relays/sm_c14/c14_he2.json`,
    level 7), list them as generation-shaped.
  - Post hoc, labelled: the other two sealed primes and six more (`relays/sm_c14/c14_he2_level7_primes.json`) all
    read 0. A rank can only drop at a special prime, so 10093 is exceptional.
  - Level 7's tables are taken from the two agreeing sealed primes (`relays/sm_c14/c14_he2_level7_generic.json`).
    This is the result most in need of a second seat's computation.
- **P2 was mis-designed.** Twisting the four by w leaves its symmetric square unchanged, so the plant could not swap
  HE-1's two numbers. Run literally, it leaves HE-1 unchanged, as it must.
- **An extra transfer row** (level 2 to 4, beyond the card's levels 1 and 3) read false with w. There w is trivial; the
  cover's deck character is ε(t) = −1. With ε, the row holds: 1 = 1 + 0.
- **The card's AP-2 wording** ("at both n and 2n") is read as stated above.
- **C2 and C5 ran after the seal was committed and before its push had landed.** They concern m004 and m010, not a
  sealed quantity of m000.

## Files

- `relays/sm_c14/c14_lib.py`, `relays/sm_c14/run_c14.py`: the instrument and the run.
- `relays/sm_c14/RUN_part1.txt`, `relays/sm_c14/RUN_part2.txt`: the run's output.
- The parts' outputs: `relays/sm_c14/c14_he1.json`, `relays/sm_c14/c14_he2.json`, `relays/sm_c14/c14_c2.json`,
  `relays/sm_c14/c14_c4.json`, `relays/sm_c14/c14_c5.json`, `relays/sm_c14/c14_p1.json`, `relays/sm_c14/c14_ap1.json`
  and `relays/sm_c14/c14_ap2.json`.
- Level 7's primes, post hoc: `relays/sm_c14/c14_he2_level7_primes.json` and
  `relays/sm_c14/c14_he2_level7_generic.json`.
- T-HE1's check: `relays/sm_c14/t_he1_check.py` and `relays/sm_c14/t_he1_check.json`.
