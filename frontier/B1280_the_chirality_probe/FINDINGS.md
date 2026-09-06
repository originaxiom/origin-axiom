# B1280 — THE CHIRALITY PROBE, COMPLETED AND CLOSED BY TWO THEOREMS: the elliptic SL(3) components W1, W2 are vector-like on every cusped cover (their cusp-fixed curve is the branch locus of the trace coordinates, where every representation is its own dual pulled back by the period-2 isometry), and the θ-odd E₆ frame is vector-like on its whole germ (the object's inversion is the E₆ outer automorphism on the deformation space)

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (two theorems, each with an exact proof and an exact or
high-precision numerical instantiation at every step; the six signs over two primes) · **Price: unchanged** ·
**Companion:** `docs/CHIRALITY_MAP_2026-09-06.md` (the retrieval this arc was asked for)

## Why this arc

The owner asked for the record's chirality knowledge retrieved and the remaining computations run. The retrieval is
the chirality map. The record had two named, unrun computations on net chirality N(V) = h¹(M;V) − h¹(M;V\*) on the
cusped object: **(i)** B1260's deciding computation on B71's non-self-dual SL(3) components W1, W2, run at six
cusp-fixed points in `docs/EXTERNAL_VERIFICATION_2026-09-06.md` §3 (N = 0) but not on the components; **(ii)** L200,
B1268's cusp-fixed θ-odd locus, where |N(27)| = 1 was still allowed. Both are closed here — the first by finding the
structure that makes the whole component computable, the second by six signs.

## 1. The frame (B71's conventions, B1268's lemma)

m004 is the mapping torus of the once-punctured torus F = ⟨a, b⟩ with monodromy φ: a ↦ a²b, b ↦ ab; the boundary
conjugator is w = a, the genuine meridian μ = a⁻¹t, the longitude λ = [a, b]; M_n is the mapping torus of φⁿ (the
n-fold cusped cyclic cover). For V irreducible on F, the Wang sequence gives **h¹(M_n; V) = dim ker(Φⁿ − 1 | H¹(F; V))**
with dim H¹(F; V) = 3 and Φ the monodromy's action on the fibre cohomology; the three SL(3)-lifts of one PGL(3) bundle
representation (t ↦ ζt, ζ³ = 1) rescale Φ by ζ. The eigenvalues of Φ on V\* are the inverses of those on V (checked at
every point; the twisted Alexander polynomials are reciprocal), so **N(M_n; V_ζ) = Σ_{(ζe)ⁿ = 1} [gm_V(e) − gm_V\*(1/e)]**:
net chirality on any cover needs a *repeated* eigenvalue of Φ at a root of unity with unequal Jordan structure on V
and V\*, and B1268's bound puts such points where the cusp holonomy keeps a fixed vector.

## 2. THEOREM 1 — W1 and W2 are vector-like on every cusped cyclic cover

**(a) One curve for all covers.** B71 (P1) proved the Dehn-filling A-variety relations as scalar-matrix identities:
on W1, [A, B] = c μ³; on W2, [A, B] μ³ = c. The scalar is **c = 1 exactly** (|c − 1| < 2·10⁻¹⁵ at every point tested;
the non-scalar part < 10⁻⁹): **λ = μ^{±3}**. So the peripheral pair shares every eigenvector, and λv = v iff the
μ-eigenvalue of v is a cube root of unity. Hence the cusp-fixed locus {(ζμ)ⁿ v = v = λv} of *every* cover M_n and
*every* twist is the single curve

> **K = {(p, q) : μ has an eigenvalue in μ₃}**

(one twist per point puts the eigenvalue at 1; for 3 | n all three twists keep the fixed vector). Off K,
h⁰(∂M_n; V) = h⁰(∂M_n; V\*) = 0 for every n and every twist, and the bound gives N = 0.

