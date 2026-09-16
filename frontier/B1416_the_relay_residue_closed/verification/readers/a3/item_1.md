# Item 1 — B1029 ↔ B647 join; the "emits invariants" law; sp.conjugate fix

Sources: `<home>/origin-axiom/audit/wt-braver/CC3_TO_CC_2026-08-11_COMPLETE_PICTURE.md`,
`<home>/origin-axiom/audit/wt-braver/CC3_TO_CC_2026-08-11_GAUGE_VS_INVARIANT.md`.

## HEADLINE (verbatim)

COMPLETE_PICTURE Part IX, item 1: *"**The B1029 ↔ B647 join** — 'Y = ½·conj(the swap's
chain anomaly)' against 'kernel exactly θ = c∘r'. Same operator, two levels, zero
citations. **A JOIN, not a computation.** The sharpest available L155 target."*

GAUGE_VS_INVARIANT §4 header: *"THE JOIN NOBODY HAS MADE, AND IT IS COMPUTABLE"* — plus
§1's headline law, *"THE OBJECT EMITS INVARIANTS. COORDINATES ARE THE OBSERVER'S,"* and
§5's tooling note: sympy `subs`-based conjugation over √−3 silently no-ops (`I·√3`
internally); use `sp.conjugate`.

## THE CLAIM

1. B1029 (value-level: the frame group's value-representation has kernel exactly
   θ = c∘r) and B647 cell 2 (chain-level: `Y = ½·conj(the swap's chain anomaly)`) are
   "the same operator at two levels" with zero cross-citations — an unasked, computable
   join, offered as cc3's sharpest L155 target.
2. A general law — "the object emits invariants, coordinates are the observer's" —
   assembled by reading five already-banked arcs (B647 c3, B884, chat1 SEALS/phase1b §5,
   B897/B883/B632) as one law nobody had stated together.
3. A silent-failure tooling note: sympy's `subs`-based conjugation over ℚ(√−3) no-ops
   (internal `I·√3` normalization); B1029's own Lane-II-1-adjacent reconstruction is
   ℚ-exact over that field and turns on conjugation, so this is a live risk to it.

## COMPUTED / CITED / ASSERTED

- Claim 1: **CITED** as an opportunity, not computed, in these two relays — both
  explicitly say "a JOIN, not a computation" / "IT IS COMPUTABLE" (future tense).
- Claim 2: **ASSERTED as a framing/synthesis** over five already-computed, already-banked
  results. No new computation in either relay; it is a re-reading.
- Claim 3: **CITED** — quoting B647's own in-run note verbatim; not a new computation by
  cc3, but a correctly-flagged risk.

## ON MAIN ALREADY?

