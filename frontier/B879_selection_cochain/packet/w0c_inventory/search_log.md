# W0c search log (read-only sweep of [machine-path])

All commands run read-only from the repo root; no files in origin-axiom
were modified.

1. `ls` repo root; located `frontier/` (663 entries), `docs/LAW_MAP.md`,
   `knowledge/THE_UNIQUENESS_ATLAS.md` via
   `find . -iname "*LAW_MAP*" -o -iname "*atlas*"`.
2. Read `PREREG_SCC.md` (the sealed W0c task text) and
   `docs/LAW_MAP.md` in full (132 lines) — the primary "banked law"
   ledger; this supplied most B-number citations and exact quoted
   statements.
3. Read `knowledge/THE_UNIQUENESS_ATLAS.md` in full — determined this
   concerns a DIFFERENT uniqueness campaign (the figure-eight knot's
   uniqueness in the classical-topology literature: minimal-dilatation,
   Reid's arithmetic-knot theorem, etc.) rather than the golden-word-
   within-the-metallic-family uniqueness this cell targets; not used as
   a primary citation source, cross-checked for overlap only.
4. `ls frontier/ | grep -E "B64|B65|B66|B67"` to enumerate B640-B670;
   listed contents of B649, B657, B662, B663, B664, B665, B666, B667,
   B668, B669, B670.
5. Read in full: `frontier/B664_metallic_landscape/FINDINGS.md`,
   `frontier/B665_landscape_reconciliation/FINDINGS.md`,
   `frontier/B663_bifocal_anatomy/FINDINGS.md`,
   `frontier/B663_bifocal_anatomy/BIFOCAL_CLARIFICATION_CC2.md`,
   `frontier/B649_silver_holonomy/FINDINGS.md`,
   `frontier/B657_invariant_line/FINDINGS.md`,
   `frontier/B662_successor_campaign/CAMPAIGN_SYNTHESIS.md`,
   `frontier/B662_successor_campaign/WAVE1_FINDINGS.md`,
   `frontier/B662_successor_campaign/WAVE2_FINDINGS.md`,
   `frontier/B662_successor_campaign/WAVE3_FINDINGS.md`,
   `frontier/B670_anatomy_full/FINDINGS.md`,
   `frontier/B670_anatomy_full/packet/loop2/b4_landscape/FINDINGS_CC2.md`,
   `frontier/B666_leads_campaign/WAVE1_FINDINGS.md`,
   `frontier/B666_leads_campaign/ADDENDUM_1.md`,
   `frontier/B669_track_h_adjudication/FINDINGS.md`.
6. `grep -rn "amphichiral" --include=*.md -l` (repo-wide) and
   `grep -rln "unit-det\|unit determinant\|prime conductor"
   --include=*.md` to find every file touching the two headline
   criteria; triaged the ~150 hits down to the load-bearing ones
   (K009, B136, S001, B197, B669 among them) by opening the
   speculation/knowledge-tier files that looked authoritative.
7. Read in full: `knowledge/K009_m1_selection_criteria.md`,
   `frontier/B136_general_amphichirality/FINDINGS.md` (via `sed -n`),
   `speculations/S001_amphichirality_theta_zero.md`.
8. `grep -n "B669" PROGRESS_LOG.md` (context around line 5812) to
   corroborate the amphichiral-refutation wording against the
   chronological ledger, not just the frontier FINDINGS file.
9. `grep -n "^| P[0-9]" CLAIMS.md` and read the P9/P10 rows; located and
   read `frontier/B197_figure_eight_volume_torsionfree/FINDINGS.md` in
   full (the volume/min-trace/min-length sharpening of P10).
10. `grep -n "^| \*\*L10[0-8]" docs/OPEN_LEADS.md` and
    `grep -n "^| \*\*L9[0-9]" docs/OPEN_LEADS.md` — pulled the exact
    L91, L100-L108 rows (the canonical current-state ledger) to
    cross-check every B662/B664/B665/B670 verdict against the
    lead-tracking document.
11. Read `frontier/B620_conductor_mechanism/FINDINGS.md` (head -40) and
    `frontier/B644_mckay_comparison/FINDINGS.md` (head -50) as primary
    sources for the conductor-identities and congruence-shadow-theorem
    entries (cited via LAW_MAP but verified against the primary file).
12. `grep -n conductor|torsion|unit` across `frontier/B591_chord_manifold/
    FINDINGS.md`, `frontier/B588_sector_exchange/FINDINGS.md`,
    `frontier/B634_conductor_chord/ERRATUM_1.md` — confirmed
    "det(A-I) = -1, the unit" wording and the ERRATUM's "G1 stands as
    computed" line.
13. `head -30 frontier/B640_hearing_group/FINDINGS.md` — confirmed the
    hearing-group theorem's exact class-equation and headline value.
14. Targeted greps that came back EMPTY or inconclusive (recorded as
    MISSING in INVENTORY.md Part C):
    - `grep -rn "R\^{n-2}L" --include=*.md --include=*.py` combined
      with "amphichiral" — no cell computes amphichirality for the
      single-L slice specifically (found only the unit-det/prime-
      conductor collapse, a different criterion).
    - `grep -rln "rank-2 categorif\|Eisenstein triangulation"
      --include=*.md` — five files, all parenthetical mentions of
      CLAIMS.md P10's four filters, no independent derivation file.
    - Confirmed L105 (2O/E7) is still OPEN via its `docs/OPEN_LEADS.md`
      row and `frontier/B666_leads_campaign/WAVE1_FINDINGS.md` CELL 1
      (refined to "2O is a quotient," not closed).
15. Cross-referenced `frontier/B530_natural_history/FINDINGS.md`
    ("three fields pairwise linearly disjoint") — read the section but
    EXCLUDED it from the inventory: it concerns a different dynamical
    substitution system (char poly x⁴-2x³-5x²-4x-1), not the golden
    RL/trace-3/disc-5 object, despite superficially similar
    "linearly disjoint fields" language. Flagged here so it is not
    mistaken for a golden-uniqueness citation by a later reader.

No files under [machine-path] were written to.
No files under [machine-path]** were touched or read.
