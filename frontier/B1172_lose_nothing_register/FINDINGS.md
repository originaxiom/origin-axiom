# B1172 — THE TRIGGER + THE BACKLOG + THE REGISTER: the relay-escalation instrument repaired and enforced; the 36-day backlog triaged; a nine-file retention-gap event found and filed (E51); the lose-nothing register banked

**Status: banked (frontier). Verdict OPEN.** The lose-nothing sweep (a 10-agent read-only workflow over 8
repo territories + a completeness critic) found the program's losses concentrated **at the seams**; this arc
executes the instrument-and-backlog half (Wave 1's S6/S7 + the owner's O3). `verification/reproduce.sh` →
`REPRODUCES`. Gate 5 clean (process instruments; no mathematics touched).

## 1. The relay-debt gate was silently DEAD — four repairs, now enforced

The sweep's finding, verified exactly: `scripts/checks/relay_debt.py` had (1) a **frozen clock** — `_today()`
read the ledger's own stamp, unchanged since 2026-08-09, so the 21-day rule *never fired* (the gate believed
no time ever passed); (2) **stale-never-fails** — stale debts were printed and swallowed by the gate wrapper;
(3) a **seat-blind regex** — only the cc3 lane matched; `CC_TO_CODEX_*`/`CC_TO_CLOUD_*`/`CC_TO_ALL_SEATS_*`
were structurally invisible (the MC1 assignment went unrowed *exactly there*); (4) a **dateless exemption** —
undated OPEN rows skipped the age check forever (the June-15 manifest was invisible for 10 weeks).

**All four repaired** (same commit as the triage, so the widened gate lands green): the real clock
(`OA_RELAY_TODAY` env override for deterministic tests); **stale FAILS the gate unless the row carries an
explicit `ESCALATED(date` marker** — escalation-by-name is now enforcement, not a print; every seat lane
matched (`<SEAT>_TO_<SEATS>_<date>_*`); dateless = stale-by-definition. Locked by the new dedicated
`tests/test_relay_debt_gate.py` (regex coverage, clock, marker, both exit paths against the real ledger).

## 2. The backlog, triaged (typed dispositions; computations became leads, not derailments)

- **`CC3_TO_CC_2026-07-22_p3_complete` (36 days, the oldest debt) → BANKED-as-triaged**: cc3's adjudication
  stands (8 CLOSED / 6 HELD); the **7 EXPOSED registered as L187** — the depth-closure backlog (B489, B500,
  B685, TOMB-L255, TOMB-L310, TOMB-L34, WALL-7; named stabilization paths, no new math; B500 doubly-owed
  with R28-6). "The kills are not wrong — underproved"; L187 is the finishing queue.
- **`HANDOFF_CC_SELECTION_COCHAIN` (24 days, row content-free) → ESCALATED + L188**: the actual awaits
  written for the first time — verify+bank the six claims per the packet's *own* reconciliation addendum
  (C1 extension / C2 stands / C3 corroboration-downgrade …).
- **`HANDOFF_MANIFEST` (dateless 10 weeks) → dated 2026-06-15 + ESCALATED**: content-audit = a named
  Review 50 item.
- **The nine 2026-08-09 rows → pre-escalated** (they were 3 days from tripping) — and the triage found:

## 3. THE RETENTION-GAP EVENT (E51): the nine relay FILES are lost; the rows are the only record

The nine 2026-08-09 relay files are **gone from main's working tree and on no reachable branch** — only
their ledger rows survive. The mechanism is the firewall's own design: relays are deliberately untracked, so
*nothing preserved them*; a between-sessions cleanup silently deleted the batch. **This is the L114 class one
level down** — B999's "branch protection preserves FILES; nothing preserved FINDINGS" becomes E51's "the
ledger preserved ROWS; nothing preserved the untracked FILES." Two of nine were processed before the loss
(STEPPING_BACK banked; PATH_BEYOND triaged in B1009); for the other seven the ledger note is main's entire
record — L114_DISCHARGE among them, *the relay whose July twin was already lost once*. **Filed as E51** with
the standing fixes: **sender-branch dual-homing** (cc3's `B8xxx/relays/` practice, now the standard for all
seats), the **re-send ask** to cc3 (`CC_TO_CC3_2026-08-27_RESEND_NINE_RELAYS.md` — their local relay dir may
retain the batch), and the repaired gate making un-dispositioned aging visible before content rots.

## 4. O3 executed + the invisible-work instances closed

The **MC1 assignment row** now exists (OPEN, formally codex's — the Cartan-matrix-only hypercharge
reimplementation, preregistered 36/36 recount; their R019 fences the theorem but is not it). The row was
missing because of defect (3) — the exact class the gate exists to catch, caught on the gate's first honest
run. Also backfilled: the two unrowed cloud relays (AUDIT_RECONCILED→B1145; MASTERPLAN_GO→B1164), the
unparseable compound first column on the MSSM row (repaired), and cc3's fab2849b acceptance recorded.

## 5. The register (the sweep's full findings, now on the record)

The sweep's verdict, banked: **the losses are at the seams, not in the banked mathematics** — (i) cross-seat
verdicts unharvested (closed by B1170/B1171), (ii) the relay/review instruments silently failed (the relay
half closed here; the **review-carry half is Review 50's opening item** — R47 mis-keyed the R46 bundle, R49
dropped R48-4…10, and `gates.py`'s review check can't see carry continuity), (iii) doctrine single-homed
(the portfolio, the governed-rooms APEX gap, chronicle_raw's unowned harvest candidates — all queued as
Wave 2). The remaining ranked queue (Wave 2 record-repairs; Wave 3 science cells, ℤ/2-identification first)
is registered in `b1172_results.json` verbatim, so the sweep's findings can no longer be lost to context.

## Fences

Process arc: no mathematics asserted; Gate 5 clean. The E51 event is honestly bounded — seven files'
content is unrecoverable *from this tree*; the re-send may recover it; if cc3 also lost them, the loss is
final and marked. The gate's far-future test path exercises real failure against the live ledger (no mock).
Not kill_graph-routed (instruments + triage; nothing killed).
