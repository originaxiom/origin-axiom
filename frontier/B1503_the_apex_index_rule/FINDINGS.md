# B1503 — THE APEX INDEX RULE: at a G₂ cone point over a finite quotient of a nearly Kähler manifold, the forced inflows of the loci one symmetry fixes cancel against each other and its isolated fixed points, because the link's Dirac index vanishes. So a lone locus forces nothing, and a cusp point can be chiral only where its locus meets something else the same symmetry fixes. On B1501's census the rule holds on all 306 classes, and forced chirality occurs exactly twice over: ℂP³'s paired SU(N) loci, and S³ × S³'s 3-symmetry, whose SU(3) locus carries inflow 3 balanced by a single fixed point.

**Date:** 2026-09-30 · **Seat:** cc (the SM-derivation branch) · **Occasion:** after B1502 §5, at the owner's go (2026-09-29). ·
**Status:** PROVED. The rule and its consequences are theorems, proved at seal. The census ran as sealed; every sealed prediction came
out YES. Seal `PREREGISTRATION.md` (sha256 `d4260750…`, SEAL_LEDGER), committed at af568744 before the instrument existed.
Instrument and banked identity at fafbf975. · **Price:** unchanged, 0 of 19 · **Numbering:** B1503.

## 0. Seen from above

B1502 §5 found that Witten's cubic inflow is what forces chirality on an SU(N) locus at a point: the locus's normal U(1) twist L has
degree n on the link of the point, and the point must carry fields with SU(N)³ anomaly n. This arc asks what the link's own geometry
says about those degrees, for all the loci one symmetry fixes at once.
- **The rule.**
  - The link of a G₂ cone point is nearly Kähler, so it has positive scalar curvature. Its Dirac operator therefore has no kernel,
    and its equivariant index vanishes for every symmetry.
  - The Lefschetz fixed-point formula turns this into a sum over the symmetry's isolated fixed points and fixed curves, which must
    vanish. Each curve enters through its cubic inflow n, with a weight set by its rotation angle.
- **What it settles, on any nearly Kähler link.**
  - A locus that is the only thing its symmetry fixes forces nothing.
  - A cusp point is chiral through the cubic half only where its locus meets another locus, or an isolated fixed point, of the same
    symmetry at the point. With B1502's mixed half, the only other way is a homologically non-trivial torus with a C-field U(1).
