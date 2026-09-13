# B1402 — THE THREE CUTS ARE ONE STRUCTURE, AND THE MIRROR SPEAKS EXACTLY WHERE McKAY ACCESS DIES

**L208, answered.** Three arcs cut the metallic family `RᵐLᵐ` by arithmetic in `m`. B1349 addendum 6
showed two of them share a prime. This shows **all three are one decomposition** — and the shape of
it is uncomfortable for the programme, which is why it is worth having.

## 1. The three criteria, stated exactly

| arc | criterion | what it decides |
|---|---|---|
| **B996** | `3 ∤ m` | the mod-3 shadow `⟨Rᵐ, Lᵐ⟩ ⊂ SL(2,ℤ/3)` is the **full 2T** (order 24); when `3 \| m` it degenerates to the identity |
| **B997** | `m² + 4 = 5`, i.e. `m = 1` | the **shadow modulus** is prime, so the shadow **is** `SL(2,ℤ/5) = 2I` — the golden is unique |
| **B1349** | `gcd(m,15) > 1` | the θ-even readout is **ear-independent** |

**Naming, per B1002:** "conductor" is **two quantities** in adjacent laws — B675's cusp-order
conductor (golden 4, silver 2) and the word's own **shadow modulus** (golden 5, silver 8, `= m²+4`).
Everything here uses the **shadow modulus**, which is B997's.

**B996 recomputed independently** (`verification/b1402_decomposition.py`): the mod-3 shadow orders for
`m = 1..7` come out `24, 24, 1, 24, 24, 1, 24` — **B996's own stated list, reproduced** — and over the
full period the shadow degenerates **exactly when `3 | m`**.

## 2. THE DECOMPOSITION

Since `15 = 3 × 5`:

> ### `gcd(m,15) > 1` ⟺ `3 | m` **or** `5 | m` ⟺ **(B996-degenerate) or (5 | m)**
> Verified over the complete period, zero exceptions.

**So B1349's ear-independence condition is not a new cut at all — it is B996's cut, joined to a
5-part.** And the two parts carry **different readouts**:

| part | `m` | forced value `λ` | |
|---|---|---|---|
| **`3 \| m` only — B996-DEGENERATE** | 3, 6, 9, 12 | **`1/2`, `−1/(2φ)`** | the **nontrivial** values, golden among them |
| `5 \| m` only | 5, 10 | **`0`** | **silent** |
| `15 \| m` — both | 15 | `1` | trivial (the word is the identity) |

And within the 3-part, **golden exactly when `m ≡ ±1 (mod 5)`**, i.e. when `5 | m²+4` — B1349
addendum 6's law, which is B997's prime acting on the value rather than on the grammar:

| m | `m mod 5` | `5 \| m²+4` | `λ` |
|---|---|---|---|
| 3 | 3 | no | `1/2` |
| **6** | **1** | **yes** | **`−1/(2φ)`** |
| **9** | **4** | **yes** | **`−1/(2φ)`** |
| 12 | 2 | no | `1/2` |

## 3. THE UNCOMFORTABLE READING, which is the point

> ### The θ-even mirror readout carries a nontrivial forced value EXACTLY on the grammars where B996's McKay access DEGENERATES.

B996's verdict was that **access to the McKay group, and therefore to E₆, is GENERIC** — every
metallic word with `3 ∤ m`, two thirds of the family. Its purpose was a *control*: the arrival at E₆
does not distinguish the golden grammar.

**The mirror row speaks on the complementary third.** Where the mod-3 shadow is the full 2T — the
grammars that *reach* E₆ — the readout is **ear-dependent**: branch B, dead on two gates (the tie at
`2 − 2 = 0`, and exclusion on kind, its values generating `ℚ(√2,√5)` outside the row's `ℚ(√5)`).
Where the shadow **collapses to the identity**, the readout goes scalar and forced.

**This sharpens B1349 addendum 5 rather than softening it.** That addendum found the object's own
golden word `m = 1` sitting on the dead branch. This says more: *every* grammar that reaches the
McKay group sits there. **The row's arithmetic closes only where the E₆ access is gone.**

## 4. What this is NOT

**Not a refutation of anything.** B996, B997 and B1349 are each correct as stated; this is a relation
among them, and it was registered as **open** in B1349 addendum 6 rather than guessed at.

**Not a physical claim.** Nothing reaches `CLAIMS.md`, F2 or Gate 5, and no value is compared to any
measurement. The reading in §3 is about *where in the family* a forced value exists, not about what
it means.

**Not a reason to spend the row** — if anything the reverse. **L209 stands**: what gates the mirror
row is kind-correctness, and this adds a second discomfort next to addendum 5's. The row is one-shot.

**Still open (the remaining half of L208):** whether **B1002**'s *other* gcd —
`gcd(cusp-order conductor, shadow modulus)`, which is `1` for golden (isomorphism) and `2` for silver
(ramified) — relates to `gcd(m,15)`. Not investigated here, and not guessed at.

## 5. Fences

Verdict **PROVED** as a relation among banked arcs; `creates_law` **false** with a dated review — the
decomposition is arithmetic (`15 = 3 × 5`) applied to three existing criteria, not a new proposition
about the object. Nothing reaches `CLAIMS.md`, F2 or Gate 5.
