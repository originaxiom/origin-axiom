# B1088 — THE PARAMETER-FREE ACTION CARD (C1 of L174, the 3d completion's first cell)

**Date:** 2026-08-19 · **Verdict: PROVED (assembly + verification; every constant derived)**

## THE CARD

| constant | value | status |
|---|---|---|
| Λ | −1 | FORCED (B259 — the object is an exact 3d Einstein solution) |
| ℓ (AdS₃ radius) | 1 | from Λ = −1 |
| Vol | 2.029883212819307250… | the object's OWN volume — recomputed here from first principles (two regular ideal tetrahedra via the Lobachevsky function), 28-digit match to the banked complex-volume figure |
| CS | **0** | THEOREM (amphichirality; the computed witness is B1086's mirror = Galois identity gal(ρ(λ)) = ρ(λ)⁻¹); verified numerically at 50 digits — and EXACTLY: 2·R(e^{iπ/3}) = **π²/6 + i·Vol**, the CS part one lattice unit precisely |
| G_N | 1/(4σ) | B1012's identification |
| c | 6σ | **derived twice**: B1012's three-entry closure AND, independently here, Brown–Henneaux c = 3ℓ/(2G_N) = 6σ exact |
| **S** | **−Vol·σ** | S = −CS·k − Vol·σ with CS = 0: **the object's own symmetry deletes the k-coupling — the theory has one term** |

## THE CLAIM, MADE PRECISE

**The action has ZERO free dimensionless constants.** Its single scale σ is not new
freedom: it is the input ledger's one unit (the ℝ₊ closing, B1015/B1017 — priced there,
and B1015's no-dimensionless-number-flows theorem plus the ray's non-normalisability
(B1079's addendum) fence what it can ever leak). "Parameter-free" = no free dimensionless
constants; the one dimensionful unit is the banked, priced input.

## What this cell buys L174

Line one of the 3d theory's statement is now a locked object: *the gravitational sector
of the object's own physics is S = −Vol·σ on an exact Λ = −1 solution with boundary
central charge 6σ, all constants derived.* Next cells: C2 (the partition-function
bridge — quantum CS/state-integral, literature-typed), C3 (the matter sector: B1086's
multiplicity law + B1087's charge complementarity under this header), C4 (the observer
card: what lives on the cut), C5 (the arithmetic-CS hole, NEEDS-SPECIALIST, sharpened:
CS = 0, so the arithmetic analogue of the VOLUME term is the whole question).

**Locks:** tests/test_b1088_action_card.py (the volume from first principles, the exact
lattice-unit CS identity, the Brown–Henneaux closure — all fast).
