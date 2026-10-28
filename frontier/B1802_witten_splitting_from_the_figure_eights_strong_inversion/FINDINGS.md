# B1802 — WITTEN'S DOUBLET–TRIPLET TOPOLOGY ON THE FIGURE-EIGHT'S EVEN FILLINGS (P-408; DATA-FREE): EACH OF m004(p/q)'S THREE INVOLUTIONS (TWO STRONG INVERSIONS, ONE PERIOD) HAS EXACTLY TWO FIXED CIRCLES WHEN p IS EVEN; EITHER STRONG INVERSION PRESERVES THE UNIQUE ORDER-2 WILSON LINE W = diag(1, 1, 1, −1, −1) AND NECESSARILY LIFTS TRIVIALLY ON ONE CIRCLE AND BY W ON THE OTHER. THAT IS WITTEN'S TOPOLOGICAL STRUCTURE AT n = 2, WHERE HIS FIRST MODEL "WOULD NOT QUITE WORK" WITH ℤ/2 ALONE — THE FULL SYMMETRY GROUP ℤ/2 × ℤ/2 ADMITS SOLUTIONS (OPEN, P-409)

**Verdict: PROVED** for the topology: a short proof from standard theorems, checked by explicit branch links and computed
lifts. The physics is open: Witten's model at n = 2 needs more than ℤ/2 (P-409). Data-free and structural; none of the 19.
cc (main), 2026-10-28, P-408. Corrected before landing at its hostile referee (§ 5). **0 of 19.**

## 1. Witten's requirement (hep-ph/0201018, § 2; its smooth model Q = S³/ℤₙ)

- **The data:**
  - a flat SU(5) bundle with holonomy W (Wⁿ = 1) breaking SU(5) to SU(3) × SU(2) × U(1);
  - a symmetry F of Q, F′ ≅ ℤₙ, fixing two circles S₁ and S₂;
  - F lifted to the bundle trivially over S₁ and by W over S₂.
- **The mechanism:** the Higgs 5 and 5̄ sit at points on S₁ and S₂. Under F′ the doublet and triplet of the field on S₂
  transform differently.
- **Witten's own caveat at n = 2** (§ 2.2): "The case n = 2 would not quite work for us, at least in the first model presented
  above, because (2.9) and (2.8) could not be obeyed."

## 2. The topology, for Q = m004(p/q), p even (p ≠ 0)

