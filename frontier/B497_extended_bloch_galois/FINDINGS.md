# B497 — Gate A class 2e: **SEALED** — the extended-Bloch class beyond the object's own is mirror-organized at every level: {+β,−β} propagates as ℤ-multiples, four shape-arithmetics under one D-negating conjugation law, and at the LIFTED level the Ptolemy coordinates ARE the seam roots with the flattening integers a Galois ±pair

**Status: banked (frontier), Closure Campaign Phase 2, class 2e (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum SEALED / COUNTEREXAMPLE /
TOOL-BLOCKED). Verdict: SEALED — at the computable horizon; the class beyond these strata/moduli
remains open (C-guardrail). Firewalled; nothing to `CLAIMS.md`.**

Gate A (S032-A) asks whether any invariant of the single seed is (1) trace-map-invariant,
(2) discretely multivalued, (3) unsymmetrizable — a forced choice. B348 sealed the seed's **own**
Bloch class (β = 2[e^{iπ/3}], the orbit {+β,−β}, the seam identity 1−z₀ = z̄₀) and named the
extended-Bloch/K₃^ind theory as the untested residual. This probe extends the class across every
in-reach stratum (the cyclic-cover tower, the metallic family m = 1..4, the forced ±5 children)
**and** computes the extended-Bloch lift itself — the seed's N=2 Ptolemy varieties solved exactly
in-sandbox and pushed through the Zickert flattening pipeline (`snappy.ptolemy`, offline) — then
runs the B330 three-condition test. Tier per step: **exact** (sympy; pari polmod), **certified-
numerical** (Newton-polished shapes at 290 digits on the exact rect system + `algdep` residual/
height + irreducibility certificates), **numerical** (double snappy), labeled throughout.

## 0. Controls (prereg: fail ⇒ INVALID; all PASS)

- **The seam identity** (B348): 1 − z₀ = z̄₀ exactly; z(1−z) = 1 ⇔ z² − z + 1 = 0 (the Eisenstein
  locus is exactly where the generic Bloch duality equals the arithmetic conjugation); plus its
  |z| = 1 face 1/z̄₀ = z₀ used by the strata sweep. ✓ [exact]
- **The orbit** {2D(z₀), 2D(z̄₀)} = {+Vol, −Vol}: sum 0 (< 1e−25), |member| = Vol(4₁) =
  2.029883212819307 (30 dps, independent of snappy and of the stored constant); D ≡ 0 on the
  fixed field ℝ. ✓
- **β = 2[z₀] live**: the seed's two shapes = z₀ (1e−9) and z₀ AND z̄₀ solve the seed's rect
  gluing system **exactly** (sympy on the live matrix — both Galois lifts are gluing solutions). ✓

## 1. The strata sweep — the pre-Bloch class beyond the object's own

| stratum | shape arithmetic | class | conjugation law | sign killed by | tier |
|---|---|---|---|---|---|
| seed 4₁ | ℚ(√−3), z₀ ×2 | β = 2[z₀] | seam: 1−z₀ = z̄₀ | own amphichirality (D4) | exact |
| cyclic covers n=2..5 | ℚ(√−3) **stationary**, z₀ ×2n | **n·β** (ℤ-multiple tower) | inherited seam | own amphichirality, every n | numerical shapes; lift exact |
| metallic m=2 (m136) | ℚ(i): **four isometric Gaussian tetrahedra** {i, 1+i, 1+i, (1+i)/2} = one tetrahedron's z, z″, z′; rect system solved **exactly**; D = Catalan each, vol = 4G | β₂ | conj multiset **self-pairs** into the D-negative Λ-orbit — EXACT sympy matching | own amphichirality (D4) | exact |
| metallic m=3 (s464) | six deg-**8** min polys (e.g. 4x⁸−31x⁷+…+1), residuals < 1e−180, irreducible | β₃ | self-pairing (1e−8) | own amphichirality (D4) | certified-numerical |
| metallic m=4 (t03910) | deg-**4** min polys (x⁴−8x³+25x²−36x+16, 4x⁴−x²−1, …) | β₄ | self-pairing (1e−8) | own amphichirality (D4) | certified-numerical |
| children 4₁(±5,1) | **one abstract octic** (below), quadratic over the trace field x⁴−x−1 | β₊, β₋ | self-pairing **FAILS** (chiral, detected combinatorially); **MIRROR-pairing holds**: conj(+5 multiset) matches the −5 multiset's D-negative orbit | the **PARENT**: amphichiral 4₁ maps (5,1)↦(−5,1) | exact polmod + certified id. |

