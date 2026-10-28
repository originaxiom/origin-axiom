# B1800 — THE COUPLINGS AS BULK OVERLAPS OF FLUX ZERO MODES (L251 AS LITERALLY STATED; P-403's GEOMETRY-FIRST STEP; DATA-FREE): WITH FLUX-ONE MATTER ON THE THREE EVEN CHARACTERISTICS AND A FLUX-TWO HIGGS, WILSON-LINE CONSERVATION GIVES B1636's PARITY PATTERN, BUT THE COUPLINGS ARE Y_pq² ∝ θ_p(τ)θ_q(τ), i.e. Y_pq ∝ η^{3/2} θ_r^{−1/2} — NOT B1636's θ_r², FOR ANY FIXED HIGGS AND ANY MATTER WILSON LINES (A q-EXPANSION PROOF); B1642's RESIDUE COUPLING HAS θ_r² BUT IS ANTISYMMETRIC, THE OVERLAP IS SYMMETRIC

**Verdict: PROVED** (no data). It contains:
- a re-derivation on main of a known closed form (Cremades–Ibáñez–Marchesano), checked by quadrature to 5 × 10⁻¹⁶;
- three identities, to 10⁻⁴⁶;
- an exact negative for B1636's coupling in this flux frame.

cc (main), 2026-10-28. Corrected before landing at its hostile referee (§ 5). **0 of 19.**

## 1. What was asked, and what the record already had

**L251 asked whether the couplings are overlaps of the fibre's zero modes:**
- **(a)** with the parity pattern conserved;
- **(b)** as a fixed multiple of B1636's Y ∝ [[0, θ₄², θ₃²], [θ₄², 0, θ₂²], [θ₃², θ₂², 0]];
- **(c)** with how many free reals.

**The record had already answered it in the fibre's point frame.** OPEN_LEADS' currency note of 2026-10-15 says so, though
L251's own status line was never updated:
- **B1642's residue coupling,** Y_pq = ε_pqr κ_r θ_r²/(2πη³), "the first coupling on the record computed with no free
  coefficient". It is rank two, with an exact massless direction, not B1636's golden matrix (B1644).
- **B1653:** a point coupling has rank at most two.
- **B1651:** no flat or harmonic Higgs couples the zero modes in the bulk.
- **The SM seat's W72:** the surface frame's overlap, full rank, with no free number.
- **The earlier hand design of this computation** (P-087, P-088), including a flux-one Higgs variant.

**This arc computes L251 as literally stated:** as bulk overlap integrals of flux modes (Cremades–Ibáñez–Marchesano). It
reaches (b)'s negative by an independent route.

## 2. The construction (`verification/overlaps.py`)

- **The fibre:** E_τ, with the lattice (1, τ) and area Im τ.
- **The modes** are Cremades–Ibáñez–Marchesano's in the symmetric gauge. The Wilson lines enter as Scherk–Schwarz phases
  (a, b).
  - Matter: flux-one modes ψ_p = N e^{iπ z Im z/Im τ} ϑ[a_p, b_p](z, τ), for the three even characteristics [0, 0] (θ₃),
    [½, 0] (θ₂) and [0, ½] (θ₄). These are three ℤ₂ × ℤ₂ flavour Wilson lines; all the fermions share one spin structure,
    so "one per even spin structure" is a label, not literal.
  - The Higgs: flux-two modes χ_{(a,b),k} = N e^{2iπ z Im z/Im τ} ϑ[(k + a)/2, b](2z, 2τ), with k = 0, 1, in each of the four
    Wilson-line sectors (a, b) ∈ {0, ½}². Two modes per sector give up to eight light Higgs doublets, and "a fixed Higgs" is
    a choice of their vevs.
- **The checks** (the referee's own code, Gauss–Legendre quadrature):
  - covariant holomorphy, to finite-difference accuracy;
  - the boundary conditions, to 10⁻¹⁴;
  - norms √(Im τ/2M), equal for every characteristic;
  - orthonormality within each sector.
- **A coupling is allowed by Wilson-line (charge) conservation** only when the integrand ψ_pψ_qχ̄ is doubly periodic, i.e.
  when L_p ⊗ L_q ⊗ L̄_h is trivial with its connection. Otherwise it is forbidden.

## 3. The results

**(a) The parity pattern is conserved.**
- The pair (p, q) couples through the sector c_p + c_q.
- In B1634's parity characters, [a, b] ↦ ((−1)^{2a}, (−1)^{2b}) on the characteristics shifted by (½, ½) (θ₂ → (+, −),
  θ₃ → (−, −), θ₄ → (−, +)), that sector is the third generation's. Each pair of generations is coupled by the third's
  Higgs sector.
