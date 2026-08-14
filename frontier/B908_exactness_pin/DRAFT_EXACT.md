# B908 LEG 3 — THE EXACT CERTIFICATE: I = −1, no height bound

Computation agent, 2026-08-05. Script `leg3_exact.py` (single file, ~18 s),
results `leg3_exact_results.json`. Route **(a) direct** — the nine colorless
atom lines built exactly in characteristic 0, the banked cubic restricted to
them, all six couplings and I computed exactly. Everything asserted below is
an exact identity (Fractions / exact mod-p integers); numerics (mpmath) were
used only to *guess* candidates that are then accepted solely on exact
verification.

## 1. Why route (a) became direct: the tower falls out of the atoms

The registered route (b) wanted the sl₃⊕sl₃ stabilizer over K = ℚ[ρ]/μ₁₃.
While building the eigenline solves the sharper fact appeared, and it
trivializes the problem:

> **The four pipeline torus generators R8, R14, R16, R22 on the 27 are
> rational matrices that commute exactly over ℚ** (verified: all six
> commutators vanish identically). For every labeling,
> span{X1, Ym, W3, R14} = span{R8, R14, R16, R22} whenever g·a ≠ 0
> (X1 = R8 + rR16, Ym = gR14 − aR16, W3 = bR16 − gR22 — solve back for
> R16, R8, R22). So every joint eigenline of the twelve labeling operators is
> a joint eigenline of ONE rational commuting family — **the tower values
> (r, g, a, b) and the b12 tower field never enter the atom lines.**

Mod-p recon confirmed it first: at all 7 primes, all 9 banked colorless atoms
are componentwise eigenlines of each of the four rational operators (252/252
checks). Phase-K's earlier interpolation failure is explained: it interpolated
eigenvalues of the *pipeline combos* (which do involve g, a, b and live in the
degree-12 tower field), not of the rational family.

## 2. The exact spectral geography

charpoly(Mc), Mc = 3R8 + 7R14 + 13R16 + 17R22, computed and factored exactly
over ℚ:

- **h_S** = x³ − 535623511707648·x − 2928461724187049852928 (mult 1) — the
  three S-atoms: ONE Galois orbit; disc(h_S) has squarefree part 77 =
  squarefree part of disc(μ₁₃); the root x_S(ρ) ∈ K is exhibited and verified.
- **h_A** (sextic, lc 19⁶ = 47045881, mult 1) — the six non-S colorless
  atoms: ONE orbit of six. Its discriminant is negative (squarefree part −3):
  the six eigenvalues are complex, so they do NOT lie in the (totally real)
  splitting field N of μ₁₃. This is the two-non-S-rows-swap in disguise (and
  why c_row1 = c_row2 held at every prime).
- a sextic of multiplicity 3 — the colored sector; untouched here.

Rational invariant blocks: W3 = ker h_S(Mc) (dim 3), W6 = ker h_A(Mc)
(dim 6), both exactly invariant under Mc, Me = 3R8+13R16, Mo = 7R14+17R22.
Structure found and verified exactly:

