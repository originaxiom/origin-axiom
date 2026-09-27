# B1386 — THE OPEN EISENSTEIN CUSP: one level above B1385's nearest miss, m004's class contains a member whose Eisenstein cusps no symmetry closes. It is cube~3.24, a degree-9 cover of o10_150725: chiral, four cusps, isometry group D₃. Its only cuspidal Higgs class v₊ is also its only class fixed by every isometry, so neither parity applies. A new congruence (L4: where an order-3 isometry rotates a cusp, χ(∂⁺) ≡ the number of its fixed points in ∂⁺, mod 3) gives N(v₊) ≡ ±1 (mod 3). So N(v₊) ≠ 0 whenever the harmonic form's first Fourier coefficient at the Eisenstein cusp is non-zero at a non-degenerate phase. By the same congruence N(v₊) ≠ ±3: this class cannot carry three generations (a cover can triple it, which is the record's open one-versus-three question, not a derivation).

> **Currency (2026-09-27, B1387): T2's hypothesis is discharged.** v₊'s L² harmonic form, computed by a Hejhal-type solve,
> has a non-zero first coefficient at both Eisenstein cusps (|c|·√covol = 1.00695) with triple phase cosine 0.370, so χ = −1 at
> each. Cusps 1 and 2 are annular. **N(v₊) = ±2, computed** (not certified). The cheap three of sL-7 is excluded for this member.
> `frontier/B1387_the_index_computed`.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** sL-6, registered by B1385 — "a member of m004's
class with a rotated hexagonal free cusp whose invariant class no isometry negates" · **Status:** PROVED (L4; the member's symmetry
data, exact) · COMPUTED (the search, 183 covers; B1370's shells; the controls) · CONDITIONAL (N(v₊) ≠ 0 rests on one analytic
coefficient, B1370's kind of residual) · **Fence:** the seat's frame (B1351 (ii), B1368–B1370, B1385), the spin-0 half only; the
partition is the sign of the leading cusp mode (B1370 §1), the convention R23 scopes · **Price:** unchanged, 0 of 19 ·
**Numbering:** B1386.

## 0. Seen from above

B1385 ended with an address and no occupant. In the seat's frame the ingredient m004 withholds is a free cusp whose partition is
disc-type. Inside m004's own class the Eisenstein face can supply it: at a hexagonal free cusp rotated by an order-3 isometry, an
invariant Higgs class has a leading cusp mode that is never annular (L1). Every such cusp B1385 met was closed by a symmetry negating
the class (L3). Its nearest miss, ocube06_08812, was open at each of two cusps and closed by a swap of the pair.

This arc searches one level up: all 183 covers of ocube06_08812 of degree 2 and 3.
- 18 carry a rotated cusp (1 double, 17 triple), in 8 isometry classes. Seven classes close: in six an isometry negates the
  invariant classes, in one the cusp's own mirrors do.
- **One class stays open: cube~3.24** (≅ cube~3.80 ≅ cube~3.105). It has 90 tetrahedra, volume exactly 45·vol(m004),
  H₁ = ℤ/3 ⊕ ℤ/3 ⊕ ℤ/9 ⊕ ℤ⁵ and four cusps, three of them hexagonal. Its isometry group is D₃, all six orientation-preserving, so the
  member is chiral.

On it:
1. **The class.** An order-3 isometry R rotates cusps 0 and 3 and translates cusps 1 and 2. Its invariant classes V = H¹(M)^R form a
   3-dimensional space. The three swaps of cusps 0 and 3 act on V with eigenvalues +1, −1, −1, and the +1 line is spanned by v₊. It
   is at once:
   - the only class every isometry fixes;
   - the only class vanishing on all four cusps, the cuspidal line (b₁ − #cusps = 1).

   No isometry negates it, so neither B1369's parity nor L3 applies.
2. **The modes.** B1370's instrument, unchanged, puts the leading allowed shell of v₊ at:
   - cusps 0 and 3: the first hexagonal shell, one rotation orbit. L1 applies: χ = ±1.
   - cusp 1: one direction. The partition is annular: χ = 0.
   - cusp 2: the √3-shell, three directions: χ ∈ {0, ±3}.
3. **The congruence (L4).** Let an order-3 isometry fix the class. Then χ(∂⁺_c) ≡ #(Fix R ∩ ∂⁺_c) (mod 3) at a cusp it rotates,
   and ≡ 0 at a cusp it translates. The swap carries cusp 0 onto cusp 3, so N(v₊) ≡ #(Fix R ∩ ∂⁺₀) (mod 3).
   - On the first shell the three fixed points carry the values 3|c| cos(φ + 2πm/3), which sum to zero. So ∂⁺₀ contains one or
     two of them, and **N(v₊) ≡ ±1 (mod 3)**.
   - From the leading shells at all four cusps, N(v₊) ∈ {±1, ±2, ±5}. Sampled over the allowed coefficients it is never 0.

What this settles and what it does not:
- **sL-6's gate is passed.** This is the record's first symmetry-protected chiral index: in the seat's frame, for the spin-0 half,
  inside m004's class.
- **It is conditional on one analytic number**: the harmonic form's first Fourier coefficient at cusp 0, which must be non-zero
  and at a phase off six values. That is B1370's residual in kind. Here the class is cuspidal, so the number is a Fourier
  coefficient of a weight-2 cusp form for an arithmetic group commensurable with PSL(2, O₃).
- **It is not three generations.** N(v₊) ∉ 3ℤ. A degree-3 cover triples it, but such a three is B1384's cover-resolution question
  (sL-5), not a derivation. The shapes are registered as sL-7.
- The spin-½ half (B1372, B1373) and the Standard-Model conditions are untouched. 0 of 19.

## 1. Where to look, and why there

- **B1385's target.** A member of m004's class with a free hexagonal cusp that an order-3 isometry rotates, whose rotation quotient
  has b₁ > 0, and whose invariant class no isometry negates.
- **B1385's ε analysis.** On o10_150725 every isometry acts on the rotation-invariant class by ε = (orientation) × (cusp-swap), and
  every cover searched inherited an isometry with ε = −1.
- **The nearest miss.** ocube06_08812, o10_150725's degree-3 cyclic cover no. 4, is chiral, and its two Eisenstein cusps are open
  one at a time. It fails only because nine orientation-preserving swaps negate its one invariant class.
- **Why its covers.** A cover can keep the rotation, lose the negating swaps, and acquire new cohomology. m004's own covers are the
  wrong place: main's S13 (dcd53824) finds hexagonal cusps on 14 of m004's 87 covers to degree 10, but an isometry rotating one on
  none. B1385's census located the rotation on o10_150725, another member of the class.

## 2. Computed

`verification/eisenstein_search.py` runs S1: the rotation filter, B1385's Eisenstein analysis on every rotation-carrying cover (B1369's
instrument unchanged), and the isometry classes. Record `eisenstein_search_run.txt`, about an hour in four parallel parts.
`verification/the_open_cusp.py` runs S2–S4 and L4's controls. Record `the_open_cusp_run.txt`, about ten minutes.
`verification/cube3_24.isosig` is the member's decorated isomorphism signature.

**S1 — the search** (ocube06_08812's covers, degree 2 and 3; cusp maps of order 3: det 1, trace −1; order 6: det 1, trace 1):

| covers | rotated cusps | isometry class | cusps, b₁, \|Isom\| | dim V at the rotation cusps | closed by | open |
|---|---|---|---|---|---|---|
| degree 2: 7 | ~2.1 | — | 5, 5, 36 (chiral) | 1 (four cusps) | an isometry negating V (L3) | no |
| degree 3: 176 | ~3.27, 3.55, 3.60 | one | 5, 5, 18 (chiral) | 1 (two cusps) | L3 | no |
| | ~3.81, 3.128, 3.156 | one | 5, 9, 18 (chiral) | 1 (two) | L3 | no |
| | ~3.102, 3.139, 3.167 | one | 5, 5, 18 (chiral) | 1 (two) | L3 | no |
| | ~3.33 | — | 9, 9, 216 (amphichiral) | 1 (six) | the cusps' mirrors (B1369) and L3 | no |
| | ~3.93 | — | 8, 10, 18 (chiral) | 2 (six) | L3 | no |
| | ~3.28, 3.82, 3.103 | one | 4, 6, 6 (chiral) | 2 (two) | L3 | no |
| | **~3.24, 3.80, 3.105** | **one** | **4, 5, 6 (chiral)** | **3 (cusps 0 and 3)** | **nothing** | **yes** |

Every instrument run used the cover's own triangulation. It is geometric and has exactly |Isom| automorphisms, so it realises the
whole isometry group. The transfer lemma (L2) was asserted on every rotation cusp.

**S2 — the member (SnapPy).** cube~3.24 is o10_150725 → covers(3)[4] (= ocube06_08812) → covers(3)[24]. Checks:
- the covering path's decorated signature equals the stored one;
- 90 tetrahedra, all positively oriented;
- volume / vol(m004) = 45 at SnapPy's high precision (difference below 10⁻⁶⁰);
- H₁ = ℤ/3 ⊕ ℤ/3 ⊕ ℤ/9 ⊕ ℤ⁵; four cusps of shapes ω, √3 i, ω, ω;
- symmetry group D₃, not amphichiral; the cusps rotated by an isometry are 0 and 3.

**S3 — the classes** (B1369's instrument, exact, on H¹(M; ℚ) in its H-basis):

| item | result |
|---|---|
| the six isometries | identity and R^{±1}, fixing every cusp; three involutions swapping cusps 0 and 3 and fixing 1 and 2; **all orientation-preserving** |
| V = H¹(M)^R | dimension 3; inside ann(P₀) ∩ ann(P₃) (L2), not inside ann(P₁) or ann(P₂) |
| the swaps on V | eigenvalues +1, −1, −1 (each of the three) |
| H¹(M)^{Isom} | dimension 1, spanned by v₊ = (1, −1, −1, 0, −2) |
| the cuspidal line ∩_c ann(P_c) | dimension 1 (b₁ − #cusps, half-lives-half-dies), **equal to ⟨v₊⟩** |
| isometries negating v₊ | **none**; every isometry fixes v₊ |

**S4 — the modes of v₊** (B1370's instrument unchanged: cusps developed from the shapes, affine actions with translation parts, the
allowed shells; norms relative to the first shell):

| cusp | lattice | fixers (sign on v₊) | R acts by | allowed shells: \|k\|² (vectors, directions, real dim) | leading | χ(∂⁺) |
|---|---|---|---|---|---|---|
| 0 | hexagonal | 3 (+1) | rotation, fixed points (⁷⁄₉, ¹¹⁄₁₈), (¹⁄₉, ¹⁷⁄₁₈), (⁴⁄₉, ⁵⁄₁₈) | 1 (6, 3, 2), 3 (6, 3, 2), 4 (6, 3, 2), 7 (12, 6, 4), … | **first shell, one rotation orbit** | ±1 (L1) |
| 1 | τ = √3 i | 6 (+1) | translation (0, ⅓) | 1 **killed**, 3 (2, 1, 1), 4 killed, 7 killed, 9 (2, 1, 1), 12 (6, 3, 3), … | one direction | 0 (annular) |
| 2 | hexagonal | 6 (+1) | translation (⅔, ⅓) | 1 **killed**, 3 (6, 3, 3), 4 killed, 7 killed, 9 (6, 3, 3), 12 (6, 3, 3), … | the √3-shell | 0 or ±3 |
| 3 | hexagonal | 3 (+1) | rotation, the same three fixed points | as cusp 0 | first shell | = χ₀ (the swap) |

- The fixers' linear parts are R^{±1} (order 3) and the identity at cusps 0 and 3, and I (three times: the identity and R^{±1})
  and −I (three times: the swaps) at cusps 1 and 2.
- The translation parts have teeth. At cusps 1 and 2, R's translation of order 3 kills every shell whose vectors pair
  non-integrally with it, the first shell included. The swaps (−I with a translation) impose a phase condition that halves every
  surviving shell.
- The L4 controls, the index sampling and the grid cross-checks are reported in `the_open_cusp_run.txt` and summarised under L4
  below.

## 3. The statements

**Lemma L4 (the fixed-point congruence).** Let M be a cusped hyperbolic 3-manifold, ω the harmonic representative of a Higgs class,
and R an orientation-preserving isometry of order 3 with R*[ω] = [ω]. Suppose the partition is regular on every cusp torus where the
sector is cusp-fixed: the zero set of the leading mode is a union of smooth curves avoiding the fixed points of R. Then:
1. If R fixes cusp c and acts on T_c with a linear part of order 3, then R has exactly three fixed points on T_c and
   χ(∂⁺_c) ≡ #(Fix R ∩ ∂⁺_c) (mod 3).
2. If R fixes c and acts on T_c by a translation, χ(∂⁺_c) ≡ 0 (mod 3).
3. If R permutes three cusps cyclically, their three contributions are equal.

Hence **N = −χ(∂⁺M) ≡ −Σ_{c rotated by R} #(Fix R ∩ ∂⁺_c) (mod 3).**

The congruence is the classical χ(X) ≡ χ(X^{ℤ/p}) (mod p) for a ℤ/p action, applied to X = ∂⁺_c. What is new here is its use on
the cusp partition, where it turns the rotation's three fixed points into a statement about the chiral index.

*Proof.*
- The harmonic representative is natural, so R*ω = ω. R has finite order, so it preserves the cusp heights. It therefore carries
  the partition at c onto the partition at R(c), which gives 3.
- At a cusp R fixes, R acts on the compact surface ∂⁺_c. By regularity its fixed points lie in the interior of ∂⁺_c or of ∂⁻_c.
  Riemann–Hurwitz for ∂⁺_c → ∂⁺_c/⟨R⟩ gives χ(∂⁺_c) = 3χ(∂⁺_c/⟨R⟩) − 2·#(Fix R ∩ ∂⁺_c) ≡ #(Fix R ∩ ∂⁺_c) (mod 3).
- A translation acts freely, so χ(∂⁺_c) = 3χ(∂⁺_c/⟨R⟩), which gives 2.
- An element A of order 3 in SL(2, ℤ) satisfies A² + A + I = 0, so det(I − A) = 3: three fixed points on the torus. ∎

*Two remarks.*
- **Fixed points are extrema.** At a fixed point of R an invariant field has zero gradient, since a rotation of order 3 fixes no
  vector. Its Hessian commutes with the rotation, so in Euclidean coordinates it is scalar. Every fixed point is therefore a local
  maximum or minimum, never a saddle. On the first shell (L1) they are the three extrema.
- **The same count in the bulk.** The chiral count is a signed count of zeros of the Higgs form (B1351's relative Euler
  characteristic). Zeros off the fixed set of R come in R-orbits of three with equal index. On a fixed geodesic of R, ω = f ds and the
  local potential h is harmonic. Its Hessian at a zero is diag(f′, −f′/2, −f′/2): symmetric, commuting with the rotation, trace-free.
  So each zero is a critical point of Morse index 1 or 2, and the zeros along each fixed line are counted by the signs of ω at its
  two cusp ends. N mod 3 is thus carried by the Higgs zeros on the rotation axes.

*Controls* (`the_open_cusp.py`). χ(∂⁺) is computed by the Morse count as primary: every critical point is found by Newton, seeded
at the fixed points and refined until the count is complete. The triangulated grid of B1385 S7 is the cross-check wherever every
critical value is at least 10⁻² of the maximum away from zero.
- *On the model torus.* 60 random fields averaged over the rotation and 60 averaged over a translation of order 3 all satisfy the
  congruence, and the grid agrees with the Morse count on all 108 resolved samples. All residues occur, including #Fix ∈ {0, 3}
  with χ ∈ {0, ±3}. So the congruence is the content and not an artefact of small numbers.
- *On the member's own invariant fields.* 1440 samples: 120 at each cusp for each of three kinds (the leading shell, four allowed
  shells, three allowed shells after the first). The congruence holds on all 1439 regular samples. One sample, at cusp 3, has a
  critical value within 10⁻⁶ of zero; it is not regular, so it is excluded and counted. The grid agrees wherever the partition is
  resolved.
- *The leading shells.* χ₀ = ±1 (62 and 58 of 120), exactly matching two or one fixed points in ∂⁺₀. At cusp 2, χ₂ ∈ {−3, 0, 3}
  (21, 81, 18); at cusp 1, χ₁ = 0 throughout.
- *The index.* 200 joint samples of the leading shells give N(v₊) ∈ {−5, −2, −1, 1, 2, 5} (15, 62, 12, 13, 82, 16), never 0, with
  N ≡ χ₀ (mod 3) in every one.
- *Without the first shell.* Cusp 0 then has #Fix ∈ {0, 3} in 47 of 120 samples (cusp 3: 72 of 119). So T2's hypothesis on the
  first coefficient is needed.
- *The history of the control.* The first run used the grid alone at n = 150. It returned 2 failures in 1440, and both were
  resolution failures:
  - one had an R-orbit of three saddles at 0.0023 of the maximum, resolved correctly from n = 300;
  - the other had an R-orbit of saddles exactly on the zero level, a non-regular partition outside the lemma.

  That is why the Morse count is primary.

**Theorem T1 (the open Eisenstein cusp).** cube~3.24 is a member of m004's commensurability class. It is a degree-9 cover of
o10_150725, which is in B1186's family. Its isometry group is D₃ and acts on H¹(M; ℚ) as in S3. In particular:
1. H¹(M; ℚ)^{Isom(M)} = ⟨v₊⟩ is the cuspidal line.
2. No isometry negates v₊, so B1369's parity and L3 are both silent on every cusp.
3. The order-3 isometry R rotates the hexagonal cusps 0 and 3, where the leading allowed shell of v₊ is the first shell, one
   rotation orbit (B1370's instrument), and translates cusps 1 and 2 by elements of order 3.

*Proof:* the computations S2–S4, exact on homology and on the isometry group's action. The cusp development and the shells are
numerical, cross-checked against SnapPy's cusp shapes as in B1370.

**Theorem T2 (the index of v₊).** Assume the partitions of v₊ are regular. Then N(v₊) ≡ #(Fix R ∩ ∂⁺₀) (mod 3).
- *Proof.*
  - N(v₊) = −(χ₀ + χ₁ + χ₂ + χ₃), since v₊ is cusp-fixed on all four cusps.
  - The swap g is orientation-preserving, fixes v₊, maps cusp 0 onto cusp 3 and conjugates R to R⁻¹. So it carries ∂⁺₀ onto ∂⁺₃
    and Fix R onto Fix R: χ₃ = χ₀ and the fixed-point counts agree.
  - L4 gives χ₁ ≡ χ₂ ≡ 0 and χ₀ ≡ #(Fix R ∩ ∂⁺₀) (mod 3). Hence N(v₊) ≡ −2·#(Fix R ∩ ∂⁺₀) ≡ #(Fix R ∩ ∂⁺₀) (mod 3). ∎
- *Consequence.* Suppose the first Fourier coefficient c₀ of ω at cusp 0 is non-zero and its phase avoids the six values of L1.
  Then the three fixed points carry 3|c₀| cos(φ₀ + 2πm/3), which sum to zero, so ∂⁺₀ holds one or two of them:
  **N(v₊) ≡ χ₀ ≡ ±1 (mod 3)**. In particular N(v₊) ≠ 0 and N(v₊) ≠ ±3.
- *The range.* If also the leading allowed shells at cusps 1 and 2 have non-zero coefficients, N(v₊) = −(2χ₀ + χ₂) ∈ {±1, ±2, ±5}.
- *The condition matters.* If c₀ vanished, the next shells would decide the signs at the fixed points. The shells of norm ≡ 0
  (mod 3) take one value at all three, so N(v₊) ≡ 0 would become possible. The control with three shells after the first shows
  #Fix ∈ {0, 3} occurring.

**Corollary (not three, and what three would mean).**
- **Not three.** The class the member itself selects gives, at best, a chiral index that is not a multiple of three.
- **Pullbacks multiply.** For any finite cover p of degree d, N(p*v) = d·N(v): each cusp partition pulls back, and Euler
  characteristics multiply. So every degree-3 cover of cube~3.24 carries a class with N = 3N(v₊) ∈ {±3, ±6, ±15}. It is ±3 exactly
  when N(v₊) = ±1, that is, χ₂ = −3χ₀ at cusp 2.
- **A free triple is such a pullback.** Suppose an isometry fixing the class permutes three rotated Eisenstein cusps and acts
  freely. Then the triple is the pullback of one cusp of the quotient manifold, and the three is three times one. That is B1384's
  one-versus-three question (sL-5), exactly as for B1378's triplet on M₆, which is the restriction of one object on M₂.
- **So in this frame, a three is not a derivation until the architecture decides which level is physical.** A three that is not a
  pullback needs a permuting symmetry with fixed points, whose quotient is an orbifold.

Both shapes are registered as **sL-7, the Eisenstein triple**, with the cover-resolution caveat attached.

## 4. What it means

**For sL-6.** B1385 said the ingredient m004 withholds had a precise address and no occupant. The occupant exists, two cover steps
above B1186's family: cube~3.24.
- At its Eisenstein cusps no symmetry forbids the index.
- The class it selects twice over (below) has N ≢ 0 (mod 3) under one analytic hypothesis.
- This is the first time in the record that the seat's frame produces a chiral index protected by the manifold's own symmetry
  rather than left to an accident of coefficients. B1370's cusps needed a coefficient to *vanish* for N ≠ 0; here N ≠ 0 needs one
  *not* to vanish.

**The class selects itself, twice.**
- v₊ spans the only line of H¹ that every isometry fixes. It is a fixed point of the symmetry, not a free orbit, so B1384's
  naturality theorem leaves it selectable.
- It is the only cuspidal class. Its harmonic representative decays at every cusp: the Higgs field is normalisable, and the sector
  is cusp-fixed everywhere.
- Neither choice is imposed from outside; both are read off the member.

**What is left is analysis, and of a better kind.** The remaining hypothesis is B1370's: one Fourier coefficient of a harmonic
1-form. Here the form is cuspidal on an arithmetic group commensurable with PSL(2, O₃), a weight-2 cusp form in the Bianchi
setting.
- If the member's group is a congruence subgroup, the coefficient is a Hecke eigenvalue datum and the first one is normalised to
  1 at a suitable cusp. Whether it is a congruence subgroup is not known here.
- Otherwise the coefficient is computable by a Hejhal-type solve. The record's nearest instrument is the Maass solver on main
  (B878/B922; B1007's correction).

Either route decides T2's hypothesis. Neither is run here.

**Three is a different shape, and a cheap one.** L4 makes the arithmetic of the three explicit:
- An index from one orbit of rotation fixed points is ≢ 0 (mod 3), so this member's selected class never gives three.
- Any degree-3 cover triples an index, and a freely permuted triple of cusps is always such a pullback. So "three" in this frame is
  available by cover resolution. It means something only once the architecture says which level is physical: B1384's
  one-versus-three question, sL-5, the same that governs B1378's triplet.
- sL-7 registers both the cheap three (a cover of cube~3.24; N = 3N(v₊), equal to ±3 iff N(v₊) = ±1) and the non-pullback one (an
  orbit whose permuting symmetry has fixed points).

The record now has three order-three elements, and they are kept apart:
- m010's cubic character δ;
- M₆'s deck C₃, whose triplet index B1378 computes;
- the Eisenstein rotation of a cusp.

L4 is the Eisenstein one's arithmetic.

**For the chain.** The ingredient list gains an existence statement: a free cusp with a symmetry-protected disc-type partition
exists in m004's class, conditional on one coefficient. Two things are unchanged:
- the spin-½ half, where B1372 and B1373 hold that the doublet halves need order-4 points the geometric path does not give unitarily;
- every Standard-Model value. The 19 stay at 0.

## 5. Fences

- **The frame.** The seat's: Pantev–Wijnholt on the cusped 3-manifold, with N = −χ(∂⁺M) for cusp-fixed sectors (B1351 (ii)), the
  free-cusp condition (B1368, B1369) and the partition by the sign of the leading cusp mode (B1370 §1). That is the convention the
  R23 scoping of B1351 names. Main's paper (S17) states that the choice of distinguished boundary part is a definition not yet
  derived from the manifold. B1386 is a statement inside the frame.
- **The half.** The spin-0 half of a generation only. No physics reading beyond the frame's.
- **The hypotheses.** T2 needs regular partitions and the non-vanishing of one coefficient at a non-degenerate phase. Both are
  generic, and no symmetry of the member forbids them. Neither is proved.
- **The search.** A search, not a classification. It covers ocube06_08812's covers of degree 2 and 3. Other members and other
  degrees may hold more open cusps, or an Eisenstein triple.
- **The motivation.** The motivation is the programme's sL-6. Nothing rests on a philosophical premise.

## 6. Files

- `verification/eisenstein_search.py`, `verification/eisenstein_search_run.txt` — S1: the filter (degrees 2 and 3), the Eisenstein
  analysis of the 18 rotation-carrying covers, the isometry classes.
- `verification/the_open_cusp.py`, `verification/the_open_cusp_run.txt` — S2–S4 and L4's controls (the model torus; the member's
  invariant fields; the index sampling; the grid cross-check with B1385's `chi_positive`).
- `verification/cube3_24.isosig` — the member's decorated isomorphism signature.
- `tests/test_b1386_the_open_eisenstein_cusp.py` — the lock. The fast part covers L4 on the model torus and the SnapPy facts; the
  instrument run is marked slow.
