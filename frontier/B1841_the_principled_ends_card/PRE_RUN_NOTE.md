# B1841 — PRE-READ NOTE: two clarifications of the reading, the inherited pins (before either card's look is read)

cc (main), 2026-11-05. Written while B1841's look runs and before its output, or B1839's, is read. Credit: the web
seat's hostile read, `relays/CHAT1_TO_CC_2026-11-05_B1841_AND_B1842_REFEREED.md` § 1, found the card correctly posed — "no
defect reaches a cell". It proposed what follows, and main adopts it. No cell, threshold, prior or instrument changes.

## Two clarifications of the reading

1. **E2 is the horoball at level ln 2,** B1840's rule: "the shallowest end at which the small-cut expansion's own disc is
   embedded". It is not the round disc |z| < ½; its boundary is that circle only at leading order, and the Frobenius term
   bends it. A pass at E2 is a pass at that level. The gloss "the largest round disc the cell holds" names where the level
   comes from, not the region.
2. **If B1841 passes and B1839 does not:** a principled end carries the six specifically, while a free level does not, the
   free level's larger look-elsewhere (23 ends against 4) costing it the screen.
   - B1841's own reading applies: A07 becomes CHOSEN, a discrete principled end priced among K = 4, with nothing fitted.
   - The candidate is frozen at B1841's best row with its entry.
   - B1839's fail is recorded as the free-level reading's, and the confirmation proceeds from B1841's row under GENESIS
     v1.62.

## Pins, completed and to be re-checked

- **B1839's dependency pins.** B1841 imports B1839's instruments, which read files B1841's ARTIFACT_HASHES did not
  carry. Their sha256 today is in `ARTIFACT_HASHES.txt`'s "after the seal" section, added by this note. They are the
  files B1839 pinned and are unchanged on main.
- **The two measured files** (B1637's HZ2021 masses, B1612's data.json) are recorded, not asserted at run time. The landing
  re-checks both hashes, as B1839's PRE_RUN_NOTE does. Both match compare.py's constants today.
- **E3 independently at every apex.** The web seat's committed check (`relays/chat1_2026-11-05_census3/apex_ends_check.py`,
  672c68160) applies E3's half-period identity at all 223 apexes. Its result is read at the landing.
