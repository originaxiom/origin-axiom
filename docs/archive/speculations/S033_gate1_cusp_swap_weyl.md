# S033 — "Gate-1": does a cusp-swap symmetry give a *simple non-abelian* factor? (the Whitehead probe)

**Status: `OPEN(MATH) · prior LOW · tool-gated` — FIREWALLED.** Nothing here promotes to `../CLAIMS.md`; P1–P16,
B85 untouched. This is a firewalled speculation with an *emergent-physics shadow only* — the leap to fundamental
physics is **not** on the table (see Boundary). Provenance: CHAT-1 LEADS REGISTER §D (lead L13).

## The lead

Each cusp of a hyperbolic 3-manifold contributes a `U(1)` to the 3d-3d gauge content (Mostow rigidity: the
peripheral data is abelian). A **simple non-abelian** factor (the SM-relevant `SU(2)`, `SU(3)`) would need the
gauge structure to mix cusps — concretely, a **cusp-swap symmetry** acting as a **Weyl reflection** on the
peripheral lattice, fusing two `U(1)`s into a rank-≥2 non-abelian factor. The metallic bundles are single-cusped,
so they cannot host this. The natural minimal multi-cusped test object is the **Whitehead link** complement (two
cusps, hyperbolic, census-standard, admits a cusp-exchanging symmetry).

> **The question.** Does the Whitehead link's cusp-exchange symmetry act on the 3d-3d gauge data as a genuine
> **Weyl reflection** producing a simple non-abelian factor — or does it remain an *abelian* permutation of two
> independent `U(1)`s (a `U(1)×U(1)⋊ℤ/2`, not an `SU(2)`)?

## Why the prior is LOW

- The peripheral structure is abelian by Mostow; a symmetry *permuting* cusps need not *fuse* their `U(1)`s into a
  simple factor — the generic outcome is a semidirect product, not a simple group.
- This is the **same wall** as `S029` (`H₁`-torsion ↦ one-form symmetry, but `T[M]` is rank-1 **abelian** so the
  `ℤ/m` is a line-spectrum symmetry, not an `SU(m)` gauge group) and the `S028` functorial hinge — each time a
  discrete/permutation symmetry is asked to become a *gauge* group, the abelian wall holds.
- The honest expectation is **negative** (the cusp-swap symmetrizes rather than fuses); a positive result would be
  surprising and would still be **emergent**, not fundamental.

## Why it is worth recording anyway

It is the **cleanest falsifiable test** of "can multiplicity (more cusps) manufacture a non-abelian factor?" — a
direct, named object with a known symmetry, rather than a vague hope. Either outcome is informative: a negative
hardens the firewall ("even a cusp-swap stays abelian"); a positive opens "Gate-1" as a genuine (emergent) lead.

## What running it needs (the tool gate)

Computing the 3d-3d gauge data and the symmetry's action on the peripheral/Ptolemy lattice needs **Sage + GKLP**
(Garoufalidis–Kashaev–Lawrence–Penner / `ptolemy_variety`-level machinery) — not available in the current
sandbox. First pass (trace-level, no Sage): check whether the cusp-exchange isometry acts on the peripheral trace
coordinates as a reflection (eigenvalue −1 on a peripheral root) or as a permutation that fixes the abelian
splitting. NEEDS-EXPERTISE / tool-gated; queued as an **open lead**, unrun.

## Boundary

Even a positive Gate-1 result would be a **non-abelian factor in an emergent 3d-3d / aperiodic-order gauge
theory**, *not* the Standard Model's gauge group, and would carry **no** chirality (that is structurally blocked,
the `P009` det=−1→CS=0 root cause). The firewall to fundamental physics is **not** tested by this probe. This sits
with the other firewalled `S`-entries (`S029`, `S028`), distinct from the MATH-only `S031`/`S032`.

**Anchors:** `S029` (the abelian-wall sibling: torsion↦one-form symmetry, rank-1 abelian `T[M]`), `S028` (the
functorial hinge), `../knowledge/K006` (the 3d-3d correspondence), `../philosophy/P009` (det=−1→CS=0, the
chirality block that rides along). External: Whitehead link complement (two-cusped, cusp-exchanging symmetry);
Garoufalidis–Kashaev / Ptolemy varieties; Mostow rigidity.
