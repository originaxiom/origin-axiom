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
