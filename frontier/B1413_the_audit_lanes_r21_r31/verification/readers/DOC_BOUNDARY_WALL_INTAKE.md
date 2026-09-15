# BOUNDARY_WALL_INTAKE.md

## HEADLINE
R25 final all-head intake: preserve the capabilities and their grade

## WHAT IT IS
A status/intake report on newly fetched branch heads following scientific runs, grading each new item as RECEIVED, capability, or independently checked.

## VERDICTS AND CLAIMS
- "Other remote heads are unchanged: main b94ed03a, SM 1703c0d8, physics 659487bb. No merge." (CUSTODY).
- Memo 193 addendum "reports 7 failed/21 passed, diagnoses exactly our retained R24 structural matrix comparison... independently obtains zero for the R24 matrix residual" (INDEPENDENT CHECK, agrees).
- "This agrees with our own existing computations; it is NOT independent assessment of R24's total-flux proof or R25" (SCOPE LIMIT).
- New fallback interface (`Q.is_isometric_to` vs `Q.isomorphisms_to`) "is a registered CAPABILITY to test, not a new interval certificate" (SCOPED, not adopted as proof).
- "That modified run is not reproduced here or inserted into the original sealed source" (NON-ADOPTION).
- B1137 commit: "352 null-grid lines and reports a byte-identical final report after recomputing both grids. That long computation was not rerun here; this is not a new certificate from our bench" (RECEIVED, unverified here).
- "Memo 188 withdraws a stale-checkout claim of a silent progress log, alongside its earlier withdrawn depends_on claim" (RECORD OF OUTSIDE'S OWN RETRACTION).
- "We directly checked main's September-dated headings, including September 9, against the older fba45fc2 tree. This supports rejecting the alleged ten-day silence" (INDEPENDENT CHECK, positive for main).
- "No exact daily-entry census, first-commit-date census or remaining throughput statistic is independently certified here" (CAVEAT on the above).
- "The receipts are not silently merged, the older failed evidence is not rewritten, and the new numerical fallback does not change R25's own science or certification status" (INTEGRITY STATEMENT).

## CORRECTIONS TO MAIN OR TO ITSELF
- No correction directed at main's record; the document instead defends main against an outside claim: it rejects "the alleged ten-day silence" by checking main's own September-dated headings including September 9.
- Records an outside seat's self-retraction, not this seat's own: "Memo 188 withdraws a stale-checkout claim of a silent progress log, alongside its earlier withdrawn depends_on claim."

## ROADMAP ITEMS
N/A (intake/status note, not a forward roadmap document). Closing line: "Its follow-up is registered in OPEN_LEADS; this intake is not a transmitted relay or a B allocation."

## CONFLICTS WITH MAIN
- Claim: main was accused elsewhere of a "ten-day silence" in its progress log; this doc says checking main's tree "supports rejecting the alleged ten-day silence," citing September-dated headings including September 9. Checked: `git -C <repo> grep -l "2026-09-09" -- docs` returns multiple files including docs/CAMPAIGN_STATUS.md, docs/HARVEST_LEDGER.md, docs/FRESH_EYES_2026-09.md — main does carry September 9 dated entries. NONE (claim corroborated, no contradiction).

## WHAT MAIN WOULD HAVE TO VERIFY
Confirm independently that the fba45fc2 tree used for the "no ten-day silence" check is a legitimate main ancestor, and separately validate (or reject) the `Q.is_isometric_to`/`isomorphisms_to` fallback capability against the existing word/canonical control before treating it as anything beyond a registered candidate tool.
