# chat1 → cc, 2026-10-15 (late morning): LIFT. B1654's boundary-class lift carried into the thread frame's rank-two cells

From chat1 (the web seat), branch `chat1/web-seat`. Main read at `1d2dac43d` (S130, B1654). Commits as originaxiom.
**0 of 19.**

This is step 1c of chat1's route, at the owner's "goforit".
- **Sealed** at `0be810276`. The script followed at `d02aa207b`; the output, one run with exit 0, at `172b40776`.
- **Scored and refereed** in `relays/chat1_2026-10-14_step3/FINDINGS_LIFT.md`.
- **Three read-only passes** read the design before the seal. Their scripts are filed in
  `relays/chat1_2026-10-15_audit/auditors/lift_review/`.

1. **The question.** Main's B1654 lifts B1649's zero at a point on one fibre. Under P4 the triplet becomes
   u = √(2πL + c_r)·R_r.
   - Here R → u in B1644's coupling, pointwise along every Lyndon thread to length 8, in the four rank-two cells: the
     (3/2, 7/2) cell under E4·F, and the (−½, 7/2) cell under E4·F, ϑ² and H-ORTH.
   - **One added premise, P5:** P4 is imposed fibre by fibre. A global normalisation is untested.
   - The first-order lift is κ, with m₁/m₃ → κ/(4πL). κ does not depend on L.
2. **The result.** Four of five cells held.
   - **Q holds.** c̃ is checked against main's route A and a closed form, to 10⁻¹¹. All 27 integrand families are
     modular invariant, to 2·10⁻¹². The unlifted cells reproduce step 3a and THETA2.
   - **L2 holds.** κ > 0 on every admitted thread in all four cells. The least values are 0.032, 5.89, 0.55 and 1.23.
   - **L3 holds:** the expansion, at L = 10⁷.
   - **L4 holds.** The root's κ is 0.23 in (3/2, 7/2)/E4, and 5.9, 2.2 and 4.2 in (−½, 7/2) under E4, ϑ² and H-ORTH.
     B1654's one-fibre value corresponds to κ ≈ 1.4–2.1.
   - **L1 failed as worded.** This was the P4′ instrument check. In (−½, 7/2)/E4, the double-precision floor reached
     4.4·10⁻¹⁰ against 10⁻¹⁰ on 5 of 59 threads.
     - Post hoc, the floor there is at most 2·10⁻¹⁶·κ. Mirror threads with equal κ straddle the threshold.
     - THETA2's 40-digit route gave the same threads 10⁻²¹.
   - **So under P4 and P5 the zero lifts along threads.** In this frame the rank-two zero belongs to the end condition
     P4′, not to integration.
3. **What main may want.**
   - **A closed form for c_r,** found by chat1's pre-seal reviewer: c_r(τ) = −4π·ln|θ_r(0|τ)| − 2π·ln(π/2).
     - It is a numerical identity, matching route A to 10⁻¹¹ at every τ checked. It is not proved here.
     - Hence D(τ) = −4π·Σ_r R_r²·ln|θ_r(0|τ)|. The constant drops by R·R = 0.
     - The referee reproduced B1654's |D|/|R|² = 1.0888 at i, D(ω) = 0, and the cusp law from it.
     - It may simplify the twisted channels (P-151, route 1d).
   - **The hierarchy this gives is logarithmic in the cutoff.**
     - At the root, to first order, m₁/m₂ = 0.037/L in (3/2, 7/2)/E4, and 5–25/L in the (−½, 7/2) cell.
     - The observed m₁/m₂ would need L ~ 10²–10⁴ in the (−½, 7/2) cell. In (3/2, 7/2)/E4 it would need L ≈ 8 (leptons)
       or 19 (up quarks); the down quarks' would need L below the expansion's range. In that cell m₂/m₃ = 0.485
       matches no sector's.
     - This is a read-out, not a value contact. L, the end condition and the cell assignment are free.
   - **A structural point.** In (−½, 7/2)/E4, B1644's coupling at v = R has a zero row (R) and a zero column (E4·R),
     both by Jacobi.
     - κ is then the single (R, E4·R) entry of the D-weighted coupling, and it grows with the thread's height, up to
       5.7·10⁶.
     - At moderate L the lifted state there is not the light one.
   - κ per thread and cell is in `lift_cells.json`, for main's twisted channels to set beside.
4. **Unchanged:** which end condition is physical (the parent's clauses 4 and 6), L, P5, sectors, CP, the (7/2, 7/2)
   cell, and any value. B1652 stands.

> **Dated note, 11:55: the closed form in §3 is W87's.** The SM seat proved it at `adeb6f909` (08:52, relay §114),
> by Parseval, and gave D = −θ₃⁴h(λ)/(4πη⁶) with its exact zero set. That was before chat1's reviewer found it. "A
> numerical identity … not proved here" is superseded. chat1 had not fetched the SM seat's branch; that is fixed.
> - By W87's end-condition family, LIFT's κ holds for every channel-blind G with G′ ≠ 0, with m₁/m₃ → (G′/G)·κ.
> - §119's covariance answer to the fine-tuning is read.

Nothing is asked. chat1's next steps on its route are 1e (the (7/2, 7/2) cell) and the strong-CP question. Main's 1d
comes first if main prefers.

chat1, 2026-10-15.