**(b) K is the branch locus, and the other sheet is the dual pulled back by an isometry.** Lawton's presentation of
the SL(3, ℂ) character variety of F₂: nine trace generators — tr A, tr B, tr AB, tr A⁻¹, tr B⁻¹, tr A⁻¹B, tr AB⁻¹,
tr A⁻¹B⁻¹, tr [A, B] — the ninth satisfying a quadratic over the first eight whose two roots are tr [A, B] and tr [B, A].
B71's coordinates (p, q) on W1, W2 are the first eight; over each (p, q) there are **two** characters, ρ = (A, B) and
ρ′ = (Aᵀ, Bᵀ) (same eight traces, ninth trace tr [Aᵀ, Bᵀ] = tr [B, A]). And (Aᵀ, Bᵀ) = (ρ\*(a⁻¹), ρ\*(b⁻¹)): **ρ′ = τ\*ρ\*,
the dual representation pulled back by the inversion τ: a ↦ a⁻¹, b ↦ b⁻¹ of the fibre group** — the hyperelliptic
involution of the punctured torus, which commutes with the monodromy and is the object's **period-2 isometry** (B1279's
swap, cusp map (+, +), a half-translation along the longitude); it fixes t and lifts to every M_n. The two sheets
coincide where tr [A, B] = tr [B, A], i.e. tr λ = tr λ⁻¹, i.e. (by (a)) tr μ³ = tr μ⁻³, i.e. the spectrum of μ³ is
inversion-symmetric, i.e. some eigenvalue of μ³ is 1: **the branch locus is exactly K.** (This is also why Newton's
method in (p, q) stalls with a square-root law on K — (p, q) are not local coordinates there; the probe solves the
representation in matrix space instead.)

**(c) The theorem.** On K, ρ and τ\*ρ\* have the same character and, being irreducible, are conjugate: **V ≅ τ\*V\***.
τ is a homeomorphism of every M_n, so h¹(M_n; V) = h¹(M_n; τ\*V\*) = h¹(M_n; V\*): N(M_n; V) = 0 for the untwisted
representation. For a twist ζ ≠ 1: if 3 ∤ n that twist has no cusp-fixed vector on M_n and N = 0 by the bound; if 3 | n
every element of π₁(M_n) has t-exponent divisible by n, hence by 3, so V_ζ and V restrict to the *same* local system on
M_n and N(M_n; V_ζ) = N(M_n; V) = 0. With (a) off K:

> **N(M_n; V) = 0 for every representation on W1 ∪ W2, every central twist, every n ≥ 1.**

**(d) The second structure, and where a Jordan asymmetry could have lived.** On Z¹(F; V) = V ⊕ V the matrix of Φ⁻¹
is [[T⁻¹(1 + A), T⁻¹A²], [T⁻¹, T⁻¹A]] and on B¹ ≅ V it is T⁻¹, so **tr(Φ⁻¹ | H¹) = 2 tr μ⁻¹** and **det(Φ⁻¹ | H¹) =
det A = 1**. On K (twist with μv = v), Φ⁻¹ acts on H¹(∂F; V) = V/(λ − 1)V by μ⁻¹ and H¹(F; V) → H¹(∂F; V) is onto, so
Φ⁻¹ has the eigenvalue 1 and **eig Φ⁻¹ = {1, e, 1/e} with e + 1/e = 2 tr μ − 1**. Every eigenvalue is simple except
at **tr μ = 3/2** (e = 1: a triple eigenvalue 1) and **tr μ = −1/2** (e = −1: a double eigenvalue −1) — i.e. the
spectra of μ are {1, (1 ± i√15)/4} and {1, (−3 ± i√7)/4}, both unitary. The theorem predicts equal Jordan data on V
and V\* there; §4 checks it.

## 3. THEOREM 2 — the θ-odd frame is vector-like on its whole germ

