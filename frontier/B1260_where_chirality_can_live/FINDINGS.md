# B1260 — WHERE NET CHIRALITY CAN LIVE: the closed wall generalised past doubles, the cusped abelian sector walled too, and the rank-3 search reduced to one branch the corpus already realised

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact; three MB12 controls, one requiring the abelian test to be exercised where h¹ actually jumps)

## The question — `docs/MAIN_GOAL.md` JOIN 1, question 1

Is the generation count to be read on the **closed double** — where **B1086** finds chirality zero —
or on the **cusped** manifold, where Poincaré duality does not obviously force pairing?

## 1. The closed wall is GENERAL, not a fact about doubles

For **N** a closed oriented 3-manifold and **V** a local system:

```
PD:        h^i(N;V) = h^(3-i)(N;V*)
chi(N)=0:  h0 - h1 + h2 - h3 = 0
substitute: h0(V) - h1(V) + h1(V*) - h0(V*) = 0
V irreducible nontrivial => h0(V) = h0(V*) = 0
=> h1(V) = h1(V*)   IDENTICALLY
```

**B1086's *"as PD forces on any closed double"* is a special case.** The wall is **dimension 3 plus
closedness** — so *any* closed assembly is vector-like, whatever its h¹ happens to be. This
generalises the banked statement and explains why the θ-odd dial's h¹ = 2 is not a chirality count.

## 2. The cusped ABELIAN sector is walled too — and not by closedness

Computed here: the Fox derivatives of m004's relator in the 1-dimensional rep are **±Δ(t)/t** with

> **Δ(t) = t² − 3t + 1**, roots **φ²** and **φ⁻²**, product **1**

**Δ is reciprocal** (verified symbolically, not cited), so its vanishing locus is symmetric under
**t → 1/t** — which is exactly **V → V\***. Hence **h¹(ℂ_t) = h¹(ℂ_{1/t}) for every t**, including at
the Alexander root where h¹ jumps. **Alexander reciprocity is a theorem for all knots**, so the
abelian sector **never** carries net chirality — cusped or not.

*(Note the object's own golden pair appearing unbidden: the Alexander roots are φ^{±2}.)*

## 3. So the question is rank ≥ 3, and it cannot factor through SL(2)

**Every Sym^n of SL(2) is self-dual** (verified for n = 0, 2, 4, 8, 12, 16), which is exactly **E65**.
And the corpus's entire SL(n) tower is the **principal** family — B71 builds its SL(3) via `sym2()`,
B153's rows are the *"principal spectrum"* — hence self-dual throughout. **The corpus's own SL(n)
work cannot answer this question.**

## 4. The search reduces to ONE branch, and the corpus already realised it

**B102**: every irreducible SL(3) figure-eight character is **Case I** (`trA = trA⁻¹` — *self-dual by
definition*) or the **`trB = trB⁻¹ = 1`** branch, verified with **"0 neither"** (33 Case I + 5 branch
+ 0 at n = 40). In the 8 trace coordinates (x₁ = trA, x₄ = trA⁻¹, x₂ = trB, x₅ = trB⁻¹; **V0 =
{x₁=x₄, x₂=x₅}** being the self-dual component that contains Sym²), B102's **genuine non-Sym²**
components are:

| | coordinates | duality |
|---|---|---|
| **W1** | (1,q,q,1,p,1,1,p) | trA = trA⁻¹ = 1, but **trB = q ≠ p = trB⁻¹** → **NOT self-dual** |
| **W2** | (p,1,1,q,1,q,p,1) | trB = trB⁻¹ = 1, but **trA = p ≠ q = trA⁻¹** → **NOT self-dual** |

and **B102 realised both as explicit SL(3) reps.** So the object required for the decisive test
exists in the corpus and has never been used for this purpose.

## The deciding computation — named, and small

> **Compute h¹(V) and h¹(V\*) on W1/W2 and compare.**
> **Differ** ⇒ the cusped manifold carries net chirality, and JOIN 1's first question resolves in
> favour of the cusped object. **Agree** ⇒ the wall extends past closedness *and* past the abelian
> sector, and the generation count cannot be a net-chirality count on this manifold at all.

**Scope, held:** B71 records that these coordinates are the **fiber group** ⟨a,b⟩, not the knot
group, and that *"a literal fiber↔knot coordinate dictionary is a separate identification (not
claimed here)."* Characters in Fix(T₁²) extend along the fibration; **which** extension is meant is
part of the deciding computation and is **not assumed here**.

## Controls (MB12, both directions)

- **The abelian test can detect a difference:** it is run at an **Alexander root**, where h¹ jumps,
  as well as at generic values — the selftest **asserts a jump was exercised**, so the equality is
  not the trivial 0 = 0.
- **Reciprocity is verified symbolically**, not cited.
- **Self-duality of every Sym^n is verified**, so §3 is a computation, not an assumption.

## Verification

`verification/where_chirality_can_live.py` — standalone.

- **Feeds on:** B1086 (the closed-double result now generalised), B1084/B1259, B102 (the SL(3)
  dichotomy and W1/W2), B71/B153 (the principal tower), E65.
- **Registers:** no change; sharpens **I-26**'s price.
