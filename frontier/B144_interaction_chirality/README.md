# B144 — chirality of cusp-glued interactions: the firewall extends structurally (MB12) + the redirect

Campaign 1 at the bottleneck, run with the **MB12** discipline (check a target for vacuity before computing). MATH
tier; firewalled.

**MB12 vacuity chain:** "orientation-independent invariant distinguishing M from M̄" (vacuous: equal by definition);
"orientation-sensitive invariant doing more than flip sign" (vacuous: CS/WRT/η conjugate for *every* 3-manifold);
chiral = no orientation-reversing self-homeo (generic, B128 — not the wall); "preferred vs convention handedness"
(vacuous for seed-gluing — mirror-closure below).

**Structural result:** for amphichiral pieces, `M̄(m1,m2,φ) ≅⁺ M(m1,m2, h₂φh₁⁻¹)` with `h_i ∈ GL(2,ℤ)` (det −1), and
`h₂φh₁⁻¹ ∈ GL(2,ℤ)` always ⟹ **the mirror is another composite of the same pieces ⟹ family mirror-closed ⟹ no
preferred handedness.** The firewall extends to cusp-interactions **structurally** (the `R↔L` mirror is a symmetry at
every level). Premise verified (both pieces amphichiral); chiral-(i) composites are generic (exist) but mirror-closed
(no preferred side). Seed-heterogeneity gives contingency (B131), not chirality-breaking.

**Gate (an AI-assisted review):** explicit closed-composite build in Regina is not in-session-tractable (boundary-torus matching is
not a single call; closed non-hyperbolic) — the structural argument carries it; no mirror-closure failure observed.

**Redirect (POSTULATED):** preferred handedness needs **breaking the `R↔L` mirror symmetry** — a chirally-asymmetric
input (a substitution not fixed by swap+reverse), not more seeds.

```
python -m pytest tests/test_b144_interaction_chirality.py -q   # 3 passed, 1 skipped (regina/sage)
~/.local/bin/sage-python frontier/B144_interaction_chirality/probe.py
```

**Tier.** MATH. New guard MB12. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B143 untouched. See `FINDINGS.md`; ledger **V133**.
