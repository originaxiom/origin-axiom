# Memo 214 — L71: THE PERIPHERAL ROUTE IS EXHAUSTED, AND THE REASON IS EXACT

**Seal:** `outside_bench/seals/L71_PERIPHERAL_EXHAUSTION_PREREG.md`, sha256 after its
**ADDENDUM 1** `d5c420834fe2a78a0c0f209ad7f32e0868ec252b8f4f5f9c25a179cc169d4de9`
(the addendum was committed **before any cell was read**; the pre-addendum seal was
`7c44a929fde9…`).
**Certificate:** `outside_bench/certificates/l71_peripheral_full.py` ·
**Output:** `outside_bench/outputs/l71_peripheral_full.txt`
**Outcomes: CELL 1 = A · CELL 2 = A · CELL 3 = NOT EXECUTABLE AS POSED · CELL 4 = A.**

---

## 0. What memo 213 left, and what this does with it

Memo 213 killed the peripheral **coker slope**: it is forced by the cusp and reads the cusp
shape. Its named successor was *"the full peripheral class, not its coker shadow —
`H¹(T²; Sym^{2m})` is 2-dimensional and the coker map crushes it to one number."*

**That successor is now dead too, and the reason is a theorem rather than a failure.**

## 1. CELL 1 — no block is cuspidal. OUTCOME A.

`res(ξ) ≠ 0` in `H¹(T²; Sym^{2m})` for **every m = 1 … 11** — all six E₆ exponents and five
non-exponents. `res(ξ)` is a cusp cocycle in every case, `dim H¹(T²;V) = 2` in every case,
and at the six exponents `(h⁰, h¹, periph_inv) = (0, 1, 1)`, matching `P2W5-L72`'s exact
ℚ(ζ₆) table.

> **No block's deformation is invisible at the boundary — and that is uniform across
> θ-parity.** The θ-odd directions are not L² / cuspidal deformations.

## 2. CELL 2 — memo 213's identity holds on the whole cusp space. OUTCOME A.

`f(ξ(λ)) = τ·f(ξ(a))` was proved in memo 213 for the restricted global class. Here it is
checked on **all of `Z¹(T²; V)`**, every m: **true for every cusp cocycle**, not just the
one that comes from the manifold.

## 3. CELL 3 — not executable as posed, and *why* is the result

The seal's addendum proposed the basis `{(k, 0), (0, k)}` with `k` spanning `ker N`. Both
are cusp cocycles; neither is a coboundary. **They are still not a basis**, and the
certificate says exactly why — for m = 1 … 6:

| | m=1 | m=2 | m=3 | m=4 | m=5 | m=6 |
|---|---|---|---|---|---|---|
| `⟨(k,0)⟩` mod B¹ | 1 | 1 | 1 | 1 | 1 | 1 |
| `⟨(0,k)⟩` mod B¹ | 1 | 1 | 1 | 1 | 1 | 1 |
| **`⟨(k,0),(0,k)⟩` mod B¹** | **1** | **1** | **1** | **1** | **1** | **1** |

Two independent-looking cocycles spanning **one** dimension. The dependence is exact and
**identical in every block**:

> **`(0,k) + (√−3/6)·(k,0) ∈ B¹(T²;V)`** — and `√−3/6 = −1/τ`, the reciprocal of the same
> cusp shape, exactly.

> **THE RESULT.** The canonical peripheral data — `ker N`, the coker functional `f`, and
> `τ` — reaches a **1-dimensional** subspace of the **2-dimensional** `H¹(T²; V)`.
> There is no canonical second coordinate. Memo 213's slope is not *a* coordinate on the
> peripheral class; it is **the whole of the canonically readable part**, and it is forced.

CELL 3's two-completion comparison could not be run because one of the two declared
completions is not a basis. **That is reported as a non-execution, not converted into an
outcome letter.**

## 4. CELL 4 — L71's computable content is in the record. OUTCOME A.

| component | where |
|---|---|
| integrability at second order, all directions | **B575** — *"Q ≡ 0. The bridge is open at second order, in every direction"* |
| the Zariski closure per direction | **B576** — *"the chirality is exactly the θ-odd motion"* |
| the cup-product obstruction at the foundation | **B270** — *"the cup-product obstruction vanishes; deformations are cusp deformations"* |
| the peripheral behaviour | **memo 213** + this memo |

## 5. What this means for L71

> **INTERPRETIVE.** L71 asks *"what ARE the θ-odd deformations?"* — *"Dehn-surgery-adjacent?
> complex-projective structures? quasi-Fuchsian-like family?"* Four computable questions sit
> under that, and **all four are answered.** They integrate (B575), they leave the principal
> SL(2,ℂ) and force full E₆ (B576), the foundation is smooth (B270), and at the boundary
> they are indistinguishable from the geometric deformation — provably, because the
> canonical peripheral data has only one dimension to work with.
>
> **What remains in L71 is the geometric NAMING, and naming is not a computation.**
> Deciding whether the deformed reps are quasi-Fuchsian-like, or carry complex-projective
> structures, is a literature-and-specialist question about a family this bench can already
> describe exactly.

**Recommendation, not an action:** L71 should be **re-posed as a literature/specialist item
or closed**, with its four computable components cited. This bench does not edit
`docs/OPEN_LEADS.md`.

## 6. Errors filed, at the point of occurrence

**BENCH ERROR #26 — the seal's declared basis was wrong.** It asserted `ker N = ⟨e_n⟩`.
With `ρ(a) = [[1,1],[0,1]]` on `e_i = x^{n−i}y^i`, `N` **lowers** the index, so
`ker N = ⟨e₀⟩` and `f` reads the `e_n` coordinate. **Asserted from habit, not computed** —
the same class as BENCH ERROR #22. The certificate reported `u₂ ∉ Z¹` and every coordinate
`None`: **the failure was loud, not silent.** Corrected by seal addendum before any cell was
read, and the certificate now **computes** `ker N`'s support and prints it (`[0]`) rather
than assuming it.

**BENCH ERROR #27 — the repair repeated the error.** The addendum then proposed
`{(k,0), (0,k)}` as a basis **without checking that it is one.** It is not: the two span one
dimension. Twice in one sitting, a basis was declared rather than verified.

> **Rule added: a declared basis is not a basis until its rank modulo the relevant subspace
> has been computed. Declare, then verify, then use — in that order, in the same cell.**

**Operational note (memo 212's subject, in this bench's own outputs).** Two background runs
wrote to the same output file; the mixture read as a completed run whose header came from
the new code and whose outcome block came from the old. It was caught by reading line 65
against the header, and the run was redone clean. **The same artifact-staleness failure
memo 212 measured in the corpus, produced here, within the same session.**
