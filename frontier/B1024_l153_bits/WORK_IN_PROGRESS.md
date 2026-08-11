# B1024 / L153 — WORK IN PROGRESS: the cell is BLOCKED on a labeling conflict between two of its own sealed inputs

**Date:** 2026-08-11 · **Lane:** MATHEMATICS. Gate 5 untouched.
**This is NOT the cell's report.** No outcome is declared; `FINDINGS.md` and `arc_verdict.json`
are deliberately absent, so the B837 reporting obligation stays open and
`tests/test_b837_file_drawer` stays red. Recording a blocker is not reporting a result.

**Seal status: VERIFIED.** `PREREGISTRATION.md` re-hashed before any compute —
`dc823e86ef7f5c9beed1b0f32b77f69b1c863a46c0eb8fe5ca7a1698098256de`, **byte-identical** to
`ARTIFACT_HASHES.txt`. The method below is the sealed method, unvaried.

---

## 1. What is settled

The sealed method's five inputs all exist with code and `results.json` (B936, B928, B939, B961,
B782). The H¹ machinery reduces cleanly:

- `X = T_ad[2] ≅ (ℤ/2)⁶` on the six E₆ Dynkin nodes; τ acts by the diagram flip
  `{0↔5, 2↔4, 1, 3}`.
- `Z¹ = X^τ` (16), `B¹ = (1+τ)X` (4), `H¹ = (ℤ/2)²`.
- **The class map is explicit** (B936 `Q_A_module`): *"chi |-> (chi at node 1, chi at node 3)
  = (Bourbaki alpha_2, alpha_4)"* — the class of a cocycle is literally its pair of coordinates
  at the two τ-fixed nodes.
- The torsor coordinate of `H(σ_χ∘τ)` is `χ·χ₊` (B936 `Q_A_torsor`).

**Recomputed here from the banked characters** (`CHI_P = (1,−1,1,−1,1,1)`,
`CHI_C = (1,−1,−1,1,−1,1)`, `ALL_MINUS`):

| element | χ | coordinate `χ·χ₊` | H¹ class |
|---|---|---|---|
| `σ_1` | `++++++` | `+-+-++` | **(1,1)** |
| `σ_χ₊` | `+-+-++` | `++++++` | **(0,0)** |
| `σ_χ₋` | `-+-+--` | `------` | **(1,1)** |
| `σ_₋₁` | `------` | `-+-+--` | **(0,0)** |
| **`σ_c`** | `+--+-+` | `++---+` | **(0,1)** |

Two consequences, both reproducing banked statements:

- **K4 = {1, σ_χ₊, σ_χ₋, σ_₋₁} has image of order 2 in H¹** — exactly B936's
  `Q_B.Klein_to_H1 = "kernel {I, D2}, image Z/2 = <[D]>"`. ✔ reproduced independently.
- **The conjugation generator's shadow `σ_c` carries class (0,1)** — nonzero, and **outside**
  K4's image `⟨(1,1)⟩`.

So conjugation contributes a genuine H¹ class, and the outcome now turns entirely on the
**reversal** generator's shadow — which the prereg itself says *"must be constructed if not
banked."*

## 2. THE BLOCKER — B936 and B939 label the shadow map oppositely, and neither declares a convention

The sealed method names **B939's shadow map** as an input: *"σ₋₁→D, σ_χ₋→D₂, σ_c→D_c"*
(B939 FINDINGS, and its verdict line adds the flip counts: *"σ₋₁ → D (12 flips) · σ_χ₋ → **D₂
(the ELEVEN)**"*).

**B936's own construction assigns them the other way round.** `cohom.py` lines 685–687:

```python
coord_D2 = bits(CHI_M)        # (-1) . chi+ = chi-
coord_D  = bits(ALL_MINUS)    # chi- . chi+ = -1
coord_D2D= bits(CHI_P)
```

D is indexed by **coordinate** `ALL_MINUS`, which is the coordinate of the element whose
**character** is `χ₋`. So in character terms **B936 has σ_χ₋ ↦ D**, while **B939 has σ_₋₁ ↦ D**.

**The flip counts confirm the conflict rather than resolving it.** B936's `Q_D_class_table`
gives `D_flips` per character: character `------` (= σ_₋₁) → **11**; character `-+-+--`
(= σ_χ₋) → **12**. B939 states σ_₋₁ has **12** and σ_χ₋ has **11**. **Exactly transposed.**

**The most likely reading — and it is a reading, not a finding — is that the two arcs index the
same elements by different parameters:** B936 by the **torsor coordinate** `χ·χ₊`, B939 by the
**character** `χ`. Under that reading both are internally correct and the labels simply collide.
**Neither arc states which parameter its names refer to.**

**Why this blocks the cell rather than being a footnote.** The shadow map is a *sealed input*.
L153's outcomes are distinguished by **which** H¹ classes the shadows generate, and the two
candidate labelings assign `(0,0)` and `(1,1)` to opposite elements. Resolving it by picking the
reading that produces a tidier answer would be choosing the outcome — precisely what sealing
before compute exists to prevent.

**This is the third undeclared-convention collision this consolidation pass has found** — after
`θ` (three objects: the E₆ fold / the `sl(n)` opposition involution / reversal-contragredient)
and B62-vs-P33 (`B62 = 2 × P33`, full height-±h space vs positive roots). All three are error
class **E1**, which `docs/ERROR_LEDGER.md` already names the programme's most recurrent.

## 3. What the cell needs before it can report

1. **Settle the labeling from the code, not the prose** — determine whether B939's `assembly.py`
   builds its σ's by character or by torsor coordinate, and record the answer as a declared
   convention in both arcs. This is a read of `assembly.py`'s `inner_gmap`/`outer_gmap` call
   sites against `cohom.py`'s `bits()`, not a new computation.
2. **Then construct the reversal generator's shadow** from the banked machinery (B928's torsor
   theorem + B939's map + B961's frame instrument) — the one construction the prereg assigns to
   this cell.
3. **Then read off the two classes and report the sealed outcome** — SAME (deficit 2),
   INDEPENDENT (deficit 4), or PARTIAL (deficit 3) — unsmoothed, per the prereg's own
   instruction that INDEPENDENT *"makes the interface bigger and must be stated as such."*

**Declared prior, unchanged and carried forward:** *"Honest: uncertain, lean SAME … But the lean
is weak: the τ-fixed-node indexing smells intrinsic to the 27, not to the observer.
Non-weakening applies."*

## 4. What is NOT claimed here

- **No outcome.** SAME / INDEPENDENT / PARTIAL is undecided and must stay undecided until step 3.
- **No error attributed to B939.** The conflict may be entirely a naming convention; the arcs'
  mathematics is not challenged. What is established is that **the two cannot both be read
  literally**, and that L153 cannot proceed until one reading is fixed *on the record*.
- **Nothing about the input count.** Whether the frame classes are new discrete inputs is exactly
  what this cell is for, and it has not answered.
