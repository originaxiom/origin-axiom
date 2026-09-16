# B1370 — THE RESIDUAL'S LEADING MODE: on the four free cusps that B1369's parity left open, the isometries fixing the cusp act on the torus by affine isometries whose translation parts are computed here, and no symmetry kills the unique shortest cusp mode for any Higgs class — on every one of the four the lowest allowed Fourier shell is a single direction, so the partition is annular and N = 0 unless the harmonic form's coefficients at the first 4, 2, 4, 2 allowed shells all vanish; sL-1's residual is reduced to the non-vanishing of one Fourier coefficient of a harmonic 1-form on each of four cusps

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the developed cusps, the affine actions, the allowed-shell census — numerically, with the lattices checked against SnapPy's cusp moduli) + OPEN, narrowed (the four cusps close only if the harmonic form's leading coefficient is non-zero; nothing in the record computes it, and no symmetry forces it to vanish) · **Price: unchanged** · **Numbering:** B1370 (sL-1's residual, B1369 §6).

## 0. Seen from above

B1369 closed 108 of the family's 112 members in the seat's frame and left four cusps: o10_150688 (cusp 0), o10_150708 (cusp 0),
o10_150716 (cusp 0), o10_150725 (cusp 1), where every isometry fixing the cusp acts by +1 on some free class and the region-swap
parity is silent. What remains there is the partition of the torus by the leading cusp mode of the Higgs form — the lowest Fourier
mode of the dual lattice whose coefficient is non-zero, since on a hyperbolic cusp the modes decay like exp(−2π|k|eᵗ) and the
smallest |k| present dominates at infinity. A symmetry fixing the cusp constrains that mode: F∘σ = εF for the affine action σ of the
isometry on the torus and its sign ε on the class, and a translation part of σ can kill a shell outright (a half-period shift with ε =
+1 forces the coefficient to zero). SnapPy's cusp maps carry no translation parts, so this arc develops each residual cusp from the
tetrahedra shapes, reads every fixing automorphism's affine action on the developed plane, and runs the constraint shell by shell.
The result is the same on all four: the unique shortest dual vector is allowed for every Higgs class (some higher shells are
killed — the half-period translations have teeth — but not the first), so the leading mode is cos(2πk·x + φ), whose zero set is two
parallel closed geodesics: an annular partition, N = 0, unless the harmonic form's coefficient at that mode vanishes for a reason
no symmetry supplies — and the first shell with two directions, where a disc could appear, comes only after 4, 2, 4, 2 allowed
single-direction shells. The residual of sL-1 is therefore one analytic fact per cusp: whether a harmonic 1-form's first Fourier
coefficient at a free cusp is non-zero. Generically it is; the record has no instrument that computes it.

## 1. The frame

1. A cusp-fixed spin-0 sector on cusp c has its Higgs class [ω] in ann(P_c) ⊂ H¹(M; ℝ) (B1369 §1). On the cusp, the harmonic form
   ω = ω_t dt + (tangential part) separates into Fourier modes k ∈ Λ* of the cusp torus ℝ²/Λ; the mode k decays like exp(−2π|k|eᵗ)
   (Bessel asymptotics of the radial equation), so as t → ∞ the sign of ω_t on the torus is that of the lowest shell with a non-zero
   coefficient: F(x) = Σ_{|k| = r_min} a_k e^{2πi k·x}, a_{−k} = ā_k. The partition ∂⁺/∂⁻ of B1351 (ii) is {F > 0}/{F < 0}.
2. An isometry g fixing cusp c acts on the class by ε = ±1 (B1369's instrument) and on the torus by an affine isometry σ(x) = Ax + b
   (A ∈ GL(2, ℤ) in a lattice basis, b the translation modulo Λ); g*ω = εω gives F∘σ = εF, i.e. a_{Aᵀk} = ε a_k e^{2πi k·b} for
   every k in the shell. A shell is *killed* when these equations (with a_{−k} = ā_k) force every a_k = 0; otherwise it is *allowed*,
   with a real dimension of allowed coefficient vectors.
3. If the lowest allowed shell is a single direction {±k}, F = |a| cos(2πk·x + φ) with k primitive: the zero set is two parallel
   closed geodesics, ∂⁺ an annulus, N = 0 — provided the coefficient is non-zero. If the lowest allowed shell contains two independent
   directions, F can have a disc-type partition and the coefficients decide.
4. For a class negated by some fixer (ε = −1) B1369's parity already gives N = 0; the question is the classes with ε = +1 under every
   fixer of their stabiliser.

## 2. Computed

`verification/residual_cusp_modes.py` (about ten seconds; record `residual_cusp_modes_run.txt`), on the manifolds' own geometric
triangulations, which realise the full isometry groups of all four members (|Aut| = |Isom|: 2, 4, 2, 12).

| cusp | developed torus | lattice (reduced modulus; SnapPy's) | fixers (orientation; linear part on Λ; translation in Λ-coordinates; sign on the class) | shells and the verdict |
|---|---|---|---|---|
| o10_150688, cusp 0 (b₁ = 2, one free class) | 40 link triangles, 26 closing-up translations, all pure translations | \|b₁\| = 2, \|b₂\| = 5√3; τ = (5√3/2)i (agrees) | identity; a reflection (−; diag(1, −1); (½, ⅘); +1) | (0, ±1) allowed (dim 1) — single direction; (0, ±2), (0, ±3), (0, ±4) allowed, single; (±1, 0) **killed** (half-period translation); first two-direction shell (±1, ±1) after **4** allowed single-direction shells |
| o10_150708, cusp 0 (b₁ = 2, ranks [1, 1], one free class) | 24 triangles, 18 translations | \|b₁\| = 2, \|b₂\| = 2√7; τ = −½ + (3√3/2)i (agrees) | identity; −I with translation (⅚, ⅓) (+); a reflection [[−1, −1], [0, 1]] with translation 0 (−); a glide [[1, 1], [0, −1]] with translation (⅚, ⅓) (−); all +1 | (0, ±1) allowed (dim 1), single; (0, ±2) allowed, single; first two-direction shell {(±1, 0), (±1, ±1)} after **2** |
| o10_150716, cusp 0 (b₁ = 2, one free class) | 40 triangles, 26 translations | as o10_150688; τ = (5√3/2)i (agrees) | identity; a reflection (−; diag(1, −1); (½, ⅖); +1) | as o10_150688: (0, ±1) allowed, single; first two-direction shell after **4** |
| o10_150725, cusp 1 (b₁ = 3, ranks [2, 1, 2], two free classes) | 24 triangles, 18 translations | \|b₁\| = 2, \|b₂\| = 2√7; τ = −½ + (3√3/2)i (agrees) | all 12 isometries fix cusp 1: three order-3 rotations of the free classes with translations (⅔, ⅔), (⅓, ⅓), three −I's, six orientation-reversing; the action on the two free classes is non-abelian (S₃-type) | six real special lines (eigenlines of fixers; three of them negated by a fixer — closed by B1369's parity) and the generic class (stabiliser trivial): on every one the shortest shell (0, ±1) is allowed (dim 1 or 2), single direction; first two-direction shell after **2** |

Cross-checks: the developing map closes up with pure translations on every cusp (the mirror convention is rejected automatically),
the reduced modulus of the developed lattice equals SnapPy's cusp modulus on all four, every affine action is an isometry (|a| = 1)
with an integral linear part of determinant ±1, the (trace, det) multiset of the fixers' linear parts equals that of SnapPy's cusp
maps on every cusp, the lattice modulus equals the one from SnapPy's `cusp_translations`, and the translation parts come out as simple
fractions of the periods (½, ⅘, ⅖, ⅚, ⅓, ⅔).

## 3. The statement

**Lemma (allowed modes on the residual).** On each of the four residual cusps, for every Higgs class in ann(P_c), the lowest Fourier
shell allowed by the fixing isometries is the unique shortest dual vector ±k₁, and the first allowed shell containing two independent
directions is preceded by n allowed single-direction shells with n = 4 (o10_150688), 2 (o10_150708), 4 (o10_150716), 2 (o10_150725).

**Consequence.** On each residual cusp the partition of every cusp-fixed spin-0 sector is annular — N = 0 — unless the harmonic form's
coefficients at the first n allowed shells all vanish. Non-vanishing of the leading coefficient is the generic situation and no
symmetry of the member forbids it; it is not proved here.

## 4. What it means

1. **The residual is one analytic number per cusp.** After B1369 (homology and parity) and this arc (the symmetry-allowed modes),
   what stands between the family and a full closure in the seat's frame is whether a harmonic 1-form with vanishing periods on a
   free cusp has a non-zero first Fourier coefficient there — four instances. Everything topological and symmetric has been spent.
2. **Symmetry could have decided it and did not.** The half-period translations do kill shells — on o10_150688 the shell (±1, 0)
   dies because the reflection translates by half a period along b₁ while fixing the class — so the test had teeth; on the shortest
   shell every fixer either reverses k (a phase condition, always solvable) or translates by a fraction compatible with the sign.
3. **Depth.** Even an accidental vanishing at the shortest mode would not open a disc: the next allowed shells are again single
   directions, four deep on the (5√3/2)i cusps and two deep on the √7 cusps; a disc-type partition needs all of them to vanish.
4. **What would close it.** The cusp expansion of the harmonic representative of a free class — a numerical harmonic-form
   computation on the cusped manifold, or, since every member is arithmetic over ℚ(√−3), the Fourier coefficients of the
   corresponding cuspidal Bianchi-type form at that cusp. Neither is in the record; the second is the exact route.
5. **The three faces.** The lattice and its shortest vector are the geometry's (the cusp shape); the killed shells are the
   isometry group's; the coefficient is the analysis's — the one face the record's instruments do not yet reach.

## 5. Caveats

1. Conditional: the closure of the four cusps rests on the non-vanishing of the leading coefficient(s); this arc proves what the
   symmetries allow, not what the form does.
2. The leading-mode reasoning (§1.1) is the record's (B1351 (ii), the B1277 addendum's leading-mode argument, fc R71's "allowed
   fields"): the dominance of the smallest present |k| at infinity is the Bessel asymptotics of the cusp; the transversality of the
   zero set for a single-direction mode is automatic (two parallel geodesics).
3. Numerical: shapes, developing map and affine actions are floating-point; lattice coordinates are rounded with tolerance 10⁻⁶ and
   every translation came out as a simple fraction; the moduli agree with SnapPy's to 10⁻⁶.
4. The special lines of o10_150725 are the real eigenlines of the fixers (complex eigenvectors of the order-3 elements are not
   classes); a generic class has trivial stabiliser and only the trivial constraint.
5. The analysis is for the spin-0 half; the spin-½ half's Higgs class on the same cusp is a free class too (B1369 §1.3), so the same
   allowed-mode census applies to it.

## 6. Registered

sL-1's residual restated: four cusps (o10_150688 c0, o10_150708 c0, o10_150716 c0, o10_150725 c1) close iff the harmonic form of
the Higgs class has a non-zero coefficient at one of its first n allowed single-direction shells (n = 4, 2, 4, 2). Instrument named:
the cusp expansion of a harmonic 1-form at a free cusp (numerical, or through the member's Bianchi-type forms). Nothing else new.

## Verification

`verification/residual_cusp_modes.py` (about ten seconds): the developed cusp tori from the tetrahedra shapes (closing-up
translations → the lattice; modulus checked against SnapPy), the fixers' affine actions (B1369's `family_isometries.py` on the
manifold's own triangulation for the automorphisms and their action on the free classes), the dual shells, the allowed dimension
per shell and per class by linear algebra on the coefficient vectors, the depth to the first two-direction shell. Lock:
`tests/test_b1370_the_residuals_leading_mode.py`.

**Sources.** B1369 (the residual, the instrument, the free classes), B1351 (the index and the partition), B1281 §2D (R71's region-swap
and its allowed fields), B1368 (the frame). SnapPy's tetrahedra shapes and cusp moduli; the separation of variables on a hyperbolic
cusp for the decay exp(−2π|k|eᵗ) of the Fourier modes of a harmonic form.
