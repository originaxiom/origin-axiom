# THE L85 CAMPAIGN — the D1 existence construction (the program's decisive gap)

**Opened 2026-07-14 (owner directive: "do L85 properly; precompute everything").
Prereg tier: campaign. Firewall: nothing SM-facing runs anywhere in this
campaign; outcome A/B only OPENS the (separately preregistered, still gated)
downstream. Provenance: all verification herein is internal (owner + AI
seats); see the Review-18 pre-committed scope.**

## The question (from chat-1's D1 prereg, adopted with B597's corrections)

Does a choice-free, width-respecting semiclassical map exist from the golden
stage's θ-odd plane to the character variety's dial {u₄, u₈}? B597 already
excluded the free-rotation outcome conditional on existence; this campaign
decides existence (A/B vs D).

## The constraint sheet (everything a candidate map must satisfy — all banked)

1. Trace/determinant compatibility: det(I − B_odd) = φ² = λ(A₁) at κ = 5
   (B595's bridge).
2. The order-level failure: the clock is NOT the cat-map period; the map must
   not force order-matching (B596).
3. The dimension caveat: well-posed as an iso only at golden (2 ↔ 2); at E₆₂
   (3 vs 2) the construction must produce the rank/quotient, not assume it
   (B595-D1, B597).
4. Width-respect: the τ-labels are non-degenerate on both parities (B597) —
   a valid map is then unique up to per-line scale.
5. The hearing coefficients are state-independent (B594) — the map is a
   property of structure, not of the 4₁ state.

## The cells

- **P0 (this arc): the C1 baseline, computed.** The SL(2) semiclassical
  dictionary datum in-sandbox: the Kashaev invariant ⟨4₁⟩_N asymptotics —
  extract the 1-loop constant and identify its τ₁ = −3 content (upgrades
  B425's identification from [CITED] to [COMPUTED]). Gate: the geometric
  growth rate must come out at Vol(4₁)/2π. Also: the machinery inventory
  (below).
- **P1: the cusp table.** The six H¹ representatives of B575 restricted to
  the peripheral subgroup: ξ_m(meridian) per block (Fox solve over the exact
  model), the meridian's nilpotent Jordan data per block (banked type), and
  the longitude word pinned to the banked B67 convention. This is the
  classical side of the map's domain, made explicit.
- **P2: the quantization arrow.** The boundary H¹(T²; block) data mapped
  through the finite Weil model (B587's machinery) at κ = 5; the candidate
  map assembled; the constraint sheet checked item by item.
- **P3: the verdict cells.** C1 (P0) ✓; C2 (θ-even, four lines — the same
  construction must force there too); C3 (level-independence: κ = 5 vs one
  higher golden multiple). Outcomes A/B/D exactly as locked in the adopted
  D1 prereg (B597).

## Machinery inventory (what exists, what must be built)

- EXISTS: the exact e₆/blocks model + letter actions (B575, OA_SLOW ~6 min);
  Fox machinery patterns (B581's script); the Weil model at any κ (B587);
  the stage odd-plane data (B584/585); the torsions (B581).
- TO BUILD (P1): the per-block H¹ Fox solver against the B575 module
  (cocycle condition via Fox derivatives of REL, mod coboundaries); the
  longitude word in the banked presentation.
- TO BUILD (P2): the weight/filtration decomposition of the boundary
  restriction under the (unipotent) meridian — the Jordan filtration data —
  and its pairing with the theta-basis of ℂ[P/5Q].

## Discipline

Each cell preregisters its own falsifiers before running; every number
banked blind before comparison; the campaign's outcome statement uses only
the A/B/D table. All verification internal (see provenance note above).


## THE READINESS CHAIN (seat-4 audit, adopted 2026-07-15 — GATING)

No target comparison, verdict, or banking of P3 until this chain is green,
in order:

1. peripheral certificate ✓ (banked: `peripheral_certificate.py`)
2. corrected all-six P1 ✓ (the six-block word-independence verification
   banked: `verify_word_independence.py`, ξ(canonical) = ξ(used) at all six)
3. gauge-invariant boundary classes ✓ (banked: `steps3and5.py` — the
   universal boundary ratio I_λ/I_μ = −2√−3 at ALL six blocks; the classical
   per-block information lives only in cross-domain normalization)
4. the explicit P2 map (domain, codomain, formula, equivariance, rank,
   kernel, polarization, normalization — Gates A/B alone are insufficient;
   the banked P2 is gates + data + a structural verdict, NOT the map)
5. the exact 27–27̄ intertwiner J ✓ (banked: `steps3and5.py` +
   `lemma_cell.py` — J symmetric, Schur-unique, invertible; NO untwisted
   form (dim 0); the move-across lemma; the forced-zero criterion splitting
   structural from genuine zeros; J-weld = raw-dot exactly)
6. exact stage data ✓ (banked: `step6_exact_stage_v2.py` — the three E₆₂
   pair amplitudes −(2/√7)sin(2πj′/7)ζ₁₄ᵏ are SYMBOLIC IDENTITIES in
   ℚ(ζ₈₄): squared identity exact mod Φ₈₄, sign branch at 1e-30, dev
   ~1e-41; v1's simplify-failure preserved as the honest first attempt)
7. the G1 recomputation in-repo (the dial-map closure with committed code
   and the certified longitude — closes the B582 finite-t provenance hole;
   until then all mirror-double existence claims are formal/jet-level)
8. sealed P3 preregistration (written and hashed BEFORE any outcome-bearing
   comparison; the failed meridian prediction recorded permanently ✓ done
   in P2's FINDINGS)
9. independent reproduction (the corrected P1 table reproduced by a second
   pipeline that does not import expected values)

Additional adopted labels: B598-P0 is relabeled a CALIBRATION against the
externally known asymptotics (the extraction is self-consistent, not
independent — the growth-rate gate uses the measured prefactor);
B583-X2R's arbitrary-weight demonstration cannot be inherited by P3's
channel combination (direct-sum torsion is multiplicative); B593/B594's
identities serve as controls only until re-proved for the J-pairing;
B597's line-distinctness does not fix relative scales (P2's normalization
must). Quarantined (outside the cone, queued pre-synthesis): the
B517→B530→B531→B532 chain findings, P43/P46/P51 (the 07-11/07-12 audit
reports at <oaudit-seat>/oaudit2/), and B591's terminology fix
("graph manifold" → mixed/Haken with two hyperbolic JSJ pieces).
