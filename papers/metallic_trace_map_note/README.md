# Two Results from the Metallic Trace-Map Program — external-review note

Status: paper candidate (**PC17**). No claims beyond governed repository artifacts. Banked from an
external-review consolidation, **independently re-derived before banking** (verify-don't-trust).

## Classification

```text
Type: THEOREM_NOTE / COMPUTATIONAL_REPORT (specialist-facing consolidation)
Readiness: NEEDS_VALIDATION (novelty NEEDS-SPECIALIST; the mathematics is verified)
Main risk: Results A and B are repackagings of banked repo work; only Result C (B155) is new here.
```

## What this is

`NOTE.md` is a clean, specialist-facing consolidation of three results that stand on their own as
character-variety / spectral-theory mathematics, with the program's physics aims **explicitly not invoked**
(its §5). Each result carries an unambiguous verification status ([symbolic-exact] / [F_p-exact] /
[hp-numeric] / [open]). The three results, and where they live in this repo:

- **Result A — `L=−M⁴` on a distinguished SL(4) slice of the figure-eight, and its completeness.**
  This is the honest, corrected scope of the former PC13 "component" claim: the family is a
  **codimension-one slice** (not a component), the boundary spectrum is **not rigid**, and off the slice
  `L=−M⁴` fails in every form. Reproducers: `frontier/B89_sl4_symbolic_M4L/`,
  `frontier/B149_sl4_ideal_completeness/`; degeneration thesis: `frontier/B153_degree_rank_degeneration/`.
- **Result B — `κ = 2+λ²`: the trace map is the Fibonacci-Hamiltonian trace map.** Places the object in
  quasicrystal spectral theory (Sütő; Damanik–Gorodetski–Yessen), a citation-backed dichotomy, **not** a
  fundamental-physics claim. Repo neighborhood: PC11, `frontier/B127`, `knowledge/K010`.
- **Result C — the "golden × phase" rational spectral bridge at n=4.** The new piece, banked here as
  **`frontier/B155_golden_phase_bridge/`** (V148): `M_g ∈ SL(4,ℤ)` with charpoly (figure-eight monodromy)
  × (order-6 cyclotomic), invariant form signature (1,3), discriminant −15, glue (ℤ/2)². The B206≅Ω₄
  unification is stated at the honest level (shared canonical object; the integer Ω family reaches the
  charpoly only at half-integer `m=−1/2`).

## Governance

- **Firewall preserved:** §5 ("What is NOT claimed") is load-bearing — no fundamental physics, no dynamical
  spacetime embedding, no bulk-geometry selection. The signature (1,3) of Result C is **algebraic inertia**,
  not spacetime. Nothing here promotes to `CLAIMS.md`.
- **Privacy:** authored "Dritëro M. (with AI-assisted computation)"; no model/chat labels.
- **Novelty:** the mathematics is verified in-repo; whether Results A/C are *known* in the
  Falbel / Heusener–Muñoz–Porti / Zickert circle is **NEEDS-SPECIALIST** (the standing external-review gate).
