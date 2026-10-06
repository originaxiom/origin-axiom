# B1483 — THE END OF THE FRAME SPACE: a spin structure puts an elliptic curve at each cusp; on a − state the two classes of spin structures put complex-conjugate curves there; and the ¼ law holds on the one five-cusped manifold that could have confined it to a single cusp

**Verdict: PROVED** — the lemma (general), and four of the five sealed predictions on their ranges; **R3 FAILED, as its
20% prior expected, and is reported as the table the SM seat asked for.** Scope: frame F-CI; objects: the 68 amphichiral
word states to length 12 (X_gen, named as that set); N₄₅ = m003's five-cusped cyclic cover of degree 45; o10_150729 =
its five-cusped cyclic cover of degree 5. Reach: general for the lemma, class for C1, single for C2. cc (main),
2026-10-07. Sealed `4ec814fbc` (sha256 f2b21a8a). Lead L250, cells (a) and (c); the SM seat's ask of 2026-10-06.
No physical quantity. **0 of 19.**

**Credit.** The SM seat attacked Theorem A on 2026-10-06, found it to hold, supplied the step main had left implicit
(an isometry has finite order, so a determinant −1 cusp map is an involution), and computed that every lifted mirror
of its cover N₄₅ is rhombic at its one fixed cusp — which is what made cell C2 a question worth asking.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /elliptic curve|j-invariant|isogen|frame bundle|frame space|real structure|2-torsion point/: 35 of 1355 arcs on main match (NEGATIVE 8, OPEN 1, PROVED 26)`
— the elliptic curves on the record are curves of the character variety (40a1, 40a3), a different object; the nearest
prior is B1277/B1293 (the physics seat's real structure on m004's cusp lattice and −I on the cusp torus with its four
fixed points), not related there to a spin structure. Controls and the SM seat's relay were seen before the seal and
are listed in it. **Literature:** a reader's report on bundles over Γ\SL(2,ℂ) is a pointer, unread on this bench; no
cell rests on it. The lemma is proved here.

## 1. The lemma

Let ρ_s be an SL(2,ℂ) lift (a spin structure), P a peripheral subgroup fixing ∞, ρ_s(γ) = σ_s(γ)·u(v(γ)) with
u(v) = [[1, v], [0, 1]], v : P → Λ the cusp lattice, σ_s : P → {±1} the peripheral sign character. Put N = {u(v)},
B = ±N. Left multiplication by N preserves a matrix's bottom row: N\SL(2,ℂ) = ℂ² − 0, B\SL(2,ℂ) = (ℂ² − 0)/±1. The
covering P_s\SL(2,ℂ) of the cusp end of the frame space X_s = Γ_s\SL(2,ℂ) maps onto B\SL(2,ℂ) with fibre B/P_s:

> **the cusp end of X_s is a principal bundle with fibre the elliptic curve E_s = ℂ/ker σ_s** — over ℂ² − 0 with fibre
> the cusp's own curve ℂ/Λ when σ_s is trivial there, over (ℂ² − 0)/±1 with a curve two-isogenous to it otherwise.

With L the rational longitude, Mu a dual class and z = Mu/L the cusp shape:
(σ(L), σ(Mu)) = (+,+): τ = z · (−,+): τ = z/2 · (−,−): τ = (z+1)/2 · (+,−): τ = 2z.
**So a spin structure is visible in the complex geometry of the frame space's end**, and Theorem A reads: a mirror
gives the cusp's curve a real structure, and fixes a spin structure only if it preserves that curve's sublattice.

## 2. Results

| | sealed prediction | prior | result |
|---|---|---|---|
| **R1** | every + state has only real end curves; every − state has exactly the classes (−,+), (−,−) with complex-conjugate j | 95% | **HOLDS, 34 of 34 and 34 of 34** (`end_curve.json`; 304 spin structures; σ(L) = −1 on every one) |
| **R2** | j is not real on at least 28 of the 34 − states | 70% | **HOLDS: 32 of 34.** The two exceptions are −LR (m003, j = 54,000, τ = i√3) and −LLRR (j ≈ 287496) — the golden and silver words, the two arithmetic ones |
| **R3** | on N₄₅ Theorem A (orbit form) excludes every (mirror, spin structure) pair | 20% | **FAILS:** all 180 mirrors are excluded for 8 of the 128 spin structures, 108 for 80, 36 for 40 — never none (table below) |
| **R4** | o10_150729 has no mirror-invariant spin structure | 50% | **HOLDS: NONE-CERTIFIED.** 40 mirror automorphisms found at word length 5, none fixing any of the 32 spin structures; all 32 signed spectra asymmetric, parting at length 2.6339 |
| **R5** | on N₄₅ every mirror has an odd number of rhombic odd orbits, no INVALID composition, CS ≡ ¼ | 90% | **HOLDS:** 180 mirrors, all of cusp-cycle type (1, 4) with the fixed cusp rhombic; CS = 0.2500; no INVALID |

**The hand at the boundary.** On a − state the two classes of spin structures — those with σ(Mu) = +1 and −1 — end in
the curves with moduli τ and −τ̄ (mod 1): complex conjugates. On 32 of the 34 amphichiral words they are not isomorphic
(j is not real): **the two mirror-related spin classes put two different elliptic curves at the cusp, exchanged by
complex conjugation.** On the golden and silver words the curve has complex multiplication and happens to be its own
conjugate — the same two members on which B1481's phase showed its number field. On a + state every end curve is real.

**N₄₅, for the SM seat** (`cover_m003_45_5.json`). 90 tetrahedra, five cusps, H₁ = ℤ/34 ⊕ ℤ/34 ⊕ ℤ⁵, 360 isometries (the
45 deck translations times m003's eight), 180 mirrors. Each mirror fixes one cusp, rhombically, and 4-cycles the others;
the class it fixes mod 2 is the same at each cusp for every mirror fixing that cusp. Of the 128 spin structures:

| cusps (of five) where the fixed class has trace −2 | spin structures | mirrors Theorem A excludes |
|---|---|---|
| 5 | 8 | 180 of 180 — **no mirror fixes any of these, by proof** |
| 3 | 80 | 108 |
| 1 | 40 | 36 |

The number of such cusps is always odd, so no spin structure escapes Theorem A entirely. The pairs it leaves open were
to be decided by the signed spectrum; SnapPy's Dirichlet construction fails on N₄₅, so **they are not decided here**.

**o10_150729** (`witness_o10_150729.json`, `validation.json`). It is m003's five-cusped cyclic cover of degree 5 — and
the manifold that killed the first sealed sentence of B1477's shear law. Theorem A in orbit form excludes between 48
and 88 of its 120 mirrors for each spin structure and all of them for none; the witness route and the spectrum settle
the rest: no mirror-invariant spin structure. The certificate was validated on this manifold before it was believed:
every word SnapPy returns carries its listed complex length (worst miss 1.8·10⁻¹⁴) and the sign-free multiset {tr²} is
conjugation-symmetric, so the asymmetry is the signs'. **"At CS = ¼ no spin structure survives the mirror" now holds on
a manifold with five cusps where the cusp theorem alone could not prove it** — one member, not a law.

## 3. What it means, and what it does not

- **For L250.** The candidate frame of the right parity is not blind to the bit at its boundary: the spin structure
  chooses the curve E_s there, and on a generic − state the mirror exchanges two non-isomorphic curves. That is the
  holomorphic datum an index with boundary would take its boundary term from. No such index is constructed here.
- **For the SM seat's lane.** On N₄₅ eight spin structures admit no mirror at all; whether the other 120 do is open.
  Nothing here bears on a count of generations.
- **Not derived:** a hand's sign, a count, a value.

## 4. Disclosed

R1 is the lemma together with B1479 and was expected. The composition of cusp maps uses the columns-are-images
convention checked on m003's longitude, and each return map is validated as an integer involution. The witness route's
coverage is bounded (40 automorphisms of 120 mirrors on o10_150729): existence would be read only from a witness, and
non-existence is read only from the spectrum. `n45_spectrum.py` is a post-seal variant written for the optional cell
(lifts by linear algebra over 𝔽₂ instead of enumeration); it did not run to a result. Numerical: HP holonomy; j by
mpmath after reduction to the fundamental domain.
