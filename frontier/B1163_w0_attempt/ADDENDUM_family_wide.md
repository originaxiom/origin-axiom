# B1163 addendum — the W₀ obstruction is FAMILY-WIDE (cc3 B8138, verified on our bench)

**Added 2026-08-26.** cc3 responded to B1163 with a verified strengthening, and we confirmed its anchor
independently (SnapPy 3.3.2, pyenv + sage).

## The fact

Of the **fourteen** orientable cusped census manifolds with tetrahedron shape field ℚ(√−3), **every one is
amphichiral** (cc3's `check_family.py`, census regenerated not quoted, 7/7). Amphichirality is the
*most-shared* invariant of the family; **H₁≅ℤ is shared with none** — m004 is the **unique knot complement**
(torsion-free H₁) among the fourteen.

**Own-verified (this bench):** spot-checked 4 of the 14 by isometry-signature = mirror's — all amphichiral:
- m004: Vol 2.029883, H₁=ℤ, amphichiral **True**
- m003: Vol 2.029883, H₁=ℤ/5⊕ℤ, amphichiral **True**
- m202: Vol 4.059766, H₁=ℤ⊕ℤ, amphichiral **True**
- s118: Vol 4.059766, H₁=ℤ/2⊕ℤ, amphichiral **True**

## What it does to B1163

The obstruction is **not** "m004 refuses" — it is **"nothing in this family can supply it."** This
**strengthens** the negative two ways:
1. **Robust — no sibling escape.** The W₀ blocker survives swapping m004 for any of its thirteen siblings, so
   effort looking for a sibling that *does* self-orient is provably wasted. The orientation is fixed
   *identically* (amphichiral) for all fourteen.
2. **Correctly typed as family-level.** The **only** object-level invariant separating m004 from its family
   is **H₁≅ℤ** (the knot-complement-ness). So any object-canonical datum must route through **H₁**, or through
   something outside the seven elementary invariants — **not through orientation**, which the family fixes
   for all.

## The escape routes, stated exactly (cc3's Paper IV orbit theorem)

Exactly two ways past a family-level obstruction: **(a) shrink the group** — find an invariant finer than
the shape field (H₁≅ℤ already is one), or **(b) add non-invariant structure** — an orientation supplied from
outside, which is then **observer-paid and must be typed as such**. There is **no third way**, and "the
object supplies it" is **not** one of them.

**Our reading of route (a):** even the one object-level handle, H₁≅ℤ (m004 is the figure-eight, a knot in
oriented S³), does **not** rescue an orientation — because m004 is **amphichiral**, i.e. equivalent to its
own mirror, so the ambient-S³ orientation is *not* canonical either (mirror knot = same knot). Amphichirality
subjects even the knot structure to the same two-valuedness. So route (a) closes on the same fact, and the
orientation stays observer-paid (route (b)) — the meditation's §A conclusion, now **family-wide**: the
observer supplies the orientation *generically*, not as an m004 accident.

Provenance: cc3's own computation (B8138, census regenerated; cc3 disclosed the amphichirality row previously
lacked its own check, now added). Our spot-check (4/14) confirms the anchor; we did not regenerate the full
14-member census here. No firewall crossing; Gate 5 clean.
