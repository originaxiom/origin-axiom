# B440 — C3 foreign control: the SL(2,C) vacuum spectra of K(5,1) — no figure-eight-unique feature

**Status: banked (C3 complete). Resolves B439's held verdict. The Inversion Law's 4th instance,
at the SL(2) floor — the sharpest (tested against the commensurability neighbour 5₂). Firewalled.**

## The complete spectra (irreducible SL(2,C) characters of the closed manifolds)

Computed convention-free from π₁ (2-generator groups): A=[[m,1],[0,1/m]], B=[[k,0],[t,1/k]],
both relators = I, eliminated to the meridian trace x = tr(A).

| K(5,1) | vacua | meridian-trace factorization | fields |
|---|---|---|---|
| **4₁ [child]** | **4** | x⁴−3x³+x²+3x−1 | all in the **−283** field |
| **5₂ [neighbour]** | **6** | (x²+x−1)·(x⁴−4x³+4x²+x−1) | 2 in **ℚ(√5)** + 4 in the **same −283** field |
| 3₁ [Seifert] | 5 | x⁵−x⁴−4x³+3x²+3x−1 | disc 11⁴ |
| 6₁ | 11 | (deg-11 irreducible) | disc 1722667·2680091 |

## Cross-validation (two independent methods agree)

The child's character-variety quartic **x⁴−3x³+x²+3x−1 is identical to B439's A-polynomial
quartic** (Cooper–Long on L=M⁻⁵). The closed-manifold character variety and the A-polynomial
intersection give the same 4 vacua — mutual confirmation, no shared code path.

## The tier-3 verdict — NO figure-eight-unique feature (break criterion applied)

1. **The −283 field is commensurability-shared.** Both 4₁ and 5₂ have −283-field vacua, and the
   two quartics generate the **same** field (the child root β = −r³+3r²−r−1 for r a root of 5₂'s
   quartic; mutual containment, both degree 4). Tier-2, exactly as B438 predicted from the trace
   field and the 121 value.
2. **The vacuum count (4/6/5/11) is genericity.** It tracks the A-polynomial degree (knot
   complexity), not the parent's distinctive arithmetic — fails break criterion (c).
3. **The golden inversion (the striking part).** The ℚ(√5) vacua — which the **golden** parent
   (Δ₄₁ = golden) might be expected to transmit — are **absent in the child** and **present in
   the non-golden 5₂'s child**. The child is golden-free (shared with 3₁, 6₁; only 5₂ carries
   golden). So the golden echo, where it appears at all, is **foreign**, never the figure-eight's.

**Reading.** Surgery launders identity. Even against its closest arithmetic sibling (5₂,
commensurable, sharing the −283 field and the 121 torsion value), the child is generic: it
shares the field (forced by commensurability), differs in count (genericity), and — where its
golden parent might have left a fingerprint — carries **no** golden structure, while a random
neighbour does. This is the strongest form yet of the campaign's null hypothesis: the object's
forced child inherits its parent's commensurability class and nothing finer.

**Bar note:** forced ✓, unsought ✓ (registered three-outcome), control ✓✓ (slope AND foreign,
both-sided coverage complete). A NEGATIVE that sharpens the target — no physics promotion.

## For the campaign

C3 is complete. The next knot-dependent channel is **C5 (WRT via surgery)** — the quantum
invariant is built from the parent's colored Jones, knot-specific in a way the trace field is
not, so it is the sharpest remaining place a figure-eight fingerprint could survive. (C4, the
E₆ lift of these vacua, composes the banked Sym^{2m} machinery on the 4 child vacua.)

**Provenance.** charvar.sage → charvar.json (sage, from π₁); verify.py → verdict.json (sympy);
lock tests/test_b440_foreign_vacuum_control.py (4/4). Cross-refs: B439 (the held verdict, now
resolved), B438 (the tier-3 bar), B437 (the Inversion Law), B436/B434 (the −283 child),
docs/AUDIT_2026-07-05.md.