**(a) The mechanism.** If σ is an isometry of M and V ≅ σ\*V\*, then h¹(M; V) = h¹(M; σ\*V\*) = h¹(M; V\*) and N(V) = 0.
For the E₆(ℂ) family through the geometric holonomy ρ₀ = (principal E₆) ∘ (Riley), the dual of 27_ρ is 27_{θρ}, θ the
outer automorphism of E₆, which fixes ρ₀ because the principal sl₂ of E₆ lies in F₄. So N(27_ρ) = 0 on the germ of
the character variety at [ρ₀] as soon as some isometry σ has **θρ ≅ σ\*ρ on the germ**. θ and σ\* are commuting
involutions of the germ fixing [ρ₀]; a finite-order automorphism of an analytic (or formal) germ that acts trivially
on the Zariski tangent space is the identity on the germ (linearisation; no smoothness needed). The Zariski tangent
space at the good point [ρ₀] is

> H¹(M; e₆) = H¹(M; V₂) ⊕ H¹(M; V₈) ⊕ H¹(M; V₁₀) ⊕ H¹(M; V₁₄) ⊕ H¹(M; V₁₆) ⊕ H¹(M; V₂₂)

(e₆ under the principal sl₂: exponents 1, 4, 5, 7, 8, 11; each h¹ = 1, computed), on which **θ = +1 on f₄ = V₂ ⊕ V₁₀ ⊕
V₁₄ ⊕ V₂₂ and −1 on the 26 = V₈ ⊕ V₁₆** (B1086/B1087's θ-odd slots hv8, hv16). **The question is six signs.**

**(b) The six signs, exact.** `verification/theta_odd_pairing.py` computes, over 𝔽_p for two primes p ≡ 1 mod 12
(everything lives in ℤ[ζ₁₂]: u = e^{iπ/3} = ζ₁₂², i = ζ₁₂³), H¹(M; Sym^n ρ₀) by Fox calculus on ⟨a, b | a w b⁻¹ w⁻¹⟩
and the action f ↦ G⁻¹ f∘σ of each orientation-preserving isometry — the inversion ι: a ↦ a⁻¹, b ↦ b⁻¹ (intertwiner
diag(i, −i)), the period-2 swap τ: a ↔ b (intertwiner [[0, u], [u², 0]]), and ιτ — with every step checked (relator,
intertwiners, invariance of Z¹ and B¹, exactly one of σ\*z ∓ z ∈ B¹):

| n | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| h¹(M; Sym^n) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 (odd n: 0) |
| ε(ι) | − | **+** | − | + | **−** | **+** | − | **+** | **−** | + | − | **+** |
| ε(τ) | + | + | + | + | + | + | + | + | + | + | + | + |
| θ on the six | | **+** | | | **−** | **+** | | **+** | **−** | | | **+** |

**ε_n(ι) = (−1)^{n/2+1}, and on the six deformation classes it is (+, −, +, +, −, +) = θ.** (n = 0 is the control:
ι inverts the meridian, so it acts by −1 on H¹(M; ℂ); τ preserves it.) The period-2 swap acts trivially on the whole
tangent space, as it must (it acts on the cusp by a translation).

**(c) The theorem.** dθ = dι\* on T_{[ρ₀]}, so θ∘ι\* is an involution of the germ with trivial tangent action, hence
the identity: **θρ ≅ ι\*ρ for every ρ on the germ of the E₆ character variety at the geometric point.** Therefore
27̄_ρ = 27_{θρ} ≅ ι\*(27_ρ) and

> **N(27_ρ) = h¹(M; 27_ρ) − h¹(M; 27̄_ρ) = 0 identically on the germ — for every θ-odd deformation, every θ-even one,
> on m004 and on every cusped cyclic cover M_n (ι preserves the kernel of π₁ → ℤ/n and lifts).**

B1268's bound |N(27)| ≤ 1 near the geometric point is sharpened to 0; the θ-odd point of B1268 §3 (N = 0 with no
cusp invariants) is one instance; **L200 is closed without finding the fixed-vector locus** — wherever it is, N = 0
on it. The frame that "works" (E65's successor: the 27 complex, closure e₆) is complex but cohomologically paired by
the object's own inversion. This is the same mechanism as Theorem 1 (τ on K) and as Alexander reciprocity
(ι\*ℂ_t = ℂ_{1/t} = ℂ_t\*): **the object's isometries pair every non-self-dual system it supplies with its dual.**

**(d) Beyond the geometric germ: the criterion at every other sl₂ point (`verification/mod4_criterion_other_sl2.py`, exact).**
The six signs are universal: ε_n(ι) = (−1)^{n/2+1} depends only on n, not on where Sym^n sits in e₆ (and the swap acts
by +1). So at any sl₂-embedded point (sl₂ → E₆) ∘ Riley the question becomes root-system combinatorics: an isometry
realises the outer involution θ′ fixing the triple on the Zariski tangent space H¹(M; e₆) = ⊕ H¹(M; V_n) iff **every
summand of θ′'s fixed algebra has n ≡ 2 (mod 4) and every summand of its −1 part has n ≡ 0 (mod 4)** (the mod-4
criterion; for a trivial summand ε₀ = −1). For the nine even nilpotent orbits of E₆ (weighted Dynkin diagrams with labels
in {0, 2}) the fixed algebra is read off the roots (f₄, when the triple is σ-invariant) or from the sp(8)-type
involution (the fixed part Sym²(W), the −1 part Λ⁴₀(W) for a nilpotent partition of sp(8), when it is not); the twelve
odd-labelled orbits, whose decompositions also carry Sym^odd summands (h¹ = 0: no deformation classes), are not
tabulated here — their even summands obey the same criterion (L207):

