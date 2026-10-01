# B1442 — THE TWO-GENERATION BACKGROUNDS: none. A module can count two on several cusps; the frame's five charged sectors cannot share it

cc, 2026-10-01. Sealed at 7f080e49 before any background was assembled on a manifold with more than one cusp
(`PREREGISTRATION.md`, SEAL_LEDGER). B1441 found seventeen several-cusped manifolds on which one rank-two module of
the frame has class index two, and said before its data that a module is not a background. This arc assembles the
backgrounds. **Verdict: NEGATIVE** (on the seventeen, with the classes tried). **Predictions: G5 YES; G1, G2, G3,
G4 NO.**

## The run

On each of the seventeen carriers: every extension character ℓ with a class, every class tried (a basis of
H¹(M; ℓ) and three random combinations), every sub-character; 8 924 firing modules in all, index two among them as
B1441 found. Then every (θ, ψ_Y, W) with ℓ = θ²/W and the six sector modules of B1432's frame.

| carriers | generation-shaped backgrounds | of count ±1 | of count ±2 |
|---|---|---|---|
| sixteen | **0** | 0 | 0 |
| m009 deg 6 #25 (two cusps, N = 8) | 32 | 32 (16 of each sign, ν^c with the generation's sign, at generic classes) | **0** |

**No background has its five charged sectors at index two. On sixteen of the seventeen manifolds no
generation-shaped background exists at all**, of any count.

## Why the sign-character carriers cannot (a lemma)

Nine of the seventeen have N = 2. There the result is forced. For a character group of exponent two, ℓ⁻¹ = ℓ and
W² = 1, so with B1438's duality V(ℓ, α)* ≅ V(ℓ, β⁻¹), β = α/ℓ:

    α_Q · α_L = θψ_Y W · θψ_Y⁻³ = θ² W ψ_Y⁻² = ℓ · W² · ψ_Y⁻² = ℓ,

that is β_Q⁻¹ = α_L: **the dual of the Q sector is the L sector.** Hence I(Q) = −I(L), and the two cannot be equal
and non-zero. A generation-shaped background needs characters of order above two.

The other eight carriers (N = 4, 6, 8) have no such lemma; there the absence is the census's.

## The sealed predictions, read (`verification/read_backgrounds.py`, run twice; record `backgrounds_summary.json`)

| | prediction | prior | outcome |
|---|---|---|---|
| G1 | some carrier has a generation-shaped background of count ±2 | 35% | **NO** |
| G2 | every carrier has a generation-shaped background of count ±1 | 55% | **NO** (one of seventeen does) |
| G3 | some count-±2 background has ν^c at ±2 as well | 15% | **NO** |
| G4 | some count-±2 background exists at a generic class | 20% | **NO** |
| G5 | no background has a charged sector above 2 | 95% | **YES** |

One of five came true where 2.2 were expected. G2 was the worst: the prior took "a module fires" for "a background
exists", and on several cusps the two come apart far more than on one.

## What it means, and the fence

- **The count per background stays at one**, on every manifold the record has computed, with one cusp or several.
  An index of two exists (B1441) and is a fact about a single sector. The frame ties its sectors together by
  charges, and those relations do not let five of them reach two together on any of the seventeen.
- **So three paths to more than one generation per vacuum are now closed on what has been computed:** a larger
  bundle on one cusp (B1440, a theorem), copies along a deck orbit (B1438's Theorem E, a theorem: they do not mix),
  and more cusps at rank two (this arc and B1441, a census to degree six).
- **What is not excluded:** covers of degree above six; a special class of a several-dimensional H¹(ℓ) other than
  those tried; three live cusps with a triple coincidence; a frame other than B1432's.
- **The fence is unchanged:** main's class index outside the reductive domain; an index is not a generation count;
  no physics reading. 0 of 19.

## Not verified here

The count-±1 backgrounds on m009 deg 6 #25 are at one prime and are not recomputed exactly: the seal reserved the
exact recomputation for count ±2, of which there is none.

## Verification

`verification/backgrounds_mc.py`, `read_backgrounds.py` (sealed); records `backgrounds_0..5.json`,
`slice_*_run.txt`, `control_run.txt`; `backgrounds_summary.json` at the arc's root. Lock:
`tests/test_b1442_two_generation_backgrounds.py`.
