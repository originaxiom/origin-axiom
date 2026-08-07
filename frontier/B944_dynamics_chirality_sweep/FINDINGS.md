# B944 — THE DYNAMICS & CHIRALITY SWEEP: we already have both, and the two "gaps" are one

**Date:** 2026-08-07 · **Seat:** cc (banking) · **Lane:** MATHEMATICS / MAP. Gate 5
untouched; nothing to CLAIMS. **Owner directive:** *"we look for ratios not values maybe,
swipe the repo for dynamics scan and chirality as we might have all of it, maybe in the
other faces, child or combinations of all of it."*

---

## The headline

**Neither dynamics nor chirality is missing from this programme.** Both are extensively
banked. What is missing is one ℤ/2 — and the sweep's finding is that **it is the same
ℤ/2 in both cases, which is nowhere stated in the repo.**

| | arcs whose *verdict line* carries it | PROVED | NEGATIVE | OPEN |
|---|---|---|---|---|
| chirality | 102 | **70** | 32 | 0 |
| dynamics | 29 | **20** | 7 | 2 |

## 1. DYNAMICS — not a gap. The object is a named dynamical system, several times over.

| what we have | where |
|---|---|
| a **transcendental positive-entropy Painlevé-VI solution**, entropy 2 log λ_m — *outside* the algebraic Lisovyy–Tykhyy list | B317 |
| a working **Schlesinger/Painlevé-VI flow**, verified monodromy-preserving, carrying dynamical degree λ_m² | B169 |
| **Δ = −(ln λ_m/π)²** — the c=1 conformal dimension *equals* minus the squared topological entropy over 2π, **exact** | B196 |
| the trace-map flow's destination is a **golden-Anosov system** (Lyapunov 4 log φ, one conserved κ, modular symmetry) | B416 |
| the symbolic face is the **Sturmian subshift** — complexity n+1, **zero** entropy | B417 |
| algebraic entropy log((m+√(m²+4))/2) across the whole metallic family | B48 |
| a closed form for the regularized E₆ **dynamical zeta** (Fibonacci-square product, apparition-prime spectrum) | B423 |
| **two** torsions: golden dynamical zeta (−5) vs geometric holonomy torsion (Eisenstein, −3) | B425 |
| the object contains **its own symmetric-to-broken flow** — Dehn filling with CS(1,n) ~ −1/(2n) | B338 |
| the observer flow closes on 12 canonical systems, with ℤ/11 conserved along it | B540, B552, B560 |

Note the pair that matters: **B416 gives positive entropy (Anosov), B417 gives zero
entropy (Sturmian)** — the same object on two faces, at opposite ends of the entropy
scale. That is the two-ended object again, in dynamical clothing.

**The one dynamical negative that bites:** B721 — the object's own clock is **tracial
type II₁ with trivial modular flow**. It has dynamics; it has no *intrinsic* time.

## 2. CHIRALITY — not absent. It has been *constructed*.

| what we have | where |
|---|---|
| **chiral matter constructed**: the θ-odd-twisted mirror-double has E₆ reps with Zariski closure full E₆(ℂ), so its **27 is complex** | **B582** |
| **the switch is binary and identified**: any deformation with nonzero **θ-odd** component is chiral; θ-even stays F₄-stable and vector-like | **B576** |
| a closing *supplies* chirality: **all 31** sampled hyperbolic Dehn fillings make the amphichiral object chiral | B432 |
| the minimal chirality input is **slope ±5**; output = the Meyerhoff manifold, new arithmetic (disc −283) | B434 |
| **√−7 is the chirality field** — reached by *breaking* amphichirality | B316 |
| a chirality-**registering** measurement is defined (the B599 pairing datum) | B871 |
| the cascade's selection principle *requires* the 27's generation stay chiral — and **terminates at the SM** because the SM is the terminal registerable algebra | B861, B863 |
| amphichirality ⊥ the ℚ(√−3) Galois involution: two **orthogonal commuting ℤ/2 legs of a V₄** | B711 |

**And the ratio-shaped laws are already banked** — which is exactly what the directive
asks for:

> **B303**: the CP *sign* is literally the sign of Chern–Simons (CS = 0 ⟺ amphichiral).
> **B340**: the CP *phase* arg κ is extremal at **π/6** at the amphichiral cusp and
> decreases as **3.8 · CS²** — i.e. **second order in chirality**.

That is a dimensionless phase controlled by a dimensionless invariant, with no value
inserted anywhere. It is the shape the programme should have been hunting all along.

**The 32 chirality walls all say one thing**, and it is worth stating once: the object
cannot chirally sign *itself*. B713 (chirality is not in the amphichiral object), B760
(no object-native operation canonically signs the θ-odd sector — the object cannot close
itself), B252 (every conjugation-odd invariant vanishes or pairs), B849 (CS(m004) = 0;
amphichirality forces every orientation-odd invariant to 2-torsion). **Not "chirality
does not exist here" — "chirality is not self-supplied."**