- The diagonal pairs couple only through sector (0, 0). B1636's zero diagonal is the absence of a sector-(0, 0) Higgs.

**The closed form** (`verification/closed_form.py`; `assertions.py`). By the theta addition formula, every allowed overlap is

  Y_{pq,(s,m)} = (Im τ)^{−1/4} · ϑ[(a_p − a_q + m)/2, b_p − b_q](0, 2τ) · e^{2πi s_m Δb}.

- The normalisation (Im τ)^{−1/4} is predicted, not fitted: the quadrature agrees to 4.7 × 10⁻¹⁶ at four τ, and at seven
  in closed_form.py. Every predicted zero vanishes.
- This is the known result (Cremades, Ibáñez and Marchesano, JHEP 0405:079, hep-th/0404229, with Wilson-line phases as in
  Abe, Kobayashi et al.), re-derived and checked on main.

**The identities,** to 10⁻⁴⁶ in `assertions.py`, and to 10⁻⁴⁰ in the referee's `ref_identities.py`:
- ϑ[¼, 0](0, 2τ) = ½θ₂(τ/2), and ϑ[¼, ½](0, 2τ) = ½e^{iπ/8}θ₂((τ + 1)/2);
- **the squares:** c₃₂² = θ₂θ₃/2, c₃₄² = θ₄(2τ)² = θ₃θ₄, and c₂₄² = (i/2)θ₂θ₄.
- So **Y_pq² = (Im τ)^{−1/2} κ_pq θ_p(τ)θ_q(τ)**, with κ = ½, 1 and i/2. By Jacobi (θ₂θ₃θ₄ = 2η³), Y_pq ∝ η^{3/2}θ_r^{−1/2}.

**(b) B1636's matrix is not these overlaps.**
- **With a fixed Higgs it is excluded exactly.**
  - In each off-diagonal sector the two Higgs modes enter through one τ-independent combination (ratio 1, i or 0 at every
    τ), so a fixed Higgs gives Y_pq = c_pq(τ) × a constant.
  - B1636 needs Y_pq ∝ θ_r², while the overlap is ∝ θ_r^{−1/2}. A fixed-Higgs reproduction would need relative sector
    components ∝ θ_r(τ)^{5/2}, which depend on τ.
- **At any matter Wilson lines, also excluded exactly** (the referee's q-expansion proof, `referee/ref_b_test.py`):
  - The setting: Re τ fixed, Im τ → ∞, a fixed Higgs of two modes per sector, and any common factor.
  - Each entry's leading exponent lies in [0, ¼] ∪ {9/16}.
  - The θ₂² entry needs e = e′ + ¼, which forces e′ = 0 for the other two entries.
  - Those two are then series in q^{1/4} with no q^{1/2} term, whereas θ₃²/θ₄² = 1 + 8q^{1/2} + … This holds for every
    labelling.
- **Approximately, it is not excluded.** Near-matches of about 2% rms over Im τ 0.7–2.2 (5% over 0.4–4) exist at continuous
  Wilson lines (`referee/ref_b_joint.py`).
- **Normalisations drop out.** Any Kähler or modular-weight factor common to all sectors does.
- **Not covered:**
  - Higgs vevs depending on τ sector by sector;
  - other flux assignments (the literature's standard M = 3 three-generation route; right-handed matter at flux −1,
    where conservation leaves only Y ∝ 𝟙);
  - point or residue frames (B1642, B1653);
  - couplings of four or more fields, and kinetic mixing.
- **The contrast:** B1642's residue coupling has B1636's θ_r², but is antisymmetric (ε_pqr). The bulk overlap is symmetric
  and ∝ θ_r^{−1/2}.

**(c) What is free.**
- No coefficient.
- What remains is τ and **five complex Higgs components**: one per off-diagonal sector, and two in sector (0, 0), whose map
  to the three diagonal entries has rank 2 (`referee/ref_q4_and_count.py`).
- The matter Wilson lines are fixed here at the even characteristics.

## 4. What it means — for P-403's flux geometry

- **In this flux frame a sector's coupling depends on the difference of its two legs' Wilson lines.** With hypercharge
  lines (charge q at q·w) that is (q_L − q_R)w: 5w (up), −w (down), −9w (leptons). The sum fixes only the Higgs's sector, a
  selection rule.
  - Pairs with equal differences give identical overlaps: (1, 2), (−1, 0) and (3, 4) all give
    0.5555537334 + 0.1187227233i.
  - Moving the Higgs off the sum breaks periodicity (`referee/ref_q4_and_count.py`).
- **The flat frame differs.** B1656's frame splits the sectors by the same difference (its R₁ = θ₁((q_L − q_R)w)), but at
  level 1 and also through the Higgs's 3w (the SM seat's §302: the up i-channel ∝ θ₂(3πw)θ₂(5πw)).
  - The flux overlap is level 2 and drops the 3w dependence.
  - B1656's zero conditions do not carry over: where 9w is a lattice point the leptons' flux couplings are θ₂(2τ) and
    θ₃(2τ), not zero.
  - **The two frames' couplings are not the same object.**
