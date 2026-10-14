# B1637 — addendum (2026-10-14, S125): the fits near Im τ 6.6–7.1 are most likely artifacts of main's evaluator

**What was found** (the SM seat's W78 and W79; confirmed on main by `verification/cusp_precision_audit.py`).
- **W78** searched the sixteen T ⊗ T structures with a sector at weight 3 in W54's model on Im τ ∈ [5, 10] (rule
  `a73cf802b`, script `ba09a2c3f`, output `a330373d4`, each committed before its one run). (5, 7, 3) does not fit there:
  the grid route gives χ²_min = 190.7 at Im τ ≈ 5.48, and refined from main's τ (0.36 + 6.79i) it gives 825.6.
- **W79** (the seat's comparison with main's code at `60c5470ae`, read-only) shows the **two models are the same.**
  - This seat's ρ_T and main's ρ_θ are isomorphic.
  - Through the intertwiner, main's weight-3 span equals the seat's to 6·10⁻¹⁴ at Im τ = 1.7 and 3·10⁻¹¹ at Im τ = 3.
  - The angle between the spans then grows like |η|⁻¹⁸ (log-slope 4.711 against 3π/2 = 4.712), reaching 4·10⁻³ at
    Im τ = 7.
  - Main's own code at main's stored up-sector τ, with 300 starts, fits the up masses only to χ² = 191, not 4·10⁻²³.
- **Main's confirmation, by an independent route.**
  - B1635's forms are degree-(k + 9) polynomials in the theta squares over η¹⁸. Their cusp condition is imposed by a
    double-precision SVD, so the coefficients keep cusp-violating residues near machine precision.
  - Every basis form, at weights 3, 5 and 7, grows spuriously far up the τ line with slope 2.05–2.10 in log₁₀ per unit
    Im τ. That is the |η|⁻¹⁸ signature, 3π/2 · log₁₀ e = 2.047.
  - The implied relative error of the forms is 1·10⁻³ to 1·10⁻² at Im τ = 6.8, and about 10⁻¹⁰ at Im τ = 3.4.
  - **Disclosed: main's first two checks could not see it.** One evaluated the same coefficients exactly, so it
    reproduced their error. The other multiplied the coefficients by (1 + 10⁻¹⁶·noise), which rounds to 1 in double
    precision, so it perturbed nothing (E82). The slope test sees it.

**So, most likely:**
- B1637's fits near Im τ 6.6–7.1 are numerical artifacts: (5, 7, 3) at χ² 1.86, (3, 7, 7) at 6.72, the up sector alone
  at 6.66 (F3), and the nine masses at 20.6 near Im τ 7.1 (F2). Each needs a mass ratio near 10⁻⁵ from forms good only
  to about 10⁻³ there.
- **The corrections B1637 made to the SM seat's W53 and W54 fall with them.** W53's 163 (masses only) and W54's sentence
  "every structure with a sector at weight 3 fails" stand on the seat's model up to Im τ = 10 (W78).
- B1637's §3 sentence "W54 refuted on one sentence" is withdrawn, and so is "the geometry's weight is excluded only when
  it is the weight of the quark sectors".
- An earlier version of this addendum, drafted before W79 was read and never landed, read the disagreement as two
  different models. W79 and the audit show it is one model, with main's evaluator failing near the cusp.

**What stands.**
- **The exact fits at weights 5 and 7 near Im τ 2.6–3.5,** where the forms are good to about 10⁻¹⁰.
- **The headline:** every fit needs at least 21 real parameters for 13 numbers. In the reliable region the smallest
  fitting P is 25, so "21 or more" holds as a bound, and all 13 flavour numbers are free under this ansatz.
- **The (3, 3, 3) exclusion on all 13.** F2 predicted χ² ≥ 100 on the nine masses and ≥ 1000 on all 13. Its grade
  ("FAILS as worded") rested on 20.6 near Im τ 7.1 and on 397 at the widest allowance. It is **suspended** until the
  re-run.

**Owed (POINT_REGISTER P-144).**
- Re-run B1637's F2–F5 with an evaluator that does not divide by η¹⁸: the forms' q-series (W51's evaluator, which the
  SM seat offers), or exact coefficients evaluated in high precision. Re-grade F2–F5 on it.
- Then correct the record's statements that rest on the artifacts. The SM seat's W80 (main's optimizer on the seat's
  precise forms) bears on the same question.
