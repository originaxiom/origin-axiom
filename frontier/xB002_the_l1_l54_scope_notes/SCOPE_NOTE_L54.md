# Scope note — L54: gate A's quantifier

**Status: the scope-correction note X15 ranks (2) — B985's "most dangerous" — and records as owed
("still unwritten as of B1101"). Written here by the xb seat on `sep16-branch`, 2026-09-16.
This is a SCOPE NOTE, not a reopening. Gate A's mathematics is quoted, not re-derived; what is
re-derived here is the one discriminating fact about its quantifier (§3).**

## What was banked

> "Gate A is sealed for **the object**."

## What was proved

No forced choice among the sealed invariant classes **of `4₁` alone**, with the irregular-cover
class stress-tested **through index 6**.

Gate A's own text already fences two of its edges honestly — *"index ≤ 6 is a computational
horizon, not a theorem"* and the C-guardrail *"this is `open`, not proof of universal
impossibility."* The defect L54 names is narrower and is not covered by either fence: it is the
word **"the object."**

## §3 — Why the horizon and the class boundary are the same wall

Under `COMPUTE_THE_PROGRAM`'s own binding definition, *"the object"* means the **full relations** —
member, ends, class, sisters, both rows, child, faces — **never a single manifold**. Gate A was run
over `4₁` and its covers. And **covers are the commensurability relation**: two manifolds are
commensurable exactly when they share a finite-sheeted cover. So a cover census is the natural
instrument for reaching the class — which is precisely why stopping it at a finite index is not
only a computational bound but a *scope* bound. The horizon and the class boundary coincide.

**The discriminating fact, computed here** (`verification/covers_vs_class.py`): a degree-`n` cover
of m004 has volume exactly `n · vol(m004)`. Within the ℚ(√−3) shape-field family at ≤ 6
tetrahedra (21 members, see the L1 note):

| | members |
|---|---|
| volume ratio to m004 an integer (cover-eligible) | 16 |
| **volume ratio 2.5 — cannot be a cover at any index** | **5** — `m410, m412, s594, s595, s596` |

Five family members are excluded from *every* cover census of m004, at index 6 or at index 10⁶, by
volume alone. (Integer ratio is necessary, not sufficient — m003 has ratio 1 and is a sibling, not
a cover — so the exclusion argument runs one way only, which is the direction needed.)

The record corroborates this independently and more strongly: B1418's class census finds that the
chirality index fires on class members that are **not** covers of m004, and that the three members
carrying chirality, the arithmetic, the door and the count of three together (`m202, s959,
o10_150726`) are **none of them covers of m004**. The class is strictly richer than the tower, and
the difference carries exactly the content the programme has been looking for.

## The corrected statement

> **Gate A is sealed for `4₁` and its covers to index 6.** It is not sealed for "the object" in the
> relational sense `COMPUTE_THE_PROGRAM` defines, because a cover census cannot reach the
> commensurability class: five members of the shape-field family alone are excluded from every
> cover census by volume, and the class members that carry chirality and the count of three are
> not covers of m004. Extending the index raises the horizon; it does not move the class boundary.

## What is NOT claimed here

- **No mathematics of gate A is disputed.** The eight sealed classes, the Galois-orbit mechanism,
  and the index-6 census stand exactly as banked. Only the quantifier in the banked sentence is
  corrected.
- **No claim that gate A fails on the class.** It is *untested* there. Per the standing epistemic
  rule, the honest words are **"not checked"**, never "the object does not supply it."
- The cover/class argument here is a *necessary-condition* exclusion on volume. It shows a cover
  census cannot reach those five; it does not classify which family members are covers.
