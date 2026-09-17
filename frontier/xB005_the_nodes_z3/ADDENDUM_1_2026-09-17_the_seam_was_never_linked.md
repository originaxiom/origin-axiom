# xB005 ADDENDUM 1 (2026-09-17) — Q3 WAS A FALSE NEGATIVE: the seam it asserted was never linked

**Beyond the seal.** `PREREGISTRATION.md` is untouched (`afb4dc82…`). This addendum re-tests
**this arc's own Q3** at the owner's instruction (*"reverify, maybe is a false negative"*), and the
instruction was **right**. New cells `Q4a`–`Q4c`, `verification/seam_independence.py`, each
asserting its own mathematics.

**Q1, Q2 and I-31 are untouched and stand.** What is corrected is Q3's headline and, more
importantly, Q3's **reason**.

## 1. The defect, stated exactly

Q3 printed:

```
mu_3  <-> Q(sqrt-3)   : Q(zeta_3) = Q(sqrt-3).  SAME OBJECT.
2T/Q8 <-> Z(E6)       : McKay.  LINKED.
node  <-> 2T/Q8       : Q2.  IDENTICAL.
=> ALL FOUR ARE CANONICALLY LINKED.
```

The first line links a group to a **field**. It is not an edge between two of the four ℤ/3's. So
the edges actually exhibited are `node — 2T/Q₈ — Z(E₆)`: a connected cluster of **three**, with the
arithmetic hat `μ₃ ⊂ ℚ(√−3)` attached by **no edge at all**. The `=>` asserts a connectivity the
links do not supply.

**The sealed criterion would have caught this.** Q3's sealed wording was *"each … is classified as
canonically linked to the others or independent, **with the link named**"*. Three links were named;
the fourth was not named because it was never found — and the cell drew the four-way conclusion
anyway. The seal was sound; the cell was not held to it.

## 2. The missing edge, tested — and it is open

If *"order 3 at the node"* and *"invariant trace field `ℚ(√−3)`"* were one fact, they could not
come apart. **They come apart, exactly, on the object's own tower.**

`(LR)ⁿ` is the `n`-fold cyclic cover of m004 along its fibration. All are commensurable with m004,
so the invariant trace field is **constant**:

| n | word | vol / vol(m004) | shape field | node order | name |
|---|---|---|---|---|---|
| 1 | `LR` | 1.000000 | ℚ(√−3) | **3** | m004 |
| 2 | `LRLR` | 2.000000 | ℚ(√−3) | **3** | m206 |
| 3 | `LRLRLR` | 3.000000 | ℚ(√−3) | **1** | **s961** |
| 4 | `LRLRLRLR` | 4.000000 | ℚ(√−3) | **3** | t12839 |

> **`s961` is m004's own 3-fold fibred cyclic cover. Its trace field is `ℚ(√−3)`. Its node order
> is 1.** A quantity that is **constant** on a family cannot be the same fact as one that is not.

This is exact and needs no census. The census confirms it in both directions anyway — over the 77
once-punctured-torus bundles `b++<w>` with `w` cyclically reduced of length ≤ 8:

* **31 of 34** bundles with node order 3 have trace field **≠** `ℚ(√−3)` (e.g. `LLLR` = m023);
* **1 of 4** bundles with trace field `ℚ(√−3)` has node order **≠** 3 (`s961`).

**The four ℤ/3's are NOT one fact wearing four hats. Three of them are one fact; the fourth is a
second, independent fact.**

## 3. …and what that second fact is worth: 0.58 bits

The correction is not a promotion, and this addendum prices it **down** rather than celebrating it.

