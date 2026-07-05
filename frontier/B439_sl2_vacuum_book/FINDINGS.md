# B439 — C3: the child's SL(2,C) vacuum book (the figure-eight core + slope control; foreign control next)

**Status: banked (C3, slope-control-complete). The held verdict is now RESOLVED by [[B440]]:
the 5₂ foreign control ran (closed-manifold character variety), 4₁'s quartic cross-validated
independently, and the tier-3 verdict is NO figure-eight-unique feature — 4₁ and 5₂ both have 4
irreducible vacua in the identical −283 field (B440 corrected by adversarial review: the golden
factor is reducible/universal, not a "golden inversion"). Firewalled.**

## The child's SL(2,C) vacuum spectrum (exact)

Vacua = points of the banked B67 Cooper–Long figure-eight A-polynomial `A_CL(M,L)=0` on the
(5,1)-filling line `L = M⁻⁵`. In the meridian trace `t = M + 1/M`:

    Q₅(t) = t⁵ − t⁴ − 5t³ + 5t² + 5t − 2 = (t + 2)·(t⁴ − 3t³ + t² + 3t − 1)

- **(t+2):** t = −2 ⇒ M = −1, the reducible/central connection.
- **the quartic t⁴ − 3t³ + t² + 3t − 1:** the **4 irreducible vacua**. Discriminant = **−283**.

## The −283 reproduce-gate — PASSES (rigorously, not just by disc)

The vacuum quartic is the child's **own invariant trace field** x⁴−x−1 (disc −283, B434/B436):
it has the explicit root **α³ − α²** (α a root of x⁴−x−1) — verified exactly by
`rem(vac(α³−α²), α⁴−α−1) = 0` — and both are S₄ with disc −283. So the geometric vacuum lives
in the child's trace field: the SL(2) floor is internally consistent with C1.

## The slope control (leg iv) — PASSES

Same construction at the **unforced** slope 7 (`L = M⁻⁷`):

    Q₇(t) = (t + 2)·(t⁶ − 2t⁵ − 3t⁴ + 5t³ + 4t² − 3t − 1)

⇒ **6 irreducible vacua**, degree-6 field of discriminant **50173 = 131·383**. Both the count
(4 vs 6) and the field (−283 vs 131·383) differ from the child — the slope control passes.

## Coverage and the held verdict

This is the **slope-control-complete** result, from the standard normalized Cooper–Long form
(no convention ambiguity). The **foreign control is mandatory** here: B438 showed 5₂ is the
child's commensurability neighbour (it shares the −283 field *and* the 121 torsion value), so
the sharp question at the SL(2) floor is whether the vacuum **structure** (count 4, the specific
quartic) is figure-eight-specific or commensurability-shared. Per the C3 prereg (asymmetric
coverage = COVERAGE-VOID), the Inversion-Law verdict is **HELD** pending 5₂(5,1)'s spectrum.
Three prereg'd outcomes stand:

1. 5₂ gives the **same** quartic ⇒ SL(2) vacuum structure is commensurability-shared
   (Inversion Law's 4th instance, at a new floor);
2. 5₂ gives a **different** count/field ⇒ a figure-eight-vs-5₂ distinguisher (**tier-3 break
   candidate** — escalate);
3. both share only the geometric −283 vacuum but differ elsewhere ⇒ partial.

**Next step (registered):** compute 5₂(5,1)'s vacuum spectrum. The A-polynomial route via
gluing-equation elimination reproduces 4₁ (Cooper–Long) and 6₁ but degenerated on snappy's
default 5₂/3₁ triangulations; the foreign control will use the closed-manifold character variety
of π₁(5₂(5,1)) directly (convention-free), with the trefoil and 6₁ as additional controls.

**Bar note:** forced ✓ (the vacua are the exact intersection, no choices), unsought ✓ (registered
two/three-outcome), control — slope ✓, foreign PENDING. Named positive mathematics; no physics.

**Provenance.** vacuum_book.py → vacuum_book.json; lock tests/test_b439_sl2_vacuum_book.py (4/4).
Cross-refs: B67 (the A-polynomial), B434 (the forced slope), B436 (the −283 trace field), B438
(the tier-3 bar), the C3 prereg (B435/PREREGISTRATION.md), docs/AUDIT_2026-07-05.md.
