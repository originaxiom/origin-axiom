# ONE QUADRATIC, TWO ENDS — on the character variety the conserved pair (κ, tr(ab⁻¹)) satisfies X² − (x²−1)X + (x²−1), with trace = norm; the hyperbolic end reads it as the Eisenstein integral (X²−3X+3, ramified, disc −3), the spherical 2I end as the golden unit (X²+X−1, disc 5)
## (outside bench, 2026-08-26; sixtieth memo; closes the memo-49 ↔ B981/B248 hook exactly; the spherical end verified from scratch; a corollary found in-run)

### THE FACTS (`certificates/one_quadratic.py`, sympy exact; asserts GREEN)
- **FACT 1/2.** P(x,z) re-derived (memo 54's route); on P = 0 the pair
  (κ, tr(ab⁻¹)) has sum x²−1 (memo 54) and — computed here — **product
  G(x) = x²−1 as well**: the conserved-pair quadratic is
  **X² − (x²−1)X + (x²−1)**, trace = norm everywhere on the component.
  Discriminant D(x) = (x−1)(x+1)(x²−5).
- **FACT 3.** At x = 2 (hyperbolic/Riley): **X²−3X+3** — trace 3, norm 3
  (the ramified prime), disc −3. Memo 41's "all 3's" is explained: the 3
  is the one function x²−1 evaluated at the parabolic cusp.
- **FACT 4.** At x = 0 (the spherical 2I end, **verified from scratch**:
  the relator factor at s = i is t²−5t+5; the full relator = I exactly over
  ℚ(√5, i) at t = (5+√5)/2; z = φ; P(0,φ) = 0): **X²+X−1** — trace −1,
  **norm −1 (a unit)**, disc 5 — with κ = φ−1 and tr(ab⁻¹) = −φ its roots.
- **COROLLARY (found in-run).** Trace = norm forces
  **(κ−1)(tr(ab⁻¹)−1) = 1 identically on the component**: the shifted pair
  are mutually inverse units — and at the Riley point κ−1 = q, the field
  generator itself (q(1−q) = 1).

> **Memo 49's two arithmetic ends are one polynomial family: the same
> conserved-pair quadratic, read at the two ends of the meridian-trace
> axis — Eisenstein/ramified at the cusp, golden/unit at the 2I point —
> the exact seed beneath B981/B248's curvature-sign crossover.** (The
> curvature reading is interpretive and fenced; every identity displayed
> is computed. D vanishes at x = ±1, ±√5 — the collision loci — measured,
> not interpreted.)

### Certificates
`certificates/one_quadratic.py`; output `outputs/one_quadratic_out.txt`.

### CONVERGENCE ADDENDUM (2026-08-26 — codex R008, an independent third derivation)
Codex R008 derived, independently and in parallel: the same component
P(x,z) = z²−x²z+2x²−z−1, the same defect τ+κ−3 = x²−4, and the same
conserved-pair quadratic K²−(x²−1)K+(x²−1) — plus two elegant extras
adopted here by reference: **κ = z−1 identically mod P** (at the Riley
point: κ = tr(ab)−1 = 1+q ✓), and the identification of the pair exchange
as the **deck involution of the Riley sheet**, z ↦ x²+1−z, under which
κ ↦ τ. Three-way convergence (memos 54/60, R008); codex's Wave-4 row
"the literal component-wide 3−κ identity is refuted" states the same
peripherality this lane banked in memo 54 — no correction owed either way.
