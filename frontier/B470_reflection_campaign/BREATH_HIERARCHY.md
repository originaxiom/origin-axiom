# B470 — the breath hierarchy: Chat-2's naming flag adopted, the relations certified, two corrections

**Banked 2026-07-08 (the pre-banking naming pass Chat-2 requested — adopted BEFORE RF1's
"the whole chain breathes" could collide with itself). Everything verified in-session;
scripts in this directory. Firewalled.**

## The three breaths, named (the campaign's vocabulary from here on)

- **root-breath**: the monodromy has an INTEGER det = −1 square root — the Gieseking
  floor exists. The FULL test is two conditions: tr(B) − 2 = t² AND t | (B − I)
  entrywise (X = (B−I)/t by Cayley–Hamilton). The trace test alone is NOT sufficient.
- **mirror-breath**: amphichirality of the bundle (CS = 0; orientation-reversing
  self-isometry). The word-level reverse+swap criterion is SUFFICIENT ONLY (see below).
- **residue-breath**: the quantum determinant det(Par·W(word)) = −ω^{#L−#R} — frozen
  at −1 iff the word is balanced; Pisano-8 rhythm otherwise (RF3, verified exactly).

## The hierarchy — certified with strictness witnesses at every step

**root ⟹ mirror ⟹ (word-mirror ⟹) balanced ⟹ frozen residue**

| implication | proof | strictness witness |
|---|---|---|
| root ⟹ mirror | the orientation double cover's deck involution is orientation-reversing (one line, geometric) | **aba** (mirror: CS = 0; rootless: 37 not a square) |
| word-mirror ⟹ balanced | revswap swaps letter counts, rotation preserves them (one line) + 0 violations in 1407 cyclic classes | **RRRLLRLL** (balanced; manifold-CHIRAL: CS = −0.0012159, its revswap partner at +0.0012159 — a genuine mirror pair) |
| balanced ⟹ frozen residue | det decomposition (B468): det = −ω^{#L−#R} | letter-tower rungs (unbalanced, Pisano-oscillating residue) |

**Chat-2's unified theorem endorsed and banked**: the letter-tower is chiral BECAUSE its
Fibonacci imbalance −F_{n−2} ≠ 0 (imbalance ⟹ residue oscillation ⟹ not word-mirror);
the body-chain's letters are balanced palindromes, freezing everything above. RF1 + RF3
= one mechanism (fewer facts, more law — the naming paid for itself within the hour).

## Two corrections to Chat-2's ten-minute run (verify-don't-trust, again)

1. **The "52 counterexamples" were ~96% contaminated**: their root test used the trace
   condition alone. With the full integrality test, exactly **2** cyclic classes at
   length ≤ 13 are genuinely rooted-but-not-word-mirror: **LLLRLLRRRLRR and
   LLLRRLRRRLLR** (trace 146, t = 12) — and BOTH are certified amphichiral (CS = 0 to
   1e-15, vol 10.0235284, an isometric pair) with homology torsion **(ℤ/12)²** — the
   root's square trace surfacing as SQUARE homology (noted: rooted bundles carry
   (ℤ/t)²-shaped torsion; the metallic letters' m² likewise). The corrected finding is
   SHARPER: the word criterion is strictly weaker than mirror-breath, witnessed by an
   exact pair, and root ⟹ mirror is confirmed geometrically on the witnesses.
2. **The chain has TWO roots, not one**: s₀ = b (u₀ − 2 = 4 = 2²) as well as s₁ = a.
   The alphabet IS the root locus — both letters are rooted, and **no composite chain
   word is: rungs 2–200 all certified rootless by mod-p QNR** (exact traces are
   infeasible past rung ~40 — 10¹²-digit numbers; the mod-p route is the honest one).

## Tooling caveat (recorded)

SnapPy's `is_isometric_to` against a `reverse_orientation()` copy returned True for the
manifestly chiral RRRLLRLL (CS ≠ 0) — the test as invoked is orientation-blind.
**Chirality verdicts in this campaign rest on CS** (0 to 1e-15 vs ≠ 0 at 1e-3 scale),
with the root argument as the structural certificate.

## Composition (Chat-2's second axis, endorsed as stated)

Balance composes always (counts add); mirror composes on palindromic alphabets (the
banked one-liner — any word in metallic letters is word-mirror); **root composes never
beyond the letters** (certified to rung 200). The metallic family is the alphabet
because roots live on letters: the family is finite because the deepest breath does not
propagate — only its shadows (mirror, balance, frozen residue) ride the chain.

## Phase-2b reframe (endorsed, preregistered by Chat-2's message)

The σ-parity column should ALIGN with the mirror column (σ-even = conjugation-stable =
CS ∈ {0, ½}); any split object is the ledger's most interesting entry. The
thermodynamic reading (breaths as order parameters, temperature killing them
top-down, rarest first) is S-room material with a preregistrable prediction for the
warm campaign — recorded, HELD naming.

## Reproduce
```
python3 hierarchy_verify.py   # the full certification (words <= 13, chain to 200, witnesses)
```
