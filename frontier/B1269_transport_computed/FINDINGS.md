# B1269 — THE TRANSPORT COMPUTED: I-26's surviving gauge group named for every holonomy the corpus supplies, the Standard-Model algebra is not a centralizer in e₆, and the object's one unitary flat connection gives a U(1)⁴ vector-like theory

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (the computations, exact) + NEGATIVE (the reading `h¹(M;27) = generations`, in every transport the corpus's frame admits) · **Price: unchanged at 14** (I-26 stays UNEARNED; its price is sharpened, not paid)

## Why this arc — I-26's two halves, and the one the corpus never wrote down

I-26 (registered 2026-09-06 at B1259's follow-through) is the identification the whole generation-count line
rests on: *a twisted-cohomology dimension of the object ≡ the number of 4d chiral generations*. Its row names
what would earn it: **"exhibit the compactification (or index theorem) in which this h¹ counts 4d chiral
generations, and name the surviving gauge group."** The corpus has scoped the transports before — **B277**
(the canonical 4d lift is class-S of the fiber, N=2, vector-like; the type is free), **B281** (the CRUX:
input-E₆ vs output-E₆), **B433** (the 3d-3d dictionary calibrated at SL(2)), **B715** (the native gauge
system is complex Chern–Simons, no compact slice), **B955** (abelian Wilson lines preserve rank
necessarily) — but nobody wrote the dictionary down against the corpus's own holonomies and computed the two
things the row asks for. This arc does, on the instrument B1267 rebuilt.

## 1. The dictionary (standard; stated, not claimed)

**Acharya–Witten** (M-theory on a G₂ space with an ADE singularity of type g along an associative 3-manifold
Q, a flat connection ρ: π₁(Q) → G with G *compact*): the 4d N=1 gauge algebra is **c_g(ρ)**, the centralizer
of the holonomy image; the massless chiral multiplets are **H¹(Q; g_ρ)** decomposed under c_g(ρ) — the
fields that live on Q are **adjoint-valued**; matter in a non-adjoint representation (a 27 for E₆) arises
**only at isolated points where the singularity enhances** (E₆ → E₇, 133 = 78 + 1 + 27 + 27̄), never from Q's
cohomology. **3d-3d** (the 6d (2,0) theory of type g on Q): the vacua are the G(ℂ)-flat connections on Q and
the massless chiral multiplets at ρ are again **H¹(Q; g_ρ)** — adjoint-valued.

> **In both transports the coefficient system of any field living on Q is the 78. The 27 is not a field on
> Q.** `h¹(M; 27_ρ)` is a well-defined number with no slot in either dictionary — which is why I-26 could
> never be found written down. This is stated here as the first half of the row's price.

## 2. The surviving gauge algebra, computed (`verification/transport.py`, exact)

| holonomy image ρ(π₁) ⊂ E₆ | c_e₆(ρ) | 4d gauge algebra (AW) |
|---|---|---|
| the principal SL(2) (the geometric holonomy, B1112) | **dim 0** | the centre ℤ₃ only |
| the subregular SL(2) (B1257's selection) | **dim 0** | ℤ₃ only |
| the θ-odd amalgam ⟨sl₂, hv8⟩ = e₆ (B582/B1086) | **dim 0** | ℤ₃ only |
| **2T** through the principal SU(2) (the object's finite quotient, I-1/I-6) | **dim 4, u(1)⁴** (B854 reproduced on a different route: the joint kernel of Ad(g) − 1 over the generators, 2T built inside SL(2, ℚ(ω)) as I = [[1+ω, ω],[ω, −1−ω]], J = [[0,1],[−1,0]]; 24 elements, orders 1¹ 2¹ 3⁸ 4⁶ 6⁸; image on the 27 of order 12) | **u(1)⁴** |
| **2T** through the subregular SU(2) (new) | **dim 4** | u(1)⁴ |

**Every holonomy with any chance of chirality (Zariski-dense or principal) leaves no continuous gauge
symmetry at all, and the only unitary holonomy the object's own chain supplies leaves an abelian rank-4
algebra.** That is I-26's second half, answered for every candidate in the corpus.

## 3. THE DOUBLE-CENTRALIZER THEOREM: the Standard-Model algebra is not a centralizer in e₆

Take **s = su(3) ⊕ su(2) ⊕ u(1)_Y** exactly as B1252's descent builds it (the D₂-stabiliser so(10), its A₄,
the A₂+A₁ subsystem, and the unique Y = [0,−5,−4,5,−2,2]/6 that grades the 16 into the SM), as a subalgebra of
e₆ on the B854 basis (dim 12, checked). Computed exactly:

| | dim |
|---|---|
| c(s) | **5** (non-abelian) |
| **c(c(s))** | **13** ≠ 12 |
| control — the full-rank Levi l = su(3) ⊕ su(2) ⊕ u(1)³ that contains s: c(l), c(c(l)) | 3, **14 = dim l** ✓ |

A subalgebra is the centralizer of something if and only if it equals its own double centralizer. **s is not.**
The smallest centralizer containing the SM algebra is 13-dimensional (su(3) ⊕ su(2) ⊕ u(1)², rank 5).
Consequently **no flat connection, no Wilson line and no adjoint VEV — in any transport — leaves exactly the
Standard-Model gauge algebra unbroken inside E₆.** This is B952's rank obstruction (*centralizers of semisimple
elements contain a maximal torus*) and B955's abelian result strengthened to **all** holonomies, abelian or not:
rank can drop 6 → 5 through a non-abelian image, and no further along this route. Rank reduction to 4 needs a
non-adjoint Higgs source (the 27 VEVs of B955's reframe), which the object does not supply
(`docs/THE_SM_VERDICT.md` §2.1).

## 4. The massless spectra, computed

| coefficient system on m004 | h¹ | reading |
|---|---|---|
| **78** through the principal embedding | **6** (h⁰ = 0) | the 3d-3d chiral multiplets of T[m004; E₆] at the geometric vacuum = dim of the E₆ character variety there (B281's rank law; B1036's 6) |
| **78** through the subregular embedding | **8** (h⁰ = 0) | the same at B1257's point: 8, not 6 |
| the trivial 1 | 1 | b¹(m004) |
| C_ω, C_ω̄ (2T → ℤ/3) | **0, 0** | Δ(ω) ≠ 0 |
| C_{−1} (the θ-twist of the E₆ singularity by 2O/2T) | **0** | Δ(−1) = 5 ≠ 0 |
| **3** (2T → A₄ on P¹(𝔽₃)) | **1** | the one charged coefficient system |

**The object's own unitary flat connection — the 2T quotient (`verification/transport_quotients.py`: 72
homomorphisms π₁(m004) → 2T, 48 surjective, B1263's numbers reproduced in this bench's own presentation; both
Aut(2T)-classes, meridian of order 3 or 6, give identical Betti numbers)** — transported by Acharya–Witten gives:

> **4d N=1, gauge algebra u(1)⁴, chiral multiplets 4·h¹(1) + 7·h¹(ω) + 7·h¹(ω̄) + 20·h¹(3) = 4 + 0 + 0 + 20 = 24:
> four neutral and twenty charged, the charges in ± pairs (the 78 is self-dual and the u(1)⁴ weights pair
> q ↔ −q). Vector-like.** If a 27 *were* a field on Q it would give h¹(27) = h¹(27̄) = 3 + 0 + 0 + 6 = 9,
> vector-like again.

The **θ-twisted** reading (the Z₂ = 2O/2T outer twist of the ALE fibre by the meridian's mod-2 class) gives 4d
**F₄** super Yang–Mills with **one adjoint** chiral multiplet (b¹ = 1) and **zero 26s** (h¹(C_{−1}) = 0). The
complex holonomies give no compact slice at all (B715), so they are not Acharya–Witten data; their transport is
3d-3d, where the numbers 6 and 8 above are the whole massless story.

## 5. What this does to I-26 and to JOIN 1

- **The row's two halves are now computed.** The surviving gauge group is named for every holonomy the corpus
  supplies (§2), and the compactification in which an h¹ of the object counts anything is exhibited (§1, §4) —
  it counts **adjoint-valued** multiplets, and the counts are **vector-like** on this object in every case.
- **The 27 has no slot.** Earning I-26 therefore cannot mean transporting `h¹(M; 27)`; it means exhibiting an
  E₇-enhancement mechanism — isolated points on the E₆ locus. The corpus's own candidate for those points is
  already banked: B1084's **three A₁ families**, which are the three imaginary quaternion units of Q₈ ⊂ 2T
  permuted by the ℤ/3 = 2T/Q₈ — a three permuted by the object's own arithmetic — but every A₁ meets E₆ along a
  **line**, and **B1259** proves no flat G₂ orbifold can do better. The price of I-26, sharpened: **a conical
  (curved) G₂ geometry with three isolated E₇ points on the E₆ locus, permuted by 2T/Q₈**. Not a computation
  this bench can run; a named object.
- **JOIN 1 q3** is thereby answered in the negative for the h¹ readings and reduced to that named object.

## Controls (MB12, both directions)

- The centralizer computation returns **4** for 2T (B854's value, different route) and **0** for the principal
  sl₂ — it can distinguish.
- The double-centralizer test **passes** on the Levi (c(c(l)) = l, dim 14) and **fails** on s (13 ≠ 12).
- The 2T enumeration reproduces B1263's 72/48 in an independent presentation, and the adjoint h¹ reproduces
  B1036's 6.
- h¹(m004; 3) = 1 sits between the trivial (1) and the characters (0), so the finite-image Fox pipeline is not
  returning a constant.

## Verification

`verification/transport.py` (~30 min, exact; run record `verification/transport_run.txt`) and
`verification/transport_quotients.py` (~1 min). Lock: `tests/test_b1269_transport.py` (the double-centralizer
theorem and the finite-image spectra fast; the 2T centralizer in the slow lane).

- **Feeds on:** B1267 (the instrument), B854 (u(1)⁴), B1252 (the SM subalgebra), B1263 (the 2T quotients),
  B1036 (h¹(ad) = 6), B277/B281/B433/B715/B955 (the transports as scoped), B1084/B1259 (the conical price),
  B952 (rank), B1250 (the D₂ stabiliser).
- **Registers:** I-26 UNEARNED, price sharpened (both halves computed; the remaining price is the named conical
  object).
