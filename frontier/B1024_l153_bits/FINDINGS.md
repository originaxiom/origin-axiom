# B1024 — L153: the torsor bits ARE the frame bits. **SAME, deficit 2.** And the shadow map's prose was transposed.

**Date:** 2026-08-11 · **Lane:** MATHEMATICS, exact. Gate 5 untouched; zero anchors; no measured
value; nothing to `CLAIMS.md`.
**Seal:** `PREREGISTRATION.md` sha-256 `dc823e86ef7f5c9beed1b0f32b77f69b1c863a46c0eb8fe5ca7a1698098256de`,
**re-verified byte-identical before any compute**. The sealed method was followed unvaried.
**Files:** `compute.py` → `results.json` · lock `tests/test_b1024_l153.py` (7 locks).

---

## THE SEALED OUTCOME: **SAME (deficit 2)**

> **The two torsor generators' 27-shadows generate H¹(⟨τ⟩, T_ad[2]) = (ℤ/2)².**
> **Conjugation → class (0,1). Reversal → class (1,1). Together they span.**
>
> **The frame bits ARE the torsor bits in a second presentation.** R11's T1 tightens to
> **d = 2**, and **the counted input list stands** — the frame classes are not new discrete
> inputs.

**The declared prior was "uncertain, lean SAME", and SAME is what fired.** Per the
non-weakening rule that is worth *less* than a result against prior, and it is recorded as such.

## What was computed

All from banked artifacts, with the class map applied independently rather than read off:

- **The class map, verbatim from B936** (`Q_A_module`): *"chi |-> (chi at node 1, chi at node 3)
  = (Bourbaki alpha_2, alpha_4)"* — a cocycle's class is its pair of coordinates at the two
  τ-fixed Dynkin nodes. The torsor coordinate of `H(σ_χ∘τ)` is `χ·χ₊` (`Q_A_torsor`).
- **Reproduction check first:** our independent map reproduces **all 16** rows of B936's own
  `Q_D_class_table` from `χ` alone. If it had not, the rest would be measuring a different object.
- **K4's image is order 2** — reproducing B936's `Q_B` string *"kernel {I, D2}, image Z/2 =
  <[D]>"* from scratch.

| generator | χ | shadow | coordinate | **H¹ class** |
|---|---|---|---|---|
| **conjugation** | `+--+-+` | `D_c` (B939, banked) | `001110` | **(0,1)** |
| **reversal** | `++++++` | `τ`, the 27↔27̄ contragredient (**constructed here**) | `010100` | **(1,1)** |

`(0,1)` and `(1,1)` are independent over 𝔽₂, so the span is all four classes.

**The vacuity control (MB12), and it is not decorative:** *not* every set of census elements
spans. **The wall Klein K4 = {1, σ_χ₊, σ_χ₋, σ_₋₁} has image of order 2** — four elements
spanning only ℤ/2. So "generates (ℤ/2)²" is a condition that can fail, and there is a banked
witness that it does.

## The one construction this cell owed, and its load-bearing step

The prereg assigns exactly one construction: *"the reversal generator's shadow must be
constructed if not banked … from the banked machinery, not assumed."*

**The construction, in one line:** THE CHAIN's **C21** defines reversal exactly — *"the
θ-involution (the 27↔27̄ contragredient `g↦g⁻¹`)"* — and on e₆ the 27↔27̄ exchange **is** the
diagram automorphism, which is precisely the τ B936 takes cohomology of (`Q_A_group`: *"tau
acting by the E6 diagram flip"*). So reversal's image under the shadow map is the **outer
generator itself**, the census element at trivial character. It is one of the sixteen already
classified, so its class is read off the same map — which is why the construction is short.

> **This identification is the cell's single inferential step, and it decides the outcome.**
> If reversal's shadow were instead a census element of class `(0,0)` or `(0,1)`, the span would
> collapse to ℤ/2 and the outcome would be **PARTIAL (deficit 3)**. The step rests on C21's own
> definition of reversal plus the standard fact that 27↔27̄ on e₆ is the diagram flip. **It is
> not a computation, and it is flagged here rather than buried** — a reader who rejects the
> identification should read this cell as undecided, not as SAME.

## THE BLOCKER THIS CELL HAD TO CLEAR FIRST — B939's shadow-map prose is transposed

The sealed method names B939's shadow map as an input. Its FINDINGS prose reads:

> *"σ₋₁ → D (12 flips) · σ_χ₋ → **D₂ (the ELEVEN)**"*

**B939's own code builds its σ's by CHARACTER** — `g_sm1 = inner_gmap(ALL_MINUS)` — and **B936's
class table records `D_flips` per character**: character `ALL_MINUS` carries **11** flips (D₂'s
count), character `χ₋` carries **12** (D's count). **Exactly the reverse of the prose.** B936's
`Q_B` coordinates agree with the character reading: `D_coordinate` is the coordinate of `χ₋`,
`D2_coordinate` that of `ALL_MINUS`.

**So the corrected shadow map, by character, is:**

| | B939 prose | **corrected** |
|---|---|---|
| `σ_χ₋` (χ = `-+-+--`) | → D₂ (11) | **→ D (12 flips), class (1,1)** |
| `σ_₋₁` (χ = `------`) | → D (12) | **→ D₂ (11 flips), class (0,0)** |

**B939's mathematics is untouched** — every one of its checks stands, and its verdict (K4 and
W_frame are distinct subgroups overlapping in one element) does not depend on which name that
element carries. **What is wrong is one prose line**, and it is wrong in a place a later cell
had to consume. Registered as a retraction row rather than a silent correction.

**This is the third undeclared-convention collision the consolidation refresh has found** —
after `θ` naming three distinct objects (B1026) and `B62 = 2 × P33` (full height-±h space vs
positive roots). All three are error class **E1**, which `docs/ERROR_LEDGER.md` already names the
programme's most recurrent, and **all three were found by diffing two surfaces against each
other rather than by reading either one.**

## What this does and does not settle

**Settles:** L153, the cell B1023 registered as pending. The discrete deficit is **d = 2**, not
2 ≤ d ≤ 4. `THE_CLAIM`'s hypothesis line needs no new bits from the frame classes.

**Does not settle — and the distinction matters:** this says the *frame* classes are not new
inputs. It says **nothing** about B787's separate finding that **inversion ι is a fourth
involution independent of ⟨c, θ, γ₅⟩**. Those are different questions: L153 asks whether B936's
H¹ classes are already spanned by the torsor generators (**yes**); B787 asks whether the torsor
itself has a fourth generator (**yes, in the character-variety-native sense, with its status as
a measurement closing unrun**). **A reader must not net them against each other.** The
"unsourced fifth input" argument's premise — *"B766's three torsor bits are all committed, and
there is no fourth"* — is **untouched by this cell** and still carries B787's open question.

**Not claimed:** no novelty (the H¹ machinery is B936's, the class map is B936's, the
contragredient/diagram-flip identity is standard); no physics; no change to any claim's label.

---

**Verdict: PROVED.** The sealed cell ran under its verified seal and returned **SAME
(deficit 2)** with its criterion shown failable; and it corrected a transposed prose line in one
of its own sealed inputs before consuming it.
