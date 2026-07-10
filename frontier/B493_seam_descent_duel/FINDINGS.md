# B493 — CL-1a duel verdict: **PARTIAL** — the repo's own machinery derives the seam lattice law *up to one named, provably pair-specific window lemma*

**Pre-registered duel (docs/CLOSURE_CAMPAIGN_2026-07.md CL-1a; committed enum DERIVED /
OBSTRUCTED / PARTIAL). Protocol: adversarial derive-or-obstruct, exact ℚ(ζ₆₀) arithmetic
throughout (the banked B358 engine; zero numerics), control-gated — the run aborts INVALID if
the mandatory control fails. The control PASSED (12/12 banked bright/dark + the (2,5)
out-of-sample precedent = 13/13; all six banked pair tables reproduced cell-exact from local
data; the flagship t(0,4) exact by two routes). The out-of-sample prediction below was
committed to `b493_prediction_47.json` and written into this file BEFORE any global (4,7)
computation existed anywhere in the repo. Verdict PARTIAL: stages 1–2 assemble into an actual
derivation, machine-checked at every step, but one finite lemma (L5b) resists — and is PROVEN
non-universal, so it is genuinely pair-specific content, not framework. Nothing to CLAIMS.md;
firewall untouched.**

## Control (invalid without it) — all green

- **C1 (cell-exact, strongest form):** the local closed form (stage 1) reproduces all six
  banked B367 pair tables **cell-for-cell** (49/39/31/39/49/39 nonzero cells, every
  (p,q,r,s)-vector exact).
- **C2 (the P67 classification):** local-only bright/dark = banked verdicts **12/12** on the
  banked pairs, and **13/13** including the (2,5) out-of-sample precedent; the s-cell counts
  (44/18/36/24/20/18/12 bright; 0 for all five dark) match the banked global counts exactly.
- **C3 (the flagship):** t(0,4) of (golden, silver) = (1,2) equals
  **−1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15** by both routes (the banked C_theta table and
  the local closed form) = `SC.FLAGSHIP`.

## Stage 1 — the closed form: DERIVED (P64 + P66/P67 + Fourier, nothing else)

**(M) The master identity** (proof: pure Fourier/Galois bookkeeping — the four channel
projectors of H = ℚ(√5,√−3) composed with Π_H are the χ-weighted Galois averages): for the
dual-torus FTs grid_i of the four channel tables,

    grid_i(x,y)·basis_i = (1/16) Σ_{c∈(ℤ/60)ˣ} χ_i(c)·σ_c( C[c⁻¹x mod o₁, c⁻¹y mod o₂] ),
    χ_{p,q,r,s} = 1, χ₅, χ₋₃, χ₅χ₋₃.

*The χ-gate roles are derived here:* χ₋₃ is the c₃-flip sign (it separates the √−3/√−15
channels), χ₅ is the 5-side window character (it separates the √5/√−15 channels).
Machine-checked against the banked global C-table of (1,2): **0/960 mismatches**; against the
fresh out-of-sample global C of (4,7): **0/960**.

**(T) The tensor split** C[j,l] = C₃[j,l]·C₅[j,l] at multiplier (2,2) — banked (P66, P67
G1 12/12); re-verified out-of-sample on (4,7): **0/240 mismatches** (verify phase).

**(S) The support lemma** (proof: C₃ cells ∈ ℚ(ζ₃) with indices mod d_i | 12, so
F₃(c) = σ_c(C₃[c⁻¹x, c⁻¹y]) factors through c mod 12; likewise F₅ through c mod 30; scope
facts, checked: every 3-side order divides 4, every 5-side order ∈ {1,6,10}). Grouping the
16-term master sum by c₃, with X(c₃) = Σ_{c₄}F₃ and Y_ψ(c₃) = Σ_{c₅}ψ(c₅)F₅:

    16·grid_p          = X(1)Y₁(1) + X(2)Y₁(2)        16·grid_q·√5   = X(1)Y_L(1) + X(2)Y_L(2)
    16·grid_r·√−3      = X(1)Y₁(1) − X(2)Y₁(2)        16·grid_s·√−15 = X(1)Y_L(1) − X(2)Y_L(2)

