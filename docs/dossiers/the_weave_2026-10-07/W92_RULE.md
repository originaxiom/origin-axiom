# W92 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **The owner's rulings, given to this seat on 2026-10-15** (answers to two questions this seat put after main's S132):
  - **Terms between threads: both readings, P-163 first.** Main's P-163 (the Higgs's defect) runs first. chat1's
    two-point term between threads is sealed alongside it as an alternative and run after.
  - **The twist: build units for both readings, sealed.** The minimal reading (B1656's twisted coupling vector with
    untwisted units) and the per-field reading (each field's units carry its own charge on the line, with R neutral).
    chat1 seals both before any comparison.
- **The minimal reading's pieces exist.**
  - W72's untwisted units: chat1's `forms.pkl`, built from this seat's code at 87cf7f55. The unit-building modules are
    unchanged since then.
  - B1656's coupling vector: W91, delivered exactly. chat1's instrument computes it directly in the same convention
    (cell V8 checks this).
- **The per-field reading's units do not exist.** This arc builds them and checks them. It compares nothing with data
  and computes no mass.

## Weave or thread?

- **Weave-type objects.** Sections over the modular curve of each line's stabiliser, for every line of order N and
  every charge, with none picked. Which threads carry them is chat1's design.

## The construction (fixed here)

- **ρ_R's components are spin structures.** In the coordinate basis (i, j, k), ρ_R's three components are the even
  spin structures θ₂, θ₄ and θ₃ (reading "units with characteristic", item 1). ρ_R acts on them by permutations with
  phases.
- **The line.** A line ℓ = (l_a, l_b) of order N, in chat1's instrument's convention: w_ℓ = (l_a + l_b τ)/N, the same
  convention its coupling vector uses.
- **A field of charge q shifts each spin structure's argument by q·w_ℓ.** The per-field unit is the untwisted unit
  dressed component by component:
  U^{(q,ℓ)}_c(τ) = U_c(τ) · D_c(τ),  with  D_c = [e^{πi(α²τ + 2αβ)} θ_{s(c)}(β + ατ | τ)]² / θ_{s(c)}(0 | τ)²,
  where (α, β) = (q l_b/N, q l_a/N) and s(i, j, k) = (2, 4, 3).
- **The z-form, not the plain characteristic form.** The numerator is θ_s(q w)² with its quasi-periodic factor, which
  is chat1's `Tc` squared. The plain characteristic theta θ[a_s + α, b_s + β](0)² differs from it by e^{−4πiα b_s}.
  That phase falls on θ₄'s component only and breaks covariance (seen before this rule, below; W91's rule found the
  same for the coupling vector's null quaternion).
- **Why this construction.**
  1. It is B1653's duplication formula applied to one field. The field's doublet paired with the neutral doublet gives
     θ_s(qw)², and the neutral pair gives θ_s(0)².
  2. At q = 0 it is W72's unit exactly.
  3. It makes no new choice: no principal part, basis or normalisation is picked.
  4. Even thetanulls have no zeros on the upper half-plane, so the units stay holomorphic there.
  5. In the z-form, the squared quasi-periodic factors are the same for every spin structure. So D transforms on the
     line's stabiliser by one scalar character (cell V2).
- **What is dressed, and by which charge.**
  - Every matter unit, by its own field's charge: F at 3/2, F at −½, and E₄·F and f at 7/2.
  - h at 5/2 and h at 9/2, by the Higgs's charge.
  - The coupling vector is the neutral R. That is the twist counted once.
- **Not built.** Units solved in the twisted local system with a prescribed unit in the twisted exponent classes. That
  is an alternative construction of the per-field reading. It needs a choice of principal parts and an existence count
  (reading, item 4). It is stated here so that chat1 can count it, and is not built.

## The closure law, per field (a correction to §130, predicted here)

- A dressed unit returns along a thread γ that fixes ℓ with the phase χ_q = exp(2πi ε c q²/N).
  - c = ⟨w, wγ⟩/N, as in chat1's law (§127).
  - ε = +1 when wγ ≡ w, and −1 when wγ ≡ −w. Here the line is written (a, b) = (l_b, l_a) for chat1's pairing.
  - chat1's law as written, exp(−2πi c q²/N), is the ε = −1 case. On ε = +1 lines the phase is its conjugate.
  - Whether a thread closes does not depend on ε, so chat1's closure counts and admissibility are unchanged.
- **The Higgs mode enters conjugated in the Petersson pairing.** So a sector's Y integrand returns with
  exp(2πi ε c (q_L² + q_R² − q_H²)/N), and a sector closes iff c·(q_L² + q_R² − q_H²) ≡ 0 modulo N.
  - The Standard Model's 6Y sums are 8 (up), −4 (down) and 36 (leptons).
  - §130 wrote +q_H², repeating the leg sums 26, 14 and 54 of chat1's 15:29 addendum. That is the correction.
  - chat1's primary configuration set (c ≡ 0 modulo N) closes for every assignment under either sign, so it is
    unaffected.
- The K norms return exactly, since each pairs a unit with its own conjugate.

## Seen before the rule (disclosed)

- **The dressing series** (exact exponents, coefficients at 60 digits) against direct theta evaluation, at N = 9 for
  three (q, ℓ) and two points: agreement to 10⁻⁶⁰.
- **The transformation law, in scratch.**
  - In the plain characteristic form: the component ratios are τ-independent but differ by component (not
    covariant).
  - In the z-form, on L·Rⁿ for n up to 44: 888 (thread, line, q) cases, all covariant to 3 × 10⁻³³. The phase is
    chat1's law on every ε = −1 line and its conjugate on every ε = +1 line (N = 9: 192 and 96; N = 11: 160 and 160;
    N = 12: 184 and 96).
  - 28 cases at N = 12 had an identically zero component; all had q = 6.
  - A scan at 30 digits for n up to 59 had a few cases matching neither phase at n ≥ 40. There the scan read σ
    numerically on the thread's axis, at Im τ near n/2, where θ₃² and θ₄² both differ from 1 by about e^{−πn/2}, below
    the scan's precision. They are not counted, and V2's points are chosen to avoid this.
