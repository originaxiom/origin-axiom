# B1486 — THE TWO ORDERS AT THE SILVER MEMBERS: the mixed direction is unobstructed at every member of both silver squares, and every fusion reached is an irreducible flat module that counts zero — the count is the order, at the hyperbolic point as at m004's counted point

**Verdict: PROVED** — all five sealed predictions hold (B1–B5), numerically at 50 digits. Scope: frame F-HE (the SM
seat's: V = ν ⊗ four at the hyperbolic point, B1297's class index on an unsealed cusp); objects the four members of
B1485 (two sign characters on each of m135 = −LLRR and m136 = +LLRR); reach single. cc (main), 2026-10-07. Sealed
`385c6891e` (sha256 d4e4b166) before any second-order term on either state was computed. The SM seat's second ask of
2026-10-03; L241's question carried from B1466. No physical quantity. **0 of 19.**

**Credit.** The SM seat for the members and the question; B1466 (main) for the method, which was controlled on its
own point before it was pointed here.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /fused|fusion|mixed direction|second.order obstruction|two orders|cup product/: 32 of 1357 arcs on main match (NEGATIVE 4, OPEN 4, PROVED 24)`
— read at the level of the verdict lines: the one prior is B1466; nothing on main computes a second-order
obstruction on a word state at its hyperbolic point. **Literature:** none used; the load-bearing inputs are B1485's
members and classes (exact, this bench) and B1466's method, controlled first (`control_c3b.json`: class zero at
residual 1.8·10⁻⁵⁷ and rank 20 as banked, an irreducible fusion with index 0; `control_three_generators.json`: the
three-generator path's numerical index equal to the exact instrument's, count by count).

## 1. Results (`fused_m135.json`, `fused_m136.json`)

| | prediction | prior | result |
|---|---|---|---|
| **B1** | each order alone is unobstructed | 99% | **HOLDS** on all four members: first-order residuals ≤ 3·10⁻⁴⁶, second-order term 0 |
| **B2** | the mixed direction c₁ + c₂ is unobstructed | 60% | **HOLDS** on all four: the class of the second-order term is zero — residual 1.9·10⁻⁴⁶, 9.4·10⁻⁴⁶ on m135 (norms 1,605 and 13,980; rank of the linearised map 43), 2.5·10⁻⁴⁵, 3.2·10⁻⁴⁷ on m136 (norms 253,673 and 217; rank 45) |
| **B3** | the fusion reached by Gauss–Newton is an exact flat irreducible module | 70% | **HOLDS** at every step that converged: residual ≤ 5·10⁻⁴⁶, commutant dimension 1 (gap ≥ 10⁴⁸), no invariant line, no invariant hyperplane — m135 at ε = 0.1 and 0.02 (both members), m136 at ε = 0.02 and 0.005 (first member; ε = 0.1 did not converge) and at all three ε (second member) |
| **B4** | the fusion reads (I(X), I(Λ²X)) = (0, 0) | 60% | **HOLDS** at every converged fusion: acyclic on both sides, h¹ = 0 for X, X*, Λ²X and its dual |
| **B5** | the same on m136 | | **HOLDS** |

In the same code path the two orders still read W₁: (−1, −1), W₂: (+1, +1) and the split module (0, 0), with
commutant dimensions 1, 1, 2 and invariants (0, 1), (1, 0), (1, 1) — the pattern of B1466's W, W′, S. The two interior
classes c₁ ∈ H¹(V) and c₂ ∈ H¹(V*) are exactly dual through the Lorentz form (proportionality residual 0), as the
seat's "V ≅ V* through β" says. The two members of each state read alike (Galois conjugates, a check). The fusions'
traces leave S's (tr t = −2.9999 … −3.005 against −3) and approach them as ε → 0 (distances 0.73, 0.18 on m136's first
member at ε = 0.02, 0.005; 0.16, 0.031, 0.0077 on its second); on m135 Gauss–Newton walked further from the seed
(distances 1.8 and 0.36 at ε = 0.1 and 0.02) before converging — the fusion it found is one point of a continuum.

## 2. What it means, and what it does not

- **At the hyperbolic point of a − state and of its + twin, the configuration that counts is a boundary point of a
  family of irreducible flat modules that count nothing.** Taking one order gives (−1, −1); the other, (+1, +1); side
  by side, 0; fused, 0 and acyclic. This is B1466's "the count is the order, and the count is a bit" read on the
  silver squares, where the seat's frame reads its one generation: the same bit, the same cancellation.
- **It bears on the audit of the generation lane** (`docs/THE_GENERATION_LANE_AUDITED_2026-10-07.md`, next landing):
  the count in this frame is a choice of order at a reducible point — the irreducible world next to it carries no
  count — so a "net chirality" can only ever be the choice, never the geometry's.
- **Not derived:** which order; any count of fermions; a vacuum that holds either order (the seat's R76 fence
  stands).

## 3. Disclosed

- **A convention error in the sealed code, caught by the sealed run's own first-order check.** The sealed
  `fused_cell.py` built the lower-left block of the opposite order as d = z₂ᵀ from the column cocycle z₂ of V*; the
  correct row cocycle is d = −(Vᵀ z₂)ᵀ. The first-order residual of "c₂ alone" read 140 instead of 0, so the sealed
  mixed-direction numbers were not even cocycles. The line was corrected, the sealed run's output kept
  (`sealed_run/`), and both states re-run; the controls had not caught it because B1466's point used its own row
  routine and the three-generator control tested the upper block only. The predictions and their priors were not
  changed.
- **Non-convergence recorded, not hidden.** On m136's first member the Gauss–Newton seed at ε = 0.1 stalled at
  residual 3.16 (the second-order term there has norm 2.5·10⁵); a guard added after the sealed run first turned this
  into an abort, then into a recorded outcome, and ε = 0.005 was added. The sealed predictions were stated "at ε =
  0.1 and 0.02"; B3 is read on the steps that converged, and the one that did not is reported.
- The numerical twin now asserts that what it counts is a representation (relator residual < 10⁻²⁵) — added after
  the sealed run.
- Numerical throughout; the obstruction class is read on the presentation complex; no claim beyond the four members.
