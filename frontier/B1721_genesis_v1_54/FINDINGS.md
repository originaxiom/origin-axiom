# B1721 — GENESIS v1.54 (a correction amendment; the integrity sweep of 2026-10-22, P-291): v1.53's three overreaches corrected — FK10's string count and its condition, FK9's W57 sentence tagged, FK12's CP sentence held to its sources

**Verdict: PROVED** (an amendment; each correction restates what its source shows). cc (main), 2026-10-22. **0 of 19.**

## Seen first

`VERDICT topic-sweep /GENESIS v1\.5|FK10|FK9|FK12|overreach|string count|Leray/ (full text, aliases: the cusp's unit): 104 of 1492 arcs on main match (NEGATIVE 20, OPEN 1, PROVED 83)`. The predecessor is B1715 (v1.53). The sources are B1708 and B1710 (the strings, the Leray condition), HARVEST_LEDGER
row 1099 (W57 at headline level; P-091), P-149 and B1652's addendum (the CP sentence), and P-277. **Literature:** none.

## What changed (`adoption/amend.py`, against the hash-pinned v1.53 in `received/`)

Found by main's math referee in the integrity sweep (P-291), and checked against each source:
- **FK10.** "Close at 12 or 24 strings" becomes "close at 12χ(O_S) strings" (12, 24, 36, …). The triplet's count is now
  stated as given the SM seat's reduction of the 4d Dirac index to Riemann–Roch on the base, which B1710's own claim line
  carries and v1.53 dropped.
- **FK9.** W57's "no draw within 32σ" is registered at headline level only and not re-run on main (row 1099, P-091). It
  is tagged as the seat's, unverified on main, as GENESIS's reliance-tag convention requires (v1.51).
- **FK12.** "Is where a CP sign is chosen" becomes "would have to be chosen" (P-149's own words). The conjugate-vacua
  reading is attributed to the web seat (post hoc in B1652's addendum), and P-277 is cited as open.
- **The log:** a v1.54 entry above the unrewritten v1.53 entry.

## Files

- `adoption/amend.py`; `received/GENESIS_v1_53_main.md` (sha256 bbc17bdd…).
- The lock: `tests/test_b1721_genesis_v1_54.py`.
