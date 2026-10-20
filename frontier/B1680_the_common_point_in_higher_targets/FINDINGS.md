# B1680 — THE COMMON POINT IN TARGETS OF HIGHER RANK: in every target tested a common point exists only at two records, and at two records it is always a Heisenberg point (Q₈ in SU(2), H(3) in U(3), H(5) in U(5)); no other finite image has one, even at two records

**Verdict: PROVED, as sealed.** cc (main), 2026-10-20. POINT_REGISTER P-209 (step 2 of main's plan). 0 of 19.
- **The order.** Sealed at `8b91162f8` (preregistration sha256 20074d73, instrument 188a4f15) and pushed before the run.
  One run of 160 s. Its output was committed unread at `bb43604dd`, with the instrument's hash identical at the seal,
  at the run and at the commit.

## 0. Seen first, and disclosed

As sealed: `VERDICT topic-sweep /common point|Heisenberg|clock and shift|Stone.von Neumann|PSL\(2, ?7\)|Klein|Delta\(54\)|higher.rank target|Sp\(2\)/: 29 of 1451 arcs on main match (NEGATIVE 4, PROVED 25)`.
The preregistration's §0b discloses:
- the n = 2 Heisenberg controls (Stone–von Neumann);
- the Sp(2) argument for the Heisenberg family at n ≥ 3;
- the filter;
- the smoke test, with every order checked and the controls at n = 2;
- Dunwoody for the solvable targets;
- the observation that p = 2 and p = 3 both give three.

No non-control target and no n ≥ 3 case was run before the seal.

**Literature:**
- the Stone–von Neumann theorem for finite Heisenberg groups (the Weyl, or clock-and-shift, representation);
- the finite subgroups of SU(3) (Miller, Blichfeldt and Dickson 1916);
- Klein's 3-dimensional representation of PSL(2, 7);
- Dunwoody 1970 and Gilman 1977;
- the SL(n)-invariants of Λ²: a trivial summand occurs only for n = 2.

## 1. The sealed run (`verification/the_common_point_in_higher_targets.py`, `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **C0** (n = 2) | H(3), H(5) and Q₈ have a common point | **HOLDS.** Every generating pair is fixed by every move: Q₈ 24, H(3) 432, H(5) 12 000 |
| **C1** (n = 3) | no target has a common point | **HOLDS.** H(3)'s 3 888 filtered generating triples are all moved, and no other target has a filtered triple |
| **C2** (n = 4) | no target of order ≤ 60 has a common point | **HOLDS.** No target has a filtered quadruple |

**Read-out, not a cell.** At n = 2 the targets with a common point are exactly the Heisenberg groups: Q₈ (the p = 2
Pauli group, up to signs), H(3) and H(5). 2T, A₄, S₄, A₅, Δ(54) and Klein's PSL(2, 7) have none: no generating pair
even passes the equal-trace filter.

## 2. What it says

- **Two records holds beyond SL(2).** In every target tested, U(3) and U(5) included, a common point of the weave of n
  records exists only at n = 2. The reason is the one disclosed: the moves preserve the commutator pairing exactly in
  rank two (SL(2) = Sp(2)).
- **The common point of two records is a Heisenberg point,** in every target tested. Its structure is the commutator
  pairing of the two records, and a target supplies only the prime p (the size of the clock and shift).
- **So the remaining choice is the prime.**
  - **p = 2** is SU(2), the quaternion (Pauli) point. Its 2² − 1 = 3 non-trivial directions are the three parities, and
    the triplet follows (T2).
  - **p = 3** gives a 3-dimensional Heisenberg point. Its 3² − 1 = 8 non-trivial directions are not a triplet.
  - Only p = 2 gives the record's triplet as directions; p = 3 gives three only as a dimension. The disclosed
    observation is sharpened: the triplet as the paper builds it (three parity lines) is p = 2's.
- **The scope.**
  - These are finite targets in U(3) and U(5); other ranks and infinite images are outside the claim.
  - The Heisenberg family at n ≥ 3 is decided by the argument and confirmed on H(3) only.
  - It fixes no number. 0 of 19.

## 3. Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt` (the seal).
- `verification/the_common_point_in_higher_targets.py` (sealed), with `.json`, `_run.txt` and `_time.txt`.
- `verification/before_the_seal/`: the smoke test of the orders and the controls.
- The lock: `tests/test_b1680_the_common_point_in_higher_targets.py`.
