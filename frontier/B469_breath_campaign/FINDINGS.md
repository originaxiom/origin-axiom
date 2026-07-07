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

## Reproduce
```
python3 br1_br2.py     # BR1 + BR2 symbolic; ALL CHECKS PASS
# BR2 SnapPy gate: NonorientableCuspedCensus[0].orientation_cover() ≅ 4_1 (session log)
pytest ../../tests/test_b469.py
```
