# B2016 — Listening card 30: the null control — the whole's small group G₃ acting on the cosets of every subgroup: where does the halving hold?

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **The guard:** on 2026-11-26 main named a null control as a guard against hearing the group's properties as the whole's:
  the same pipeline on actions that are not the whole's orbit. B2012 found one law that is the group's (the four-move
  pairing). The halving is the open case.
- **The decisive comparison:** B2009 says the halving is decided by the stabiliser's condition. So the test keeps the group
  fixed and changes the stabiliser.
  - G₃ is the image of the modular group on the orbit of (3,3,3) mod 27, of order 216.
  - It is made to act on G₃/H for every conjugacy class of subgroups H.
  - The same six moves are read as words in C and σ: σC², σC, Cσ, C²σ, CσC, C²σC².
  - The whole's own orbit is H = Stab(3,3,3), of order 3.

## The checks

- **N0 (sanity):** on H = Stab(3,3,3), the coset action reproduces the halving identity p_neutral(2x) = 2^d (x² − 9) x S(x).
- **N1:** for every class of subgroups H, the action on G₃/H; C's fixed points there; and whether ρ is trivial on H.
- **N1's classification (exact, FLINT):**
  - (a) the identity in the whole's form;
  - (b) the charged polynomial divides p_neutral(2x)/2^d, so every charged mode is paired;
  - (c) neither.

  The counts of each, and the list of the classes in (a) with their orders.
- **N2:** the same over G₄ (mod 81, order 1944), if its subgroup classes are enumerable in twenty minutes.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| N0 | the identity holds on G₃/Stab(3,3,3) | 0.97 |
| N1 | (a) holds for few classes (at most a fifth of them), and among them for every H conjugate to the whole's stabiliser | 0.6 |
| N2 | the same pattern over G₄ | 0.5 |

## What it means

- **If few coset spaces halve:** the halving is a property of the whole's orbit within its group, not of the group's action
  in general. The group's twist is necessary; the whole's stabiliser is what makes it hold.
- **If most halve:** it is closer to the group's, and the record says so.
- **Nothing is compared with data.**
