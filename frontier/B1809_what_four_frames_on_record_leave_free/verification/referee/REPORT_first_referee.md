# P-406 THEOREM_DRAFT — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back (the referee could not write report files). Its scripts and outputs are beside
this file: r1_finite_L_at_i, r2_line_at_i, r3_two_torsion_lines, r4_robustness, r5_theorem_A_checks, r6_a0_at_i (each .py
with its .json or _run.txt), l1_rerun.txt, topic_sweep_full.txt. Each reuses banked code read-only (B1691's q-series, its
S164 b1656_funcs.py). No data read. Main's verification of the findings is § V at the end.

## Verdict per part

- **Definition — ill-posed.**
  - It has two readings. Under (a), "some object-built condition makes the quantity constant", the Corollary is false.
    Under (b), "the conditions the frame itself imposes", Theorems A and B drop out of the proof and the Corollary is a
    census.
  - It is vacuous on an empty locus.
  - It can be satisfied by enlarging an infinite discrete menu.
  - It has no rule separating a condition from an input.
  - It cannot see relations between outputs.
- **Theorem A — correct.** It is classical, holds for subgroups (r5), and is generic: every member has the same G (E20(c)).
  Its use in the Corollary is wrong (B2).
- **Theorem B — false as stated inside its own scope** (zero line, H-cov). It is unscoped for lines, and its neighbourhood
  and cusp clauses are imprecise.
- **Theorem C — overstated in every frame** (C2–C5).
- **Corollary — false or vacuous as worded** (B1, B4, C1).
- **Proposition D — three labels fail the record** (C6). The rest pass with wording fixes.
- **Overall — a census with one classical lemma, not a theorem.** It also does not meet P-406's own request ("frames … with
  no added moduli").

## BLOCKING

**B1. The definition decides the Corollary, and neither reading supports it.**
- **Reading (a).** "τ ∈ Fix(S)" is built from G, and imposing it pins values: m₂/m₃ = 1 (k ≡ 3/2 mod 4, B1806); 2/3 for
  a₀ (r6); J = 0 on mirror-fixed loci.
- **Reading (b).** The frames impose no selection of τ (τ = ω is retired), so Theorem A plays no part in the proof.
- **Variational conditions.** "Minimise V" has no solution at finite height (W175, W176), so it fixes every quantity
  vacuously.
- **Infinite menus.** With infinitely many weights, orders, fillings or fluxes, "one value per element of a finite set"
  misreads the menu.
- **Condition versus input.** There is no rule. P-425's note already calls requiring CM by K a choice, and "τ ∈ Fix(H)"
  is equally a choice of H.
- **Relations.** The definition cannot see them:
  - F1 with DR has 2 real data per choice against about 10 outputs, so at least 8 relations hold;
  - B1742's "the six are four";
  - B1691's m₁/m₃ ∝ Im τ·(m₂/m₃)².
