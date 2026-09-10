# m002, and why axiom 5 destroys the chirality bit (2026-09-10)

Prompted by the question "what about m002 instead of m004?". The answer is no, for three reasons —
but the question leads somewhere the paper does not go.

## What m002 is

| | m000 (Gieseking) | m002 | m003 | m004 |
|---|---|---|---|---|
| orientable | no | **no** | yes | yes |
| cusps | 1 | **2** | 1 | 1 |
| volume | 1.0149416064 | **2.0298832128** | 2.0298832128 | 2.0298832128 |
| `H_1` | Z | Z/2 + Z | Z/5 + Z | Z |

m002 is tiled by **two exactly-regular ideal tetrahedra** (both shapes `= 1/2 + (sqrt3/2)i` to 1e-9;
`vol / vol(reg tet) = 2.000000`), so it is arithmetic with invariant trace field `Q(sqrt-3)` — the same
commensurability class as m003, m004 and the Gieseking manifold.

**It cannot replace m004.** (i) Non-orientable, so it fails axiom 5 — and worse, on a non-orientable
manifold chirality is not *definable*: there is no orientation to reverse, so the bit the programme
wants is not a property m002 has. (ii) Two cusps, while the whole §7 index framework is one-cusped
(the multi-cusp extension is exactly what L202(b) still owes). (iii) Not a knot complement, so the
`H_1 = Z` discriminator and Reid's uniqueness theorem do not apply.

## First consequence: §2 undercounts

§2 says m003 "shares its volume exactly --- **both** are 2.0298832128". There are **three**: m002 sits
at the same volume, in the same arithmetic class. The genericity argument is stronger than the paper
states it, at the cost of one word.

## Second consequence: the orientation fork lands on the amphichiral member, and that is forced

The fork that produced m004 has a two-cusped twin:

- m000 (1 cusp, non-orientable) → orientation double cover = **m004** — amphichiral
- m002 (2 cusps, non-orientable) → orientation double cover = **m203** — amphichiral

And **m202** sits beside m203: volume 4.0597664, four regular ideal tetrahedra, `H_1 = Z + Z`, two
cusps — every invariant the same — but **chiral**. The two are a chiral/amphichiral pair, and the
orientation fork reaches only the amphichiral one.

That is not an accident of these examples. It is a theorem:

> **Every orientation double cover is amphichiral.** If `X -> N` is the orientation double cover of a
> non-orientable `N`, the non-trivial deck transformation is orientation-reversing, and by Mostow
> rigidity it is realised by an isometry. So `X` admits an orientation-reversing isometry.

Verified over the census: **250 orientation double covers tested, 250 amphichiral, 0 chiral.**

## What this changes

**Axiom 5 does not merely select an orientable manifold — it guarantees an amphichiral one.** The
chirality bit is not withheld by the arithmetic, and is not an empirical absence discovered downstream:
it is destroyed by the axiom that buys orientability. m202 is a chiral manifold with the object's
arithmetic that the fork provably cannot reach, because no orientation double cover is ever chiral.

The record already carries the observation (B1083/B1091: "orientability and amphichirality bought
together at tick two"; THE_LADDER X23). **The paper does not.** §2 grades the orientation axiom "the
most expensive" and justifies it only by the nearness of the discarded sibling; the sharper reason is
that the axiom costs the chirality bit outright, and that is provable in two lines.

Three places this tightens the paper:

1. **§7** — "the object withholds the chirality bit" acquires a mechanism instead of a census.
2. **§7's tower result** — why covers escape is now clear: a cover of m004 is *not* an orientation
   double cover of m004, so the deck argument does not apply. Hence 66 of its 87 covers are chiral.
3. **§11 falsifier 6** — looking on chiral covers is the right instinct, and now has a reason: covers
   are the only place the forcing does not reach.

It also sits well with the paper's own honesty standard: the bit is not missing because the object is
poor, but because a named axiom spent it. That is a located boundary, which §9 prefers to a confessed gap.