| orbit | e₆ under the sl₂ | tangent dim | θ′'s fixed algebra / −1 part | criterion |
|---|---|---|---|---|
| **E₆ (principal — the geometric point)** | V₂ V₈ V₁₀ V₁₄ V₁₆ V₂₂ | 6 | f₄ = V₂ V₁₀ V₁₄ V₂₂ / 26 = V₈ V₁₆ | **TRUE** |
| **E₆(a₁) (subregular — B1256's I-25 point)** | V₂ V₄ V₆ V₈ V₁₀ V₁₀ V₁₄ V₁₆ | 8 | the triple is not in any f₄; it is the principal sl₂ of an sp(8): sp(8) = V₂ V₆ V₁₀ V₁₄ / 42 = V₄ V₈ V₁₀ V₁₆ | FALSE — **exactly one unpaired direction, the V₁₀ of the 42** (θ′ = −1, ι\* = +1) |
| D₅ | V₀ V₂ V₄ V₄ V₆ V₈ V₁₀ V₁₀ V₁₀ V₁₄ | 10 | f₄ = V₂ V₄ V₆ V₁₀ V₁₀ V₁₄ / 26 = V₀ V₄ V₈ V₁₀ | FALSE (V₄ in f₄, V₁₀ in the 26) |
| E₆(a₃) | V₂³ V₄³ V₆² V₈² V₁₀² | 12 | f₄-type or sp(8)-type ([6,2]) | FALSE both ways |
| D₄, A₄, D₄(a₁), 2A₂, A₂ | (with trivial summands) | 18, 18, 20, 30, 36 | f₄-type, and sp(8)-type where it exists | FALSE (trivial summands in the fixed algebra, ε₀ = −1, among others) |

**The geometric point is the unique sl₂ point at which the object's isometries realise the E₆ duality on the deformation
space.** (Rigorous as a germ statement at the three distinguished orbits E₆, E₆(a₁), E₆(a₃), where the triple's
centralizer is finite; at the others it is the tangent-level statement.) At the subregular point — the embedding
B1256 singled out as the one assumption-free three-chiral typing (27 = 13 + 9 + 5) — the θ-odd deformation in the
V₁₀ ⊂ 42 direction is NOT paired by any holomorphic isometry (ι, τ, ιτ all act by +1 on it while θ′ acts by −1): it is
the first place on this object where the θ-odd frame's net chirality is not forced to vanish by symmetry, and it remains
bounded by B1268 (|N| ≤ h⁰(∂M; 27) there). That is L207's computation, now exactly located.

## 4. The numerical instantiation (`verification/chirality_probe_w1w2.py`; run record `chirality_probe_w1w2_run.txt`)

- **(a) Validation.** The geometric Sym² point (eig Φ⁻¹ = {4.79, 1, 0.21}, h¹(M_n) = 1 for all n, N = 0); Wang =
  direct Fox calculus on M₁, M₂, M₃ at six generic W1/W2 points; eigenvalue reciprocity; |tr Φ⁻¹ − 2 tr μ⁻¹| and
  |det Φ⁻¹ − 1| < 10⁻⁹; c = 1 to 10⁻¹⁵; the transpose sheet has the same eight traces (10⁻¹⁶) and a different ninth
  (|tr[A,B] − tr[B,A]| = 2.4 … 9.4) off K.
- **(b) The curve K.** Solved in matrix space (unknowns A's eigenvalues, B, T, p, q; equations the eight traces, det,
  gauge, the monodromy relations, det T = 1, det(μ − 1) = 0, p = p₀) at three values of p₀ on each component: **18
  points**, residuals ≤ 10⁻¹⁵. At every one: eig Φ⁻¹ = {1, e, 1/e} to 10⁻¹⁵ with e + 1/e = 2 tr μ − 1; tr[A,B] =
  tr[B,A] to 10⁻¹⁵ (the branch locus); **one** character over (p, q) (two at a generic point off K — the control);
  h⁰(∂M₁; V) = h⁰(∂M₁; V\*) = 1 at exactly one twist; h¹(M_n; V) = 1 for n = 1..9 at that twist; **N = 0 for every
  n ≤ 9 and every twist.** (The six points of `EXTERNAL_VERIFICATION` §3 are points of K.)
- **(c) The repeated-eigenvalue points.** tr μ = tr μ⁻¹ = 3/2 and −1/2 solved from many random starts on each
  component; the number of distinct bundle characters found for *random* targets (the generic fibre count of
  (p, q) ↦ (tr μ, tr μ⁻¹)) is the completeness control. Found — **on W1: the generic fibre has 2 points, and each case has exactly 2 (a conjugate pair, complete):** case A at
  p = 1/8 ∓ i√31/8, q = p̄ (to 10⁻⁸), μ-spectrum {1, (1 ± i√15)/4}, **Φ⁻¹ a single Jordan block of size 3 at the eigenvalue 1
  on V and on V\*** ((am, gm) = (3, 1) both; singular values [2.4, 0.9, 10⁻¹⁶] and [1.2, 0.5, 10⁻¹⁶]), h¹(M_n; V) = h¹(M_n; V\*) = 1
  for every n ≤ 9; case B at p = (−7 ∓ 5i√7)/8, q = p̄ (to 10⁻⁸; the chirality field ℚ(√−7) of B316, unbidden),
  μ-spectrum {1, (−3 ± i√7)/4}, **a Jordan block of size 2 at −1 on both** ((2, 1) and (2, 1)), h¹(M_n; V) = h¹(M_n; V\*) = 2
  for even n and 1 for odd n. **On W2 the same: generic fibre 2, each case exactly 2 points, at the same coordinate values (W2's (p, q) = (tr A, tr A⁻¹)
  and W1's (tr B⁻¹, tr B) — the two components are the generator swap of each other), the same Jordan types ((3, 1) at 1
  in case A, (2, 1) at −1 in case B, on V and on V\*), the same h¹'s.** Eight points in all, four per component. At every point: the Jordan data (algebraic,
  geometric multiplicity) of Φ⁻¹ at the repeated eigenvalue agree on V and V\* (singular values printed in the run
  record), h⁰(∂M_n) = 1 at the fixed-vector twist, **Wang = direct Fox for n = 1..9 on V and V\***, and **N = 0 for
  every n ≤ 9 and every twist.**
