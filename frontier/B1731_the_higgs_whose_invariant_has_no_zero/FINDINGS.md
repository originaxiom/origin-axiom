# B1731 — THE HIGGS WHOSE INVARIANT HAS NO ZERO (P-306, P-303): AMONG THE ZERO-FREE HIGGS LINES, EXACTLY ONE HAS A ZERO-FREE QUADRATIC INVARIANT — F₆ = η⁻³(θ₂⁶, θ₄⁶, iθ₃⁶), WITH det S = −48η⁶; THE LEAST-DATUM HIGGS 2η⁴R IS NULL, SO IN B1656'S FRAME IT MAKES det Y ≡ 0

**Verdict: PROVED** (proved for every a; checked exactly for |a/2| ≤ 15 and numerically to 10⁻⁴⁰). cc (main),
2026-10-23. No data. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /zero-free|PF1-W|theta power|theta-power|eta.quotient|Gamma_0\(2\)|Γ₀\(2\)|h\(r, ?n\)|W133/` (B1730's
sweep, 6 of 1500); and for the determinant:
- B1659 (the joint law in B1656's frame: det Y(S, M) = 4 det S det M tr(εSMᵀ));
- B1691 (R·R ≡ 0);
- B1646 and B1649 (R as a null vector in the older frames);
- B1730 (the zero-free lines F_a).

None asks which zero-free Higgs has a zero-free invariant. **Literature:** Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴; the λ-function
maps the upper half plane onto ℂ ∖ {0, 1} (the Hauptmodul of Γ(2)); standard.

## 1. The question

Under PF1-W read on the Higgs field, the Higgs is one of B1730's F_a = η^{3−a}(εθ₂^a, εθ₄^a, iθ₃^a), a ≡ 2 mod 4.

- **The least datum.** With no end-data unit the only zero-free weight-3/2 Higgs is F₂ = 2η⁴R. That is h(4, 0); among
  the twists r ≡ 4 mod 8 no other n = 0 space is non-zero, and the untwisted h(0, 0) is empty.
- **The other reading (P-303).** PF1-W read on each sector's mass determinant. In B1656's frame
  det Y(S, M) = 4 det S det M tr(εSMᵀ) (B1659), so the Higgs enters det Y through the factor det S. Which F_a have that
  factor zero-free?

## 2. The theorem

For S = a_iQ_I + a_jQ_J + a_kQ_K (the frame's basis), det S = a·a = a_i² + a_j² + a_k² (checked: 1.8 × 10⁻¹⁵). For F_a,
with ε² = 1, u = θ₂⁴, v = θ₄⁴ and θ₃⁴ = u + v, and with λ = θ₂⁴/θ₃⁴ and n = a/2 (odd):

det S(F_a) = η^{6−2a}(θ₂^{2a} + θ₄^{2a} − θ₃^{2a}) = η^{6−2a} θ₃^{2a} p_n(λ), where p_n(λ) = λⁿ + (1 − λ)ⁿ − 1.

η and θ₃ have no zero, and λ maps the upper half plane onto ℂ ∖ {0, 1}. **So det S(F_a) is zero-free iff p_n has no
root outside {0, 1}.**

- **n = 1 (a = 2):** p₁ ≡ 0. **F₂ = 2η⁴R is null** (Jacobi's identity; R·R ≡ 0, B1691).
- **n = 3 (a = 6):** p₃ = 3λ(λ − 1), roots only 0 and 1. **det S(F₆) = −3η⁻⁶(θ₂θ₃θ₄)⁴ = −48η⁶, zero-free.**
- **n ≥ 5 odd:** p_n has degree n − 1 (the λⁿ terms cancel), and its roots at 0 and 1 are simple (p_n′(0) = −n ≠ 0,
  p_n′(1) = n ≠ 0). So n − 3 ≥ 2 roots lie in ℂ ∖ {0, 1} and **det S has zeros**. For n ≡ ±1 mod 6 one root is
  λ = e^{iπ/3}, attained at τ = e^{iπ/3}.
- **n ≤ −1:** the numerator (1 − λ)^m + λ^m − λ^m(1 − λ)^m (m = −n) has degree 2m and equals 1 at 0 and at 1. So all
  2m roots lie in ℂ ∖ {0, 1} and **det S has zeros**.

**So among the zero-free Higgs lines exactly one, F₆ = η⁻³(θ₂⁶, θ₄⁶, iθ₃⁶), has a zero-free quadratic invariant;
F₂ is null; every other member's invariant vanishes somewhere.** F₆ lives at one unit with twist r = 12
(h(12, 1), B1730). χ_η¹² is SL(2, ℤ)'s sign character (−1 on T and on S), so under the modular group the twist
multiplies the coupling only by ±1.

**Checks** (`verification/the_invariant.py`):
- the closed form for all seventeen members a ∈ {−22, …, 50} at three τ, to 1.6 × 10⁻⁴⁰;
- F₆ against −48η⁶ to 3.3 × 10⁻⁴⁰;
- exactly (sympy), for every odd n ∈ [−15, 15], the roots of p_n off {0, 1}: none only at n = 3, identically zero at
  n = 1, and 2, 4, …, 30 elsewhere;
- at τ = e^{iπ/3} (λ = e^{iπ/3} to 10⁻¹⁶), det S vanishes for a = 10, 14, −2, 22 and is 3 (normalised) for F₆.

## 3. In B1656's frame

On 16 seeded points (no data; B1726's best rows not used), with the Higgs F₂ the first generation is massless in every
sector (0 of 48 non-zero): **det Y ≡ 0**, as B1659's law and det S(F₂) = 0 require. With F₆ it is massive in 43 of 48;
the five exceptions all lie on lines of order 4 and 12, where B1716's exact zeros act through the matter's factor, not
the Higgs's.

## 4. What it means (labelled readings)

- **The two readings of PF1-W conflict at the least datum.** On the field it admits F₂ (the least-datum Higgs, the
  coupling triplet's own direction); on the determinant in B1656's frame it excludes F₂, whose invariant is null.
- **Read both ways, they select one Higgs: F₆.** The Higgs is zero-free and its factor of det Y is zero-free. This is a
  necessary condition only. det Y also carries det M and tr(εSMᵀ), which involve the matter on the line and can vanish
  (B1716's zeros); the four-channel frame is outside PF1-W as written (its zeros sit in the Wilson-line variable).
- **For H-cov (P-115).** The Higgs used in every sealed mass test so far, ∂R, is zero-free under neither reading
  (B1730: no untwisted Higgs is zero-free). If the record adopts PF1-W in both readings (the owner's call, P-303), the
  Higgs direction is fixed with no choice left, at FK10's one unit with the sign character as twist. **Whether F₆
  carries the hierarchy is a question for a sealed test with the data**, not for this arc.

## Files

- `verification/the_invariant.py` → `the_invariant.json`, `the_invariant_run.txt`.
- The lock: `tests/test_b1731_the_higgs_whose_invariant_has_no_zero.py`.

## Addendum 2026-10-23 (P-308, B1732): ∂R's invariant, and the four cases

- **∂R·∂R = η⁶/4 exactly.** Computed as an exact q-series to x¹⁵⁰ with B1691's module; B1691 had recorded the order x²
  and the leading coefficient ¼. So ∂R's quadratic invariant, its factor of det Y in B1656's frame, has no zero. ∂R and
  F₆ (−48η⁶) both have invariant a multiple of η⁶.
- **The four cases**, against the two readings of PF1-W (P-303):
  - ∂R passes the determinant reading's Higgs factor and fails the field reading (B1730).
  - F₂ = 2η⁴R fails the determinant reading (its invariant is null) and passes the field reading.
  - F₆ passes both.
  - Every other F_a fails the determinant reading and passes the field reading.
- **B1732 (sealed) tested F₆ in the two-ingredient frame.** The six still fit (1.62) but not specifically (7.1% of
  random hierarchies as good, against ∂R's 0.12%). So the reading that keeps the frame's one specific contact with the
  masses is the determinant reading alone, which keeps ∂R. §4's "read both ways" stands as mathematics; as a selection
  for this frame it fails B1732's test.
