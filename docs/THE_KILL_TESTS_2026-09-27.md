# The kill tests (2026-09-27): what the Eisenstein mechanism gives, and where physics has to enter

*Seat: cc (the SM-derivation branch). Written for the owner after the four kill tests on the chirality mechanism. Arcs B1388–B1392
on this branch. 0 of 19.*

## The plan

The plan was to attack the record's one positive result with tests that could kill it, sealing each test before computing wherever
its outcome was open.

The result under test was **B1386–B1387**. On cube~3.24, a degree-9 cover of o10_150725 in m004's commensurability class, the
cuspidal Higgs class v₊ has a symmetry-protected chiral index, **N(v₊) = ±2**.
- It is protected by L4, the fixed-point congruence of the order-3 rotation.
- It was computed by a Hejhal-type solve of the harmonic form.

## The four tests

| # | test | how decided | outcome | what it means |
|---|---|---|---|---|
| 1 | **The cutoff** (B1388): is N independent of where the cusps are cut? | sealed at 68c1b809 | **UNSTABLE** | The relative index moves with the cut (+4, +7, +8, +2, −1 up the Eisenstein cusps). The asymptotic +2 is minus the signed number of Higgs zeros on the whole manifold (Morse's boundary formula). The physical reading of "protected chirality" is retired. |
| 2 | **The full spectrum** (B1389): what is the frame's whole chiral spectrum? | sealed at 8d9498d2 | **MIXED** | Positive: the 27's spin-0 15 gives whole, anomaly-free generations for Higgs directions round γ, two on cube~3.24. Negative: the 78's broken roots make the bulk anomalous in every direction (a parity law, E₈ included), so the completion must carry the anomaly. |
| 3 | **The three** (B1390): can the mechanism give three? | a theorem, before any search | **no protected, non-pullback three** | In m004's class an order-3 symmetry either rotates cusps or acts freely, because ℚ(√−3) puts its axes' ends at cusp points. So a three is either a pullback of a one (the level question, sL-5) or rests on rotation residues that cancel mod 3, which no symmetry forces. |
| 4 | **The Yukawas** (B1391): what does the geometry fix? | banked theorems plus B1390's fixed sets | **NEGATIVE for ratios** | The generations carry the isometries' action. On cube~3.24 they are the doublet of D₃ ≅ S₃, so at the symmetric point they are exactly degenerate. The pullback three carries B1362's circulant degeneracy, or S₃'s "2 + 1". The geometry supplies a flavour group, not the ratios. |

**What joins them (B1392).**
- In this frame the chirality is carried entirely by the *free cusps*, where the Higgs class vanishes and the Higgs field dies off.
- Those are exactly the ends where the problem is not well-posed: the 1-form continuum there starts at 0.
- A Higgs class that stays alive at every cusp gives a clean, Fredholm problem, and its count is **zero**.

So each open question above points at the same place:
- which count is physical (test 1);
- who carries the anomaly (test 2);
- whether the level is the cover or the quotient (test 3);
- what breaks the flavour symmetry (test 4).

That place is what physically completes the free cusps.

## Two things the tests found along the way

- **The family is not the class (E4).** 13 of B1186's 112 "family" members have non-integral traces. They are non-arithmetic, so they
  are not commensurable with m004, and the class's census part is 99. No verdict changed, since every member the results rest on is
  arithmetic, but B1385's identification and one reading of main's B1418 are scoped (relayed).
- **The "2 + 1" symmetry is common.** 115 of B1386's 184 members have a free order-3 symmetry inverted by another isometry: the
  structure under which a pullback three would be S₃'s singlet + doublet. The binding condition is a unit index on the quotient, which
  nobody has found yet.

## Where physics has to enter

**0 of 19.** What the tests did is locate the entry points:
1. **The completion of the free cusps (sL-8).** Any definite generation count, and the anomaly's cancellation, is a statement about
   what sits at the ends where the Higgs field dies off.
2. **The level (sL-5).** If three comes as a pullback, the architecture must say whether the cover or the quotient is physical.
3. **The Higgs sector's breaking of the flavour group.** It is the source of every hierarchy between symmetry partners.

## The next step

Seal, one at a time, candidate completions of the free cusps. Test each against three requirements the record already fixes:
- **CPT.** An end's contribution must flip sign with the sector's charge.
- **The anomaly** (B1389 §7). On the γ-slice the ends must carry an odd SU(5)³ anomaly per unit N. The minimal way is a single 5 (or
  10) per unit N at the cusps.
  - With a 5, the total is one (anti-)generation per unit N: the 10s from the bulk, the 5̄s from the ends.
  - A 10̄ would instead cancel the 10 and leave nothing chiral.
  - So the anomaly allows a chiral completion; it does not force one.
- **The count.** Whatever remains is the physical number of generations.

The candidates:
- a conical point at each free cusp, where the Higgs field vanishes as it does at its zeros;
- a physical wall at a cut, whose boundary modes B1388's relative index counts;
- a Dehn filling. It is vector-like (B1351), so it kills the count.

sL-8's rule stands: no completion may be chosen because it rescues a count. The choice of which completion paradigm to test first
is where the owner's steer would help most.

## Where the record is

| arc | commit | verdict |
|---|---|---|
| B1388 the cutoff test | 68c1b809 (seal), f0e914d0 | NEGATIVE (as sealed) |
| B1389 the full spectrum | 8d9498d2 (seal), 3e28e277, fefb938a | PROVED (MIXED, as sealed) |
| B1390 the Eisenstein axes | 57d2bcdf | PROVED (+ the E4 correction) |
| B1391 the generations' flavour | 8f9ebc3f | NEGATIVE (routed) |
| B1392 the ends carry the chirality | 56c25699 | PROVED |

Open leads: sL-8 (the completion), sL-7 (the route to three, with its flavour), sL-5 (the level). The letter to main carries the
fiftieth to fifty-fourth notes.
