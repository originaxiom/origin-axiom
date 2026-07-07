# B469 — the Breath Campaign, first wave: BR1 + BR2 + BR4 banked; BR3 queued

**Status: first wave banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md`
(committed before computation). The campaign object: the RESIDUE (the orientation
character — the one ℤ/2 that survived every register: B466/B467/B468, banked B289/B356)
and THE BREATH (its oscillations). Names live in the S-room; this file is arithmetic.**

## BR1 — the two-register breath law: VERIFIED at four levels (exact)

At N ∈ {15, 45, 75, 225}: the quantum residue det(Par@N) AND the classical residue
sign(σ on (ℤ/N)²) both equal **(−1)^((N−1)/2)** — the two registers breathe TOGETHER,
and the breath is the level's class mod 4 (15 → −1, 45 → +1, 75 → −1, 225 → +1).
Adjudication: derivable (the negation permutation has (N−1)/2 transpositions; the
classical sign is the Jacobi character (det|N) = (−1|N)) — LAUNDERS as classical
arithmetic, banked as the exact exhibit. The seam level 15 sits in the odd-signed class;
the first tower level above it (45) exhales to +1.

## BR2 — the family Gieseking theorem: every metallic bundle double-covers a non-orientable bundle

**X_m = [[m,1],[1,0]] satisfies X_m² = A_m = [[m²+1, m],[m,1]] and det X_m = −1, for ALL
m symbolically.** So every metallic once-punctured-torus bundle (monodromy A_m) is the
orientation double cover of the non-orientable bundle with half-monodromy X_m — the
residue's geometric carrier exists FAMILY-UNIFORMLY, not just at m=1.
**SnapPy gate (m=1): PASS** — the smallest non-orientable cusped census manifold m000
(the Gieseking manifold, vol 1.0149416) has orientation cover isometric to the
figure-eight (volume ratio exactly 2). Lit-gate: Gieseking-type quotients of
punctured-torus bundles are standard-shaped (cited, not claimed as new); the
FAMILY-UNIFORM statement's novelty status is NEEDS-LIT. Consequence for B466: the
σ_m-action (the deck action of these quotients) exists at every m — BR3's subject.

## BR4 — the breath at the wall: the exact classification of the census collisions

From the banked B467 census (certified isometries + CS):

| collision | orientation behavior |
|---|---|
| 4₁(−5,1) = 5₂(5,1); 4₁(1,2) = 5₂(−1,1) = 6₁(1,1) | **preserving** (CS equal) |
| 4₁(5,1) ~ 5₂(5,1); 4₁(−1,2) ~ {5₂(−1,1), 6₁(1,1)}; 5₂(−1,2) ~ 6₁(−1,2) | **reversing** (CS signs flip) |

The law-shaped exhibit (derivable from amphichirality): **whenever the amphichiral parent
(4₁) is involved, every unoriented collision appears in BOTH oriented forms** (its mirror
slopes supply the partner: CS(4₁(p,1)) = −CS(4₁(−p,1)) — the banked B289 sign law,
re-verified across the window); between two chiral parents (5₂, 6₁) a collision may exist
in only one orientation class (5₂(−1,2) = mirror of 6₁(−1,2) with no preserving partner
in-window). The child is chiral at every hyperbolic slope in the window (CS ≠ 0
throughout) — the wall breaks the parent's orientation symmetry, and the residue reappears
as the ± pair of mirror children.

## BR3 — the breath fields (queued, the campaign's compute cell)

The σ_m-orbit structure on Fix(σ_m²) per family member (B466's computation at every m):
the period-2 orbit of each geometric structure and its field (golden: ℚ(√−3), banked).
Requires the metallic trace-map family (B48/B154 machinery); queued as the next wave.

## Phase 2 — the σ-parity classification (Chat-2's seat; files committed verbatim + CC bank)

Chat-2 independently launched the same campaign as "proposed B469" — merged here as
**Phase 2** (`PREREG_SIGMA_PARITY.md` + `PHASE2A_RESULTS.md`, committed with the
falsifier-fired audit trail intact, which is the point). CC's bank:

- **The σ-lift VERIFIED EXACT** (upgraded from their 1e-15): conj(W(m,1)) =
  Par·WR₁₄^m·Par·D(m,14) at p = 61, 421 for m = 1, 2 (`sigma_lift_check.py`; conj = the
  ring hom z → z¹⁴, licensed — the construction is polynomial in z over ℚ). σ's operator
  realization is the c ↦ −c ≡ 14 twist, Par-dressed on the Fourier part: **a twisted
  two-world correspondence (c=1 ↔ c=14), not an internal mirror.**
- **The +j obstruction is symbolically exact**: T₋ⱼ − Tⱼ = c·m·j — the quadratic form's
  non-centeredness is what prevents similarity; verified also spectrally (conj(M₁) and
  M₁₄ have angle gap 1.26 — not similar).
- **P1b restated and endorsed** (one-line arithmetic): −1 is a QR mod 5 and ≡ 2 mod 3 —
  so σ preserves the Legendre-5 classes and exchanges the mod-3 classes: **the √5 axis is
  σ-even, the √−3 class-pairing is σ-odd** — the B465-addendum two-axis complementarity
  now carries its parity reading.
- **Their Phase-2a records the FOURTH naming collision of the arc** (B466's character-
  variety components vs the Weil operators — same letter, different objects), caught by
  their own prereg falsifier. The shuttle rule ("name the operator") is now
  load-bearing in all three seats.

## P2b — the derivation of the pair's emptiness (CC's assignment, delivered)

With banked anchors only: (i) V₁/V₂ are real-form (PU(2,1)/spherical-CR) components
(B444's Falbel anchor; B458's launder) ⇒ each component is **conjugation-stable as a
set**; complex conjugation is orientation-reversing, and Vol is odd under it ⇒
**Vol(Vᵢ) = 0 derived exactly**; CS is odd mod 1 ⇒ **CS(Vᵢ) ∈ {0, ½} derived** — the
parity mechanism forces the emptiness up to the intrinsic mod-½ ambiguity of parity
arguments, and the banked B458 computation selects 0. (ii) The σ̂ deck exchange
(B466: V₁ ↔ V₂) adds the consistency relation CS(V₁) = −CS(V₂). So the year's
"beautiful, symmetric, empty" verdict at this floor now has a MECHANISM: the emptiness
is a σ-parity selection rule (odd invariants on conjugation-stable components must
vanish mod ½). Bin: derivation from banked facts — the load-bearing input is the
real-form conjugation-stability (banked-anchored, Falbel); no new computation claimed.

## BR-N — the norm identity (the owner's sentence, verified as three exact statements)

*"The smallest residue that can't cancel is the norm of the scale, frozen at −1 across
the entire family, living on the golden axis alone."* All three clauses are exact
(`br_n_norm.py`):

1. **The residue IS the norm of the scale**: X_m = [[m,1],[1,0]] is the COMPANION MATRIX
   of the metallic mean's minimal polynomial x² − mx − 1, so det(X_m) = N(λ_m) = −1 —
   BR2's orientation bit and the field norm of the scaling unit are literally the same −1.
2. **Frozen across the family**: symbolically for all m; and it survives the same-field
   degeneracy — the ℚ(√5) members m = 1, 4, 11, 29 are exactly φ^{1,3,5,7} (the ODD
   powers; the banked L16 Pell sub-lead), so N = (−1)^odd = −1 even where λ_m is a proper
   power. The orientable cover A_m = X_m² has det = N(λ_m²) = +1: **norm −1 lives on the
   half — the Gieseking floor — and the cover pays for orientability with norm +1.**
3. **On the golden (real/scale) axis alone**: imaginary quadratic norm forms are positive
   definite — a unit of norm −1 is IMPOSSIBLE there. The geometry end of the two-ended
   object (√−3, √−7, √−15) structurally cannot carry the residue's norm-realization; only
   the scale end can. (Coheres with P1b: the real axis is the σ-even one.)

Adjudication: classical algebra throughout — LAUNDERS, banked as the exact exhibit. The
identity closes a loop across three registers: **norm −1 of the scale ⟺ det −1 of the
half-monodromy ⟺ the non-orientable quotient exists** — arithmetic, linear algebra, and
topology giving the same bit.

## Reproduce
```
python3 br1_br2.py            # BR1 + BR2 symbolic; ALL CHECKS PASS
python3 sigma_lift_check.py   # Phase 2: the lift exact at two primes + the +j obstruction
python3 br_n_norm.py          # BR-N: the norm identity, three exact statements
# BR2 SnapPy gate: NonorientableCuspedCensus[0].orientation_cover() ≅ 4_1 (session log)
pytest ../../tests/test_b469.py
```
