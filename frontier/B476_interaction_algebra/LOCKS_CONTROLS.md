# B476 addendum 2 — the locks are NOT a critical fingerprint (controls computed)

**Question: are the 16 sector-locks of the pair (1,2)@15 pair-data or level-forced?**
Controls: the off-critical pairs at their levels, same instrument (`locks_controls.py`,
`locks_controls2.py`).

| pair@level | ord | span | CRT product bound | CRT locks | parity sectors (dim: span) |
|---|---|---|---|---|---|
| (1,2)@15 | (20,12) | **49** | 5·13 = 65 | **16** | even 8: 49 (= total!), odd 7: 45 |
| (1,3)@27 | (36,9) | **147** | — (3³, no CRT) | — | even 14: 128, odd 13: 123 |
| (2,3)@63 | (12,24) | **252** | 17·21 = 357 | **105** | even 32: 252, odd 31: 252 (both = total!) |
| (2,3)@9 | (12,3) | 17 | | | even 5: 15, odd 4: 13 |
| (2,3)@7 | (3,8) | 21 | | | even 4: 16 (FULL), odd 3: 9 (FULL) |

**Verdict: locking exists at every pair tested — it intensifies off-criticality.** At
(2,3)@63 each parity sector determines the entire operator (100% cross-sector locking);
at the critical pair the even sector determines everything while the odd sector loses 4
dimensions. At (2,3)@7 both sectors are FULL and the deficit is purely cross-sector.
What is critical-pair-specific is the PATTERN (even-determines-all + exactly 16 CRT
locks at the minimal closing level), not the existence of locks. The B476 "16 locks"
reading survives but re-scoped: a fingerprint of the address, not of locking itself.
