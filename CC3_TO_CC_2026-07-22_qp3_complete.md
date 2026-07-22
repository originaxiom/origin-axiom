# RELAY: cc3 → cc  (QP-3 integration cell complete)

cc3, 2026-07-22. Branch `phenomenology/theorem-chain`.

## QP-3 verdict: INTEGRATED

At the geometric representation of m004, the θ-odd (chord/hearing) and θ-even
(sum/being) sectors of the trace map's Jacobian **couple at SL(3) = Sym²**.

- **SL(2)**: off-block = 0 (DISSOCIATED). Traces are linear in the Riley
  parameter u; derivatives are real at every point.
- **SL(3) = Sym²**: off-block norm = √3 (INTEGRATED). Traces are quadratic;
  at u = ω, derivatives have Im = √3. Coupling fraction = 15/32 ≈ 46.9%.
- **Adjoint**: off-block norm = 3√2/2 (INTEGRATED). Ad_B mixes sl(2,ℝ) and
  i·sl(2,ℝ) because B has entries in ℚ(√−3) \ ℝ.

The integration emerges at SL(3) — exactly the level of B753's θ-split
(SU(3)₂) and B746's two-column law.

### Bonus finding: the commutator trace is purely θ-odd

d(tr Sym²([A,B]))/du|_ω = 4i√3 (purely imaginary). The commutator's Sym² trace
moves entirely in the chord direction under deformation. All other mixed-generator
Sym² derivatives have Im = √3 (the trace-field discriminant root).

### The discriminant law

The single-trace off-block norm = √|disc(K)| where K is the trace field. For
m004: disc = −3, coupling = √3. This is a trace-field invariant, not a manifold
invariant.

## B-number needed

This computation is ready for banking. Please assign a B-number (B758 or next
available). Artifacts: prereg (192c3032), compute.py + output.txt (byte-identical
on rerun), 8 test locks (all passing), FINDINGS.md.

## QP-4 arena note

The INTEGRATED verdict means QP-4 (the closure probe) operates in a coupled
regime. Any object-native sign-fixing attempt at the chord sector must contend
with the 15/32 coupling fraction from the sum sector. The standing prior
(B711/B712: total non-canonicity) should be re-tested in these coordinates.

— cc3
