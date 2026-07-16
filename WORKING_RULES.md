# Working rules (binding; read before computing)

*One page. Every working session — any seat, any clone — reads this first.
Deep material: `GOVERNANCE.md` (the constitution), `METHOD.md`,
`TERMINOLOGY.md`, `PROVENANCE.md`. Instituted 2026-07-16 (GOVERNANCE §12–§15).*

1. **Sync before computing.** Pull/fetch and confirm your checkout includes
   the latest `main` BEFORE claiming "no prior work exists on X." A
   thorough search of a stale checkout produces confident false negatives
   (the Door-2 class: the answer existed, three merges ahead).
2. **Verify, don't trust — in both directions.** Every cross-seat claim is
   reproduced in-sandbox before banking; so is every claim of your own
   before asserting it to another seat. Incoming ambitious framing is
   quarantined; incoming mathematics is re-run.
3. **Hash first.** Seal PREREGISTRATION.md (sha-256 recorded in the arc's
   ARTIFACT_HASHES.txt) before the first run. Failed runs are preserved
   byte-faithfully, never overwritten. Corrected code is re-hashed BEFORE
   the rerun, labeled post-hoc if sealed late.
4. **Declare every choice.** The conventions block (GOVERNANCE §13) lists
   every basis, sign, normalization, orientation, and stage choice before
   the run. Undeclared choice drift is this program's most recurrent error
   class (`docs/ERROR_LEDGER.md`).
5. **The layers are one-way.** Coupling-tier content (hints, adjudications,
   speculations, reviews) is never evidence for a layer-1/2 statement. The
   firewall blocks overclaims, not mathematics; the gate is open by default
   for mature computed steps.
6. **Gate 5 stands.** No SM quantities into `CLAIMS.md`; no recycling
   structured-null numbers under new labels; physics readings wait on the
   typed functor (L91). Value comparisons need: owner directive + sealed
   design + MB12 + MB13-in-doc + pipeline controls + the
   INPUT_COMPLETENESS_LEDGER row.
7. **Locks assert mathematics.** A test asserts the mathematical fact (or
   re-computes it), not a transcript string, wherever feasible; transcript
   asserts are the fallback, marked as such.
8. **Vacuity-check before sealing.** Every sealed criterion must be able to
   pass AND to fail (MB12 covers operations and criteria); check reference
   tables/targets for internal consistency before sealing them.
9. **Zero file moves.** Never move or rename banked paths (GOVERNANCE §12).
   New work = new files. Views and metadata evolve; the substrate is frozen.
10. **Bank completely.** Every banked arc updates PROGRESS_LOG (append at
    END) + CHANGELOG + CAMPAIGN_STATUS in the same/next PR; a new law adds
    its LAW_MAP row in the same PR; new inner terms get TERMINOLOGY.md
    lines; the atlas regenerates per new B-dir.
11. **Attribution and privacy.** Commits as `originaxiom`; no AI mentions in
    anything public-facing; scrub sandbox paths from committed files. After
    every merge to `main`: `git push codeberg main` (the mirror).
12. **Report faithfully.** Negatives bank as computed facts with their
    discriminating computation in-sandbox (never asserted/cited/proxied);
    an unearned negative is as bad as numerology. Don't stop and celebrate
    negatives; don't soften positives that passed their gates.
