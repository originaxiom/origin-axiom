# B502 — CL-3C / Gate C: **CLOSES** — every computable realization of the commensurator ℤ/3 gives the trinification factors (the wrong 3) or fails to be copies at all; three symmetric copies of the 27 appear nowhere

**Status: banked (frontier), Closure Campaign Phase 3, CL-3C (prereg `docs/CLOSURE_CAMPAIGN_2026-07.md`
+ local `README.md`; outcome enum OPENS / CLOSES / BLOCKED, committed before compute). Verdict:
CLOSES — OPENS not reached, no owner escalation; BLOCKED considered and not taken (§5). Controls
(prereg: fail ⇒ INVALID): both PASS. Firewalled; nothing to `CLAIMS.md`.**

Gate C (`docs/OPEN_PROBLEMS.md`) asks whether the figure-eight's *intrinsic* commensurator ℤ/3 — the
order-3 Eisenstein units of `ℚ(√−3)` acting in `PGL(2,𝒪₋₃)` (B302; 4₁ index 12, Neumann–Reid) —
realizes as three generations. The gate carries a **written refutation condition** (quoted verbatim
in §4) precisely so the adjudication is not the absorbing loop. This probe computes the ℤ/3 action
explicitly on **every substrate the banked mathematics provides** — the 3-fold cyclic cover's H₁
(B326), the exact Chevalley 𝔢₆ (B351), the 27's weight system in two independent frames, the banked
`(θ,φ)` triality (B299), and the banked `27|₂T` branchings (B329) — and tests the condition verbatim.

## 0. Controls (prereg: fail ⇒ INVALID; all PASS)

- **B302 reproduced.** The object has no order-3: `Sym(m004) = D4`, order 8, full group (live
  SnapPy). The commensurator does: `[[0,−1],[1,−1]]³ = I` and the Eisenstein unit `ω³ = 1`
  (re-verified); the figure-eight covers the minimal orbifold `ℍ³/PGL(2,𝒪₋₃)` at **index 12.0**
  (Humbert covolume, Riley); B302's banked `verdict()` returns True. ✓
- **B326 reproduced.** `H₁(unique 3-fold cyclic cover of 4₁) = ℤ ⊕ ℤ/4 ⊕ ℤ/4` (live SnapPy) = the
  exact Alexander SNF `diag(4,4)`; deck char poly `≡ Φ₃ mod 4` (no roots mod 2 or 4 — irreducible),
  order 3; `disc Δ = 5`, `|torsion| = Δ(ω)Δ(ω²) = 16`. ✓

## 1. The deck ℤ/3 acts irreducibly WITHIN one Eisenstein module — it does not permute three copies

The frame's own identification (B335, cited in Gate B's settled facts): *the generation ℤ/3 is the
deck transformation of the 3-fold cover*, and the generation-breaking datum is exactly this cover's
congruence torsion (B326). Sharpened here to an **exact identification** (new, all exact-tier):

- `Φ₃ − Δ = 4t`, so on the torsion module (killed by 4) **`t² + t + 1 = 0` holds exactly**;
  `Δ(1) = −1` (unit) kills the `(t−1)`-part; `Δ(ω) = −4ω` with norm 16; SNF of `ℤ[t]/(Δ, Φ₃)` is
  `diag(4,4)`. Hence **the torsion is the rank-ONE Eisenstein module `ℤ[ω]/4`** — the local Galois
  ring `GR(4,2)`, residue field `𝔽₄` — **and the deck map is multiplication by `ω`**
  (`T² + T + I ≡ 0 mod 4`, `T³ ≡ I`).