**Claim 1 — YES, computed and banked, one day later.** `frontier/B1037_theta_join/`
(seat cc, 2026-08-12, prereg sealed `63cd367a` *before* compute) is titled, verbatim,
"Plan Arc 4 — THE θ-JOIN (B1029 ↔ B647)" (`docs/SEAL_LEDGER.md:626`) and its
`PREREGISTRATION.md:1` reads: *"# B1037 PREREGISTRATION — plan Arc 4: THE θ-JOIN (B1029
↔ B647; sealed before compute)"*; line 5: *"B1029's value-kernel the value-level shadow
of B647's chain-level defect law?"* `FINDINGS.md:24` states the verdict: *"the value-
kernel (B1029) and the chain defect law (B647) are two banked facts without an exhibited
one-operator join"* — verdict **DISTINCT** for the sealed evaluation-order-alternation
projection (J2 fails at its first clause; J3's positive sub-fact `J² = +1` survives).
The scope fence (`FINDINGS.md:18-26`) explicitly leaves open a re-pose at the
argument-antisymmetrization level as "a new cell with a new seal." Registered in
`docs/CAMPAIGN_STATUS.md:1251` ("the θ-join died clean at its first sealed test —
DISTINCT").

**CONTRADICTED: `docs/RELAY_LEDGER.md:304-305` (this repo's own tracking rows for these
two exact relays) say the opposite.** Row for `COMPLETE_PICTURE.md`: *"OPEN — main would
need to show whether the B1029↔B647 join ... was ever explicitly computed anywhere; not
located ... no joined arc found."* Row for `GAUGE_VS_INVARIANT.md`: *"OPEN — the join
itself (B1029 kernel vs B647 chain-anomaly) is still not located as a computed result on
main."* Both rows carry an `ESCALATED(2026-09-15)` tag from the B1412 retirement sweep.
**This is a genuine discrepancy**: B1037 names both arcs by number in its own title, is
sealed, PROVED, and in `docs/SEAL_LEDGER.md` and `docs/CAMPAIGN_STATUS.md` — a plain
`git log`/`grep -rl "B1037" docs frontier` finds it in seconds. The RELAY_LEDGER rows
appear to have searched for the join under the relay's own vocabulary ("join",
"kernel"+"anomaly" together) rather than by arc number, and missed B1037.

**Claim 2 (the general law) — PARTIALLY, as a sharper, fenced theorem, not this
phrasing.** `frontier/B1032_type_law/FINDINGS.md` (same day, 2026-08-11, PROVED) verifies
and amends the construction seat's resolution bound into **THE TYPE LAW**: *"the object's
forced outputs live in a finite algebraic menu ... a crossing may target (i) a RELATION
... or (ii) a FINITE LABEL ... it may NOT target a generic real by value"* — scoped
explicitly to the dimensionless coupling channel, with stated fences (Vol, CS=0, c=6σ
excluded). This is the computed content behind cc3's "emits invariants" framing but is
**not phrased that way anywhere on main** (confirmed independently; matches
`docs/RELAY_LEDGER.md:305`'s own search note) — main's version is narrower-scoped and
fenced, which is an improvement, not a gap.

**Claim 3 (sp.conjugate) — heeded in practice, not promoted to a named error class.**
`frontier/B1029_invariant_ring/b1029_cells.py:26-28` uses `sp.conjugate` correctly
throughout (not `subs`). `docs/ERROR_LEDGER.md` has **no entry** for this specific
sympy-conjugation-over-√−3 failure mode (grepped for "sympy", "subs-based", "silently
no-op" — zero hits); it survives only as B647's own in-run prose
(`frontier/B647_core_mechanism/FINDINGS.md:69-70`), exactly as flagged ("never
promoted").

## NEEDS COMPUTATION HERE

DOCUMENTARY for claim 1 (already computed on main as B1037 — the work is to correct the
RELAY_LEDGER rows, not to recompute). DOCUMENTARY for claim 2 (B1032 is the banked
answer). For claim 3, one discriminating fact + recipe if a reader wants to promote it:
`grep -rn "\.subs(" frontier/ --include="*.py" | grep -i "conj\|sqrt(-3)\|I\*sqrt"` across
every arc touching ℚ(√−3) (B632, B884, B1029, B1036, B1037...) and confirm each hit uses
`sp.conjugate`/exact algebraic conjugation rather than a substitution-based stand-in —
under 2 minutes, not run here (out of scope for this reader's bound).

## GRADE PROPOSAL

**ALREADY-ON-MAIN** for claim 1 (B1037, `frontier/B1037_theta_join/FINDINGS.md:24`,
`docs/SEAL_LEDGER.md:626`) — **and DISPUTED against this repo's own RELAY_LEDGER rows**,
which should be corrected from OPEN to BANKED/ALREADY-ON-MAIN citing B1037 by number.
**ALREADY-ON-MAIN (fenced, sharper)** for claim 2 (B1032 THE TYPE LAW). **REGISTER** for
claim 3 (the sp.conjugate risk is real, in-practice-heeded, but never became a named
ERROR_LEDGER class — a cheap E-class addition, not a computation).
