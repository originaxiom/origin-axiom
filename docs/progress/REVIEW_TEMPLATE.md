# The review template (GOVERNANCE §15; instituted 2026-07-16)

*Every decadal review follows this template. The REQUIRED core is small by
design — a review that is too heavy to run is worse than a light one that
runs. Schema and governance changes are proposed as separate arcs, never
inside a review.*

## REQUIRED core (every review)

1. **The loop (first, always).** Open the previous review's
   `### Action items` block. Every `- [ ]` item is either resolved (`[x]`,
   with the evidence pointer) or explicitly carried (`[>]`, restated in
   this review's own block with the same id). The `review-actions` gate
   fails the suite if a superseded block retains open items.
2. **The declared modulus.** State what this review sampled and what it
   can and cannot certify (the window of merges, which arcs read in full
   vs skimmed, which locks re-run vs trusted-green). Silent truncation is
   forbidden (GOVERNANCE §15).
3. **Advancement.** What moved between LAW_MAP strength classes
   (THEOREM / LAW / MECHANISM / PLACEMENT / WALL) this window; what has
   been stuck in one class longest; whether any row's stated status
   exceeds its banked evidence.
4. **Error-class recurrence.** Check the window's disclosed errors against
   `docs/ERROR_LEDGER.md`: which known class recurred (cite instances);
   any NEW class gets a ledger entry. The question is always "what
   standing rule would have caught this," not "who slipped."
5. **The provenance spot-sweep.** Grep the window's public-facing files
   for external-verification pretense (the Review-18 phrase list +
   PROVENANCE.md §0); verify papers carry true status; verify new
   load-bearing inner terms are glossed in TERMINOLOGY.md.
6. **The §5.1 promotion sweep.** Candidates meeting the §5 bars, processed
   through the gates or explicitly deferred with the blocker named.
7. **Protocol integrity.** Spot-verify the window's sealed hashes against
   their banked lines; confirm hash-first order was honored; note any
   omission repaired (with the repair PR).
8. **The action items block** (parseable; this is what the loop closes
   next time):

   ```
   ### Action items (Review N)
   - [ ] RN-1: <item> (owner: <seat/owner>; source: <arc/PR>)
   - [>] RN-2: <carried item, restated> (carried from R(N-1)-4)
   ```

## OPTIONAL enrichments (any subset; declare which ran)

- **Methodology delta** — a standing-rule proposal distilled from the
  window's error instances (files as a separate arc).
- **Governance delta** — an amendment proposal per §10 (separate arc).
- **Source-code health** — toolkit duplication, dead scripts, lock
  runtimes, environment drift vs REPRODUCIBILITY.md.
- **View regeneration** — LAW_MAP / status views rebuilt from metadata;
  hand-maintained docs reconciled against generated state.
- **Reader-path check** — walk one entry path (README → claim → lock) as
  a stranger; file the friction found.

## Banking

The review is one entry in `docs/progress/REVIEWS.md` (append-only), ends
with its action-items block, and adds `anchor-commit:` once the merge hash
exists (a follow-up one-line PR is the established pattern). The counter
(`scripts/gates/gates.py review-due`) reads the last anchor.