## 3. THE UNBANKED CONNECTION — the two gaps are one ℤ/2

B717's capstone spine lists TIME and CHIRALITY as **separate rows, from separate arcs**
(B716 and B713). But read B716's probe 1 as written:

> the object's only internal time is the suspension of its Anosov monodromy … **no arrow**,
> because of **amphichiral time-reversal** (σ ~ σ⁻¹).

**The flow has no arrow for the same reason the object has no handedness: amphichirality.**
One unbroken involution, showing up as two different "missing" things on two different
faces. A grep confirms this identification appears **nowhere** in `frontier/`,
`docs/LAW_MAP.md` or `knowledge/` — the nearest statement is B467's *"the three thoughts
converge on the same ℤ/2"*, about a different trio.

If it holds, the consequence is sharp and cheap: **one closing supplies both** — the
arrow and the handedness together, not two separate inputs — and B340 then fixes the CP
phase to second order in the same closing's CS. Three of the programme's named gaps
would collapse to one choice.

## 4. THE SCOPING COMPUTATION — and it says NOT SO FAST

The tempting move is to assert the identification. It was tested instead, at the level
where the object's monodromy lives (φ = RL = [[2,1],[1,1]], trace 3):

- **time reversal** of the suspension: φ ↦ φ⁻¹
- **the mirror / chirality involution**: R ↔ L, i.e. φ ↦ JφJ = LR

**First result: they are not equal.** mirror ≠ inverse, as matrices.

**Second result, and the one that matters:** counting integer conjugators C with
CφC⁻¹ = target, by determinant —

| target | det +1 (orientation-preserving) | det −1 (orientation-reversing) |
|---|---|---|
| φ⁻¹ (time) | **6** | **8** |
| LR (mirror) | **8** | **6** |

**Both involutions are realized by conjugators of *both* determinants.** So the
matrix/GL(2,ℤ) level **does not decide** whether these are the same ℤ/2 — it cannot
separate them by orientation, which is precisely the discriminator the question turns on.

**This is the repo's own recurring trap, avoided rather than walked into**: the
abelianized/matrix level is *necessary, not sufficient* (`abelianization is not a
proxy`; `θ is trivial on the character variety`, where the same conflation was named
across three prior arcs). The question must be asked at the **mapping-class / 3-manifold
level**, where the amphichiral condition is the GHH anti-palindromic criterion already
banked (B134, B136, B613) and where fiber-orientation and base(S¹)-orientation reversal
are genuinely distinct ℤ/2's whose *product* is the total orientation reversal.

**Registered, not claimed.** See §6.

## 5. THE CHILDREN — swept, and the record says no

The directive asked about children explicitly. The answer is already banked and it is
negative, twice over:

- **B443**: the child program cleared **no** emergence bar — every floor is
  numerator-forced or shared with 5₂; nothing figure-eight-unique.
- **B718**: beyond H₁ = ℤ/p the child is **arithmetically generic** and authors no ADE
  skeleton (SL(2,F_p) is McKay only at p = 3, 5), with exactly three arithmetic children.
- **B437** is **RETRACTED**: the child's "golden return" was withdrawn as inheritance —
  the trefoil control showed ℚ(√5) is slope-5-forced, leaving only generic or
  class-shared content.
- B441/B442: the child's WRT field and E₆ data are forced by the surgery skeleton and
  commensurability-shared with 5₂.

**The children are not where the missing structure is.** The one thing they *do* supply
is the chirality input itself (slope ±5 → disc −283, B434) — the child is the *closing*,
not a source of new structure.

## 6. What this sweep registers (leads, not claims)

- **L126 — THE ONE-ℤ/2 QUESTION.** Is the amphichiral time-reversal of the Anosov
  suspension the *same* involution as the chirality/orientation ℤ/2? Must be posed at
  the mapping-class level; the matrix level is proved inadequate here (§4). If YES: one
  closing supplies arrow + handedness, and B340 fixes the CP phase from the same CS.
- **L127 — THE ENTROPY PAIR.** B416 (Anosov, entropy 4 log φ) and B417 (Sturmian,
  entropy 0) are the same object on two faces at opposite entropy ends. Is there a
  **ratio** law connecting them, in the shape of B196's exact Δ = −(ln λ_m/π)²?
- **L128 — THE CP RATIO CHAIN, branch-symmetric.** B303 (sign) + B340 (π/6, second order
  in CS) is the programme's cleanest already-banked ratio law touching a measured-side
  quantity. Under the B941 refinement it should be re-posed **symmetrically over all
  three branches** before it is ever compared to anything.

---

**Verdict: MAP + one scoping negative.** Dynamics and chirality are both richly banked;
the two named "gaps" are plausibly one unbroken ℤ/2; the identification is **not**
decidable at the level where it was tested, and is registered rather than asserted. The
children are a closed door. The ratio-shaped laws the directive asks for **already
exist** (B196, B303, B340) and had never been collected in one place.
