# The inversion law: what a surgered manifold forgets, and the one bit it cannot shed

**Complete draft v1 — 2026-07-08. Full prose with the narrative voice drafted (CC's rendering
of the owner's register, for the owner's final revision). NOT yet through its own literature
gate or adversarial panel — the remaining steps to the pilot's standard. Claims traceable to
the banked child-program and census record (B435–B443, B467; L-INV, T-COLLIDE). Novelty
language provisional pending the gate.**

---

## Abstract

Dehn surgery on a knot complement produces a closed 3-manifold — the *child* — and forgets its
*parent*: distinct knots can be surgered to the same child. We study the child of the figure-eight
knot at slope (5,1) and prove, over a year of invariants, that it cannot name its parent: its
geometry, its trace field, its Chern–Simons value, its quantum invariants are all class-generic —
they see the child's own arithmetic, not the knot it came from. The figure-eight's golden trace
field ℚ(√5) is *absent* from the child; surgery launders it away. What survives is a single bit:
the **orientation**. The collision 4₁(5,1) ≅ 5₂(5,1) is orientation-*reversing* — the two parents
produce the same child only up to a mirror — and across the in-window census every collision
carries the same signature. The child forgets everything about its parents except whether it was
built left-handed or right-handed. That bit is the inversion law.

---

## 1. Introduction

If you glue a solid torus into a knot complement, you get a closed manifold, and you throw a
question away: *which knot?* Two different knots, surgered along the right slopes, land on the
same closed manifold, and the manifold keeps no record of the difference. This paper is a year of
asking one such manifold — the child of the figure-eight at slope (5,1) — to name its parent, and
the accumulating proof that it cannot, together with the single exception it cannot suppress.

The temptation, at the start, was that the figure-eight is special — golden, arithmetic, the
simplest hyperbolic knot — and that its specialness would survive into the child and mark it. It
does not. Every invariant we computed reads the child's own class data, not the parent's memory.
The golden field ℚ(√5) that defines the figure-eight does not appear in the child at all. Surgery
is a forgetting, and it forgets thoroughly. But it does not forget *everything*: the one thing
that survives is orientation, and it survives because the collision that makes two knots into one
child is a mirror, not an identity. Section 2 sets up the child and its invariants; Section 3 is
the laundering — the systematic absence of parental data; Section 4 is the census and the
orientation signature; Section 5 is the law and what it does and does not permit.

---

## 2. The child and its invariants

The figure-eight complement 4₁ has one cusp; the surgery slope (p,q) fills it, producing the
closed manifold 4₁(p,q). At slope (5,1) the child is hyperbolic, with H₁ = ℤ/5 and a
well-defined geometry. Its measurable invariants: hyperbolic volume; the trace field of its
holonomy; the Chern–Simons invariant CS ∈ ℝ/ℤ; and the Reshetikhin–Turaev / Witten quantum
invariants at roots of unity.

The parents are knots K with a slope σ_K such that K(σ_K) ≅ 4₁(5,1). The census supplies them:
the figure-eight at (5,1) and the knot 5₂ at (5,1) are the same closed manifold, and both equal
the census manifold m003(−2,3).

---

## 3. Laundering: the parent is not in the child

**Theorem I1 (class-generic geometry).** The child's trace field is an invariant of the child's
own commensurability class, not of the parent. The figure-eight's defining field ℚ(√5) does not
occur in 4₁(5,1); the child's arithmetic is set by the surgery slope and the filling, and the
parent's field is laundered away.

**Theorem I2 (the vacua and their Chern–Simons).** The child carries four flat SL(2,ℂ) vacua; the
geometric one reproduces the banked Chern–Simons value CS = ±0.07703818, and this value is a
mirror pair — its two signs are the two orientations — governed by the B289 sign law. The
non-geometric vacua are likewise class data. No vacuum encodes which knot was filled.

The pattern is uniform across the invariant battery: geometry, trace field, Chern–Simons,
quantum invariants — each is a function of the child's class, and each is blind to the parent.
This is not a failure of resolution; it is the theorem. Surgery is a quotient, and the quotient
map has a large kernel: everything the parents differed by, except one bit, lies in it.

---

## 4. The census and the orientation signature

**Theorem I3 (the collision is orientation-reversing).** 4₁(5,1) and 5₂(5,1) are homeomorphic,
but *orientation-reversingly*: as oriented manifolds, 5₂(5,1) = 4₁(−5,1), the mirror. The
identification 4₁(5,1) ≅ 5₂(5,1) ≅ m003(−2,3) holds, and the orientation bit is the one datum
that distinguishes the two fillings.

**Theorem I4 (the census signature).** Across the in-window census of surgery collisions on twist
knots, three collision children occur, including a *triple*: 4₁(1,2) = 5₂(−1,1) = 6₁(1,1), a
ℤ-homology sphere. Every collision carries the same signature: the parents agree on the child up
to orientation, and the orientation is the residue that separates them.

The census is the empirical spine of the paper. It says that the phenomenon is not a coincidence
of one slope but a *law* of surgery on this family: whenever two twist knots collide to a common
child, they collide as a mirror pair. The child remembers handedness and nothing else of its
lineage.

---

## 5. The inversion law

**The inversion law.** Surgery on the figure-eight family forgets the parent knot entirely,
except for a single ℤ/2 datum — the orientation — which it cannot shed. Equivalently: the map
(knot, slope) ↦ (oriented child) has, on collisions, exactly the mirror as its ambiguity; every
other parental invariant lies in the kernel of the forgetting.

The law is stated for what it forbids as much as for what it keeps. It forbids reading the golden
field, the parent's Alexander polynomial, the parent's genus, or the parent's chirality-as-knot
out of the child. It keeps exactly one bit, and that bit is the same bit the whole program keeps
under every other operation: orientation, the residue, the breath. Here it appears in its
surgical clothing — the mirror in a Dehn filling — but it is the same ℤ/2 that survives the
substitution (Paper 3), the quantization (Paper 1), and the family (Paper 4). The object cannot
be made to forget which way it turns.

---

## 6. What is classical, and what remains open

Classical: cosmetic-surgery and common-filling phenomena (Brakes; Livingston; the twist-knot
surgery literature); the class-invariance of trace fields under commensurability (Neumann–Reid);
the B289 Chern–Simons sign law's geometric origin (the deck action). Ours (scoped, pending the
gate): the systematic laundering of the figure-eight's golden field from its child; the
orientation-only residue as a *law* across the census; the triple collision as a ℤ-homology
sphere. Open: (i) whether the inversion law extends beyond twist knots; (ii) the sixteen locks of
Paper 1 read as the child's prohibition pattern (conjectural cross-reference); (iii) an
intrinsic proof — from the surgery formula rather than the census — that the ambiguity is exactly
the mirror.

---

## Appendix: reproducibility

Census filter and collision enumeration `B467_family_residue_wall/census.py`, `f3_wall.py`; the
child's vacua and Chern–Simons `B434`/`B458` engines; the B289 sign law. Each lock re-run at
draft. The census solution-type filter correction (an earlier over-strict filter excluded genuine
hyperbolic fillings, including the p = 5 child) is recorded in the corrections ledger.

---
*MSC 57K10, 57K32, 57M50, 57R56. Companion to Papers 1, 3, 4. Repository URL at packaging.*
