# The inversion law — [FROZEN INTERNAL NOTE, NOT PUBLICATION-READY]

**⚠ FROZEN (2026-07-09) as an internal note.** After three adversarial re-panel rounds, this write-up
still carries framing/labelling defects (documented in `SCRUTINY_P1P3_round3.md`) — notably that the
"≤ one bit" law is partly tautological (a collision is *defined* by a shared unoriented child). Retained
as an internal record only; **the verified computations live in the cited B-nodes** (B435–B443, B467).
Do not circulate as a paper.

**Complete draft v3 — 2026-07-09. v3 fixes the re-panel (round 2) precision findings: (a) "no
quadratic subfield" is justified by the **S₄** Galois group (the point-stabilizer S₃ is maximal), not
by the discriminant being non-square (an invalid inference — C₄/D₄ quartics have non-square disc yet
do have quadratic subfields); (b) the laundering is reframed structurally (an S₄-generic quartic sharing
no subfield with the parent), since — the child having no quadratic subfield — the bare "field X is
absent" is vacuous for every quadratic X, ℚ(√−3) included. v2 (2026-07-08) fixed v1's two fatal errors:
a misidentified trace field (ℚ(√5) for ℚ(√−3)) and an over-strong orientation law (claimed uniformly
orientation-reversing; the paper's own triple is orientation-preserving); the thesis was weakened to the
0-or-1-bit residue. Full prose in the owner's register. NOT yet re-cleared. Claims traceable to the
banked child-program and census record (B435–B443, B467; L-INV, T-COLLIDE), re-verified at revision
(snappy trace fields; S₄ Galois group; conjugate embeddings).**

---

## Abstract

Dehn surgery on a knot complement produces a closed 3-manifold — the *child* — and forgets its
*parent*: distinct knots can be surgered to the same child. We study the child of the figure-eight
knot at slope (5,1) and prove, over a year of invariants, that it cannot name its parent: its
geometry, its trace field, its Chern–Simons value, its quantum invariants are all class-generic —
they see the child's own arithmetic, not the knot it came from. The figure-eight's invariant trace
field ℚ(√−3) is *absent* from the child: the child's trace field is the quartic ℚ[x]/(x⁴ − x − 1),
a field with Galois group S₄ and **no quadratic subfield at all**, so no quadratic parent-field can survive. What
can survive a collision is at most a single bit — the **orientation** — and even that survives only
sometimes. The collision 4₁(5,1) ≅ 5₂(5,1) is orientation-*reversing*: the two children are a
mirror pair (conjugate geometric embeddings of the same quartic, Chern–Simons ±0.07703818), so
here orientation is the one datum that distinguishes the parents. But the twist-knot *triple*
4₁(1,2) = 5₂(−1,1) = 6₁(1,1) is orientation-*preserving* (one oriented manifold, equal
Chern–Simons), so there orientation distinguishes nothing. The surviving parental data is therefore
zero or one bit, never more, and which of the two depends on the collision. That is the inversion
law: surgery on this family launders the parent's arithmetic completely, and what is left is at
most orientation.

---

## 1. Introduction

If you glue a solid torus into a knot complement, you get a closed manifold, and you throw a
question away: *which knot?* Two different knots, surgered along the right slopes, land on the
same closed manifold, and the manifold keeps no record of the difference. This paper is a year of
asking one such manifold — the child of the figure-eight at slope (5,1) — to name its parent, and
the accumulating proof that it cannot, together with an honest account of the single bit that
sometimes, but not always, survives.

The temptation, at the start, was that the figure-eight is special — arithmetic, the simplest
hyperbolic knot, its trace field the Eisenstein field ℚ(√−3) — and that its specialness would
survive into the child and mark it. It does not. Every invariant we computed reads the child's own
class data, not the parent's memory. The field ℚ(√−3) that defines the figure-eight does not
appear in the child at all; indeed the child's trace field has no quadratic subfield to hold it.
Surgery is a forgetting, and it forgets thoroughly. The one candidate for a survivor is
orientation — and here the story is subtler than we first wrote it. Sometimes the collision that
merges two knots into one child is a mirror, and then orientation is exactly the surviving
distinction. Sometimes the collision is orientation-preserving, and then even orientation is gone.
Section 2 sets up the child and its invariants; Section 3 is the laundering — the systematic
absence of parental data; Section 4 is the census and the *non-uniform* orientation signature;
Section 5 is the law, stated for what it forbids and honest about what it keeps.

---

## 2. The child and its invariants

The figure-eight complement 4₁ has one cusp; the surgery slope (p,q) fills it, producing the
closed manifold 4₁(p,q). At slope (5,1) the child is hyperbolic, with volume 0.9813688, H₁ = ℤ/5,
and a well-defined geometry. Its measurable invariants: hyperbolic volume; the trace field of its
holonomy; the Chern–Simons invariant CS ∈ ℝ/ℤ; and the Reshetikhin–Turaev / Witten quantum
invariants at roots of unity.

The parents are knots K with a slope σ_K such that K(σ_K) ≅ 4₁(5,1). The census supplies them:
the figure-eight at (5,1) and the knot 5₂ at (5,1) are the same closed manifold, both equal to the
census manifold m003(−2,3).

For orientation bookkeeping, recall the diagnostic used throughout: for an oriented hyperbolic
3-manifold, the trace field carries a distinguished *geometric* complex embedding (the one through
which the holonomy is read), and the mirror image carries its complex conjugate. Two children with
the same abstract trace field but conjugate geometric embeddings are mirror images; two with the
same embedding are the same oriented manifold. Chern–Simons is the numerical shadow of the same
bit: CS(M̄) = −CS(M).

---

## 3. Laundering: the parent is not in the child

**Theorem I1 (class-generic geometry; the field is laundered).** The child's trace field is an
invariant of the child's own commensurability class, not of the parent. Concretely, the trace
field of 4₁(5,1) is the quartic field ℚ[x]/(x⁴ − x − 1), whose Galois group is **S₄** (order 24,
CC-verified; discriminant −283). Because the point-stabilizer S₃ is maximal in S₄, this quartic
field has **no proper subfield at all** — in particular no quadratic subfield. So the child's field
is an S₄-generic quartic, sharing *no* subfield with the parent's ℚ(√−3): the parent's arithmetic
is laundered away by the filling.

*Remark (avoiding a vacuity trap).* One must not confuse two fields of the figure-eight. Its
*invariant trace field* is ℚ(√−3) (the Eisenstein field, disc −3; 4₁ is the arithmetic manifold
of PSL₂(O₃)). The golden field ℚ(√5) that appears everywhere else in this program is the field of
the *monodromy eigenvalue* — the metallic mean λ₁ = φ — a different object living upstairs in the
mapping-class data, not in the hyperbolic trace field. Now, *because* the child has no quadratic
subfield, the bare statement "field X is absent from the child" is vacuous for *every* quadratic X
— including ℚ(√−3) — so the laundering content is not "a particular field is missing" (an earlier
draft's ℚ(√5)→ℚ(√−3) fix merely traded one vacuous absence for another). The honest, non-vacuous
statement is structural: the child's trace field is an S₄-generic quartic with no subfield shared
with the parent — the parent's field is not recoverable because the child's field has *no room* to
contain it, and the two share nothing below the full quartic.

**Theorem I2 (the vacua and their Chern–Simons).** The child carries four flat SL(2,ℂ) vacua; the
geometric one reproduces the banked Chern–Simons value CS = ±0.07703818, and this value is a
mirror pair — its two signs are the two orientations — governed by the B289 sign law. The
non-geometric vacua are likewise class data. No vacuum encodes which knot was filled.

The pattern is uniform across the invariant battery: geometry, trace field, Chern–Simons, quantum
invariants — each is a function of the child's class, and each is blind to the parent. This is not
a failure of resolution; it is the theorem. Surgery is a quotient, and the quotient map has a
large kernel: everything the parents differed by, save at most one bit, lies in it.

---

## 4. The census and the orientation signature (non-uniform)

**Theorem I3 (the (5,1) collision is orientation-reversing).** 4₁(5,1) and 5₂(5,1) are the same
underlying manifold m003(−2,3), but as *oriented* manifolds they are mirror images. The evidence is
arithmetic and geometric at once: both have trace field ℚ[x]/(x⁴ − x − 1), but with **complex
conjugate** geometric embeddings (root −0.2481 + 1.0340 i for 4₁(5,1), root −0.2481 − 1.0340 i for
5₂(5,1)), and their Chern–Simons values are the mirror pair ±0.07703818. Here the orientation bit
is the one datum that distinguishes the two fillings.

**Theorem I4 (the triple is orientation-preserving — the law is not uniform).** Across the
in-window census of surgery collisions on twist knots, a *triple* also occurs: 4₁(1,2) = 5₂(−1,1)
= 6₁(1,1), a ℤ-homology sphere (H₁ = 0, volume 1.3985089). These three fillings are the *same
oriented* manifold — equal Chern–Simons (CS = −0.246607, not a ± pair) — so the collision is
orientation-**preserving**. Here orientation distinguishes nothing: three distinct parents, one
oriented child, and not even a mirror between them.

The census is the empirical spine of the paper, and it refutes the clean law we first proposed.
It is *not* true that every collision on this family is a mirror pair. What is true is weaker and
still sharp: whenever two (or more) knots of the family collide to a common child, the parents
agree on *everything measurable about the child*, and the only datum on which they can possibly
disagree is orientation — a single ℤ/2 — which they sometimes do (the (5,1) mirror pair) and
sometimes do not (the orientation-preserving triple).

---

## 5. The inversion law

**The inversion law (corrected).** Surgery on the figure-eight family forgets the parent knot's
arithmetic entirely — trace field, Alexander polynomial, genus, chirality-as-knot — and the
residual distinction between colliding parents is *at most* a single ℤ/2 datum, the orientation of
the child. That bit survives non-uniformly: some collisions are mirror pairs (orientation the sole
surviving distinction, as at (5,1)), and some are orientation-preserving (no surviving distinction
at all, as in the twist-knot triple). Equivalently: the map (knot, slope) ↦ (oriented child) has,
on collisions, an ambiguity of zero or one bit — never more — and the bit, when present, is the
mirror.

The law is stated for what it forbids as much as for what it keeps. It forbids reading the
Eisenstein field ℚ(√−3), the parent's Alexander polynomial, the parent's genus, or the parent's
chirality-as-knot out of the child. What it may keep is one bit, and no more; and that bit is the
same ℤ/2 the whole program keeps under its other operations — orientation, the residue, the breath
(Paper 3) — here in its surgical clothing, the mirror in a Dehn filling. The honest headline is not
"the object cannot be made to forget which way it turns." It is: *surgery forgets the parent almost
completely, and whether it remembers even the handedness depends on the collision.*

---

## 6. What is classical, and what remains open

Classical: cosmetic-surgery and common-filling phenomena (Brakes; Livingston; the twist-knot
surgery literature); the class-invariance of trace fields under commensurability (Neumann–Reid);
the B289 Chern–Simons sign law's geometric origin (the deck action); the conjugate-embedding
diagnostic for mirror images (Maclachlan–Reid). Ours (scoped, pending the gate): the systematic
laundering of the figure-eight's Eisenstein field from its child (with the child's quartic trace
field having no quadratic subfield); the *non-uniform* orientation residue across the census (the
(5,1) mirror pair versus the orientation-preserving triple); the triple collision as a ℤ-homology
sphere. Open: (i) a *characterization* of which collisions are orientation-reversing and which are
orientation-preserving — the (p,1) versus multi-slope pattern seen here is not yet a theorem;
(ii) whether the laundering extends beyond twist knots; (iii) an intrinsic proof — from the
surgery formula rather than the census — that the ambiguity is at most the mirror.

---

## Appendix: reproducibility

Census filter and collision enumeration `B467_family_residue_wall/census.py`, `f3_wall.py`; the
child's vacua and Chern–Simons `B434`/`B458` engines; the B289 sign law. Revision verification
(2026-07-08): trace fields of 4₁, 5₂, 4₁(5,1), 5₂(5,1) via SnapPy/Sage `find_field` — x²−x+1,
x³−x−1, x⁴−x−1, x⁴−x−1 respectively; the conjugate geometric embeddings −0.2481 ± 1.0340 i
confirming the (5,1) mirror pair; the triple's equal volume 1.3985089 and H₁ = 0 confirming a
common oriented ℤ-homology sphere. The census solution-type filter correction (an earlier
over-strict filter excluded genuine hyperbolic fillings, including the p = 5 child) is recorded in
the corrections ledger, as is the v1→v2 correction (the ℚ(√5)→ℚ(√−3) field fix and the
orientation-law weakening).

---
*MSC 57K10, 57K32, 57M50, 57R56. Companion to Papers 1, 3, 4. Repository URL at packaging.*
