# B438 — the missing FOREIGN control: nothing about the child is figure-eight-UNIQUE

**Status: banked (the 2026-07-05 audit's decisive correctness finding). Corrects B436/B437.
Firewalled.**

B436's "arithmetically special child" (C1) shipped with only the SLOPE control (sibling
4₁(7,1)) and **skipped its own pre-registered FOREIGN control** — a foreign hyperbolic knot at
slope 5. That is the same omission that had already sunk B437's "golden return." Run here.

## The two controls, both directions

- **FIELD (trace field of K(5,1), exact via algdep on the SnapPy generator):**
  4₁(5,1) = **5₂(5,1) = x⁴ − x − 1** (disc **−283**) — SHARED. 6₁(5,1), m003(5,1), m007(5,1)
  give DIFFERENT fields.
- **TORSION VALUE (total abelian torsion = |Res(Φ₅, Δ_K)|):**
  4₁ → **121**, 5₂ → **121** — SHARED; trefoil → 1 (different parent, different value).

So **{4₁, 5₂} share BOTH the −283 exit field AND the 121 torsion value** — a commensurability
class. The child's "special" arithmetic is not the figure-eight's fingerprint; it is shared
with 5₂. Still real vs *generic* knots (6₁/m003/m007 differ), but not figure-eight-unique.

## The Inversion Law, sharpened to three tiers (all verified)

1. **numerator-forced** (every knot at slope 5): H₁ = ℤ/5, the √5 character field, the 26
   abelian E₆ vacua.
2. **commensurability-shared** (4₁ ≈ 5₂, not generic): the −283 exit field, the 121 value.
3. **figure-eight-UNIQUE:** **none found.** The forced birth records the parent's
   commensurability class, not its individual identity.

**Break criterion RAISED.** A genuine inheritance break must distinguish 4₁ from **5₂** (its
commensurability neighbor), not merely from the trefoil or a generic knot. Therefore **C3's
interior→exit control set now includes 5₂**, and C5 (WRT via the parent's colored Jones) becomes
the sharpest tier-3 test — the quantum invariant is knot-specific in a way the trace field is not.

## Corrections carried

- **B436:** "arithmetically special child" → "special vs generic knots, class-shared with 5₂";
  the {−283 ⇔ figure-eight} identification retracted; the {4₁ special vs 6₁ generic} distinction
  survives.
- **B437:** "the Lucas-square law is FAMILY-GENERIC" → the FORMULA |Res(Φₚ,Δ_K)| is generic; the
  VALUE 121 is Δ_K-specific (trefoil → 1) and commensurability-shared (5₂ → 121).

**Bar note:** control ✓ (both slope and foreign now run); the finding is a NEGATIVE that
sharpens the target — no physics promotion.

**Provenance.** foreign_control.py → foreign_control.json; lock tests/test_b438_foreign_control.py
(3/3). Cross-refs: B436 (C1), B437 (C2, the Inversion Law), B434 (the forced slope), B425
(the torsion machinery), docs/AUDIT_2026-07-05.md.
