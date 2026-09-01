# R19 — B725 Born-form theorem (scoped recomputation), Ring R2

Cell: `reports/fresh_physics_seat_2026-09-01/recompute/R19_born_form/`
Date: 2026-09-01. Arc: `frontier/B725_born_rule/`.

## VERDICT: MATCH (both scoped sub-claims; exact where the claim is exact)

## Blind-first disclosure

**Read BEFORE writing my code:** `frontier/B725_born_rule/FINDINGS.md` header + probe-1
paragraph (lines 1-50) and the probe-3 paragraph (lines 66-76) — only far enough to
extract the banked claim and numbers: N_{C/R}(psi)=x^2+y^2 degree 2; falsifier field
Q(2cos 2pi/7) with minpoly t^3+t^2-2t-1 giving a degree-3 norm; harmonic core
"variance vanishes only at l={0,2}", non-constant at l=1,3,4,5,6, dims 1+5=6=dim Sym(3x3);
dim-2 counterexample h(n)=n_z^3.

**Read AFTER my code ran and passed:** `b725_probe1.py` (part c), `b725_probe3.py`
(parts B/C), both `*_out.txt`, and `tests/test_b725_born.py`. Never read: probe2 internals,
the modular-conjugation/GNS code (out of my scope).

## My blind recomputation (different methods than the arc's, by construction)

### Part (a) — degree of the norm form = order of the swap (`r19_part_a_norm_form.py`, 14/14 PASS)
- psi*c(psi) = x^2+y^2 = prod over Gal(C/R); total degree **2**; c verified an involution
  (order 2). Exact sympy.
- Order-3 analog built independently: verified 2cos(2pi/7) is a root of t^3+t^2-2t-1
  **exactly** (p(z+1/z)*z^3 = 1+z+...+z^6) and to 1e-170 numerically; verified
  sigma: t -> t^2-2 permutes the roots and has order exactly 3 mod the minpoly
  (sigma^2(t) = -t^2-t+1, sigma^3 = id).
- Norm N(x0+x1*a+x2*a^2) = xi*sigma(xi)*sigma^2(xi) reduced mod minpoly is t-free,
  **homogeneous of total degree 3**, integer coefficients:
  `x0^3 - x0^2 x1 + 5 x0^2 x2 - 2 x0 x1^2 - x0 x1 x2 + 6 x0 x2^2 + x1^3 - x1^2 x2 - 2 x1 x2^2 + x2^3`.
  Cross-checked against the resultant construction Res_t(p, X-xi) and multiplicativity
  N(ab)=N(a)N(b) (exact spot check: -1 * 97 = -97).
- So the claim's own falsifier shape holds: order-2 swap -> degree 2; order-3 swap -> degree 3.

