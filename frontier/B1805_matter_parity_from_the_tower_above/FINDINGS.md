# B1805 — MATTER PARITY FROM THE TOWER ABOVE, TESTED (P-414; DATA-FREE): Spin(10)'s ORDER-2 CENTRAL ELEMENT IS EXACTLY MATTER PARITY AND SURVIVES EVERY FLAT BREAKING — BUT IN WITTEN'S G₂ FRAME IT DOES NOT REACH THE STANDARD MODEL, AND MOVING THE 3-CYCLE'S GROUP FROM SU(5) TO Spin(10) KILLS WITTEN'S DOUBLET–TRIPLET MECHANISM FOR THE FILLINGS' SYMMETRIES. THE FIRST TEST OF THE OWNER'S TOWERS QUESTION FAILS IN THIS FRAME

**Verdict: NEGATIVE** for "a tower above SU(5) supplies the matter parity B1803 lacked, in Witten's G₂ frame".
- **The group theory is PROVED** (exact, two routes: main's `verification/c1_spin10_checks.py` and the referee's explicit
  Clifford construction, all regenerating on main).
- **The physics hope fails in this frame:**
  - the parity dies at the U(1)_X breaking;
  - Witten's mechanism dies with real Higgs 10's.

Data-free; none of the 19. cc (main), 2026-10-29, P-414 (from the owner's towers question, P-415). Corrected before landing
at its hostile referee (§ 4): two blocking findings overturned the draft's "trade".

**0 of 19.**

## 1. The question

B1803: with SU(5) on Q and the fillings' ℤ/2 alone, Witten's first model needs a matter parity the fillings do not supply.
P-414 asks whether a tower above SU(5) (SO(10), a D₅ singularity along Q) supplies it.

## 2. The group theory (PROVED)

- **(a) The breaking pattern.** In SU(5), W = diag(1, 1, 1, −1, −1) has centraliser S(U(3) × U(2)), of dimension 12.
  - In Spin(10), W lifts to an order-2 element, diag(+1⁶, −1⁴) on the vector and eight +1 / eight −1 on the 16.
  - Its centraliser is exactly (SU(4) × SU(2) × SU(2))/ℤ₂, connected: Pati–Salam (the referee's 32 × 32 Clifford
    construction, r1). W and z₂W are conjugate, so the sign of the lift does not matter.
- **(b) The centre is matter parity, exactly.** Spin(10)'s order-2 central element z₂ is −1 on the 16 and +1 on the 10
  and the 45.
  - With Q_X = 2Σλ = 5(B − L) − 4Y, z₂ = exp(iπQ_X) = (−1)^{3(B−L)} on every MSSM field and on ν^c.
  - z₄ = exp(iπQ_X/2) is central, with z₄² = z₂.
- **(c) Matter parity is not in the Standard Model's gauge group, in any global form.** L and H_d carry identical gauge
  quantum numbers, but matter parity separates them. ν^c, a singlet with parity −1, says the same.
- **(d) z₂ survives every flat breaking.** It is central, so it lies in C(H) for every holonomy group H, abelian or not. It
  is an exact, anomaly-free discrete gauge symmetry, forbidding (10)(5̄)(5̄) ⊂ 16³ (Witten's (2.8)) and L·H_u (his
  (2.6)), but not (10)³(5̄) ⊂ 16⁴ (his (2.9)).
- **(e) No flat Spin(10) connection gives exactly the Standard Model.** The commutant of the Standard Model's algebra in
  so(10) is the abelian span of Y and Q_X. So C(H) ⊇ SM forces C(H) ⊇ U(1)_X and rank ≥ 5 (r4). This extends B952's rank
  obstruction to non-abelian holonomy.

## 3. Why the physics hope fails in this frame (NEGATIVE)

- **(i) The parity does not reach the Standard Model.**
  - U(1)_X must be broken, and by (e) only a VEV can do it.
  - Localised matter at enhancement points comes from the adjoint of the enhanced group restricted to so(10). Adjoint
    weights have norm² ≤ 2, while the 126's highest weight has norm² 5. So only 1, 10, 16, 16̄ and 45 occur (Acharya–Witten
    hep-th/0109152; checked on the so(12) and e₈ roots, r2).
  - The only localised field that can break U(1)_X is a 16 or 16̄, which is z₂-odd and leaves no residual parity.
  - A parity survives only as z₂·F′, with the breaking 16's F′-charge chosen opposite to the matter's: a geometric
    assignment of the very kind B1803 found missing.
  - The 126 route, "126-type keeps it", is correct group theory but not available here (B964's analogue: string
    constructions often supply only 27's).
- **(ii) Witten's mechanism fails in Spin(10) for the fillings' symmetries** (r3, on Witten's (2.1)–(2.9) at source).
  - The Higgs are now real 10's. For an F′ of exponent 2, every self-mass 10_H² is invariant, so every Higgs doublet is
    heavy.
  - With real 10's and a twist of order ≤ 2: under all of Witten's conditions, none of 31 groups tried (ℤ/2 to ℤ/24 and
    products) has a solution. Letting z₂ do (2.6) and (2.8), only ℤ/10 and ℤ/20 do, and the fillings have no symmetry of
    those orders.
  - With the top Yukawa and the Weinberg operator allowed and a twist of order ≤ 2, H_u's 10 self-mass is allowed in all
    440 cases.
  - With matter in whole 16's at trivial-lift points, σ = τ. Then (2.7) gives σ = π, then α = δ = 0, so the doublet mass is
    allowed, even with (2.6) and (2.8) dropped.
- **(iii) Pati–Salam is forced when F′ contains a strong inversion.**
  - The period P preserves every line. Its ℤ/6 line (6 ∣ p, p ≡ 2 mod 4) breaks Spin(10) directly to
    SU(3) × SU(2) × U(1)_Y × U(1)_X (dimension 13), with no Pati–Salam stage, and its cube splits the Higgs 10 (r4).
  - B1802 (f)'s premise holds in SU(5) but not in Spin(10), where Weyl sign changes invert several lines containing the
    Standard Model.
  - The corrected lemma: any lift inverting a line of order above 2 lies outside C(SM), so the resulting F′ never commutes
    with the Standard Model.
- **So the move up the tower is not a gain here.**
  - SU(5) on Q: Witten's mechanism works (B1802, B1803), but matter parity is missing.
  - Spin(10) on Q: matter parity exists above the U(1)_X scale, but Witten's mechanism dies for the fillings' symmetries,
    and the parity dies at the U(1)_X breaking unless F′ is assigned by hand.
  - The first worked test of the owner's towers question (P-415) fails in Witten's G₂ frame.
- **What it does not exclude:**
  - other frames (F-theory, where matter curves and monodromy give geometric parities; Hayashi–Kawano–Tsuchiya–Watari,
    arXiv:1004.3870, to read);
  - a non-VEV (Stückelberg-type) breaking of U(1)_X (unchecked);
  - an E₆ meeting point with a different localised content.
- **0 of 19.**

## 4. The referee (hostile, read-only; `audit/referee_b1805/`, scripts kept in `verification/referee/`)

**Verified:** (a)–(d), with the global form settled (r1) and the exactness of (b) and (c). Main's scripts reproduce
byte-identically, and r1–r4 regenerate identically on main.

**Two blocking findings, applied:**
- the parity does not survive to the Standard Model in this frame (§ 3 (i));
- Witten's mechanism fails in Spin(10) for the fillings' symmetries (§ 3 (ii)).

The draft's "one discrete input replaced by structure" and "the first worked case of one tower supplying what another
lacks" are withdrawn.

**Corrections applied:**
- "W splits each 16" holds only at W-lift points (at trivial-lift points the fatal constraint is σ = τ);
- "the split persists" holds for the charges, not the mechanism;
- the Pati–Salam price restated (forced only with a strong inversion; P's ℤ/6 line bypasses it);
- the literature: Martin, "Some Simple Criteria for Gauged R-parity", Phys. Rev. D 46 (1992) 2769, hep-ph/9207218; the
  Hayashi–Kawano–Tsuchiya–Watari paper on dimension-4 proton decay is arXiv:1004.3870 (2010), not 2009; added
  Tatar–Watari hep-th/0602238 and Acharya–Witten hep-th/0109152;
- the seen-first list;
- "exact" scoped to (b) and (c), since (a) used a floating-point rank, now confirmed by r1.

**Notes applied:**
- c1's real-rank method is valid here only by the image's structure (r5);
- the NOTES' ℤ/4 idea is a gauge redefinition (r3: 0 solutions);
- "non-abelian holonomy that kills U(1)_X" would also break the Standard Model (r4).

## Seen first

`VERDICT topic-sweep` (2026-10-28/29, `--full` with the seat lanes):
- Pati–Salam: 17 arcs;
- matter parity and R-parity: 12 arcs;
- Spin(10) and SO(10) Wilson lines, centre, D₅: 39 arcs.

None states the centre as matter parity.

**Bearing on it:**
- B952 (the rank obstruction);
- B962 and B964 (the VEV is an input; "only 27's");
- B992 (the E₆ analogue of the commutant);
- B1221;
- B1802, B1803;
- docs/GUT_REQUIREMENTS_LEDGER.md;
- docs/THE_TOWERS.md;
- P-414, P-415, P-416.

**Literature** (metadata and abstracts checked by the referee):
- Martin (1992);
- Pati–Salam (1974);
- Witten hep-ph/0201018;
- Acharya–Witten hep-th/0109152;
- Tatar–Watari hep-th/0602238;
- Hayashi–Kawano–Tsuchiya–Watari arXiv:1004.3870.

## Files

- `verification/c1_spin10_checks.py` → `c1_run.txt`.
- `verification/referee/`: `r1_spin10_clifford.py`, `r2_matter_parity_and_vevs.py`, `r3_witten_conditions_spin10.py`,
  `r4_lines_and_rank_spin10.py` and `r5_c1_hstack_note.py`, with their runs.

The lock: `tests/test_b1805_matter_parity_from_the_tower_above.py`.
