# B1217 — THE SEAT INTEGRATION: nineteen commits harvested, four things verified, one evidence-contract gap found

**Verdict**: `OPEN` (harvest arc) · **2026-08-30** · **Gate 5 clean** · discharges the integration
debt the owner named: *"did you sync/merge/integrate the rest of the branches as per our rules, and
all banked and reflected?"* — the honest answer at the time was **no**, and this is the fix.

**Scope**: codex **2** commits (R025, R026) + their R027 lead; cloud **17** commits. cc3: nothing new.
Per *integrate-don't-merge*, nothing is merged — harvested, verified where possible, rebanked here.

## VERIFIED ON THIS BENCH

**codex R026 — the determinant frame.** Their certificate runs here with output identical to theirs
(exact Euler minor rows (0,1,2,3,6,7), determinant **−72ζ²**, characters **B:6 W:11 G:7**, wedge sign
**+1**, quotient-lift invariance PASS). Re-running a script is not verification, so two cores were
re-derived from first principles:

- **W:11 is the direct sum of the selected ray characters** (0+2+6+8+9+10 = 35 ≡ 11 mod 12).
- **The three determinant characters cancel**: B + W + G = **24 ≡ 0 (mod 12)**. *That cancellation is
  the equivariance the frame requires* — and codex reports the three numbers **without flagging it as
  the consistency check**. Controls confirm it is not automatic: (6,11,8), (5,11,7), (6,10,7) all fail.
- **The wedge sign is +1 by inversion count** (the differences are forced; permutation (1,2,4,3,5,0),
  6 inversions), with a parity control returning −1 on an odd rearrangement.

> **Δ_G is built — component 1 of 3** of the evaluator that decides the ℙ³. Their scope carries
> verbatim: the normalized H³(O_Y) trace is still required for all 18 connecting entries, and the
> Serre map for tails. **B1208's fork and the ℙ³'s surviving dimension remain open.**

**codex R027's simplification — confirmed, and it matters.** Their claim that the normalized product
trace needs no 36-chart reduction, because a factor trace cycle has eight triangles whose
Eilenberg–Zilber cross product gives at most **8² × 6 = 384** product simplices: **384 confirmed
here, and the 6 is exactly the count of (2,2)-shuffles**, C(4,2). The degrees work too — a 2-cycle
crossed with a 2-cycle is a **4-cycle**, the right degree to evaluate an H⁴ class. This replaces a
432-open refinement with an explicit finite cycle. **A lead, not a delivered result** — it is theirs
to run, and it is component 2 of 3.

**codex R025 — independent confirmation of B1215.** They certify the same law this bench derived
separately: `A_a B_ρ B_σ` is invariant **iff ρ + σ ≡ 3 − a (mod 12)**, so A₇ needs 8 and A₁₁ needs 4.
They go further than we could: the physical charged-lepton/Higgs block is explicitly
**A₁₁ × B₂ × B₂**, and its only pure-tail term repeats the one-dimensional tail-2 direction and is
zero by skewness. **Their own scope line is carried**: no mixed or connecting term is evaluated, so
the fork stays open. *(B1216 separately corrected B1215's enumeration — it missed (8,8).)*

**cloud's V-NEG — verified at both checkable points, against our own data.**

- Their **hygiene pre-step runs here** against B1137's own `basis.py` and reproduces exactly: the
  three volume directions (`vol`, `vol_pinorm`, `vol_over_zetaK2`) are **independent** of B1137's
  25-entry pruned basis, **0 dropped**, with Vol(m004) = 2.029883212819307… **computed** from
  ½·Im Li₂ rather than quoted.
- Their **gating control is confirmed against B1137's own banked report**: **117** raw relations,
  **all 117** passing `involves_V`, **0** passing `involves_regulator` — matching their claim exactly.
  And the target they name as losing nine cells in the extended run, **|Vub|**, carries `raw_found = 9`
  with **`involves_regulator = 0`** — so their 117 → 108 explanation **holds from our side**:
  dropping those cells masks no hit, because the deciding column is zero in both runs.

## THE EVIDENCE-CONTRACT GAP

**Cloud's extended run — the V-NEG headline itself — is not reproducible as committed.** The file at
`outside_bench/certificates/vol_basis_extended.py` on their branch contains the **basis builder**
(R48-3), not the extended probe. No committed certificate carries the `involves_regulator` gate
except an unrelated staleness re-check, and **their own memo names no path for it**.

> **Typed precisely**: the headline is **CITED**, with **both checkable sub-claims CONFIRMED** and the
> run itself unreproduced. This is an **evidence-contract gap, not a mathematical one** — and it is
> the same class codex flagged and cloud fixed one instance of on the same day. Relayed, not fixed
> here: their branch, their call.

## HARVESTED AND TYPED (read, not re-run)

**Cosmology — the three blind rows are one obstruction.** Rows 2 and 8 are **not two gaps**: one
needs the log of a volume ratio, the other an exponent with respect to a scale factor, and **both are
the same missing object**. Row 8's growth is exponential-class, not power-law (log-log slope climbs
2.81 → 10.14 while the log-linear slope is near-constant), **so no exponent exists to compare
whatever its value** — and there is no scale factor to differentiate against, banked twice. Row 7 is
dispositioned target-by-target rather than by blanket inheritance: **part proved-negative, part still
missing**, and they flag that split as deliberately weaker. Beside it: the proposed *"expansion"* is
**determinant-one shear, not FRW volume expansion**, so no e-fold derivation or physical scale factor
follows. **This lands on `COSMOLOGY_LEDGER.md` and should be reflected there at the next review.**

**Governance — both owner-authorized, both handled with restraint.** The **θ-even crossing (I3)** hold
was released by the owner **and cloud did not fire it**: they ran the prior question — *does the shot
have a determinate output?* — and found **four independent reasons it does not, any one sufficient**,
with all four of I3's own pre-work items outstanding. **The licensed row is unspent.** The
**specialist send-queue** hold was released, and they note two rules survive a blanket release: the
send is the owner's act under the owner's name, so the bench prepares rather than transmits; and
*"nothing leaves without a per-item word, which a blanket release does not supply."* Their readiness
audit then found **Q1 stale by eight post-queue arcs — because of our B1209** — and rewrote it.

**Their own self-correction**: *"Q2 disposition: the staleness flag was mine and it was wrong"* —
diagnosed as a false positive **of the same shape B1210 caught on its own first pass**. Third seat,
same lesson. They also **fixed the floating-ref defect** codex flagged and we relayed, and adopted a
**push-as-you-go** practice so other seats read a current head.

## ONE REPAIR TO OUR OWN LOCK

The L154 drive-by-mention lock tripped twice on legitimate discussion and both are admitted with the
conditional test intact: **B1207's FINDINGS** — which *documents the repair of that very lock* and so
quotes its criterion (*"Brown–Henneaux and (E₆)₁ in one file"*) — **the third instance of the
self-documenting-instrument class** this week, after `already_banked.py` and B1207's own machine-path
literal; and **`docs/THEOREM_REGISTRY.md`**, which B1214's re-audit populated with theorem rows that
name the partition function and the boundary. **A registration surface is the last place that lock
should be barring discussion.**
