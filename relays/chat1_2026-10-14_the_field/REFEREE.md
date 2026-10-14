# The referee's report on the first version (86df2722), and what changed

An independent agent refereed the first version without seeing the reasoning behind it. It re-ran the three scripts,
which reproduced exactly, read every citation, re-derived the mathematics, and grepped the absence claims. Its scratch
scripts (`ref1.py`, `ref2.py`, `ref3.py`) were run off the repository and are not committed.

| # | finding | severity | disposition |
|---|---|---|---|
| 3 | "keeps the cusp ⇒ a·a = 0" fails when the flat side carries a parabolic weight: at c = 0, b ≠ 0, κ = −2 still holds with a·a = −b² | ERROR | Fixed. "Unfiltered flat side" is now in H-RES, O3, O4, the title and the philosophy note, and O3 states the failing case |
| 4 | O6 is not unpredicted. B1642 R1 and R2 give Φ_R = −2F Fᵀ ε dz, the zero mode's own square, nilpotent because Fᵀ ε F = 0 | ERROR (framing) | Fixed. O6 is credited to B1642, and the uniqueness is marked as the new part. B4 is answered |
| 5 | B5: m₁ = 0 needs only R·R = 0; Σ R_r² e_r = 0 plays no role | ERROR | Fixed (B5, and O6's last bullet) |
| 6 | B1: the heavy mass lies between \|R\|\|a\| and 2\|R\|\|a\|, so it does not measure the separation | ERROR | Fixed (B1, O7, C5b) |
| 7 | C7 is a restatement of a closed form, not a test, and it skips the nilpotent case | OVERSTATEMENT | Fixed (C7 row) |
| 8 | "a·a = (ℓ/8π)²" depends on the normalisation; "closed geodesic" holds only for Fuchsian holonomy | OVERSTATEMENT | Fixed (O5: complex length) |
| 9 | O4's "answer to P-115": P-115 is DONE (B1646), and a Higgs on the cone gives m₂ = 0; κ = −2 is the cusp premise, not PF1 | OVERSTATEMENT | Fixed (O4; §3, "the cusp condition is a premise") |
| 10 | O5's "reading of P-113": FK10's unit sits at the modular cusp, not the puncture; B2's "both quarter-turns" is wrong | OVERSTATEMENT | Fixed (O5, §4.4, B2) |
| 11 | O7's "every null direction": the six coordinate-plane lines are reached only at cusps; the X(4) reading upgraded (Γ(4) invariance, degree one) | MINOR | Fixed (O7) |
| 12 | e_r used for both the units and ℘'s half-period values; the pairing is forced by B1642 R2 | MINOR | Fixed (notation line; C10 row) |
| 13 | O4 needs a·R ≠ 0; C8 has a closed form C = (1 + \|R̂†â₀\|)⁻² ∈ [¼, 1]; O8's normalisation; B150 has no Seiberg–Witten curve | MINOR | Fixed |
| 14 | §4.2's uniformising test lives on L ⊕ L(−p), outside O1's space | MINOR | Fixed |
| 16 | S037 says *the object* is more primitive, with Φ on the "filling" side | WRONG citation | Fixed (§0; philosophy note) |
| 17 | candidate (c) is "end data at both ends"; W64's cone comes from K6, its eigenline Higgs from K4; W64's "both" means ±3 and the direction | MINOR | Fixed (§0) |
| 19 | absence claim wrong: W65 H3 and W67 have τ ↦ [R(τ)] on X(4) | WRONG absence | Fixed. O7 is now "confirms W65 H3 and W67" |
| 20 | θ_s/θ₁ is on record as the fermion bilinear (B1642 R2, T-RESIDUE-ANTISYMMETRIC, P-088, the audit lane's residue audit) | omission | Fixed (§0) |
| 21 | the record's caution "a local nilpotent Higgs field does not certify a globally non-semisimple monodromy" (R35, sm:B1502) | omission | Fixed. Cited, and answered by O3's global half |
| 22 | the philosophy note asserts H-RES and readings as facts | OVERSTATEMENT | Fixed (conditional wording throughout) |
| 23 | "exactly one point" (the trivial character (2,2,2) is also fixed, at κ = 2, and PF1 removes it); "the seed sits at the node" contradicts step 3 | MINOR | Fixed. Step 1 now names both fixed points, and the seed sentence is removed |
| 25 | a tension: the record's real Higgs directions (W60, W63) would, under H-RES, open the puncture far from the cusp | MINOR | Stated (O4) |
| 2, 1, 15, 21, 24 | the numbers reproduce (C10's control range corrected to 0.29–1.47); the citations check out; no contradiction with B1645, B1646, B1649 or W64–W65 | OK | — |

## Second pass (the same referee, on the revised pages)

It found the fixes in place (3, 5–8, 10–14, 16, 17, 19–22, 23), the new O3 global argument correct, and the note's
step 2 correct. It also found these, all now fixed:

| # | finding | disposition |
|---|---|---|
| 2 | O6: B1642's constant is unit-dependent, c = (−1, −1, i), and the equality with R_r f̂_r is exact | fixed |
| 3 | O3: the eigenvalues are −1, −1 only for a nilpotent residue; the global half rests on Simpson's bijection (cited from memory) | fixed |
| 4 | O4's tension: for a real direction a·a = \|a\|², so κ = −2 cosh(4π\|a\|) depends on the external scale; with phase i the cusp holds only with a weight | fixed. The conclusion stands: an exact, unfiltered cusp excludes real directions |
| 5 | GM4 lists the puncture itself as CONDITIONAL, not its parabolicity | fixed (both pages) |
| 6 | the moves jointly fix exactly two points, but each move alone fixes two lines | fixed ("exactly two points are fixed by every move"; checked with sympy) |
| 7 | the common point's puncture is central, so "the only unitary point at the cusp" should read "on κ = −2"; no unitary point has a parabolic puncture | fixed (both pages) |
| 8 | B4: candidate (d) is a bilinear of τ-sections on the weave's surface, not Φ_R at fixed τ | fixed |
| 9 | the note's "the departure between them is Φ" needs a chosen τ and no weight; "residue", not "value"; "up to scale" | fixed |
| 10 | B2: W64's cone comes from K6 in the fibre frame; only K4's eigenline route sits at the modular cusp | fixed |
| 1 | O7's degree-one claim has a full proof (Γ̄(2) free of rank 2; Γ̄(4) the kernel of its largest elementary abelian 2-quotient) | added, credited |
