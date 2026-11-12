# B[[N]] — The thread results on every thread to length six: what the weave shares and what one thread has

*Main, 2026-11-12 (S306p). The first step of the plan's package WP-1.5 (the root, selection, and thread results), and
main's recomputation of the weave rows of the harvest that a second session had checked (rows 908 to 922; its card
X-C1a). Everything is computed by main's own instrument; none of the SM seat's code is run. Sixty digits for the
readings on covers, exact arithmetic for the lines at the common point. No measured number is read. 0 of 19.*

## 1. The answer first

- **The package's question:** under the weave's rule no thread is chosen. Which results survive as statements about
  the weave, and is the root anything more than an origin of coordinates?
- **What survives as a statement about the weave** (true on every state computed, each with a proof that uses nothing
  of one thread):
  - the three classes of a state by its act on the three parities, and that no state has its three parities both
    separate and carried into one another at its own tick (row 917; 758 states);
  - no rank-one line on a once-punctured-torus bundle is interior (row 918; all 24 states, exactly);
  - where a forced cover has members with a parity, a third of them sit on each parity (row 910; seen on ±LR).
- **What is a thread result:**
  - members at characters of order 4 and 3 on the forced cover appear only on ±LR among the twelve odd-trace threads
    to length six (row 922): +LR has 54 members in 8 orbits of the deck group among its 1,024 characters of order dividing 4, and 6 among its 81 of order dividing 3; −LR has 6 and 6; the other ten threads have none among their 15,946 characters;
  - at the tick where the weave separates the parities, members sit on exactly two of the three or on none, state by
    state (row 916): six states carry members (±LLR, ±LLLLR, ±LLRR), each on exactly the two parities its own symmetry exchanges; eighteen carry none, the twelve odd-trace states among them; none carries a member at the zero parity;
  - the three-ended covers: +LLLR's and −LLLLLR's each carry exactly three members that read (−1, −1), so the three-orbit singles out no state; on all thirteen covers every member at a sign character reads (−1, −1) and no member of order four does (row 909).
- **The root.** Among the twelve odd-trace threads the golden pair is the only one whose forced cover has members.
  That is a fact about two threads, found by a census with a rule named in advance. It is not a rule of the weave that
  picks them, and the plan's fork on the root (FK9) is not ruled by it.
- **Every cell of the seat's rows that main recomputed is the seat's.** Main's instrument is a different one (§ 2),
  and at the sign characters it also reproduces main's own stored census.

## 2. The instrument

Main's earlier instrument for a cover (B1602) reads the cover through SnapPy's triangulation of it and SnapPy's own
presentation of its group. That presentation does not say how the cover's group sits in the base's, so it gives no
deck action on the cover's characters: no orbits and no parities. The rows to recompute are about orbits and parities.

**The kernel site** (`kernel_site.py`) builds the cover's group from the base's presentation alone, by the method of
Reidemeister and Schreier: a transversal, the generators and relators it gives, the cusps as cosets of the peripheral
group's image, the holonomy by multiplying the base's own matrices, and the deck group's action on characters as
integer matrices. The reading is B1492's, unchanged: h¹ from the Fox matrices, r¹ the rank of the restriction to all
cusps at once, n = h¹ − r¹.

| guard | what it holds |
|---|---|
| the number of generators | \|Q\|(g − 1) + 1 |
| every relator in the holonomy | to 10⁻³⁰ (found: 10⁻⁵⁰ or better) |
| each peripheral pair commutes | to 10⁻³⁰ |
| the deck matrices | carry characters to characters |
| the sealed code on the same presentation | gives the fast assembly's answer |
| the sign characters | read as B1602's stored rows, as multisets: two presentations of one group, one reading |

- **Sixty digits.** B1492's module sets forty; at forty the peripheral pairs of the longer threads' covers commute
  only to 10⁻²⁹. SnapPy's high-precision holonomy carries 63.
- **Shortened presentations.** A base group with three generators gives a cover with 25. Tietze moves bring it to
  about ten, which makes a reading twelve times faster and changes nothing that is read.
- **Orbits.** A deck transformation carries the module to an isomorphic one, and the frame is a real module, so a
  character, its deck images and its complex conjugate read alike. One character of each orbit is read, and every
  orbit that holds a member is then read in full.

## 3. What was recomputed, row by row

