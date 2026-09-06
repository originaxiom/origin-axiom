# R70 — WHAT THE TWO ARE TWO OF: the θ-even directions the object can carry a count on give vector-like spectra, and the 16 sits on the θ-odd direction where the count is zero

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report, not banked. Exact over ℚ(√5) and in B351's Bourbaki coordinates; scripts `computations/r70_what_two_of.py`, `computations/r70b_true_theta.py`, `computations/frame_fast.py`. Follows R69 (net = ±2 on Fix(θ)).

## 1. Which θ — and the record already caught the confusion

Pantev–Wijnholt's count on Fix(θ) needs a θ-**even** U(1) direction u (R69). "θ-even" refers to the involution the manifold's σ induces on the local system — B353's, which is B351's **diagram automorphism** (fixed algebra 𝔣₄; on the Cartan: fixed dimension **4**, 24 fixed roots). B1270 (SM-derivation branch) had called **quaternion conjugation** on the icosians "θ"; its own addendum (E69, *"θ is the inversion, not the mirror"*, IDENTIFICATION-BY-RESTRICTION) withdrew that. Independently confirmed here: conjugation is outer on E₆ (it sends the 27-class (½,0) to a 27̄-class), but on the E₆ root system it is exactly **−s_β with β = φ⁻¹**, the real root — fixed Cartan dimension **1**, 2 fixed roots — the "1/5 signature" E69 records. So R68's two-sided frame is conjugation-stable but **not** stable under the diagram automorphism (it maps none of the three planes to a frame plane), and the frame's single conjugation-fixed line is not "the θ-even direction"; it happens to have the same centralizer (dim 36) and the same 27-spectrum as ω₂^∨, but that is not a selection.

## 2. The θ-even Cartan and its spectra

The diagram automorphism (1↔6, 3↔5) fixes the 4-dimensional span of **ω₂^∨, ω₄^∨, ω₁^∨+ω₆^∨, ω₃^∨+ω₅^∨**. For the four coweight directions, the U(1) charges on the 27 and on the 78 (exact, from the icosian E₆ transported to Bourbaki coordinates; the same numbers follow from the weight tables):

| u (θ-even) | centralizer in E₆ | 27 by charge | 78 by charge |
|---|---|---|---|
| ω₂^∨ | **A₅ ⊕ u(1)** (36) | 15₀ + 6̄_{+½} + 6̄_{−½} | 35+1 at 0; 20_{±½}; 1_{±1} |
| ω₁^∨+ω₆^∨ | **D₄ ⊕ u(1)²** (30) | 9₀ + 8_{±½} + 1_{±1} | 30 at 0; 16_{±½}; 8_{±1} |
| ω₄^∨ | A₂⊕A₂⊕A₁⊕u(1) (20) | 9₀ + 6_{±½} + 3_{±1} | … |
| ω₃^∨+ω₅^∨ | A₁⊕A₂⊕A₁⊕u(1)² (16) | 5₀ + 6_{±½} + 3_{±1} + 2_{±3/2} | … |
| **control: ω₁^∨ (D₂, the SO(10) direction) — θ-odd** | D₅ ⊕ u(1) (46) | **1_{2/3} + 16_{1/6} + 10_{−1/3}** | 45+1 at 0; 16_{±½} |

Every θ-even row has its charged components in **±q pairs of θ-conjugate representations**: 6̄_{+½} with 6̄_{−½} (θ acts on A₅ as the outer 6 ↔ 6̄), 8 with 8, 6 with 6, 3 with 3. R69's count on Fix(θ) gives, for a θ-even u, the left-handed spectrum 2·(⊕_{q>0} R_q) ⊕ 2·(⊕_{q<0} R̄_q). With the pairing this is **2·(R ⊕ R̄)** for every component: **vector-like under the non-abelian centralizer**, chiral only with respect to the U(1) that u itself breaks (and anomalous under it — PW's own remark on their toy U(1)s). For ω₂^∨: 2·(6 ⊕ 6̄) of SU(6), hence 2·(5 ⊕ 5̄ ⊕ 1 ⊕ 1) under its SU(5) — nothing chiral.

The only row with a chiral non-abelian content is the control: **ω₁^∨**, the record's own D₂/SO(10) direction, whose positive half is 1 + 16 and negative half 10 — two 16's and two 10's would come out of the ±2. **But ω₁^∨ is θ-odd** (the flip sends it to ω₆^∨; its generator lies in the 26): R69's θ-odd clause — the region swap — gives it **zero**, and a θ-odd field cannot have its charges on Fix(θ) at all.

> **The two of R69 are two copies of a vector-like pair. The direction that would make them two generations is θ-odd, and on that direction the object's count is zero.** This is B576's "θ-odd is where chirality lives, θ-even is F₄-stable and vector-like" reproduced in the endpoint frame, with the mechanism visible: a θ-even singular field pairs every charged component with its θ-image.

## 3. Scope

- The transport of the manifold's θ into B1270's E₈/icosian frame is B1270's identification, not this bench's; the statements above are made in B351's Bourbaki coordinates where B353's θ is defined, and in the icosian picture only through R66's root-system matching (which fixes θ's class, F₄-type, and its fixed Cartan). The frame/conjugation statements are exact in the icosian picture.
- "Vector-like" is a statement about the unbroken centralizer C(u) ⊂ E₆ at the tree level of the count; it does not exclude chirality arising from *several* Higgs directions in a non-abelian configuration (PW §3.1's spectral covers), which are not θ-equivariant abelian fields and are not examined here.
- Nothing here is a value.

*Sweep: E69 (SM-derivation branch) withdraws conjugation = mirror and records the 1/5 signature; the −s_β form, the θ-even coweight spectra and the pairing argument are not in either branch.*
