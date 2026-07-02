# B367 (W2.3) — the value-map s(m₁,m₂): PRE-REGISTRATION (written before computing)

**Campaign W2.3. Two-outcome. This document is committed BEFORE any value-map computation runs.**

## Step 0 — the exact six-pair s-matrices, matched labels (the reconciliation substrate)

Construction (declared): for each pair (m₁,m₂) ∈ {1,2,3,4}², m₁<m₂, compute the full s-matrix
s(k₁,k₂) = the √−15 coefficient of the H-projected `tr(Par·P_{k₁}·Q_{k₂})`, where P_k/Q_k are the exact
eigenprojectors of ρ₁₅(W_{m₁})/ρ₁₅(W_{m₂}) onto eigenvalue exp(2πik/ord) (Lagrange interpolation in the
ℚ(ζ₆₀) integer engine — the B358 machinery; no PSLQ, no floats in the readout; exact solve in
H = span{1,√5,√−3,√−15}). Labels = ascending exponent lists (cross-seat convention):
K1=K4=[0,1,4,5,6,9,11,14,15,16,19] (ord 20), K2=[0,1,2,3,4,5,7,8,9,10,11] (ord 12), K3=[0,1,2,4,5] (ord 6).

Pre-registered step-0 checks (each pass/fail):
- S0.1 Every row and column sums exactly to 0 (forced by ΣQ=I; both seats verified samples).
- S0.2 Pair (1,2): the 8 cross-seat entries reproduce exactly: (0,4)=+1/48, (0,7)=−1/48, (3,1)=+1/120,
  (3,5)=−1/480, (3,8)=−1/160, (8,3)=−1/160, (8,6)=+1/120, (8,10)=−1/480.
- S0.3 Pair (2,3): the six ±1/144 entries reproduce at their labels; PREDICTION: the previously
  height-blocked entries contain ±1/288-type values (from my banked ±1/288 blocks) — or the block↔label
  map explains the split with no new values. Which of the two resolves is recorded.
- S0.4 Pairs (1,3), (1,4): identically zero at FULL identification (upgrades the zeros to exact-tier), or
  the first nonzero entry is reported with its label.
- S0.5 Pair (2,4): full table; consistency with my banked block values {±1/120,±1/240,±1/480} under
  block-summation; (3,4): full table (was 19/55, 2 entries ±1/48).
- S0.6 The 11×11 (1,2) structure claims (received, unverified): rank = 4; antisymmetry under k₂ ↦ 12−k₂
  (exactly: s(k₁, 12−k₂) = −s(k₁,k₂) on K2); three disjoint K1-support sectors {0,4}·{exponent-pair A}·
  {exponent-pair C} with the {0,4} sector carrying max |s| = 1/48. Each verified exactly or refuted.
- S0.7 Aggregates Σs² per pair against the cross-seat values: 7/6400 (1,2) · 1/3456 (2,3) · 1/19200 (2,4) ·
  1/1152 (3,4) — noting theirs were partial-coverage, so equality is NOT required, only ≥ (identified
  subsets); the exact aggregates are new data.

## The value-map hypothesis (the actual W2.3 target), pre-registered

**H-form (the local-symbol ansatz):** every nonzero entry factors as
    s(k₁,k₂; m₁,m₂) = ε · 2^{−a} · 3^{−b} · 5^{−c}
with ε ∈ {±1}, and the exponents (a,b,c) and the support pattern determined by LOCAL data of the two seeds
at p ∈ {3,5} plus the exponent labels: the ellipticity type of tr = m²+2 mod p (the B361 local law gives
the support gate), the eigenvalue exponents k_i mod the p-parts of the orders, and Hilbert-symbol-type signs
(κ_i, κ_j)_p with κ = m²+4. Concretely testable sub-claims:
- V1 (denominators): every |s| is of the form 2^a·3^b·5^c in the denominator with a ≤ 5, b ≤ 2, c ≤ 1
  (all observed values 1/48,1/80,1/120,1/144,1/160,1/240,1/288,1/480 satisfy this).
- V2 (support): the bright/dark pattern per pair follows the banked local law (elliptic at BOTH primes for
  at least one seed with partner requirement) — already banked; the value map must REFINE, not re-derive.
- V3 (the map): there exists a single formula, uniform in (m₁,m₂), expressing s at declared complexity:
  a product of at most 4 local factors, each depending only on (seed data mod 3, mod 5, k-labels).
  Search space declared FINITE and enumerated in the probe (no post-hoc extensions).

**Null (MB8/MB12, declared before computing):** generate 200 random tables with the SAME support pattern,
sign-balance, and denominator profile (2^a·3^b·5^c pool) as the true six-pair data; run the identical
V3 search on each. The value-map claim survives only if the true data admits a V3 formula AND fewer than
5% of the random tables do (the target can fail; vacuity check passes by construction).

**Held-out verification (declared now):** the V3 search runs on pairs {(1,2),(2,3),(2,4),(3,4)} ONLY.
Any found formula must then PREDICT, zero-parameter: (i) the (1,3) and (1,4) zeros; (ii) the full s-matrix
of the NEW pair (2,7) — computed banked-blind in B362's lineage but never entered in the fit — and (iii) a
genuinely new pair (3,7) re-derived at matched labels. A formula that fits the training pairs and misses
the held-outs is REFUTED, recorded, and the table banks as a table.

**Outcomes (two, both bank):** (A) a local-symbol closed form passes training + null + held-outs ⇒ the
value-boundary claim upgrades one tier (the first forced dimensionless relations of the program — still
firewalled MATH, promotion decision deferred to adversarial review); (B) no formula at declared complexity
⇒ the exact six-pair table + the sharpened structure (S0 results) bank as the channel's exhibit, and the
value-map lead closes at this complexity budget (label: open at higher complexity, not "impossible").

MB guards: MB12 (the null defines failure), MB8 (random-table baseline), exact-first arithmetic throughout,
atlas + FAILURE_ATLAS consulted (no prior value-map probe exists; the numerology fence K020/PMNS lesson
applies to any dictionary talk — none is licensed by this probe).
