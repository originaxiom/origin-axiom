# xB023 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-17. Sealed, hashed and pushed before any cell runs.**

## P0

A lemma about Chern–Simons classes of hyperbolic 3-manifolds under free orientation-reversing
involutions. Named mathematics. No value, no generation count, no physics reading, nothing to
`CLAIMS.md`. Gate 5 absolute.

## The owner's instruction

> *"do them properly and apply all the verifications u can think of, verify also banked data when u
> refer to them"*

— the second continuation xB021 fenced: **L194's open half.** xB020 established that complex
conjugation forces `CS` into the 2-torsion `{0, ¼}`; it did **not** derive **which of the two the
object takes.** That selection is what this arc attacks.

## WHAT WAS RUN BEFORE THIS SEAL (declared, not hidden)

1. `snappy.Manifold('m004').symmetry_group()` and `dir()` on its `Isometry` objects. **Result, which
   this arc will restate as cell W1 rather than assume:** `Isometry` exposes exactly
   `cusp_images, cusp_maps, extends_to_link, num_cusps` — **no translation part.** This confirms
   L194's stated instrument gap first-hand rather than on the lead's word.
2. Reading of L194's register entry, B1239's `FINDINGS.md`, B1235's bite-control paragraph.

**No cell of this arc has been run. No prediction below has been tested.**

## What is already banked, and its exact grade

L194, refined by B1239, splits the conjecture *"a free orientation-reversing deck kills the ¼ class"*
into three:

| case | banked status |
|---|---|
| closed manifolds | **closed** — APS `3η ≡ 2cs + τ (mod 2)`, `η = 0`, `τ ∈ ℤ` ⇒ `cs ∈ {0, ½}` mod 1 |
| cusped, no cusp fixed by the isometry | **closed** — B1239's swap corollary |
| **cusped with a τ-invariant cusp** | **OPEN. This is where m004 lives, and it is this arc's target.** |

**Every count above is re-derived in cell W0 before it is used.** B1239's bucket counts and B1235's
bite control are **not** taken on the record's word.

## THE CONFIGURATION AXES — declared first

| axis | values | this arc |
|---|---|---|
| **the locus** | the object `m004` / its sister `m003` / the one-cusped amphichiral census | **all three** |
| **the census window** | orientable cusped census, by tetrahedron count | **declared explicitly in the findings; results are stated relative to it and NOT generalised past it** |
| **the obstruction used** | free-quotient search (census-bounded) / a torsion obstruction (census-free) | **both, and their fences stated separately** |
| **held fixed** | SnapPy's `chern_simons()` reduced mod ½ | **stated; the 0-vs-½ distinction is invisible to it and this arc does not claim it** |

## The predictions — each falsifiable, each stated before the data

**W0 — re-derive the banked inputs.** Recompute, from SnapPy: `cs(m004)`, `cs(m003)`, `H₁(m004)`,
`H₁(m003)`, whether `m000`'s orientation double cover is `m004`, and whether `m003` is an orientation
double cover of any non-orientable census manifold. *Prediction:* `cs(m004) ≡ 0`, `cs(m003) ≡ ¼`,
`H₁(m004) = ℤ`, `H₁(m003) = ℤ ⊕ ℤ/5`, `m000 → m004` **yes**, `m003` **no**.
*Any mismatch halts the arc and is reported as a correction to the banked record.*

**W1 — the instrument gap, stated as a result.** Show by enumeration that SnapPy's `Isometry` carries
no translation part, so freeness on a τ-invariant cusp is **not** decidable from `cusp_maps()` alone.
*Prediction:* confirmed. *And the reason must be given, not just the API listing:* for an
involution with linear part of determinant `−1` the fixed-point condition depends **only** on the
translation along the `+1`-eigenvector, so the linear part **cannot** decide freeness. This cell must
prove that algebraically, not assert it.

**W2 — THE TORSION LAW, computed here rather than cited.** B1239 invokes a theorem of Kawauchi
(free involution ⇒ `Tor H₁ ≅ A ⊕ A`). **This arc has not read Kawauchi and will not cite it as a
theorem** — E58's clause, minted in this session for exactly this failure. Instead: take the
orientation double covers available in the census, compute `|Tor H₁|` for every one, and **measure**
whether it is always a perfect square.
*Prediction:* **every orientation double cover has `|Tor H₁|` a perfect square.**
*Grade it will carry:* a **computed law on N instances**, N stated, **not** a theorem.
*Refutation:* one orientation double cover with non-square torsion order kills the law, and the arc
must then drop it entirely rather than weaken it.

**W3 — THE SELECTION AT THE OBJECT.** *Prediction, and the sharpest thing this arc can deliver:*
`|Tor H₁(m003)| = 5`, **not a perfect square**, so under W2's law `m003` admits **no** free
orientation-reversing involution — while `m004` has `Tor H₁ = 0`, trivially square, and does admit
one (`m000`). **If both hold, the selection of `0` over `¼` at the object is explained by a property
of `H₁`, which is exactly the invariant xB022 predicts A5 moves.**
*Kill condition, binding:* if `m003` turns out to admit a free orientation-reversing involution, or
if `|Tor H₁(m003)|` is square, **this explanation is dead and must be reported dead.**

**W4 — THE CENSUS TEST, both directions, with base rates.** Over the one-cusped amphichiral census
window: classify by `CS` class (`0` vs `¼`) and by whether the manifold is an orientation double
cover.
*Prediction:* **no ¼-class manifold is an orientation double cover**, and a substantial fraction of
`0`-class ones are. *Required:* the **base rate** of `0` among amphichiral manifolds that are **not**
orientation double covers — without it, "the free ones are all at 0" is not evidence.
*Kill condition, binding:* **one ¼-class orientation double cover kills L194's conjecture outright,**
and this arc must report that as the headline if it happens.

**W5 — THE TORSION FILTER APPLIED TO THE ¼ CLASS.** *Prediction:* ¼-class amphichiral manifolds have
`|Tor H₁|` non-square at a rate **significantly above** the base rate among `0`-class ones.
*Required honesty:* if the rates are comparable, the filter explains nothing and the arc must say so.

**W6 — WHAT REMAINS OPEN.** The cusp-local lemma in full generality requires the translation part
this arc does not compute. *Declared in advance:* **this arc does not close L194.** It may narrow it
at the object. Any sentence in the findings that reads as "L194 is closed" is a violation of this
seal.

## Controls required before any cell counts

- **Every banked number recomputed** (W0), and any that disagrees reported as a correction.
- **A base rate beside every rate** (W4, W5) — the E-class this session hit twice.
- **A positive control** for the orientation-cover search: `m000 → m004` must be found by the same
  code that reports the negatives, or the negatives are void. This is the swallowed-`RuntimeError`
  lesson from earlier in this session, applied in advance.
- **Exactness:** torsion orders are exact integers; `CS` comparisons carry a declared tolerance and
  a declared modulus.
- **The census fence stated numerically**, not as a hedge.

## What this arc may NOT conclude

It may not conclude L194. It may not promote W2's measured law to a theorem, nor cite Kawauchi for
it. It may not claim the `0`-vs-`½` distinction, which SnapPy's mod-½ readout cannot see. It supplies
no value and nothing reaches `CLAIMS.md`.
