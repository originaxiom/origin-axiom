# B629 — THE SEALED INTERACTION-LAYER VALUES (the interaction round's value bank)

**Sealed 2026-07-15. SHA-256 of this file goes into
frontier/B598_l85_campaign/ARTIFACT_HASHES.txt at banking, BEFORE any
comparison design exists. Computed by four independent value-only cells
(no cell saw any measured mixing value; the running cell used measured
couplings as RGE *inputs* per its task and compared nothing). Scope per
the interaction-round directive: exactly ONE comparison is authorized
downstream (§1 vs the PMNS moduli table, under a separately sealed
design); §2–§4 are sealed as values/targets and are NOT-FOR-COMPARISON
pending their own preregistrations.**

## §1 The E₆₂ 3×3 odd hearing form B (the authorized comparison's framework side)

Construction: exactly B594's (weld B = Uᵀ·Cm·ρ(A1)·U on the three θ-odd
pairs (27,27̄), (351′,351̄′), (351,351̄) of E₆ level 2), rebuilt at 100-digit
working precision with exact integer W(E₆)/root data; every gate residual
≤ 2e-100. Reproducer: `hp_hearing.py`.

**Closed form (new, exact at working precision):** with
A_k = (2/√7)·sin(2πk/7) and ζ = e^{iπ/7} (so B lives in ℚ(ζ₁₄, √7) ⊂ ℚ(ζ₂₈)):

    B = [ A₁ζ¹⁰   A₂ζ⁶   A₃ζ⁴  ]
        [ A₂ζ²    A₃ζ⁵   A₁ζ³  ]
        [ A₃ζ¹²   A₁ζ¹   A₂ζ⁶  ]

The A-index pattern is the Latin square [[1,2,3],[2,3,1],[3,1,2]]: each
amplitude appears once per row and once per column.

**Verified gates (all banked values reproduced):** trace(B) = −1 exactly;
diagonal = −(the banked sine-kernel amplitudes) for 27, 351′, 351;
B is EXACTLY UNITARY (BB† = B†B = I); eigenvalues exactly {i, −i, −1}
(charpoly (x+1)(x²+1), so B⁴ = I, order 4); B² Hermitian with real
diagonal (−A₂, −A₁, +A₃).

**The moduli-squared table (the sealed framework matrix for the one
authorized comparison), 50 digits:**

    |B|² row0: 0.34929169541608982979682930414194135984753016250416
               0.54313396225783403606745780557355572890454833203767
               0.10757434232607613413571289028450291124792150545817
    |B|² row1: 0.54313396225783403606745780557355572890454833203767
               0.10757434232607613413571289028450291124792150545817
               0.34929169541608982979682930414194135984753016250416
    |B|² row2: 0.10757434232607613413571289028450291124792150545817
               0.34929169541608982979682930414194135984753016250416
               0.54313396225783403606745780557355572890454833203767

i.e. |B_ij|² = A_{k(i,j)}² with A₁² = (4/7)sin²(2π/7),
A₂² = (4/7)sin²(4π/7), A₃² = (4/7)sin²(6π/7); A₁²+A₂²+A₃² = 1 exactly.
Because B is unitary, |B_ij|² is exactly doubly stochastic (all row and
column sums = 1).

**THE CIRCULANT DISCLOSURE (held-out accounting, stated at sealing):**
|B_ij|² is a circulant — every row/column is a permutation of the SAME
three moduli, and those three scalars are precisely B615's A3–A5 (one of
which, A₂² ≈ 0.5431, was one of B615's three coarse-tier angle matches).
The off-diagonal entries' PHASES are new numbers, but moduli-squared
kills them. What is genuinely held out in the matrix comparison is
therefore the JOINT STRUCTURE — the Latin-square arrangement and the
matrix-to-matrix geometry (which value sits in which slot against the
measured table), NOT nine virgin scalars. The framework matrix has 2
free real parameters (A₁², A₂² with the third determined), arranged in a
fixed circulant pattern. The null model in the sealed design must be a
matrix-level null (Haar), which accounts for this automatically.

**The eigenframe (basis-canonical; eigenvalues non-degenerate):**
eigenvalues (−i, +i, −1); |V_ij|² (columns ordered (−i, +i, −1)):

    row0: 0.72233966614520537373966535469464941367095436134359
          0.14614844840458374742937779880793563530982888944201
          0.13151188545021087883095684649741495101921674921440
    row1: 0.26953765421745664392782397746541374455152191258539
          0.52596687003559511880114888153427615967204749718968
          0.20449547574694823727102714100031009577643059022493
    row2: 0.00812267963733798233251066783993684177752372607103
          0.32788468155982113376947331965778820501812361336831
          0.66399263880284088389801601250227495320435266056067

The SVD frame is NOT canonical (B unitary ⇒ all singular values = 1
identically; any orthonormal frame is a valid SVD frame) — recorded so
no future arc mistakes an algorithm artifact for structure. The
eigenframe |V_ij|² is sealed HERE as a value; it is NOT part of the one
authorized comparison (adding it would double the look-elsewhere; any
future test of it needs its own preregistration).

## §2 The golden 2×2 frame at κ=5, and the κ=10 correction (values; NOT-FOR-COMPARISON)

Construction: exactly B601's odd_form() on SU(3) level k=2 (κ=5), rebuilt
at 80-digit precision. Reproducer: `exact_hearing.py`.