- **What the census shows (B1501's 694 classes, run as sealed).**
  - The rule holds on all 306 classes with fixed points; the worst residual is 1.2 · 10⁻¹³.
  - Forced chirality occurs in exactly two ways.
    - On ℂP³, two fixed spheres always pair at one angle with inflows ±N (22 classes, N = 3 to 12). These are two SU(N) loci meeting
      at the apex, the M-theory form of two intersecting brane stacks with bifundamental matter between them.
    - On S³ × S³, the 3-symmetry fixes one sphere and one point. The sphere's SU(3) locus carries inflow ±3, and the rule balances it
      against the isolated point, a codimension-6 singular line through the apex. This was decided at design time and confirmed.
  - Nowhere else: S⁶, F₁,₂ and every torus locus carry none.

**For question 1 (the cusp point).** In the homogeneous census every torus-fixing element fixes the torus and nothing else, so it
forces nothing (B1502, now by a route that does not need homogeneity). A chiral cusp point needs its torus locus to share its symmetry
with another locus or an isolated point.

## 1. The theorem

**Setting.** Y is a compact nearly Kähler 6-manifold with its SU(3)-structure (g, J, ω, Ω), and γ ≠ 1 an automorphism of finite order
of that structure.
- **Fixed sets.** dγ commutes with J and lies in SU(3) on each fixed tangent space. So Fix(γ) is a disjoint union of:
  - isolated points p, with eigenvalues e^{iθ_j(p)} (j = 1, 2, 3) on T^{1,0}, none equal to 1, product 1;
  - closed J-holomorphic curves C, with eigenvalues (1, e^{iθ_C}, e^{−iθ_C}).
- **Notation.** On a curve with θ_C ∉ πℤ, the normal bundle splits into J-complex lines N₁ (e^{iθ_C}, 0 < θ_C < π) and N₂, of degrees
  d₁ and d₂. Write Δ_C = d₁ − d₂.

**Theorem (the apex index rule).** For every such γ,

  Σ_p Π_j (1 − e^{−iθ_j(p)})⁻¹ + Σ_C (i/8) cot(θ_C/2) sin^{−2}(θ_C/2) Δ_C = 0,

where a curve with θ_C = π contributes 0.

**Proof.**
- **(1) The vanishing.** Y is spin and has positive scalar curvature (Einstein), so the spin Dirac operator has no kernel
  (Lichnerowicz). Its equivariant index vanishes for every lift of γ.
- **(2) The symbol.** γ lifts through SU(3) ⊂ Spin(6), and S ≅ Λ^{0,*} ⊗ K^{1/2} with K trivialised by Ω. So D has the equivariant
  symbol of the Dolbeault–Dirac operator, and its equivariant index is the holomorphic Lefschetz number.
- **(3) The formula.** By Atiyah–Singer III, §4, that number is Σ_F ∫_F Td(TF) Π_θ ch_γ(λ₋₁N_θ*)⁻¹. The formula depends only on the
  symbol, so it holds for almost complex Y.
- **(4) The terms.** An isolated point gives Π_j (1 − e^{−iθ_j})⁻¹. For a curve, c₁(Y) = 0 gives x₁ + x₂ = −c₁(TC); the χ(C) terms
  cancel, leaving (i/8) cot(θ/2) sin^{−2}(θ/2) (d₁ − d₂), independent of the genus. ∎

**Witten's inflow.** For a curve with transverse ℤ_N (N the order of e^{iθ}, N ≥ 3), the twist L of B1502 §5 has degree
n = (N/2)Δ. N₁ ⊗ N₂ carries the locus's spin connection, and N₁ ⊗ N₂* carries Λ′ with weight 2/N. So each curve enters the rule as
(i/4N) cot(θ/2) sin^{−2}(θ/2) n.

**Consequences.**
- **(C1) A lone locus forces nothing.** If Fix(γ) is a single curve with θ ≠ π, then Δ = 0 and n = 0.
- **(C2) The cusp point.** A torus locus is chiral through the cubic half only if its symmetry also fixes isolated points or other
  curves, which are cones through the apex. Otherwise, only B1502's mixed half remains, which needs [F] ≠ 0 and a C-field U(1).
- **(C3) Order two** gives no condition, as SU(2) has no cubic anomaly.

## 2. The census (`verification/apex_index_rule.py`, record `apex_index_rule_run.txt`, 876 s)

- **Banked identity** (`identity_run.txt`; it must pass before any census number is read):
  - The instrument's terms give holomorphic Lefschetz number 1, to 2 · 10⁻¹⁵, on:
    - ℂP¹ with z ↦ λz (two points);
    - ℂP² with diag(1, 1, λ): a fixed line with normal O(1) and a fixed point.
  - The closed curve term equals the general Todd form to 10⁻¹⁴.
  - Qi–Wu–Zhang gives ±1 and 0.
  - The J-structures of all four links check.
  - Six controls of order 13, outside the census, one of each fixed-set shape. On each the rule holds to 5 · 10⁻¹⁴, and the weights
    and the lattice agree on every sphere.
  - At the start of the run, S⁶'s 44 two-point classes have opposite terms, to 5 · 10⁻¹⁴.
- **The components** were recomputed by B1501's own routine with its seeds. They match `census.json` in number and type on all 694
  classes.
- **The degrees.**
  - 222 fixed spheres have θ ≠ π. On each, d₁ and d₂ come out integral with d₁ + d₂ = −2 from the isotropy weights. They agree with
    the lattice Chern numbers on both grids (16 × 32 and 24 × 48).
  - Tori are (0, 0), as in B1502 §5.
  - 9 curves have normal angle π and contribute 0.
- **The rule** holds on all 306 classes with fixed points; the worst |S| is 1.2 · 10⁻¹³.

## 3. The reading

**Decided at design time, confirmed.**
- **D1.** S⁶'s single-sphere classes all have Δ = 0: 22 spheres at (−1, −1), plus one with θ = π.
- **D2.** The 25 torus classes have n = 0.
- **D3.** S³ × S³'s 3-symmetry.
  - σ acts at eΔ with all three angles 2π/3; the point's term is −i/(3√3).
  - The sphere has θ = 2π/3 and (d₁, d₂) = (0, −2). So Δ = 2, N = 3 and n = 3.
  - σ² is the conjugate: Δ = −2 and n = −3.

**The sealed predictions.**

| prediction | prior | answer | what was found |
|---|---|---|---|
| P1: ℂP³'s two-sphere classes pair at one angle, n = ±N | ~65% | **YES** | all 22 classes of order ≥ 3; (d₁, d₂) = (0, −2) and (−2, 0); N = 3, …, 12 |
| P2: ℂP³'s one-sphere classes have n = 0 | ~75% | **YES** | all 22; the two points' terms cancel; the sphere is (−1, −1) |
| P3: F₁,₂'s spheres all have n = 0 | ~80% | **YES** | 132 spheres in 45 classes at (−1, −1); 3 more with θ = π |

**P4 (read).**

| link | classes with fixed points | (d₁, d₂) met | classes with n ≠ 0 | largest \|n\| | a curve balanced by points |
|---|---|---|---|---|---|
| S⁶ | 67 | (−1, −1) | 0 | 0 | none |
| S³ × S³ | 31 | (0, 0), (0, −2), (−2, 0) | 2 | 3 | σ and σ² |
| ℂP³ | 95 | (−1, −1), (0, −2), (−2, 0) | 22 | 12 | none |
| F₁,₂ | 113 | (−1, −1), (0, 0) | 0 | 0 | none |

## 4. What it settles, and what it does not

**Settled.**
- **The rule, on every finite quotient of every compact nearly Kähler cone.** It needs neither homogeneity nor the census.
- **C1 and C2.** A lone locus forces nothing. A cusp point's chirality, through the cubic half, needs a partner locus or point of the
  same symmetry.
- **The census's forced chirality.**
  - ℂP³'s paired SU(N) loci, which match the known physics of intersecting brane stacks (Acharya–Witten; Berglund–Brandhuber).
  - S³ × S³'s 3-symmetry, whose SU(3) locus is balanced by an isolated point instead of a partner locus.
- **B1502's torus models re-derived.** They force nothing because each torus is its element's only fixed component, without using
  homogeneity.

**Not settled.**
- **What sits at the 3-symmetry's isolated point.** Acharya–Witten have no useful description of codimension-6 lines, and the rule
  is an identity, not an anomaly-cancellation argument. So what the point carries physically is open.
- **Links outside the census.**
  - Foscolo–Haskins' S⁶ is a candidate. Every automorphism of it has Lefschetz number 2, so a torus fixed there must come with
    partner components.
  - Non-cyclic groups are covered only element by element.
- **The mixed half's torsion refinements.**

## 5. Prior art and fences

- **The sweep** (2026-09-29, re-checked 2026-09-30). This branch, main (`987c0c8f`) and the audit lane (`b72c6ae1`).
  - No record states an index or Lefschetz identity at a G₂ cone point.
  - B1355, B1356 and B1360 use Witten's global sum rule over the apexes of a closing, which is a different statement.
- **Literature.**
  - Witten (hep-th/0108165): the inflow and n.
  - Acharya–Witten (hep-th/0109152).
  - Bilal–Metzger (hep-th/0303243): local cancellation per singularity, with no identity among loci.
  - Berglund–Brandhuber (hep-th/0205184): intersecting stacks at a cone apex.
  - Anguelova–Lazaroiu (hep-th/0208177).
  - Atiyah–Singer III; Lichnerowicz; Fukui–Hatsugai–Suzuki; Qi–Wu–Zhang.
- **No novelty is claimed.** The ingredients are standard.
- **Fences.**
  - B1501's homogeneous links and cyclic classes of order ≤ 12.
  - Witten's n is read only for A-type loci with N ≥ 3.
  - The isolated points' terms have no physical reading here.
  - No physics is crossed. 0 of 19.

## Files

- `PREREGISTRATION.md`: the seal.
- `verification/apex_index_rule.py`: the instrument. It writes `apex_index_rule.json` and `apex_index_rule_run.txt`.
- `verification/identity_run.txt`: the banked identity.
- Lock: `tests/test_b1503_the_apex_index_rule.py`.
