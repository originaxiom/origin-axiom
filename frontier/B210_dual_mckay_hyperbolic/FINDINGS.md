# B210 — golden's dual McKay structure (E₈ + E₆), and the WRT face is not the shadow group

**Date:** 2026-06-25. **Status:** two genuinely-uncomputed paths, run. (1) **Golden carries BOTH exceptional
McKay-congruence groups** — `E₈` from its monodromy arithmetic, `E₆` from its (newly computed) hyperbolic
arithmetic. (2) **Resolved-negative:** the WRT modular-rep image at the golden level is *not* `2I` — so the
quantum face and the congruence shadow connect only arithmetically (B208), not as a group. Firewall-clean
representation theory / arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V209**.

## (1) The dual McKay structure — golden carries E₆ *and* E₈

The metallic bundles carry **two** arithmetics: the *real* monodromy field `ℚ(√(m²+4))` (used throughout) and
a *complex* **hyperbolic invariant trace field** (the cusped manifold's own arithmetic) — never computed
before. Computed (SnapPy via sage-python, `invariant_trace_field_gens().find_field`):

| m | bundle | hyperbolic trace field | monodromy field |
|---|---|---|---|
| **1 golden** | m004 | `x²−x+1` = **ℚ(√−3)** (ram. 3) | `ℚ(√5)` (ram. 5) |
| 2 silver | m136 | `x²+1` = **ℚ(i)** (ram. 2) | `ℚ(√2)` (ram. 2) |
| 3 bronze | s464 | degree 8 (non-arithmetic) | `ℚ(√13)` |
| 4 | t03910 | degree 4 (non-arithmetic) | — |

So golden's two arithmetics ramify at **3 and 5 — exactly the two McKay-exceptional congruence primes:**
```
  monodromy  ℚ(√5)  →  prime 5  →  SL(2,𝔽₅) = 2I = E₈   [B206]
  hyperbolic ℚ(√−3) →  prime 3  →  SL(2,𝔽₃) = 2T = E₆   [NEW]
```
`E₇=2O` is excluded — `|2O|=48` is no `|SL(2,𝔽_p)|` (B207) — so **neither** arithmetic can reach it. **Golden
is the unique metallic mean whose both arithmetics hit exceptional McKay primes** (silver hits the degenerate
prime 2 on both sides; bronze onward are non-arithmetic on the hyperbolic side). The two exceptional McKay
groups that *are* congruence quotients (`2T=E₆` at 3, `2I=E₈` at 5) are exactly golden's two ramified-prime
shadows — and golden is arithmetic on both sides (figure-eight is the arithmetic punctured-torus bundle over
`ℚ(√−3)`; its monodromy is in `SL(2,ℤ)`).

## (2) The WRT face is not the congruence shadow as a group (resolved-negative)

Is the WRT modular-rep image at the golden level (`SU(2)₃`, `q=e^{2πi/5}`) the group `2I`? **No** — the image
`⟨S,T⟩` has order **2880** (`SL(2,ℤ/20)`-related; `ord(T)` gives congruence level 20, not 5). So the quantum
face is a *bigger* object, **not** `2I`. This **answers** the open question: the WRT↔shadow connection is purely
**arithmetic** (through `det(γ+I)=m²+4`, B208), not a representation-image identity. B208 is the full story of
that link; the quantum face is a different (larger) object.

## Honest status
Trace fields computed (sage-python, solid). The "ramified prime → congruence-McKay group" is the same
construction as B206 (genuine for the arithmetic golden/silver). Ingredients standard; the dual-McKay assembly
(golden carries E₆ *and* E₈ via its two arithmetics, E₇ excluded) is the new connection — **novelty UNCHECKED**
(prior-art not run; do not claim). Firewall: McKay/representation-theoretic `E₆`/`E₈`, **not** physics. Nothing
to `CLAIMS.md`.

## Reproduction
- `python dual_mckay.py` — the dual-McKay structure + the WRT-image order (2880). (pyenv)
- `sage-python verify_trace_fields.sage.py` — the hyperbolic trace fields (Sage-gated).
- `tests/test_b210_dual_mckay_hyperbolic.py` — 3 locks. 3 passed.