- **The two readings' pair products** (plain form, N = 9, three sectors, three lines): on lines with α = 0 the
  difference is the odd spin structure's term with signs (−1, −1, +1) on (i, j, k). On lines with α ≠ 0 the plain
  form fails, as above.
- **W72's untwisted units were rebuilt in scratch** with this seat's code, as chat1's `build_forms.py` builds them, to
  time the build. No integrand was evaluated on them.
- No Y or K integrand on any dressed unit, no mass and no comparison with data has been computed.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, the dressing series** | for N = 9, 11 and 12, every primitive line up to sign, every q from 1 to ⌊N/2⌋ and each component, the exact series to exponent 30 equals direct theta evaluation at τ = 0.13 + 1.1i and −0.4 + 2.3i to 10⁻⁴⁰ relative (identically zero components: both below 10⁻⁴⁰ absolute) | 99% |
| **V2, the multiplier** | on every L·Rⁿ with n ≤ 3N² that fixes a primitive line up to sign, on every such line and every q from 1 to ⌊N/2⌋: the three components' ratios D_c(γτ)/D_σ(c)(τ) agree and are τ-independent to 10⁻³⁰, and equal exp(2πi ε c q²/N); skipping only components that vanish identically (V4). The points are τ = −(n + 1) + i y₀ with y₀ = 1 and 0.8, so that γτ = 1 + i/y₀ and both have Im τ near 1 for every n; σ is read from the untwisted thetanull squares at those points | 95% |
| **V3, per-field closure on W72's units** | on the three smallest n with L·Rⁿ fixing a primitive line, at each N, on every fixed line, with the Standard Model's charges: the dressed integrands Y1, Y2x and Y3x at γτ₀ equal exp(2πi ε c (q_L² + q_R² − q_H²)/N) times their values at τ₀ (τ₀ the period's start, as chat1's instrument), and the K norms are equal, to 10⁻²⁵ relative; the phase with +q_H² misses by more than 10⁻³ wherever c·2q_H² ≢ 0 modulo N | 90% |
| **V4, the odd structure's zero** | a component's dressing vanishes identically exactly when its shifted characteristic is odd. Among N = 9, 11, 12 this happens only at N = 12 with q = 6, on one component of every primitive line: i when l_a is odd and l_b even, j when l_a is even and l_b odd, k when both are odd | 95% |
| **V6, the two readings compared** | component by component, in the z-form, the per-field pair product and the minimal reading's coupling differ by exactly the odd spin structure's term: θ_s(x + y)θ_s(x − y)θ_s(0)² = θ_s(x)²θ_s(y)² + ε_s θ₁(x)²θ₁(y)², with ε = (−1, −1, +1) on (i, j, k), x = q_L w and y = q_R w; to 10⁻⁴⁰ for the three sectors on every primitive line at N = 9, 11 and 12 | 90% |
| **V7, THETA2** | at q = 0 the Serre derivatives of the −½ units give θ² = E₄F + βf with W72's β (control). For q ≠ 0 the dressed units miss that relation by more than 10⁻³ relative, so THETA2's completion does not apply to them | 95% |
| **V8, the minimal reading's coupling** | chat1's `coupling` (units_cells.py at 39ffb3928) equals W91's V_s up to one constant, the same for the three components, on the Standard Model's sectors at N = 9, 11 and 12, at two points per line, to 10⁻³⁰ | 90% |

V5 is not used.

**The read-outs (no prior).**
- Each dressed unit's lowest exponent per component, for the Standard Model's fields on the lines (1, b) at N = 9, 11
  and 12.
- The number of distinct exponents in the product series.

## The delivery

- **`the_per_field_units.py`, a module.**
  - The exact dressing for any (N, ℓ, q): numerator terms as exact exponents with phases in turns, and the inverse
    thetanull squares as exact rationals.
  - `PerFieldSource`, a drop-in for chat1's UnitSource. It returns dressed series for `units` and `higgs`, the neutral
    R for `coupling`, and `None` for `completion_beta` (THETA2 does not apply, by V7).
  - `dressing_at(τ, q, ℓ, N)`, for evaluating the factors directly. U^{(q)}(τ) = U(τ)·D(τ) exactly, and factored
    evaluation is cheaper than the product series.
- **`the_per_field_units_delivery.json.gz`.** For N = 9, 11 and 12, every primitive line up to sign and every q from 0
  to ⌊N/2⌋, the exact dressing numerators to exponent 31, with the three inverse thetanull squares.
- The minimal reading needs no new delivery. Its pieces are chat1's own `UntwistedSource` and W91.

## After the run

- Record in the weave dossier's NOTE (section W92, the table), the state page, relay §133 to chat1 and main, CHANGELOG
  and PROGRESS_LOG.
- A test reads the JSON and recomputes one dressing coefficient and one closure phase in process.

0 of 19.
