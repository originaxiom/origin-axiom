# Item 1 — B8087 the neutrino selector (⟨ν^c⟩ purity)

## HEADLINE (relay's ask, verbatim)
From `CC3_TO_CC_2026-08-19_BLOCKER_EXPIRED_AUDIT_STARTING.md` §4:
> "**B8087** — `⟨ν^c⟩` is a **second free selection**: purity is the unique rank-4 condition (pure
> stabiliser 34, toral 4; generic 29, toral **0**), but Spin(10) is transitive on the pure cone. So
> B1017's single "VEV direction" row is right **only in the PAIR space** (`27⊕27`)."

Task's framing of the open question: "B8087's purity/VEV-direction claim has no trace on main" —
what exactly does B8087 prove, is it computed, and does main already book two selections or one?

## THE CLAIM (every number)
Arc `audit/wt-cc3/frontier/B8087_neutrino_selector` (cc3, 2026-08-19), instrument `so(10)` on the
16-dim even half-spinor, built explicitly over ℚ as fermionic bilinears on the even part of
Λ*(ℂ⁵): `so(10) = Λ²(ℂ⁵) ⊕ gl(5) ⊕ Λ²(ℂ⁵)*`, 10+25+10 = 45 generators, no structure constants
quoted (990 bracket pairs implicitly, rank 5).

- **Pure spinor**: literal stabilizer dim **34** (`sl(5) ⋉ Λ²(ℂ⁵)`), orbit dim **11**, toral part
  **4** — rank 5→4 happens here.
- **Generic spinor**: stabilizer dim **29**, orbit dim 16, toral part **0** — rank destroyed
  entirely.
- **Transitivity**: `45 − 34 = 11` = dim of the (affine) pure spinor cone (projectively `S₁₀` is
  10-dim) — Spin(10) is transitive on the pure cone, **one orbit**.
- **Control that mattered**: the first build (omitting the spinor shift `h_i = a_i†a_i − ½`) gave
  an algebra isomorphic to so(10) (dim 45, closed, rank 5, every structural check green) but in a
  **character-twisted representation**, silently moving the stabiliser to **35**. Only the
  predicted stabiliser dimension caught it.

**Conclusion drawn**: `⟨ν^c⟩` is a **second, free** selection, not forced by `⟨1⟩`. B1017's single
"VEV direction" ledger row is correct only if read as one point in the **pair space** `27⊕27̄`
(Kato–Yukie's object); read as one direction inside a single 27, it **undercounts by one**.

## COMPUTED / CITED / ASSERTED
**COMPUTED.** Function: `neutrino_selector.py` (in the arc) builds the 45×45 matrix
representation, computes stabiliser dimensions by exact rank of a linear map (pure vs two
independent random-rational generic vectors), and checks orbit-dimension = cone-dimension.
`results.json` records `stab_dim: 34` (pure) / `29` (generic), `rank_after_breaking: 4` / `0`,
`orbit_dim: 11` = `orbit_equals_cone_dim: true`. Gate 5 untouched (SM enters only as the rank-4
*target*, no SM quantity produced) — self-declared and consistent with the file contents.

## ON MAIN ALREADY? — YES, independently re-derived and SHARPENED, one day later
1. **`frontier/B1017_recount/FINDINGS.md`** (main, cc, 2026-08-10 — predates B8087 by 9 days) is
   the ledger B8087 is arguing against. It already states, verbatim (line 20):
   > "the 6→4 drop is entirely `⟨1⟩` then `⟨ν^c⟩`, **neither an involution**"
   B1017's own recount table books **one** row, "VEV direction," as **UNSOURCED**, and explicitly
   flags: "the VEV's *magnitude* is weight-1 and may fold into the ℝ₊ — the fifth resource could be
   shared rather than new." So main's own B1017 already treats the two-step VEV as a live open
   question about resource-counting — it does NOT silently claim "one selection" as settled fact;
   it flags the slot as unsourced/open.

2. **`frontier/B1092_purity_selector/FINDINGS.md`** (main, 2026-08-20 — one day after B8087) is an
   **independent own-code re-derivation of the identical theorem**, with two sharpenings beyond
   B8087: it disentangles the **literal** stabiliser (34, matching B8087 exactly) from the
   **projective** stabiliser of the line ℂv (**35** = `gl(5) ⋉ Λ²`, the parabolic, with
   `45 − 35 = 10 = dim 𝕊₁₀` exactly, the textbook parabolic dimension) — precisely resolving the
   ambiguity that caused B8087's own "34 vs 35" character-twist bug. Verdict: PROVED. Quote:
   > "The second VEV `⟨ν^c⟩` must be a pure spinor... Spin(10) is transitive on the pure cone — the
   > selector exists as a CONDITION, not a POINT... the one-slot count is pinned to the PAIR space
   > `27⊕27̄`."
   This is the *exact same conclusion* as B8087, independently computed.

3. **`docs/SM_SPECIFICATION_LEDGER.md:213-214`**: "charge taking **two** — a chirality sign *and* a
   rank-reducing VEV — ~~which B963 proves compete for one resource~~ *(corrected 2026-08-10,
   B1017: the compete-corollary is retracted — the VEV closing is not effected by an involution;
   the two holes need two resources, the second unsourced)*." And **line 277-279**: "**Jointly with
   B1092's purity selector** (the second VEV is a condition on an 11-dimensional cone, not a
   point... completeness of the anomaly content and the purity condition on the VEV side are two
   faces of one fact), the current honest sentence for THE RANK WALL is: **one unsourced slot,
   pair-space-valued, purity-conditioned**..."

**So main already books TWO selections** (chirality sign + rank-reducing VEV, itself two-step:
`⟨1⟩` then `⟨ν^c⟩`), consistent with B8087's reading, not the single-row misreading the relay
worried about.

**Discrepancy in the harvest audit itself**: `frontier/B1412_the_relay_backlog/FINDINGS.md:29`
grades this relay "OPEN — B8087's purity/VEV-direction claim has no trace on main... trace: B8087:
NONE (docs/HARVEST_LEDGER.md row 261 = SCHEDULED, no main arc names it)." **This is only true of
HARVEST_LEDGER's frontier-arc scan.** `docs/OPEN_LEADS.md:1905`, row **L168**, explicitly names
B8087 by band ("the seat computed (B8087, their band)...") and is marked
**"CLOSED — B1092 (2026-08-20); the selector is a CONDITION, proof grade."** B1412 missed this
because it did not check OPEN_LEADS.md's L168 row. B1092 itself, however, does NOT cite "B8087" or
"cc3" anywhere in its FINDINGS.md/arc_verdict.json text — the credit lives only in OPEN_LEADS.md,
not in the arc file itself (a thin provenance gap, not a missing result).

## NEEDS COMPUTATION HERE
None — main already carries an independent, sharper re-derivation (B1092) verified proof-grade,
plus the ledger-level bookkeeping (B1017 + SM_SPECIFICATION_LEDGER D3/D4) already reflects two
selections. No discriminating fact is outstanding for this item.

## GRADE PROPOSAL: **ALREADY-ON-MAIN** (superseded in the strong sense — B1092 is a sharper,
independently-verified re-derivation of B8087's exact claim, landed one day after B8087, and the
ledger already books two selections, not one)

**Residual action, not mathematical**: `frontier/B1092_purity_selector/` should gain a citation
line crediting cc3/B8087 as the prior independent hit (currently silent on provenance), and
`docs/HARVEST_LEDGER.md` row 261 should be updated from SCHEDULED to reflect L168's CLOSED status
in OPEN_LEADS.md — the harvest ledger and the open-leads ledger disagree about whether main "names"
B8087.
