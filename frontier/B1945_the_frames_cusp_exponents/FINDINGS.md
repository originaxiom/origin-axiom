# B1945 — Frame C's cusp exponents are the census lines', and its average takes their minima

**Verdict: PROVED** (at leading order in |q|; every cell, both generations, equal to B1788's closed form and tropical
rule, which rest on B1659's law, shown here to hold on frame C exactly; planted charges caught; its second computation the web seat's W-F25, which agrees, § 1b). Main, 2026-11-15. Data-free: nothing here is set
beside a measured number. Register row P-859. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /cusp exponent|power of q|q-power|Froggatt|exponent in q|decay rate in the cusp|high in the cusp/: 1 of 1686 arcs on main match (PROVED 1); 6 register rows match (DONE 3, QUEUED 3)`.
  The register rows led to the record's earlier work, read for this arc:
  - **B1788** (PROVED): the closed form of the exponents in B1656's frame, e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2.
  - **The SM seat's W178** (harvest row 1497, reproduced by main bit for bit): every census line's cusp exponents
    exactly, and its skeleton test, in which no single line's cusp pattern passes.
  - **B1691 and B1692** (the exponent ½ in the older frames); **B1698** (the order-5 lines at one τ: NEGATIVE as
    sealed, and Y_e = Y_dᵀ exactly on them); **P-169, P-593.**
- **So the pointwise table below is not new.** What is new:
  - frame C's 24 points carry exactly the census exponents: the exact channel weight and Theorem 90's correction do not
    move them;
  - the average over the points takes the minima, a pattern that mixes points.
- **The literature:** the leading power of a theta constant with characteristic (α, β) is |q|^(‖α‖²/2) (standard).

## 1. The table (`verification/pointwise_exponents.py`, `pointwise_exponents_a0.py`)

- **What was computed.** At each point of order 5, in each sector and each Higgs reading, the ratios σ₂/σ₃ and σ₁/σ₃
  of frame C's coupling were computed with B1940's extended-precision frame, on the column x = 0.13:
  - the points with a ≠ 0 at heights 24, 32 and 40;
  - the four points with a = 0 at heights 40, 60 and 80, at 40 + 3.5 Im τ digits.
- **How the rate is read.** A ratio C·y^s·|q|^k (|q| = e^(−2π Im τ)) gives k from the two slopes between the three
  heights. The rates settle on multiples of 1/200, the grid the characteristics allow, within 1e-3 (a ≠ 0) and 2e-3
  (a = 0, whose cells carry corrections beyond one power of Im τ).
- **The rates depend only on the point's first coordinate a:**

  | a | up, S | up, S̃ | down, S | down, S̃ |
  |---|---|---|---|---|
  | ±1/5 | 1/10, 3/5 | 1/10, 1/2 | 1/5, 11/20 | 1/5, 13/20 |
  | ±2/5 | 3/10, 1/2 | 3/10, 4/5 | 1/5, 11/20 | 1/5, 13/20 |
  | 0 | 1/2, 1 | 1/2, 1/2 | 1/2, 1 | 1/2, 1/2 |

  Each cell gives the rate of m₂/m₃, then of m₁/m₃.
- **Against the record.**
  - Every m₂/m₃ cell, all 96, is B1788's closed form. For the up sector (q_L, q_R) = (1, −4), it gives 1/10 at
    a = ±1/5, 3/10 at ±2/5 and 1/2 at 0. For the down sector (1, 2), it gives 1/5 and 1/2.
  - The points a = ±2/5 give W178's tuple for the slope-2/5 lines, (3/10, 4/5, 1/5, 11/20).
- **The lock** (`test_b1945_cusp_exponents.py`) checks the closed form, W178's tuple and the a = 0 cells.
  - With the up quark's charge planted as −3 for −4, the closed form breaks in all 20 cells it touches.
- **A failed run, disclosed.** A first run of the a = 0 points at heights 60, 80 and 100 used the frame's default
  30 + 2 Im τ digits.
  - Its m₁/m₃ rates on the S reading came out erratic, from 0.57 to 1.43.
  - The cause: a ratio of rate 1 is about 10^(−2.73 Im τ), which the default does not hold above height about 40.
  - The rerun at 40 + 3.5 Im τ digits settles at 1.
  - Its files were overwritten by the rerun.
  - This does not reach B1940's values. Their averaged rates are at most 0.55, within the default's reach at every
    height they use.

## 1b. The second computation (the web seat's W-F25, harvest row 1834)

- **Independent.** The web seat sealed its card W-F25 at 10:50:50 (+0100), nine seconds before this arc landed
  (10:50:59), on its own transcription of the frame, in double precision, at heights 2 to 10.
- **Its convention:** E = −(1/π) d log r / d Im τ, which is twice the rate in |q| used here.
- **It agrees** wherever it converged:
  - at the a = ±2/5 points: up (0.6, 1.0), down and leptons (0.4, 1.1), which are (3/10, 1/2) and (1/5, 11/20) here;
  - at the a = ±1/5 points: up (0.2, 1.2) on S and (0.2, 1.0) on S̃, which are (1/10, 3/5) and (1/10, 1/2);
  - the slow cells approach the values here (up S̃ 1.58 to 1.95 toward 1.6; down S̃ 1.12 to 1.31 toward 1.3);
  - the a = 0 cells sit near 1 and 1.9, which are 1/2 and 1 with their power of Im τ.
- **Its own expectations Y1 to Y3 failed as sealed,** as its card records: convergence, independence of Re τ and of the
  end, at heights the double precision reaches.
  - With B1924's constant end, which turns negative above height about 6, its exponents change. That is a property of
    that end, not of the canonical end this arc uses.

## 2. The ingredients

- **The Higgs triplet is itself hierarchical.** Its components' leading terms (the record's q-series, B1691's
  `the_exponents.py`) give

  S ≈ (1/12) q^(−1/8) E₁₂ − (i/3) q^(1/8) diag(1, −1) − (5/3) q^(3/8) E₂₁ + …

  These are three steps, each q^(1/4) apart. At leading order det S = (1/4) q^(1/4).
- **The residues' rates come from the characteristics.** Each unit's residue is a product of two theta constants over
  η³. In the up sector:
  - the d-characteristic is (½, ·) or (0, ·), for rate 1/8 or 0;
  - the unit "1" vanishes at every point, since its d-characteristic is always (½, ½).
- **B1659's determinant law holds on frame C** (`determinant_law.py`): det Y = 4 det S det M tr(εSMᵀ), with worst
  relative residual 1.8e-30 over 48 cases.
- **Each piece has a closed form.** Write D = ‖2q_L a‖/2 and E′ = ‖2q_R a‖/2. Measured at the three kinds of point:
  - the largest entry: e(Y) = D² + E′² − ¼;
  - the adjugate: e(adj Y) = 2D² + 2E′² − D − E′;
  - the matter's determinant: e(det M) = [(½ − 2D)² + (½ − 2E′)²]/2. M's leading part is nilpotent, like the Higgs's;
  - the Higgs's determinant: e(det S) = ¼.
- **The first generation is B1788's tropical rule** (`tropical_check.py`). B1788 derived it in B1656's frame from
  B1659's law. It predicts every cell of § 1, both generations, both readings: 192 cells within 1.2e-3. With the up
  quark's charge planted as −3, 80 cells break.

## 3. The average takes the minima

- **What the average does.** High in the cusp, the average over the 24 points of each ratio is set by the points with
  the smallest rate.
- **What that gives:**
  - up: m₂/m₃ falls as |q|^(1/10), from the a = ±1/5 points; m₁/m₃ as |q|^(1/2), from the a = ±2/5 points (S) or the
    a = ±1/5 and a = 0 points (S̃);
  - down: m₂/m₃ falls as |q|^(1/5); m₁/m₃ as |q|^(11/20) (S), or as |q|^(1/2) from the a = 0 points (S̃).
- **The check.** The lock checks these minima against the decay rates of B1940's own averaged file, between heights 30
  and 37, within 5e-3.
- **What is new about the pattern.** It mixes points. In the up sector on the S reading, the second generation comes
  from one pair of points and the first from another. No single census line has this pattern, so W178's skeleton
  test, which tested lines one at a time, does not cover it.

## 3b. The mixing in the cusp is a permutation at every point (agy-exp's diagnosis, recomputed)

- **Where it comes from.** agy-exp found this and the author relayed it on 2026-11-15 (harvest row 1830; its files are
  in its own scratch space, not on its branch). Main recomputed it on its own code (`cusp_mixing.py`, run at height 30).
- **The finding.**
  - At every one of the 24 points, in both reading pairs, |V| = |U_uᴴ U_d| is a permutation matrix.
  - |V₃₃| is at most 9.7e-5 there. The heaviest up quark and the heaviest down quark sit in orthogonal directions.
  - On (S̃ up, S down): the 14 points with a = 0 or ±1/5 give |V₁₃| = 1, and the 10 points with a = ±2/5 give
    |V₁₂| = |V₂₃| = 1.
  - These are B1940's averaged limits: 7/12 = 14/24, and 5/12 = 10/24.
- **Why** (§ 2's pieces): the two sectors' largest residues sit in different units.
  - **The up sector:** units j and k, since q_L − q_R = 5 ≡ 0 mod 5 makes unit 1 vanish.
  - **The down sector:** units 1 and i.
  - So the top rows come from orthogonal parts of the quaternion basis.
- **The lock** checks five points at height 30.
- **What it means.** High in the cusp, frame C's mixing is structurally wrong at every point, whatever the measure. This
  is a second, independent reason the cusp is no way out for frame C: its mixing is a permutation, not near the
  identity.
- **A related point in the record:** P-566's sector-odd singlet, a Higgs component odd between up and down, proposed
  for an earlier frame's corner inversion (B1825).

## 3c. Neither candidate level aligns the mixing (`levels_mixing.py`, data-free)

- **The question.** P-845's two levels for the leptons are order 10 (SM-C13b) and order 15 (B1942). Does either also
  align the two sectors' top rows high in the cusp?
- **No.** At height 30, |V₃₃| is small at every point of exact order, in both reading pairs:

  | order | points | largest \|V₃₃\| at height 30 |
  |---|---|---|
  | 10 | 72 | 9.7e-5 |
  | 15 | 192 | 3.5e-2 |

  Most cells are the same cyclic permutations as at order 5.
- **What it means.** The misalignment is not a property of level 5. It comes from the frame's bilinear quaternion
  contraction, which puts the up and down sectors' top residues in different units.
  - The level can separate the leptons from the down quarks, but it cannot repair the mixing.
  - The mixing needs a change of structure: agy-exp's point (d) on P-860, a shared doublet mode for the two sectors' top
    rows.
- **The lock** checks four points of order 10 and 15.

## 4. What this corrects in B1944

- **B1944 pointed to a read-out that gives the cusp its weight by a principle.** That is not open ground for this
  family.
- **What the record already holds:**
  - **the cusp, line by line:** no census line's cusp pattern passes W178's skeleton test, and the a = ±2/5 points
    here are W178's slope-2/5 lines;
  - **one τ on the order-5 lines:** B1698 found NEGATIVE as sealed, with 1.675 % of random hierarchies fitted as well
    against a 1 % bar. On those lines the leptons are the down quarks transposed, which the data's split forbids;
  - **the bulk:** B1944 found the average over the whole surface FAIL in every option.
- **What survives for this family:**
  - the structural fault, that at order 5 the leptons copy the down quarks (B1698, B1934);
  - P-845's fork of the level, order 10 or order 15 (B1942, SM-C13b), which is how the frame separates them;
  - but neither level aligns the mixing (§ 3c). That needs a change in the coupling's structure (P-860 (d)).
  - This is a question about the frame's structure, not about how to weight the surface.
- **One cusp pattern of the masses is untested:** the averaged one in § 3. Testing it would be a new look under a sealed rule
  (P-859). But the mixing there is a permutation (§ 3b), so frame C's cusp fails on structure before any comparison.

## 5. Foreknowledge, disclosed

- While planning this arc, main recalled from memory the rough size of one measured quantity: the down quarks'
  ln(m_d/m_b)/ln(m_s/m_b), about 1.8. The averaged pattern's corresponding numbers are 11/4 (S) and 5/2 (S̃).
- No comparison is banked here.
- A test of the averaged cusp pattern must count this as part of a look already made, and must be ruled before any
  value of it is compared.

## 6. The amplitude read-out needs a connection first (P-860 (a), data-free)

- **The candidate** (agy-exp's point (a)): sum frame C's coupling over the 24 points with equal weights, then take the
  SVD of the sum.
- **It is not a function on the modular surface** (`amplitude_sum.py`). Its mass ratios at τ and at τ + 1 differ, by up
  to 80 %: up S at 0.13 + 1.7i gives 0.066 against 0.119. The canonical end is the same at both, since it is read at
  Re τ mod 1. The pointwise ratios are covariant (B1928; B1940's V2), so their average is invariant, but the sum of the
  couplings is not.
- **Phases do not repair it.** Under τ → τ + 1 each point's coupling goes to another point's, changed by a unitary
  that mixes entries, not by phases alone (a scratch comparison of entrywise moduli, which differ by about 0.1).
  - So a covariant amplitude read-out needs a flat unitary connection over the 24 points, built from B1724's transport
    rules.
  - With that connection, (a) and agy-exp's (b), the Chern–Simons phases, become one question. It must be built before
    the read-out is even defined.
- **The lock** checks that the equal-weight sum changes under τ → τ + 1.

## Not claimed

- That any cusp pattern matches or fails the data. The comparison is not made here.
- Rates on columns other than x = 0.13. B1940's five-column average agrees with the minima, which is the only check
  across columns.