- **The symmetries.** Sym(m004) = D₄. Its orientation-preserving part is {1, P, h₁, h₂}, with cusp maps I, I, −I, −I
  (the referee's `r1`):
  - P is the period-2 rotation (B1297: "axis disjoint from the knot");
  - h₁ and h₂ are the two strong inversions (B1462 § 1: "the dualising symmetry of Ballas' family"). They preserve
    orientation and are distinct from the amphichirality, which belongs to the four orientation-reversing classes.
  - On every filling, Sym(Q) = ℤ/2 + ℤ/2 = {1, P, h₁, h₂} (13 fillings, p odd included; `r1`).
- **(a) A strong inversion extends to every filling** (the Montesinos trick).
  - It acts on the cusp torus by −1, so it preserves every slope and extends over the solid torus.
  - Q/h = S³, so Q = Σ₂(S³, L), with L the image of the fixed set: four arcs glued at the cusp torus's four 2-torsion
    points, hence at most two circles.
- **(b) Exactly two circles when p is even, one when p is odd.**
  - dim H₁(Σ₂(L); ℤ/2) = #components(L) − 1.
  - dim H₁(Q; ℤ/2) is 1 for H₁ = ℤ/p with p even, and 0 for p odd.
  - This settles both directions at once.
- **Explicit check** (found by the referee's `r3` scan of links up to 14 crossings; each row reproduced on main without the
  scan by `verification/branch_links.py`: the double branched cover isometric to Q by SnapPy):

  | filling | branch link | components |
  |---|---|---|
  | m004(6, 1) | L11n132 | 2 |
  | m004(8, 1) | L13n4507 | 2 |
  | m004(8, 3) | L13n4800 | 2 |
  | m004(4, 3) | L14n24777 | 2 |
  | m004(5, 1) | K10n31 | 1 |
  | m004(7, 1) | K12n749 | 1 |
  | m004(3, 2) | K13n2180 | 1 |

- **(c) A strong inversion preserves the order-2 line.**
  - H₁(Q) = ℤ/p has exactly one order-2 character χ.
  - h acts on H₁ by −1, and χ(−x) = χ(x).
  - W = diag(1, 1, 1, −1, −1) has det 1 and commutant S(U(3) × U(2)): it breaks SU(5) to the SM group. It is Witten's (2.11)
    at e^{iρ} = −1. The only other order-2 class has commutant S(U(1) × U(4)).
- **(d) The lift is forced.**
  - A flat ⟨W⟩-bundle on Q with an h-lift is a homomorphism from the orbifold group π₁(S³ ∖ L)/⟨⟨μ₁², μ₂²⟩⟩.
  - Its restriction to π₁(Q) is χ, which is nonzero on μ₁μ₂. So **necessarily** g₁⁻¹g₂ = ρ(μ₁μ₂) = W. The only options are
    (1, W) and (W, 1) (`r5` (c)).
  - Under W the doublet gets −1 and the triplet +1.
- **(e) The period P also has two fixed circles when p is even** (the axis and the filling's core; Q/P = L6a2 filled at
  [(2, 0), (p, 2q)], its 2-fold cover isometric to Q on 9 fillings; `r4`, `r5`).
  - P acts on H₁(Q) by +1, so it preserves every line, including B1801's ℤ/3 and the ℤ/6.
  - Its order-2 lifts differ by W exactly when p ≡ 2 mod 4: true on (6, 1), (2, 3) and (10, 3); not on (8, 1), (4, 3) or
    (12, 1).
- **(f) The lines of higher order.**
  - Neither strong inversion preserves a line of order above 2, since it sends χ to χ̄.
  - For any involution the relative lift is an order-≤ 2 holonomy. So the pure ℤ/3 line admits no relative lift (`r7`: (0, 0)
    only).
  - Under P, the ℤ/6 line diag(ω, ω, ω, −1, −1) (commutant the SM's) has lifts differing by W³ = diag(1, 1, 1, −1, −1) when
    6 ∣ p and p ≡ 2 mod 4: on (6, 1), (6, 5) and (18, 1), not on (12, 1). The split is by W³, not by the holonomy's
    generator.

## 3. Computed checks (`verification/checks.py`; the referee's `verification/referee/`)

- **The order-2 Reidemeister torsion is 5/4** (Δ₄₁(−1) = −5) on all 59 even fillings listed.
  - Without Turaev's formula, the 2-fold cyclic cover has ∣H₁∣ = 5p/2 on every one (main's 59, by SnapPy; the referee's 13,
    by its own Smith normal form, q < 0 included).
  - Friedmann–Witten's L(Q) for this line is ∣H₁∣/∣τ∣ = 4p/5. As B1801 showed, it fixes no coupling.
- **Smith's bound is consistent:** for p even, Σ dim H_*(Q; ℤ/2) = 4, so two circles are allowed; for p odd it is 2, at most
  one.
- **Witten's conditions, enumerated** (the referee's `r8_witten_conditions.py`: (2.1)–(2.9), with the geometric constraint
  that the twisted circle's character is W's):

  | F′ | full solutions | dropping (2.8) | the mass-term split only |
  |---|---|---|---|
  | ℤ/2 | 0 | 1 | 8 |
  | ℤ/3 | 0 | 0 | 54 |
  | ℤ/4 | 2 | 3 | 192 |
  | ℤ/5 | 0 | 0 | 500 |
  | ℤ/6 | 4 | 5 | 1 080 |
  | ℤ/2 × ℤ/2 | 6 | 9 | 192 |

  - **ℤ/2 alone fails,** as Witten says. The one solution without (2.8) has σ = 0, which F′ cannot protect against the
    renormalisable (10)(5̄)². It needs an added matter parity.
  - **The fillings have no symmetry of order above 2.** But their full group Sym(Q) ≅ ℤ/2 × ℤ/2 = {h₁, h₂, P} admits 6 full
    solutions. Realising one needs the fields at the right fixed loci of all three, which is not checked (P-409).

