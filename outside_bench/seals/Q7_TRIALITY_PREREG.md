# SEAL — Q7: THE TRIALITY TEST (the group scheme), AND THE PAIR SCOUT

**Sealed 2026-08-30, pushed BEFORE any computation.** Follows memo 161.

## 0. The question this decides

Memo 161 identified the stabilizer **Lie algebra** as `𝔰𝔬(8)` and immediately fenced it:
*"a Lie algebra is not a group scheme — `𝔰𝔬(8)` is compatible with **Spin(8), SO(8) and PGO(8)**,
and **only the simply connected Spin(8) gives strong approximation**."*

**That is decidable by representation theory.** Under `Spin(8) ⊂ F₄ ⊂ E₆`:

> `27 = 1 + 1 + 1 + 8v + 8s + 8c`   (3 + 24 = 27)

The **spin** representations `8s` and `8c` are representations of **Spin(8) and not of SO(8)**. So if
the 27 breaks into three **inequivalent** 8s, the group acting is the simply connected form.

## 1. Cells

### T-1 — invariants · **BLIND**
`dim {v ∈ 27 : M·v = 0 ∀ M ∈ 𝔰}`, exact over ℚ(√−3).
- **T1-THREE** (= 3, matching three singlets) vs **T1-OTHER**.

### T-2 — the commutant, and this is the discriminator · **BLIND**
`dim {X ∈ gl(27) : [X, M] = 0 ∀ M ∈ 𝔰}` = `Σ mᵢ²` over the isotypic multiplicities.
- three singlets + three **inequivalent** 8s ⟹ `3² + 1 + 1 + 1 = ` **12** ⟹ **triality ⟹ Spin(8)**
- three singlets + three **equivalent** copies of `8v` ⟹ `3² + 3² = ` **18** ⟹ **SO(8)**

- **T2-TRIALITY** (12) · **T2-VECTOR** (18) · **T2-OTHER** (neither).

**Method fence, stated in advance because it is the cell's one soft spot.** The exact ℚ(√−3)
elimination on a 729-column system is beyond this bench's time budget, so the commutant rank is
computed **modulo primes** `p ≡ 1 (mod 3)` where `√−3` exists. **This is rigorous in the direction
that matters:** reduction can only *drop* rank, so `nullity_p ≥ nullity_ℚ`. **A modular answer of 12
therefore proves `nullity_ℚ ≤ 12`, which rules out 18 outright.** It does **not** by itself prove
the value is exactly 12; that direction is stated as inference, not as computation, and several
primes are run.

### T-3 — the pair scout · **BLIND**
`B990` says *"the pair being already integral in the B854 Chevalley frame."* The scout found `B884`
pins the **frame** (structure constants all ±1), which is not the same as pinning a **vector**.
Search the record for an explicit `(x, y)`.
- **T3-PINNED** — an explicit pair exists; test whether its stabilizer is 28-dimensional.
- **T3-UNPINNED** — the record fixes the integral *frame* but no explicit pair. **Then say so
  plainly**: memo 161 and this cell describe the **generic** pair, and either Q7 must be posed
  generically or the record owes a specification. **That is a finding, not a failure.**

## 2. Fences carried forward, unchanged

1. **Even `T2-TRIALITY` does not conclude Route A crosses.** It would close hypothesis 3 of five,
   leaving hypothesis 5 (orbit count = class set) — the genuinely specialist one — untouched.
2. **`B990`'s UNFAVOURABLE prior stands unrepudiated**, and it was stated *with a reason*:
   homogeneity has won every previous time.
3. A representation-theoretic identification of the acting group is still not a statement about the
   **integral** group scheme over ℤ, which is what a class-set argument ultimately needs. **That
   further gap is named here so it cannot be skipped later.**

**Declared prior:** **T1-THREE, T2-TRIALITY, T3-UNPINNED.** If T2 returns 18 the route fails at the
group scheme and that is a clean negative to be reported as one.

## 3. Gate 5
No measured value. Representation theory over ℚ(√−3) and finite fields.
