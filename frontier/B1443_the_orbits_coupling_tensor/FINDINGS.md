# B1443 — THE ORBIT'S COUPLING TENSOR: each member of a deck orbit couples to its own Higgs class. On the root's three-fold cover that holds for every orbit and every coupling

cc, 2026-10-01. Occasion: this seat reported B1438 and B1440 to the owner as "the number three is never a property
of one vacuum, and its copies cannot be told apart", and the owner asked: *"why is this a blocker? or we just dont
understand it properly, and we have missexpectations on how should reality / sm emerge."* The theorems were sound.
The blocker was an expectation this seat had imported: that the generations' differences must be numbers inside
one background. This arc computes what the theorems actually leave: the shape of an orbit's couplings.
**Verdict: PROVED** (a corollary of B1438, checked directly, and tabulated on every orbit of B1439's population).
Not sealed: it is a tabulation of sealed censuses, made after a look at nine levels; no prediction was at stake.

## The tensor (a corollary of B1438 C and E)

Let B₀, …, B_{m−1} be a deck orbit of generation-shaped backgrounds whose extension characters differ. For a
coupling type (two sectors A, B) member i couples to the spin-0 character of its own data,
η_i = (α_A β_B)_i^(−sign), with strength y = s(ℓ_i) − s(η_i), the same for every member because s is
deck-invariant. No invariant functional joins sectors of two members (E), and a character other than η_i admits no
functional on member i's sectors with a non-zero triple product. So

    Y(i, j; k) = y · [i = j] · [η_i = η_k],

and the whole shape of the tensor is the map i ↦ η_i: **how many distinct Higgs characters the orbit couples to.**

**Checked directly** (`verification/one_higgs_per_member.py`, record `one_higgs_per_member.json`): on s961 and on
the three-fold cover of −LLLR, for every background and **every** character of the level tried as the Higgs, all
invariant functionals by linear algebra and their triple products by B1435's sealed instrument. A non-zero
coupling occurs for exactly one character, the background's own (48 of 48, for Q·u^c and for Q·d^c); one further
character admits a functional (quotient·quotient) with coupling zero; every other admits none.

## The census (`verification/orbit_tensor.py`, record `orbit_tensor.json`, `orbit_tensor_run.txt`)

Every deck orbit of every level of B1439's population with k ≥ 2: 142 levels, **18 788 orbits**, by slopes alone.
On every orbit the vanishing and the value of each coupling are constant along the orbit (asserted), and the down
and lepton couplings use the same characters (asserted).

| orbit size | orbits | one Higgs character per member, up and down | some coupling with fewer |
|---|---|---|---|
| 2 | 9 108 | 5 200 | 3 908 |
| **3** | **4 904** | **4 464** | 440 |
| 4 | 1 264 | 784 | 480 |
| 5 | 432 | 432 | 0 |
| 6 | 696 | 528 | 168 |
| 7 | 928 | 928 | 0 |

Orbits of three, in detail: the extension characters are distinct on 4 896 of 4 904; one Higgs character per member
for both up and down on 4 464; with both couplings also non-zero on 1 504; with ν^c firing and its coupling on three
distinct characters as well on 552.

**The root.** On s961, the root's three-fold cover, **all 16 orbits** have three distinct extension characters,
three distinct Higgs characters for the up coupling, three for the down and lepton coupling, three for the
neutrino coupling, and every one of those couplings non-zero. Of the 25 three-fold levels carrying orbits, that
holds for every orbit on exactly two: the root's and −LLLR's. On the root's tower the same shape continues where
the level is prime: five distinct at level five, seven at level seven.

## What follows by linear algebra alone

Give each Higgs class k a number v_k (whatever sets it). The mass matrix of a coupling type on an orbit with one
Higgs class per member is M = y · diag(v₀, …, v_{m−1}):

- its singular values are y|v_k|: **the ratios of the masses are the ratios of the v_k**, and nothing else;
- it is diagonal in the orbit's own basis for every coupling type at once: **no mixing between members**;
- v equal on all members (the deck-symmetric point) gives m equal masses; v on one member gives rank one — one
  massive member and the rest massless;
- the down and lepton matrices are equal, entry by entry.

Where an orbit couples to **one** Higgs character for all members (440 of the orbits of three, for at least one
coupling type), M = y·v·1 and that coupling type is degenerate whatever v is.

## What this corrects

B1438 wrote "the frame cannot split generations … whatever distinguishes three generations is not in this frame",
and this seat reported it upward as a limit. Sharpened by `ADDENDUM_1` there: the frame does not split generations
**by a number inside a background**, and on most orbits it supplies a separate Higgs class for each member; what it
has not been asked for is what fixes the v_k.

## What is and is not known about the values v_k (checked at the owner's instruction, the same day)

The owner, on this seat's first draft of the paragraph below: *"are we sure sure sure, check for errors on that whole
math."* Two errors were found, both in the draft's sentence that "the record has proved, three separate ways, that an
invariant rule cannot supply a point of its own orbit, and the hierarchy is that point."

1. **The three arcs cited (B782, B990, B1225) are about other orbits**: the eight closings of the measurement
   torsor; the G(ℚ)-orbit of a pair of 27s, which says of itself that it is "not about a manifold"; the menu of
   values. None concerns a deck orbit of Higgs classes. For this orbit the corresponding statement is elementary
   and is verified directly: the slope function is deck-invariant (B1438 D), every slope of every character of a
   background is constant along its orbit on the nine levels checked here, and each coupling's vanishing and value
   are asserted constant on all 18 788 orbits. No computed invariant tells the members apart.
2. **The inference was wrong.** That no invariant rule singles out a member does not mean the pattern of the v_k is
   not supplied. Which member carries the largest v is a label. The pattern, as an unordered set, is an invariant.
   A deck-invariant function of (v₀, …, v_{m−1}) can have minima that are not deck-symmetric: the rule is symmetric,
   the set of minima is symmetric, each minimum is not. **Nothing proved in the record forbids the object from
   fixing the pattern. What is missing is a deck-invariant function of the Higgs classes, and none has been looked
   for.**

**A first candidate, computed while checking** (`verification/higgs_product.py`, record `higgs_product.json`): on
the root's three-fold cover the product of an orbit's three Higgs characters is trivial, for the up, the
down-and-lepton and the neutrino Higgs alike, on all 16 orbits. (The product over a deck orbit is deck-fixed, and on
the root's tower the deck fixes no non-trivial character, so there the product is trivial at every level: also at
levels four to seven, as computed.) So a cubic term joining the three Higgs classes of an
orbit is allowed by the characters and is deck-invariant. Whether it is non-zero is not computed. It does not hold
on every level: on the three-fold cover of −LR the product is not trivial.

## The reading — FENCED. Everything above is computed; nothing below is.

> **Speculation, tagged.** If a deck orbit of three on the root's three-fold cover is read as three generations
> (the SM lane's open bit: the deck kept, not gauged), then the Standard Model's pattern — three copies identical
> under every gauge interaction, distinguished only by their couplings to the Higgs sector, with no mixing at
> leading order — is what this tensor has, and the masses would be m_k = y·v_k. The hierarchy would then be a
> property of the vacuum: the minimum of a deck-invariant function of the Higgs classes. A cubic h₀h₁h₂, if
> present, is of the kind whose minima switch on one class and leave two off.

| speculative step | what it would take, as a computation | status |
|---|---|---|
| the three members are present together | the deck kept: one physical configuration carrying the orbit (sm:sL-5) | open, not computed |
| a deck-invariant function of the three Higgs classes | first: is the character-allowed cubic h₀h₁h₂ non-zero (a triple product of three spin-0 classes; none of them is interior, so the relative product of B1435 does not apply as it stands) | **not computed**; the characters allow it on the root's cover |
| its minima are not deck-symmetric | the function itself, then its critical points | not computed |
| the light generations are not exactly massless, and mixing is not exactly zero | a correction beyond the cubic: the couplings between members vanish exactly (B1438 E) | not computed |
| down and lepton masses equal generation by generation | already forced here; observed only roughly | a tension, recorded |
| three Higgs classes rather than one | the frame gives one per member | not examined |

**The fence, unchanged:** main's class index on non-semisimple backgrounds; an index is not a generation count; a
coupling here is a number of the frame in the longitude normalisation, not a Yukawa coupling; E₆'s Clebsch–Gordan
constants are not computed; nothing here is a value. 0 of 19.

## Registered

Lead L235: what fixes the Higgs values — the deck-invariant functions of an orbit's Higgs classes.

## Verification

`verification/orbit_tensor.py`, `one_higgs_per_member.py`, `higgs_product.py`; records `orbit_tensor.json`,
`orbit_tensor_run.txt`, `one_higgs_per_member.json`, `higgs_product.json`. Lock: `tests/test_b1443_orbit_tensor.py`.