## 4. What it means, and what it does not

- **Supplied by the figure-eight's own fillings:**
  - SU(5) → SM breaking: the order-2 line, or the ℤ/6 line under P;
  - involutions with exactly two fixed circles when p is even;
  - lifts that necessarily differ by W.

  That is Witten's topological structure at n = 2. It answers B1801's withdrawn claim: the split, if any, comes from the
  symmetry and its fixed circles, not from the Wilson line alone.
- **Not supplied, and open:**
  - Witten's first model needs more than a ℤ/2. Whether the full ℤ/2 × ℤ/2, with its 6 enumerated solutions, can be
    realised with the fields at its fixed loci is open (P-409).
  - A G₂ manifold with Q as its A₄ locus and the symmetries extending to it: existence open, I-36.
  - The Higgs at conical points on the fixed circles: postulated.
  - π₁(Q) is infinite, so the χ-line is one flat vacuum among many, unlike Witten's ℤₙ.
- **Hyperbolicity is unused:** the topology holds for every even p ≠ 0.
- **No input removed. 0 of 19.**

## 5. The referee (hostile, read-only; `audit/referee_b1802/`, scripts kept in `verification/referee/`)

**Verified independently:**
- the Montesinos extension;
- the fixed-set count, by explicit branch links;
- h = −1 on H₁;
- the non-conjugacy of the ℤ/3 lines;
- W's uniqueness;
- the torsion and covers;
- Smith's bound;
- Friedmann–Witten's 4p/5.

**One blocking finding, applied:** Witten's n = 2 caveat was omitted, and the draft's "Witten's mechanism needs exactly the
structure found here" overclaimed (§ 1, § 3, § 4).

**Corrections, applied:**
- three involutions, not "the" strong inversion;
- the period P and its ℤ/6 split;
- (f) restated;
- the seen-first's B1297 and B1462;
- the strong inversion distinguished from the amphichirality;
- both directions of the parity argument;
- the forced lift;
- the symmetry groups' coverage.

**Notes, applied:**
- the lock now tests the branch links' component counts rather than K's determinant;
- the scope (hyperbolicity unused, infinite π₁).

## Seen first

`VERDICT topic-sweep /strong(ly)? inver|Montesinos|branched cover|involution|fixed circle|Smith theory|doublet.triplet|P-408|period 2|2-bridge/ (full text): 219 of 1549 arcs on main match (NEGATIVE 42, OPEN 10, PROVED 164, RETRACTED 3); 7 register rows match (DONE 3, QUEUED 4)`.
- **Bearing on it:**
  - B1297: the period-2 symmetry;
  - B1462 § 1: D₄ and the strong inversion as the dualising symmetry;
  - B1484, B1794, B1795;
  - B1801 and its referee;
  - I-36.
- **Literature:**
  - Witten (hep-ph/0201018), § 2 and § 2.2;
  - Montesinos (1975);
  - the ℤ/2-homology of double branched covers;
  - P. A. Smith;
  - Friedmann–Witten (hep-th/0211269).

## Files

- `verification/checks.py` → `checks_run.txt`.
- `verification/branch_links.py` → `branch_links_run.txt` (§ 2's seven rows on main).
- `verification/referee/`: `r1_isometries.py`, `r2_torsion_order2.py`, `r3_branch_link_search.py` (with `r3_run_13.txt`,
  `r3_run_14.txt`), `r4_period_quotient.py`, `r5_period_fixed_set_and_lifts.py`, `r6_m004_8_1_check.py`,
  `r7_period_Z6_and_general_lift.py`, `r8_witten_conditions.py`, and their runs.

The lock: `tests/test_b1802_witten_splitting_from_the_figure_eights_strong_inversion.py`.
