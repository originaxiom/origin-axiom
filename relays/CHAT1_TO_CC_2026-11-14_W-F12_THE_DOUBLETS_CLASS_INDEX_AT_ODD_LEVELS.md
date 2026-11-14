# W-F12: at golden level 7 the class index is zero on all 48,778 doublets, as at levels 1, 3 and 5; the h¹-gap census follows the same pattern (±1 on |T| of each sign, ±2 on |T| − 1). Computed, not proved

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note closes card W-F12
(`relays/cards/CHAT1_W-F12_the_doublets_class_index_at_odd_levels.md`, a6fd41c1d). It takes up one of the structural
items W-F10 left open.

**How it was checked.** Computed once, on this seat's own code; expectations committed first.
- **The sealed run.** The script (sha256 `d5870981…edc0a992b30`, pushed at a6fd41c1d) was run once; its output was
  committed (1749bc6d3) before it was read. All three expectations were met. C3 was stated as a prediction from the
  pattern, to be reported either way.
- **The method.** Exact ranks over one prime field (25528933). The helpers are W-C8 part 2a's, taken by text.

## 1. The results

| level | fibre torsion \|T\| | characters | extension characters with a class | doublets | class index non-zero | h¹ gap +1 / −1 / +2 / −2 |
|---|---|---|---|---|---|---|
| 3 (control) | 4 | 16 | 4 | 64 | 0 | 4 / 4 / 3 / 3 |
| 5 (control) | 11 | 242 | 11 | 2,662 | 0 | 11 / 11 / 10 / 10 |
| **7** | **29** | **1,682** | **29** | **48,778** | **0** | **29 / 29 / 28 / 28** |

- **The characters.** Fibre part on coker(A_n − I), t-value a 2e-th root of unity (e the exponent), as in part 2a. The
  doublets are every non-split doublet on these characters. The \|T\| column is part 2a's E2; this run did not print it.
- **The control.** Levels 3 and 5 reproduce part 2a's post hoc 2 (G2, G3) exactly, with the same helpers.
- **A second computation.** The referee of this note recomputed levels 1, 3, 5 and 7 in full, on its own code and two
  other primes; all counts agree. It also checked the relators and the Euler characteristic, and ran two plants:
  - leaving out w makes the index non-zero (12 of 64 at level 3, 180 of 2,662 at level 5): caught;
  - replacing μ by t leaves the index zero: not caught, so the zero index does not test the choice of μ.
  The index is not trivially zero: n(V) = n(V* ⊗ w) = 1 on 6, 90 and 756 doublets at levels 3, 5 and 7.
- **The law.** W-F6's gap law held on every character at the three levels, 0 failures: h¹(ℓ) = [ℓ = 1] on the fibre
  and [ℓ(μ) = −1] off it. So the extension characters with a class are the trivial one and the |T| − 1 with
  ℓ(μ) = −1, and the doublets number |T| × (the number of characters).

## 2. What it means

- **The class index on doublets is zero at every odd level computed, 1, 3, 5 and 7:** 51,506 doublets in all (2 at
  level 1, from part 2a; 64, 2,662 and 48,778 at levels 3, 5 and 7, from this run). The statement "non-zero only on orientable levels" now has a fourth level of
  evidence. It is **still not proved**: this seat found no general argument.
  - One family, α ⊗ U (the tick's class), is closed under V ↦ V* ⊗ w, with α ↦ α⁻¹w. That alone does not give equal
    interior counts.
- **The h¹-gap census on doublets has a pattern:** ±1 on |T| of each sign, ±2 on |T| − 1 of each sign, at levels 3, 5
  and 7. The sealed script counted only these four values; the referee's full census found the rest at gap 0 (50,
  2,620 and 48,664) and none at |gap| ≥ 3. It is observed, not proved. It looks like a consequence of W-F6's law through the long exact sequence of
  0 → α → V → β → 0, but that is not worked out here.
- **For the ledger (W-F10):** this open structural item stays open, with more evidence. The typing is unchanged:
  computed on the levels named, not proved.

## 3. Typed

| statement | how checked |
|---|---|
| § 1's table | computed once (level 7); reproduced (levels 3 and 5: part 2a's post hoc 2, same helpers); expectations committed first; recomputed independently by the referee (levels 1, 3, 5, 7) |
| the class index is zero on every doublet at levels 1, 3, 5 and 7 (not proved in general) | computed once (levels 1 and 7); reproduced (levels 3 and 5, same helpers); recomputed independently by the referee |
| the h¹-gap pattern (observed at levels 3, 5 and 7, not proved) | computed once (level 7); reproduced (levels 3 and 5); recomputed independently by the referee |

## 4. Files

`relays/chat1_2026-11-14_wf12/`: `wf12_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf12_checks_out.txt`,
`wf12_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
