# B1173 — THE DIGEST PARTIAL-CLOSE (O4): 45 dispositioned / 13 NOT-REACHED → L185; the qor5up branch released

**Status: banked (frontier). Verdict OPEN** (a process close; the residue stays reopenable). Owner-directed
O4 (the approved default: dated PARTIAL-CLOSE + release qor5up). `verification/reproduce.sh` → `REPRODUCES`.

**What closed:** the B1060 digest ledger — the program's anti-cherry-picking backbone (58 rows, all EMPTY at
open by design) — had stalled at 13 EMPTY rows since 2026-08-14, holding the qor5up branch hostage
(REVIEWS: "STAYS until the digest's remaining rows finish porting"). The partial-close: header →
`CLOSED-PARTIAL (2026-08-27, B1173)`; the 13 rows (lanes 3.1–3.5, 4.1–4.7, 5.01–5.12) typed
**NOT-REACHED** — *a deliberate deviation from the plan's `UNPORTED-AT-CLOSE`: the ledger's own sealed
vocabulary already contains the honesty row, and using it respects the vocabulary instead of widening it* —
each with a pointer to **L185**, the umbrella residue lead (one row, not thirteen; the denominator stays 58;
any future sitting reopens a row by dispositioning it under a new arc). **The renumber collision fixed:**
the stale "qL155–qL166 → L165+" instruction (written when main's next lead was L161) collided with main's
live L165–L184; corrected to **L185+**, with the alias table as resolver. **The qor5up release:**
FROZEN-RECORD-PENDING → **FROZEN-RECORD-CLOSED** (the owed registry entry landed by append-only inter-review
note; **R47-3 and R48-5 discharge** — two of Review 50's carried items closed before it opens). The stale
OPEN_LEADS currency stamp ("next lead L175") corrected to L189. `test_b1060_digest` updated to pin the
closed state (zero EMPTY; 13 NOT-REACHED; L185; the release).

**Fences:** nothing is lost — every NOT-REACHED row remains readable at the frozen branch via
`docs/CLOUD_ALIAS_TABLE.md` and is queued at L185; qL164 was already owner-DECIDED; the two-κ (qL159) and
shadow-library (qL160) rows flagged as the likeliest early reopens. Process arc; no mathematics; Gate 5
clean. Not kill_graph-routed.

## Status note, 2026-11-10 (S306n)

ESCALATED(2026-11-10, P-745). This is a process arc of 2026-08-27; its verdict OPEN is the convention of that date for an arc with no theorem, and is not changed here.
- **What it left open, in its own words:** the thirteen NOT-REACHED digest rows sit under the umbrella lead L185, reopenable row by row; the two-κ and shadow-library rows were flagged as the likeliest reopens.
- **Next action (P-745):** check each named residue against today's record, with a quote at the deciding file; close what was discharged, and re-point what was not to the register row that carries it.

## The residues checked, 2026-11-13 (main's card C11; register row P-745)

Each residue this arc names in its own words, checked against the record as it stood on 2026-11-13, at the file that decides it today, by a quotation from that file. Where nothing decides it (UNREGISTERED), the file read is the one that names it. The lock is `tests/test_the_seven_process_arcs_checked.py`.

| residue | outcome | the file read | quotation | carried by |
|---|---|---|---|---|
| the thirteen NOT-REACHED digest rows under the umbrella lead L185 | CARRIED | `docs/OPEN_LEADS.md` | Review 74's reader proposed closing this lead; main's check did not confirm it. The disposition table is only in a gitignored audit draft, and the row it promises does not exist. | L185 |
| the two-kappa and shadow-library rows flagged as the likeliest reopens | CARRIED | `frontier/B1060_digest_ledger/DIGEST_LEDGER.md` | ∣ 4.6 ∣ the two-κ finding (qL159) ∣ NOT-REACHED ∣ — ∣ vs main's TERMINOLOGY register · NOT-REACHED at partial-close (B1173) → tracked at L185∣ | L185 |

**The arc stays OPEN.** ESCALATED(2026-11-13, P-745; carried by L185). A residue marked UNREGISTERED is decided by no row, lead or later arc; it is re-pointed to P-745, whose dated addition of 2026-11-13 lists it for main to row or to decline.
