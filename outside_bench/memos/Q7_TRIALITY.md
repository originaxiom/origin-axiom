# MEMO 162 — THE GROUP IS Spin(8): Q7 GOES TO FOUR OF FIVE

**Banked 2026-08-30.** Seal `seals/Q7_TRIALITY_PREREG.md`, pushed before computing.
Certificate `certificates/q7_triality.py`; output vendored.

**`SUMMARY: T1-THREE | T2-TRIALITY`** — and **`T3-PINNED`**, against a declared prior of
`T3-UNPINNED`.

---

## 1. THE 27 DECOMPOSES AS THE TRIALITY PATTERN

Memo 161 fenced its own result: *"a Lie algebra is not a group scheme — `𝔰𝔬(8)` is compatible with
Spin(8), SO(8) and PGO(8), and only the simply connected Spin(8) gives strong approximation."*
That fence is now discharged, by representation theory rather than by argument.

| cell | result |
|---|---|
| **T-1** | `dim {v ∈ 27 : 𝔰·v = 0} = 3`, **exact over ℚ(√−3)** — three singlets |
| **T-2** | commutant dim = **12** at `p = 100003` **and** `p = 1000003` (rank 717 of 729, both) |

**12 is the triality signature and 18 is not.** Three singlets plus three **inequivalent** 8s gives
`3² + 1 + 1 + 1 = 12`; three **equivalent** copies of `8v` — the SO(8) reading — gives
`3² + 3² = 18`. So the 27 breaks as

> **`27 = 1 + 1 + 1 + 8v + 8s + 8c`**

and `8s`, `8c` are the **spin** representations: they exist for **Spin(8)** and **not** for SO(8).

**The modular method is rigorous in the direction used.** Reduction can only *drop* rank, so
`nullity_p ≥ nullity_ℚ`; a modular **12 proves `nullity_ℚ ≤ 12`**, which **rules out 18 outright**.
That the value *equals* 12 is inference, not computation, and is labelled so — but the elimination
never needed the equality: it needed 18 excluded.

**⇒ the acting group is the simply connected form, `Spin(8)` — the hypothesis strong approximation
requires.**

---

## 2. T-3 — THE PAIR IS PINNED, AND MY PRIOR WAS WRONG

I sealed **T3-UNPINNED**, expecting the record to fix only the integral *frame*. It fixes the pair.

**`B969`: "THE OBJECT'S CANONICAL PAIR RETURNS K"** — *"pair source chosen **before** computing: the
vacuum 3-block"*, instrument the pencil norm `N(sA+tB)` whose splitting algebra **is** the cubic
étale algebra. **Verified 3 for 3**, all three pencil cubics **irreducible over ℚ** with squarefree
kernel `{7, 11}`.

And the connective tissue is exact: **`μ = s³ − 12s − 5` is K's own defining polynomial**, with
`disc(μ) = 6237 = 3⁴·7·11` — the same K Route A turns on, **reached from the object's vacuum block
rather than assumed**.

**What that buys, stated as my inference with the reasoning visible:** a pair whose pencil cubic is
irreducible with non-zero discriminant has **étale** splitting algebra, hence lies in the
**regular** stratum of the Kato–Yukie classification. **So memo 161's generic stabilizer result
applies to the object's own pair**, not merely to a random one. The gap memo 161 flagged in its own
fence closes — **from banked material neither memo had cited.**

---

## 3. WHERE Q7 NOW STANDS — four of five

| hypothesis | state | by |
|---|---|---|
| `H(ℝ)` non-compact | **CLOSED** | `B904` — split Zorn octonions ⟹ split Spin(8) |
| stabilizer algebra is D₄ | **CLOSED** | memo 161 — dim 28 by construction, rank 4, **simple** |
| the object's own pair is regular | **CLOSED** | `B969` — étale pencil cubic returning K |
| the group is **simply connected** | **CLOSED** | **this memo** — triality, `8s`+`8c` present |
| orbit count = the class set | **OPEN** | the Borel–Serre / Bhargava bijection |

**One hypothesis remains, and it is the genuinely specialist one.**

> **[SUPERSEDED 2026-08-31 by memo 167 — this table is not the theorem's hypothesis list.]** It lists
> *the object's own pair is regular* as a hypothesis; it is not one (it is what licenses applying a
> **generic** stabilizer result to the object's own pair, and belongs under the identification row).
> In its slot, **`ℚ-simple` is missing** — a genuine Kneser–Platonov hypothesis, typed
> `HOLDS-CONDITIONALLY` in memo 160 and never closed here. Memo 167 **closes it by computation**
> (centroid dim 1 at two primes, Killing form rank 28/28 ⟹ central simple ⟹ absolutely simple ⟹
> ℚ-simple) and **repairs the table**. The count **four of five stands**; two of its four rows did
> not. Repaired table: `THE_GATE_SENDS.md` addendum 5.

---

## 4. THE FENCES — and they bind harder now, not less

This is the point in a line of work where over-claiming becomes easy, so the seal's clauses are
restated rather than assumed:

1. **This does not cross Route A.** Four of five is not five of five, and the fifth is not a
   formality — it is the bijection the whole count rests on.
2. **`B990`'s UNFAVOURABLE prior stands unrepudiated.** It was stated *with a reason*: homogeneity
   has won every previous time in this record. Nothing here touches that reason.
3. **Identifying the acting group over ℚ is still not a statement about the INTEGRAL group scheme
   over ℤ**, which is what a class-set argument finally needs. **Named in the seal precisely so it
   could not be skipped here, and it is not skipped.**
4. **Even a full crossing yields a direction, never a value** — `B991`'s normalisation no-go is
   untouched, and the SM's numbers stay where nine proved negatives put them.

## 5. WHAT TO DO WITH IT

**Q7 should now be rewritten and is worth sending.** The ask has become a single narrow question
with four hypotheses discharged and the fifth named:

> *The stabilizer of the object's regular pair is a trialitarian **Spin(8)** — computed: the 27
> breaks `1+1+1+8v+8s+8c`, so the spin representations are present — over **split** octonions, with
> `K = ℚ[x]/(x³−12x−5)` totally real, `Gal = S₃`, `h(K) = 1` and every classical obstruction proved
> absent. **Does the count of `G(ℤ)`-orbits inside the `G(ℚ)`-orbit equal this stabilizer's class
> set — and is that class set trivial by strong approximation?***

That is answerable by someone who knows the area, in a sitting. **Not sent — the send is the
owner's act.**

**Gate 5 clean throughout.** Exact linear algebra over ℚ(√−3); finite fields used only where the
seal declared them and only in the direction that is rigorous.
