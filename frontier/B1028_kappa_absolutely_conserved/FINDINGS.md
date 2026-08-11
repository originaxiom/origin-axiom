# B1028 — κ = 2 IS ABSOLUTELY CONSERVED: every endomorphism of F₂ scales κ − 2, and the information-losing ones land *inside* "nothing"

**Date:** 2026-08-11 · **Lane:** MATHEMATICS, exact. Gate 5 untouched; nothing to `CLAIMS.md`.
**Band:** CONSOLIDATION REFRESH, B400–B499 — the densest debt band after the v3 recount.
**Files:** `compute.py` → `results.json` · lock `tests/test_b1028_kappa_conserved.py`.

---

## 1. THE FINDING

**B497** classifies `End(F₂)` acting on the character variety into four strata and proves a law
for each. **It is carried by no curated consolidation**, and it completes the κ picture that
B1027 opened.

| stratum | citizen | **κ-law (re-verified here)** |
|---|---|---|
| **1** — injective, det ±1 (**Aut**) | the metallic `a→aᵐb, b→a` — *the programme's own* | **κ′ = κ** |
| **2** — injective, \|det\| ≥ 2 | `A→A², B→B²` | **κ′ − 2 = (κ − 2)·x²y²** |
| **3** — injective, det 0 | Thue–Morse `a→AB, b→BA` | **κ′ − 2 = (κ − 2)(x² + y² − xyz)** |
| **4** — **non-injective** | `a→ab, b→ab` | **image ⊆ {κ = 2}** |

> ### Every law is a multiple of **κ − 2**. So κ − 2 — the *obstruction*, the thing the founding sentence is about — is exactly what an endomorphism scales, and **κ = 2 is invariant under every endomorphism of F₂**.

**And stratum 4 is the sharpest line.** A non-injective endomorphism — one that *loses
information* — has its whole image inside `κ = 2`. Verified: `a→ab, b→ab` sends both generators
to one word `w`, so the image is cyclic, and in trace coordinates
`(x′,y′,z′) = (z, z, z²−2)` gives **κ′ = 2 identically, for every z**.

**Stated plainly:** *the cancellation completes exactly when the map forgets which letter was
which.* That is the same collapse B1027 found at λ = 0 on the transfer-matrix face — there the
two letters become the same **matrix**; here they become the same **word**. Two faces, one
mechanism.

## 2. WHAT THIS ADDS TO B1027

B1027 gave κ = 2 three meanings. This is the fourth, and it is the only *functorial* one:

| face | κ = 2 is | arc |
|---|---|---|
| founding | the cancellation completes ⟺ **nothing** | B309/B518 |
| transfer-matrix | **λ = 0**, the free metal of a *measured* chain | B160 · B505 |
| spectral | the **unique** fiber with positive-measure spectrum | B162 |
| **functorial** | **absolutely conserved** — fixed by *every* endomorphism, and the image of every information-losing one | **B497** |

## 3. A SCOPE STATEMENT THE PROGRAMME OWES ITSELF

B497's own sentence, and it is in no consolidation:

> **"The program to date = stratum 1 of 4."**

The whole corpus works in the **automorphism** stratum, where **κ′ = κ** — κ is conserved *because
of where the programme stands*, not as a general fact about the object's maps. Strata 2–4 exist,
have exact laws, and are unexplored. That is a first-order scope statement about the entire
research programme.

B497 also notes the second stratum's `x²−2` component **is the Chebyshev map**, so via the banked
P3 anchor (`L+R` = the Ising transfer matrix) `A→A²` is **literally transfer-matrix decimation** —
*"the RG face is matrix-level, not metaphor."*

## 4. AN ERROR THIS ARC MADE AND CAUGHT

The first run modelled stratum 4 as `(z, z, z)` and **FAILED**. Wrong: `φ(ab) = w·w`, not `w`, so
`z′ = tr(w²) = z² − 2` by Cayley–Hamilton. **The check caught my modelling error, not B497's
law** — recorded because a passing test on a wrong model would have "confirmed" the law without
touching it.

## 5. TWO NEIGHBOURS IN THE SAME BAND, verified present and uncited

- **B416** — the trace-map flow's destination is a **golden-Anosov** system: Lyapunov `{0, ±4 log φ}`,
  one conserved κ, modular symmetry. **Its own bar check says NOT CLEARED**, and its control is
  sharp: the golden-Anosov structure is *generic* to the metallic family, *"not even
  figure-eight-specific."*
- **B417** — the symbolic face is the **Sturmian subshift**: complexity `n+1`, **entropy 0**,
  gap group `ℤ+ℤφ`. Also **NOT CLEARED**; other Sturmians give `ℤ+ℤα`.

**Together they are a genuine two-faced fact the consolidations do not state:** the *flow* has
positive entropy `4 log φ` while the *subshift* has **zero** entropy — two dynamical faces of one
object — and **both arcs record their own bar as unmet.** Honest negatives, uncited.

## 6. NOT CLAIMED

- **No novelty.** The Hopf dichotomy is Nielsen–Schreier + Mal'cev (B497 cites it as folklore);
  the κ-invariance of the reducible locus is known. **The content is the re-verification and the
  joining to B1027's κ = 2 cluster.**
- **B497's stratum-1 citizen is the programme's own trace map**, so "κ′ = κ" is not independent
  evidence for anything the programme claims — it is the statement of where it stands.
- **B416/B417 are cited, not re-verified** here.

---

**Verdict: PROVED.** Four exact κ-laws re-derived from the substitutions; κ − 2 shown to be the
coordinate every endomorphism scales; κ = 2 shown invariant under all four strata and equal to the
whole image of the non-injective one; and the programme's own position located at stratum 1 of 4.
