# Card W-F9: the order at the scar (V against V*): derived, or irreducible?

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free), by hand with a computed check. **Committed before any
work of it.** It serves the foundations' goal (status file, ruling of 2026-11-14).

## Why this card

W-C8 part 4's page leaves the order at the scar (V against V*) open. The SM seat's candidate system calls it the one
free bit every route ends in. SM-C8 found that the partner relation carries the order and does not choose it. The
question here: is the order fixed by any line of the system, or by any symmetry, or is it irreducible?

## The claims to test

1. **Duality permutes the record's modules.** The dual of V(ℓ, α) = [[α, cβ], [0, β]] (β = α/ℓ, c(λ) = 1) is the
   record module V(ℓ, ℓα⁻¹), so duality is an involution on the record set.
2. **The index is odd under it.** I(V) = n(V) − n(V*) changes sign, so the census is balanced at every orientable
   level.
3. **By hand:**
   - twisted Poincaré–Lefschetz duality gives n(V*) = n²(V), the rank of H²_c(V) → H²(V), so I(V) = n¹(V) − n²(V);
   - every automorphism of the group that keeps the peripheral subgroup, the mirror included, preserves n and so I.
   - So the order is the degree in which the frame reads matter. No symmetry fixes it, and no clause invariant under
     duality fixes it.

## Method

- Own code, exact ranks over a prime field: the record modules at golden levels 4, 6 and 8 and bronze level 2.
- Computed:
  - (h⁰, h¹, n) of V* against V(ℓ, ℓα⁻¹);
  - I on both members of each dual pair;
  - a plant, the wrong partner V(ℓ, α⁻¹).
- Expectations in the script's header, sha256 recorded, committed and pushed before the one run.
