# Card W-F6: the character-gap law and the normaliser, as theorems

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free): two proofs by hand, each with a computed check.
**Committed before any work of it.** It serves the foundations' goal (status file, ruling of 2026-11-14).

## Why this card

W-C8 part 4's page leaves two items open:
- **Line 5:** the normaliser ±J_mⁿKᵉ was found by search for m = 1 to 5 only, and is open beyond.
- **Part 5, § 2:** at every odd level computed, the number of characters with gap +1, and with −1, equals the fibre
  torsion. Observed, not proved.

## The claims to prove

1. **The gap law.** Let G = F₂ ⋊ ⟨t⟩, with t acting by a hyperbolic automorphism φ of the once-punctured torus's group,
   φ(λ) = gλˢg⁻¹ (s = ±1, the determinant), and μ = g⁻¹t. Then:
   - for a character χ non-trivial on the fibre, h¹(G; χ) = [χ(μ) = s], and the class is non-zero on λ;
   - for a character trivial on the fibre, h¹(G; χ) = [χ trivial].
   - So at s = −1 the characters with gap +1, and those with −1, number exactly the fibre torsion. At s = +1 every
     character's gap is 0, and the record's data number the fibre torsion minus one.
2. **The normaliser.** For every m ≥ 1, the centraliser of J_m = [[m, 1], [1, 0]] in GL(2, ℤ) is ±⟨J_m⟩, and the
   normaliser of ⟨J_m⟩ is {±J_mⁿKᵉ}, K = [[0, 1], [−1, 0]].

## Method

- Proofs by hand, written in the note.
- Computed checks:
  - the law on the golden, silver and bronze ticks and on two non-metallic monodromies, at several levels, with
    t-values both roots of unity and not;
  - the units of ℤ[J_m] in a box, for m = 1 to 60.
- Plants: the law with s replaced by −s; the units with J_m² in place of J_m.
- Expectations in the script's header, sha256 recorded, committed and pushed before the one run.
