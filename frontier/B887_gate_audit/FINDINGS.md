# B887 — R37-1 executed: the 19-gate could-it-still-fail audit (workflow panel) — ~40 HIGH drift findings, four repaired tonight, the rest queued

cc banking seat, 2026-08-04. The masterplan's WF-PANEL lane proving itself on the review
ledger's "highest-value instrument task": one adversarial agent per gate plus a verify stage
(37 agents total; full reports preserved in `audit_reports.json`). Instrument scope.

## 1. The headline findings — Review 36's pattern continues

No gate is *incapable* of failing, but the audit produced ~40 HIGH-severity drift findings,
including **two live-demonstrated holes** (the auditors injected, observed PASS, reverted —
tree verified clean afterward):

1. **gate_framing never scanned root-level files outside a hardcoded 8-name list** — a banned
   phrase injected into `WORKING_RULES.md` (the binding rules file!) passed. Same blindness
   for TERMINOLOGY.md, ROADMAP.md, and any future root doc.
2. **gate_claims validated evidence paths only inside the Proven slice** — a fake E-row citing
   a nonexistent test in `## Certified data` passed.
3. gate_atlas_fresh compared *cardinalities*, so opposite-direction drift cancels silently.
4. Review 37's B877 lesson had no gate at all (FINDINGS without a sibling verdict).

## 2. Repaired tonight (each with the audit's scenario as its rationale, in-source)

| repair | mechanism |
|---|---|
| framing | scans **all** root `*.md` (no name list to go stale) |
| claims | evidence-path existence checked over the **whole ledger** (execution stays the suite's job by design — rationale recorded in-source) |
| atlas-fresh | **set equality** with named diffs, not cardinality |
| **arc-verdicts (new, gate #20)** | every frontier dir with FINDINGS.md must carry `arc_verdict.json`; grandfather = the 13 pre-convention arcs + `P3_depth_exposure` (frozen constants) — and the new gate immediately caught P3, which the shell-glob sweep had missed |

All 20 gates pass; `tests/test_repo_gates.py` green.

## 3. The repair queue (registered, prioritized — not silently dropped)

The remaining HIGH findings, for the next instrument pass (R38 candidates): firewall-oneway's
3-room blacklist missing `knowledge/` and bare-ID citations; attribution checking only HEAD's
author; test-vacuity's receiver-blind whitelist; views-fresh equating "touched" with
"refreshed"; append-only's archive trust; chain-locks' brittle block-split regex;
law-map-provenance's syntactic-only B-number check; knowledge-index substring masking;
id-collisions' bare-number grandfathering; practices-register's prose-mention satisfaction;
log-changelog-paired's self-resetting reference; views-generated's intersection scoping;
path-refs' live-filesystem resolution; atlas-lexicon-current's hand-run cache. Full detail
per gate in `audit_reports.json`.

## 4. Lane verdict

The WF-PANEL lane works as designed: 37 agents, ~5.5 minutes wall, two live-demonstrated
holes in binding governance instruments that three decadal reviews had not found. The audit
question ("could it still fail?") earns its place as a standing cadence item.

`tests/test_b887_gate_audit.py`