The derivative of the mapping-class action at the node generates a group of order **24** with
element orders `{1,2,3,4}` and all determinants `1` — **`S₄`, the rotation group of the cube**. So
the node order is the monodromy's image in a **finite congruence quotient**, not an arithmetic
invariant. `DF_L` and `DF_R` are 4-cycles, hence **odd**, so a word of length `n` has sign
`(−1)ⁿ`: even words land in `A₄` (order 12, **8** three-cycles), odd words in the odd coset, which
has **no** element of order 3. The census matches both priors exactly — even-length **34/51 =
0.6667** against `8/12`, odd-length **0/26** against `0`.

m004's monodromy is `LR`: the **shortest** pseudo-Anosov word, length 2, hence even, hence in `A₄`.

> Prior for "order 3" given that: **8/12**. The coincidence is worth **log₂(3/2) = 0.58 bits** —
> **under one bit, essentially negligible.**

## 4. The corrected verdict

> **Q3's HEADLINE survives. Q3's REASON does not.** The ℤ/3 recurrence is still not evidence — but
> **not** because it is one fact wearing four hats. It is **two independent facts whose agreement
> is cheap** (0.58 bits). Right answer, wrong proof.

**Withdrawn:** the claim that this arc extends B727/I-17's *"the recurrence is FORCED, not
evidence"* to a fourth hat. It does not — the fourth hat is not another presentation of the atom.
**B727 itself is untouched**: its three hats are genuinely E₆-internal and its conclusion about them
stands.

## 5. Why the wrong proof mattered — the harvest

"One fact wearing four hats" closes the seam **permanently**. "Two independent facts, cheaply
agreeing" leaves it open. The difference is load-bearing, because of what Q4a incidentally proves:

> **The node's ℤ/3 is NOT a commensurability invariant.** It is 3 on m004 and 1 on m004's own
> 3-fold cover `s961`.

Every arithmetic handle this programme uses — the trace field, the invariant trace field,
arithmeticity, the atom `ℚ(√−3)`, the quaternion algebra — is a **commensurability-class**
invariant, and therefore **cannot distinguish m004 from `s961`**. The node's ℤ/3 can. It is the
first item in this cluster that sees the *manifold-with-its-fibration* rather than the class.

That is a **lead, priced as a lead and nothing more**: the programme has several open questions of
exactly the form *"which member of the class?"* — I-6's *which 2T*, xB002's `SCOPE_NOTE_L1` (*the
genesis selects a family; knot-ness selects the member*), L54's cover census. A non-commensurability
-invariant handle is the right **type** of object for those questions. Nothing here shows it
answers any of them, and 0.58 bits buys no conclusion. **Q3's false negative would have discarded
the handle without ever pricing it** — that, and not the lost half-bit, is what the error cost.

## 6. New error class: **E82, the ASSUMED-CONNECTED LINKAGE class**

A set of matching structures is declared *"all canonically linked"* — hence one fact, hence not
evidence — when the exhibited links form a **proper subgraph**, leaving at least one member joined
by nothing. The negative then over-reaches by exactly the missing edge.

**Standing rule that catches it:** *a kill needs the same map a promotion needs.* Write the link
graph, list the edges you actually exhibited, and check **connectivity** before writing "all N are
linked". An unlinked member is an **independent** hat and the coincidence keeps its weight.

**Why this class is new and why it bit here.** B1231's Identification Rule polices claims of the
form *"X here IS Y there"* — and it is enforced, by a gate and a ledger, **on promotions**. This
arc made exactly that kind of claim in the opposite direction, to **kill** evidence, and nothing
checked it: the same seat that correctly registered I-31 with an exhibited, acting map asserted a
four-way sameness with no map at all, one cell later. **The identification discipline was applied
to what the record claims and not to what it discards.**

**Provenance.** `verification/seam_independence.py` (cells Q4a–Q4c) → `verification/reproduce.sh`.
Depends on: snappy's census identification, `ManifoldHP` shapes at 60 dps, the shape field =
invariant trace field (Neumann–Reid). Cross-refs xB002 (`s955…s961`, `t12839` — the same members
this seat met in B1136's widened family), B727/I-17, I-1, I-31, B1231.
