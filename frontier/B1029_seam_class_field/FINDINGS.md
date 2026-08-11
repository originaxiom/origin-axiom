# B1029 — THE SEAM IS NOT A THIRD FACE: its Hilbert class field *is* the two ends

**Date:** 2026-08-11 · **Lane:** MATHEMATICS, exact. Gate 5 untouched; nothing to `CLAIMS.md`.
**Band:** CONSOLIDATION REFRESH, B300–B399. **Files:** `compute.py` → `results.json` ·
lock `tests/test_b1029_seam_class_field.py`.

---

## 1. THE FINDING

THE CHAIN's **C7** banks the object's forced quadratic faces as **exactly three, a Klein
four-group**: being `ℚ(√−3)`, hearing `ℚ(√5)`, meeting `ℚ(√−15)`. That is on a curated surface.

**B334 says something strictly stronger, and is carried by no curated consolidation:**

> ### The Hilbert class field of the seam `ℚ(√−15)` **is exactly** `ℚ(√5, √−3)` — the compositum of the two ends.

So the third face is **not an independent third thing**. It is the field whose *class field* is
the other two. The Klein four-group is not three faces plus a relation — it is **two faces and
their class-field closure**.

## 2. VERIFIED HERE, elementary and self-contained

Genus theory for an imaginary quadratic field of class number 2 — no external tables:

| step | result |
|---|---|
| the seam is the product of the ends | `√5 · √−3 = √−15` |
| prime-discriminant factorisation | `disc ℚ(√5) = 5`, `disc ℚ(√−3) = −3`, and `5 · (−3) = −15` — both **prime discriminants** |
| class number, by counting reduced primitive forms of disc −15 | `[(1,1,4), (2,1,2)]` ⟹ **h = 2** |
| genus theory | `t = 2` prime discriminants ⟹ genus field has degree `2^(t−1) = 2` over the seam — **equal to h**, so the **genus field IS the Hilbert class field** |
| the compositum | `ℚ(√5, √−3)` has degree 4 over `ℚ`, hence **degree 2 over `ℚ(√−15)`** — matching |

**The two ends are exactly the two prime discriminants of the seam.** That is why the
factorisation is forced rather than chosen: `−15` has exactly one decomposition into prime
discriminants, and it is `5 × (−3)`.

## 3. WHY IT MATTERS TO THE PROGRAMME'S OWN THESIS

`THE_FRAMEWORK` Layer 1 presents the two ends as **geometry** — the cone-angle transition through
all three curvature signs, hyperbolic `ℚ(√−3)/E₆` to spherical `ℚ(√5)/E₈`. **B332** (also uncited;
registered as **L156** by B1027) derives the same two ends **algebraically**, from the two letters:
`R·L` has disc 5, `−R·L⁻¹` has disc −3.

**B1029 adds the third leg: given the two ends, the seam is forced by class field theory.** So the
Klein four-group of faces has three independent derivations — geometric (B248), combinatorial
(B332), arithmetic (B334) — and **only the first is on a curated surface.**

## 4. NOT CLAIMED

- **No novelty whatsoever.** Genus theory is classical (Gauss); that the genus field of a
  discriminant with two prime-discriminant factors is the compositum of those two quadratic fields
  is textbook. **The content is that this classical fact is what pins the object's third face, and
  that no consolidation says so.**
- **No physics.** These are number fields attached to the object's arithmetic, nothing more.
- **C7 is not corrected** — it is *sharpened*. Three faces forming a Klein four-group is true; the
  addition is that one of the three is determined by the other two.

---

**Verdict: PROVED.** The seam's Hilbert class field re-derived from scratch as the compositum of
the two ends, by counting forms and applying genus theory; and the programme's three-face
structure shown to be two faces plus a class-field closure.
