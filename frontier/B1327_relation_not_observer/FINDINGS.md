# B1327 — "observer" is the wrong type for most of these rows; the right one is *relation*

**Verdict: OPEN.** A typing proposal with one verified computation, three proposed row moves, and one
over-count raised as a question. Nothing here closes a row.

## The misframe

The record's no-go is stated everywhere as:

> an invariant selector cannot pick a point of its own orbit

That is a theorem about the object acting **on itself**. It says nothing about a **relation to a
second thing**. "Observer" collapses the two — it imports an *agent* where the mathematics asks only
for a *second relatum*.

The record already found the gap and used it exactly once. §8: the chirality bit is *"an invariant of a
heterogeneous pair … belonging to neither relatum, and arrives without any act of selection."* Then §9
books the other five discrete rows as "externally supplied" and the section is titled *The observer,
priced*.

## Four types, replacing "externally supplied"

| type | meaning | needs |
|---|---|---|
| **D** by design | a unit; a category error to list as missing | nothing |
| **T** external by theorem | proved absent from the object | nothing — it is settled |
| **R** relational | an invariant of a pair, invariant under simultaneous symmetry | **a partner**, not an act |
| **S** selected | an orbit with no invariant selector *and* no available relation | **somebody** |

**Only S needs anybody.** That is the whole content of the reframe.

## Proposed row moves

| row | now | proposed | why |
|---|---|---|---|
| `l` | external by design | **D** | unchanged |
| `lambda` | external by theorem | **T** | unchanged, and proved |
| the chirality bit | relational, selection-free | **R** | the record got here first |
| **the real-structure closing** | externally supplied | **R** | the paper proves only that *the object's own mirror* cannot supply the antilinear involution — **one relatum refuted, not all** — and an antilinear involution *is* a relation to a conjugate. The question becomes *which partner*, not *who chooses*. |
| **family, VEV, filling** | finite menus, terminal | **candidate R** | the standing argument kills *invariant* selectors only; a relation can break an orbit that no endomorphism can |
| **the colour frame** | finite choice | **candidate R** | a `Z/3` orbit, triality-transitive. A partner breaking triality decides it; nothing internal can |
| **the Standard-Model shaping** | an input | **S, and the worst row** | this is *target knowledge*, not a relation to any mathematical partner. It imports the answer. |

## The verified computation

Link 54 says the mirror is the swap times the arrow. Checked here on the object: its **eight isometries
realise 4 of the 8 a priori sign triples** — exactly the index-2 subgroup cut out by `det = s_m · s_l` —
with **zero violations**.

```
arrow=-1 swap=-1 mirror=+1  x2      arrow=+1 swap=-1 mirror=-1  x2
arrow=-1 swap=+1 mirror=-1  x2      arrow=+1 swap=+1 mirror=+1  x2
```

**Three named bits, one relation, two free.** No act of selection appears anywhere in that sentence.

## A possible over-count, raised as a question and not asserted

The genesis **swap** is booked in §2's pre-object assumptions; the **arrow** and the **chirality bit**
are booked in §9. A relation among three bits spanning two tables is exactly where a double count
would hide.

**This is not a claim.** §8's chirality bit is a Fricke-`kappa` torsor class of a *pair*, and may not be
the same object as the manifold's mirror sign. Whether they are the same bit is for the seat that owns
§8 to adjudicate. If they are, one of the three rows is not an independent input.

## What re-typing does not do

**It closes nothing.** The chirality bit is already **R** and still carries *"which pair is used remains
supplied."* Re-typing moves the residue from an **act** to an **identity**.

That is progress for one reason only, and it is worth stating plainly: **an identity can be searched
for, and an observer cannot.** "Who observes?" forces Non-claim 8 and Scope 17 to fence metaphysics the
construction cannot express. "What is the second relatum?" is a mathematical question with a findable
answer — and on the one row where it was asked, it produced a theorem.

Reproduce: `verification/three_bits_one_relation.py`.
