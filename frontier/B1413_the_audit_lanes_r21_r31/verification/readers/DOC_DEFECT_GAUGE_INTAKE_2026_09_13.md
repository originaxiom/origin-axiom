HEADLINE
# Source-tube gauge mechanism: retrieved prior, not an executed R29

WHAT IT IS
An intake/preparation note (2026-09-13) documenting retrieval, prior-result review, and a proposed-but-unexecuted next calculation (R29) for a gauge-covariant finite-width source model; explicitly not a new proof.

VERDICTS AND CLAIMS
- "preserves preparation without advertising a new proof or completed source mechanism. No new B number is allocated" (scope statement).
- "All reserved bands, including B1350--B1399, stay untouched" (status check).
- "The other bench's table calls its own allocations main; that wording does not override the observed origin/main SHA" (CORRECTION of another branch's terminology, not main's actual record).
- "the latest return handoff's `main=f06d3405` is not the freshly fetched origin/main here" (CORRECTION — flags a stale/mislabeled hash in another branch's handoff doc).
- Scanner result: "28,141 blobs, 3,038,502,401 bytes, 4,332 commits, with 3,151 matching versions under 240 example paths" — "No corpus-wide absence or first-ever-mechanism claim follows from this scan."
- "R16's weighted radial capacity/domain calculation ... is existing prior, not a new general capacity discovery."
- "A field defined only on a contractible tube is a changed model, not a counterexample to that theorem's hypotheses" (re R22).
- "The shift by an input density does not already supply a charged source field" (re R28).
- de Rham source: "explicitly allows a consistent renormalized defect EFT; its electrodynamics example is not automatically our bulk gauge field."
- SM B1352/B1355 findings "read" but "not independently certified here."
- Paper-review return handoff: "retains the all-generating-pairs/Nielsen-class distinction for the Jorgensen claim ... These are received dispositions, not newly proved facts on this branch."
- "Its family-sector Z-prime statement is not automatically the fate of R19's extra centralizer U1; the fields and operator must be mapped" (scope caveat).
- Outside memos 218/219: "exact quantum-invariant and PARI/capability reports ... were not reproduced."
- Proposed R29 expected outcome explicitly disclaimed: "This expectation is NOT a new scientific result."
- Final instruction: "Next write the complete design, proof, producer and mathematical tests; hash, commit and push them BEFORE first execution. At this checkpoint only retrieval and the separate 78-test old-result recheck have run."

CORRECTIONS TO MAIN OR TO ITSELF
No correction to main. Two corrections aimed at OTHER audit-adjacent branches (not main): (1) "The other bench's table calls its own allocations main; that wording does not override the observed origin/main SHA" — i.e., another bench mislabels its own branch as "main." (2) "the latest return handoff's `main=f06d3405` is not the freshly fetched origin/main here" — flags that a handoff doc's recorded main hash is stale relative to this document's own fresh fetch (`b94ed03aecba8aae3afc62504e22ec664c26e94f`).

ROADMAP ITEMS
N/A for this document itself (it is an intake/preparation note, not the roadmap doc — it explicitly defers the roadmap to a separate file: "The user also requests a complete roadmap and observational assessment; those are separate status and compatibility documents"). Its own numbered "discriminating tasks" for the proposed R29 (not a repo roadmap, task list for one calculation):
1. "Derive gauge covariance, currents and ALL coupled first variations."
2. "Derive the actual transverse extra-U1 fluctuation operator from the quadratic action."
3. "Compare finite-width positivity with the shrinking-tube limit on the fixed bulk Hilbert space."
4. "Check whether a proposed positive line-trace mass term is a closed form on that Hilbert space."
5. "Use an independently diagonalized finite Kaluza-Klein toy matrix to test a zero-mode-only truncation."
6. "Only after a compatible source/gauge result, compute its actual fermion domain and full anomaly."

CONFLICTS WITH MAIN
Checked `git -C <repo> grep -l -F "f06d3405" -- docs frontier`: hit only in `docs/handoffs/RETURN_TO_THE_CROSSING_SEAT_2026-09-13.md` — this is the very handoff document the intake note is correcting, and it IS present in main, confirming the intake's target exists in main's docs/handoffs (not a conflict with main, but confirms the corrected document is itself part of main's record — worth flagging that main carries the stale-hash handoff this note disputes). Checked "B1350--B1399" and "1350": present in main's `docs/CAMPAIGN_STATUS.md`, `docs/ERROR_LEDGER.md`, `docs/HARVEST_LEDGER.md`, `docs/HINT_LEDGER.md`, `docs/LEAD_REGISTER.md` as reserved bands, consistent with the intake's "stay untouched" claim. NONE (no outright contradiction found; one caution noted above).

WHAT MAIN WOULD HAVE TO VERIFY
Whether `docs/handoffs/RETURN_TO_THE_CROSSING_SEAT_2026-09-13.md` (present in main) still records `main=f06d3405` uncorrected, since this intake asserts that hash is stale versus the actual origin/main tip it fetched (`b94ed03a...`, now superseded further by main's current HEAD). Also whether reserved bands B1350-B1399 remain untouched at current HEAD.
