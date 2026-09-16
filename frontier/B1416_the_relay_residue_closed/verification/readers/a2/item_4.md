# Item 4 — CC_TO_CC3 "FOUND_THE_P1_SCRUTINY" / two different "F1"s

## HEADLINE (verbatim ask)
"what are B8123's 'one live defect, now fixed' (m13: Z[t]/mu called a non-maximal order?) and
B8107's 'F1 fix created one new instance of F1's own pattern'; is each fix present in main's
current paper or arcs (grep main for 'maximal order', 'Z[t]/', 'F1', 'backfill')?"

## THE CLAIM (every number and name)
Source: `audit/wt-cc3/CC_TO_CC3_2026-08-21_FOUND_THE_P1_SCRUTINY_ON_v4h3tb_F1_IS_THE_ADELIC_ENTRANCE.md`
(the target relay, cc→cc3) + arc `B8123_scrutiny_closed` + arc `B8107_r48_verify`.

**IMPORTANT — two unrelated things are both labeled "F1" and must not be conflated:**

**(A) The target relay's own "F1"** (from the *P1 golden-grammar adversarial scrutiny*, branch
`<vendor>/scrutinize-v4h3tb`): "the entrance consumes no arithmetic" — Theorem 7.7 (cc3's paper's
six-finite-group classification) "would read identically without a Sturmian word; the manifold
enters only via the ungraded gesture ℚ(√−3)⟹2T." cc calls this the **ADELIC ENTRANCE-SPLIT**: the
entrance is finite-place (arithmetic classification), the manifold is the archimedean side, and
they meet at one link that "must become a numbered theorem." cc offers to draft "F1's ℚ(√−3)⟹2T
theorem" (a Levi-style classification) on the main-seat bench, and ties it to B727 (E₆ forced,
only the atom object-specific) and the audit/b775 forcedness result (39/43 forced).

**(B) B8107's "F1"** (from the *R48 cold-review cycle*, a completely different, main-seat-facing
audit round) = **R48-F1** = the `THEOREM_REGISTRY.md` backfill/gate requirement: main marked
R48-F1 and R48-F2 RESOLVED; cc3's cold verification (B8107) confirmed the backfill is real
(B1012, B1080, B1094, B1098, B1100 all present in `THEOREM_REGISTRY.md`), the gate
(`gate_theorem_registry`) fires only when `creates_law is True` (995 legacy verdicts unaffected;
required from B1103 on — a cutover). **B8107's new finding, R48-F4**, is what the ask means by "the
F1 fix created one new instance of F1's own pattern": `creates_law` is required and schema-locked,
but `docs/BANKING_PROTOCOL.md`'s own arc_verdict field checklist did not list it — so a seat
following the binding checklist exactly would omit a required field and fail the lock. Severity
LOW (a wasted round-trip, not a silent error), but named because "F1 was 'the rule exists, no gate
reads it'; F4 is 'the gate exists, the protocol doesn't say it'" — the same structural pattern one
iteration later.

**B8123's "one live defect, now fixed" = m13** (from the P1 scrutiny, arc `B8123_scrutiny_closed`):
of 35 total scrutiny items (2 fatal, 11 major, 13 minor, 4 round-2, 5 constructive) against an
ancestor of cc3's paper, exactly one survived into the then-current text: **m13** — a remark
(`\label{rem:discmu}`) called $\mathbb{Z}[t]/\mu$ a "non-maximal order," but $\mu$ is not monic
(leading coefficient **500716339200** $= 2^{16}\cdot3^4\cdot5^2\cdot7^3\cdot11$, quoted in the same
sentence) so $\mathbb{Z}[t]/\mu$ is not an order at all. "The arithmetic was never in question" —
only the phrasing. Repaired with an App C entry (confirmed live at
`papers/structure_paper/arxiv/main.tex:3272-3275`, verbatim: "Remark~\ref{rem:discmu} called
$\Z[t]/\mu$ a 'non-maximal order'. It is not an order at all: $\mu$ is not monic. The arithmetic
was and is correct; the phrasing was not."). B8123 also discharges R1 (the scrutiny's "single
worst defect," about CS/amphichirality wording) and E5 (superseded by cc3's own B8078's
eleven-value rung spectrum).

## COMPUTED / CITED / ASSERTED
- COMPUTED (cc3, in-arc): the polynomial coefficient check (500716339200, non-monic) is a direct
  read of the paper's own displayed equation, confirmed present at
  `papers/structure_paper/arxiv/main.tex:3134,3148`.
- COMPUTED (cc3, in-arc, B8107): the THEOREM_REGISTRY.md backfill presence-check and the gate's
  scoping (`creates_law is True` only) are direct file/code reads against `origin/main` — this arc
  is itself a verification of MAIN's work, not of cc3's own paper.
- ASSERTED: "R1 discharged emphatically," "E5 discharged by our own B8078" — narrative summaries,
  not independently re-verified here (out of budget; both concern cc3's own paper, not main).

## ON MAIN ALREADY?
**Split answer — the two "F1"s and the m13 fix have three different outcomes:**

1. **m13 (Z[t]/mu phrasing)** — **NOT on main**, and irrelevant to main regardless: this is a
   remark inside cc3's own `structure_paper` (`rem:discmu`), a paper main never adopted (see items
   1-2). `grep -n "maximal order\|Z\[t\]/\|500716339200\|non-maximal" papers/P3_THE_PAPER/main.tex`
   returns **nothing**. The fix is confirmed landed only in cc3's archive
   (`papers/structure_paper/arxiv/main.tex:3272-3275`).