| row | the seat's statement | main's computation | result |
|---|---|---|---|
| 908 | the room census: 27 companions, 26,158 sign characters | main's own enumeration | every one of 247 cells equal |
| 914 | the group on the triplet | the rotations of the cube, order 24, with the sign 48 | equal (the group part; the reading about mixing is not opened) |
| 917 | the trichotomy and Theorem S | 758 states: 326 three-cycles, 268 involutions, 164 identity; the normaliser's image of order at most 2 on the 164 | equal |
| 922, 910 | twelve threads at orders 4 and 3; 48 members, 16 per parity | the forced tetrahedral cover of each of the twelve threads as a kernel; 13,824 characters of order dividing 4 and 3,564 of order dividing 3, in orbits of the deck group with conjugation; 1258 readings at 60 digits; the deck group's translations and the four punctures for the parities | equal on all twelve: the numbers of characters, of members and of orbits. On +LR the members' structures are 24 × (3, 2, 1), 24 × (1, 0, 1) and 6 × (4, 0, 4); 24 are fixed by one translation, 24 live on an edge between two punctures, 6 are fixed by all three: 48 with a parity, 16 on each. On −LR the 6 are fixed by one translation each, 2 on each parity. The 480 sign characters read as B1602's stored rows, and every member orbit read in full reads alike |
| 916 | the parity sectors at the resolving tick, 24 states | the tick as the kernel of the map to ℤ modulo 3, 2 or 1; the 48 characters whose fibre restriction is a parity, with κ a twelfth root of unity; 1,152 readings | equal on all 24 states: the tick, the number of parities with a member (two or none, never one, never three), one member on each, and the structure (2, 1, 1) on ±LLR and ±LLLLR. On +LLRR the two members read (1, 0, 1) and on −LLRR (2, 1, 1) |
| 918 | the frame at the common point; Lemma V | 768 characters of order dividing 4 on the 24 ticks, exactly: h¹ ≤ 1; where h¹ = 1 the character is trivial on the cusp and the class restricts to it injectively; one line on each parity, 72 in all | equal; the proof read and found right |
| 909 | the three-ended covers: thirteen on ten states, 138 members | the covers by rule: every map of a state's group onto ℤ/3 that kills the peripheral pair, up to sign; ten states to twelve ends and eight letters, thirteen covers; the characters of order dividing 4 in orbits; the members' readings by B1493's own code on the kernel's presentation; 410 readings | equal on every state: 138 members, 18 at sign characters and 120 of order four; the readings (−1, −1) at the 18, and (−1, 0) at 36, (0, −1) at 72 and (0, 0) at 12 of the others; no member on −LLRLR, +LLLLRRR and the four covers of +LLLRRR. Each member has one interior class |
| 912 | the spin cover, held by the seat as a draft | not recomputed | it is on no path of the map |
| 915 | a synthesis of the rows above | nothing of its own to compute | — |

## 4. What is not shown

- **Why members appear only on the golden pair.** The seat cites that ±LR are the only arithmetic odd-trace primitive
  threads. Twelve threads are a pattern.
- **Any count of generations as physical.** A member is a character with an interior class. Which count is physical
  is the foundation's fork on the deck (FK7), which this arc does not touch.
- **Threads longer than six letters,** and characters of other orders.

## Seen first

`python3 scripts/checks/topic_sweep.py` for the forced cover, the three-ended covers, the parity sectors, the
resolving tick, the common point and covers built from a presentation: 34 of 1,643 arcs match. B1600 verified the
weave's first facts and the parity lemma on main. B1602 read the forced cover of every thread to length eight at its
sign characters, through SnapPy's triangulation of the cover. B1492 and B1493 hold the reading and the room on the
three-ended companion of +LLLR. None reads characters of order 4 or 3 on the forced covers, the parity sectors at the
resolving tick, the lines at the common point, or the three-ended covers of the other nine states; and none builds a
cover from the base's own presentation. Register row P-419 holds selection as an object of study, as a lead.

**The literature:** not searched. The method of Reidemeister and Schreier and Tietze's moves are standard and are
used, not proved.

## Disclosed

- **The first run of the twelve threads was stopped** after the six threads with 13-generator covers: the other six
  took four minutes a reading. They were read again with shortened presentations. The stopped run's 72 readings of
  those covers are kept apart and were not used.
- **A double-precision reading was tried and removed:** the singular values it kept and those it dropped met at 10⁻⁷.
- **Main read the seat's statements and its tables before computing,** so nothing here is blind to them.

## Reproduce

```
python3 -B frontier/B[[N]]_[[slug]]/verification/the_twelve_threads.py 6
python3 -B frontier/B[[N]]_[[slug]]/verification/the_twelve_threads_read_out.py
python3 -B frontier/B[[N]]_[[slug]]/verification/the_parity_sectors_on_main.py
python3 -B frontier/B[[N]]_[[slug]]/verification/the_common_point_on_main.py
python3 -B frontier/B[[N]]_[[slug]]/verification/three_ended_covers_on_main.py
python3 -m pytest -q frontier/B[[N]]_[[slug]]/verification/
```