- **Proposed definition.**
  - A frame is (C, D, Φ, 𝒦): continuous configurations C; discrete choices D (P-418's scoreboard); dimensionless
    outputs Φ, each named against the 19; object-built conditions 𝒦, listed and typed (symmetry, canonical
    construction, variational, arithmetic).
  - A condition enters 𝒦 only if the record derives it without choosing among alternatives. A finite choice goes into D.
  - For each choice d, C_d = {c satisfying 𝒦}, required non-empty.
  - Output j is fixed at d iff it is locally constant on C_d.
  - The free count f(d) is the generic rank of Φ on C_d, and the forced relations number m − f(d).
  - Symmetry selections (configurations fixed by H, counting τ, line, section and reading together) are reported
    separately with their values.

**B2. "Each point where the object could fix them is one of Theorem A's" is false within F.**
- **F2 holomorphic (B1804).** Fluxes force isolated CM points (i, ω, √−3, 2√3 i, (iφ, i/φ)): a countable dense set, not
  all in the orbits of i or ω.
- **F4 (W175).** At fixed height, Re τ = X*(y) off the mirror lines, with a pitchfork at Im τ ≈ 2.22.
- **F1 (B1667).** The canonical end fixes L as a function of τ.
- **The thread.** LR's axis ∣z − ½∣² = 5/4 is no reflection line (radius > 1; r5).
- **Boundary points.** Theorem A ignores them (the cusp, LR's golden points), though Theorem B uses the cusp.
- The Corollary survives these cases only through Theorem C.

**B3. Theorem B is false inside its own scope.**
- **The counterexample (r6).** B1697's unique weight-7/2 section with no end data, a₀ = ∂²R − E₄R/48, has t = −1/48 in
  B1806's closed form, so x = 3/2 and **m₂/m₃(i) = 2/3 exactly** (SVD: 0.666666666666667). This is neither a character
  constant nor coefficient-dependent.
  - At the canonical end, (m₁/m₃, m₂/m₃) = (0.0753, 0.658) at L₂(i) and (0.585, 0.731) at L_max(i).
- **Parameter-free sections.** "The coefficients are free" is false for the record's actual Higgs: DR and a₀ have none.
- **The functional form.** "A power of the distance" fails when the value at the point is nonzero. The correct form is
  r₀ + c·δ^p.
- **Open or off-record items.** m₁ near i in the k ≡ 3/2 class was P-431, open. m₁ at the cusp for DR at finite L is not
  on record (local slopes 0.62–0.86 in ∣q∣, still drifting).
- **Supports the draft (r1):** m₁(i) = m₁(e^{iπ/3}) = 0 and m₂/m₃ = 1 for DR at zero line and finite L (five values of L).

**B4. The CP and θ̄ clauses contradict the record.**
- **J.** The mirror sends J to −J and fixes every mass ratio and ∣V∣ (B1750 § 3), so J = 0 is fixed on the geodesics.
- **θ̄.** "Not computed, so not fixed" is a non sequitur. The referee claimed θ̄ ∈ {0, π} under I-18. (Main: this
  overreaches; see § V.)
- **Mixing.**
  - B1620: with couplings in τ alone every mixing matrix is a permutation. At zero line V ≡ 1.
  - B1612: six fixed patterns, none in the data.
  - P-224 (DONE) already states the stabiliser no-go. F leaves out the residual-symmetry frame.

## CORRECTIONS

- **C1. What F does not compute.**
  - The scale (ratios only; B1168, B1183, B1184).
  - y_t, y_b, y_τ, λ and θ̄.
  - The gauge couplings, known only up to (α_GUT, M_GUT).
  - F computes about 10 dimensionless combinations; 6–7 of the 19 are not reached. State the count.
- **C2. F1.**
  - Isotropic sections (R; t = −5/288; η⁶R) give constants (0).
  - "Mixing non-constant" is false at zero line.
  - "Real-analytic" fails where singular values cross, and for L_max.
  - The family is undefined; with DR it is τ alone.
  - Prove non-constancy without data, from B1691's exponents, not from W173.
  - B1645 and B1646 are zero-line results.
- **C3. F2.** The fixed set is countable and dense, not finite. There is no LR-invariant Kähler class. F2 computes none of
  the 19.
- **C4. F3.**
  - The y·b_a term shifts M_GUT. Say "leaves the one-loop sin²θ_W unchanged" (B1801).
  - The generic SU(5) relation is imposed.
  - Friedmann–Witten's G_N relation contains an unknown shape a.
- **C5. F4.**
  - W175's dV/dy ≥ 288 holds only for Im τ in [1.2, 4]. W176's least is at the domain's edge, and local minima are not
    excluded.
  - § 320 is a READING, in the democratic limit only.
  - F4 does fix Re τ at each height, and the height ≈ 2.22.
- **C5b. The stabiliser must be the whole configuration's** (τ, line, section, reading).
  - A line of exact order N ≥ 4 has a torsion-free stabiliser, so i and ω are never configuration-fixed on the record's
    order-5 and order-10 lines (r5).
  - With lines, values at i are definite: DR on line (0.1, 0.3) gives (0.065, 0.648) at L₂(i). On the S-fixed line
    (½, ½) it gives (0.0381, 0.519) at L₂(i) and (0.416, 0.708) at L_max(i) (r3, r4; exploratory).
  - On ω's ST-fixed line (1/3, 2/3) the values are (0, 1).
  - B1730's F_a directions are outside B1691's and B1806's proofs.
- **C6. Proposition D.**
  - **The arrow is generic under GM5b.** B1083's addendum: the monoid home "is gone"; it is escape (B1662 W3), shared by
    every member and by m003; its side is CHOSEN.
  - **π₁ ↠ 2T is not object-specific.** B727: 7₂, 7₃ and 8₁ surject; only the arithmetic origin is specific.
  - **The hand is not forced.** FK10 is OPEN; B1796 assumes the hand.
  - **Correct:** hypercharge and ℤ₆, both generic. For ℤ₆, use B1221's reason.
  - **E₆ across the faces** is not SM data.
  - **"Three" and the doublet–triplet labels are correct.**
- **C7. G's sources.**
  - Inverses need GM5b.
  - The mirror comes from B1750 § 3 and amphichirality; GM5c is OPEN.
  - Under positivity alone no word is elliptic (B1662 F3).
  - The elliptic classes are S, ST and (ST)⁻¹.

## NOTES

- **N1. l1_fixed_loci.py.** It reproduces 180/17/26/137, but:
  - it is floating-point with a 10⁻⁹ tolerance, not exact;
  - it classifies by trace, without computing the geodesics;
  - it counts the identity as empty;
  - it checks elements only. r5 adds subgroups: 31 of 31 meeting pairs of reflection lines meet at i (13) or ω (18).
- **N2. PLAN.md is stale against B1806** ("→ ½" near i).
- **N3. P-406 asked for frames with no added moduli.** F1–F4 all add moduli, so the draft proves "can fit, cannot derive"
  for four frames.
- **N4. The title collides.** docs/THE_FORCED_AND_THE_FREE.md (2026-08-19) has the same title and thesis (the torsor
  pattern; Hom(G, ℝ₊) = 0). Also on record:
  - P-224 (DONE);
  - B1620 ("reduces none of the 13"); B714; B736 ("zero of 24 reduced");
  - B758, B1123;
  - GENESIS v1.55 / B1750.

  The sweep found 88 of 1 553 arcs and 3 rows.
- **N5. "No scale" and "small parameter" are undefined.** Tabulate the fixed values (2/3, 0.075, 0.585, 0.038, 0.519).
- **N6. Grades.** B1789–B1791 at their grades: B1791 is a three-line census, and all three are scoped to DR.

## Strongest honest title (the referee's)

> WHAT THE FOUR FRAMES ON RECORD LEAVE FREE (P-406; a census with one classical lemma): each of F1–F4 keeps a continuous
> datum the object does not fix; every computed dimensionless output varies with it except the degenerate ones; the
> object's symmetries pin only PGL(2, ℤ)'s fixed loci, where they force degeneracies and the CP bits, and for
> parameter-free sections definite order-one values (m₂/m₃ = 2/3 at i), never a hierarchy; per discrete choice the frames
> fix relations, whose count is P-406's deliverable; the forced discrete SM structure is generic; the object-specific
> residue is the arithmetic origin ℚ(√−3), a mathematical fact.

## V. Main's verification (2026-10-29)

- **N4: verified.** docs/THE_FORCED_AND_THE_FREE.md exists (2026-08-19, at the B1078/B1079 commit). It has the same title
  and the torsor thesis ("the object supplies an option-space carrying a transitive symmetry and withholds the point").
  An E54 instance on main's side: the draft was named without sweeping the docs' titles.
- **B3: verified independently.** With main's own evaluator (audit/drafts/p431/a0_at_i_check.py; exact SVD, 50 digits),
  B1697's a₀ at τ = i gives m₂/m₃ = 0.666666666666667, and B1806's exact closed form gives 2/3 (t = −1/48, x = 3/2). The
  near values are 0.666666666666666 at ε = 10⁻⁸ and 0.66666438 at ε = 10⁻³. **"No scale at the forced points" is false as
  written.** What survives is narrower: no hierarchy is fixed at a forced point.
- **C6, the arrow: verified.** B1083's 2026-10-16 addendum: "Under GM5b … every move is invertible, so that home is gone.
  The arrow survives as escape."
- **C6, 2T: verified.** B727 lines 38–40: 7₂, 7₃ and 8₁ surject onto 2T; "what is object-specific is only the
  arithmetic origin".
- **C5b: verified,** a standard fact. Γ₁(N) is torsion-free for N ≥ 4, so a line of exact order N ≥ 4 has no elliptic
  stabiliser. The referee's line values (r2–r4) are exploratory and not re-run by main.
- **B4, J: accepted** (the mirror's action, B1750 § 3).
- **B4, θ̄: the referee overreaches.** I-18 is UNEARNED. B1246's sharpening (2026-09-03): "THE TYPE DICTIONARY REACHES θ,
  NOT θ̄" — the observable θ̄ = 0 "carries a Yukawa-sector contingency the chain does not derive".
  - So the record does not pin θ̄, even conditionally. Under I-18 it pins the type of an E-type parameter: θ, not θ̄.
  - The referee's other point stands: "not computed, so not fixed" is a non sequitur; say "not reached".
- **B1, B2, C1–C5, C7, N1–N3, N5, N6: accepted** as stated. Each is a reading of cited arcs and needs no new computation.
- **Consequence.** The draft is withdrawn as a theorem. It is rewritten as a census under the referee's sharper
  definition (`CENSUS_DRAFT.md`), and main's recommendation on P-406 is revised.
