# R26 — B1080 residuals (six-realization uniformity, row-4 Γ = ℤ/5) + B1011 C5/C6 counts (992 / 284)

**Verdict (A) B1080 residuals: MATCH** (all numbers reproduced by two independent routes; one
vacuity-flavour note on what "uniformity across realizations" can test).
**Verdict (B) B1011 C5/C6: MATCH** on 992 / 284 and on the C6 15-value set, **with a VACUITY note
on the banked lock** (the committed check is an arithmetic tautology with hard-coded 8/2/2) and one
semantics note on C6.
**Overall: MATCH** (worst of the two is MATCH; the vacuity is in the lock layer, not in the numbers,
and this cell now supplies the falsifiable enumeration the arc lacked).

## Blind discipline — file log

**Read BEFORE writing any code** (claim statements / definitions only):
- `frontier/B1080_global_form/FINDINGS.md` (32 lines, whole file — it contains no definitions),
  `ADDENDUM_2026-09-01.md`
- `recompute/R05_z6_kernel/FINDINGS.md` (prior cell; to learn what it left unrecomputed)
- `frontier/B1079_wilson_menu/FINDINGS.md` lines 1–40 and `B1210 …/FINDINGS.md` lines 40–60 (to learn
  what "row 1 / row 4 / cascade terminus" are: Wilson-menu centralizer types)
- `b1080_results.json`: **grep for the word "realization" only** — needed because the FINDINGS never
  define the six realizations. Extracted definition: A2+A1 Levis of E6 (Bourbaki), su(3) on nodes
  {1,3} or {2,4}, su(2) on a non-adjacent node; row 1 = A2+2A1 on the five B1079 node subsets;
  row 4 = the four A4 chains. Nothing else of the JSON was read pre-blind.
- `frontier/B1011_mckay_tensor/FINDINGS.md` lines 1–70 and the `forced` lines of
  `PREREGISTRATION.md` (the definition of "forced": θ-odd ⟺ A ∈ ker χ or B ∈ Z(2I); θ-even ⟺
  A ∈ Z(2T) or B ∈ Z(2I)); `recompute/R1_REPORT.md` R02 table (R02 did not touch 992/284).

**Read only AFTER `blind_A_output.txt` / `blind_B_output.txt` were on disk:**
- `b1080_results.json` in full (both agents), `frontier/B1011_mckay_tensor/b1011_match.py`
  lines 125–170, `tests/test_b1011_mckay_tensor.py` lines 56–82.
- Not opened at all: any B1080 scratchpad script (none is committed), `b1011_cells.py`,
  `b1011_exact.py`.

## (A) B1080 — my instrument (`blind_levi_kernel.py`, exact `Fraction`/integer arithmetic)

Γ for a Levi L ⊂ E6 (simply connected) is Z(S) ∩ Z(L)⁰ inside the common maximal torus — by
faithfulness of the 27 this equals the arc's "elements of Z(S) × U(1)^k acting trivially on the
27" with **all** centre u(1)'s allowed. Two independent routes, asserted equal on every subset:

- **Route 1 (root datum, SNF):** Γ ≅ dual of P_L/K, K = P ∩ span_ℝ(Φ_L) (saturation of the Levi
  root lattice in the E6 weight lattice); invariant factors = Smith normal form of K's basis
  restricted to the L coordinates; |Γ| = |Z(S)|/[K:Q_L].
- **Route 2 (the 27's weights, SNF congruence solve):** 27 = Weyl orbit of ω₁ (built by simple
  reflections, 27 weights, root-basis denominators 3 as required); for each z ∈ Z(S) the
  existence of a compensating s ∈ Z(L)⁰ is the solvability of C·t ≡ b (mod ℤ²⁷), decided
  exactly via the integer left kernel of C (own SNF with unimodular transforms). Kernel
  collected, closure-checked, element orders taken.

Exhaustive sweep over **all 63 node subsets** (every Levi), so the arc's six / five / four
realizations are strict subsets of what was run.

### Diff (mine vs banked)

| item | mine (blind) | banked (B1080, post-verifier) | verdict |
|---|---|---|---|
| cascade terminus A2+A1: number of node subsets | 10 | verifier: 10 ("original tested 6") | MATCH |
| Γ on each of the 10 | 6, cyclic, invariants [6], orders {1,2,3,3,6,6} | ℤ/6 on all 6 (orig.) / all 10 (verifier) | MATCH |
| row 1 A2+2A1: number of subsets | 5 = {1235,1236,1246,1256,2356} | 5, same subsets | MATCH |
| row 1 full-centre Γ | 12, invariants [2,6] = ℤ/6×ℤ/2, not cyclic, orders {1:1,2:3,3:2,6:6} | ℤ/6×ℤ/2, same order census | MATCH |
| row 1 core (drop either su(2)) | = entries (1,2,3),(1,3,5) of the A2+A1 sweep → 6 | 6 both ways | MATCH |
| row 4 A4: number of subsets | 4 = {1234,1345,2456,3456} | four su(5)-embeddings | MATCH |
| row 4 own level Γ | **5**, cyclic, **invariant factor [5]**, [K:Q_L] = 1 on all four | ℤ/5, "elementary divisor exactly 5", uniform over all four (verifier-corrected from 1) | MATCH |
| "the 78 changes nothing" | automatic: Γ ⊂ T is the identity in E6 (faithful 27) so acts trivially on every rep | unchanged in all tests | MATCH (vacuous by construction) |

