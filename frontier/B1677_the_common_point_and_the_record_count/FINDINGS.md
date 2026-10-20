# B1677 — THE COMMON POINT AND THE COUNT OF RECORDS: among the finite non-abelian SU(2) characters, the weave of n records has a common point only at n = 2 (for n ≤ 4) — the quaternion point — so the count of two records follows from the existence of a common point, and the triplet with it

**Verdict: PROVED, as sealed.** cc (main), 2026-10-20. POINT_REGISTER P-205 (first in the foundations quest) and P-201.
0 of 19.
- **The order.** Sealed at `33a40692b` (preregistration sha256 85f3fb67, instrument 76f45370) and pushed before the
  run. One run of 16 s. Its output was committed unread at `2b04ffa80`, with the instrument's hash identical at the
  seal, at the run and at the commit.
- **Why.** The owner asked for the best parameter-free structure that could show the principle has real ground, and
  whether "two records" (GENESIS GM1, a postulate) is forced (P-201, P-205).

## 0. Seen first, and disclosed

As sealed: `VERDICT topic-sweep /common point|quaternion point|Nielsen|generating (pair|triple|tuple)|record count|substrate count|two records/: 14 of 1448 arcs on main match (NEGATIVE 1, PROVED 13)`.
The preregistration's §0b discloses:
- the design facts;
- the counts by hand;
- Dunwoody's theorem for the solvable groups;
- the trace-zero argument;
- the rank-2 smoke test;
- the SM seat's exploratory rank-3 note.

No rank-3 or rank-4 case was run before the seal. **Literature:** Neumann and Neumann 1951; Dunwoody 1970; Gilman
1977 (transitivity of Aut(F_n) on generating n-tuples of PSL(2, p) for n ≥ 3); Procesi, and Fricke–Vogt (the
trace coordinates).

## 1. The sealed run (`verification/the_common_point.py`, `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **C0** (n = 2, control) | the quaternion character is the only common point among the groups | **HOLDS.** Q₈ (Dic₂): 24 generating pairs, one common character, traces (0, 0, 0). Every other group has none: 2T's 24 and 2I's 120 filtered pairs are all moved |
| **C1** (n = 3) | no common point | **HOLDS.** Filtered generating triples exist for Q₈ (48), 2T (48) and 2I (240), and every one is moved |
| **C2** (n = 4) | no common point | **HOLDS.** Only 2T has filtered generating quadruples (48), and every one is moved |

## 2. What it says

- **The common point fixes the count of records.**
  - Among the characters of F_n in SU(2) with finite non-abelian image, a point fixed by every move of the weave
    exists only at n = 2, for n ≤ 4. There it is unique: the quaternion point.
  - So the count of two records (GM1) follows from a weaker, stated input: **the weave of the records shares a
    persistent point, in SU(2), with a finite non-abelian image.**
  - The triplet then follows from that point: three parities, 2T, the A₄ triplet, the Γ(4) theta multiplier (the
    paper's T2, T3).
  - This is the first time a postulate of the record's foundation has been replaced by a consequence of a weaker
    input.
- **The binary dihedral family is covered for every m** (an argument after the run, labelled). A generating set of Dic_m
  needs a trace-zero element. The filter then forces every generator and every pairwise product to trace zero, and
  such elements generate at most Q₈. So m ≥ 3 never has a common point; the census's m ≤ 15 are instances. With the
  cyclic groups abelian, the list Dic_m, 2T, 2O, 2I is every finite non-abelian subgroup of SU(2).
- **What is new and what is not.** That the Nielsen moves act transitively on generating n-tuples for n > d(G) is known
  for solvable groups (Dunwoody) and for PSL(2, p) (Gilman). The census confirms it, including the non-solvable 2I at
  n = 3 and 4. The reading is the record's own: the existence of a common point is what fixes the count of records.
- **The scope.**
  - The input "SU(2), finite image" is a choice; it stays priced.
  - Characters with infinite image, and targets other than SU(2), are outside the claim.
  - n ≥ 5 is not covered: a sub-tuple can pass the filter without generating.
  - Whether the principle *requires* a common point is a reading: "something persists under every act" is close to
    "existence is what remains", but it is not derived.
- **Graded on the record's two axes.**
  - *Importance:* high. It is the first structural link from the principle's shape to the count that gives "three",
    and it could have failed (2I is not solvable).
  - *Evidence:* a sealed census with a theorem behind most of it. It fixes no number. 0 of 19.

## 3. Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt` (the seal).
- `verification/the_common_point.py` (sealed), with `.json`, `_run.txt` and `_time.txt` (the run).
- `verification/before_the_seal/`: the design facts and the rank-2 smoke test.
- The lock: `tests/test_b1677_the_common_point_and_the_record_count.py`.