### Part (b) — Gleason harmonic core on S^2 (`r19_part_b_frame_harmonics.py`, 16/16 PASS)
Method (deliberately different from the arc's): harmonic subspaces H_l (l=0..6) built
exactly as ker(Laplacian) on homogeneous polynomials (dims 1,3,5,7,9,11,13 confirmed);
frame-sum F_H(R) = sum_i H(Re_i) evaluated at **12 exact rational rotation matrices**
(rational quaternions), so non-constancy is an exact disproof, not a numeric std.
Full basis of every H_l tested (irreducibility makes one generic element sufficient;
all 2l+1 tested anyway).
- Survivors: **l=0 and l=2 only**; every basis element of l=1,3,4,5,6 has >=2 distinct
  exact frame-sum values (generic l=4 element: 7 distinct exact values). Matches banked.
- l=2 survival proved **symbolically** for a general quaternion-parametrized rotation:
  frame-sum of any quadratic form x^T A x equals tr(A) identically; harmonic l=2 =
  trace-free forms -> frame-sum == 0. Constant, exactly.
- Dim count: 1 + 5 = 6 = dim Sym(3x3). Matches banked.
- **Planted-positive control** (exclusion claim => required): (x^2+y^2+z^2)^2 — degree-4,
  non-harmonic, identically 1 on S^2 — is correctly detected as a SURVIVOR with exact
  frame-sum 3 at every rotation. The detector can see survivors, so the l=4 kill is
  the harmonicity+frame constraint doing real work, not a broken test.
- Dim-2 non-vacuity: h(n)=n_z^3 on the Bloch sphere satisfies h(n)+h(-n)=0 exactly
  (dim-2 frame = antipodal pair) yet is not affine (not Tr(rho P)) — Gleason genuinely
  needs dim>=3. Matches banked.

## Diff against the arc (post-blind)

| item | banked (B725) | mine (blind) | diff |
|---|---|---|---|
| N_{C/R} | x^2+y^2, degree 2 | same, exact | MATCH |
| swap order 2 | conj involution | same | MATCH |
| cubic field | Q(2cos2pi/7), t^3+t^2-2t-1 | same minpoly, root verified exactly | MATCH |
| cubic norm | det(reg. rep.), degree 3, int coeffs | sigma-orbit product mod minpoly | **coefficient-level identical** (`r19_cross_diff_out.txt`, DIFF = 0) |
| admissible l | {0,2}, l=0..6 scanned, numeric std<1e-9 on zonal P_l, 4000 random SO(3) | {0,2}, full bases, exact rational rotations + symbolic l=2 | MATCH (mine strictly stronger: exact) |
| excluded l | 1,3,4,5,6 non-constant | same, exact witnesses | MATCH |
| dim count | 1+5=6=Sym(3x3) | same | MATCH |
| dim-2 counterexample | (1+n_z^3)/2 with f(n)+f(-n)=1 | n_z^3 with h+h(-n)=0 | MATCH (affine renormalization of the same function; convention resolved per E23) |

Methods were independent: the arc's cubic norm uses the regular-representation
determinant, mine the Galois-orbit product + resultant; the arc's harmonic scan is
numeric on zonal harmonics only (justified by the SO(3)-equivariance argument it
states), mine is exact on complete bases.

## Notes / minor observations (no verdict impact)

1. **Lock-test weakness (vacuity-flavored, on the TEST not the claim):**
   `tests/test_b725_born.py::test_probe1_quadratic_degree_equals_cswap_order` checks the
   falsifier only as `sp.Poly(minpoly, t).degree() == 3` — the degree of the *minimal
   polynomial*, which is 3 by construction and could not have failed; it never computes
   the norm form. The probe script itself (`b725_probe1.py` c.2, `assert deg3 == 3`)
   does the real check, and my recomputation confirms it, so the *arc claim* is not
   vacuous — but the committed lock does not by itself guard the degree-3 norm fact.
2. The arc's zonal-only scan (one harmonic per l) is sound because the frame-sum
   operator is SO(3)-equivariant and H_l is irreducible — the arc states this; my
   full-basis run confirms empirically that no mixed verdict occurs within any H_l.

## Caveats (cited-classical, NOT recomputed here — per cell scope)

- The full **Gleason theorem** (every frame function, not just smooth/polynomial ones,
  on dim>=3 is Tr(rho P); the hard continuity lemma) is the cited load-bearing classical
  theorem. My computation, like the arc's, reproduces only its algebraic/harmonic core.
- The **type-III observer algebra / modular conjugation J** apparatus (probe 1's GNS
  construction, probe 2's SSB weights, the II_1/III_1 factor statements) is outside this
  cell's recomputable scope and was not re-run.
- "Amplitudes live in C" (hence swap order 2) is an input from B715/B716, flagged as
  such in the arc itself.

## Files

- `r19_part_a_norm_form.py` + `r19_part_a_out.txt` — part (a), 14/14 PASS
- `r19_part_b_frame_harmonics.py` + `r19_part_b_out.txt` — part (b), 16/16 PASS
- `r19_cross_diff_out.txt` — coefficient-level diff of the two cubic-norm constructions (0)
