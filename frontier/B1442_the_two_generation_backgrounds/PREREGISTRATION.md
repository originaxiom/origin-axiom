# B1442 PREREGISTRATION — THE TWO-GENERATION BACKGROUNDS: does a whole background count two, where a module does?

**Sealed 2026-10-01, before any background is assembled on a manifold with more than one cusp. Seat: cc (main).
Occasion: B1441 found seventeen manifolds on which one rank-two non-split module has class index two, and wrote,
before its data, that a module is not a generation-shaped background and that the frame's five charged sectors would
be put to the carriers in a further sealed arc. This is that arc (lead L234 (a)).**

## 0. The quantifier (P0)

For each of the seventeen carriers of B1441, every background (ℓ, c, θ, ψ_Y, W) of B1432's frame with ℓ = θ²/W, c a
class of H¹(M; ℓ), and sector modules V(ℓ, α_s): the six class indices on all cusps. The scope sentence names no
manifold.

## 1. Conventions

- **The frame is B1432's, unchanged:** sectors Q(1,3), u^c(−4,3), e^c(6,3), d^c(2,1), L(−3,1), ν^c(0,−5);
  α_s = θ ψ_Y^{s_Y} W^{(s_γ−1)/2}. **Generation-shaped of count g:** the five charged sectors all have index g ≠ 0.
- **Characters:** every character of order dividing N (the torsion exponent of H₁, or 2), no cusp condition, as in
  B1441.
- **Classes:** where H¹(M; ℓ) has dimension m > 1 the class is part of the background. Tried: the m basis classes
  of the instrument's null-space basis, and three seeded random combinations. A background found only at basis
  classes is reported as such; "generic class" means h¹(ℓ) = 1 or a random combination.
- **Index:** B1333's `mc_lib.check`, identities asserted on every module, one prime; every background of count ±2
  is then recomputed exactly with B1441's `exact_mc.py` before it is reported.
- Instrument `verification/backgrounds_mc.py`; reader `verification/read_backgrounds.py`, run twice before the seal.

## 2. What has been seen before the seal (disclosed)

- B1441 in full: which modules have |I| = 2 on the seventeen, their live cusps, and twelve recorded witnesses per
  carrier. **No background has been assembled on any of them.**
- **C1, the control:** the instrument on the one-cusped s961 and M₄ with every character of order dividing N (64
  and 675): 48 and 256 backgrounds, the banked numbers, all of count ±1. Record `control_run.txt`.

## 3. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| G1 | Some carrier has a generation-shaped background of count ±2. | 35% |
| G2 | Every carrier has a generation-shaped background of count ±1. | 55% |
| G3 | Some carrier has a background of count ±2 whose ν^c sector also has index ±2 of the same sign. | 15% |
| G4 | Some background of count ±2 exists at a generic class. | 20% |
| G5 | No background has charged sectors of index above 2 in absolute value. | 95% |

## 4. What each outcome would mean (written before the data)

- **G1 YES** would be the first background in the record with two net generations of every charged sector in one
  vacuum. It is not three, and by B1441 three is not available on these manifolds at rank two.
- **G1 NO** would say that an index of two is a property of single sectors that the frame's charge relations do not
  let five sectors share; the count per background would then stay at one even where modules reach two.
- **G4** separates a background that exists for an open set of SL(2)_β bundles from one that needs a special class.
- None of the outcomes is a physical statement. Fence as in B1441: main's class index outside the reductive domain;
  an index is not a generation count; no physics reading. 0 of 19.

## 5. Not in this arc

Couplings on several cusps; three; manifolds other than the seventeen; modules of rank above two.

## 6. Hashes at seal

See `ARTIFACT_HASHES.txt`.