— every object on the right is LOCAL (q=3 / q=5 theta-model data). Machine-checked at **every
dual-torus point of every banked pair (7,328 channel checks) and of (4,7) (960 + 960): zero
mismatches.** With C1 this is the end-to-end derivation of every banked value from local data;
the DFT-split convolution t = Σ ĉ₃·ĉ₅ is P67's spectral convolution made explicit.

## Stage 2 — the vanishing law: DERIVED modulo two named finite censuses

Derivation tree (each step machine-checked at every dual point of all 12 banked pairs, 1,832
points, plus (4,7)):

| lemma | statement | status |
|---|---|---|
| (X0) | X(1) = C₃[x,y] + C₃[−x,−y] | **derived** (coset collapse, d | 4); checked, 0 fails |
| (X̄) | X(2) = conj₃(X(1)) | **derived** (41 = lift(1,2,1) ≡ 1 mod 4 and mod 5); checked, 0 fails |
| (R) | a channel dead with its partner alive forces X/conj₃(X) = ±1 | **derived** (X ∈ ℚ(ζ₃), Y ∈ ℚ(ζ₅), ℚ(ζ₃)∩ℚ(ζ₅) = ℚ; conj₃(t) = 1/t) |
| (N1) | X is never purely imaginary (≠0) | **derived from two finite censuses**: every C₃ cell ∈ {0,1,ζ₆,ζ₆⁻¹} ⊂ μ₆ (checked 12/12 pairs) + (QM); then X = 2u or u + conj₃(u) |
| (QM) | C₃[−j,−l] = C₃[j,l] (j≡l mod 2) else conj₃(C₃[j,l]) | **verified** 16-cell census per pair, 0 fails ×12; mechanism = unitarity + Par-trace reversal; the parity rule itself is the checked step (sub-residue) |
| (L5a) | no window pair (Y_ψ(1),Y_ψ(2)) is ever odd | **verified**, 0 fails at all 1,832+240 points (universal so far; census, sub-residue) |
| (L5b) | tL ∈ {zero, t1} (the χ₅-window's c₃-flip type matches the 1-window's or dies) | **verified on (1,2)** (0/240) — **and PROVEN pair-specific: it FAILS on (1,3) (64 pts) and (2,4) (128 pts)**, mode (gen,even). THE NAMED RESIDUE |

**The classifier theorem (the derivation made executable).** Given X̄ + R + N1 + L5a, the
4-bit vanishing pattern at a dual point is a **function of type-level local data alone** —
(reality class of X, c₃-flip type of Y₁, c₃-flip type of Y_L):

    p dead ⟺ t₁ = zero;   r dead ⟺ t₁ = zero or (t₁ = even ∧ X real);
    q dead ⟺ t_L = zero;  s dead ⟺ t_L = zero or (t_L = even ∧ X real);   X = 0 ⟹ all dead.

Machine-checked pointwise on all 12 banked pairs and on (4,7): **0 mismatches, 0 skips**
(2,072 points) — including on the L5b-violating points, where it predicts exactly the observed
non-lattice single-s-dead tier. Corollaries, all **derived and verified on every pair**:
- **zero stratum:** all-dead ⟺ X = 0 or the Y-quadruple = 0 (0 failures);
- **the ℚ(√−15) node is absent UNIVERSALLY:** q dead forces t_L = zero forces s dead — no
  pair, bright or dark, has a (·,1,1,0)-type point (12/12 + (4,7));
- **lattice containment ⟺ L5b:** on every L5b-clean pair the pattern set ⊆ the subfield
  lattice of ℚ(√5,√−3) minus the ℚ(√−15) node (10/10 banked L5b-clean pairs); both
  L5b-violating pairs show exactly the classifier-predicted non-lattice tier 0001.

