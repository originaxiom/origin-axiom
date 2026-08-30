# B1143 — SP-1 CLOSES: the physical B−L is a genuine FOURTH Cartan direction — confirmed two-bench with cloud memo 25

**Status: banked (frontier). Verdict PROVED (SP-1 closes — the physical B−L is independent of
{Y, T₃R, T₃L}, robustly across the whole solution family), CONFIRMED TWO-BENCH with cloud memo 25
(both benches build B−L the same way — a Cartan functional from the forced targets — and both
find a 1-parameter family that is physical on all 27 and independent). Harvest arc — cloud memo 25
(SP-1/SP-3/SP-4), re-derived on THIS bench with own code (own linear solve + span-membership +
anomaly batteries on B1139's actual banked 27; cross-checked IDENTICAL to B1139's captured run
on a₀,a₂,β_L,β_R,weights). Cloud seat credited. Gate 5 (pure group theory, quantized charges).
Lock `tests/test_b1143_bl_fourth_cartan.py`.**

**Reframed 2026-08-25 (see B1144). An earlier version of this arc claimed a "load-bearing
correction to the cloud's stated vector" (that memo 25's vector was Y − T₃L). That claim is
WITHDRAWN.** Verification against memo 25's **primary certificate** (`sp1_bl.py`) shows the memo
builds B−L in the **closing's own coordinates** and gets it physical on all 27, independent — its
construction is correct. The apparent mismatch was a **cross-frame artifact**: the memo's
frame-specific components, evaluated in B1139's differently-ordered 27, spuriously read as Y − T₃L
(in-span, non-uniform). This is the same adoption-layer class as the ℚ(√−3) basis slip (B1144 §1),
**not** a defect in memo 25. The two benches AGREE on the substance.

## SP-1 — CONFIRMED: B−L is a genuine fourth Cartan direction

Solving f(α₀)=f(α₂)=0 (color) + the 10 forced quantized targets (the six colored Y=⅙ states ↦
+⅓, the three colored Y=−⅔ ↦ −⅓, the singlet Q=+1 ↦ +1) on B1139's banked 27 gives **rank 5,
nullity 1** — a genuine **1-parameter family c = [0, c₁, 0, −⅓, 1, 0]** (β_L is auto-redundant,
f(β_L)≡0 along the family; β_R over-constrains). At the representative pin (c₁=0, c = [0,0,0,−⅓,1,0]):
- **Tr(B−L) = 0 and Tr(B−L)³ = 0 identically for the WHOLE family** (stronger than one pin); all 27
  weights land in {0, ±⅓, ±⅔, ±1}, matching textbook fermion assignments.
- **THE LOAD-BEARING CLAIM (fourth direction), exact + symbolic for the whole family:**
  span{Y, T₃R} is **UNSOLVABLE** (witness w with w·Y=w·T₃R=0 but **w·B−L = 3/2**); span{Y, T₃R, T₃L}
  is **UNSOLVABLE** (witness **w·B−L = 3**). Both robustly unsolvable — B−L is independent of the
  existing charges. **SP-1 closes** (B1139's open cell).

## Reconciliation with memo 25 (the apparent vector mismatch was a frame difference, not an error)

The naive vector this bench evaluated — `c = [0,−1,0,4/3−c₅,c₅−1,c₅]`, pinned `[0,−1,0,⅓,0,1]` —
does not solve the construction **on B1139's 27** (only 2 of the 12 equations hold), and in
B1139's frame it is exactly Y − T₃L (combo x=1,y=0,z=−1), which sits in span{Y, T₃L} and is not
SU(2)_L-uniform. But memo 25's own certificate (`sp1_bl.py`) builds B−L **in the closing's
coordinates** (a different Cartan frame / simple-root ordering than B1139's), where it is physical
on all 27 and independent — verified in the golden_gate primary source. So the mismatch is a
**frame difference**: the same physical B−L has different component vectors in the two frames, and
reading one frame's numbers in the other produces a spurious non-solution. **The correct statement
is two-bench agreement**: B−L is a genuine fourth Cartan direction (this bench's family
c = [0, c₁, 0, −⅓, 1, 0] in B1139's frame; memo 25's c₅-family in the closing's frame). The
withdrawn "catch" is recorded in B1144 as an adoption-layer (cross-frame) misjudgment.

## SP-3 — table invariance CONFIRMED; the "36/36" count FLAGGED

The exhaustive assignment search finds **72 distinct physical (β_L,β_R,s,t) assignments**, all
inducing the **same single (T₃L,Y,Q) table** — invariance confirmed. Own anomaly batteries: a
5-charge battery (30 traces, linear+cubic+mixed over T₃L,T₃R,Y,Q,B−L) → **30/30 vanish**; a Y/Q-only
battery (6 traces) → **6/6 vanish**. **FLAGGED:** neither battery — nor natural degree-≤3 monomial
counts on 2 or 5 charges — reproduces the memo's specific **36** without fitting to that number;
the anomaly-freedom is real, the count "36/36" is not independently reproduced. (memo 25 states
36 physical assignments in the closing's frame; this bench's 72 is in B1139's frame — plausibly the
same set up to the same frame/pin freedom, not reconciled to the count here.)

## SP-4 — FLAGGED (not computable from the one-line spec at bank time)

At bank time no primary SP-4 text was in-repo; the "2592" grep hits were coincidental. Arithmetic
note only: 6⁴·2 = 2592 is *consistent with* ⟨W(A₂)⁴, NEG⟩ being an index-2 extension — but B1143's
frame is **three** A₂ slots (W(A₂)³, order 216), not four. The primary SP-4 material now lives in
golden_gate (memo 25's four-slot ℤ₂ = the E₈ antipode w₀ = −1); reconcilable there if promoted.

## Net

SP-1 closes — the object's forced structure carries a genuine fourth Cartan (B−L), independent of
Y/T₃R/T₃L; combined with the fork's charges (B1138/B1139) the closing's Cartan content is complete.
**Confirmed two-bench with memo 25** (both build it from forced targets; both get a physical,
independent fourth direction). The earlier "load-bearing catch on the cloud" is withdrawn as a
cross-frame artifact (B1144). Cloud seat credited.
