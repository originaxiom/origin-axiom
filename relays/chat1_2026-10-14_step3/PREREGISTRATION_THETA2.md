# THETA2: the other parameter-free completion of the 7/2 cells (chat1, 2026-10-15, morning). Sealed before the script is committed

**Why.**
- The owner asked at 08:04 how the audit changes the verdicts and how to proceed. The completion of the 7/2 cells is
  the cheapest open question that decides part of the answer.
- Every one-unit 7/2 section is E4·F_l + c f, where F_l is the unique −½ section and f the unique holomorphic 7/2
  section. F₊ is R, so E4·R is isotropic.
- In the E4 basis, the + column of the coupling under any completion is c₊ times f's column.
- **Already computed** (`post_hoc_completions.*`, labelled):
  - H-ORTH (the sealed choice, thread-dependent) gives rank 3 with a nearly degenerate light pair.
  - H-E4 (c = 0) gives rank 2.
  - Every other admixture computed gave the degenerate pair. Those runs were void as named, but valid as arbitrary
    admixtures.
- **The other parameter-free completion is ϑ²F**, the Serre derivative applied twice and normalised at the unit. By the
  referee's one-coefficient read-out it is E4·F + β f with β = (−224, −4, −112), so c₊ = −4.
- Step 3a's particular sections are E4·F + α f, with α = (−221, −4, −112). They coincide with ϑ²F on the ± lines and
  differ by 3f on e_i.

**Instrument** (`theta2_completion.py`, committed after this seal and before its one run).
- It is `post_hoc_completions.py` unchanged in its integrals, admission and mass formula (K_L^{−½} Y (K_R^{−½})ᵀ).
- Its void identity fits are replaced by the one-coefficient read-out:
  - α and β are read off the (e_i, 1/8) coefficient, which the particular sections zero;
  - each identity is checked in value at five points of the fundamental domain;
  - the isotropy identity is checked in value.
- Completions: H-ORTH and H-E4 (both controls), H-PART (c = α) and H-THETA2 (c = β), in the cells C2 = (3/2, 7/2)
  with h at 9/2 and C3 = (−½, 7/2) with h at 5/2, on every Lyndon word of length 2–8.

**Controls (Q)**, holding if all hold:
- (a) the identities hold in value to 10⁻¹²;
- (b) α and β agree with the referee's (−221, −4, −112) and (−224, −4, −112) to 1%;
- (c) H-ORTH reproduces `weights_cells.json` to 10⁻⁶ on admitted threads;
- (d) H-E4 reproduces `post_hoc_completions.json` to 10⁻⁶ on admitted threads;
- (e) the integrands are invariant to 10⁻⁹ under 20 moves.

| | prediction | prior |
|---|---|---|
| Q | the controls hold | 85% |
| T1 | under H-THETA2, C2 has rank 3 on every admitted thread (m₁/m₃ > 10⁻¹⁰) | 95% |
| **T2** | under H-THETA2, no admitted C2 thread in the band m₂/m₃ ∈ [0.002, 0.07] has m₁/m₂ ≤ 0.005 | 85% |
| T3 | under H-THETA2, C2's least m₁/m₂ in the band is ≥ 0.3 | 70% |
| T4 | under H-THETA2, C3 has rank 2 on every admitted thread (an instrument check: its R row vanishes) | 98% |
| T5 | under H-THETA2, C3's root has m₂/m₃ in [0.002, 0.07] | 55% |

**What a result means, fenced.**
- **If T2 holds,** no parameter-free or norm-based completion splits the light pair at rank 3 in the (3/2, 7/2) cell,
  and that cell's rank 2 belongs to E4·F alone.
- **If T2 fails,** the ϑ² completion splits it, and a sealed sector test follows. A hit is not an assignment.
- **Not tested:** which completion is physical; the (7/2, 7/2) cell; sectors; the lift; CP.
- No value. **0 of 19.**

**Disclosed: seen before the seal.**
- `post_hoc_completions.*`, all of it, and its referee's read-out of α and β (`../chat1_2026-10-15_audit/`).
- No H-THETA2 or corrected H-PART number has been computed by chat1.

chat1, 2026-10-15.
