# xB026 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-18. Sealed, hashed and pushed before any cell runs.**

## P0

Homology and twisted-cohomology data of cyclic covers of two hyperbolic 3-manifolds. Named
mathematics. **No physics reading, no generation count promoted to physics, no value, nothing to
`CLAIMS.md`. Gate 5 absolute.**

## The question

xB021/xB022 split the object's invariants into two species: **`CS` and `H₁` have an orbit** (moved by
**A5**, the `b++`/`b+-` bit); **volume and the trace field do not**. B1375, on the SM-derivation lane,
finds **one net generation on every one of 80 800 backgrounds** of the object's own tower — never
two, never three.

> **Which species does the generation count belong to? Does A5 move it?**

Nobody has asked. It is the join of the session's two strongest results and it is falsifiable.

## WHAT WAS RUN BEFORE THIS SEAL (declared, not hidden)

1. **Instrument scout only:** `frontier/B1297_the_spectral_cover_index/verification/d2lib.py` and
   `frontier/B1413_the_audit_lanes_r21_r31/verification/main_r27_exact_lift.py` were **read** to see
   whether the index machinery on this branch is reusable. **Nothing was run.**
2. `B1374`/`B1375` verdicts read (xB025, banked).
3. xB013's Y2 cell **read** — it records the tower `(LR)ⁿ` as `m004, m206, s961, t12839,
   o10_150696, otet12_00013`, matching B1375's `Y₂…Y₅`.

**No cell of this arc has been run. No prediction below has been tested.**

## THE CONFIGURATION AXES — declared first

| axis | values | this arc |
|---|---|---|
| **the tower** | `b++(LR)ⁿ` (the object's) · `b+-(LR)ⁿ` (its A5 image) | **both** |
| **the level** | n = 1…6 | **as far as SnapPy resolves; the reached level is stated** |
| **the datum** | `H₁` / the census inputs / the index itself | **`H₁` and the inputs are MUST; the index is ATTEMPT, declared as such below** |
| **the frame** | B1374's SM frame (`c(SM) = SL(2)_β × ℂ*²`) | **NOT reproduced here — it lives on the lane and this arc does not re-derive it** |

## The cells and their predictions

**G1 — the scaffolding, as control.** Rebuild `b++(LR)ⁿ` and identify each level by **isometry
signature**. *Prediction:* `n = 1…5` give **m004, m206, s961, t12839, o10_150696**, reproducing
B1375's `Y₂…Y₅` and xB013's Y2 independently. *If this fails the arc halts* — the tower is
misidentified and nothing downstream means anything.

**G2 — THE CELL THAT DECIDES, and the kill condition.** Compute `H₁` exactly for both towers.
*Prediction:* **they DIFFER at every level** — A5 moves `H₁` (xB022 V3: 494/494 on the base).
> **BINDING KILL CONDITION: if `H₁` agrees at every computed level, then A5 is in the stabiliser of
> the tower's homology, the generation census's own inputs do not move, and the orbit hypothesis for
> the generation count is DEAD AT THE INPUT LEVEL. It must then be reported dead — as a
> theorem-shaped negative, not re-scoped into something softer.**

**G3 — the census inputs.** B1374 builds its character groups at `N = lcm(12, torsion exponent of
H₁)`. Compute `N` for both towers. *Prediction:* the `N` differ wherever `H₁` does, so B1374's census
**cannot be literally the same object** on the sister's tower.

**G4 — ATTEMPT, and declared in advance as one that may not land.** Generalise the branch's own index
instrument (`main_r27_exact_lift.py`'s `counts`, currently 2 generators / 1 relator over ℚ(u)) to a
cover's presentation, and compute the index at **at least one locus** on the sister's tower.
*No prediction is offered.* **If it does not land, the arc says so plainly and G2/G3 stand alone.**

**G5 — WHAT THE RESULT DOES NOT DECIDE, written before the data.** Moving the **inputs** does **not**
prove the **count** moves. *"One per background"* could survive on different loci — which would make
**one** the invariant and the backgrounds merely the orbit. **The arc must state which of these its
data supports and must not read a moved locus as a moved count.**

## Controls required

- **Isometry signature**, not volume, for every identification (volume coincidences are exactly how
  this record's sister pair arose).
- **Exact `H₁`**, no numerics.
- **A positive control** that the comparison can see a difference: the two towers' base level is
  `m004` vs `m003`, already known to differ (`ℤ` vs `ℤ ⊕ ℤ/5`).
- **Every failure counted, never swallowed** — the swallowed-`RuntimeError` lesson.

## What this arc may NOT conclude

It may not claim three generations, nor promote any count to physics — **B1374/B1375 fence
themselves identically and this arc inherits the fence**. It may not re-derive the SM frame. It may
not read a difference in loci as a difference in the count (G5). **It supplies no value.**
