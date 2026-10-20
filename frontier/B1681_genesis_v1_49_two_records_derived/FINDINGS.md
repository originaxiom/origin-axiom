# B1681 — GENESIS v1.49: GM1 DERIVED GIVEN ONE INPUT (two records follow from a non-trivial common character in SL(2, ℂ)), AND THE PRINCIPLE'S FORM STATED AS THE FAMILY OF WORDINGS

**Verdict: PROVED (an amendment arc).** cc (main), 2026-10-20. POINT_REGISTER P-208, after the full suite of S150. 0 of 19.
- **What it amends.** GENESIS.md, the foundation document, from v1.48 to v1.49, through `adoption/amend.py` against a
  hash-pinned copy of v1.48 (`received/GENESIS_v1_48_main.md`).
- **The grounds.**
  - **B1677** (sealed, every cell held): a common point among the finite non-abelian SU(2) characters exists only at two
    records, for n ≤ 4.
  - **B1679** (the SM seat's W109, verified on main): the same for every n, in SL(2, ℂ), with no finite image assumed.
  - **B1676** (the SM seat's W107, verified): the golden rule's tick is a class property.
  - **P-206**, the SM seat's proposal to state the principle as the family.

## 0. Seen first

`VERDICT topic-sweep /GENESIS|GM1|two records|amend/: 96 of 1453 arcs on main match (NEGATIVE 15, OPEN 10, PROVED 71)`
— chiefly B1454 (GENESIS v1 adopted), B1662 (v1.48, the last amendment), B1323 (the words route and C2b), and B749
(fork F9, the substrate count). **Literature:** none beyond the grounds' own (B1677, B1679).

## What changes in GENESIS

| item | v1.48 | v1.49 |
|---|---|---|
| GM1, two records | POSTULATED | **DERIVED given one input**: the records have a non-trivial common character in SL(2, ℂ). The finite image at n = 2 is forced (Q₈), the triplet follows from that point (T2), and the rank-two target stays priced (P-209) |
| the words route | aperiodic → Sturmian → golden slope (C2b) → LP | the same, and **the principle's form is the family of wordings**: a → ab, b → a is its smallest instance under C2b, not forced. Results stated of the golden rule's word, clock or tick are thread results (B1676) |
| the log | — | a v1.49 entry. v1.29's "the principle's tick" reads "the golden rule's tick"; the history is not rewritten |

## What it does not do

- **It does not re-count the price.** One postulate is exchanged for one input. Whether the input is weaker than "two
  records" or the same choice renamed is the web seat's question, and it is open.
- **It does not touch GM4 (the carrier), GM5c (the swap) or GM5d (positivity).**
- **It derives no number.** 0 of 19.

## Files

- `received/GENESIS_v1_48_main.md`: v1.48 as amended, hash-pinned in the script.
- `adoption/amend.py`: the amendment, with `--check`.
- The lock: `tests/test_b1681_genesis_v1_49.py`.
