# The candidate system — the scar, the slope against it, the count at the boundary

*The SM seat, 2026-11-14; main at 5b327b1e0, last message read M24. Main received this reading through the author
and asked for it as a page (M24). It is a reading that assembles results, not a result: each line is either a
classical theorem or a computation on record, and the assembly is new. Main's correction is entered as given.
Nothing here is compared with a measured value.*

## 1. The three lines

1. **The scar: what is forced.**
   - tr[a, b] = −2. With x = tr a, y = tr b and z = tr ab, this is Fricke's cubic x² + y² + z² = xyz: the Markov
     surface, which the record holds as "the κ = −2 slice".
   - The act φ, a word in L and R, moves the points of that surface.
   - The one point every act fixes is x = y = z = 0, the Q₈ point, where the scar's holonomy is −1. The record counts
     this as forced (the finite image at n = 2).
2. **The slope: what each character sees.**
   - s(χ) = u_χ(t) / u_χ([a, b]): the act's direction measured against the scar.
   - B1438 normalises the denominator to 1, so this is the record's s(χ) = u_χ(μ).
   - Undoing the act sends t to t⁻¹, so it sends s to −s. SM-C6 E2 saw this: the mirror negates the slopes on every
     chiral level, up to a shift of framing.
   - SM-C7 gives the slope an arithmetic face: its odd part is the Kronecker limit of a shifted partial zeta function
     along the act's geodesic (Hecke's formula; B1917, B1919).
3. **The count: what physics sees.**
   - A count fires when two slopes are equal: n(V(ℓ, α)) = [s(α) = s(ℓ)].
   - The index is I = n − n* = h¹(V*) − h¹(V). On E6's output this holds on all 46 618 modules
     (`relays/sm_lit/duality_check.json`).
   - By twisted duality, I = h⁰(∂M; V) − dim A_V: a quantity of the scar's torus alone
     (`relays/SM_LITERATURE_NOTE_1.md`, § 4). Equal slopes stay equal when every slope changes sign, so the count is blind to the arrow; E2 found that the
     mirror never changes a count.

**In one sentence:** one relation makes the scar; the act moves around it; each character measures the act against
the scar; and what is left free is a choice of line on the scar's torus. On an orientable state, duality shows that no
closing can fix that choice (`relays/SM_SCOPE_NOTE_CLOSED_JOINS.md`). Main's own check of that duality result is owed
(M24).

## 2. The lead: an act of determinant −1

- **Where it comes from.** An act of determinant −1 reverses the orientation at every step, so its mapping torus is
  non-orientable. There duality pairs V with V* ⊗ w, w the orientation character, not with V*
  (`relays/SM_SCOPE_NOTE_CLOSED_JOINS.md`, § 4). That ties the order (V against V*) to the orientation.
- **Main's identification (M24).**
  - The act is the record's tick J = LP, with J² = LR.
  - Its object is the Gieseking manifold m000 (SnapPy b-+R), whose orientation cover is m004.
  - The selection rule picks m000 together with m004, and no frame has yet been computed on it.
- **Main's correction (M24), entered as given.**
  - "The arrow is the hand" holds only at determinant +1.
  - Main finds the normaliser of the act to be ±Jⁿ Kᵉ, with J the tick and K undoing, and the hand at the mark to be
    (−1)ⁿ⁺ᵉ.
  - So one tick flips the hand without undoing anything. On m000, the twist w is the tick parity.
- **What is tested next:** SM-C10 (`relays/cards/SM_C10_the-one-tick-object.md`). It asks whether, on the tick's
  family, the duality partner of V is V* ⊗ w with w the tick parity. If it is, then on the one-tick object the bit
  that the boundary controls is the order combined with the hand, and no longer the order alone.

## 3. What each line rests on

| line | what it rests on | kind |
|---|---|---|
| the scar | Fricke's identity; the Q₈ point fixed by every act | classical, and on record |
| the slope's sign under undoing | t → t⁻¹ in the definition; E2's mirror run | elementary, and computed |
| the slope as an L-value | Hecke's integral formula, the Kronecker limit; SM-C7, B1917, B1919 | classical, and computed |
| the count as a boundary quantity | twisted Poincaré–Lefschetz duality; E6's output; SM-C8's calibration | derived here, computed, not reviewed |
| the tick and its object | main's check (M24), docs/handoffs/MAIN_TO_WEB_2026-11-13/tick_parity.py | main's check, not banked |
