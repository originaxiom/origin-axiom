# B1830 — THE REGISTER TRIAGED: EVERY OPEN ROW TYPED (DEBT, LEAD, PROCESS), ONLY DEBTS AGE, THE 59 DEBTS RANKED BY THE LOAD THEY BEAR (THE OWNER'S RULING ON P-587)

**Verdict: PROVED** (a record of the owner's ruling, the gate that enforces it, and the first triage; nothing computed on
the mathematics). cc (main), 2026-11-03. **0 of 19.**

## 1. The question and the ruling

The owner, 2026-11-03: *"at what time should we deal with all open leads, and queued that are on our register? whats the
point of keepin them there? if theyre open do they bear load on our current math?"* Main measured it (P-587): 255 open
rows; the queue's slot table stale; the point-debt gate about to fail every push from 2026-11-04 (32 rows unmoved since
2026-10-13); 72 open rows question a banked result later work cites, about 15 bearing on current math — one of them, P-355,
on the candidate family B1829 had registered an hour earlier. Main proposed typing every open row DEBT, LEAD or PROCESS,
ageing only debts, and triaging now. The owner: **"yes"**.

## 2. What changed

- **The gate** (`scripts/checks/point_debt.py`, rule 6; `tests/test_point_debt_gate.py`, a new planted test): every QUEUED
  or LEAD row carries exactly one type tag in its *where* cell; only [DEBT] rows age (21 days, then ESCALATED with a next
  action); every open debt is on the ranked list under "## The debts, by load", which names only open debts.
- **The register** (docs/POINT_REGISTER.md): the typing section and the ranked list before the queue; the queue's slots
  kept for the rows that name them, its order superseded by the typing.

## 3. The triage (verification/)

- **Five readers** typed the 250 open QUEUED and LEAD rows and proposed closures with evidence (batch_1–5.md,
  proposals_1–5.json); **main verified every proposed closure** (MAIN_VERIFICATION.md).
- **Closed:** DONE P-386 (B1787), P-495 (B1823, B1825), P-502 and P-503 (the tools calibrated), P-510 (KIND_TABLE's ruling),
  P-520, P-521, P-522 (B1825's card), P-587 (here); P-292 merged into P-337. **Rejected closures** (kept open): P-485 and
  P-487 (the exclusion half never ran; B1825 ran only a restriction), P-218 (its question not carried by P-210).
- **Typed:** 59 debts, 141 leads, 41 process. P-321 retyped a debt by main. 15 debts older than two weeks escalated with
  their next action.
- **The ranked debts, by load:** first the debts bearing on current work — the strip candidate (P-585: P-355's D, P-384,
  P-586, P-446, P-517, P-559, P-444), the live prediction P10 (P-157), B1825's machinery (P-542, P-524, P-557, P-516, P-448);
  then false or stale statements in foundation and front documents (P-318, P-427, P-374, P-579, P-581, P-320, P-321, …);
  then checks that cannot fail and instruments (P-317, P-239, …); then unverified premises under structural results
  (P-156, P-054–P-057, …).

## Seen first

- `VERDICT topic-sweep /point register|POINT_REGISTER|point-debt|triage of the register|register triage|typed (rows|points)/
  (full text): 52 of 1576 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 43); 4 register rows match (DONE 3, QUEUED 1)` — the
  register's own opening (2026-10-13, the owner: points lost between sessions) and its gate; the arcs that cite rows; no
  earlier typing of rows. The lead and relay debt gates (lead_debt.py, relay_debt.py) age their own items and are unchanged.
- **Literature (pointers):** the typing follows the common practice of issue trackers, which separate defects (owed fixes to
  what is in use) from feature requests and chores, and age only the first; an analogy for the shape, not a source.

## Disclosed

- The readers' KEEP means "not confirmed paid", not "confirmed unpaid": three of five batches sampled the record. Leads and
  process rows do not age, so a missed payment there costs nothing until the decadal review reads them; a missed debt ages
  and returns. The ranking within each tier is main's judgement.
