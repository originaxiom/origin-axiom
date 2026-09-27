# B1387 — THE INDEX COMPUTED: the harmonic cusp form of cube~3.24's self-selected class, solved numerically, gives N(v₊) = ±2. The first Fourier coefficient at both Eisenstein cusps is non-zero (|c|·√covol = 1.00695, equal at the two, as the swap demands). Its triple phase has cosine 0.37, so each Eisenstein cusp is disc-type with χ = −1 (L1). The two other cusps are annular. B1386's hypothesis holds, and the record's first symmetry-protected chiral index, computed rather than conditioned, is two: not zero and not three. The instrument is the one B1370 said the record lacked.

> **Currency (2026-09-27, B1388, sealed kill test 1): the physical reading is retired as sealed.** The seat's count, a relative
> index at the cut, moves with the cut. At both Eisenstein cusps χ(∂⁺) runs +4, +7, +8, +2, −1 as the cut rises (tangencies at
> τ = 0.0986, 0.1053, 0.1867; the Higgs zeros on the rotation axes at 0.1034). *After the seal:* the asymptotic count here equals
> minus the signed number of Higgs zeros on the whole manifold (Morse's boundary formula). The six zeros near the Eisenstein cusps
> are all equidistant from them, so a cut respecting the isometries loses none. Which count is physical is sL-8. The mathematics
> here stands. `frontier/B1388_the_cutoff_test`.

> **Currency (2026-09-27, B1389): "the spin-0 half" is a whole generation in the 27-frame.** With the Higgs direction in the cone
> −1 < a/b < 2/3 round γ, the count ±2 applies to the whole 15, the 5 entering as the 5̄: two complete, anomaly-free generations in the
> 27-frame. The frames carrying the 78's broken roots are anomalous in every direction. `frontier/B1389_the_full_spectrum`.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** B1386's T2, conditional on "the harmonic form's
first Fourier coefficient at the Eisenstein cusp, non-zero at a non-degenerate phase"; B1370's residual of the same kind ·
**Status:** PROVED in the computational sense of the record's numerical arcs: a Hejhal-type least-squares solve, stable to four
digits across five runs. The member's symmetries (rotation, swap, −I, the killed shells) are reproduced without being imposed. The
qualitative conclusions carry margins of 0.13 and more. Not certified by interval arithmetic · **Fence:** the seat's frame, spin-0
half; no physics crossed · **Price:** unchanged, 0 of 19 · **Numbering:** B1387.

## 0. Seen from above

B1386 found cube~3.24: a chiral member of m004's class whose one cuspidal Higgs class v₊ is fixed by every isometry and negated by
none. It showed by a congruence (L4) that the index is ≡ ±1 (mod 3), *if* the harmonic form's first Fourier coefficient at the
Eisenstein cusp does not vanish at a degenerate phase. Symmetry cannot decide that; only the form can.

Here the form is computed. The class is cuspidal, so its harmonic representative is L²: ω = dF for a harmonic function F on H³ with
F(γx) = F(x) + v₊(γ). At every cusp F has the expansion
- F = A_c + Σ_{k ≠ 0} c_k · t K₁(2π|k|t) · e^{2πik·x}, valid on all of H³.

A Hejhal-type solve fits the c_k:
- sample points are pulled back into SnapPy's developed fundamental polyhedron;
- each is re-expanded in its best cusp chart;
- the resulting linear equations are solved by least squares.

The results:

| cusp | leading shell | \|c\|·√covol | reading | χ(∂⁺) |
|---|---|---|---|---|
| 0 (Eisenstein, rotated) | the first hexagonal shell | 1.00695 (×3) | cos of the triple phase 0.370 | **−1** (disc) |
| 3 (Eisenstein, rotated) | the first hexagonal shell | 1.00695 (×3) | the same phase: the swap | **−1** |
| 1 (τ = √3 i) | one direction (the first shell killed) | 1.789 | annulus | 0 |
| 2 (hexagonal, translated) | the √3-shell (the first killed) | 0.335, 0.335, 2.209 | one direction dominates 6.6× | 0 |

**N(v₊) = −(χ₀ + χ₁ + χ₂ + χ₃) = ±2.** The sign is the choice of generator of the cuspidal line, the sector's charge sign. L4's
congruence N ≡ χ₀ (mod 3) is met: 2 ≡ −1.

What it means, in one line each:
- **B1386's conditional is discharged.** The first symmetry-protected chiral index of the seat's frame is computed.
- **The count is two.** The two rotated Eisenstein cusps of the swap orbit contribute one each; the others are annular. A three
  by this mechanism needs an orbit of three rotated cusps (sL-7).
- **The cheap three is excluded for this member.** Pullbacks give 2·degree, always even.
- **No physics is crossed.** This is the frame's count, for the spin-0 half.

## 1. The method

- **The object.** B1386's member, built by its covering path and pinned by its decorated signature; v₊ recomputed independently as
  the null line of SnapPy's unsimplified presentation's relators and all eight peripheral words (dimension 1).
- **The polyhedron.** SnapPy's `FundamentalPolyhedronEngine`: 90 developed ideal tetrahedra, 74 polyhedron vertices and the 46 face
  pairings of the unsimplified presentation. The matrices satisfy every relator to 4.5·10⁻¹³. The polyhedron is conjugated by
  z ↦ 1/(z − z₀) so that no vertex sits at ∞; the choice of z₀ is a seed, and the results do not depend on it.
- **The pull-back.** A walk through the ideal tetrahedra. Leaving through a face-pairing face applies the inverse pairing and adds
  v₊ of the generator, so F(x) = F(x*) + accumulated v₊.
- **The charts.** For every polyhedron vertex, the element carrying it to its cusp's base vertex, found by a breadth-first search over
  the face pairings.
  - Closing loops of that search are the cusp's parabolics. They give the lattice, whose shapes match SnapPy's cusp shapes.
  - v₊ vanishes on every parabolic to 10⁻¹⁵, an independent confirmation that the class is cuspidal.
- **The solve.**
  - Unknowns: three constants (one fixed) and the c_k with |k|·√covol ≤ K_n, in the half-lattice with reality imposed.
  - Equations: sample points at normalised height τ = 0.08–0.10 in every chart, below the polyhedron's cusp regions, which reach down
    to 0.115. Each is pulled back and re-expanded in the chart of the tetrahedron's vertex where it sits highest.
  - Least squares, full rank in every run.
- **Reading the modes.**
  - The leading non-vanishing shell at each cusp decides the partition at large height: ∂⁺ = {ω_t > 0}, which is where the leading
    shell of F is negative, since t K₁(2π|k|t) decreases.
  - On a rotation orbit, L1's sign is the sign of the cosine of arg(c_{K₁}c_{K₂}c_{K₃}) over a sum-zero triple. This is invariant, so
    the rotation matrix is not needed.
  - Otherwise χ comes from B1386's Morse count, with its completeness check, or its grid for one direction.

This is Hejhal's method in kind, the standard tool for automorphic forms on non-compact quotients. What is new here is its use on
this member's cuspidal class, to decide a chiral index.

## 2. Computed

`verification/harmonic_cusp_form.py`, record `harmonic_cusp_form_run.txt` (about twenty seconds on an idle machine).

| run | K_n | τ | chart seed | sample seed | unknowns | equations | condition | fit residual | test residual (τ = 0.06, 0.09) | killed shells, max \|c\|·√covol | N |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a | 6 | 0.10 | 1 | 1 | 473 | 1024 | 5.2·10² | 3.7·10⁻³ | 1.7·10⁻² | 1.4·10⁻³, 1.7·10⁻³ | +2 |
| b | 10 | 0.10 | 1 | 1 | 1259 | 2500 | 7.5·10³ | 3.0·10⁻⁴ | 3.2·10⁻³ | 7.2·10⁻⁵, 6.0·10⁻⁵ | +2 |
| c | 14 | 0.10 | 1 | 1 | 2459 | 4624 | 1.2·10⁵ | 3.1·10⁻⁵ | 8.6·10⁻⁴ | 4.3·10⁻⁶, 6.7·10⁻⁶ | +2 |
| d | 12 | 0.08 | 3 | 9 | 1805 | 3364 | 6.6·10³ | 4.9·10⁻⁴ | 1.9·10⁻³ | 4.5·10⁻⁵, 7.3·10⁻⁵ | +2 |
| e | 14 | 0.09 | 2 | 3 | 2459 | 4624 | 5.5·10⁴ | 7.6·10⁻⁵ | 8.6·10⁻⁴ | 1.8·10⁻⁵, 1.3·10⁻⁵ | +2 |

Every run is full rank, and v₊ vanishes on every parabolic to 1.6·10⁻¹⁵. The lowest pulled-back normalised height is 0.111–0.119,
so the sampling heights lie below the polyhedron's cusp regions, as Hejhal's method needs.

**The symmetries, reproduced without being imposed.**
- *The rotation at cusps 0 and 3.* The three first-shell magnitudes agree to 10⁻⁴ relative.
- *The swap.* |c|·√covol agrees across cusps 0 and 3 to 10⁻⁴, and the cosines of the triple phases agree. The chart-invariant
  combination is the right one: under a similarity of charts, heights scale with √covol and c inversely.
- *The killed shells.* The first shells at cusps 1 and 2, which B1386's instrument (B1370's) says R's translation kills, come out at
  10⁻³ of the leading ones at K_n = 6 and fall with K_n to 5·10⁻⁶ at K_n = 14.