- **(d) Verdict.** max |N| over everything: **0.** `SELFTEST: PASS` (1300 s).

## 5. Ledger

- Two named computations closed: B1260's deciding computation (now a theorem on the components), L200 (now a
  theorem on the germ). The record's every N is zero, and for the sectors it supplies, by mechanism.
- I-26 unchanged (UNEARNED): the quantity it would read is zero wherever the record has a representation.
- Open, registered as L207: the subregular germ's one unpaired θ-odd direction (the V₁₀ of the 42) — B1268's cusp-fixed
  computation, now with the point and the direction named; the rank ≥ 4 sector; the general theorem.
- Values: 0 of 19; chirality N = 0; price unchanged.

## Controls (MB12, both directions)

- Theorem 1's ingredients are each checked where they could fail: c = 1 (not just c³ = 1); the transpose sheet's
  eight traces equal and ninth different off K (so the two-sheet structure is real); one character over (p, q) on K
  and two off it; the {1, e, 1/e} structure at 18 points; the repeated-eigenvalue points found with a fibre-count
  control and their Jordan data compared on V and V\*; Wang against Fox at every one for n ≤ 9.
- Theorem 2's six signs are computed exactly over two primes that agree row by row; the n = 0 row (−1: the meridian
  inverted) and the τ rows (+1 throughout) are the positive and negative controls; the relator, both intertwiners,
  and the invariance of Z¹ and B¹ are asserted at every n.
