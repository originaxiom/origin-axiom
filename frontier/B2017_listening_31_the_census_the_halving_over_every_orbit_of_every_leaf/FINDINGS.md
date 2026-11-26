# B2017 — Listening 31: the census — over every orbit of every leaf at mod 27, 25, 49 and the primes 5 to 13, the halving holds on exactly three orbits: the three sisters on the cusp's leaf at mod 27

**Verdict: PROVED for its checks (exact for orbits of at most 1200 points; 20 orbits between 1200 and 2400 points in double
precision; 21 orbits at mod 49 above 2400 points left out).** Main, 2026-11-26, in the author's /loop "continue the listening
line". Data-free. 0 of 19.

## Seen first

- **B2014:** the three 72-point sisters mod 27 and the halving without left-out modes on (3,3,15). **B2016:** the null
  control; the halving is the whole's orbit's. **B1983 and B2012:** the orbits of the moves over the finite fields.
- **agy-exp's EL-3** (harvest row 2015): no bound-state leaf but the cusp's halves.
- **Swept:** `VERDICT topic-sweep /census|every orbit of every leaf|all residues/: 173 of 1758 arcs on main match (NEGATIVE 27, OPEN 10, PROVED 136); 116 register rows match (DECLINED 2, DONE 81, QUEUED 33)`.
  The matches are the record's many censuses of other things. None classifies the halving over every orbit.
- **The literature (standard):** none beyond B2016's.

## The census (`census_run.txt`; expectations hashed before the run)

| level | residues | orbits | (a) the whole's form | (a′) no left-out modes | (b) pairing only | (c) neither | left out |
|---|---|---|---|---|---|---|---|
| mod 27 | 19,683 | 118 | **2**: (3,3,3) and (3,3,12), C fixing 3 | **1**: (3,3,15), C fixing none | 0 | 115 (6 numerical) | 0 |
| mod 25 | 15,625 | 72 | 0 | 0 | 0 | 72 | 0 |
| mod 5, 7, 11, 13 | 125 to 2,197 | 10, 15, 26, 27 | 0 | 0 | 0 | all | 0 |
| mod 49 | 117,649 | 149 | 0 | 0 | 0 | 128 (14 numerical) | 21 (3,136 or 3,528 points) |

- **C1 holds:** at mod 27 the halving holds on exactly three orbits, the three 72-point sisters, all on the cusp's leaf k = 0.
- **C2 holds:** at mod 25, 49 and the primes 5 to 13, no orbit halves, and none even pairs its charged modes.
- **C3 holds,** in everything run: no orbit off the cusp's leaf halves. The 21 orbits at mod 49 above 2400 points are not
  covered.

## What the whole does, read in its own terms

- **The halving lives on the cusp's leaf at the prime 3 and nowhere else run.** Of 417 orbits at seven levels, three halve.
  They are the three sisters on the cusp's leaf mod 27.
  - (3,3,3) is the one that lifts up the tower.
  - (3,3,12) halves in the same form.
  - (3,3,15), where ω's exchange fixes nothing, halves with no left-out modes.
- **Elsewhere the charged modes do not even pair.** B2016's coset spaces of the whole's own group often paired without
  halving. The other leaves and primes do neither.
- **With B2016, the census answers the question it was set:** what was heard is the whole's, at its own leaf and its own
  prime. The ear did not pick a common feature and call it special.
- **No rate is read as physical, and nothing is compared with data.**

## Disclosures

- The card was hashed before any run.
- **What is not exact:** orbits of 1200 to 2400 points (6 at mod 27, 14 at mod 49) were classified in double precision, all
  as (c). The 21 orbits at mod 49 above 2400 points are left out.
- **What is not covered:** higher levels (mod 81 and beyond, mod 125, mod 343) were not censused. B2002 to B2015 cover the
  orbit of (3,3,3) there.
- agy-exp's EL-3 asked about the bound-state leaves in 2I, a different set. The census agrees in kind: no non-cusp leaf
  halves in what was run.
