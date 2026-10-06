# B1483 — PREREGISTRATION: THE END OF THE FRAME SPACE — the elliptic curve a spin structure puts at a cusp, and Theorem A where there are several cusps

**Sealed before any cell runs beyond the controls named in §0.** cc (main), 2026-10-07. Lead L250, cells (a) and (c);
and the SM seat's ask of 2026-10-06 ("N₄₅ under Theorem A").

**The questions.** L250 names the six-dimensional frame space X_s = Γ_s\\SL(2,ℂ) as the candidate frame of the right
parity; the record's states are cusped, so the first thing to know is what X_s looks like at a cusp and whether the spin
structure is visible there. Second: B1477's "at CS ≡ ¼ no spin structure survives the mirror" is proved on one-cusped
census manifolds; does it hold where there are several cusps — on the SM seat's cover N₄₅, and on o10_150729?

## 0. Seen first

- `VERDICT topic-sweep /elliptic curve|j-invariant|isogen|frame bundle|frame space|real structure|2-torsion point/: 35 of 1355 arcs on main match (NEGATIVE 8, OPEN 1, PROVED 26)`
  — read at the level of the verdict lines, the FINDINGS bodies not opened: the elliptic curves on the record are curves of
  the *character variety* (40a1 / 40a3: B211, B509, B510, B1237, B1238), a different object; the nearest prior is B1277 and
  B1293 (the physics seat's R61, R62: "a real structure on the fiber, the cusp lattice ℤ + ℤ(2+4ω) exactly"; "θ = −I … on
  the cusp torus (Fix = 4 isolated points)") — the cusp torus of m004 with its 2-torsion points, not related there to a
  spin structure. Twenty-three matches are in bodies I did not open. No verdict line states that a spin structure's
  peripheral sign is an index-two sublattice of the cusp lattice or that the frame space's end is fibred by its curve.
- `VERDICT topic-sweep /o10_150729|N_45|N₄₅|degree-45|five cusps/: 4 of 1355 arcs on main match (PROVED 4)` — B1477 (o10_150729
  kills the first sealed sentence of the shear law) and the SM seat's harvest rows.
- **The SM seat's relay of 2026-10-06** (`SM_TO_CC_AND_CODEX_2026-10-06_THE_FLOOR_AT_THE_CUP_KERNEL.md` on its branch, read in
  full): Theorem A attacked and found to hold, with the step I had left implicit supplied (an isometry has finite order, so
  a determinant −1 cusp map is an involution) — **credited**; on N₄₅ every lifted mirror fixes one cusp, rhombic, and
  4-cycles the other four; no mirror lifts to its four degree-60 covers; its ask: "If its longitude trace is −2 there,
  Theorem A says no lifted mirror fixes a spin structure of N₄₅."
- **Seen in data before this seal, all of it.** (i) `end_curve.py` on the two controls: m004 — two end curves, j ≈ −52,512 and
  ≈ 8.04·10¹⁸, both real, different; m003 — both spin structures give τ = i√3, j = 54,000 (also computed by hand).
  (ii) `cover_theorem_a.py` on m004 (rectangular, nothing excluded), m003 (rhombic, fixed class the longitude, both spin
  structures excluded for every mirror) and the declared control cover, m003's five-cusped cyclic cover of degree 5 —
  **which SnapPy identifies as o10_150729**: 240 isometries, 120 mirrors of cusp-cycle types (1,1,1,2), (1,4), (2,3), every
  odd orbit rhombic, 32 spin structures, Theorem A excludes between 48 and 88 of the 120 mirrors for each and all 120 for
  none. (iii) The list of m003's cyclic covers: six of degree 45, exactly one with five cusps. Nothing else: no end curve of
  any other state, no run on N₄₅, no witness search or signed spectrum on o10_150729.
- **Literature.** A reader's report on bundles over Γ\\SL(2,ℂ) (Winkelmann's memoir, Fei–Yau, Otal–Ugarte–Villacampa and
  others) was received today; it is a pointer, unread on this bench, and **no cell rests on it** (the owner's rule of
  2026-10-06). The lemma of §1 is proved on this page.

## 1. The lemma (proved here)

Let Γ_s ⊂ SL(2,ℂ) be the image of a lift ρ_s and P a peripheral subgroup, conjugated to fix ∞: ρ_s(γ) = σ_s(γ)·u(v(γ)),
u(v) = [[1, v], [0, 1]], v : P → ℂ an isomorphism onto the cusp lattice Λ, σ_s : P → {±1} the peripheral sign character
(B1477). Put N = {u(v)} ≅ ℂ and B = ±N. Left multiplication by N preserves the bottom row of a matrix, so
N\\SL(2,ℂ) = ℂ² − 0 and B\\SL(2,ℂ) = (ℂ² − 0)/±1. The covering P_s\\SL(2,ℂ) of the cusp end of X_s maps to B\\SL(2,ℂ)
with fibre B/P_s (B is abelian). If σ_s is trivial on P, P_s ⊂ N and the end is a principal bundle over ℂ² − 0 with fibre
ℂ/Λ. If not, v maps ℂ onto B/P_s with kernel Λ_s = v(ker σ_s), of index two in Λ, and the end is a principal bundle over
(ℂ² − 0)/±1 with fibre **E_s = ℂ/Λ_s**. ∎ The cusp end is the part where the bottom row is small.

