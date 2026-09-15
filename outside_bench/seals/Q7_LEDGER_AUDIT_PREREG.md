# SEAL — THE Q7 HYPOTHESIS-LEDGER AUDIT: a row that left the tally, and two fields called K

**Sealed 2026-08-31, pushed BEFORE the instrument is written or run.**
This is an audit of **this bench's own chain** (memos 160 / 161 / 162), not of main.

## 0. What prompted it

Reading the ledger to answer *"how do we proceed"*, two things surfaced. Both are **stated here as
what I noticed, not as findings** — the cell decides.

**(a) A hypothesis row is in one tally and not the other.** Memo 160's certificate types the five
Kneser–Platonov hypotheses as:

> simply connected · **ℚ-simple** · `H(ℝ)` non-compact · the stabilizer *is* a form of Spin(8) ·
> orbit count = class set

Memo 162 §3 tallies "four of five" over a different five:

> `H(ℝ)` non-compact · stabilizer algebra is D₄ · **the object's own pair is regular** ·
> simply connected · orbit count = class set

**`ℚ-simple` is in the first and not the second.** What occupies its slot is *pair regularity* — a
real result (`B969`), but **not a hypothesis of the theorem**. The count stayed at five.

**(b) `ℚ-simple` was never closed, only conditioned.** Memo 160 types it `HOLDS-CONDITIONALLY`, on
the twist being **outer**. Memo 162 computed that the three 8s are **inequivalent as
representations** (commutant 12, not 18). That is the algebra's action on the 27. *Outerness is a
statement about a Galois action on the Dynkin diagram.* Whether the first discharges the second is
exactly what has not been checked.

**(c) And memo 161's `S3-SIMPLE` is weaker than the word "simple".** Its test is: no basis element
has centraliser dimension ≥ 14, *"which a whole g2 factor would force"*. That is a **necessary
condition against one named alternative**, not a proof that the algebra has no proper ideal. It is
recorded in memo 161 as **SIMPLE**.

**(d) Two different fields are both called `K`.** Route A's classifying cubic is
`K = ℚ[x]/(x³−12x−5)`, totally real, S₃ (`B1093`, memo 160 R-1). `B575`'s basis — where memos 161
and 162 do all their arithmetic — writes `K` for **ℚ(√−3)**, the object's trace field. Strong
approximation over ℚ and over ℚ(√−3) are different statements, and the integral orbit count is over
**ℤ** in one and **ℤ[ω]** in the other. `B1002` banked the standing rule for this exact shape:
*any future arc using the word must say which.*

## 1. Cells

### A — **THE CENTROID.** Is the stabilizer *central* simple, or a Weil restriction?

The discriminator memo 161 needed and did not have. For a Lie algebra 𝔥 over a field F, the
**centroid** is `Γ(𝔥) = {T ∈ End_F(𝔥) : T[x,y] = [Tx,y] = [x,Ty] ∀ x,y}`. Scalars always lie in it,
so `dim_F Γ ≥ 1`, and:

| `dim_F Γ` | what 𝔥 is |
|---|---|
| **1** | **central** over F — rules out **both** `𝔤₂ ⊕ 𝔤₂` **and** `Res_{L/F}(𝔤₂)` in one computation |
| **2** | either `𝔤₂ ⊕ 𝔤₂` (Γ = F × F) or `Res_{L/F}(𝔤₂)` for L/F quadratic (Γ = L) |

**This matters because `Res_{L/F}(𝔤₂)` has F-dimension 28 and generic centraliser F-dimension 4 and
has no proper F-ideal** — it passes *every* test memo 161 ran, including `S3-SIMPLE`. It is the
alternative that was never excluded.

- **A-CENTRAL** (`dim Γ = 1`) vs **A-NONCENTRAL** (`dim Γ ≥ 2`).
- Also computed: the **Killing form rank** (Cartan's criterion — nondegenerate ⟹ semisimple).
- **Method and its direction of rigour, declared now:** the exact system is 784 unknowns; nullity is
  bounded **modulo two primes**, and *reduction can only drop rank*, so `nullity_p ≥ nullity_F` and a
  modular **1** PROVES `dim_F Γ ≤ 1`, hence `= 1`. The elimination never needs the equality — the
  same logic memo 162 used and marked. **Any equality claim is INFERENCE, not computation, and will
  be labelled.**

### B — **THE BASE FIELD.** Over which field does the chain actually run?
Computed, not argued: how many entries of `B575`'s `E6_BASIS` have a nonzero √−3 component. If
**zero**, the e₆ and every subalgebra of it are defined over **ℚ** and the memos transfer to Route
A's arena without comment. If **nonzero**, memos 161/162 computed over ℚ(√−3) and Route A's orbit
problem is over ℚ, and **the chain owes a statement it has not made.**
- **B-RATIONAL** vs **B-TWO-FIELDS**.

### C — **THE LEDGER.** Restore the tally.
Rebuild the five Kneser–Platonov rows with each one's *actual* current status and the arc or memo
that closed it. **C-RESTORE** (the row is missing and the tally needs repair) vs **C-INTACT** (the
substitution is defensible and I have misread it).

## 2. Declared priors — recorded before running

- **A-CENTRAL.** Memo 162's triality decomposition (`8v`, `8s`, `8c` inequivalent) is 𝔰𝔬(8)-shaped,
  and I expect the centroid to be trivial. **If it returns A-NONCENTRAL, memos 161 and 162 both
  need correction and Q7 loses its group identification** — that outcome is named here so it cannot
  be softened later.
- **B-TWO-FIELDS.** I expect `B575`'s basis to genuinely use √−3.
- **C-RESTORE.**

## 3. Fences

- **This audits my own chain.** Any defect found is a **bench error**, filed at the point of
  occurrence, not a charge against main or against `B575`/`B969`/`B904`, whose results are cited and
  not re-derived.
- **Nothing here can make Route A cross.** `B990`'s declared **unfavourable** prior stands
  unrepudiated whatever A returns, and hypothesis 5 (orbit count = class set) is untouched by every
  cell above.
- A **Lie algebra is not a group scheme**; memo 161's fence stands and this cell does not lift it.
- Gate 5 untouched: exact arithmetic and modular reduction, no measured value.
