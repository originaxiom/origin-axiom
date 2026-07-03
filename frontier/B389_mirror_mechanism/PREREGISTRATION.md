# B389 (W3.ii) — PRE-REGISTRATION: the mirror mechanism

**Committed before computation. Target: the mechanism of the banked mirror law
t(a,−b) = τ₃(t(a,b)) (P61), which is NOT induced by any single Galois element.**

## The route (Ŝ-dihedral + inversion)

The banked dihedral relation ŜW_mŜ⁻¹ = W_m⁻¹ moves both exponents: (a,b) → (−a,−b). If Par
commutes with Ŝ (expected: Ŝ² = J and Par, J commute per P57 machinery), the pair trace is
inversion-invariant with NO Galois action.

- **M1 (the inversion law):** t(−a,−b) = t(a,b) — all four H-components equal — on every
  stored cell of the banked (1,2) table. KILL: any cell where it fails.
- **M2 (the reduction, conditional on M1):** the mirror law becomes equivalent to the
  a-flip law t(−a,b) = τ₃(t(a,b)). Verify directly on all stored cells. If both hold, the
  mirror MECHANISM = (Ŝ-inversion) ∘ (a-flip Galois law): the non-Galois content of the
  mirror is exactly the group-side inversion, and the residual open piece sharpens from
  "why the b-flip is τ₃" to "why the a-flip is τ₃" — a strictly stronger position since
  the a-side carries the value sector (rows ±6).
- **M3 (operator check):** [Ŝ, Par] = 0 exactly in the engine (Ŝ = F/g; verify F·Par =
  Par·F entrywise — g scalar). KILL: they do not commute (then M1's mechanism is different
  from the dihedral route even if M1 holds numerically).

Outcomes: each of M1–M3 banks either way. Machinery: banked step0_tables.json (Fraction
arithmetic) + one entrywise engine check. Firewalled.
