# W-F16: the two-way choices settle each other, with one test left. The hand, the arrow and the tick parity settle among themselves; the order, the Higgs reading and the hypercharge sign settle among themselves if the order fixes the hypercharge sign (W-F13's criterion 3) and the order and the Higgs bit flip together as a symmetry (D∘C). That is main's test

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free), with a reading. This note closes
card W-F16 (`relays/cards/CHAT1_W-F16_the_two_way_choices_settle_each_other.md`, df84ef44c). The card was approved by
the author on 2026-11-14 (status file).

**How it was checked.** Computed once, on this seat's own code; expectations committed first; tested against planted
errors (1, caught).
- **The sealed run.** The script (sha256 `1e390d50…b2ae5890a4f924`, pushed at df84ef44c) was run once; its output was
  committed (da4cc8a26) before it was read. All three expectations were met.
- **The method.** Exact arithmetic mod N (H1) and over one prime field, 18000601 (H2). The helpers are W-C8 part 2a's.

## 1. The thesis, made countable

- **The kind.** Every choice that survived is a pair exchanged by an involution: a ℤ/2-torsor.
- **A bit flipped by a symmetry** of everything the structure computes is a convention.
- **Two bits flipped together** by one involution keep their relative sign under it. If a relation fixes that sign,
  fixing one fixes the other; if none does, the relative sign is itself a free bit (H3's fourth row).
- **The free bits** are the number of bits, minus the rank of the relations, minus the rank of the symmetries (over
  F₂), every symmetry preserving every relation. This is the log₂ of the number of orbits of the symmetries on the
  solutions of the relations.

## 2. The results

| line | result |
|---|---|
| H1 | **The hand law** h = o + e (the hand of ±JⁿKᵉ at the mark is (n + e) mod 2) holds for every odd m from 1 to 41, n = 0 to 7, e ∈ {0, 1}, both signs. This reproduces W-C8 part 1 (m ≤ 11) and extends it |
| H2 | **The mirror** (the tick acting on the fibre, t fixed) pulls every record module back to a module. It **preserves the index on every one**: 12, 210 and 1,892 modules at golden levels 4, 6 and 8, and 56 at bronze level 2. This extends W-F9's referee check at golden level 4. It is what W-F9 § 2.3 implies: the mirror sends the peripheral subgroup P to aᵐPa⁻ᵐ, so the equality follows by hand, and the computation confirms it. The plant (t ↦ t⁻¹) failed the relators at every level; it tests the relator check only |
| H3 | **The count of free bits** among (hand h, tick parity o, undoing e, order r, Higgs reading q, hypercharge sign y) is given below |

The H3 variants:

| symmetries | relations | free bits |
|---|---|---|
| J, K, D, C | h + o + e; q + y | **0** |
| J, K, D (C not a symmetry) | h + o + e; q + y | **1** |
| J, K, D∘C | h + o + e; q + y; r + y (W-F13's criterion 3) | **0** |
| J, K, D∘C | h + o + e; q + y | **1** |

## 3. What it means

- **The hand, the arrow and the tick parity settle among themselves.**
  - The relation h = o + e is proved by hand for every odd m (part 1) and computed here to m = 41.
  - The tick flips (o, h) and the undoing flips (e, h).
  - So none of the three is free: given any two, the third follows, and the remaining freedom is moved by symmetries.
  - "The hand is the arrow" holds in this precise sense: hand = parity + undoing.
- **This block does not reach the order.**
  - The mirror flips the hand at the mark (it is the tick acting on the fibre), but it preserves the index on every
    record module computed (H2).
  - So no involution computed ties the hand to the order. At orientable levels the order is not the hand, as W-F9 said.
  - The undoing's action on the index is not computed. That it keeps the order (as H3 assumes) rests on W-F9 § 2.3, if
    the undoing is realised by an automorphism keeping the cusp.
  - The bits form two blocks: {hand, arrow, parity} and {order, Higgs reading, hypercharge sign}.
- **The second block settles if one of two things holds:**
  - charge conjugation C (with S ↔ S̃) is by itself a symmetry of the frame's output, with duality D also one (H3's
    first row); or
  - the order and the hypercharge are tied (W-F13's criterion 3), and duality combined with charge conjugation, D∘C, is
    a symmetry (H3's third row).
  - M24 reports that the two readings' limits differ, which suggests C alone is not. Then everything rests on criterion 3
    and D∘C: does the frame assign its hypercharge through the matter modules, and does flipping the order and the
    Higgs reading together leave the frame unchanged?
  - If both, the order and the Higgs bit settle each other, and no choice is left anywhere. If D∘C is a symmetry
    without criterion 3, one bit remains: the order's sign against the hypercharge's (H3's fourth row). If D∘C is not
    a symmetry, at least one bit remains, and it is a genuine input.
- **Main's test.** Run the frame with the degree-2 reading and S ↔ S̃, and compare it with the frame as it stands. It
  needs the frame's readings, which this seat's firewall holds. A prediction for main: by the author's thesis, D∘C is
  a symmetry and criterion 3 holds, so the count is zero.
- **What would prove the thesis wrong here:** the frame's output changing under D∘C, with C alone also not a symmetry
  and no relation fixing the Higgs reading. Analyticity adopted as a line would break D∘C, but it is such a relation:
  with criterion 3 (or with D a symmetry) the count stays zero. The bit would then be settled by an inside principle,
  not by its partner, and W-F9's irreducibility would need revisiting (W-F13 § 3).

## 4. Typed

| statement | how checked |
|---|---|
| H1, odd m ≤ 41 | computed once; expectations committed first; reproduces W-C8 part 1 (m ≤ 11); recomputed independently by the referee (n ≤ 15); by hand for every odd m (part 1, not independently checked) |
| H2 | computed once; expectations committed first; tested against planted errors (1, caught; the plant tests the relator check only); follows by hand from W-F9 § 2.3; recomputed independently by the referee (golden 4 and 6, bronze 2; two primes each) |
| H3 | computed once (F₂ ranks); expectations committed first; recomputed independently by the referee (orbit enumeration on F₂⁶) |
| the two blocks, and the second's dependence on criterion 3 and D∘C | a reading |
| D∘C is a symmetry of the frame's output | a prediction, for main to test |

## 5. Files

`relays/chat1_2026-11-14_wf16/`: `wf16_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf16_checks_out.txt`,
`wf16_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
