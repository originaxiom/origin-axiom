# B1143 — SP-1 CLOSES: the physical B−L is a genuine FOURTH Cartan direction — and the cloud's stated vector was wrong (it was Y − T₃L). A verify-don't-trust catch

**Status: banked (frontier). Verdict PROVED (SP-1 closes — the physical B−L is independent of
{Y, T₃R, T₃L}, robustly across the whole solution family), with a LOAD-BEARING correction to the
cloud's memo 25 and two honest flags (SP-3's "36/36", SP-4). Harvest arc — cloud memo 25
(SP-1/SP-3/SP-4), re-derived on THIS bench with own code (own linear solve + span-membership +
anomaly batteries on B1139's actual banked 27; cross-checked IDENTICAL to B1139's captured run
on a₀,a₂,β_L,β_R,weights). Cloud seat credited. Gate 5 (pure group theory, quantized charges).
Lock `tests/test_b1143_bl_fourth_cartan.py`.**

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

## The load-bearing correction to the cloud's memo 25 (relayed)

The memo's literal `c = [0,−1,0,4/3−c₅,c₅−1,c₅]` (pinned `[0,−1,0,⅓,0,1]`) **does not solve the
construction** on B1139's actual 27 (only 2 of the 12 equations hold; the Y=⅙ sextet returns −⅓,
never +⅓ — mismatch table pinned). And the pinned vector is **exactly B−L = Y − T₃L** (verified
component-for-component, combo x=1,y=0,z=−1): it sits **IN span{Y, T₃L}**, so it **FAILS** the
independence test, and it is **not SU(2)_L-uniform** (−⅓ vs +⅔ on the same Y=⅙ sextet), which a
true B−L must be. **Had the cloud's literal numbers been banked uncritically, they would have
banked a false positive on the one question that matters.** This is a *load-bearing* correction
(unlike the family_triplet / spin-payment convention slips): the memo's **conclusion is right**
(B−L is a 4th Cartan direction) but its **stated vector is wrong** — the correct family is
c = [0, c₁, 0, −⅓, 1, 0]. Priority relay to the cloud seat.

## SP-3 — table invariance CONFIRMED; the "36/36" count FLAGGED

The exhaustive assignment search finds **72 distinct physical (β_L,β_R,s,t) assignments**, all
inducing the **same single (T₃L,Y,Q) table** — invariance confirmed. Own anomaly batteries: a
5-charge battery (30 traces, linear+cubic+mixed over T₃L,T₃R,Y,Q,B−L) → **30/30 vanish**; a Y/Q-only
battery (6 traces) → **6/6 vanish**. **FLAGGED:** neither battery — nor natural degree-≤3 monomial
counts on 2 or 5 charges — reproduces the memo's specific **36** without fitting to that number;
the anomaly-freedom is real, the count "36/36" is not independently reproduced.

## SP-4 — FLAGGED (not computable from the spec)

No primary memo-25 / SP-4 text exists in the repo; the "2592" grep hits are coincidental numeric
substrings. Arithmetic note only: 6⁴·2 = 2592 is *consistent with* ⟨W(A₂)⁴, NEG⟩ being an index-2
extension — but this frame is **three** A₂ slots (W(A₂)³, order 216), **not four**; no rank-8 /
four-A₂ structure is established here. NEEDS the cloud's primary text; not independently computable.

## Net

SP-1 closes — the object's forced structure carries a genuine fourth Cartan (B−L), independent of
Y/T₃R/T₃L; combined with the fork's charges (B1138/B1139) the closing's Cartan content is complete.
The one *positive-with-a-correction* of the value remainder, and a clean demonstration that
verify-don't-trust catches load-bearing errors, not just convention slips. Cloud seat credited.
