# B1276 — B1174's LEGS ARE B730's FACES: the same V₄, discovered twice, never joined — and `face` registered as overloaded

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (a join, not a correction; four MB12 controls) · **Re-probe of B1174 on owner instruction**

## The instruction, and what the re-probe found

Owner: *"should we reprobe properly with enriched knowledge the B1174 instead of taking it for granted.
maybe it was misinformed."* **Re-probed. B1174 is NOT misinformed — it is better than this seat
represented it, and the re-probe yields a JOIN rather than a correction.**

**What this seat got wrong.** It cited B1174 as *"the four ℤ/2's are NOT all one involution"* — which is
B1174's **headline**. Its actual one-line theorem is:

> *"**NOT ONE TORSOR — ONE SHARED INVOLUTION** (two V₄'s sharing exactly the c-leg; everything the
> observer's orientation touches is the c-leg; the value/genus/form-class bits are provably **OTHER
> LEGS**)."*

**B1174 never said the ℤ/2's are unrelated.** It said they are **legs of V₄'s** — and it names one
explicitly: **"meeting V₄ = Gal(ℚ(√−3, √5)/ℚ)"**.

## The join — and neither arc knows it

**B730** (three-way verified, theorem-grade) proves the object's arithmetic forces **exactly three**
quadratic faces — **being ℚ(√−3), hearing ℚ(√5), meeting ℚ(√−15)** — the three involutions of
**Gal(ℚ(√−3,√5)/ℚ) = V₄**, with **being · hearing = meeting**.

> **B1174's "meeting V₄" IS B730's three forced faces.**

**Cross-citation, measured by grep: B1174 → B730 = 0. B730 → B1174 = 0.** The same group, found twice,
from two directions, **never joined** — the assembly failure this programme keeps rediscovering.

## The parity law makes the join sharp

B1174's mechanism — **c acts nontrivially on a quadratic field iff the field is IMAGINARY** — verified
here on all three faces and on the non-face stage:

| face | field | imaginary? | c acts? | consequence |
|---|---|---|---|---|
| **being** | ℚ(√−3) | yes | **yes** | **CAN carry the orientation bit** |
| **hearing** | ℚ(√5) | **no (real)** | **no** | **MIRROR-EVEN — cannot carry it** |
| **meeting** | ℚ(√−15) | yes | yes | a different leg |
| *stage* | ℚ(√−7) | yes | yes | *control: off the face set* |

> **The one uncancelable bit (B467's orientation ℤ/2) lives on the BEING face, and it lives there
> BECAUSE that face is the imaginary one.** The golden/hearing ladder is **mirror-even by arithmetic**,
> not by accident.

**And that is the field-level statement of what E65 found representation-theoretically tonight:** every
Sym^n of SL(2) is self-dual, so the sl₂ frame is mirror-even and carries no net chirality. **Two
derivations of one fact, from arithmetic and from representation theory.**

## Consequence

**The programme's ℤ/2's are neither four unrelated bits nor one bit: they are INDEXED BY THE THREE
FORCED FACES.** The observer's orientation bit is the **being-leg**; the value torsor is a hearing-side
swap (**provably not c** — c is trivial on the reals); the genus bit of ℚ(√−15) fixes √−15 and flips
**both** generators, so it is the **meeting-leg**.

## Companion fix — `face` registered as overloaded (TERMINOLOGY.md)

The five-angle sweep found **`face` is the repo's most overloaded word — six live, mutually
incompatible senses**, and **none was in the overloaded-symbol registry**, against B1176's own rule
that *"every load-bearing overloaded symbol gets a row here before its next use."* Now registered:
the forced-field sense (1); Face I–IV lenses; K020's "four faces of one κ"; the eleven-plus-twelfth
anatomy taxonomy; P2_trinity's seven; and the **adelic** two faces — which collide with sense (1)
**inside TERMINOLOGY.md itself** (lines 573–575), so only the qualifier *golden/eisenstein* pins it.

## Controls (MB12, both directions)

- **Cross-citation counts are MEASURED by grep**, not asserted.
- The parity law is computed on all three faces **and on ℚ(√−7)**, a non-face — so the law is exercised
  off the face set too.
- The V₄ group law **being · hearing = meeting** is checked on the discriminants (−3 × 5 = −15).
- **B1174's headline and its one-line theorem are both quoted**, so the difference between them — the
  thing this seat missed — is **visible rather than smoothed over**.

## Verification

`verification/legs_are_faces.py` — standalone.

- **Feeds on:** B1174 (re-probed), B730, B467, B1168, B957, S068, E65/B1260, B1176 (the registry rule).
- **Registers:** no status change; joins two banked structures and fixes a terminology collision.
