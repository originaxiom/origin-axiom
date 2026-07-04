# PAPER 1 — the theorem spine (precise statements + proof sketches, lock-backed)

Setup: level N = 15; W_m = WR^m D^m the theta-lift Weil matrix (D = diag ζ₁₅^{j(j−1)/2},
WR = F D⁻¹ F⁻¹), Par the parity operator, X/Z the Heisenberg generators, t(a,b) =
tr(Par·P_a·Q_b) the parity-inserted pair invariants (P_a,Q_b the eigenprojectors of W₁,W₂),
H = ℚ(√5,√−3), s(a,b) = the √−15 component ("the seam"). All arithmetic exact in ℚ(ζ₆₀).

**Theorem 1 (the order law, all N).** ord(W₁ at level N) = π(N)/2, the half Pisano period;
equivalently the tower is the quantized golden cat map A=[[2,1],[1,1]]. Verified N=15,45,75,
135,225. [frame: Hannay–Berry / Kurlberg–Rudnick, cited] [lock: test_b376/P59]

**Theorem 2 (the twist invariant).** The theta lift and the canonical lift are inequivalent
(exhaustive intertwiner search empty); Par commutes with the entire canonical image (⇒ the
canonical seam is identically 0) but not with the theta image, where Par−J is the Weyl step
(J=ζ₆⁻¹XZ); the twist is exactly the half-characteristic diagonal cocycle ζ₁₅^{−j(j+1)/2}.
Hence seam ≠ 0 ⟺ the quantization carries the twist. [lock: test_b381/P62]

**Theorem 3 (the shifted trace formula & the 1/12).** On the domain det(γ−I)∈(ℤ/15)ˣ,
    tr(U_γ·XᵃZᵇ) = tr(U_γ)·ζ₁₅^{ ½ω(v,(γ−I)⁻¹v) − ½ab − ½ω(v,(1,1)) },
the twist entering as the single half-characteristic term −½ω(v,(1,1)); the whole Par-table
factorizes through the formula (661/661 over all six banked pairs); the slot constant is
−(φ/6)√−3 = (0,0,−1/12,−1/12), and its det-class decomposition is 1/12 = 1/16 (generic) +
1/48 (5-boundary), with magnitudes |χ|²=#Fix(γ′). [lock: test_b382, test_b396/P64]

**Theorem 4 (the closed form).** C[j,l] = C₃[j,l]·C₅[j,l] on all 240 cells at the multiplier
(u₃,u₅)=(2,2); the class partials assemble as two-branch products of the 3-side ℤ₄×ℤ₄ table
and 5-side parity-branch constants, reproducing −1/16 and −1/48 exactly; the golden boundary
couples equal parities only. [lock: test_b386/P66]

**Theorem 5 (locality of brightness).** For every banked pair the s-classification (√−15
channel) is reproduced from the two LOCAL theta models (q=3,5) alone via spectral
convolution (12/12: seven bright, five dark); predictive out-of-sample (pair (2,5) called
dark from local data, verified). [lock: test_b390/P67]

**Theorem 6 (existence law, general N).** The value sector at N=3^a·5^b exists iff NOT (a
even AND b even): doublets at odd prime powers only (3-side 90°; 5-side 36°/108° by QR
class), lines on the inert 3-side always / ramified 5-side even powers only. Predictive at
nine sub-verdicts (375,405,675) + census-confirmed at 243,625. [lock: test_b377_*/P63]

**Theorem 7 (the root-of-unity gate).** Every det-class-1 cell of the generic Par-table is a
root of unity in μ₆₀ (142/142); the orders are genus-character-gated: 3 | ord(C) ⟺
χ₋₃(det(γ′−I)) = −1 (the Eisenstein gate; ⇒ the cell-wise ℚ(√5)-reality where χ₋₃=+1), and
χ₅(det)=−1 forces 5|ord one-directionally. [lock: test_b404/P68]

**Theorem 8 (row-16 reality).** t(16,b) ∈ ℚ(√5) for all b (finite exact verification); the
√−3/√−15 components vanish across the whole row, by a zero of the anti-table's ζ₅-spectrum
at the 16-exponent. [lock: test_b383/P65]

**Theorem 9 (Galois covariance).** σ₃₁-invariance t(31a,31b)=t(a,b) on all six tables; the
full-vector mirror t(a,−b)=τ₃(t(a,b)); the rigid-sector reduction t(a,b)=⟨v_a|u_b⟩⟨u_b|Par|
v_a⟩/(‖v_a‖²‖u_b‖²). [lock: test_b379, test_b380/P60,P61]

**Theorem 10 (the class-field organization).** H is the Hilbert class field of ℚ(√−15); the
ℤ/2 class group acts on the banked value constants (slot ↔ −(3-block); the two ±1/24 faces
form one orbit); the component basis {1,√5,√−3,√−15} is the Gauss-sum basis of the three
genus characters; two genus selection rules (the Eisenstein gate; the boundary
equipartition). [lock: test_b401]

**Theorem 11 (the boundary theorems / the walls).** (no scale) every internal channel
contracts, the tower-measure is flat; (no frame) the golden and ℤ/3 sectors are exactly
orthogonal under both ℤ/3 and ℤ/2. The object emits only dimensionless quantities and
self-provides no canonical frame — structural theorems, no physics. [lock: test_b408,
test_b413, test_b400, test_b422]
