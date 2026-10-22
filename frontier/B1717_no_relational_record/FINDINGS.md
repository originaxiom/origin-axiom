# B1717 — NO RELATIONAL RECORD ON THE PRIVATE MODULES (P-278; no data): at the common point the moves' only invariant relations on B1675's private classes are the scalars — each private module is irreducible, the two are not isomorphic, and neither meets the coefficient module

**Verdict: PROVED** (a computation, exact up to numerical rank at 10⁻⁹, with a positive control). cc (main), 2026-10-22.
No physical quantity. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /relational record|equivariant map|private (class|module|state)|commutant|Hom_G|no thread keeps/ (full text): 63 of 1487 arcs on main match (NEGATIVE 15, OPEN 3, PROVED 45)`. Bearing on it:
- B1675, the source;
- B1678, whose joint 192-element image on the matter and the boundary is reducible, with its commutants computed there;
- B1641 and B1621, on the moves' action on T.

None computes equivariant maps on B1675's private modules.

B1675 (the SM seat's W34 verified on main): at the common point, with coefficients Sym^{2k} ρ_Q, the private states (the
kernel of restriction to the puncture, modulo coboundaries) have dimensions 0, 4 and 2 for k = 1, 2, 3, and no thread
and no move fixes a private class. Its last sentence leaves "a relational record (an invariant relation between changing
parts, a non-zero equivariant map)" open. The web seat's ingredients map ranked the question fifth among its sealable
questions (§6.5; P-278). No arc computes it. **Literature:** none (linear algebra).

## 1. What was computed (`verification/no_relational_record.py`, B1675's own module imported unchanged)

**The construction.**
- On each private module V_k = K/B (k = 2: dimension 4; k = 3: dimension 2), the induced action of the moves is computed
  from B1675's `pullback`.
- The image of a private complement is checked to stay in the restriction kernel K, then reduced modulo the coboundaries
  B.
- The commutants are solved as linear systems.

| quantity | G = ⟨L, R⟩ | G = ⟨L, R, P, −I⟩ |
|---|---|---|
| dim End_G(V₂) | 1 | 1 |
| dim End_G(V₃) | 1 | 1 |
| dim Hom_G(V₂, V₃), Hom_G(V₃, V₂) | 0, 0 | 0, 0 |
| dim Hom_G(ρ_Q, V_k), Hom_G(V_k, ρ_Q), k = 2, 3, the largest over every sign choice of the lifts | 0 | 0 |
| control: End_G(V₃ ⊕ V₃), End_G(V₂ ⊕ V₃) | 4 and 2, as M₂(ℂ) and ℂ ⊕ ℂ require | — |

## 2. What it means

- **No non-scalar relational record exists in this setting.**
  - Each private module is irreducible with scalar commutant, and the two are not isomorphic.
  - The finite-image coefficient module ρ_Q maps into neither. That is expected, since every thread acts on V_k as a
    hyperbolic matrix tensored with a finite-order map (B1675).
  - So the only relations the moves keep between private classes are the trivial ones.
- **With B1675:** neither a fixed record nor a relational one exists on the common point's private classes. A record
  needs an end (B1675) or a module beyond these.
- **Scope.**
  - The private modules of B1675's coefficients, k ≤ 3.
  - Higher symmetric powers, tensor products of different k, and other coefficient systems are not computed.

## Files

- `verification/no_relational_record.py` → `no_relational_record.json`, `no_relational_record_run.txt`.
- The lock: `tests/test_b1717_no_relational_record.py`.

> *Dated note 2026-10-22 (the math referee's audit, S188).* §2's "irreducible with scalar commutant" inferred
> irreducibility from the commutant. That step needs a semisimple action, and L acts on V₃ non-semisimply (rank(L + I) = 1).
> Irreducibility is now checked directly by Burnside's theorem in the script: the moves generate all of End(V₂)
> (dimension 16) and all of End(V₃) (dimension 4). The conclusion stands on that check.