**Planted controls (the instrument can say "no"):** Levis where Γ ≠ Z(S): A5 (nodes 13456):
|Z(S)| = 6, Γ = ℤ/2 (agrees with the hand branching 27 = 15₀ + 6̄₊₁ + 6̄₋₁); A2+A2 (1356):
9 → 3; A1+A2+A2 (12356): 18 → 6; E6 itself: 3 → 1. So "Γ = full centre" is a genuine
two-outcome property and the ℤ/6 / ℤ/5 / ℤ/6×ℤ/2 results are not tautologies of the method.

### Notes

1. **Convention (E23):** the arc's six realizations, as quoted ("su(3) on {1,3} or {2,4} crossed
   with su(2) on 2, 5, 6, 1"), name only five valid A2+A1 subsets ({2,4}+5 is A3, not A2+A1);
   the sixth is not identifiable from the text. Immaterial: all ten valid subsets give ℤ/6.
2. **Vacuity flavour on "uniformity across Weyl realizations":** Γ = Z(S) ∩ Z(L)⁰ is a
   conjugacy invariant of the Levi, and Levi subalgebras of a given type in E6 form a single
   Weyl orbit (my sweep is consistent: Γ is constant on every type). The sweep therefore tests
   the *instrument's* basis-independence (which the arc itself needed — its first pass found
   orders 1, 2, 4 from a labeling bug), not an E6 fact that could have come out otherwise. The
   headline "ℤ/6 at every landing" is nonetheless real content: it is the saturation statement
   K = Q_L for those Levis, which fails for A5, A2+A2, E6 (controls above).
3. "Using only 1 of its 3 u(1)'s": any cyclic torsion subgroup of a torus lies in some circle
   subgroup, so this is automatic once Γ is cyclic; I did not reproduce the arc's specific
   basis statement (u1_2 = u1_3 = 0), which is basis-dependent.

## (B) B1011 C5/C6 — my instrument (`blind_forced_counts.py`)

Explicit 2T (24 Hurwitz units) and 2I (120 icosians, built from the ½(0,±1,±φ⁻¹,±φ) even-
permutation recipe, closure and unit-norm asserted) as quaternions over ℚ(√5) (pairs of
`Fraction`s); V₂ = the SU(2) matrix of left multiplication (rep property spot-checked); χ = the
ℤ₃ character assigned by Q₈-coset and **verified multiplicative on all 576 pairs**; ω handled in
an exact tower ℚ(√5)(√3, i). For **every one of the 2880 cells** I form the actual representing
matrix (M_odd = χ(A)V₂(B), 2×2; M_even = V₂(A)⊗V₂(B), 4×4) and call the cell forced iff its
Hermitian part is a scalar matrix — i.e. the real quadratic form Re⟨u,Mu⟩ is listener-
independent. This criterion never mentions ker χ or the centres.

### Diff

| item | mine (blind) | banked | verdict |
|---|---|---|---|
| \|ker χ\|, \|Z(2T)\|, \|Z(2I)\| | 8, 2, 2 (computed) | 8, 2, 2 | MATCH |
| θ-odd forced cells | **992** by the Hermitian-scalar criterion; 992 by the arc's definition; the two agree **cell-by-cell** (asserted both directions) | 992 | MATCH |
| θ-even forced cells | **284**, same cell-by-cell agreement | 284 | MATCH |
| forced values | odd: Re χ(A)·½tr B, even: ½tr A·½tr B — asserted equal to the scalar on every forced cell | same formulas | MATCH |
| C6 mirror value set | {0, ±1/4, ±1/(4φ), ±1/2, ±1/(2φ), ±φ/4, ±φ/2, ±1} (15 values) **over all 2880 cells** | same 15 values | MATCH |
| control | "tr M_odd real" criterion gives 1440 ≠ 992 — the enumeration distinguishes criteria | — | bite live |

### Notes

1. **VACUITY (lock layer).** Post-blind reading: `b1011_match.py` lines 137–142 set
   `kerchi, ZI, ZT = 8, 2, 2` **by hand** (the comment says "from the model's subgroup data", but
   the numbers are literals) and assert `8*120+24*2-8*2 == 992`; `tests/test_b1011_mckay_tensor.py`
   lines 58–59 assert the same integer identities. As committed, the 992/284 check **could not have
   failed**: nothing enumerates cells or evaluates a forcing criterion. The FINDINGS' "matching the
   incoming enumeration" refers to an uncommitted external run. The inputs 8/2/2 are separately
   verified in the repo (R02 confirmed χ with kernel Q₈, the centres), so the *numbers* are right;
   this cell now supplies the falsifiable version (independent criterion, cell-by-cell).
2. **Semantics of C6.** The 15-value mirror set is the value set of ½tr A·½tr B over **all**
   cells (the arc's code loops over all 63 classes). Restricted to the 284 *forced* cells the set
   has only 9 members — the quarter values ±1/4, ±1/(4φ), ±φ/4 occur only when **both** A and B
   are non-central, i.e. exactly where the listener-independent (forced) reading does not apply.
   The FINDINGS' wording ("the Re(ω) = −½ classes' contribution") is consistent with the all-cells
   reading; the preregistration's "θ-even forced … value ½tr A·½tr B" is not what the quarter
   family is drawn from. Not a numerical discrepancy; a scope clause the mirror-law statement
   should carry.
3. Gate 5: nothing measured enters either sub-claim.

## Artifacts (this cell)
- `blind_levi_kernel.py`, `blind_A_output.txt` — E6 Levi kernel instrument (two routes) + exhaustive sweep + controls
- `blind_forced_counts.py`, `blind_B_output.txt` — 2T×2I cell enumeration with the Hermitian-scalar criterion
