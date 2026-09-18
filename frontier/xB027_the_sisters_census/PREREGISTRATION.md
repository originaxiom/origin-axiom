# xB027 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-18. Sealed, hashed and pushed before any cell runs.**

## P0

A twisted-cohomology census on cyclic covers of a hyperbolic 3-manifold, using **another seat's
machinery, borrowed with provenance**. Named mathematics. **No physics reading, no generation count
promoted to physics, no value, nothing to `CLAIMS.md`. Gate 5 absolute.** This arc inherits
B1374/B1375's own fence verbatim: *"main's index on a non-semisimple background, no physics reading,
no value."*

## The question xB026 left, now answered rather than handed over

xB026 decided that **A5 moves the census's inputs at 6 of 6 levels** but could not compute the
**count**, and named the bounded next step: *"run B1374's SM-frame census on `b+-(LR)ⁿ`."*
**This arc runs it.**

## WHAT IS BORROWED, AND FROM WHERE

`index_lib.py` and `tower_generations.py` from the SM-derivation lane
(`<remote>/standard-model-derivation-0qt6ao` at `23532539`), authored by seat `cc`, **copied with a
provenance header and NOT rewritten**. The only edit is to **which manifold the driver builds**:
the published driver hard-codes `snappy.Manifold('m004').covers(n, cover_type='cyclic')`.

## WHAT WAS RUN BEFORE THIS SEAL (declared, not hidden)

1. The lane's files were **read**; `tower_generations_run.txt` (its published output) was read.
2. **A cover-structure check was run and it changed the design:** `m004`'s degree-`n` cyclic cover
   **is** `b++(LR)ⁿ` (homology matches xB026 at every level), but **`m003`'s cyclic covers are NOT
   `b+-(LR)ⁿ`** — at `n = 2` SnapPy gives `ℤ⊕ℤ/5` where the bundle gives `ℤ⊕(ℤ/3)²`, and at `n = 5`
   there are **six** of them, which would trip the driver's `assert len(M) == 1`.
   **Reason: `m004` has `H₁ = ℤ` so its cyclic cover is unique and is the fibre-direction one;
   `m003` has `ℤ⊕ℤ/5` and it is not.** The driver must therefore be pointed at the **bundle**
   `b+-(LR)ⁿ` directly. **Had this not been checked, the arc would have silently censused the wrong
   manifolds.**

**No census cell has been run. No prediction below has been tested.**

## The cells

**C1 — THE BINDING CONTROL. The adapted driver must reproduce B1375's published numbers on the
object's own tower, or nothing downstream counts.** Targets, from `tower_generations_run.txt`:

| level | `H₁` | `N` | `|Hom|` | loci | firing | generation backgrounds |
|---|---|---|---|---|---|---|
| n = 2 | `Z/5 + Z` | 60 | 300 | 9 | 16 | **0** |
| n = 3 | `Z/4 + Z/4 + Z` | 12 | 192 | 31 | 0 | **0** |
| n = 4 | `Z/3 + Z/15 + Z` | 60 | 2700 | 89 | 976 | **12 800 on 64 loci**, signs `{1: 6400, −1: 6400}` |

*Kill:* **any mismatch voids the arc.** The adaptation would then be wrong and no sister number may
be reported.

**C2 — THE CENSUS ON THE SISTER'S TOWER.** Run the same driver on `b+-(LR)ⁿ`, `n = 2, 3, 4`
(further levels if they are cheap; the reached level is stated).

**C3 — THE PREDICTIONS, stated before the data.**
- *Predicted:* **the number of generation-shaped backgrounds DIFFERS** from the object's tower
  level-for-level — xB026 showed the loci, `H₁` and `N` all move.
- *Predicted:* **wherever anything fires, the count is still `|1|`** — never 2, never 3. Ground:
  B1375's own mechanism, `h¹(χ²) = 1` at **every** locus on **every** published level, which bounds
  `|I| ≤ 1`; nothing in it is special to `m004`.
- **BINDING KILL CONDITION, and the one that would matter:** **if any generation-shaped background
  on the sister's tower carries `|count| ≠ 1` — in particular 3 — that is the arc's headline and
  must be reported as such, whatever it does to the tidiness of the picture.**

**C4 — WHAT THE ANSWER MEANS, written before the data.**
- If the sister's count is also uniformly **one**: **`one` is the invariant, the generation count is
  STABILISER-FIXED like volume and the trace field, and "three generations is not derivable from
  this object" becomes theorem-shaped rather than vague.**
- If it is not: **the count is ORBIT-STRUCTURED like `CS` and `H₁`, and the family rather than the
  object is where three could live.**
- **`h¹(χ²)` must be reported for every locus on the sister's tower**, since that is the mechanism;
  a level where it exceeds 1 is the only place a count above 1 could come from.

## Controls required

- **C1 is absolute.** No sister number is reported unless C1 reproduces exactly.
- **Every non-zero index re-checked over the driver's two further primes**, as the borrowed code
  already does; the spurious-locus count is reported as it reports it.
- **Every failure counted, never swallowed.**
- **Provenance header on every borrowed file**, naming lane, commit and author seat.

## What this arc may NOT do

It may not claim three generations or promote any count to physics. It may not re-derive the SM
frame — it **uses** the lane's frame and says so. It may not present borrowed code as this seat's.
**It supplies no value.**
