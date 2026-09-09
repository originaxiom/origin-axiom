# B1263 — I-6's side A verified, its multiplicity measured at TWO, and a tempting reading refuted

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact, finite; three MB12 controls) · **Price: unchanged at 14**

## Why this arc

**B1261** made the identification ledger the scoreboard (price = 4 axioms + UNEARNED rows) and
**B1262** moved it **15 → 14** by running a discriminator a row had been carrying unrun. This arc
audits the next candidate. **I-6** — *π₁(m004) ↠ 2T ≡ the 6d type's ALE Γ* — has a **side A** that is
a finite, decidable group-theoretic claim, and **nobody had checked it.**

## 1. Side A is real — so the row is NOT refutable there

Enumerating all 24² = 576 pairs in **2T = SL(2,3)** and imposing the relator `abABaBAbaB = I`:

> **72 homomorphisms π₁(m004) → 2T, of which 48 are SURJECTIVE.**

The object really does have 2T quotients. **I-6 stays UNEARNED; the price stays at 14.** This is a
negative result for the cheap move, and it is worth recording as such: the row survives its first
real test.

## 2. But "THE 2T" is not well defined — there are two

Those 48 surjections fall into:

| acting group | orbits |
|---|---|
| inner automorphisms (conjugation by 2T) | **4** |
| **full Aut(2T) = S₄** (order 24, *constructed*, not assumed) | **2** |

> **The object supplies TWO genuinely distinct 2T quotients, never one.**

This is the **H5 pattern at a sixth level** — after the closing (C22), the order (A7), the partner
(B1192), the sl₂ embedding (I-25) and n (B1248). *Every space, never a point.*

**It sharpens I-6's price:** earning the row needs not merely a map to the transverse ALE Γ, but a
statement of **which** of the two quotients is meant — or a proof that the map is independent of the
choice.

## 3. The tempting reading, tested and REFUTED

Two quotients invites the reading that they are **mirror images**, so that choosing one *is* the
orientation bit — which would tie I-6 straight into the chirality story. **It is false.**

Four relator-preserving automorphisms of π₁ — `a↔b`; `a,b → a⁻¹,b⁻¹`; the composite; and
`a → a, b → aba⁻¹` — each map surjections to surjections, and **every one fixes both Aut-orbits,
48/48. No tested symmetry exchanges the two quotients.**

So the choice between them is a **genuine binary with no symmetry reason to prefer either**, and it
is **not** the orientation bit. *(This arc's own hypothesis, killed by its own control.)*

## Controls (MB12, both directions)

- **The group is validated:** |SL(2,3)| = 24 checked, and **|Aut(2T)| = 24 is constructed** by
  extending generator images and rejecting non-bijections — not assumed.
- **The orbit count is sensitive to what acts:** inner gives **4**, full Aut gives **2** — so the
  counting is not a fixed point of the method.
- **The symmetry test can detect a swap:** it reports swapped/fixed per automorphism, and a map
  failing to preserve the relator is asserted against rather than silently counted.

## Verification

`verification/two_2T_quotients.py` — standalone, finite, exact.

- **Feeds on:** B1261 (the price), B1262 (the third move), B1228 (where I-6 was registered), B1146,
  B302, I-1 (McKay, EARNED).
- **Registers:** I-6 unchanged **UNEARNED**, price detail sharpened.

---

# PART 2 — Does Fibonacci/golden play a role? Structurally YES; as the mirror, NO

*(Owner's question mid-arc: "does or could a ab fibonaci or golden play a role here?")*

## It does, and the corpus already carried it

**B71's own header** records the monodromy as **φ = [[2,1],[1,1]] = M²** with **M the Fibonacci
matrix**. Verified here from the substitutions themselves:

| | substitution | abelianisation | det |
|---|---|---|---|
| **σ** | x → xy, y → x — **the Fibonacci substitution** | **[[1,1],[1,0]]** | **−1 → ORIENTATION-REVERSING** |
| **σ²** | x → xyx, y → xy | **[[2,1],[1,1]]** — the banked monodromy | **+1** |

> **The object's monodromy is the SQUARE of an orientation-reversing map** — which is the
> amphichirality structure itself, written in the fibration's own language. Two other golden facts
> surfaced independently this session: the Alexander polynomial **Δ = t² − 3t + 1** has roots
> **φ²** and **φ⁻²**, and B1260 found it **reciprocal**.

## The cross-check that works — and the diagnostic that found it

A fibered knot's fiber is the **commutator subgroup**, so a surjection π₁ ↠ 2T restricts on the fiber
to **[2T, 2T] = Q₈** (order 8; 2T/Q₈ ≅ ℤ/3), **not** to 2T. Asking the fiber to surject onto 2T
returns **0** monodromy-invariant pairs — kept in the script, because that zero is what located the
wrong target rather than a dead end. With the right one:

```
generating pairs F2 ->> Q8                        : 24
invariant under the monodromy up to 2T-conjugacy  : 24   (all extend)
monodromy-invariant CLASSES up to 2T-conjugacy    :  2
```

> **And that 2 MATCHES part 1's two Aut(2T)-orbits, computed from the KNOT presentation.**
> Two independent presentations, the same answer, **with no fiber↔knot dictionary assumed** — which
> matters, since B71 records that dictionary as a separate, unclaimed identification.

## And the tempting consequence is refuted — now from the second side

If σ is the orientation-reversing half, the two classes might be its two "sides", making the choice of
2T quotient **the orientation bit**. **False: σ FIXES each class — 0 swapped, 24 fixed.** Combined
with part 1 (four knot-group automorphisms, **48/48 fixed**), **the reading fails from both
presentations.**

**So: the 2-fold multiplicity is real and now cross-checked, and Fibonacci does not explain it.** The
golden structure is genuinely present — it *is* the monodromy — but it is not the source of the binary.

**Controls:** the abelianisations are computed and checked against the banked monodromy, not assumed;
|[2T,2T]| = 8 is computed; the wrong-target run is retained and reported; the swap test reports
swapped and fixed separately and would show a swap if one existed.
