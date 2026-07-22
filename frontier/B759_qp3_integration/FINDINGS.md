# FINDINGS — QP-3: the integration cell — INTEGRATED

cc3 audit seat, 2026-07-22. B-number pending (requested from cc via relay).
Branch `phenomenology/theorem-chain`. Prereg 192c3032 sealed before computation.
Gate 5-Q throughout; nothing to CLAIMS.

## Verdict: INTEGRATED

At the discrete faithful representation of the figure-eight knot complement,
the θ-odd (chord/hearing) and θ-even (sum/being) sectors of the trace map's
Jacobian **couple at SL(3) = Sym² but not at SL(2)**. The two voices speak to
each other where the object lives, but only at the level where B753's θ-split
operates.

## The two-level result

| Level | Off-block | Verdict | Mechanism |
|---|---|---|---|
| SL(2) | 0 | DISSOCIATED | tr(AB) = 2 − u is linear in u; derivative d/du = −1 is real at every point, including ω |
| SL(3) = Sym² | √3 | **INTEGRATED** | tr(Sym²(AB)) = (2−u)² − 1 is quadratic; at u = ω, d/du = −5 + i√3 has Im = √3 ≠ 0 |
| Adjoint | 3√2/2 | **INTEGRATED** | Ad_B mixes sl(2,ℝ) and i·sl(2,ℝ) because B has entries in ℚ(√−3) \ ℝ |

The integration **emerges at SL(3)**. This is exactly the level of B753's θ-split
(SU(3)₂ = quantum SL(3) level 2) and of the two-column law (B746). The SL(2)
trace map is blind to the coupling — the golden/hearing and Eisenstein/being
columns first interact at Sym².

## The full Sym² off-block ledger

| Word | tr(g) | d(tr Sym²(g))/du at ω | Im |
|---|---|---|---|
| A | 2 | 0 | 0 |
| B | 2 | 0 | 0 |
| AB | 2 − u | −5 + i√3 | √3 |
| A⁻¹B | u + 2 | 3 + i√3 | √3 |
| AB⁻¹ | u + 2 | 3 + i√3 | √3 |
| A⁻¹B⁻¹ | 2 − u | −5 + i√3 | √3 |
| [A,B] | u² + 2 | 4i√3 | 4√3 |

- Total off-block norm² = 4·3 + 48 = **60**
- Total Jacobian norm² = **128**
- Coupling fraction = 60/128 = **15/32 ≈ 46.9%**
- The commutator [A,B] has a **purely imaginary** Sym² derivative (4i√3) — its
  Sym² trace moves entirely in the θ-odd (chord) direction under deformation.

## The discriminant law

The single-trace off-block norm for tr(Sym²(AB)) is:

> |Im(d tr(Sym²(AB))/du)| = √|disc(K)| where K = ℚ(√−3) is the trace field

This is a trace-field invariant: for a manifold with trace field ℚ(√−d), the
leading Sym² coupling norm is √d. The coupling records the arithmetic distance
from the θ-fixed locus (the real character variety). For the figure-eight knot:
disc = −3, coupling = √3.

## The adjoint off-block

The 3×3 adjoint action Ad_B on sl(2,ℂ) in the basis {h, e, f}:

```
Im(Ad_B) = [[0,      √3/2,  0],
             [0,      0,     0],
             [−√3,    √3/2,  0]]
```

||Im(Ad_B)||_F = 3√2/2 ≈ 2.121. The off-diagonal block is nonzero because B
has entries in ℚ(√−3) \ ℝ (specifically, the Riley parameter ω = (−1+i√3)/2).
Ad_A has all-real entries and zero off-block. The coupling lives entirely in the
second generator.

## Q2 controls

**θ-fixed locus (u = −2, real):** All Sym² derivatives are real; all adjoint
entries are real; off-block = 0 everywhere. **CONFIRMED**: the block-diagonalization
on the fixed locus is exact.

**Q2b comparator (m003, the sister manifold):** m003 shares the same Riley
polynomial u² + u + 1 = 0, so the trace functions are identical. The coupling
fraction 15/32 is the SAME. Object-specificity enters through the monodromy
Jacobian (B98's object), not through the coupling fraction: m004's monodromy RL
gives char(DT²) = (t−1)(t²−5t+1) with τ = −3; m003's monodromy LR gives a
different torsion. The coupling fraction is a trace-field invariant; the full
integration (coupling × monodromy) is manifold-specific.

## What this means for the program

1. **The object's voices couple where it lives.** The geometric representation
   has nonzero off-block Jacobian norm at SL(3), with coupling fraction 15/32.
   The chord and sum sectors are not independent at the geometric point.

2. **The coupling emerges at SL(3), not SL(2).** This is coherent with B753
   (the θ-split is SU(3)₂ = Sym²) and B746 (the two-column law first manifests
   at the Sym² level of the trace tower).

3. **The coupling norm √3 is program-internal.** It equals √|disc(ℚ(√−3))|,
   the trace-field discriminant. No SM value is involved; no SM comparison is
   possible. Gate 5-Q Q5 satisfied.

4. **QP-4 arena sharpened.** The integration result means the closure probe
   (QP-4) operates in a coupled regime — the object cannot isolate one voice
   from the other at SL(3). Any sign-fixing attempt at the chord must contend
   with the sum sector's coupling (off-block 15/32 of the Jacobian energy).

## Artifacts

- `PREREGISTRATION.md` (hash 192c3032, sealed before computation)
- `compute.py` + `output.txt` (deterministic, reproducible)
- `../../tests/test_qp3_integration.py` (lock tests)