**Dictionary.** With L the rational longitude, Mu a dual class, z = Mu/L:
(σ(L), σ(Mu)) = (+,+): τ = z · (−,+): τ = z/2 · (−,−): τ = (z+1)/2 · (+,−): τ = 2z.

**Consequences, to be checked by C1.** A mirror acts on Λ by complex conjugation in suitable coordinates. Rectangular
(Re z ∈ ℤ): every index-two sublattice is conjugation-stable, so every end curve has real j. Rhombic (Re z ∈ ½ + ℤ) with
σ(L) = −1: the two classes (−,+) and (−,−) have τ and −τ̄ mod 1 — **complex-conjugate curves**; j is real only if the
curve happens to be isomorphic to its conjugate (which for Re τ = ¼ forces (Im τ)² ∈ ℚ, a CM point — as on m003).

## 2. Cells

- **C1** `end_curve.py all`: the 68 amphichiral word states to length 12 (B1479's table), every spin structure: σ, τ, j.
- **C2a** `cover_theorem_a.py m003 45 5`: N₄₅ — its mirrors (SnapPy's complete isometry list), the return map on every odd
  cusp-orbit, its fixed class when rhombic, the sign of every spin structure there; Chern–Simons class.
- **C2b** B1477's `zero_witness.witness("o10_150729")`, unchanged: mirror automorphisms by the matrix route (word length
  5, 6, 7), the spin structures they fix, and the spin-signed trace spectrum to length 3.0 for all 32.
- The signed spectrum of N₄₅ (90 tetrahedra) is attempted at length 1.5 and reported as not computed if SnapPy's
  Dirichlet construction fails or runs beyond thirty minutes.

**Instruments (sha256, first 16):** `end_curve.py` 830cca6bedbd14cc, `cover_theorem_a.py` 2ae94924e38d57f4, B1477's `zero_witness.py` 4c7cc47bfbcb5cb7.

## 3. Predictions

| | prediction | prior |
|---|---|---|
| **R1** | C1: every + state has only real end curves; every − state has exactly the two classes (−,+), (−,−) with complex-conjugate j | 95% (it is the lemma with B1479) |
| **R2** | C1: on at least 28 of the 34 − states the end curve's j is not real | 70% (m003's is real: seen) |
| **R3** | C2a, the SM seat's question: on N₄₅ Theorem A in orbit form excludes every (mirror, spin structure) pair | 20% (on the control it excludes 48–88 of 120) |
| **R4** | C2b: o10_150729 — five cusps, CS ¼ — has NO mirror-invariant spin structure: all 32 signed spectra asymmetric and no witness | 50% |
| **R5** | C2a: on N₄₅ every mirror has an odd number of rhombic odd orbits, no INVALID composition, and CS ≡ ¼ (the shear law's orbit form on a manifold of neither tested range) | 90% |

**Kills.** R1: a + state with a non-real end curve, or a − state whose two classes are not conjugate — then the lemma or
an instrument is wrong. R2: more than six real. **R4 is the one that can kill something banked in spirit:** a witness on
o10_150729 means "¼ forces the swap" is a ONE-CUSP law, and T-QUARTER-FORCES-SWAP's row is narrowed to say so; a symmetric
spectrum without a witness is reported as UNDECIDED, not as a kill. R3 failing is expected and is then the table the SM
seat asked for, with the undecided pairs named. R5: one even count, one INVALID, or CS ≢ ¼.

**Reading.** Whatever R2–R4 do, the lemma stands: the spin structure is visible in the complex geometry of the frame
space's end as the curve E_s. R2 holding: on a generic − state the two classes of spin structures put complex-conjugate,
non-isomorphic curves at the cusp — the hand as a holomorphic invariant of the boundary, which is where an index with
boundary would take its boundary term. Not banked as physics; no count; no value.

## 4. Disclosed

The cover instrument's composition of cusp maps uses the columns-are-images convention that B1477 checked on m003's
longitude, and validates each return map as an integer involution. The witness route's coverage is bounded (word length
≤ 7, 40 solutions): existence is read only from witnesses, non-existence only from the spectrum. Numerical: HP holonomy;
j by mpmath's kleinj after reduction to the fundamental domain, "real" meaning |Im j| < 1e−9·max(1, |j|). The SM seat's
table for N₄₅ was computed with its own code from lifts of m003's mirrors; SnapPy's isometry list of N₄₅ may contain
more, and is reported.

## 5. Scope

Frame F-CI. Objects: the 68 amphichiral word states to length 12 (X_gen); N₄₅ = m003's five-cusped cyclic cover of degree
45; o10_150729 = its five-cusped cyclic cover of degree 5. Reach: general for the lemma; class for C1; single for C2.
No physical quantity. 0 of 19 before and after.
