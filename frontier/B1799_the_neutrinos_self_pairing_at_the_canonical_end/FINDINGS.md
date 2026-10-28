# B1799 — THE NEUTRINO'S SELF-PAIRING AT THE CANONICAL END (P-283; L221; DATA-FREE): A SELF-PAIRING HAS R₁ = 0 EXACTLY AND, WITH A TRACELESS PARTNER, AN EXACTLY SYMMETRIC COUPLING. ON THE 286 CENSUS LINES AT THREE POINTS NEITHER MAJORANA PAIRING'S det M VANISHES — PROTECTION IS LIFTED THERE, m₁ ≠ 0 — BUT THE WEINBERG PAIR'S det M DOES VANISH ON CP LINES (8 ORDER-8 LINES AT Re τ = 0, 18 AT Re τ = ½) AND AT ISOLATED POINTS. A PURE TYPE-I SEESAW'S LIGHTEST NEUTRINO IS MASSLESS ON THE CENSUS EXACTLY WHERE THE ELECTRON IS, AND ON NO SLOPE-2/5 LINE

**Verdict: PROVED** (one derivation, identities to machine precision, a structural census; no data). cc (main), 2026-10-28,
P-283 (from P-146, the web seat's remark of 2026-10-14) with L221. It ran only after B1795's sealed outputs were committed,
since on lines of order dividing 6 its sectors coincide with B1795's pairs. Corrected before landing at its hostile
referee (§ 5). **0 of 19.**

## 1. The question

The web seat read the neutrino's first generation as massless: a Majorana pairing has δ = 0, so B1703's protection gives
R₁ = 0. But the consequence m₁ = 0 is a leading-order statement, and B1667's canonical end lifts it (B1711, B1716). Is
m₁ = 0 kept at the canonical end, for a Majorana pairing and against a Dirac one?

## 2. The census (`verification/majorana.py` → `majorana_rows.jsonl`, `majorana.json`, `majorana_run.txt`)

The sectors:
- ν^cν^c (6Y 0, 0), line-free;
- LL (−3, −3), the Weinberg operator's pair;
- the Dirac L ν^c (−3, 0).

They are computed on B1795's 286 lines at its three points (B1716's two generic τ and the six's strip point), through
B1795's `sector()`, with the partner typed as the frame's Higgs section (S and S̃). For ν^cν^c that is B1795's typing of
a 6Y = 0 singlet; for LL, whose partner HH has 6Y = 6, it is a further hypothesis.

| sector | rows | R₁/‖R‖ (max) | det M: least Dn; exact zeros | ∣Y − Yᵀ∣/∣Y∣ (max) |
|---|---|---|---|---|
| ν^cν^c (Majorana) | 3 points | 3.7 × 10⁻²⁰ | 7.1 × 10⁻⁴; none | 1.2 × 10⁻¹⁶ (symmetric) |
| LL (Weinberg pair) | 858 | 4.6 × 10⁻¹⁷ | 1.1 × 10⁻⁵; none on the census | 2.0 × 10⁻¹⁶ (symmetric) |
| L ν^c (Dirac) | 858 | 0.71 | 5.7 × 10⁻¹⁹; 162 rows on 54 lines | up to 1.4; symmetric only on the 5 lines of order 1 and 3, where −3w is in the lattice and L ν^c equals ν^cν^c (B1703's N ∣ 3 protection) |

## 3. What is derived, and what it means

- **R₁ = 0 for a self-pairing, identically.** The residue of `bil` is v_x v_yᵀ/θ₁′(0) for every twist pair (the referee's
  `r1`, to 3.8 × 10⁻¹¹; from θ₁(u + τ) = −e^{−iπτ}e^{−2πiu}θ₁(u)). Equal twists give v ⊗ v with the phases included, so
  R₁ = vᵀεv = 0. This derives B1703's rule for δ = 0. R₁ never depended on L; what B1716 showed is leading-order is its
  consequence m₁ = 0.
- **The coupling is symmetric, as a Majorana mass must be — given a traceless partner.**
  - B1736 writes B1656's coupling as Y = u hᵀ + h uᵀ − (u·h)1 + u₁[h]_× + h₀(u₁1 + [u]_×). The form holds in the code's
    block order (j, i, k) to 2.2 × 10⁻¹⁶.
  - R₁ = 0 makes u₁ vanish, and the frame's Higgs section has h₀ = 0 exactly, so Y = u hᵀ + h uᵀ − (u·h)1, symmetric.
  - **The typing matters:** a partner with a "1" component adds h₀[u]_×. Typing HH as the quaternion square S·S = −(h·h)1
    makes Y_LL exactly antisymmetric (its Majorana-allowed part vanishes), and S·S̃ gives neither symmetry (the referee's
    `r6`).
- **On the census, det M ≠ 0 for both Majorana pairings, at every line and point.** This is an observation, consistent
  with B1716's numerical converse; B1716's sufficient condition cannot fire for equal twists. So det Y = 4 det S det M
  tr(εSMᵀ) (B1659) is generically non-zero there: protection is lifted, m₁ ≠ 0.
- **Off the census the Weinberg pair's det M vanishes** (the referee's `r3`, `r8`, `r5`, `r9`):
  - **Re τ = 0:** on 8 order-8 lines, (1/8, odd/8) and (3/8, odd/8), at every Im τ tried (1.7, 2.2, 2.6, 3.0375). The
    reflection equalises the three regularised norms, c_i = c_j = c_k, and with R₁ = 0 B1716's Z2 cancels D. This is
    P-292's kind.
  - **Re τ = ½:** on 18 lines of orders 4 and 12.
  - **At the generic point 0.37 + 2.2i:** at isolated non-torsion lines.
  - **The ν^cν^c pairing shows no zero** on a 41 × 23 grid of τ over [−½, ½] × [1.3, 3.5] (least Dn 1.5 × 10⁻⁴).
- **The Dirac sector agrees with B1716's law on all 858 rows** (`verification/law_check.py`).
  - Its 162 zero rows follow from the law's proved "if" direction (B1716's dated correction 2), and fall on the charged
    leptons' own zero lines: the same left twist −3w, and the same 162 rows as L e (the referee's `r7`).
  - Its 696 non-zero rows extend the law's numerical converse to a right twist of 0 and to a third τ, the strip (232
    rows).
  - Over the whole twist torus at 0.37 + 2.2i, and on 266 lines at four CP values of τ, the Dirac det M has no zero off the
    law (the referee's `r5`, `r3`).
- **For a pure type-I seesaw** m_ν = −Y_D N⁻¹ Y_Dᵀ with N, the ν^cν^c mass matrix, invertible (its σ₃ > 0 at the three
  points): det m_ν = 0 iff det Y_D = 0. This is linear algebra and holds for any invertible N, e.g. P-326's weight-3 form.
  - **On the census,** the lightest light neutrino is exactly massless, for every τ, reading and horocycle, on those 54
    lines — **the lines where the electron is massless** — and on no other census row.
  - **Off the census,** det Y_D also vanishes at isolated points where B1659's pairing factor tr(εSMᵀ) vanishes (`r10`).
  - A direct Weinberg term would lift these zeros, so this holds for a pure type-I seesaw only.
- **On the slope-2/5 lines** the law's proved sufficient condition never fires at any order, since −3w then has order
  divisible by 5. On the census's 30 slope-2/5 lines (orders 5, 10 and 60, including B1792's six order-60 carriers; the
  carriers of orders 15, 20 and 30 not computed) neither route has a zero: LL's Dn ≥ 6.1 × 10⁻², ν^cν^c's ≥ 7.1 × 10⁻⁴, and
  no Dirac zeros. On the six's carriers at the strip, the lightest state is 6.6 × 10⁻⁵ – 5.1 × 10⁻³ of the heaviest for LL
  and 1.7 × 10⁻⁵ – 4.0 × 10⁻³ for the Dirac sector.

