# THE CLOCK AND THE LINE SECTOR — pre-registration (the web seat, 2026-11-06)

**For:** the owner's 10:37 message ("if smth is allowed to happen it will hapen … what if multiple choices coexist").
This seat answered that a plenitude reading moves the remaining choices into one: the weight on histories, that is,
the clock (P-437, P-439). The owner then chose "Attack the clock", and at 10:49 asked for a comprehensive sweep first.

**The sweep** (main at 307fa9101; reported to the owner before this file) found the record far along:
- **Four clocks:**
  - moves: Minkowski; B1813, and B1815 ("the record's walk has Minkowski's exit law, exactly");
  - length: area / Liouville, the critical point s = 1;
  - Weil–Petersson: B1816;
  - the action, volume: P-476, "supercritical — vol(LᵃR) stays near 3.664, the Whitehead link's volume … it does
    not suppress deep runs and its thread sum needs a cutoff".
- **Doors:**
  - A (Dani): chosen;
  - B (the walk theorems): open whether the walk is the dynamics;
  - D (a clock-free observable): queued.
- **P-438's open question:** "whether anything in the record forces 'followed'".
- **P-478's literature lead:** Bousso–Yang's counting-equals-following passes only the geometric clock.
- **The verdicts:** "the clock stays CHOSEN" (B1815); nothing ranks the clocks (B1816); no point picks a height (P-441).
- **So this check does not recompute volumes.** P-476 already has them.

**Kind:** data-free arithmetic on weights of histories. No coupling, scale ratio or held-out quantity is computed, and
nothing is compared with data. The six are not a criterion (P-708). The weights' parameters are generic (s = 1 and
2). **Written before** `clock_check.py` is run; a reduced smoke copy runs outside the tree, its values unread.

## What is new since Oct 29

**The line sector.** Since 904f19136, a departure that keeps the history's own line is a run n ≡ 1 mod 5 (reading
(ii)). P-437 to P-479 never restricted to it.

**The read-out's premise.** (N2) (c6b813450) reads τ at a point of one Teichmüller history.

## The argument (stated before computing)

**(C) (N2) is "followed".**
- The read-out reads one geodesic, the history, at its own symmetric point. The history is traced in its own time,
  arclength. That is P-438's "followed", not "counted".
- **If (N2) holds, P-438's open question is answered:** the record's own read-out presupposes "followed".
- **With plenitude** (every allowed history with equal standing, followed from a typical start), the measure is
  Liouville (P-438), i.e. the critical point s = 1 and Gauss–Kuzmin runs. That would also answer P-437's "why the
  critical point", conditional on (N2) and plenitude.

**The price.** A Liouville-typical history has departures throughout (Gauss–Kuzmin). The one-departure history is the
dilute idealisation and has measure zero.

## The computation

The share of the run of 6 among the line sector's departures, n ∈ {6, 11, 16, …}, under each clock's depth law:
- **(moves)** fair-coin letters. The run law is Geometric(½), 2^{−n}; for a single departure in a golden background
  the weight is 2^{−(n−1)}. Both give the same share.
- **(length)** single departures in a golden background, weight e^{−s·ΔS_n} with ΔS_n = 2 log((n − 1 + √5)/√5)
  (0772952e3; a34f5cdd1), at s = 1 and 2.
- **(Liouville)** the Gauss–Kuzmin run law log₂(1 + 1/(n(n + 2))).
- **(volume)** not computed. P-476 shows it does not suppress depth, so it has no normalisable sector law without a
  cutoff.

Also: the sector's share of all departures (n ≥ 2) under each normalisable law.

## Predictions (hand-derived)

| law | share of the run of 6 in the sector | the sector's share of all departures |
|---|---|---|
| moves | 31/32 = 0.96875 exactly | 1/31 ≈ 0.0323 |
| length, s = 1 | 0.487 ± 0.01 | 0.109 ± 0.01 |
| length, s = 2 | 0.85 ± 0.01 | 0.028 ± 0.005 |
| Gauss–Kuzmin | 0.50 ± 0.05 | 0.10 ± 0.02 |

**Disclosed:**
- The move and length values were computed earlier this session as scratch arithmetic, reported to the owner as
  such, not pre-registered. This check is their committed computation.
- The Gauss–Kuzmin values are hand estimates. The departures' total there is 1 − log₂(4/3).

**What would refute:** any value outside these ranges.

## What follows if all hold (to be stated in the note)

- **Under (C) the clock rides on (N2).** It is not a separate choice. Under plenitude the measure is the critical one,
  and the run of 6 is the most likely line-sector departure (about one half), not a certainty. τ becomes a
  distribution over the apexes τ*_n, n ≡ 1 mod 5, and most departures leave the sector (about 90% under
  Gauss–Kuzmin).
- **Under moves** the run of 6 is nearly certain (31/32), but moves are not the read-out history's own time.
- **The record's candidate,** the golden thread with one departure, is typical only near the golden end of the s-axis
  (P-441, "the principle's golden path"), that is, if the substitution itself is the selection (P-465), not plenitude.
  That tension is named here and not resolved.

0 of 19.
