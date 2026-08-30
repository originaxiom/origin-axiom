# SEAL — Q7 CONTINUED: COMPUTE THE STABILIZER, DO NOT GUESS IT

**Sealed 2026-08-30, pushed BEFORE any computation.** Follows memo 160.

## 0. What memo 160 left, and why this cell exists

Memo 160 named a route and left **two hypotheses unverified**. The first is:

> **the stabilizer IS a form of Spin(8)** — *"a 28-dimensional stabilizer is CONSISTENT with D₄ and
> is not a proof. The identification requires the actual stabilizer scheme of the object's own pair,
> which this cell did not compute."*

**It can be computed.** `B575`'s `l51_obstruction.py` builds the **exact e₆-in-gl(27) basis** over
ℚ(ω), and `B632` already execs its stages 0–3 to get it. The stabilizer of a pair is then an
**exact nullspace**: `𝔰 = {A ∈ e₆ : A·x = 0 and Aᵀ·y = 0}`.

**And dimension 28 does not settle the type.** Two semisimple algebras of dimension 28 have rank 4:
**𝔰𝔬(8)** and **𝔤₂ ⊕ 𝔤₂**. Both even have 24 roots. They are separated by **simplicity** (𝔰𝔬(8) is
simple; 𝔤₂⊕𝔤₂ is not) and by **root lengths** (D₄ is simply laced; G₂ is not). So the cell must
test simplicity, not just count.

## 1. Cells

### S-1 — the generic stabilizer's dimension · **BLIND**
Build e₆ ⊂ gl(27) exactly; take a pair `(x, y)` in general position over ℚ; compute `dim 𝔰` as an
exact nullspace.
- **S1-28** — the dimension is 28, confirming memo 160's dimension count *by construction* rather
  than by subtraction.
- **S1-OTHER** — it is not, and memo 160's R-2 count is wrong.

### S-2 — the rank · **BLIND**
Compute the rank of `𝔰` (dimension of the centraliser of a generic element of `𝔰`).
- **S2-RANK4** vs **S2-OTHER**.

### S-3 — simple or not · **BLIND, and this is the discriminator**
Decide 𝔰𝔬(8) vs 𝔤₂⊕𝔤₂ by testing whether `𝔰` is **simple**: search for a proper non-zero ideal
(an ad-invariant subspace).
- **S3-SIMPLE** ⟹ type D₄ ⟹ **the identification is made, not guessed**.
- **S3-DECOMPOSABLE** ⟹ it is **not** a form of Spin(8), and memo 160's route **fails at
  hypothesis 1**. That would be a clean negative and is reported as such.

### S-4 — is the object's own pair generic? · **BLIND**
The hypothesis is about the object's pair, not an arbitrary one. Check whether the record pins a
specific pair and whether it lies in the open orbit (non-degenerate invariant).
- **S4-PINNED** — the record's own pair is identified and tested.
- **S4-UNPINNED** — it is not, and **this cell's result is about the generic pair only**, which must
  then be said plainly and not quietly widened.

## 2. The fence, carried forward unchanged

Memo 160's binding clauses still hold, and one is sharpened:

1. **Even `S3-SIMPLE` does NOT conclude that Route A crosses.** It would close hypothesis 1 of five
   and leave hypothesis 5 (orbit count = class set) untouched.
2. **A Lie-algebra computation identifies the algebra, not the group scheme.** `𝔰𝔬(8)` as a Lie
   algebra is compatible with several group schemes (Spin(8), SO(8), PGO(8)) and **only the simply
   connected one gives strong approximation.** Whatever this cell finds, **that gap is stated, not
   glossed.**
3. **`B990`'s UNFAVOURABLE prior stands unrepudiated.**

**Declared prior:** **S1-28, S2-RANK4, S3-SIMPLE, S4-UNPINNED.** I expect to identify the *generic*
stabilizer as D₄ and to be unable to pin the object's own pair. Recorded so that S3-DECOMPOSABLE —
which would kill the route — is not quietly softened, and so S3-SIMPLE is not read as more than
one hypothesis of five.

## 3. Gate 5

No measured value. Exact linear algebra over ℚ(ω).