**This is a structural statement, not a value.** The size of m₁ needs the neutrino sector's own inputs (P-326; any
oscillation comparison sealed). Neutrino masses are not among the Standard Model's 19. **No input removed. 0 of 19.**

## 4. Scope

- **The frame:** B1656's coupling at B1667's canonical end.
- **The census:** 286 lines at three points.
- **The partner:** typed as the frame's Higgs section, a hypothesis. The symmetry and the LL statements depend on it.
- **Not examined:** the weight-3 Majorana form of P-326 (a different slot), the light spectrum's ordering against data, and
  other typings.
- **The exploration** that first saw the symmetric coupling (`verification/exploration/`) also, by accident, fixed B1795's
  pairs on 14 lines (disclosed in B1795's FINDINGS).

## 5. The referee (hostile, read-only; `audit/referee_b1799/`, scripts kept in `verification/referee/`)

**Custody clean:**
- 858 distinct rows, matching split.lines();
- 10 random rows reproduce exactly;
- the instrument and rows are byte-identical to the draft;
- the disclosed overlap holds: LL's Dn equals B1795's H-pair Dn on the 60 rows of order dividing 6, to 2 × 10⁻¹².

**One blocking finding, applied:** the draft's "det M never vanishes" for the Majorana pairings was false outside the
census for LL (the CP lines and isolated points above). The title and § 3 are scoped to the census.

**Corrections, applied:**
- the seesaw statement holds on the census, at the electron's lines, for a pure type-I seesaw; its matrix is renamed N;
- "out-of-sample" withdrawn: the zero rows follow from the law's proved direction;
- R₁'s L-independence stated correctly;
- the symmetry tied to the partner's typing;
- the strip's light states quoted on the six's carriers;
- the slope-2/5 census described exactly (30 lines);
- the Dirac sector's symmetric lines noted.

**Notes:** u₁ = 0 is also enforced by the instrument's cut (∣R_s∣ ≤ 10⁻¹², c_s None), which is harmless given the analytic
R₁ = 0. The log's doubled exit line is the wrapper's echo.

## Seen first

`VERDICT topic-sweep /Majorana|neutrino|seesaw|Weinberg|nu\^c|ν\^c|m_?1 ?= ?0|self.pairing|P-283|P-326|L221/ (full text): 74 of 1544 arcs on main match (NEGATIVE 14, OPEN 2, PROVED 57, no verdict file 1); 8 register rows match (DONE 3, QUEUED 5)`.
- **Bearing on it:**
  - B1616: on the retired ruled-branch weave a constant Majorana mass has no invariant; the coupling here is τ-dependent
    with a partner section, so this is not that.
  - B1674: the anomaly requires a ν^c.
  - B1703: protection.
  - B1711; B1716 with its dated corrections 1 and 2: the converse numerical, the "if" proved for any charges.
  - B1659: the joint law.
  - B1736: the coupling's channel form.
  - B1795: the instrument and the overlap.
- **The register:** P-146, P-157, P-283, P-292 (a CP-line exception of the same kind), P-326, P-290; L221.
- **Literature:** the type-I seesaw and the Weinberg operator (standard; det m_ν = det(Y_D)² / det N); modular flavour models' Majorana sectors (Feruglio's programme), in which the Majorana mass is a modular form — P-326's route, not this coupling.

## Files

- `verification/majorana.py` → `majorana_rows.jsonl`, `majorana.json`, `majorana_run.txt`, `majorana_log.txt`.
- `verification/law_check.py` → `law_check_run.txt`.
- `verification/exploration/look.py` → `look_run.txt`. Its repository path was made relative, and the log regenerates
  identically.
- `verification/referee/`: r1–r10 and their runs.

The lock: `tests/test_b1799_the_neutrinos_self_pairing_at_the_canonical_end.py`.
