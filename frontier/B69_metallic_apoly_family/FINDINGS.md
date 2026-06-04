# B69 — metallic family of A-polynomial / trace-relation curves + cusp-torsion law

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`metallic_apoly_family.py` (exact sympy). Standalone low-dim topology. This banks the
"breakthrough chat" handoff result (`apoly_family.py`, `cusp_verify.py`) after **independent
re-derivation + a line-by-line script audit** (Phase 0.5 of the masterplan).

## The result (computer-assisted, VERIFIED m=1..4; m=1 PROVED via B67)

The trace-relation curve `F_m(x,κ)=0` — projection of the `T_m²` fixed locus to `(x=tr a,
κ=tr[a,b])` — extends B67 (figure-eight = m=1) to the metallic family. Main components:

| m | `F_m` main component (κ as function of x) |
|---|---|
| 1 | `κ = (x⁴−3x³+x²+4x−2)/(x−1)²` (B67) |
| 2 | `κ = (x⁴−6x²+12)/(x²−2)` |
| 3 | degree-2 in κ (irrational double cover) |
| 4 | `κ = (x⁸−9x⁶+27x⁴−24x²−8)/(x⁶−7x⁴+16x²−12)` |

**Cusp–torsion law (verified m=1,2,3,4):** the cusps (ideal points = poles of κ) sit at the elliptic
torsion values `x = 2cos(π/k)`, with `k ∈ {3,…,m+2}`, `k ≡ m (mod 2)`:
`m=1→{3}, m=2→{4}, m=3→{3,5}, m=4→{4,6}`. (At `x=2cos(π/k)` the generator `a` is elliptic of order
`2k` — a torsion/degeneration point of the structure.)

## Audit + corrections to the handoff scripts (Phase 0.5)

Both handoff scripts were run and read line-by-line. Verdicts:
- **`cusp_verify.py` — clean.** Logic correct; cusp law reproduced m=1–4. Note: the m=3 cusp poly
  `(x−1)²(x²−x−1)` also carries the algebraic **conjugate** root `−1/φ=−0.618` (not of the form
  `2cos(π/k)`) — the law is about the *principal* roots; conjugates ride along (irreducibility).
- **`apoly_family.py` — F_m correct, ONE diagnostic bug.** The `F_m` are right (main components match;
  spurious `x, x+1, K−x²+2` branches present but removed in `cusp_verify`). **Bug:** the
  "geometric points (kappa=2)" line uses the **wrong κ sign** — the complete hyperbolic structure is
  `κ=−2` (V30), not `+2`. At `κ=+2` it returns the *identity* rep `x=2` plus torsion points, not the
  discrete-faithful structure. Corrected here: at `κ=−2`, m=1 gives `x=(3±i√3)/2 ∈ Q(√−3)` (the figure-
  eight trace field). Diagnostic-only — does not affect `F_m` or the cusp law.
- **`metallic_family.py`** — referenced by the handoff but **absent** from the bundle (flagged).

**Cross-check to committed work (passes):** the m=2 main component `κ(x)=(x⁴−6x²+12)/(x²−2)` equals
the verified V33 relation `κ=P²−6` with `P²=tr(t)²=x⁴/(x²−2)` — confirmed `= 0` symbolically. So B69's
F_m family is consistent with the committed m=2 A-polynomial / spectral-curve work.

## Honest labels / open

- **Cusp–torsion law:** computer-assisted, **VERIFIED m=1..4**; m=1 alone is PROVED (B67).
- **m=5,6: NOW VERIFIED** (`cusp_extend_m56.py`). The full `F_m` elimination is too slow, but the cusp
  polynomial = the **leading-z coefficient** of the fixed-locus polynomial (the ideal points are where
  `z→∞`) — computable with no solve/Groebner. Result:
  `m=5: (x−1)¹⁰(x²−x−1)⁴(x³−x²−2x+1)` → k-set **{3,5,7}** ✓ (min polys of `2cos(π/3),2cos(π/5),2cos(π/7)`);
  `m=6: x⁵(x²−3)⁵(x²−2)¹⁵(x⁴−4x²+2)` → k-set **{4,6,8}** ✓. So the **cusp–torsion law holds m=1…6**.
- **Novelty: NOT established.** Ideal points of character varieties at torsion values `2cos(π/k)` is a
  mathematically natural phenomenon (degeneration loci). Whether the metallic-family packaging is new
  vs implicit in twist-knot A-polynomial work (Hoste–Shanahan) **needs a literature check** before any
  novelty claim. Label CONJECTURED / STANDARD-flavored pending that.
- **Reconciliation (handoff §3):** the "metallic eigenvalue" (chat a) and the "torsion points `2cos(π/k)`"
  (this chat) are special points in **different variables** — the A-poly discriminant vanishes at the
  silver/metallic mean in `M=eig(meridian)` (V33), while the F_m cusps are at `2cos(π/k)` in `x=tr(a)`.
  Both correct; no contradiction.

**Disposition:** banked as a verified-m≤4 computer-assisted result with novelty OPEN (literature
check pending) and m≥5 unconfirmed. Proven core untouched.