- **Mo|W3 = 0**: the S-atoms have λ14 = λ22 = 0 exactly (a rational-eigenvalue
  block — the task's CHECK is answered in this precise form).
- char(Me|W6) = g², g cubic, with root **α(ρ) ∈ K** and **α = −x_S/2 exactly**
  (per column, the three colorless eigenvalues of Me sum to zero — the
  zero-sum certificates' character-0 face).
- char(Mo|W6) = even polynomial; its cubic-in-x² has root **B(ρ) ∈ K**; per
  column j the non-S pair has Mo-eigenvalues ±β_j, β_j² = B(r_j).

## 3. The hidden sign correlation: one global √−3

A first computation in the "uncorrelated" ring N[b₁,b₂,b₃]/(b_j² − B(r_j))
(dimension 48) produced support on ALL EIGHT one-atom-per-column sign
patterns — too many: the banked support has exactly two (the non-S rows). So
the three square roots must be correlated. The correlation is total:

> **B(ρ) = −3·w(ρ)² with w ∈ K, exhibited and verified exactly**
> (w = (−73438908480/247, −40696614604800/169, 2177455129952256000/41743)).
> Hence β_j = w(r_j)·τ for ONE global τ = √−3: the entire colorless
> configuration is defined over **M̄ = N(√−3), degree 12**, and the only
> residual choice is the sign of τ, whose flip swaps the two non-S rows.

The −3 of disc(h_A) and the field ℚ(√−3) — the program's atom field — is
where the colorless square-root correlation lives. (Flagged as an
observation; nothing here leans on it.)

## 4. The certificates (all exact)

1. R8, R14, R16, R22 commute over ℚ and are exact derivations of the banked
   45-monomial ±1 cubic (checked on all monomials).
2. Nine explicit nonzero vectors over M̄ (S_j = σ_j(v_S); A_j^± = σ_j(u) ±
   τ·σ_j(w·w̃), from 1-dimensional kernels over K and K(β), free coordinate
   exactly 1 — the nonvanishing certificate survives every ring hom since the
   rational block bases have rational left inverses) are **joint eigenlines
   of all four operators**: componentwise proportionality on all 351
   coordinate pairs, per operator, per atom.
3. **Identification**: at each of the 7 full-tower primes, all 12 embeddings
   M̄ → F_p send the nine exact lines onto the nine banked atom lines
   (projective match). Mod-p simplicity of the nine Mc-eigenvalues (rank 26)
   pins uniqueness: any characteristic-0 construction whose reduction is the
   banked state has THESE lines.
4. **Support**: the restricted cubic vanishes IDENTICALLY in M̄ on all 159
   non-coupling multisets and is nonzero exactly on the six banked couplings.
   This upgrades the zero-sum-certificate argument (DRAFT_LEG3 §2) to an
   unconditional characteristic-0 identity.
5. **The pin**: v = P_R + P_C = 0 exactly, and
   **I = P_R / P_C = −1 exactly** in M̄. I is atom-scaling gauge-free (each
   atom sits in exactly one row and one column coupling), so this is THE
   value of the invariant. No height bound, no CRT, no reconstruction.

In the script's gauge the couplings come out with closed forms worth
recording (gauge-dependent, unlike I):

- c_S = **−disc(μ₁₃)** = −557339020487762273068236197068800 exactly;
- the two non-S row couplings are **equal integers**
  1685950536975480876031414496133120000 (the 7-prime equality c_row1 = c_row2
  was real — forced by the τ-flip Galois symmetry — while the leg-2 CRT
  candidate value for them was spurious, as suspected: true atom entry
  heights run to 10²² against a 7-prime bound of ~10¹⁶);
- the three column couplings are K-conjugates (τ-free, in σ_j(K)), with
  rational product P_C = −P_R.

## 5. What this closes and what remains

DRAFT_LEG3 §6 "what remains for full exactness":

1. the char-0 det-type certificate — **CLOSED, strengthened**: instead of
   exhibiting the stabilizer, the couplings themselves are exact and I = −1
   outright. The sl₃⊕sl₃ statement follows as a corollary: with I = −1 a
   det-frame rescaling exists over a quadratic extension of M̄, conjugating
   the restricted cubic to the det pattern, whose stabilizer is the proven
   16-dimensional sl₃⊕sl₃ (theory anchor 2/T, exact over ℚ).
2. the brute-CRT alternative — moot (and its near-bound reconstructions are
   now known to have been unreliable except where forced by symmetry).
3. the standing leg-1 reduction assumption — reduced to pure naming: the
   exhibited configuration is unconditional characteristic-0 fact, matched to
   the banked states at 7 primes × 12 embeddings; "the pipeline's char-0
   atoms are these" needs only that the pipeline reduces correctly at ONE of
   the seven primes (simplicity does the rest).

Honest inventory of find-vs-verify: sympy charpoly/factor and mpmath
root-guessing sit on the FIND side only; every accepted object (roots in K,
w, kernels, eigenlines, support, couplings, I) is accepted on re-verified
exact identities computed by the script's own Fraction arithmetic. The b12
tower coefficients were never needed. The K₃,₃/Galois symmetry lemma of the
DESIGN is not needed for the verdict either — I = −1 is computed, not
argued.

## Files

`leg3_exact.py` (this certificate, self-contained; env: SESSION_SCRATCH,
SESSION_SCRATCH_RUN), `leg3_exact_results.json` (verdict + all check flags +
exact K-data), alongside the mod-p machinery `leg3_mechanism.py` and the
seven state pickles it reads.
