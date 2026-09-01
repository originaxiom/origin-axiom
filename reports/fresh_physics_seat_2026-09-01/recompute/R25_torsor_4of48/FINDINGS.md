# R25 — B1127 antilinear completion: 4 of 48 torsor elements give compact color

**Verdict: MATCH.** Own from-scratch construction reproduces the banked count exactly:
48 torsor elements (16+8+16+8), exactly **4** give compact su(3) color I2 = (0,8,0), all
four in antipodal/class-A, all four with global antilinear signature (26,52,0) = E6(-26).
Planted controls green. Per-element raw-invariant multisets agree with the arc's
`b1127_results.json` in every family.

## What I read BEFORE writing code (blind-first record)

- `frontier/B1127_antilinear_completion/FINDINGS.md` (claim, banked numbers 4/48, (0,8),
  (26,52), families antipodal/permute x classes A/B, "(5,3) or (4,4)" for the other 44).
- `frontier/B1127_antilinear_completion/b1127_NOTES.md` (definition of the torsor: two
  Chevalley-automorphism families -- permute: e_r -> eps e_{pi r}; antipodal:
  e_r -> eps e_{-pi r} -- crossed with pi in {pi_mirror (class A), pi_mirror o w0(I2)
  (class B)}, each with its F2 kernel of involutive sign lifts; sigma = tau o theta with
  tau = coefficient conjugation in the Q-rational Chevalley basis; COMBINE formula
  V+(theta) (+) i V-(theta)).
- `frontier/B1125_compact_color/FINDINGS.md` (the linear torsor, 48 elements).
- `frontier/B1114_lorentz_double/FINDINGS.md` + NOTES "A2+A2 subsystem" section (the
  datum needed: hatch = simple roots {a1,a3} (indices 0,2); I2 simple pair
  {(-1,-2,-2,-3,-2,-1),(0,1,0,0,0,0)} = {-theta_high, a2}; Bourbaki labels 0..5).

NOT read before the diff: `b1127_sweep.py`, `b1125_sweep.py`, `b1114_verify.py`, any
`tests/test_b1127_*`, `b1127_results.json`. Read AFTER my run: `b1127_results.json` and
`b1127_sweep.py` lines 382-470 (the kernel solver) for the diff only.

## What I built (r25_torsor.py, all own code)

1. E6 root system from the Bourbaki Cartan matrix (36 positive roots by reflection
   closure; highest root (1,2,2,3,2,1) recovered).
2. Chevalley basis by the lattice-cocycle construction (bimultiplicative eps(a,b) with
   eps(a,a) = -1): [e_r,e_s] = eps(r,s) e_{r+s}, [e_r,e_{-r}] = eps(r,-r) h_r,
   [h_i,e_r] = (a_i,r) e_r. **Jacobi verified exactly on all 78^3 triples (defect 0).**
