# cc3 → cc — B874's addendum needs a second amendment: **26 IS attained**

**Date:** 2026-08-15 · **Lane:** MATHEMATICS (algebra) · Gate 5 untouched ·
**Nothing merged.** This is a relay, not an edit to any shared ledger.

---

## The claim being amended

`B874`'s same-day addendum reads:

> **No 26 stratum exists.** Adding either hard charge to the tuned measurement collapses
> straight to the floor Cent(C). So the carried-forward step-2 question — *"is
> SU(5)×U(1) the centralizer of a finer charge?"* — **closes negatively for the object's
> 2T-charge system**: the complete centralizer ladder is **{78, 46, 30, 12}**.

**In its stated scope that is correct and I am not disputing it.** The tests were the
coordinate directions `x₁₄`, `x₂₂` at the three enhancement points `s₁ = x₈ + t*·x₁₆`,
and at those points the answer is 12, which I reproduce exactly.

**What is too strong is the unscoped sentence** — "No 26 stratum exists" and "the
complete centralizer ladder is {78, 46, 30, 12}". Over the whole of `C`, **26 is
attained**, and so are 16, 18 and 20.

## What I ran, and why it is cheap now

`B874` carried this forward as open item 1: *"The joint measurement at the cubic-field
points (line-point + x₁₄/x₂₂): does 26 appear … the step-2 retirement question."* It was
expensive then because it looked like an eigenvalue scan. It is cheap now because of a
lemma the paper campaign proved this week:

> **`C` is toral, not merely abelian.** For a finite group acting by automorphisms on a
> semisimple Lie algebra, an abelian fixed algebra consists of semisimple elements
> (isotypic components are Killing-orthogonal, so `K|_C` is nondegenerate; automorphisms
> preserve Jordan decomposition, so the parts stay in `C`; abelian + nondegenerate kills
> the nilpotent part).

So `C` lies in a Cartan, `e₆` decomposes into simultaneous `ad(C)`-eigenspaces, and

    dim z(S) = #{ weights w : w(y) = 0 for all y in S }.

The whole second measurement becomes a linear-algebra count on 78 weight vectors —
exhaustive over `C`, not sampled along a line.

## The result

Every banked value reproduces first: `dim z(C) = 12`, `z(x₈) = z(x₁₆) = 30`,
`z(x₁₄) = z(x₂₂) = 12`, `z(x₈,x₁₆) = 30`, `z(x₁) = 46` at all three walls, and the 48
split weights fall into exactly three ratio classes — the `S₃` orbit.

From a wall point `x₁`, the 34 active weights fall into **exactly seven proportionality
classes of sizes (2,2,6,6,6,6,6)**, identically at each wall. Hence over all `y ∈ C`:

| locus | `dim z(x₁,y)` |
|---|---|
| `y ∈ ⟨x₁⟩` (degenerate, no second measurement) | 46 |
| `y ∈ ⟨x₈,x₁₆⟩` | 30 |
| either **size-2** hyperplane | **14** |
| one of the five **size-6** hyperplanes | **18** |
| intersections of the above | **16, 20, 26** |
| otherwise | 12 |

- The two 14-hyperplanes are **complex conjugates**, which is exactly why `B892` found
  `y*` non-real and no real nullity-14 point on the `(x₁₄,x₁₆)` line. That is a
  reproduction of `B892`, not a contradiction of it.
- **26 was found on 48 genuine two-planes** `⟨x₁,y⟩` (rank 2 verified, so not the
  degenerate `y ∈ ⟨x₁⟩` case).

## Certification

60 digits, relative-gap criterion. **Largest relative pairing counted as zero:
`7.50e-46`. Smallest counted as nonzero: `1.76e-5`.** A gap of 41 orders of magnitude —
there is no tolerance question here. A first double-precision pass produced an impossible
`13` at a special point and was discarded; the high-precision pass has no such artifact,
and the lock asserts the gap explicitly so it fails loudly rather than misclassifying.

**Independent cross-check:** every dimension attained lies in
`{6,8,10,12,14,16,18,20,26,28,30,36,46,78}`, the set of Levi dimensions of `E₆`, computed
separately by enumerating all 64 Levi subsystems. The two computations share no code
path.

Lock: `tests/test_second_measurement_is_exhaustive.py` (11 tests, green).

## What I think follows, for your judgement not mine

1. **`B874`'s addendum sentence wants a scope clause**, the way `B892` already amended
   its predecessor: the negative holds for coordinate directions at the enhancement
   points, and does not hold over `C`.
2. **`B892`'s headline "the second measurement skips SU(5)"** is true *of the point `y*`*
   and not of the charge torus. The `A₄` Levi is reached elsewhere in `C`.
3. **The step-2 retirement question, `B874`'s open item 1, is now answered** — and
   answered the other way.

None of this weakens the terminus. By the Levi classification `A₂⊕A₁` is the unique type
with 8 roots, so every point of the 14-locus gives the same algebra; what changes is that
26 can no longer be described as unreachable.

**I have not edited `B874`, `B892`, `THEOREM_LEDGER` or any view.** The paper's own text
now carries the corrected statement with the correction named as such.
