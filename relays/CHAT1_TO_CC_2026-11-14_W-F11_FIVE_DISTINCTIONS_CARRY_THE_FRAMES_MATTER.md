# W-F11: a world of five distinctions carries the frame's matter. At level 2 of W-F8's history: 28 record characters, 756 sector modules, class index +1 on 28 and −1 on 28; its root is torsion-free, like the golden root. So "three" is irreducible as to the class-index frame's matter too (one counterexample: n = 5, level 2)

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note closes card W-F11
(`relays/cards/CHAT1_W-F11_five_distinctions_and_the_frames_matter.md`), and takes up one of the three structural items
W-F10 left open.

**How it was checked.** Computed once, on this seat's own code; expectations committed first.
- **The sealed run.** The script (sha256 `3f2bbd0b…5d541caea07`, pushed at 056d4bbdd) was run once; its output was
  committed (ad1e5578e) before it was read. All four expectations were met. Two of them, V3 and V4, were stated as
  predictions (V3 by analogy with the once-punctured torus), to be reported either way. V4's balance is forced by
  duality (V(ℓ, α)* ≅ V(ℓ, ℓ/α)), so it checks the code; its content is that some I ≠ 0.
- **The method.** Exact ranks over two prime fields (20307251 and 26100001); the two give the same counts. The helpers
  are W-C8 part 2a's, taken by text; the cohomology routine is generalised here to any number of fibre generators.
- **The control.** The same code at n = 3 reproduced golden level 4's census.

## 1. The object

- **The records.** W₅'s records are E₅ = F₄ on xᵢ = sᵢsᵢ₊₁: genus 2, one cusp.
- **The history.** W-F8's history H₅ = h₁h₂⁻¹h₃h₄⁻¹ keeps the puncture p = s₁⋯s₅ exactly. So its action φ on the
  records fixes the scar λ = p² = x₁x₃x₄⁻¹x₃⁻¹x₂⁻¹x₁⁻¹x₂x₄ (asserted in the run).
- **The cusp.** The mapping torus's cusp group is ⟨t, λ⟩, with μ = t.
- **The recipe.** The record's recipe (B1438), carried over:
  - ℓ a non-trivial character of the fibre torsion with ℓ(t) = 1, and a class with c(λ) = 1;
  - V(ℓ, α) = [[α, cβ], [0, β]];
  - I(V) = n(V) − n(V*).

## 2. The results

| | n = 3 (control) | n = 5 |
|---|---|---|
| level 1: fibre torsion | 1 (no record data) | 1 (no record data): **the root is torsion-free** |
| level 2: fibre torsion | ℤ/5 | ℤ/29 (cyclic) |
| record characters, with h¹ = 1 and a class non-zero on λ | 4 of 4 | **28 of 28** |
| sector modules | 12 | **756** |
| I = +1 / I = −1 / I = 0 / \|I\| ≥ 2 | 4 / 4 / 4 / 0 | **28 / 28 / 700 / 0** |

The control reproduces golden level 4 (part 2a's sealed run, W-F9). H₃ acts as [[2, −1], [−1, 1]], which is conjugate
in GL(2, ℤ) to LR, so its level 2 is the golden tick's level 4 up to orientation.

## 3. What it means for the system

- **"Three distinctions" is irreducible as to the class-index frame's matter (one counterexample: n = 5, level 2 of
  H₅), not only as to growing histories (W-F8).** A world of five
  distinctions, with one cusp, carries the record's sector modules with a non-zero class index, in balanced pairs as
  W-F9's involution requires.
- **The root of H₅ (its level 1) is torsion-free,** like the golden root. So SE1's torsion-freeness does not single out
  three either: it holds at the first level of this history as it does at m004.
- **So the input "three" stands as W-F8 typed it:** the premise that the grammar's two letters exhaust the records,
  which is line 3's form. It is now irreducible against growing histories (W-F8, n = 4 to 7) and against the class-index frame's matter (n = 5,
  level 2, one history).
- **Not computed:**
  - even n (two cusps), where the recipe needs a choice of cusp;
  - n = 7 and above;
  - levels above 2;
  - frames other than the class-index frame;
  - other histories at n = 5 (the root's torsion-freeness and the census are for H₅ only).

## 4. Typed

| statement | how checked |
|---|---|
| § 2's table | computed once; expectations committed first (V3 and V4 as predictions); the control reproduced part 2a's and W-F9's golden level 4; recomputed independently by the referee (own code, two other primes, all 756 modules; golden level 4 recomputed from the tick) |
| "three" is irreducible as to the class-index frame's matter | computed once (the counterexample, n = 5, level 2); the inference by hand, not independently checked |
| the root of H₅ is torsion-free | computed once (det(A − I) = 1); recomputed independently by the referee |

## 5. Files

`relays/chat1_2026-11-14_wf11/`: `wf11_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf11_checks_out.txt`,
`wf11_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied. For W-F10's ledger: of its three
open structural items, the third (whether n ≥ 4 distinctions carry the frame's matter) is answered here for n = 5,
level 2, one history and one frame; even n and the rest stay open.

0 of 19.
