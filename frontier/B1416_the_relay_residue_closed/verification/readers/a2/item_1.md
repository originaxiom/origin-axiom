# Item 1 — B8121 m4_closed / BMR cyclic-commensurability correction

## HEADLINE (verbatim ask)
"the 'BMR cyclic-commensurability correction' and a script 'check_arithmetic_tail.py' — what is
the correction (state it exactly, with the manifolds/fields involved), where does the script live
in the archive, was it ever merged into main's paper (papers/P3_THE_PAPER/main.tex — grep
'commensur', 'Borel', 'Maclachlan', 'Reid') or any main arc?"

## THE CLAIM (every number and name)
Source: `audit/wt-cc3/frontier/B8121_m4_closed/relays/CC3_TO_CC_2026-08-21_M4_CLOSED_13_OF_13_...md`
+ `FINDINGS.md` + `arc_verdict.json` + `results.json` (all consistent, one voice).

- **BMR = Bowditch, Maclachlan, Reid** — confirmed directly in cc3's paper source,
  `audit/wt-cc3/papers/structure_paper/arxiv/main.tex:3444`:
  `\bibitem{BMR} B.~H. Bowditch, C. Maclachlan and A.~W. Reid, \emph{Arithmetic...`; the theorem is
  `thm:arith` (line 768: `\begin{theorem}[cf.~\cite{MaclachlanReid,BMR}]\label{thm:arith}`, line
  775-777: "Bowditch, Maclachlan and Reid prove that for a fixed fibre type there are only finitely
  [many cyclic commensurability classes]... for the once-punctured torus there are precisely
  three~\cite{BMR}, carried by [RL, RRLL, RRL]"). Citation given by the relay is **Math. Ann. 302
  (1995) 31-60**.
- **What BMR actually prove** (verbatim from relay): "there are only finitely many cyclic
  commensurability classes of arithmetic hyperbolic surface bundles with any given fibre type...
  a complete classification in the case of once-punctured torus bundles showing that there are
  precisely three cyclic commensurability classes."
- **M3 verdict**: FULLY DISCHARGED — the paper's "precisely three" attribution matches verbatim.
- **M4, the defect**: the paper's original sentence claimed "exactly those [monodromies] conjugate
  to a power of one of the three words" — this is STRONGER than what cyclic commensurability
  proves. Cyclic commensurability only yields: SOME power of one monodromy is conjugate to SOME
  power of the other (not "conjugate to a power of a specific listed word").
- **The three words / fields** (from CHANGELOG.md:14128, the OLD/pre-fix formulation, dated
  2026-06-08, B126): `RL → ℚ(√−3)`, `RRLL → ℚ(i)`, `RRL → ℚ(√−7)` (√−7 flagged non-metallic).
- **Verification performed**: exhaustive block-sequence match of `(R^m L^m)^j` against `W^k` for
  `W ∈ {RL, RRLL, RRL}`, over `j,k ≤ 8`, `m` from 1 to 12. Result: m=1 matches RL; m=2 matches
  RRLL; every 3 ≤ m ≤ 12 matches nothing at any pair of powers. Bite control: RLRL matches (RL)².
- **Repairs claimed**: proof restates cyclic strength; comparison rewritten power-vs-power;
  `verify/check_arithmetic_tail.py` added with bite control; App B gains a row for `thm:arith`;
  App C records the overstated strength. Suite reported 21/21, "clean-room compile green, 51pp."
- **Script location in archive**: `audit/wt-cc3/papers/structure_paper/verify/check_arithmetic_tail.py`
  (and a duplicate copy at `audit/wt-cc3/papers/structure_paper/arxiv/verify/check_arithmetic_tail.py`).
  This is cc3's own `structure_paper`, NOT `papers/P3_THE_PAPER`.

## COMPUTED / CITED / ASSERTED
- CITED: the BMR abstract (external literature, fetched not re-derived).
- COMPUTED (by cc3, in-arc): the exhaustive power-vs-power block match, m=1..12, j,k≤8 — a bounded
  check, explicitly flagged by the arc itself as "not a proof for all j,k,m."
  Not independently re-run here (outside the 2-minute budget and the no-computation-here scope for
  a DOCUMENTARY item; see below).
- ASSERTED: "Suite 21/21... clean-room green, 51pp" — not independently checked in this reading.

## ON MAIN ALREADY?
**NOT** — and this has already been checked once before on main, with the same negative result:
- `docs/RELAY_LEDGER.md:420` — row for this exact relay: *"OPEN — main would need to verify
  whether the BMR cyclic-commensurability correction and check_arithmetic_tail.py script were ever
  merged into the paper/verification package; no trace found; trace on main: NONE found — no
  'cyclic commensurability', 'check_arithmetic_tail', 'BMR' theorem-fix, or 'verify_all 21/21' text
  on current main; docs/HARVEST_LEDGER.md row 294 (B8121) = SCHEDULED, 'no main text nam[es it]'.
  ESCALATED (2026-09-15) by name at the retirement sweep: residue of B1412, owed a verification on
  main, not a row."
- `frontier/B1412_the_relay_backlog/FINDINGS.md:30,40` — same conclusion, same exact-string search,
  same NONE-found result; line 40 lists "the BMR cyclic-commensurability fix with
  `check_arithmetic_tail.py` (untraced)" among "the ten that matter, for the next harvest slice."
- `docs/HARVEST_LEDGER.md:326` — row 294: `B8121` = **SCHEDULED** ("no main text names it — the
  slice D backlog, read before Review 57"), depends-on `B1306 (D)`, dated 2026-09-09.
- Independently confirmed here: `grep -n "commensur\|Maclachlan\|Bowditch\|BMR"
  papers/P3_THE_PAPER/main.tex` returns only unrelated hits — `main.tex` uses "commensurability"
  and Maclachlan–Reid (`\cite{maclachlanreid}`) only in the context of the object's OWN invariant
  trace field / chirality-vs-commensurability-invariant argument (lines 47-48, 70-71, 388-390,
  463-469, 578, 1030-1031, 1320, 1566) — a completely different theorem than BMR's three cyclic
  classes. No "RRLL", "RRL→", "BMR", "Bowditch", or "cyclic commensurability classes" anywhere in
  `main.tex`. Main's own `papers/structure_paper/` (distinct from cc3's archived one of the same
  name) is only `ABSTRACT_DRAFT.md` + `SKELETON.md` — a stub, no verify/ directory, no BMR content
  at all. So: **the fix, the script, and even the pre-fix claim it corrects are absent from
  P3_THE_PAPER; the pre-fix (overstated) three-word/three-field claim survives only in CHANGELOG.md
  history (B126, 2026-06-08) as a dated record, not as a live claim in a current paper or theorem
  registry.**

## NEEDS COMPUTATION HERE
DOCUMENTARY. The relay's own arc already ran the discriminating computation (the exhaustive
block-match, j,k≤8, m≤12) and reports it verified; re-running it is a re-verification of cc3's
own bounded check, not new information about whether the fix reached main. The open question here
is purely a location/provenance question (is it on main), which is answered by exact-string search
above (already run twice before by main itself, and reproduced here a third time with the same
result). If this item is later promoted to REPRODUCE-AND-BANK, the one discriminating fact to
recompute is: does `(R^m L^m)^j` fail to match `(RL)^k`, `(RRLL)^k`, `(RRL)^k` for all 3≤m≤12,
j,k≤8? (a ~10-line brute-force string script, seconds to run) — but that recomputation belongs to
whoever ports the fix, not to this documentary reading.

## GRADE PROPOSAL
**REGISTER** (not REPRODUCE-AND-BANK, since the correction is entirely internal to a paper —
cc3's `structure_paper` — that main never adopted; not ALREADY-ON-MAIN, since nothing of it is
present; not SUPERSEDED or DISPUTED — nothing on main contradicts it, main simply never had this
theorem/citation at all). Concretely: this item adds no new fact beyond what
`docs/RELAY_LEDGER.md:420` and `frontier/B1412_the_relay_backlog/FINDINGS.md:30,40` already
recorded — it is a third confirmation of the same NONE-found result. If P3_THE_PAPER or any future
paper ever cites BMR/Bowditch three-cyclic-classes machinery, the corrected (weaker, power-vs-power)
statement and `check_arithmetic_tail.py` are sitting in the cc3 archive ready to port; until then
this is dormant, correctly-flagged-OPEN residue, not a discrepancy needing dispute resolution.
