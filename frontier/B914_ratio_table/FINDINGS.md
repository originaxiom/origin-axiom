# B914 — R2′ the signed skeleton + R3′ the colorless-first ratio table: THE TABLE IS ONE NUMBER — all six normalization-free couplings are EXACTLY EQUAL; the H-unit gauge is the determinant gauge

Computation agent, 2026-08-05. Script `ratio_table.py` (single file, ~52 s with
the cached B854 base), results `results.json` (51/51 checks PASS). Per the
register amendment (masterplan 2026-08-05): R2′ = the signed skeleton, R3′ =
the colorless-first ratio table; the colored sector enters ONLY through the
B913-sealed magnitude |det Gram|^{1/3} with mandatory (1,2,0) signature tags —
no other magnitude appears anywhere in this cell. Gate 5: structure only; no
experimental number enters or is compared.

## 0. The basis reconciliation (the cell's critical step — done exactly, not patched)

The task's danger point: B908's exact atom lines live in the solo handoff
realization, which B912 proved is a **27̄** (weight multiset = negatives of
B883's); B912's H and the banked scales live on the **banked B883 27**. Mixing
them would be a basis error. Resolution: the entire B908 route-(a) exact
construction was **re-run on the banked B883 27** — same rational commuting
charge family R₈, R₁₄, R₁₆, R₂₂ (from the B854 invariants; commutation
re-verified exactly), same tower K = ℚ[ρ]/μ₁₃ → N (splitting algebra, deg 6)
→ M̄ = N(τ), τ² = −3 — so the nine colorless lines, the couplings, AND the
H-norms are all computed **on the same exact vectors in the same coordinates**.
No dps-60/exact mixing occurs anywhere in T; every T entry is an exact element
of the real field N. Certificates:

- the banked H₊ (B912's integer ±1 signed permutation) re-verified: symmetric,
  and **RₙᵀH + εₙHRₙ = 0 exactly** for the four charges, ε = (−1,+1,−1,+1);
- the invariant cubic re-solved exactly on the B883 27: 45 weight-zero
  triples, equivariance kernel **dim 1**, integer-primitive, coefficients ±1,
  and the **derivation identity verified exactly for all 78 generators**
  (B884's banked summary made explicit; triples+coeffs now recorded in
  `results.json`);
- charpoly(Mc) = h_S·h_A·h_col³ with h_S the exact **mirror x ↦ −x of B908's
  handoff h_S** — the 27̄ relation seen in the spectra, as predicted;
  Mo|W3 = 0, α = −x_S/2, **B = −3w²** (the global √−3 correlation) all
  reproduce on this side;
- the nine exact atoms are joint eigenlines of all four operators
  (componentwise proportionality in M̄, all pairs); they are **exactly
  H-orthogonal pairwise** (upgrading B912's < 10⁻⁴⁵ numerics to identities on
  the colorless nine), with H-values qᵢ ∈ N, all nonzero, and D = H₊⁻¹H₋ acts
  as +1 on every colorless line exactly (σ± give the same table);
- numeric reconciliation at dps 80: the embedded exact lines coincide with
  fresh eigen-atoms line-for-line (worst distance 4.4×10⁻⁷³, atom residuals
  ≤ 3.8×10⁻⁶⁶), and the exact Rayleigh scales reproduce **all nine banked
  B912 scales to their full stored 35 digits** (worst rel. diff 1.16×10⁻³⁵);
- on the same exact vectors: support = exactly the two pencils (159/165
  multisets vanish identically in M̄), the non-S row couplings are equal
  integers, the column couplings τ-free K-conjugates, and **P_R + P_C = 0,
  I = −1 exactly in this realization too** — the B908 verdict is
  realization-independent. Bonus: in this gauge c_S = −disc(μ₁₃) and the
  non-S row integer are **identical** to B908's handoff-gauge values (the
  mirror realization lands in the same normal form).

## 1. R3′ — the ratio table: T is ONE number (the headline)

For each lll coupling t = (i,j,k), on the SAME exact basis vectors uᵢ whose
H-norms define the scales (H in the banked normalization: Rayleigh value +1 on
the frame-2 vacuum line):

> T_t := |c_t|² / (sᵢ sⱼ sₖ)

T is invariant under any per-atom complex rescaling (c picks up λᵢλⱼλₖ, the
same-vector H-norms pick up |λ|² per slot), so the unit-vector route gives the
same number — verified as an EXACT identity (`T_gauge_invariance_...`), i.e.
the banked B912 unit-vector scales and these T are one consistent frame.

**THE RESULT (exact, in N):**

> **T(S0,S1,S2) = T(A0m,A1m,A2m) = T(A0p,A1p,A2p) = T(A0m,A0p,S0)
> = T(A1m,A1p,S1) = T(A2m,A2p,S2) — ALL SIX ARE EQUAL, as one exact
> identity in N. Every one of the 15 pairwise ratios is the exact
> rational 1.**

The single value is an explicit degree-3 algebraic number, T = σ₂(t_K) with
t_K ∈ K exhibited (coordinates in `results.json`), minimal polynomial
certified by exact linear algebra in N (coefficients in `results.json`,
lc ≈ 3.309×10²⁰¹ — 202 digits, deg 3):

> T = 4.775781328852112587377582312996804957776592668646×10⁻³² (50 digits)
> √T = |c| on H-unit atom vectors = 2.185356110306078373488497108665608×10⁻¹⁶

- Row products = column products = T³ = 1.0892643747900423×10⁻⁹⁴, and the
  consistency gate **∏(rows T) = ∏(cols T) holds exactly** (= I² = 1, as
  required; asserted independently of the equality).
- T is **canonical**: the cubic is the banked integer-primitive ±1 form
  (unique up to sign, and T = |c|² kills the sign) and T is invariant under
  the one-real-scale freedom of H (r_ref³ cancels against the qᵢ) — the only
  convention inside T is B912's *choice of which vacuum line* is the
  normalization line (frame 2, banked).

**Independent verification (no shared machinery):** a second route using the
numeric unit eigenvectors (mp.eig at dps 80, residual-certified), the numeric
H, and the numeric cubic — different vectors, different gauge, different
arithmetic — reproduces the banked scales (1.16×10⁻³⁵), finds the six T equal
with spread 1.05×10⁻⁸⁰, and matches the exact T to 9.2×10⁻⁷⁶. The task's
40-digit certification bar is exceeded by ~35 digits, and no exact/dps mixing
was ever needed.

## 2. The honest analysis: forced vs new

A priori the table has 6 numbers. Banked symmetry forces exactly two
relations BEFORE this cell:

1. **T(row m) = T(row p)** — the τ-flip (global √−3 conjugation) swaps the
   two non-S rows; H is real; the pair scales are equal (B912) and the row
   couplings equal (B908). FORCED.
2. **∏(rows T) = ∏(cols T)** — this is I² = 1 with I = −1 (B908). FORCED.

So 4 degrees of freedom remained. The computation finds THREE further,
UNFORCED identities — the cell's new information:

3. **T(S-row) = T(non-S rows)** — nothing banked relates the S-line coupling
   c_S = −disc(μ₁₃) to the non-S orbit; their T-equality is new.
4. **T(col 0) = T(col 1) = T(col 2)** (two relations) — the three column T's
   are the three K-conjugates σⱼ(Y)·r_ref³ of one K-element; Galois only
   forces their PRODUCT rational. (Sharper: for conjugates, pairwise-RATIONAL
   ratios already force ratio 1 — a ∈ ℚ with the 3-cycle gives a³ = 1 — so
   "rational" and "equal" coincide here; either way it is not banked
   symmetry.) NEW.

**New-information count: 3 unforced exact identities + 1 exact algebraic
number (T, deg 3, = σ₂(t_K), t_K ∈ K explicit).** The normalization-free
content of the entire colorless coupling grid collapses to a single number.

**The reading (fenced, one step):** B908 proved the sign pattern is the
determinant's (rows +, columns −, the Leibniz sign, stabilizer sl₃⊕sl₃).
B914 now proves the MAGNITUDES also agree: on H-orthonormal atom vectors all
six couplings share one magnitude √T. Together: **the canonical Hermitian
structure H (the norm cell) and the invariant cubic (the coupling cell) are
exactly compatible — the H-unit gauge IS the det gauge**, and the entire
colorless flavor cube is det(3×3) times one canonical constant. The two
independently-banked structures meet in a single number; that they CAN (that
the 4 remaining dof close to 1) was not guaranteed by anything banked.

## 3. R2′ — the signed skeleton

The 3×3 colorless grid (rows/cols = the two banked pencils; every colorless
atom positive-definite, sign +1 after the banked normalization; scales exact,
50 digits in `results.json`, reconciled to B912's banked 35-digit values):

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| **S row** | S0 = atom 14 (vacuum, frame 0), **s = 1.6803202716…**, + | S1 = atom 9 (vacuum, frame 1), **s = 19.1420207439…**, + | S2 = atom 0 (vacuum, frame 2), **s = 1** (the normalization line), + |
| **m row** | A0m = atom 3, **s = 53.0786384386…**, + | A1m = atom 8, **s = 0.7862600340…**, + | A2m = atom 13, **s = 3.0889357198…**, + |
| **p row** | A0p = atom 4, **s = 53.0786384386…**, + | A1p = atom 7, **s = 0.7862600340…**, + | A2p = atom 12, **s = 3.0889357198…**, + |

(atom numbers = B912's indices; pencils in B912 indices: rows
[[14,9,0],[3,8,13],[4,7,12]], cols [[3,4,14],[8,7,9],[13,12,0]]. Every column
= one S atom + one conjugate pair — the K-embedding σⱼ; the m/p rows are
swapped by the τ-flip.)

The six colored atoms (B913-sealed magnitudes, mandatory tags — recorded as
banked, NOT as scales): pairs (1,2): |det Gram|^{1/3} = 1867.6882465…,
(1,2,0) each; (5,6): 702.4634612…, (1,2,0) each; (10,11): 451.7161785…,
(1,2,0) each.

**The perfect matching** (computed here from the full 680-multiset support
scan in the B883 realization; 17 couplings reproduce the banked probeC count,
margin: smallest coupling 6.8×10⁻¹⁶ vs largest zero 5.7×10⁻⁶², a gap of
10⁴⁶): the 9 ccl couplings each contain EXACTLY ONE colorless atom, and the
nine colorless atoms are hit bijectively — a perfect matching {colored pair}
↔ {colorless atom}, annotated with the sealed magnitudes and tags:

| colored pair (magnitude, tags) | ↔ colorless atom (scale, sign) |
|---|---|
| (10,11) — 451.72, (1,2,0)² | atom 0 = S2, vacuum frame 2 (s = 1, +) |
| (5,6) — 702.46, (1,2,0)² | atom 9 = S1, vacuum frame 1 (s = 19.142, +) |
| (1,2) — 1867.69, (1,2,0)² | atom 14 = S0, vacuum frame 0 (s = 1.680, +) |
| (1,11) — 1867.69/451.72 | atom 7 = A1p (s = 0.786, +) |
| (2,10) — 1867.69/451.72 | atom 8 = A1m (s = 0.786, +) |
| (1,6) — 1867.69/702.46 | atom 13 = A2m (s = 3.089, +) |
| (2,5) — 1867.69/702.46 | atom 12 = A2p (s = 3.089, +) |
| (5,11) — 702.46/451.72 | atom 3 = A0m (s = 53.079, +) |
| (6,10) — 702.46/451.72 | atom 4 = A0p (s = 53.079, +) |

Structure read off the matching (all conjugation-consistent, the pairs swap
under 1↔2, 5↔6, 10↔11): the three **conjugate** colored pairs couple to the
three **vacuum lines**; the six **opposite-chirality cross pairs** couple to
the six non-S colorless atoms. The remaining 2 couplings are ccc: (1,5,10)
and (2,6,11) — the two **same-chirality colored transversals** (one atom from
each pair, swapped by conjugation). 6 lll + 9 ccl + 2 ccc = 17.

## 4. Honest scope and precision

- **Exact (identities in ℚ, K, N, M̄):** the charge family, H's charge
  equivariance, the cubic (kernel dim 1 + all-78 derivation), the nine atom
  lines, their joint-eigenline and pairwise H-orthogonality certificates,
  qᵢ, nᵢ, the scales as elements of N, the six couplings, the support
  (159 identical zeros), P_R + P_C = 0, I = −1, all six T, all 15 ratios
  (= 1), the row/col products, the gate, T's minimal polynomial, t_K.
- **dps-certified numerics:** the eigen-atom cross-check (residuals
  ≤ 3.8×10⁻⁶⁶, line distance ≤ 4.4×10⁻⁷³ at dps 80); the banked-scale
  reconciliation (limited by B912's stored 35 digits: 1.16×10⁻³⁵); the
  independent T route (spread 1.05×10⁻⁸⁰, vs exact 9.2×10⁻⁷⁶); the colored
  support scan (dps 50, gap 10⁴⁶ — the support pattern is also banked via
  probeC/B906, reproduced here in the B883 realization).
- The colored sector enters descriptively only (B913 seal respected: the
  |det|^{1/3} magnitudes + (1,2,0) tags, nothing else, and no colored RATIO
  is defined or used — colorless-first per the register amendment).
- The matching table is the computed coupling-support structure; the banked
  probeC "perfect matching" phrase is hereby given its explicit form on this
  build (bijection certified by the scan's margins).
- Conventions carried: B912's frame-2 vacuum normalization (banked); the
  cubic's sign convention (first weight-zero triple = +1; T is sign-blind);
  the exact-atom names Sj/Aj± are internal to this cell's embedding labels —
  the bridge to B912's atom indices is computed and banked in
  `results.json["match_exact_name_to_B912_atom"]`.
- Gate 5: these are STRUCTURE ratios of the object. No experimental number
  was compared, and none appears in this arc. R4 remains sealed.

## Files

`ratio_table.py` (everything above, 51 checks) → `results.json` (the full
exact record: cubic triples/coeffs, q/n/T coordinates in N, t_K, minimal
polynomials, the grid, the matching, all margins), this draft. Env:
SESSION_SCRATCH optional (isolated B854 exec + cache); repo paths relative.

## Depends on

B912 (H, scales, atom indices, D), B913 (the sealed colored magnitude), B908
(the exact route + I = −1 + the gauge constants), B906 (the atoms, the grid,
probeC's 17), B889 (frames/vacuum lines), B884 (the cubic's banked summary),
B883 (the 27), B854 (the charge invariants).


## Banking-seat verification (cc, 2026-08-05)

The shipped script re-run at banking (all checks pass on the rerun); the four
locks in `tests/test_b914_table.py` pin: 51/51 checks, the one-number collapse
(all six T equal at the certified 50 digits, all pairwise ratios exactly 1),
T's degree-3 minimal polynomial, the 35-digit scale reconciliation against
B912's banked values, c_S/(−disc μ) = 1 and the 27̄ mirror relation. The
LAW_MAP-worthy sub-lemmas (the all-equal-T identity; the exact colorless
H-orthogonality) are flagged for the next promotion pass per working rule 10.
R3′'s colorless deliverable is COMPLETE: the table is the single algebraic
number T, and the colored sector enters only as the B913-sealed
signature-tagged magnitudes. The ladder now stands one rung from the crossing;
R4's timing is the owner's call, per the register.
