# R34 — B252: "E6's 27 is complex, the 78 is real" recomputed from the Cartan matrix

**Target.** `frontier/B252_chirality_obstruction` (reader: COMPUTED, reproducible **no** — the check was done in Sage,
"H36 (amphicheirality = E6 outer automorphism) re-confirmed in Sage", nothing committed runs without it).

**What R34 did** (`r34.py`, pure Python, 1 s): Weyl orbits of the six fundamental weights of E6 in the ω-basis from
the Bourbaki Cartan matrix; an irreducible is self-dual iff its weight set is closed under negation.

| weight | orbit size | orbit = −orbit | −w₀·ωᵢ |
|---|---|---|---|
| ω₁ (27) | 27 | **no** | ω₆ |
| ω₂ (78, adjoint) | 72 roots (+6 zero) | **yes** | ω₂ |
| ω₃ | 216 | no | ω₅ |
| ω₄ | 720 | yes | ω₄ |
| ω₅ | 216 | no | ω₃ |
| ω₆ (27̄) | 27 | no | ω₁ |

**Verdict: MATCH.** The 27 is complex (its dual is the 27̄ = orbit of ω₆), the 78 is real; −w₀ acts as the diagram
flip 1↔6, 3↔5, which is B252's "chirality = outer automorphism" statement in weight language. This is textbook
E6 (the only simple algebras with complex representations are A_n (n ≥ 2), D_{2k+1}, E6), so the cell certifies the
bank's arithmetic, not a discovery.

**Physics content:** the 27 being complex is the standard reason E6 GUTs can host chiral fermions. Nothing in
B252 turns that into a prediction about this object (no fermion assignment, no anomaly sum, no scale). "No
observable content."