**B_odd(κ=5) closed form (off-diagonals new, never before published):**

    B_odd = [ 1/(2φ) + i·sin(2π/5)/√5     −φ/2 − i·sin(π/5)/√5 ]
            [ φ/2 − i·sin(π/5)/√5          1/(2φ) − i·sin(2π/5)/√5 ]

Exactly unitary; det = 1; trace = 1/φ (the banked trace law);
eigenvalues exactly e^{±2πi/5} (the banked golden pair).

**The frame angle (exact):** the eigenvector mixing angle satisfies
tan(θ_frame) = 1/φ EXACTLY; θ_frame = arctan(1/φ) =
0.55357435889704525150853273008926852003502382270072 rad
= 31.717474411461005324213903139773352664397892850177°;
|V₁₁|² = cos²θ_frame = (5+√5)/10; |V₂₁|² = sin²θ_frame = (5−√5)/10.

**The structural identity:** |V₂₁|² = |h₃|² = (5−√5)/10 — the frame's
mixing weight EQUALS the hearing amplitude's modulus². Consequence for
held-out accounting: sin²θ_frame is numerically IDENTICAL to B615's A1
(already tested, null at both tiers); the frame angle therefore adds NO
new comparable scalar and is excluded from comparison on that ground —
sealed here as structure only.

**The κ=10 correction:** the task premise "8×8" was WRONG — dim_odd at
κ=10 (SU(3) k=7) is 16 (the sequence is 2,4,6,9,12,16,20,… for k=2..8;
no k gives 8). The true 16×16 B_odd(κ=10) is also exactly unitary;
trace = 1/φ (trace law); all 16 eigenvalues unimodular in 8 conjugate
pairs at arguments ±{18°,24°,54°,72°,96°,126°,144°,162°} (all multiples
of 6° — 60th-root clockwork); EXACTLY ONE pair is e^{±2πi/5} — the
κ=5 golden pair recurs as a genuine 2-dim eigenspace, but delocalized
over 10 of the 16 pair-directions with golden-rational weights (e.g.
(5±√5)/100); the raw 2×2 submatrix on the κ=5 pair-directions is NOT
golden (eigenvalue moduli² ≈ 1.43e-5, 0.0550; not a conjugate pair) —
consistent with B601's banked naive-test defect.

## §3 The composite inventory (cell L; SEALED, NOT-FOR-COMPARISON — deferred per the directive's point 3)

~40 exact values: the four |A|² (h₃ and the three E₆₂ amplitudes), the
Rosetta-fraction-weighted products f_class·|A|² for the V4/V8 shallow
lines (su3 = 1/2 both; su2 = 2/29 (V4), 8/25 (V8); mult = 25/58 (V4),
9/50 (V8)) and top lines (pure multiplet-q, su3/su2 projections exactly
0), the cross-layer products {1/5, 1/49}×{fractions}, and the ratios
29/4 (V4), 25/16 (V8). Full table with exact radical forms and 30-digit
decimals: `composites.py` / `composites2.py` output, recorded in
FINDINGS.md. These are frozen NOW so any future preregistration cannot
tune them; comparing them requires a structural derivation of WHICH
composition ↔ WHICH observable, stated before any distance is computed.

## §4 The object-scale coupling targets (cell M; SEALED TARGETS, NOT-FOR-COMPARISON — deferred per the directive's point 2)

Measured-derived: PDG 2024 M_Z inputs (α₁ = (5/3)α_Y = 0.0169434946,
α₂ = 0.0338011066, α₃ = 0.118) run by pure-SM gauge RGEs (1-loop
b = (41/10, −19/6, −7); standard gauge-only 2-loop matrix; no
thresholds; RK4 cross-checked vs RK45 at rtol 1e-12) to the declared
scales Λ_A = 3.8597e14 GeV (= |τ₈|/|τ₄|·GeV, declared before running),
Λ_B = 3.520e16 GeV, μ_ref = 1e16 GeV. Frozen 2-loop values at Λ_A:
1/α₁ = 39.83460291, 1/α₂ = 43.95914437, 1/α₃ = 41.27201275,
sin²θ_W = 0.398360534; at Λ_B: 1/α₁ = 36.86882881, 1/α₂ = 46.20925869,
1/α₃ = 46.3265441, sin²θ_W = 0.4292254757; at μ_ref: 1/α₁ = 37.69573286,
1/α₂ = 45.5816094, 1/α₃ = 44.91746102 (1-loop values in
`run_sm_rge.py` output). Comparing anything to these requires a NEW
sealed design with the principled scale argument stated first — the
directive's re-testing bar. Frozen now so that design, if ever written,
cannot move the targets.

## MB12 (computed at sealing)

- Non-trivial: the closed-form B (Latin square, exact unitarity), the
  off-diagonal golden entries, θ_frame, the κ=10 16×16 facts, and the
  |V₂₁|² = |h₃|² identity are all NEW (never banked); the |B_ij|² table
  as a MATRIX was never sealed anywhere.
- The one authorized downstream comparison can PASS and can FAIL: a
  circulant from {0.349, 0.543, 0.108} may or may not sit near a
  measured doubly-stochastic table under a matrix-level null — both
  outcomes are live (the discriminating computation is the sealed
  design's Monte Carlo, not this file).
- The known hazards are disclosed IN this file (the circulant/held-out
  accounting; the sin²θ_frame ≡ A1 identity; the SVD artifact), not
  discovered after.