**The generalized seam (the probe's first new structural fact).** At every amphichiral stratum,
complex conjugation acts on the shape multiset by a **perfect matching into its own D-negative
Λ-orbit** {1/z, 1−z, z/(z−1)} — the B348 seam (z ↦ 1−z at the Eisenstein point) is one face of a
law that persists across all four shape-arithmetics: conj(class) = −class through Bloch moves,
and the member's own amphichirality identifies the pair. At the **chiral** children the same test
fails on the object itself and succeeds against the mirror: the pairing is inherited from the
parent — the value-level B496 mirror organization, now at the shape/class level.

**The child pair's shape field, COMPUTED (the probe's second new computation).** Raw HP (64-digit)
LLL sees nothing (that wall was real); after a 290-digit Newton polish on the exact filled rect
system: each child's two spun shapes generate a **degree-8 field**, the full filled gluing system
holds **exactly** in ℚ[x]/(octic) (pari polmod arithmetic; geometric identification certified at
290 digits); octic(+5) = x⁸−12x⁷+53x⁶−100x⁵+105x⁴−67x³+27x²−7x+1, octic(−5) =
x⁸−x⁶−x⁵−4x³+6x²−x+1, **nfisisom ≠ 0** — the mirror pair shares ONE abstract field, a quadratic
extension of the trace field (nfisincl(x⁴−x−1) ≠ 0; poldisc contains 283²). The two children
differ only by the **embedding** = the orientation choice: Galois-orbit-member structure at the
field level. (B434's quartic re-verified exactly: irreducible, disc −283, Galois S₄ ⇒ no
quadratic subfield — the child's arithmetic is external-input, not object arithmetic.)

## 2. The extended-Bloch lift (the decisive new computation)

- **The seed's N=2 Ptolemy varieties, exactly, offline** (sympy Groebner with nonzero saturation;
  reproduces B495 §4 independently): obstruction class 0 **EMPTY**; class 1 cut by
  **c² − c + 1 = 0** — *the Ptolemy coordinates are the seam roots e^{±iπ/3}*.
- **Both Galois lifts through the Zickert pipeline** (`snappy.ptolemy` flattening machinery fed
  with our exact solutions — no network, no magma/sage): extended classes with cvol
  **∓2.029883213** — the orbit **{+ĉ, −ĉ}, sum 0, CS-part 0**; and the **integer flattening data
  negates under conjugation**: (p,q) = (0,1)² ↔ (0,−1)². The B348 {+β,−β} pattern holds at the
  lifted level with the discrete lift data itself a Galois ±pair.
- **Independent cross-check**: our own evaluation of Neumann's extended Rogers L̂ on the
  pipeline's certified flattening triples (Def 3.1, N=2) agrees with the pipeline's value to
  **exactly +1 unit** of its declared modulus iπ²/6, at both lifts (integer defect: certified).
- **The covers**: extended class = n·(seed class) (complex volume = n·Vol + 0i, 1e−8, n = 2..5) —
  the ℤ-multiple tower, canonical, no new choice.
- **m136, all 8 obstruction classes**: 6 empty; class 5 **POSITIVE-DIMENSIONAL** (a continuous
  non-geometric family — the B130 clause-(2) exhibit *inside* this class: continuous ⇒ never a
  forced discrete choice); class 6: **8 points** (eliminant c⁴ + 2c² + 2), cvol multiset
  {+4G ×4, −4G ×4} — **sign-balanced, sum 0, CS-part 0**: the silver member's extended class
  collapses onto {+ĉ₂, −ĉ₂}.

## 3. The three-condition test (the seal)

1. **Trace-map-invariant** ✓ — the (extended-)Bloch class is a topological/representation
   invariant (Neumann–Yang), and every stratum is intrinsic: canonical covers, the K010 monodromy
   family, the boundary ±5 of the maximal exceptional set (B434), ALL obstruction classes
   enumerated. No presentation gauge anywhere.
