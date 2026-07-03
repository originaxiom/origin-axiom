# B394 (M2) — BANKED: the registered kill + THE UNIFIED SINGLES LAW

**Status: M2 complete. Prereg committed first (both candidates registered before
computation — both KILLED). Firewalled.**

## The kill (as registered)

The 405 support is a ≡ 31 (mod 45) — TWELVE cells, not four (neither 59 nor 86 mod 135;
the spacing stayed 45 while the cell count tripled). The naive CRT walk rule is dead; the
deeper 3-adic form is the staged residue.

## THE UNIFIED LAW (the kill's reward)

The twelve 405-values form four ζ₉⁺-Galois orbits of the exact triple

    v = (1 + c)/12,   c ∈ {c₁, c₂, c₄} = the ζ₉ + ζ₉⁻¹ conjugates,

(reconstructed (x,y,z) = (1/12, −1/12, −1/12) on the orbit order 31→121→76; the wrong-order
first attempt left only the order-invariant average 1/12 clean — itself the tell). And the
old constant UNIFIES: **1/4 = (1 + 2)/12** — the degenerate orbit c = 2. Two exact
invariants across all four levels (15, 45, 135, 405):

- **the sum rule: Σ_support singles = 1** (4 × 1/4 = 1; 12 × avg = 12 × 1/12 = 1);
- **the value form: (1 + c)/12** with c walking down the cyclotomic tower (c = 2 through
  level 135; the ζ₉⁺ orbit opens at 405, where the 3-side hits depth 4).

This AMENDS W5's P-SCALE verdict: not "the constant is frozen" but "the SUM is frozen and
the value form is (1+c)/12" — the de-rationalization is the home-growth pattern (B372) in
the singles channel. The 1/12 appears a second time in the program, now as the universal
singles normalizer.

**Hygiene banked:** `__main__` guards added to census_big.py and k1_fullfield.py (the
module-level-execution import trap fired twice; imports now 0.08 s).

**Provenance.** singles_405.py (numpy, 2 primes) → singles_405.json; identify_triple.py →
triple.json; locks tests/test_b394_walk.py.