2. **R48-F1 + R48-F4 (BANKING_PROTOCOL/creates_law)** — **ALREADY ON MAIN**, and this is the one
   genuinely positive result among all four items in this harvest slice:
   - `docs/THEOREM_REGISTRY.md:204,206,215,219,221` — B1012, B1080, B1094, B1098, B1100 all present
     as rows (T-C6SIGMA, T-GLOBALFORM, T-TWO-ROUTE, T-HATCH, T-LANDING) — the backfill B8107
     verified is real.
   - `docs/BANKING_PROTOCOL.md:23-25` — the arc_verdict.json field list **currently reads**: `id`,
     `verdict`, `instrument`, `claim_one_line`, `depends_on`, `supersedes`/`superseded_by`,
     `authored_by`, **and explicitly `creates_law (bool; REQUIRED from B1103 on — a true demands a
     THEOREM_REGISTRY.md row in the SAME PR; the theorem-registry gate reads it, the schema lock
     enforces it — R48-F4)`** — i.e. main's protocol document names **R48-F4 by number** and
     documents exactly the missing field cc3 flagged.
   - `git log -S"creates_law" -- docs/BANKING_PROTOCOL.md` → commit `6683c0a2`, dated 2026-08-21
     (same day as B8107), message "B1104 THE 4D SUSPENSION SELECTION TEST... **R48-F4 fixed; R48
     closes**." So main itself closed R48-F4 the same day cc3's cold review flagged it — this is
     the one item across all four residue relays where the fix was demonstrably ported into main's
     own living documents, not left dormant in the cc3 archive.
   - `scripts/gates/gates.py:1077,1228` — `gate_theorem_registry` present and wired into the gate
     table, confirming the mechanism B8107 verified is live.

3. **The relay's own F1 (adelic entrance-split, "state ℚ(√−3)⟹2T with hypotheses" as a numbered
   theorem)** — **PARTIALLY ON MAIN, not exactly as asked.** No dedicated theorem titled around
   "the entrance consumes no arithmetic" or stating the ℚ(√−3)⟹2T gluing "with hypotheses" as a
   discrete Levi-style classification exists (`grep` for "entrance consumes"/"ramified 3"/"2T.*E_6"
   in `main.tex` and `THEOREM_REGISTRY.md` finds nothing matching that exact framing). But
   `docs/THEOREM_REGISTRY.md:236` carries **T-ADELIC (B1117)**, banked shortly after this relay
   (the relay itself lists B1112-B1116 as landing "on my side" the same day, immediately preceding
   B1117): *"The object is adelic (B1117, verified 32 digits): m004 is arithmetic (Reid), its
   finite shadow is structure (E₆ = reduction mod the ramified √−3) and its archimedean shadow is
   physics, glued by quantum modularity... Vol(m004) = 9√3·ζ_K(2)/π²."* This is the same
   finite-place/archimedean-split idea the relay names, formalized independently on main's own
   sequence (not drafted by cc3, not citing this relay by number) — a stronger, differently-shaped
   theorem (with an explicit volume/L-value identity) rather than the specific "ℚ(√−3)⟹2T with
   hypotheses" theorem cc offered to draft. Whether B1117 counts as answering the relay's specific
   ask is a judgment call, not a clean match — flagged as **DISPUTED** below rather than asserted
   either way.

## NEEDS COMPUTATION HERE
DOCUMENTARY for parts 1 and 2 (settled by exact grep + git history, both reproducible in seconds).
Part 3 is a judgment call, not a computation: whether T-ADELIC (B1117) satisfies the relay's
specific request for a numbered "ℚ(√−3)⟹2T with hypotheses" theorem is a textual/scope comparison
a math-literate reader should make directly (read `frontier/B1117*/FINDINGS.md` against the
relay's ask), not something a script can decide. No further computation is warranted here.

## GRADE PROPOSAL
Three-way split:
- **m13**: **REGISTER** (dormant in cc3's own paper, irrelevant to main's current paper set — same
  disposition as items 1-2).
- **R48-F1/R48-F4 (BANKING_PROTOCOL)**: **ALREADY-ON-MAIN** — confirmed ported and closed same-day
  (`docs/BANKING_PROTOCOL.md:23-25`, commit `6683c0a2`). No further action; cite as the one clean
  positive in this harvest slice.
- **The relay's own F1 (adelic entrance-split theorem)**: **DISPUTED** — main has a related,
  independently-derived theorem (T-ADELIC / B1117) that covers the same physical idea (arithmetic
  finite shadow + archimedean shadow glued by one number) but was not verified here to be the same
  claim, with the same hypotheses, that the relay specifically asked cc3 (or cc) to draft. Spelling
  this out: the relay's ask was narrow — "state ℚ(√−3)⟹2T with hypotheses" as a discrete
  classification theorem (a Levi-style group-theoretic statement) — while B1117/T-ADELIC is a
  broader analytic identity (Vol = a zeta special value) that *subsumes* the entrance-split
  motivation but may not supply the specific hypothesis-stated group theorem the relay names. A
  reader closer to the E₆/2T machinery than this documentary pass should confirm whether B1117
  (or some other T-* row) actually discharges this specific ask, or whether the narrow theorem is
  still owed.
