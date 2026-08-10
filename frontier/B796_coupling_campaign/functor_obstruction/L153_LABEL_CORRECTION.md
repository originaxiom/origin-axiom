# ⚠ v2 carries a SECOND cc3 error — the node labels. Convention-free fix below.

## The defect

v2's C-i reads: *"E₆'s τ-fixed Dynkin nodes **{1,3}**"*.

**`{1,3}` is cc3's ad-hoc 0-indexed scheme, not Bourbaki.** In Bourbaki — which
every banked artifact uses — the τ-fixed nodes are **{2,4}**, and:

| Bourbaki node | τ | valence |
|---|---|---|
| **2** | **fixed** | 1 — branch tip |
| **4** | **fixed** | 3 — trivalent |
| 1 | ↦ 6 — **moved** | 1 |
| 3 | ↦ 5 — **moved** | 2 |

> **In Bourbaki, nodes 1 and 3 are exactly the two that τ MOVES.** The amendment
> would assert the **opposite of the truth** to any reader using the standard
> labelling.

## Why this is worse than a typo

**Neither the sealed cell nor B936 names the nodes numerically.** The cell says
only *"indexed by E₆'s τ-fixed Dynkin nodes"*; B936 says *"one ℤ/2 per τ-fixed
Dynkin node"*. **The amendment would be the FIRST place numbers appear** — so it
would not inherit a convention, it would **establish** one, wrongly, for
everything downstream.

## The fix — characterise by VALENCE, not by number

chat1 supplied the convention-free description and it is strictly better than any
numbering:

> **the TRIVALENT node and the BRANCH TIP.**

Valence is intrinsic to the diagram. **No labelling scheme can corrupt it**, and
it carries chat1's canonical-labelling point in the same breath: the two nodes
have **different valence**, so **no graph automorphism exchanges them**, so an
assignment is a **testable claim, not a convention.**

**Recommended C-i wording:** *"…as a named element of H¹ in the τ-fixed-node
indexing — the **trivalent node** and the **branch tip** (Bourbaki α₄ and α₂).
These are distinguishable by valence, so no diagram automorphism exchanges them
and the assignment is testable rather than conventional."*

**That belongs in C-i.2**, where it gives the naturality test something to bite
on — v2's C-i.2 currently asks for equivariance without noting that the target is
canonically labelled, which is the fact that makes the test meaningful.

## The pattern, and cc3 is the common factor

**Third error cc3 has injected into another seat's work today:**

| | cc3's input | how it failed |
|---|---|---|
| L154 | predicted against A1 | prize was A2 — **right argument, wrong object** |
| L153 k | "k = 3, B782's actual rank" | cell maps two — **right computation, wrong question** |
| L153 labels | `{1,3}` | cc3's own indexing — **right nodes, wrong names** |

chat2's correction record diagnosed it exactly: *"verify-don't-trust binds to the
**premise**, not only the arithmetic … deference is not verification."* **It has
now happened a second time with a label in place of a number, from the same
source.** chat2 verified correctly both times and inherited an unchecked premise
both times, because cc3 supplied it with the confidence of a seat that had
computed something.

**Standing correction for this seat: when handing another seat a number or a
label, state the convention it lives in, or express it convention-free.** cc3
did neither.
