# SEALED PREREGISTRATION — the VOLUME-IN-BASIS probe (extending B1137)
## (outside bench, 2026-08-29. WRITTEN AND COMMITTED BEFORE ANY COMPUTATION. This is a VALUE-CROSSING cell — the most dangerous kind this programme runs — and it is preregistered accordingly. Nothing below may be edited after the run; findings go in an addendum or a memo.)

## §0 — WHY THIS CELL EXISTS, AND WHY IT IS SMALL

Memo 139 found, while re-checking a staleness flag, that **B1137's
regulator basis does not contain the complex volume.** Its basis is
verbatim:

> {L(n,χ₋₃) n=1..6, ζ_K(n) n=2..6 [ℚ(√−3)], L(n,χ₅) n=1..4, ζ_F(n) n=2..4
> [ℚ(√5)], π, √3, √5, log φ, ζ(3)}

**re-read from primary and confirmed: no Vol, no CS.** Meanwhile **B1209**
banks (citing Lee, arXiv:2502.11950) that the complex volume **is a
Beilinson regulator over ℚ(√−3)** — the object's own field. **So the
object's most canonical regulator was absent from the regulator probe.**

**This is an untested corner of one instrument, NOT a hole in the
negative.** B1126 already swept a **volume/ζ_K(2) family** among 16 sealed
periods against 22 SM targets (352 pairs, 351 below two significant
figures). **The honest prior is a ninth value-crossing negative**, and
this cell is run to *close the corner I found*, not because a hit is
expected.

## §1 — THE INSTRUMENT (reused verbatim; the exhaust-before-building rule)

B1137's own modules, read from the pinned commit: `regulators.py`,
`basis.py`, `targets.py`, `pslq_probe.py`, `verify.py`. **The only change
is the addition of basis entries.** No re-implementation, no
re-tuning of thresholds, no change to the gate.

**ADDED BASIS ENTRIES (the whole intervention):**
- `vol` — Vol(m004), the hyperbolic volume;
- `vol_pinorm` — Vol/π (matching the basis's own π-normalization
  convention for ζ_K/ζ_F);
- `vol_over_zetaK2` — Vol/ζ_K(2), the combination B1126 itself named.

**CS is NOT added**, and the reason is stated: the record banks **CS = 0**
for the cusped m004, so the complex volume is Vol + 0i and CS contributes
no independent direction. Adding a zero would be padding.

## §2 — GATE 5, STATED EXPLICITLY

Measured SM values enter **only as comparison targets for a computed
negative** — never as inputs to any derivation. This is the same standing
allowance B1137 and B1126 ran under. The targets are **B743's sealed
`pdg_targets.json`, loaded verbatim with its sha256 recorded**, not
fetched or re-selected by this bench. **No measured value touches the
basis.**

## §3 — THE PREREGISTERED TWO-OUTCOME, FIXED NOW

- **V-NEG (expected):** adding the volume directions yields **no new
  gated hit**. ⟹ B1137's DISJOINT verdict **extends to a basis containing
  the object's own canonical regulator**, and the corner memo 139 named is
  **closed negatively**. This strengthens the value wall; it does not
  weaken it.
- **V-HIT:** some SM target becomes a bounded-height algebraic combination
  involving a volume direction, **passing B1137's own unmodified gate**.
  ⟹ the value verdict's named untested tier closes the other way, and
  **this bench says so in advance.**

**A V-HIT IS NOT BANKED ON SIGHT.** It must clear, in this order, before
any claim is made:
1. **B1137's own `involves_regulator` gate** — a relation with zero
   volume content is the V-alone tautology and is NOT a hit;
2. **the look-elsewhere account** — the added directions enlarge the
   search space, and the base rate must be recomputed against B1137's own
   matched null, not quoted from it;
3. **the height/precision discipline** — the relation must survive at the
   declared working precision with the declared coefficient-height bound;
4. **the kind check** — per `KIND_TABLE.md`, a relation must not pair
   kind-inadmissible quantities.
**Failing any of the four, the outcome is reported as V-NEG with the
near-miss exhibited**, exactly as B1126 handled its one escalation-bar
pair (C1/C0 vs sin θ₁₂, dismissed on three independent grounds).

## §4 — WHAT WOULD MAKE THIS CELL WORTHLESS, NAMED IN ADVANCE

- If the added directions are **linearly dependent** on the existing basis
  at working precision, the cell adds nothing and must say so — B1137's
  own `basis_hygiene_check` found six such redundancies and dropped them.
  **The same check is run on the new entries first**, and a dependent
  entry is dropped, not kept.
- If the run cannot reproduce **B1137's original result on the unmodified
  basis**, the instrument is not faithfully reused and **no extended
  result may be reported at all**. This is the gating control.

## §5 — THE CONTROL, STATED BEFORE THE RUN

**REPRODUCTION CONTROL (gating):** run the unmodified basis first and
confirm B1137's headline — **0 of 18 targets involve a regulator**. Only
if that reproduces does the extended basis run.

**Sealed 2026-08-29, before any computation. The bench commits to
reporting the outcome that fires.**