2. **Discretely multivalued** ✓ — finite per stratum: {±β}, {±nβ}, {±β_m}, the ±cs child pair,
   the ±ĉ Ptolemy orbits, the ±(p,q) flattening integers; the value lattice iπ²/6·ℤ is discrete.
3. **Symmetrizable** ✓ — exhaustive three-bin classification:
   - **bin F (forced / fixed-locus)**: field data (min polys, discs, S₄ — ℚ-rational symmetric
     functions); vol magnitudes; D ≡ 0 on the fixed field; CS ≡ 0 at every amphichiral stratum
     (B496's 2-torsion pins, cited).
   - **bin P (±pairs, sum 0)**: {+β,−β} and its ℤ-multiples; {±β_m} with conjugation self-pairing
     into the D-negative orbit (exact at m=1,2; 1e−8 at m=3,4); the lifted orbits {+ĉ,−ĉ} with
     (p,q) ↦ (−p,−q); the chiral child pair, mirror-paired **by the parent**.
   - **bin L (external labels)**: cover degree n, family index m, slope sign, lattice
     representative.

**No forced choice exists in this class ⇒ SEALED.** The object hands you seam-locked orbits and
labels — never a member; even the discrete lift data of the extended class comes as a ±pair.

## 4. Honest scope (C-guardrail) — what remains out of reach

- **The sharp modulus tower** (Neumann π²ℤ for PSL₂, GTZ 4π²ℤ for SL₂): the in-sandbox pipeline
  DECLARES its complex volume only mod iπ²/6 (its cross-N normalization). Certifying the
  4π²-sharp SL(2) statement needs snappy's verified/exact machinery (sage-gated) or magma / the
  Ptolemy database (network) — **TOOL-BLOCKED (named)**. Our from-scratch Neumann evaluation
  agrees to an integer unit (certified); the normal-path parity condition needed to pin the finer
  lattice from scratch is **PARTIAL, named** — not silently approximated.
- **K₃^ind torsion** (the ℚ/ℤ summand, e.g. torsion of K₃^ind(ℚ(√−3))): invisible to every
  dilogarithm-based numeric (D, R̂) *by construction*; étale/motivic machinery — out of sandbox
  scope entirely. This is the honest boundary of "extended-Bloch ≅ K₃^ind" in-sandbox: the
  ℚ-vector-space face is computed; the torsion face is named.
- **Ptolemy N ≥ 3** (the SL(n) lift): exact enumeration beyond Groebner reach — B495's named
  block, unchanged.
- The **universal** all-invariants statement stays **open**: "sealed at the computable horizon;
  the class beyond these strata/moduli remains open," not victory-by-exhaustion.

## The fence

`probe.py` (runnable, ~4 s, tiers labeled, exit 0) → `b497_extended_bloch.json`;
lock `tests/test_b497_extended_bloch_galois.py` (pure backbone: the seam, the orbit, the child
quartic and octic facts, JSON/verdict integrity; snappy behind importorskip: the live controls,
the m=2 exact Gaussian solve, the Ptolemy pipeline orbit, one cover). Method reuse: B495 (the
Groebner-with-saturation idiom + the enum), B496 (cs values cited, not re-derived; the mirror-law
mechanism), B348 (the anchor + the scoped-precision rule — honored the hard way: an mpmath
`abs()` outside the precision context silently rounds to ambient dps and cost one debugging
round; `to_pari` now formats without arithmetic). Cross-refs: **B330** (mechanism), **B348**
(anchor), **B318** (amphichiral involution = conjugation), **B151** (the lattice), **B434/B443**
(the child), **B489/B350** (the cover tower), **B495/B496** (sibling seals),
`docs/OPEN_PROBLEMS.md` Gate A, **K020**. Lit: Neumann (Extended Bloch group and the CCS class,
Geom. Topol. 8, 2004 — Def 3.1 flattenings, the extended Rogers L̂), Zickert (The volume and
Chern–Simons invariant of a representation, Duke 150, 2009 — the Ptolemy flattening formula),
Garoufalidis–Thurston–Zickert arXiv:1111.2828 (ĉ ∈ ℂ/4π²ℤ — the named blocked modulus),
Neumann–Yang (Bloch invariants of hyperbolic 3-manifolds), Zagier (the dilogarithm), Suslin
(K₃^ind and the Bloch group — the named torsion residual).

**Nothing to `CLAIMS.md`; firewall untouched.**
