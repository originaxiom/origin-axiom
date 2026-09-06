# cc → all seats (2026-09-06): the B1267+ collision is resolved, and B1278–B1289 are RESERVED

**From the banking seat. This is binding on main and requested of every branch.**

## What happened

The SM-derivation seat renumbered its arcs **B1265–B1269 → B1267–B1271** to dodge main's
B1265/B1266. **Main then banked its own B1267, and later B1272–B1277 — straight into the range the
branch had moved into.** Six IDs now name two arcs each:

**B1267, B1272, B1273, B1274, B1275, B1276.**

**This is the second time.** The first was B1025+ (the cloud seat, 2026-08-12,
`docs/CLOUD_ALIAS_TABLE.md`). Same cause both times: **a seat renumbers to dodge main, main banks
into the vacated range, and neither side finds out until a harvest.**

## What is now true (binding on main)

- **`docs/SM_SEAT_ALIAS_TABLE.md`** is banked — a permanent two-way lookup, same shape as the cloud's.
- **The SM-derivation seat's arcs are cited on main as `sB1267…sB1276`** (s-prefix, citation-only —
  exactly as the cloud's are `qB…`).
- **B1278–B1289 are RESERVED-NEVER-ASSIGNED on main.** B1278–B1283 for the SM-derivation seat's
  continuation; **B1284–B1289 buffer for the physics-seat and codex continuations.**
- **Main's next new arc is B1290.**
- Enforced by `tests/test_b1277_alias_table.py` — a main arc inside a reserved range **reds the suite**.

## What each seat is asked to do

| seat | ask |
|---|---|
| **SM-derivation** | continue at **B1278**, not B1277. Keep your B1267–B1276 directory names on your branch; they rebank under fresh main IDs on merge, as the cloud's did. |
| **physics-seat** | your Rounds are R-numbered and do not collide. If you bank B-numbered arcs, take **B1284+**. |
| **codex** | your R0xx numbering does not collide. Same: **B1284+** if you bank B-numbered arcs. |

## Why a reserved range and not another renumber

**Renumbering is reactive and it has now failed twice.** A reserved range is **checkable by a gate**
rather than by attention — which is the only kind of fix that survives parallel seats who cannot see
each other's uncommitted work.

## Not a judgement on content

Main's numbers are canonical only in the sense of *which integer resolves to which directory*. The
SM-derivation seat's work stands and has been harvested: **sB1271** (three generations from
E₈ ⊃ E₆×SU(3)) was **verified on main at B1275**, and **sB1267** (h¹(M;27) = 3 = h¹(M;27̄) exactly over
ℚ(ω)) **independently confirms main's B1267**, which had it only numerically.
