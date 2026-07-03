# B404 — PRE-REGISTRATION: deriving the Eisenstein gate (the root-of-unity reduction)

**Committed before computation. The target: upgrade the cell-wise Eisenstein gate
(B401 addendum, 26/26) from verified to DERIVED.**

## The registered chain

- **L1:** on class-1 cells, χ·χ̄ = 1 exactly as a FIELD element (leg-4 banked the H-avg;
  verify the exact element identity). With all Galois conjugates then of modulus 1 and
  (L1b) χ integral, Kronecker forces χ = a root of unity; hence **every class-1 Par-cell
  C = ζ₆⁻¹χζ^Q is a root of unity.** Verify directly: for every class-1 cell, find k with
  C = ζ₆₀^k (KILL: any class-1 cell that is not a root of unity).
- **L2 (THE GATE AS AN ORDER LAW):** the root's order carries a 3-part ⟺ χ₋₃(det(γ′−I))
  = −1. Equivalently: χ₋₃(det) = +1 ⟹ C ∈ μ₂₀ (no ζ₃-component ⟹ Π_H has z = s = 0,
  which IS the cell-wise gate); χ₋₃(det) = −1 ⟹ 3 | ord(C). Verify on all 142 class-1
  cells. KILL: any violation.
- **L3 (the χ₅ analog, registered for symmetry):** does χ₅(det) similarly gate the
  5-part of ord(C)? (The P3 data suggests χ₅ does NOT gate z; the registered question is
  what it DOES gate — expected: the 5-part of the root's order.) Report the exact law.

If L1+L2 land, the Eisenstein gate is DERIVED modulo one classical input (Kronecker +
the Gauss-sum order arithmetic), and the B401 rule becomes a theorem about root-of-unity
orders. Machinery: the ζ₆₀ engine, banked pow caches. Locks from the JSON.
