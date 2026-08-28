# THE FULL STABILIZER CENSUS — row 4 closed at character level: the 27's weight geometry FORBIDS an abelian dark-matter stabilizer
## (outside bench memo 123, 2026-08-28; certificate `certificates/dm_census.py`, GREEN; the continuation memo 122 named as "a separate, unrun cell")

Memo 122's negative was on **four** banked elements. This asks the
structural question: can **any** abelian character of the 27 stabilize
N1 or N2?

**The test.** A character w ↦ ζₙ^(⟨a,w⟩+c) stabilizes a neutral iff its
**charged set is a nonempty subset of {N1, N2}** — charges add on
products, so a charged state with only-neutral company cannot decay
into uncharged visible states.

**⚠ In-run correction filed:** the first pass tested only **linear**
characters (c = 0). Memo 92 found D₂ᵗʷ has polarity ε = −1 — it *is*
affine — so the shift c must be enumerated too. With a shift the
charged set is the complement of a level set, so a stabilizer needs
some level set to hold **≥ 25** of the 27 weights. Both cases are now
covered.

| n | (a,c) pairs | stabilizers | min \|charged\| | max \|level set\| (nontrivial) |
|---|---|---|---|---|
| 2 | 128 | **0** | 11 | 16 |
| 3 | 2,187 | **0** | 12 | 15 |
| 4 | 16,384 | **0** | 11 | 16 |
| 5 | 78,125 | **0** | 11 | 16 |
| 6 | 279,936 | **0** | 11 | 16 |

**VERDICT: zero stabilizers out of 376,760 (a, c) pairs.** The
smallest charged set any nontrivial character produces is **11
states**; the largest level set is **16 of 27**, where a stabilizer
needs 25. **Both bounds fail by wide margins.**

**Why, structurally:** the 27's weights are spread across the Cartan
so that no linear functional mod n isolates the two singlets. **The
obstruction is the weight geometry** — which is why memo 122's
four-element negative was not an accident of *which* four.

**THE CLOSURE THIS EARNS.** Row 4 asked whether a forced discrete
symmetry stabilizes a neutral. Memo 122: no, for the forced ones.
This cell: **no, for every abelian character of this form.**
**Dark-matter stability cannot come from an abelian symmetry of the
27.** It would have to come from a non-abelian symmetry, a kinematic
(mass-ordering) accident, or structure outside the 27 — **and the
record supplies none of those.**

**Fence:** this is a *necessary-condition* census — it does not impose
Yukawa/coupling consistency, which could only **shrink** the candidate
set, so the negative is a superset negative and stands a fortiori.
Non-abelian stabilizers and kinematic stability remain untested, named
here and not claimed done. Gate 5 untouched.
