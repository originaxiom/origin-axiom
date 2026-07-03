# B388 (W3.i) — BANKED: the registered KILL + the coarsening structure

**Status: banked (frontier). Pre-registration: PREREGISTRATION.md (committed first; C0–C3
all tested, all fail — the kill clause requires the exact mismatch structure, below).
Firewalled.**

## The kill

No transport law of the registered forms exists: C0 (identity), C1 (affine relabel +
character), C3 (the ζ₉→ζ₃ specialization + affine relabel + congruence-class character) all
fail — verified exhaustively over all affine maps u·a+v (u ∈ (ℤ/12)ˣ) and all character
assignments on {const, mod 2, mod 3, mod 4} classes (transport_law.json).

## Why (the structure that forbids it — each fact exact from the banked tables)

1. **c₁ ≡ 0**: the level-45 m=2 singles carry NO c₁-component anywhere — only the c₂ slot
   of the ζ₉⁺ basis is populated.
2. **The bare block takes exactly TWO values**, determined by a mod 3: (1/24, −1/24) at
   a ≡ 1 (mod 3), else (5/48, 1/48).
3. **The c₂-block is supported on even a only**, is ODD under the half-period a → a+6
   (c₂(a+6) = −c₂(a)) with magnitude pattern (1,2,1)·(1/48, −1/48) over {0,2,4} — the same
   ℤ₂ half-period structure as the B385 anti-tables and the B386 parity branches.
4. Level-15's m=2 singles take FIVE distinct values (plus a zero at a=6); level-45's data
   is strictly coarser (two bare values, one signed c₂ ladder, no zeros) — **no bijective
   relabel can exist. The m=2 single-seed structure COARSENS up the tower, while the m=1
   single transports identically (PR #484): the two seeds have opposite level behavior.**

**Provenance.** transport_law.py (exhaustive candidate scan) + the comparison table (in
transport_law.json / this file); source data banked+locked (E16, t2_level15_singles).
Locks: tests/test_b388_transport.py.