- **Three-copies tests, all failing independently.** A ℤ/3 cyclically permuting three nonzero copies
  `A⊕A⊕A` must have (i) fixed subgroup ⊇ the diagonal `≅ A ≠ 0` — here **Fix = {0}**
  (`det(T−I) = Δ(1) = −1`, a unit; equivalently `N(1−ω) = 3` is invertible mod 4 — the ramified 3
  itself makes the action fixed-point-free); (ii) order `|A|³` a perfect cube — here **16 is not a
  cube**; (iii) eigenvalue 1 mod every prime (a permutation matrix fixes `(1,…,1)`) — here **Φ₃ has
  no root mod 2**.
- **The full invariant lattice, brute-forced over all of `(ℤ/4)²`:** the deck-invariant subgroups
  are exactly `0 ⊂ 2M ⊂ M` (orders 1, 4, 16) — **a 3-chain**, the ideal chain of the local ring
  `GR(4,2)`. No invariant decomposition into three (or even two) summands exists at all.

**The deck ℤ/3 is scalar multiplication by ω within one indecomposable copy.**

## 2. The ℤ/3 on the E₆ structure: everything acts WITHIN the single 27; the images are the trinification factors

All exact (integer/symbolic), on B351's Jacobi-verified Chevalley 𝔢₆ and the banked B299 matrices.

- **The ω-grading (B305's trinification ℤ/3 — the one whose eigenvalue is the object's Eisenstein
  `ω`).** `deg = ht mod 3` grades the exact bracket: **0 violations on all 6084 table entries**, so
  `ζ = ω^deg` is an order-3 automorphism. Eigenspaces: `𝔢₆ = 24 ⊕ 27_ω ⊕ 27_ω²` with fixed
  subalgebra **three mutually-orthogonal A₂'s** (each verified as `{a, b, a+b}`, `(a,b) = −1`) +
  Cartan = `𝔰𝔲(3)³` — the trinification. The `ω`- and `ω²`-spaces are **one 27 and its conjugate**
  (their root sets are negatives of each other), and ζ acts by *scalars* within each — images =
  the trinification pieces, never three copies of anything.
- **The 27's weights, two independent frames** (Bourbaki/B351 and B299's non-Bourbaki frame): the
  grading charge splits `27 = 9 ⊕ 9 ⊕ 9`, and each 9-block restricts to the three A₂'s as
  (trivial ×9 | (anti)fundamental ×3 | (anti)fundamental ×3) — trivial under exactly **one** SU(3),
  bifundamental under the other two: **the trinification factors (the color/L/R block structure)**.
  The E₆ *centre* ℤ/3 acts on all 27 weights by the single scalar ω (one root-lattice coset, by
  construction) — trivially "within".
- **The banked `(θ,φ)` ℤ₃×ℤ₃ (B299, reproduced: order 3, det 1, preserve the E₆ Cartan, free on
  the 27 with 9 orbits of 3), block action computed (new):** θ and φ each **3-cycle the three
  9-blocks (0→1→2→0) WITHIN the single 27**; `θφ²` and `θ²φ` **preserve every block** (the
  within-elements); `θφ` is the reverse 3-cycle. Every element of the banked ℤ/3×ℤ/3 maps the one
  27 into itself — **its images are the trinification factors**, and no element produces a second
  27. (Note recorded honestly: in the banked matrices *both* generators are block-permuting and the
  block-preserving ℤ/3 is `⟨θφ²⟩`; K020 §8's θ↔L3 / φ↔L4 naming attaches to the roles, not to
  which banked generator carries which role.)
- **The banked branching data (B329, reproduced: `27|₂T = 3·1⊕3·1′⊕3·1″⊕6·3` principal and
  `9·1⊕3·1′⊕3·1″⊕3·2′⊕3·2″` trinification, both `n₁=n₂`):** the arithmetic 2T's order-3 element
  acts on the 27 with eigenvalue multiplicities **(9,9,9)** (principal) / **(15,6,6)**
  (trinification route) — an eigen-decomposition **within the single 27** for *both* canonical
  embeddings of the object's arithmetic.
