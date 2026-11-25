# B1983 — Listening 1: the moves acting together on the fibre's characters over every finite field connect the cusp's leaf, and no other integer leaf, at every prime; they fix only the common point and the trivial character; the swap changes no orbit

**Verdict: PROVED (exact on the stated range; two readings post hoc, labelled).** Main, 2026-11-25. Data-free. The first
listening card at the author's word: listen to the interactions' natural unfolding, choose nothing, do not sculpt the
Standard Model. Register rows P-882, P-845, P-629 and P-694. **0 of 19.**

## Seen first

- **The seed** (GENESIS §§ 1–2):
  - two records;
  - the moves L and R as Fricke maps on the characters (B1600, B1601);
  - κ = tr[a, b] conserved by every move (B497's stratum 1, B1342);
  - κ = 2 is "nothing" (B309);
  - the cusp's leaf is κ = −2, with the common point (W2).
- **What the record had already heard:**
  - W1 to W4 (B1600): the three, the common point, 2T, the triplet;
  - B1601: the common point is every odd-trace thread's geometry mod 3;
  - B1347: the non-invertible strata have a direction, and the grammar's stratum does not;
  - B177: κ conserved, the trace map reversible;
  - B451: one thread's escape rate;
  - B1868, B1923, P-632: on τ alone no point carries weight.
- **Swept:** `VERDICT topic-sweep /Markoff mod|mod p orbit|orbits of the moves|connected leaf|finite field.{0,20}character|Markov surface over/: 0 of 1724 arcs on main match (none); 0 register rows match (none)`. No arc on main computes the orbits of the moves over finite fields.
- **The literature, cited from memory and not checked at source:** on the Markov surface mod p, Bourgain, Gamburd and
  Sarnak (2016) conjectured, and proved for most primes, that the moves act transitively on the nonzero points; W. Chen
  (2024) completed it for every large prime. Here the run itself is the evidence; the citation is the calibration.

## The results (`verification/listen1.py`, `listen1_run.txt`, `listen1_run.json`; exact, 4 s)

- **The system.** The Fricke maps L and R, then L, R and the swap P, act on 𝔽_p³ for every prime p ≤ 47, each leaf κ ∈ 𝔽_p.
  Each map is checked to be a bijection, and κ to be conserved.

| cell | outcome |
|---|---|
| E1: the cusp's leaf κ = −2 is one orbit of nonzero points for every p ≥ 5 | **holds**, 13 of 13 primes, with or without P (the calibration) |
| E2: at p = 2 and 3 the cusp's leaf is the origin or nearly | **holds**: at p = 3 the leaf is the common point alone (B1601's fact, from the whole); at p = 2, one orbit of 4 and the origin |
| E3: some other leaf splits | **holds**: at p ≥ 29 more than half the leaves split |

- **What every move fixes.** Only the common point (0, 0, 0), on the cusp's leaf, and the trivial character (2, 2, 2),
  on "nothing" (p ≥ 3; at p = 2 they coincide).
- **The swap P changes no orbit, at any prime or leaf.** GM5c, open in GENESIS, is invisible to the whole action's orbits.
- **Post hoc, labelled** (`leaves_posthoc.py`, `leaves_posthoc_run.txt`; written after the run was read):
  - **among the integer leaves κ = −40, …, 40, only the cusp's leaf κ = −2 is connected at every prime 5 ≤ p ≤ 47.**
  - The leaves whose commutator has finite order (κ = −1, 0, 1) are connected at one or two primes at most.
  - The "nothing" leaf, κ = 2, is connected at none.

## What the whole does, read in its own terms

- **The cusp is not chosen; the whole singles it out.** Of the frustration levels the moves conserve, the cusp's is the
  only one, among the integers to ±40, on which the whole action connects everything at every prime, apart from the
  common point. The selection is of the first family on record, a finite classification with a test of membership:
  the leaves mod p classified by their orbits, membership meaning connected at every prime in range.
- **The whole forces two states:** the common point and "nothing". It forces no other.
- **On the cusp's leaf the whole leaves structure only at the primes 2 and 3.** At every prime from 5 to 47 it connects
  the leaf. With B1601 (the geometry of every odd-trace thread meets the common point at a prime of norm 3, and at no
  other prime), this suggests that the weave's own levels are 2 and 3. That is a reading, not yet a theorem.
  - Level 5, where the record's work has lived (B1698 to B1979), is m004's private prime. A thread of trace t fixes a
    point of order p up to sign (B1733) only where p divides (t − 2)(t + 2), which is 5 for the golden thread (t = 3).
  - This bears on P-845: the whole's levels appear to be 2 and 3, and level 5 is one thread's.
- **No Standard Model shape was asked for, and none is read here.**

## What is open

- **The theorem** behind the post hoc reading: the cusp's leaf is the only leaf connected at every prime. Partly known for
  the Markov surface; the other leaves' splitting is to be checked at source.
- **The next listening step:** the field the whole forces at its own levels, 2 and 3 (FK15), and then the loop (PF5).
