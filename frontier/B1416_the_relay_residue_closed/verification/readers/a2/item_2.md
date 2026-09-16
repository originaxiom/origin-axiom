# Item 2 — B8107 r48_verify / P1 Defect 2 (su(6) table)

## HEADLINE (verbatim ask)
"which paper was 'P1' then (find the tarball/paper name it cites), what is 'defect 2' and the
'su(6) table fix', and does the current papers/P3_THE_PAPER/main.tex carry that table correctly
(find the su(6) branching table if any)?"

## THE CLAIM (every number and name)
Source: `audit/wt-cc3/frontier/B8107_r48_verify/relays/CC3_TO_CC_2026-08-21_P1_DEFECT2_IS_NOT_LIVE_VERIFIED_IN_THE_TARBALL.md`.

- **"P1"** = cc3's own paper submission, tarball **`oa-structure-paper.tar.gz`** — this is the same
  paper as cc3's `structure_paper` (the one holding `thm:arith` / the BMR fix in item 1); confirmed
  by matching content (the su(6) table line is present verbatim in
  `audit/wt-cc3/papers/structure_paper/arxiv/main.tex`).
- **Defect 2**: a table cell claimed to still show a dash for row `A_3=Z/3 → su(6)`, i.e. the
  question was whether `su(6)` "having a complex fundamental" was still shown as answered
  incorrectly ("no"/dash) in the *submitted* artifact.
- **Verification**: cc3 extracted the tarball and read `main.tex` line 1549 (submitted copy):
  `$2$ & $A_3=\Z/3$ & $\Z/6$ & $\widehat{A}_5\to\su(6)$ & \textbf{no} & yes---but see below\\` —
  "yes—but see below," **no dash**. Confirmed byte-identical to the working `main.tex` via MD5
  `0b4305200e07f12b5fe734e9ca96800b` on both sides — i.e. the submission is not stale relative to
  the working copy.
- **The su(6) table fix, exact mechanism** (quoted in the relay, confirmed live in the archive at
  `papers/structure_paper/arxiv/main.tex:1569,1578-1582`):
  1. Mechanism: "`su(6)` **does** have a complex fundamental, since $-1\notin W(A_n)$ for $n\ge2$."
  2. Retraction, in the paper's own voice: "the earlier table's dash in that column **was wrong**:
     it read as 'no' where the answer is 'yes'."
  3. Cross-reference to §entrance: the same fact is what makes the chirality-capability criterion
     fail to isolate $E_6$ alone — complexity of the fundamental selects
     $\{A_n:n\ge2\}\cup\{D_{\text{odd}}\}\cup\{E_6\}$, and A-type is in that set.
  4. Concession beyond the reviewer's ask: "Complexity alone never excluded A-type and was never
     going to. Exceptionality is what excludes it, and exceptionality is the input the paper
     declines to derive." — the Scope block is titled
     `\begin{scope}[the two exclusions are not the same exclusion]\label{sc:twogrounds}`.
- **cc3's overall verdict**: "So the P1 find is a hit on a stale version, not the current one" —
  both of the reviewer's defects (Defect 1 and Defect 2) are closed in the submitted tarball, and
  Defect 2's fix is judged more complete than the reviewer's own proposal.
- Process note (self-correction): cc3's first grep for the retraction sentence returned 0 hits
  because the apostrophe in "table's" broke the pattern; caught by checking MD5 instead of
  trusting the grep count.

## COMPUTED / CITED / ASSERTED
- COMPUTED (by cc3, in-arc): direct read of tarball-extracted `main.tex` line 1549 + MD5 comparison
  against the working copy. This is a concrete, reproducible byte-level check, not an assertion.
- Not independently re-run here: the tarball itself is not present anywhere in the archive I have
  access to (only the resulting `main.tex` under `papers/structure_paper/arxiv/`), so the original
  MD5 claim cannot be re-verified without the tarball; the *content* of the fix (lines 1569,
  1578-1582) is independently confirmed present in the archive's current `main.tex`.
- ASSERTED: that this fix is "more complete than the reviewer's proposal" — a judgment call, not
  a computed fact.

## ON MAIN ALREADY?
**NOT — and "P1"/`oa-structure-paper` does not correspond to any paper in main's current tree at
all.** This exact question was already run once before, with the same negative result:
- `docs/RELAY_LEDGER.md:421` — "OPEN — process note: main would have to confirm which current
  paper (if any) corresponds to this old 'P1' submission and whether its su(6) table fix is still
  intact; trace on main: NONE — no file named 'oa-structure-paper' or matching text exists in the
  current tree; this appears to reference an earlier/renamed paper submission, not the current
  papers/P3_THE_PAPER. ESCALATED(2026-09-15)... residue of B1412, owed a verification on main, not
  a row."
- `frontier/B1412_the_relay_backlog/FINDINGS.md:31` — same conclusion, same NONE-found trace.
- `docs/HARVEST_LEDGER.md:312` — row 280, `B8107` = **SCHEDULED** ("no main text names it — the
  slice D backlog, read before Review 57"), depends-on `B1306 (D)`, dated 2026-09-09.
- Independently confirmed here: `grep -n "su(6)\|A_3=\|complex fundamental"
  papers/P3_THE_PAPER/main.tex` returns **nothing**. `main.tex` does discuss McKay/E₆ extensively
  (lines 85, 132, 165, 238, 291, 422-423, 438, 582, 1514) but in a completely different register —
  the McKay correspondence handing over $E_6$ at the "hyperbolic end," not the A-type/D-odd/E₆
  complex-fundamental exclusion table from cc3's `structure_paper`. **The su(6) branching table
  does not exist anywhere in main's current paper.** Main's own `papers/structure_paper/` (a
  different, un-related stub directory of the same name — see item 1) contains only
  `ABSTRACT_DRAFT.md` + `SKELETON.md`, no such table.

## NEEDS COMPUTATION HERE
DOCUMENTARY. The discriminating fact (line 1549 of the submitted tarball vs. MD5 match) was already
computed by cc3 in-arc and is a closed, reproducible byte-level check; it cannot be meaningfully
re-run here because the original `oa-structure-paper.tar.gz` tarball is not present in this
archive (only its extracted/working `main.tex` descendant is). The open question this item actually
turns on — "is this on main" — is a location question, answered definitively by exact-string
search (`su(6)`, `A_3=`, `complex fundamental`, `oa-structure-paper`): zero hits, confirmed twice
independently (once by main's own B1412 harvest, once here).

## GRADE PROPOSAL
**REGISTER.** Not REPRODUCE-AND-BANK (the fix and its target paper live entirely outside main's
current paper set — there is nothing on main to bank it into); not ALREADY-ON-MAIN (confirmed
absent); not SUPERSEDED (nothing on main contradicts it — main simply never had this table); not
DISPUTED (no disagreement between sources — RELAY_LEDGER, HARVEST_LEDGER, B1412 FINDINGS, and this
reading all agree: NONE found). This is dormant, correctly-flagged-OPEN residue tied to a paper
(`oa-structure-paper` / cc3's `structure_paper`) that main never adopted. If any future paper
revives the A-type/D-odd/E₆ exceptionality-exclusion argument, the corrected table and its Scope
block are sitting ready in the cc3 archive at `papers/structure_paper/arxiv/main.tex:1569-1582`.
