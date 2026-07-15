# B598 — the L85 campaign opened; P0 (the C1 baseline) computed

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities. The
campaign document: CAMPAIGN.md (cells P0–P3, the constraint sheet, locked
outcomes per the adopted D1 prereg). Locks `tests/test_b598_p0.py`.
Provenance: all verification internal (owner + AI seats) — see the
pre-committed Review-18 scope in docs/progress/REVIEWS.md.**
Run: `python3 p0_c1_baseline.py` (mpmath, ~2 min).

## P0 — the C1 baseline: a CALIBRATION (relabeled per the seat-4 audit, 2026-07-15)

(The extraction is self-consistent rather than independent — the growth-rate
gate uses the measured prefactor; the identified constants agree with the
externally known asymptotics, which is what a calibration establishes.)

The Kashaev invariant ⟨4₁⟩_N (the Habiro sum), N = 100..1600 at 40 digits:
- **The growth gate:** the corrected rate equals Vol(4₁)/2π to 1.15×10⁻⁴¹.
- **The 1-loop constant:** Richardson-extrapolated,
  > r_∞ = 0.759835685659812 = **3^{−1/4}** (agreement 8×10⁻¹²; the nearest
  > competing candidate is 24% away).
So ⟨4₁⟩_N ~ N^{3/2}·3^{−1/4}·e^{N·Vol/2π}: the τ₁-content is exactly where
the semiclassical correspondence puts it. Normalization bridge (recorded):
in the standard 1/√T one-loop form, T = √3 with **T² = |τ₁| = 3** (B581's
convention) — the Gaussian width enters squared, consonant with the hearing
law's quadratic structure. This upgrades the D1 prereg's B425-row from
[CITED] to [COMPUTED]: the SL(2) dictionary's baseline datum is now
in-sandbox.

## The campaign (CAMPAIGN.md)

P1 (the cusp table: the six H¹ representatives restricted to the peripheral
subgroup — the classical domain made explicit), P2 (the quantization arrow
through the Weil model at κ = 5, checked against the five-item constraint
sheet), P3 (the verdict cells C2/C3 and the locked A/B/D outcome). The
machinery inventory distinguishes what exists (B575/B581/B587 machinery)
from what P1/P2 must build (the per-block Fox H¹ solver with the peripheral
restriction; the Jordan-filtration pairing with the theta-basis).

## Governance registered alongside (owner directive)

Review 18's pre-committed scope now includes the provenance sweep (no
banked language may read as external verification/peer review — all
verification is internal, owner + AI seats since day 0; PROVENANCE.md to be
created at review) and the inner-terminology legibility sweep
(TERMINOLOGY.md or rephrasing). Registered in docs/progress/REVIEWS.md and
in the standing memory.

## Anchors

Chat-1's D1 prereg via B597 (adopted, corrected), B595/B596/B597 (the
constraint sheet), B581 (τ₁ = −3), B587 (the Weil machinery for P2), B575
(the H¹ model for P1), B67 (the longitude convention to pin in P1).

## P1 — THE CUSP TABLE, computed (exact; the classical domain data for P2)