- **No 3·27 substrate exists anywhere banked:** `3×27 = 81 > 78 = dim 𝔢₆`; the grading yields
  exactly one 27 (+ its conjugate); single-object multiplicity is 1 (B307/B321, banked); the
  diagram involution (B351's θ) is order 2 (`27 ↔ 27̄`), not a ℤ/3.

## 3. L3 vs L4 (K020 §8): one ramified 3 — and the commensurator's ℤ/3 computes as the wrong one

`(1−ω)² = −3ω` (verified exactly): **3 ramifies in `ℚ(√−3)`**, and both ℤ/3s of K020 §8 are
multiplication by the *same* ω from this one prime. The L3 form (gauge/trinification, *within* a
generation) is the scalar-ω grading of §2. The L4 slot (the commensurator's Eisenstein unit, B302
— "generations, *between* copies") has exactly two computable realizations, and **both land in the
L3 shape**: the deck ℤ/3 (the frame's own generation-ℤ/3, B335) is scalar-ω multiplication within
**one** rank-1 Eisenstein module (§1), and the `(θ,φ)` triality (the frame's own L4 assignment) is
a permutation of the **trinification factors within the single 27** (§2). The generation form — a
permutation of three symmetric 27-copies — is realized nowhere, and its necessary conditions fail
wherever the ℤ/3 acts. The two ℤ/3s are one ω seen twice; nothing computable makes the
commensurator's copy a *between-copies* symmetry.

## 4. The written refutation condition, verbatim, and its outcome

From `docs/OPEN_PROBLEMS.md`, Gate C (also `README.md` here; locked verbatim by the test):

> It **opens** iff the commensurator `ℤ/3` gives three *symmetric copies of the 27*. It **closes**
> iff those three images are the trinification factors (color/L/R, B302/B305 — the *wrong* 3) or
> otherwise fail to be symmetric matter copies.

| realization of the commensurator ℤ/3 | the three images | branch |
|---|---|---|
| deck ℤ/3 on the 3-fold cover's torsion (B335/B326) | not copies at all: one indecomposable `ℤ[ω]/4`, Fix = 0, chain lattice | **CLOSES** (fail to be copies) |
| ω-grading on 𝔢₆ and the 27 (B305) | the trinification pieces: `𝔰𝔲(3)³ ⊕ 27_ω ⊕ 27_ω²`; the 27's three 9-blocks | **CLOSES** (trinification factors) |
| `(θ,φ)` triality on the 27 (B299; the L4 assignment, K020 §8) | the three 9-dim color/L/R blocks, 3-cycled **within** the single 27 | **CLOSES** (trinification factors — verbatim) |
| arithmetic 2T order-3 on the 27 (B329, both canonical embeddings) | eigenspaces (9,9,9) / (15,6,6) within the one 27 | **CLOSES** (fail to be copies) |

**Outcome: the condition lands on its CLOSES branch in every computable realization; the OPENS
exhibit (three symmetric copies of the 27) exists nowhere in the banked structures and its
necessary conditions are positively refuted wherever the ℤ/3 acts. Verdict per the committed enum:
CLOSES.** OPENS was not reached — no owner escalation.

## 5. The adversarial audit (the absorbing-loop caveat, applied to this verdict)

- **Both branches were live a priori.** Concrete counterfactuals that would have OPENED: had the
  cover torsion been a permutation module (e.g. `(ℤ/2)³` with the deck cycling coordinates — Fix =
  diagonal ≠ 0, order a cube), the object side would hand three symmetric labeled copies to the
  matter dictionary; had the grading eigenspaces contained three ζ-permuted isomorphic summands,
  likewise. The computations *refute those shapes positively* (Fix = {0}; 16 not a cube; chain
  lattice; `24 ⊕ 27 ⊕ 27̄` with scalar action); they do not merely fail to find them.
- **Why not BLOCKED.** BLOCKED is for an adjudication that cannot run ("the orbifold computation
  names its missing tool"). Here the written condition's test ran to completion on every banked
  substrate and every outcome lies in one branch; no computed fact is ambiguous between OPENS and
  CLOSES (the probe asserts this: any AMBIGUOUS realization would have forced BLOCKED, not a soft
  CLOSES).
- **The named residual (honesty, not a hedge).** Not computed: the full character/matter theory of
  the commensurator quotient `ℍ³/PGL(2,𝒪₋₃)` at E₆ — sage/magma orbifold machinery plus a 3d-3d
  matter dictionary for an *exceptional* group (not standard; the same wall as Gate B). That is the
  one place a genuinely **new** `3·27` substrate could in principle appear. **Revival condition:** a
  specialist exhibit of the commensurator ℤ/3 permuting three symmetric 27-multiplets in an actual
  `T[ℍ³/PGL(2,𝒪₋₃); E₆]` spectrum — new structure, not a reinterpretation of the banked one.
  Absent that exhibit, the gate's own written test is settled on the CLOSES branch; re-posing the
  question at the uncomputable spectrum after the written test has landed would itself be the
  absorbing-loop move the condition was written to forbid.
- **Scope guard.** This CLOSES adjudicates the *written refutation condition*; it does **not**
  prove "three generations are impossible" — multiplicity/heterogeneity (K014/B131, two distinct
  seeds) remains the live mechanism, and B307's count-3 obstruction stands independently. And it
  derives no values (structure only; the firewall is a theorem, K020).

## Verdict

**CLOSES (banked).** The commensurator ℤ/3, computed explicitly on every substrate the program's
banked mathematics provides, gives the trinification factors (the wrong 3 — the L3 gauge structure
within a single 27/single family) or fails to be symmetric matter copies at all (one indecomposable
Eisenstein module with scalar-ω action); three symmetric copies of the 27 appear nowhere, and no
computed fact is ambiguous between the branches. Gate C's generation reading fails its own written
test at every computable point. Nothing to `CLAIMS.md`; firewall untouched.

## The fence

Exact tier for everything load-bearing: sympy/integer arithmetic (the Eisenstein module `ℤ[ω]/4`,
the brute-forced invariant lattice, the Chevalley grading on B351's Jacobi-verified integer
bracket, the 27-weight blocks in two frames, the `(θ,φ)` block maps, the B329 character theory).
SnapPy 3.3.2 for the controls (symmetry group, cover homology); mpmath Humbert covolume (numerical
index ≈ 12, as banked in B302). sage/magma not available: the residual orbifold computation is
**named** in §5, not silently absorbed. The generation/physics reading stays firewalled (S045).
Nothing to `CLAIMS.md`; firewall untouched.

`probe.py` (pyenv: controls + the four realizations + the verbatim-condition test; exit 0) ·
`tests/test_b502_gateC_commensurator.py` (< 60 s; SnapPy behind importorskip). Related: **B302**
(the ℤ/3 located: hidden, relational, `PGL(2,𝒪₋₃)`, index 12), **B326** (the cover torsion +
`Φ₃` deck action), **B335** (generation ℤ/3 = the deck map), **B305/B299** (the trinification
grading + triality — the wrong 3), **B329** (`27|₂T`, both canonical embeddings `n₁=n₂`), **B351**
(the exact 𝔢₆), **B307/B321** (count-3 obstruction; single-object multiplicity 1), **K020 §8**
(the four levels, L3 vs L4), `docs/OPEN_PROBLEMS.md` Gate C, `docs/CLOSURE_CAMPAIGN_2026-07.md`
CL-3C. Lit: Neumann–Reid (commensurators, hidden symmetries), Riley (index 12), Calegari
(`math/0603152`, cyclic-cover torsion), Milnor (the Alexander module), Gross/Kostant (the
principal `27 = V(16)+V(8)+V(0)`, via B327/B329), Slansky 1981 (`E₆ ⊃ SU(3)³`).
