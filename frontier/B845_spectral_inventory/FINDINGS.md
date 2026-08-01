# B845 — the spectral inventory, checked: what exists, where, and one artifact that disagrees with its own table

cc banking seat, 2026-08-01. Repository-instrument scope; Gate 5 untouched.

## Why this exists

The review register carried *"the spectral paper, still finished and unshipped"* through **five
reviews**, and I repeated it roughly six times this session without opening a directory. When P5's
Phase 0 finally looked, `papers/` held **no spectral paper at all**.

The review seat then corrected itself and named the real location — **and I checked that correction
too, rather than swapping one unverified description for another.** It is directionally right and
its numbers do not match main.

## What is actually in `main`

| arc | content | state |
|---|---|---|
| **B797** `maass_spectrum_harvest` | **17 certified Maass eigenvalues**, r = 3.9389 → **9.8371**, with multiplicities; mode-count certified **664 → 900 modes** (Bessel margins 21.0 → 27.0), **max \|Δr\| = 5.42×10⁻⁹**; n = 6 identified as the **parent (Bianchi) ground state** by direct S-invariance (S-invariant to 7×10⁻¹⁰ while all others break at order 1 — **nine orders of separation**) | harvested from cc3 |
| **B795** `eigenvalue_verification` | **7/7 independently verified** — re-derived on this seat's own instrument, not a re-run | verification receipt |
| **B794** `congruence_level4` | **Γ₄₁ is a congruence subgroup of level (4)**; the **mod-4 trace law PROVED** | harvested from cc3 |

**`B792` is not in `main`.** It is **cc3's** arc, and cc3 never merges — B795 and B797 are the
harvest and the receipt. Citing B792 as if it were here is the same class of error as the phantom
paper: a real thing, in a place other than the one named.

## The number that did not check out, and why it probably still is true

The correction described **"43 eigenvalue parameters to r = 13.5"**. **Main carries 17, to
r = 9.84.** Those are not the same claim.

> **The most likely reconciliation: cc3's B792 holds more than main harvested.** 43-to-13.5 would be
> cc3's own extent; B797 took 17 of them. That is exactly what the never-merge rule produces — the
> audit seat's spectrum is deeper than the harvest — **and it means the harvest is incomplete, not
> that the number is wrong.**

**Not asserted here.** cc3's tree is not in this repository and this seat has not seen it. **What is
verified: 17 in main, 7 of them independently re-derived.**

## An artifact that disagrees with its own findings

**`B797/eigenvalues_final.json` carries 6 eigenvalues. The FINDINGS table certifies 17.**

The machine-readable artifact holds a **third** of the certified spectrum, and anything downstream
reading the JSON rather than the prose gets a truncated spectrum with no signal that it is
truncated. **Recorded, not silently repaired** — the fix is either to complete the JSON from the
table or to rename it as the partial extract it is, and that is a judgement about which is the
source of truth.

## The corrected sentence, for the register

> **Certified spectral results exist in `frontier/` (B794, B795, B797). A spectral paper does not
> exist anywhere.** Two different things, blurred for five reviews.

## Carried

1. ~~Complete or rename `eigenvalues_final.json`~~ — **DONE (B846): completed to all 17.** The table
   is the certified artifact and the JSON is its serialization; renaming would have preserved the
   trap. The 11 added entries carry `r`, `λ`, multiplicity from the table with diagnostics marked
   **ABSENT rather than invented**, since cc3's per-eigenvalue data was never harvested.
2. **The harvest gap — one line, and then it is dropped.**
   > **Main has 17. cc3's B792 may hold more. Harvest completeness UNVERIFIED.**

   **Not to be investigated from here:** cc3's tree is not in this repository, and chasing it would
   be the same error as citing B792 as if it were in main.
3. The register's *"spectral paper"* phrasing is corrected here; it should not reappear.

`tests/test_b845_spectral_inventory.py`