- **P-403's sealed design** should therefore:
  - name the U(1) that carries flux 1 and 2 (B1789 excluded only a net hypercharge flux in B1656's frame);
  - compute the three sectors' couplings in closed form, from (q_L − q_R)w;
  - read R₂, R₁ and D, before any data.
- **No input removed. 0 of 19.**

## 5. The referee (hostile, read-only; `audit/referee_b1800/`, scripts kept in `verification/referee/`)

**The mathematics reproduces.** The referee's own theta series and Gauss–Legendre quadrature give the closed form to
4.9 × 10⁻¹⁵ at three τ, two of them new, with K predicted.

**One blocking finding, applied:** the draft's "it answers L251 … never computed" contradicted the record — the currency note
and B1642, B1644, B1651, B1653, W72 and P-087/P-088 were missed in its sweep. § 1 is rewritten, and L251's status line gets
a dated note.

**Corrections, applied:**
- the diagonal sector carries two Higgs components (c);
- the exact squares Y_pq² ∝ θ_pθ_q make (b) a one-line proof;
- (b) is scoped, with the q-expansion proof at every Wilson line, the approximate near-matches and what is not covered;
- § 4's transfer to B1656 is corrected (not the same object);
- "the third" sector is made explicit;
- K and the identities are asserted in a script;
- the attribution: CIM's closed form, re-derived.

**Notes:**
- "the retired ruled branch" was unsupported (the record retires τ = ω on it, not the branch). It is removed here, and
  B1799's phrase gets a dated note.
- The quadratures in overlaps.py and closed_form.py share their theta and mode functions; the referee's are independent.

## Seen first

`VERDICT topic-sweep /overlap|zero mode|magneti[sz]ed|flux.one|flux.two|Wilson.line sector|L251|golden spectrum|B1636/ (full text, aliases: the golden spectrum): 99 of 1547 arcs on main match (NEGATIVE 20, OPEN 1, PROVED 78); 42 register rows match (DONE 32, LEAD 3, QUEUED 7)`.
- **Bearing on it:**
  - B1634 (the θ-square lifts; the parity characters), B1635 and B1636 (the coupling), B1640;
  - B1642 and B1644 (the residue coupling, rank two), B1649, B1651 (no flat or harmonic Higgs couples in the bulk),
    B1653 (a point coupling's rank);
  - B1656, B1789(b), B1792 and the SM seat's §302;
  - the SM seat's W49 and W72;
  - P-087, P-088, P-401, P-403.
- **Literature:**
  - Cremades, Ibáñez and Marchesano (2004), "Computing Yukawa couplings from magnetized extra dimensions";
  - Abe, Kobayashi et al. (Wilson-line and Scherk–Schwarz phases);
  - Kikuchi, Kobayashi et al. (2020) (modular transformation);
  - the theta addition formula and Jacobi's identity (standard).

## Files

- `verification/overlaps.py` → `overlaps_run.txt`.
- `verification/compare.py` → `compare_run.txt`.
- `verification/closed_form.py` → `closed_form_run.txt`.
- `verification/assertions.py` → `assertions_run.txt`.
- `verification/referee/`: `ref_overlaps.py`, `ref_identities.py`, `ref_b_test.py`, `ref_b_joint.py`,
  `ref_q4_and_count.py`, and their runs.

The lock: `tests/test_b1800_the_couplings_as_overlaps_of_the_fibres_zero_modes.py`.
