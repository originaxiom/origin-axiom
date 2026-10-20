# B1671 — THE DEDEKIND PHASE, VERIFIED AND SCOPED ON MAIN: the triplet's parameter-free Yukawa sectors carry no hierarchy at any τ (m₂/m₁ ≥ ½) and no Cabibbo angle; the determinant of the weight-one coupling is 8η⁶; with real coefficients the strong-CP phase approaches π·Re τ at large Im τ

**Verdict: PROVED (a verification arc, with the claims scoped).** cc (main), 2026-10-17. POINT_REGISTER P-192. 0 of 19.
- **What this arc re-banks.** The referee lane's sealed arc, numbered B1669 on its branch (sealed 20ed2c300; output
  5aea6a66c; findings cf579644d). That number collides with main's B1669, so main re-banks the arc here under its own
  number.
- **How it was verified.** One reading pass for main checked the seal, re-ran the sealed instrument, and verified every
  identity independently. Main's scripts, logs and report are in `verification/`. An unmodified copy of the referee
  lane's instrument (sha256 c15a524f…) sits beside them.

## 0. Seen first

`VERDICT topic-sweep /sum rule|zero-diagonal|Dedekind|theta.bar|strong CP|m1 = m2 \+ m3|parameter-free/: 33 of 1442 arcs on main match (NEGATIVE 6, OPEN 3, PROVED 24)`
— chiefly B1636 (the sum rule m₁ = m₂ + m₃ for every symmetric zero-diagonal O⁺ coupling, at weights 1, 3, 5, 7) and
B1635 (the dimension table by piece). **Literature:** the strong-CP angle as the phase of the quark mass determinant is
standard. The theta-constant identities (θ₂θ₃θ₄ = 2η³) are classical.

## 1. What was verified

| task | result |
|---|---|
| (a) the seal | **PASS.** The instrument's sha256 c15a524f… is the same at the seal, the output and the findings commits, as recorded. The preregistration and the pre-seal files match their hashes. The output is byte-identical at the output and findings commits |
| (b) re-execution | **PASS for the deterministic cells.** All six cells hold (`rerun/`; 667 s against 640 s). The deterministic numbers agree to rounding. For example, the random floor of m₂/m₁ is 0.5005758359792, the value at ω is ½, and the grid maximum is 0.99978 against 0.99984 committed. The Nelder–Mead fits of N10c are platform-dependent: χ²_min of 4228, 29 542 and 38 905 here against 4248, 33 517 and 33 521 committed. All exceed the 500 bar |
| (c) independent verification | **PASS.** The sum rule: e₁² − 4e₂ = 0 identically for complex symmetric zero-diagonal Y (sympy), and 4e₂ − e₁² factors as (s₁+s₂+s₃)(−s₁+s₂+s₃)(s₁−s₂+s₃)(s₁+s₂−s₃), so one singular value is the sum of the other two; 50 000 random cases give m₁ = m₂ + m₃ to 10⁻¹⁵. The dimension table reproduces B1635's exactly. det Y₁ = 2θ₂²θ₃²θ₄² = 8η⁶ exactly. For the weight-3 couplings det/(η⁶E₆) is constant (to 10⁻⁹ over six τ). For weight 5, det/η⁶ lies in span{E₄³, Δ} (4.5 × 10⁻¹⁰). For the weight-2 T̄ ⊗ T coupling, det/E₆ is constant (2 × 10⁻¹⁵) |

## 2. What it says, scoped

- **No hierarchy in the parameter-free sectors.** In a symmetric zero-diagonal sector the singular values obey
  m₁ = m₂ + m₃ (B1636's theorem, with the symbolic proof above). With m₃ ≤ m₂ this gives m₂/m₁ ≥ ½ at every τ, with
  equality at ω. The two parameter-free sectors are the weight-one O⁺ coupling and the identity, and neither can carry
  a hierarchy. **Scope:** for a general zero-diagonal coupling the sum rule fails. 50 000 of 50 000 samples break it,
  and min m₂/m₁ = 0.128.
- **No Cabibbo angle in the parameter-free sectors.** This follows from a dimension fact, not from the sum rule. At the
  minimal weights, dim M₁(ρ̄ ⊗ ρ̄) = 1 and dim M₀(ρ̄ ⊗ ρ) = 1 (the identity), so the up and down sectors' couplings are
  proportional, given the same τ and the same representation, and V = 1.
- **The determinants are modular forms.**
  - The weight-one coupling has det Y₁ = 8η⁶.
  - The weight-3 couplings have determinant η⁶ times a constant times E₆.
  - The weight-5 couplings have determinant η⁶ times a form in span{E₄³, Δ}.
  - The weight-2 T̄ ⊗ T coupling has determinant a constant times E₆.
- **The phase law.** For a product of determinants, θ̄ − θ_QCD = arg c + 12 arg η(τ) + arg f, where c collects the
  coefficients and f the level-one forms. With real coefficients and arg f = 0, 12 arg η(τ) = π·Re τ + O(∣q∣): the
  deviation is at most 1.7 × 10⁻⁶ at Im τ = 2.5, and 2.1 × 10⁻² at Im τ = 1. **Scope:** this is a large-Im τ law, for
  ∣Re τ∣ ≤ ½ with the triplet basis fixed (τ ↦ τ + 1 shifts it by π), and at tree level. **Convention:** here θ̄ − θ_QCD = +arg det; the SM seat's W101 and the paper's draft 7 write
  θ̄ = θ − arg det(M_u M_d), so the same law reads −π·Re τ there. The magnitude agrees; the sign is the convention.
  With a Dedekind counterterm the phase is constant at weight one (W101).
- **What it does not show.**
  - The fits of N10c are local-minimiser upper bounds and platform-dependent; "three orders of magnitude" is not
    established.
  - That the triplet "begins to fit at weight 5" is not computed here.
  - The Zee-texture θ₁₃ values are zero in exact arithmetic, so only "< 10⁻⁸" is meaningful.
  - No value of the Standard Model is derived.

## 3. Files

- `verification/REPORT.md`, the reading pass's report.
- `verification/my_verify*.py` with their logs: main's independent checks. `my_verify2` is a first sampling-based
  solver, ill-conditioned and superseded by `my_verify3`, which reproduces B1635's table exactly; it is kept for the
  record.
- `verification/rerun/`: the re-execution's output and log.
- `verification/referee_lane_instrument_the_dedekind_phase.py`, with its committed output and run log for comparison.
- The lock: `tests/test_b1671_the_dedekind_phase_verified.py`.