`p1_cusp_table.py` (OA_SLOW; full output with all exact values:
`p1_cusp_table_output.txt`). For every block m ∈ {1,4,5,7,8,11}: a fresh Fox
cocycle solve over the exact B575 model gives **dim H¹ = 1** (an independent
re-derivation of B575-G4 — and a second, more direct discharge of B572-V2),
the regular-unipotency gate rank(ρ(a)−1) = d−1, and the exact peripheral
values **ξ(μ = a)** and **ξ(λ = [b,a])** (the fiber-boundary longitude, B67's
convention), normalized to leading coordinate 1. The m = 1 row, in full:
ξ(μ) = [1, 0, 3/8 − w/8], ξ(λ) = [3/4 + 3w/4, 1/4 + w/4, −w/2] (w = √−3).
The six (ξ(μ), ξ(λ)) pairs are the campaign's 6×2 boundary data — the dial's
cusp shadow, now explicit, exact, and entirely ℚ(√−3)-arithmetic (the
role-separation law's structural side, on display).

## The handoff adjudication (HANDOFF_ADJUDICATION.md)

The shifted-saddle ansatz adopted; the S₁-factorization registered as a P3
gate; the number-field claim CORRECTED in-sandbox (√−3 ∉ ℚ(ζ₂₀); the
amplitude lives in ℚ(ζ₅)) and replaced by the cleaner role-separation law;
the width bridge's θ-odd extension registered as P3's check; the anisotropy
remark held as a [HOOK]. Review-18 timing override registered (fires on L85
resolution, owner directive).


## CORRECTION (2026-07-15) — the longitude word; Gate A's catch

P1's first run evaluated ξ on "baBA" = [b,a] — the FIBER-frame boundary
commutator (B67's convention belongs to the trace-map/fiber presentation) —
which is NOT the longitude of B575's meridian presentation
⟨a, b | aWb⁻¹W⁻¹⟩, W = bABa. **P2's Gate A (the ℤ²-cocycle compatibility)
failed at every block and caught it.** The true longitude was then found by
direct search in the geometric SL(2) rep (c = (1+√−3)/2 solved from the
relator): **λ = "abABaaBAbA"**, self-certified by its image
−[[1, 2√3·i],[0,1]] — the off-diagonal is exactly the banked cusp shape
τ = 2√3·i, and it commutes with the meridian. With the true λ, **Gate A
passes at every block** (P1's table is a genuine ℤ²-cocycle restriction) and
the λ-column is regenerated (p1_cusp_table_output.txt superseded in place;
the ξ(μ) column, the H¹ = 1 gates, and the unipotency gates were never
affected). The same correction goes to chat-2: their item-5 input is
λ = "abABaaBAbA", not "baBA" as I first answered (B599's FINDINGS note
corrected below).

## P2 — the quantization arrow: gates green; the first-order table is DATA; the arrow is quadratic

`p2_quantization_arrow.py` (OA_SLOW; output `p2_output.txt`). With the true
longitude: **Gate A (ℤ²-compatibility) and Gate B (the coordinate ↔ gl(27)
embedding intertwines Ad) both pass at every block.** The first-order
boundary character shifts δtr₂₇(μ), δtr₂₇(λ), δtr₂₇(μλ) are banked exactly
per block — all six blocks generically NONZERO. **The registered parity
prediction (odd rows zero) was WRONG and is retired with its diagnosis:**
tr₂₇ is not a Θ-invariant contraction (θ maps the 27 to the 27̄), so the
selection rule never applied to it; the Θ-structured pairing for the
campaign's matching is the Ω-form pairing (chat-2's algebraic face), where
the k = 1 vanishing IS proven (L1, B599-ALG). Consequence for P3 (the
structural verdict): the arrow's Θ-graded content is quadratic — the
classical side of the matching is the banked B599-ALG t²-family; the
first-order δtr table is the even-channel (gauge) boundary data.

## Readiness steps 3 + 5 — banked (2026-07-15)

**Step 3 — THE UNIVERSAL BOUNDARY RATIO.** The gauge-invariant content of the
cusp table, per block: the invariant form G (unique up to scale, solved
exactly), the peripheral-invariant line w, and the invariant ratio. The
result: **I_λ/I_μ = −2√−3 at every one of the six blocks** — the gauge- and
scale-invariant content of the entire table is ONE number, and it is the
banked universal cusp datum τ (PC25's "single universal cusp datum across all
exponents"), now re-derived from the Fox pipeline through canonical
functionals. Gauge gates and rank-6/6 nonvanishing asserted (failure-
enforcing). What this does NOT supply (D4): the cross-domain normalization —
step 4's obligation, unchanged.

**Step 5 — THE EXACT 27–27̄ INTERTWINER J.** Solved on the generators
{e_pr, f_pr, v₄} with θ = ±1 by block parity, weight-reduced (support 49 of
729): **Schur-unique (solution dim 1), invertible (rank 27), group-gate
green (A27ᵀJA27 = J)** — and the control seat 4 demanded: **the untwisted
solve (no θ) returns dimension 0** — there is no E₆-invariant bilinear form
on 27×27, verified as a computation. Convention fixed: J intertwines ρ₂₇
with the θ-twisted contragredient on the SAME explicit 27 basis
(ρ(X)ᵀJ + Jρ(θX) = 0). **The J-corrected L1 zeros hold:**
(v_m v₀)ᵀJv₀ = 0 exactly at m = 4 and 8 — chat-2's parity lemma survives on
the legitimate pairing. The restated selection-rule lemma for the J-pairing
(the linear-C vs antiunitary-Θ distinction, D5's full demand) is now
well-posed and queued as the next document, with these zeros as its first
data. Locks: `tests/test_b598_steps35.py` (OA_SLOW, subprocess-manifest,
D8-compliant).

## The restated symmetry lemma (D5 complete) + the forced-zero map — banked (2026-07-15)

`lemma_cell.py` (assert-hardened; first-run output `lemma_cell_output.txt`,
hashed; re-verification in flight at bank time — the asserts encode the
observed values and the OA_SLOW lock follows its green):

- **(i) J is SYMMETRIC** (Jᵀ = J, Schur-forced).
- **(ii) THE MOVE-ACROSS LEMMA** ⟨Xu, v⟩_J = −ε_X ⟨u, Xv⟩_J — exact on all
  six block generators × random vectors. This is the selection rule restated
  for the legitimate pairing (replacing the retracted linear-C reasoning).
- **(iii) THE FORCED-ZERO MAP:** ⟨v_m v₀, v₀⟩_J = 0 is FORCED by (i)+(ii)
  exactly when ε_m = +1 — so the even-block first-order silences
  (m ∈ {1,5,7,11}) are structural, while **the θ-odd zeros (m = 4, 8) are
  NOT forced and yet hold: genuine facts about the object.** Chat-2's parity
  lemma survives the D5 correction with its content sharpened. P3's
  structural-zero map: no comparison may count a forced zero as agreement.
- **(iv) THE J-PAIRED WELD VALUES equal the raw-dot values EXACTLY**
  (m=4: −536479695357 + 536483888640·w; m=8: 536481792003 − 536481792000·w —
  identical integers to B599-ALG's output, including scale). The
  "recompute the classical family under J" sub-item resolves as exact
  agreement; recorded observation: J restricts to the raw dot on the
  weight-pairs these contractions involve, in this basis (the solver-scale
  caveat noted — the agreement including scale is the empirical fact).

**Consequence for P3 (the owner's standing question):** with the universal
boundary ratio (step 3) and this lemma, the classical side's per-block
discriminating content is now provably concentrated in (a) the cross-domain
normalization (step 4) and (b) the non-forced θ-odd quadratic data — the
even-block channels are structurally silent at first order and the boundary
classes are block-independent. P3's verdict will ride on exactly those two
ingredients.

## STEP 6 COMPLETE (2026-07-15): the stage data is exact — the three E₆₂ amplitudes are symbolic identities

**The verdict.** The three E₆₂ pair-amplitude coefficients used by P3,
−(2/√7)·sin(2πj′/7)·ζ₁₄ᵏ for (j′,k) = (1,3), (3,−2), (2,−1), are now
SYMBOLIC IDENTITIES in ℚ(ζ₈₄) — cyclotomic-exact, not float. The chain's
step-6 requirement (exactify the B587/B589 stage data) is met.

**The method (v2, `step6_exact_stage_v2.py`).** Exact group-ring arithmetic
in ℤ[x]/(x⁸⁴−1): the Weyl-collected amplitude p and the normalizer N² are
assembled as exact cyclotomic elements; the squared identity
p² = target²·N² is proved by polynomial reduction mod Φ₈₄ over ℚ (remainder
identically zero, all three pairs); the remaining ± branch is fixed
numerically at full mpmath precision with a 1e-30 gate — achieved deviations
2.3e-41, 4.6e-41, 1.8e-41. Output: `step6_v2_output.txt`. Lock:
`tests/test_b598_step6.py` (OA_SLOW, subprocess, failure-enforcing).

**The honest first attempt (v1, preserved).** `step6_exact_stage.py` proved
the same Weyl collection but asked sympy's `simplify` to denest
√N² for a genuine cyclotomic real N² — it could not, and returned three
false NONZEROs (the printed residuals are exactly the denesting gap).
v1 is kept on disk as the failure record; the squared-identity route
exists because of it. Two float-precision iterations of v2's sign branch
(complex() casts flooring at 1e-16 against a 1e-25 gate; an mpf format
string) are visible in the git history of the script.

**What this does for P3.** Every stage-side number P3 will consume —
the amplitudes, their field (ℚ(ζ₅) golden / ℚ(ζ₁₄)-component E₆₂), the
sine-kernel coefficients — is now certified exact. Combined with step 5's
forced-zero map (which silences are structural) and step 3's universal
boundary ratio (all classical discriminating content lives in cross-domain
normalization), the remaining P3-bearing unknowns are exactly: the typed
P2 map + normalization (step 4), G1-FINITE (step 7), the sealed prereg
(step 8), and the independent P1 pipeline (step 9).

**Chain state: 1 provisional · 2 ✓ · 3 ✓ · 5 ✓ · 6 ✓ · 4/7/8/9 open.**

## STEP 4a COMPLETE (2026-07-15): the domain is typed — six lines, uniformly

**The verdict.** The P2 map's domain is typed (P2_MAP.md slot 1). At EVERY
one of the six blocks V_m, exactly and uniformly:
dim H¹(π_K; V_m) = 1 (re-certified); the peripheral T² module has
h⁰ = 1, h¹ = 2, h² = 1 with duality h⁰ = h² holding; [W_μ, W_λ] = 1; and
res: H¹(π_K; V_m) → H¹(T²; V_m) is INJECTIVE (the restriction class is
nonzero mod coboundaries) — the half-lives-half-dies face: each cusp line
is half of a 2-dimensional H¹(T²). The μ-leg alone detects the class at
every block. Script `step4a_domain.py` (failure-enforcing), output
`step4a_output.txt`, lock `tests/test_b598_step4a.py` (OA_SLOW).

**The frame consequence.** h⁰(T²; V_m) = 1 at every block: the bending
(Johnson–Millson) family at the weld torus has exactly ONE canonical
parameter per block — so the declared bending domain (P2_MAP.md) is six
lines with no choice beyond scale, and the banked B599-ALG twist family is
that domain's realization (4b gate (i) certifies its direction is the
peripherally-fixed vector). An honest vacuity note: the Euler identity
h¹ = h⁰ + h² is automatic by rank-nullity (MB12) and is reported, not
gated; the duality h⁰ = h² is a genuine check and holds.

## STEP 4b COMPLETE (2026-07-15): the bending responses — the hearing lines carry ONE number each, on conjugate phases

**The honest first pass.** The originally registered parity prediction
FAILED and is preserved permanently in the script header: it predicted
θ-odd t¹ silence AND θ-even t¹ noise; the even half was wrong — a careless
transfer from the P2-preflight TRACE functional. For the J-v0 functional
the step-5 forced-zero criterion FORCES the even zeros. Diagnosis recorded:
the functional matters.

**The verdict (all gates green, `step4b_responses.py`, output
`step4b_output.txt`, lock `tests/test_b598_step4b.py`).**
- Gate (i): all six bending directions v_m are peripherally fixed
  (certified longitude) — the bending lines of 4a are realized.
- Gate (ii): the degree-2 truncation reproduces B599-ALG's banked Lagrange
  witnesses EXACTLY (+2096640 at m=4/b2; −536481792000 at m=8/b2).
- Gate (iii, corrected): the t¹ J-responses vanish at ALL six blocks ×
  all 20 frozen words — FORCED at the even blocks, GENUINE at {4, 8}.
- **R1 = 0; rank R2 = 2; ker R2 = the four θ-even lines exactly.** The
  entire second-order classical content of the P2 map lives on the two
  θ-odd (hearing) lines. The deaf sector receives ZERO — the equivariance
  slot realized in the strongest form.
- **The column law:** every b2-containing word responds N_m·(1 ± √−3):
  m=4 rides (1+√−3) = 2ζ₆ with N₄ = 2096640 = 2⁹·3²·5·7·13; m=8 rides the
  CONJUGATE (1−√−3) with N₈ = 536481792000 = 2¹⁵·3⁵·5³·7²·11; the single
  mixed word a1b2A1B2 (one b2, one B2) carries the conjugated phase in
  both columns; words without letter-2-b content are silent. The two
  hearing lines are phase-conjugates — the chirality signature at the
  classical level. N₈/N₄ = 2⁶·3³·5²·7·11/13 (recorded as data; no reading
  assigned).
- Polarization quotient trivial (R1 = 0): the t² responses are
  well-defined outright.

**What P3 inherits.** The classical side of the comparison is now TWO
integers (N₄, N₈) + one universal word-pattern + the conjugate-phase
assignment; everything else is forced by structure (steps 3, 4a, 5). The
stage side is the exact hearing-law amplitudes (step 6). The comparison
itself remains SEALED behind steps 7–8–9.

## STEP 1 UPGRADED (2026-07-15): the peripheral certificate is exact

The provisional numerical certificate (least_squares; kept on disk) is
superseded by `peripheral_certificate_exact.py`: over ℚ(√−3) symbolically,
the relator FORCES c² − c + 1 = 0 (so c = (1±√−3)/2 = ζ₆ or ζ̄₆ — the same
ζ₆ that is the stage parameter of the 27-model's B = exp(ζ₆ f)); at both
branches the certified longitude "abABaaBAbA" commutes with the meridian,
is null-homologous, is group-equal to a(bABaaBAb)a⁻¹, has the banked cusp
shape −[[1, ±2√−3],[0,1]] with trace −2, and c is a UNIT (c·c̄ = 1): the
geometric rep lives over the ring of integers of ℚ(√−3). Output
`peripheral_certificate_exact_output.txt`; lock
`tests/test_b598_step1_exact.py` (ungated, ~1 s). Chain step 1:
provisional → EXACT.

## STEP 7 COMPLETE (2026-07-15): G1-FINITE — the dial map re-derived in-repo; the B582 hole closed

**The verdict (`step7_g1_finite.py`, output `step7_output.txt`, lock
`tests/test_b598_step7.py`).** The mirror-double amalgam at FINITE t = 1
(the banked weld frame; copy-2 log = Ad(exp(v_m))(ζ̄₆·f̄)), with committed
code and the certified longitude:
- Gate (i): all six dial slots v_m peripherally fixed (exact).
- Gate (ii), the SUBSET face: every generator of every dial lies in the
  exact K-span of the 78-dim e₆ basis — no closure can leave e₆.
- Gates (iii)+(iv), the RANK face (mod-p certificates at p = 10009, 10039,
  both ≡ 1 mod 3, agreeing everywhere):

    THE DIAL MAP:  no-twist → 3;  slot 1 → 3;  slots {5,7,11} → 52;
                   slots {4,8} → 78.

  rank mod p ≤ rank over the field ≤ 78, so 78 mod p certifies EQUALITY:
  **the θ-odd-twisted amalgam's algebra IS e₆(ℂ), dim 78, at finite t.**
  B582's existence chain (mirror-double with θ-odd dial ⇒ full E₆ ⇒
  complex, chiral 27) is now re-derived end-to-end in-repo. The
  provenance hole (the never-committed G1 code, caught in the item-6
  adjudication) is CLOSED.

**The refinement over the banked "3/52/78".** The dial is organized by the
fold: slot 1 gives 3, not 52 — its top vector IS the principal e (V₁ = the
sl₂ block itself), so it twists inside the wall; the three θ-EVEN slots
land exactly on f₄ = the θ-FIXED subalgebra (the deaf sector); only the
two θ-ODD slots breach the fold to full e₆. The same parity that carries
the hearing lines (step 4b), the genuine zeros (step 5), and the sign-flip
theorem organizes the dial map. Even bends stay under the fold; odd bends
open the whole stage.

**Chain state: 1 ✓ (exact) · 2 ✓ · 3 ✓ · 4 ✓ · 5 ✓ · 6 ✓ · 7 ✓ —
remaining: 8 (the sealed prereg) and 9 (the clean-room P1, computing).**
