# The decadal repo reviews — ledger (GOVERNANCE §11)

Every ~10 merges on `main`, a whole-repo review fires: full suite + all gates +
atlas regeneration + a claims-vs-frontier promotion-candidacy sweep + a framing sweep +
a stale-leads check, ending in a dated report appended here. The gates surface DUE
status automatically (`python3 scripts/gates/gates.py review-due`).

Protocol per review: (1) suite green; (2) gates green; (3) atlas regenerated and fresh;
(4) sweep `frontier/` FINDINGS for entries that meet the GOVERNANCE §5 promotion bars
and list the candidates (promotion itself happens only through the §5 gates, logged);
(5) sweep for framing drift and stale `OPEN_LEADS` rows; (6) append the report below
with a new anchor-commit.

---

## Review 0 — 2026-07-03 (baseline; the reform itself)

anchor-commit: 7d8786d0dcf7e0e332a53e26815f55a954208447

The instituting review. Gates implemented and green (7/7); suite lock added; the
promotion-audit lane registered (see `docs/OPEN_LEADS.md`); ledger sections extended
with **Certified data**. Next review due after 10 merges from this anchor.