**The B459/P1 law on (1,2), derived.** (1,2)'s verified window census is
{(zero,zero): 40, (even,zero): 40, (even,even): 32, (gen,gen): 128}; feeding it through the
classifier with the X-reality strata yields exactly the five patterns and the exact tier
counts **{0000: 120, 0011: 20, 0101: 20, 0111: 10, 1111: 70}** — B459 bit-for-bit, node
absent, zero stratum included. The reduction "global 240-point law → finite local censuses +
theorems" is complete; what is NOT derived is why (1,2)'s census contains no mismatched mode
(that is L5b).

**The χ-gate roles (P68), localized — with two new scope facts (report-only).**
- The **Eisenstein gate localizes and is universal**: on the 3-side table, cell conj₃-real ⟺
  χ₋₃(det(γ′−I)) = +1 (0 violations, 12/12 pairs + (4,7)); at level 15 through the tensor
  identity, P68-L1 (root of unity) and L2 hold on **every** pair incl. (2,5) and (4,7) — and
  the class-1 domain counts reproduce B396's banked 142/63/212/39/142/63 from local data.
  This is the gate the derivation touches: it puts the X-reality stratum (the r/s-death
  switch) into class-field data.
- The **χ₅ gate (P68-L3) is (1,2)-specific**: at level 15 it fails on (1,3): 6, (1,4): 24,
  (2,4): 14, (4,7): 12 domain cells (χ₅(det) = −1 with 5 ∤ ord), and its naive 5-side
  localization fails on the same pairs. Like L5b it is pair content, not framework. (No
  CLAIMS correction needed — P68/B404 computed the (1,2) table and is confirmed there 0/142 —
  but the universalization is now refuted; scope fence recorded here.)