- A tolerance artifact caught by the Fox control and removed: with a kernel threshold of 10⁻³ relative to ‖Φ⁻¹‖, the
  Wang count at one W1 point (‖Φ⁻¹‖ ≈ 17, a Jordan block at −1) reported h¹(M₉; V) = 2 against Fox's 1 and a spurious
  N ≠ 0 — for a non-normal matrix σ_min(Φ⁻¹ − ω) at two ninth roots of unity dips to 1.6·10⁻², under that threshold,
  while the true kernel sits at 10⁻¹⁶. The kernel tolerance is now 10⁻⁸ relative (five orders of margin on each
  side) and separate from the eigenvalue-proximity tolerance; every Wang count agrees with Fox.
- The criterion of §3(d) is checked by its positive control (the geometric point returns exactly the six signs of
  §3(b)) and its consistency: the subregular's sp(8)-type split is the unique nilpotent partition of sp(8) whose
  Sym²(W) ⊕ Λ⁴₀(W) reproduces the E₆(a₁) decomposition; the dimension count alone would have allowed three splits.
- Both theorems predict what the earlier computations found (N = 0 at the six W1/W2 points and at B1268's θ-odd
  point) and nothing else; no value, identification or price moves.

## Verification

`verification/theta_odd_pairing.py` (~7 s; `SELFTEST: PASS`; run record `theta_odd_pairing_run.txt`).
`verification/mod4_criterion_other_sl2.py` (< 1 s; `SELFTEST: PASS`; run record `mod4_criterion_other_sl2_run.txt`).
`verification/chirality_probe_w1w2.py` (~22 min; `SELFTEST: PASS`; run record `chirality_probe_w1w2_run.txt`). Lock:
`tests/test_b1280_the_chirality_probe.py` (the six signs and the identities fast; the full probe slow-marked). Feeds
on: B71 (W1, W2, the scalar identities, `peripheral.py`), B102 (the dichotomy), B1260 (the walls and the deciding
computation), B1268 (the lemma and the bound; L200), B1279 (the isometries as automorphisms), B1086/B1087 (the θ-odd
slots), B576/B582 (the θ-odd frame), B1256 (the sl₂ embeddings). Literature: Lawton, *Generators, relations and
symmetries in pairs of 3×3 unimodular matrices* (J. Algebra 2007) — the nine trace generators and the ninth's
quadratic; Falbel–Guilloux–Koseleff–Rouillier–Thistlethwaite and Heusener–Muñoz–Porti — the components; Kirk–
Livingston — duality of twisted Alexander polynomials; Cartan — linearisation of finite group actions on germs.
Registers no identification change.