3. Killing form K = tr(ad ad) computed directly (K(h_i,h_i) = 48 = 4 h-dual-Coxeter;
   K(e_r,e_{-r}) = -24, same orientation as the arc's corrected <e_r,e_{-r}> = -1).
4. I2 = A2 on the B1114 simple pair; verified orthogonal to the hatch; pi_mirror =
   diagram fold (0<->5, 2<->4) fixes I2 pointwise and maps hatch -> I1's roots;
   w0(I2) = s_a s_b s_a on the root lattice.
5. Signed lifts: for each family/class and each of the 64 sign choices on the simple
   root vectors, the lift is extended recursively to all 72 root vectors, then checked
   DIRECTLY as a bracket automorphism (all 78^2 pairs) and as an involution (theta^2 = I).
   Counts: **antipodal/A 16, antipodal/B 8, permute/A 16, permute/B 8 = 48** (all 64
   sign lifts are automorphisms; the involution condition cuts them to pi-invariant
   characters). This reproduces the arc's torsor from its definition alone.
6. Compactness: the sigma-fixed real form on I2 computed directly as
   V+(theta|I2) (+) i V-(theta|I2) (sigma-fixedness checked symbolically), exact sympy
   Gram matrix of K on it (checked real), exact signature. Global antilinear signature
   via COMBINE (numpy, large eigenvalue gaps).

## Numbers (mine vs banked)

| family/class | n | characters | I2 antilinear sig | global antilinear sig |
|---|---:|---|---|---|
| antipodal/A | 16 | {+2} x16 | **(0,8) x4**, (4,4) x12 | (26,52) x4, (42,36) x12 |
| antipodal/B | 8 | {+2} x8 | (4,4) x8 | (42,36) x8 |
| permute/A | 16 | -26 x4, +6 x12 | (5,3) x16 | (40,38) x16 |
| permute/B | 8 | {+6} x8 | (5,3) x8 | (40,38) x8 |

Banked: 4/48, all antipodal/A, all (0,8), global (26,52); other 44 give (5,3) or (4,4);
characters {+2},{+2},{-26,+6},{+6}. **All match.** Element-level diff (after opening
`b1127_results.json`): the multiset of (character, raw K-signature on V+ cap I2, raw on
V- cap I2) per family is identical to the arc's in all four families, and the four hits'
full raw invariants (eigendims (38,40), global raw (14,24)/(28,12), color eigendims (3,5),
color raw (0,3)/(5,0)) coincide exactly. The arc labels hits by kernel bits
(0,0,0,0),(0,1,0,0),(1,0,0,0),(1,1,0,0); mine are simple-root signs
(1,1,1,1,1,1),(1,1,-1,1,-1,1),(-1,1,1,1,1,-1),(-1,1,-1,1,-1,-1), i.e. eps(a2)=eps(a4)=+1
fixed and the two pi-swapped-pair signs free -- the same coset of a 2-dim subgroup of the
4-dim kernel (parametrizations differ by base point; the invariants identify the sets).

## Planted controls

- Positive: antipodal/pi=id family (64 involutive lifts of -1): exactly ONE element gives
  global (0,78,0) -- the compact conjugation sigma_c -- and it gives I2 = (0,8,0). 16 of
  the 64 give compact I2 (the detector fires when it should, and not always).
- Negative: theta = identity (sigma = tau, split form): global (42,36,0), I2 = (5,3,0).
  Every permute element: (5,3). Every antipodal/B element: (4,4).
- The arc's Layer-8b secondary construction and the unsigned-fold check were not re-run
  (outside the cell's stated computation).

## Convention notes (E23)

Killing-form normalisation differs (mine tr(ad ad), theirs a scaled invariant form);
signatures are scale-invariant. Cocycle sign conventions differ, so eps labels of
individual elements differ; the torsor SET and all invariants agree.

## Not vacuous

The count could have been 0, 16, or split across families; the (5,3)/(4,4) alternatives
are actually realised by 44 elements; the antipodal/id control shows sigma_c is one
element out of 64, so the (0,8) detector is not trivially satisfied. Structural reading
(mine, not needed for the verdict): for antipodal/A the restriction of the 16
pi-invariant sign characters to I2's rank-2 sign space is surjective, so exactly
16/4 = 4 hit the compact pattern; the non-hits flip two of the three I2 root pairs,
giving (4,4). Also observed: within antipodal/A, compact color <=> global E6(-26)
(the other 12 land on E6(6), (42,36)).

## Files
- `r25_torsor.py` (full computation), `r25_lib.py` (library half used for the diff),
  `my_results.json` (all 48 elements + 64 control elements), `run.log`.
Gate 5: no measured SM values used.

## ADDENDUM (2026-09-01, later the same day) — Layer-8 fences re-run (`r25_layer8.py` → `r25_layer8.json/.txt`, ~20 s)

The "not re-run" line under Planted controls is now closed. Own construction (r25_lib), exact arithmetic.

**(a) Unsigned fold (bank `layer8a_unsigned_pi_mirror`).** The bare permutation lift of π_mirror
(e_r → e_{πr}, h_r → h_{πr}, all signs +1, no sign extension): θ² = I **true**; automorphism **false** —
**672 of 78² = 6084 basis pairs fail**, all of them e–e pairs (0 h–e, 0 h–h), and they are exactly the 672
root pairs (r, s) with r+s a root on which the cocycle is not π-invariant, ε(πr, πs) ≠ ε(r, s). Bank: 38/60
random sparse-vector trials fail; the same trial style (seeded) gives 40/60 here. So the unsigned diagram
fold is not a Lie-algebra automorphism and a genuine sign lift is required — matches the bank's
`valid_as_automorphism: false`, now with an exact count and the reason.

**(b) Secondary "compact-referenced" construction (bank `layer8b_secondary_compact_referenced_construction`).**
σ′ = τ∘θ_split∘θ_A with θ_split = antipodal/π=id, ε=+1 (re-checked: global antilinear signature (0,78,0), i.e.
the linear shadow of the compact conjugation) and θ_A ∈ antipodal/A. The bank ran one base element; here
**all 16** antipodal/A elements (including the 4 R25 compact hits) were composed with θ_split:

| check | result (all 16 bases) | bank (1 base) |
|---|---|---|
| θ_split, θ_A commute | True ×16 | True |
| product involution / automorphism | True / True ×16 | True / — |
| product lies in permute/π_mirror family | True ×16 | — |
| I2 stable under product | True ×16 | True |
| I2 antilinear signature | **(5,3,0) ×16**, 0 compact | (5,3,0), not compact |
| global antilinear signature | (40,38,0) ×16 | — |

Structural reading: antipodal∘antipodal = permute, so θ_split∘θ_A is a permute/π_mirror element, and R25's
table already had (5,3) on all 16 permute/A elements; the bank's Layer-8b number is therefore forced for
*any* choice of base, not just theirs. The compact-referenced alternative cannot produce compact colour
from the mirror. B1127 verdict unchanged: **MATCH** (now including both fences).

Not physics: nothing here touches an observable; **no observable content** is created or removed.
