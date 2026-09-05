# B1259 — NO FLAT G₂ ORBIFOLD CAN SUPPLY ACHARYA–WITTEN ISOLATION: B1084's census was a theorem all along, and its hatch cannot be walked by changing the group

**Date:** 2026-09-06 · **Seat:** cc · **Status:** NEGATIVE (structural; two MB12 controls, one showing the statement is dimension-specific rather than trivial)

## The question — JOIN 1 of `docs/MAIN_GOAL.md`

**B1084** built the flat G₂ orbifold `(ℂ² × ℝ³)/Ĝ`, |Ĝ| = 96, and found: **one E₆ locus** with
pointwise stabilizer **exactly 2T**, three A₁ families, the Acharya–Witten **collision** criterion
**MET** at the apex — and **ISOLATION FAILS**, because the fixed-dimension census over the 95
nontrivial elements is **{3d: 53, 1d: 42}** with **no 0-dimensional fixed set**. Every A₁ locus
therefore meets E₆ along a **line**, every localized state extends along a flat direction, and all
matter is **vector-like**. It named the mechanism — *flatness ⇒ non-isolation ⇒ pairing* — and left a
**hatch**: *"chirality costs a deformation making an A₁ locus meet the E₆ locus at an isolated
transversal point — resolving the enhancement lines."*

**The hatch was never walked.** Verified across ~1180 arcs: only **one** declares a dependency on
B1084/B1086/B1087, and it is a bookkeeping follow-through. This arc asks whether it *can* be.

## The theorem

> **G₂ ⊂ SO(7)**, so every element acts on ℝ⁷ with **det = +1**.
> **Every element of SO(2k+1) has eigenvalue +1.** The characteristic polynomial is real of **odd**
> degree, so it has a real root; non-real eigenvalues come in conjugate pairs of modulus 1, each
> contributing **+1** to the determinant; the real eigenvalues are ±1 and their product must be
> **det = +1**; an **odd** number of them multiplying to +1 forces at least one to be **+1**.
> Hence **every nontrivial element of any flat G₂ orbifold group fixes at least a LINE**, and a
> 0-dimensional fixed set cannot occur — **for any Ĝ, not merely order 96.**

**So B1084's census result was forced.** It is not a property of that particular group of order 96;
it is a property of **flatness in seven dimensions**.

## Consequence

**Acharya–Witten isolation is unavailable in the entire class of flat G₂ orbifolds.** The hatch
cannot be walked by hunting a better finite group — **that whole search space is closed in one
line.** Chiral matter by this route requires genuine **curvature**: a *conical* G₂ singularity, whose
local model is a cone over a 6-manifold rather than a linear action on ℝ⁷.

This converts B1084's routed negative from an **empirical census** into a **structural no-go**, and
it is the kind of negative worth having: it says precisely what sort of object would be needed.

## What this does NOT say

**It does not say chirality is impossible.** The corpus has chirality **constructed** — B944's
census: **102 arcs, 70 PROVED** — by a different route entirely: the **θ-odd twisted, full-E₆(ℂ)**
frame (**B582**: Zariski closure full E₆(ℂ), so the 27 is genuinely complex; **B576**: the switch is
binary), with a **closing** supplying the bit (**B432/B434**: 31/31 sampled Dehn fillings chiralize).
It says the **flat G₂ route specifically** is closed.

**It also does not resolve JOIN 1.** The live problem stands: **B1086**'s spectrum law gives the
θ-odd (chiral) dial **h¹ = 2**, not 3, and **B1087** shows the charge operator commutes with neither
cusp holonomy. What this arc removes is one plausible-looking way out that would have cost a search.

## Controls (MB12, both directions)

- **The statement is dimension-specific, not trivial:** SO(6) elements generically **do** avoid
  eigenvalue +1 — **2000/2000** sampled — while SO(7) elements never do (**0/4000**).
- The parity argument is exhibited as **independent of |Ĝ|**, which is exactly what upgrades
  B1084's census to a statement about the class.

## Verification

`verification/flat_cannot_isolate.py` — standalone.

- **Feeds on:** B1084 (the orbifold and its hatch), B1086/B1087 (the spectrum law and the fourth
  language), B944 (the chirality census), B582/B576/B432 (the frame that does work).
- **Registers:** no identification change. Routes a **structural** node to the kill graph, replacing
  B1084's empirical one.
