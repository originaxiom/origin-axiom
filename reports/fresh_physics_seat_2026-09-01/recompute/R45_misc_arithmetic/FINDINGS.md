# R45 — small arithmetic checks (Phase C, tier C-3, batch 3)

`r45.py` (PARI via cypari); output `r45_output.txt`.

| # | arc | claim | computed | verdict |
|---|---|---|---|---|
| 339 | B554 | h(ℚ(√5)) = h(ℚ(√29)) = h(ℚ(√−3)) = h(ℚ(i)) = h(ℚ(√φ)) = 1 | bnfinit class numbers 1, 1, 1, 1, 1 (ℚ(√φ) = ℚ[x]/(x⁴−x²−1), disc −400, signature (2,1)) | MATCH |
| 236 | B407 | φ⁴ + φ⁻⁴ = 7 | 7.000000 = L₄ | MATCH |
| 41 | B92 addendum | companion class number h(m²+4): unique class for m ≤ 5 and m = 7, 8; first non-uniqueness at m = 6 | h = 1,1,1,1,1,2,1,1 for m = 1..8 | MATCH (and R42 for m = 9..12) |
| — | B1067 (cross-check of sweep verdicts #1002/#1004) | fundamental unit and regulator of ℚ(√5) | fu = −φ (up to sign), regulator 0.4812118 = log φ | MATCH |

All MATCH; nothing changes a verdict of record.