- *The −I at cusp 2.* The triple phase is real (cosine 0.99999), and the two small magnitudes agree.

**The invariants, across the five runs** (K_n = 14, run c; the other runs agree to the digits shown in the record).
- cusp 0: |c|·√covol = 1.00695 (×3); cos Φ = 0.36997;
- cusp 3: 1.00695 (×3); 0.36997;
- cusp 2's √3-shell: 0.33546, 0.33545, 2.20905;
- cusp 1: 1.78949.

**The partitions** (the Morse count complete; the grid agreeing).
- χ₀ = χ₃ = −1, the smallest critical value at 0.134 of the maximum.
- χ₂ = 0, with a gap of 0.54.
- χ₁ = 0, one direction.

## 3. The statements

**Theorem (the index of cube~3.24's self-selected class, computed).** In the seat's frame, the spin-0 sector whose Higgs class is the
cuspidal, isometry-invariant v₊ of cube~3.24 has N = ±2. The sign is that of the charge.
1. At the Eisenstein cusps 0 and 3 the leading shell is the first shell, with non-zero coefficient. Its triple phase Φ has
   cos Φ = 0.370 > 0, so {F₁ > 0} is a disc (L1). Hence ∂⁺ = {F₁ < 0} has χ = −1 at each.
2. At cusp 1 the first shell is killed and the leading shell is one direction: an annulus, χ = 0.
3. At cusp 2 the first shell is killed, and the leading √3-shell has one coefficient 6.6 times the other two: an annulus, χ = 0.
4. So N = 2, and N ≡ χ₀ (mod 3) as L4 requires.

*Evidence.* The computation of §2, with every conclusion stable across the five runs. The margins:
- cos Φ is 0.37 away from its degenerate value 0;
- the critical gaps are 0.13 and 0.54 of the maxima;
- the leading coefficients are 10³–10⁵ times the numerical error.

**Corollary 1 (B1386's T2 discharged).** The hypothesis "first coefficient non-zero at a non-degenerate phase" holds. The first-shell
coefficient is 1.007/√covol₀, and the phase is 0.37 in cosine from degeneracy.

**Corollary 2 (not three by pullback).** For any finite cover p of degree d, N(p*v₊) = 2d, which is never ±3. sL-7's cheap three is
excluded for this member.

**Corollary 3 (the count is the orbit).** The index is carried entirely by the swap orbit of rotated Eisenstein cusps, one each, and
the non-rotated cusps are annular. Read structurally, a protected count equals the number of rotated Eisenstein cusps in the
class's orbit when the other cusps are annular. Three needs an orbit of three that is not a free pullback (sL-7's second target).

## 4. What it means

**For the question the owner asked today, "did we cross physics at any level?":** still no. This is the frame's count of net
chirality in one charged spin-0 sector, on one member of m004's class, for the one Higgs class the member itself selects. The frame
remains assumed: M-theory's local model on a G₂ space along the 3-manifold, with the sign partition as boundary condition (R23). The
spin-½ half (B1372, B1373) and every Standard-Model value are untouched.

**For the programme.** Three things change.
- **The first computed non-zero chiral index in the frame.** B1370's cusps needed a coefficient to vanish for any index; B1386 showed
  where a protected index could live. B1387 computes one: two.
- **An instrument.** The record can now compute harmonic cusp forms on cusped members of the class. That is B1370's missing tool,
  with B1370's four residual cusps as a natural next use. Their classes are not cuspidal, so the non-L² (Eisenstein) part needs a
  convention first.
- **Two, and why not three.** The count is the size of the Eisenstein orbit. Three would need three rotated Eisenstein cusps in one
  orbit of a class-fixing symmetry that does not act freely (sL-7). A free triple is a pullback, and a pullback of this member gives
  even numbers only.

## 5. Fences

- **Numerical.** Double precision throughout: least squares, with SciPy's K₁. Evidence of convergence: the fit residual falls from
  3.7·10⁻³ to 3.1·10⁻⁵ over K_n = 6 → 14, and the invariants are stable to four digits over five runs varying K_n, the sampling
  height, the sample seed and the chart conjugation. Not certified; interval arithmetic would be the upgrade.
- **The representative.** For a cuspidal class the L² harmonic representative is canonical. No convention is chosen.
- **The frame.** The seat's, spin-0 half. The sign partition of the leading cusp mode is the R23-scoped convention.
- **The motivation.** The motivation is the programme's sL-6. Nothing rests on a philosophical premise.

## 6. Files

- `verification/harmonic_cusp_form.py`, `verification/harmonic_cusp_form_run.txt` — the polyhedron, the class, the charts, the
  solve, the reading of the modes; five runs.
- `tests/test_b1387_the_index_computed.py` — the lock (a K_n = 6 solve, seconds: the symmetries reproduced, the partitions, N = ±2).