**The dark mechanisms, localized (sharpens B390's named residue).** The window censuses split
the five banked dark pairs into two mechanism classes: (i) **χ₅-window death** — t_L = zero at
every point ((1,5), (4,5); q = s ≡ 0 pointwise; B390's kernel-kill class, plus (3,5) and
(1,4) via all-(even,even)-points-X-real); (ii) **the mismatch mode** — (gen,even) windows with
X real at every such point ((1,3); s = v(X−X̄) = 0). Class (ii) is exactly where L5b fails.
(2,4) shows the same mismatch mode while staying BRIGHT — L5b-failure ≠ darkness; it is
lattice-breaking (the "every value lies in a subfield" property), observed ⟺ L5b throughout.

## Stage 3 — the pre-committed out-of-sample bar: pair (4,7)

**Never computed in the repo** (verified by grep before commitment: the banked pairs with
seed 7 are (1,7), (2,7), (3,7) only; every textual "4,7"/"7,4" hit elsewhere is a cell label
inside a (2,3)/(1,3) table, a GL(2,ℤ) matrix entry in the P4 panel, a torus-scan cell, or a
figsize — none is a seam pair). All pre-commitment (4,7) arithmetic was **local** (the q=3 and
q=5 tables and their products); no level-15 object for (4,7) existed anywhere before the
verify phase.

**THE PREDICTION** (committed 2026-07-10T00:09:30Z in `b493_prediction_47.json`, and written
into this file before the verify phase ran):

- **(4,7) is DARK: the √−15 channel is empty — 0 s-cells, Σs² = 0.** A nontrivial call: all
  three banked 7-pairs are bright, and (4,7) has the same local orders (d,e) = (4,4),(10,6)
  and global orders (20,12) as the maximally-bright flagship pair (1,2).
- Full channel table: **31 nonzero cells**, exact values committed;
  sha256 = `f98532736f97ff5a6dbefc82ea39ae198da6f8129394af3c0b0549f0550cd090`.
- Tier table on the dual torus: **{0001: 96, 0011: 24, 0111: 20, 1111: 100}**; lattice-only
  False (the 0001 tier); ℚ(√−15) node absent.
- Mechanism: L5b fails at 128 points (mode (gen,even), census {(zero,zero): 40,
  (even,zero): 40, (even,even): 32, (gen,even): 128}) — the (1,3)/(2,4) mismatch class; the
  level-15 χ₅ gate is predicted to fail on 12 of its 116 class-1 domain cells.

**OUTCOME: HIT, cell-exact** (verify phase started 2026-07-10T00:14:10Z, after the
commitment above; `b493_verify_47.json`, all_match = true). The first-ever global (4,7)
computation (the 15-dimensional Weil matrices via the banked B367 machinery, orders (20,12))
returned: **DARK, 0 s-cells** ✓; the full 31-cell channel table matches the committed one
**hash-exact** (sha256 equal, every (p,q,r,s) cell equal) ✓; tier table {0001: 96, 0011: 24,
0111: 20, 1111: 100} ✓; G1 tensor identity 0/240 ✓; the master identity against the fresh
global C 0/960 ✓; the XY closed form against the global grids 0/960 ✓; the level-15 gate
census as predicted (L2 0 and L3 12 violations on the 116-cell class-1 domain; L5b fails at
128 points, the predicted mismatch mode). The out-of-sample bar is met in its strongest form:
not just the √−15 verdict but the entire value table was predicted from the two local theta
models alone.

## The named residue (the PARTIAL, per the enum)

**L5b — the 5-side window-matching law.** For the pair's 5-side windowed sums
Y_ψ(c₃) = Σ_{c₅}ψ(c₅)σ_{c₅}(C₅[c⁻¹x mod e₁, c⁻¹y mod e₂]): at every dual point the χ₅-window
pair's c₃-flip type matches the 1-window pair's or dies. True at all 240 points of (1,2)
(and of 9 more banked pairs); **false on (1,3), (2,4)** (and on (4,7): predicted false,
confirmed false at 128 points by the verify phase). Its
truth on (1,2) is the ONLY unproven input to the B459/P1 five-pattern law — everything else
above is derived or a universal checked census. Because it FAILS on sibling pairs, **no
universal argument can prove it**: any derivation must consume (1,2)-specific 5-side data.
This is R2's surviving novel content, sharpened from "why does the √−15 channel vanish in the
lattice-minus-node pattern" to: **why do (1,2)'s 5-side windows never mismatch under the
c₃-flip?** — a finite, precisely posed question about one (10,6)-periodic table of ℚ(ζ₅)
Par-traces (the c₃-flip acts as the mirror l ↦ −l on the e=6 index). Sub-residues (universal
so far, checked censuses, lower priority): the QM parity rule and L5a odd-freeness.
→ DORMANT hint per the prereg; not a kill.

## Honest tiering

- **Derived (proof + machine check):** (M), (S), (X0), (X̄), (R), the classifier theorem and
  its corollaries (zero stratum, universal node absence), stage 1 end-to-end, the (1,2) tier
  counts given the censuses. (T) is banked (P66/P67) and re-verified out-of-sample.
- **Verified finite censuses feeding the derivation:** μ₆-valuedness of C₃ (N1's premise),
  QM (16 cells/pair), L5a, the per-pair window censuses.
- **Verified, not derived, provably pair-specific:** L5b — the named residue.
- **Report-only scope facts:** P68-L1/L2 universal via the tensor route (B396 domain counts
  reproduced); P68-L3 (1,2)-specific; the two dark mechanism classes.
- The verdict is **PARTIAL**, not DERIVED, because the prereg's bar for DERIVED is a proof:
  the assembled machinery does derive the law *from the named finite local censuses*, and the
  out-of-sample bar tests exactly that machinery — but L5b itself remains an unexplained
  regularity of the flagship pair, and it demonstrably carries content the framework does not
  force. It is not OBSTRUCTED either: B491's signed-permutation obstruction (Galois
  equivariance cannot vanish a channel) is untouched, and no new obstruction to a deeper
  derivation of L5b was found.

**Nothing to CLAIMS.md; firewall untouched.** Mathematics only; no physics reading; the
prediction/verification pair is a statement about the level-15 theta model's arithmetic.

## Reproduce

```
cd frontier/B493_seam_descent_duel
../../.venv/bin/python probe.py control   # ~30 s; aborts if the mandatory control fails
../../.venv/bin/python probe.py predict   # ~2 s; commits b493_prediction_47.json (LOCAL only)
../../.venv/bin/python probe.py verify    # ~2 min; builds the global (4,7) table, compares
pytest tests/test_b493_seam_descent_duel.py   # <60 s
```
