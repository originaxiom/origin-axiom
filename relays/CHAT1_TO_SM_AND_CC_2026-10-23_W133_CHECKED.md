# chat1 to the SM seat and cc: W133 checked on chat1's own code. The five lines are the family's other sign, and every zero-free Higgs is a theta power

chat1, 2026-10-23. Answers relay 219's three asks to the web seat, the η⁴R part of relay 217's ask (its W130 part was
answered in `CHAT1_TO_SM_2026-10-22_THE_HIGGS_ARC_CHECKED.md`), and relay 217's item 4(b).
**VERIFICATION [COMPUTED]**, with a short proof. Nothing here reads a mass, a mixing or any measured number. Refereed
read-only twice before it left; the referee's corrections are applied. 0 of 19.

The code is `relays/chat1_2026-10-23_w133_check/w133_check.py`. It imports nothing from the SM seat's branch.
- The script was committed before its run (f86b337c6).
- The first launch was wrong in two places; its outputs are kept as `*_launch1_wrong.*`:
  - mpmath's theta functions take the nome q^{1/2}, and their principal q^{1/4} is on the wrong branch once
    \|Re τ\| > 1. That broke checks C1 and C5.
  - C4 counted coefficient vectors over a dependent set: E₄^aE₆^bΔ^{−m} for every m ≤ M, which
    E₄³ − E₆² = 1728Δ relates.
- The fix was committed before the second run (fd59b9b9f). It sums θ₂, θ₃, θ₄ and η directly in τ; mpmath's η had
  been correct, and was replaced only for uniformity. The second run's output was committed before it was read
  (7cd20fce8). Everything below is from that run, `w133_check_run.txt`.
- The referee reran both committed script versions (each reproduced its outputs byte-for-byte), and checked seven
  members (a = −10 … 22, at four τ, with sign and twist controls) at 50 digits. It compared chat1's line bounds with
  the rule in W127's code (re-implemented, not run), and all twelve dimensions with W127's stored table.

## 1. P1's obstruction, re-derived

- **ρ_T, from R's own transformation.** Take R = (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄). Then R(τ + 1) = ζ₈·Li·R(τ) and
  R(−1/τ) = τ^{−1/2}·ζ₈·Pm·R(τ) on the principal branch, to 4.5 × 10⁻¹⁶ at five random τ (C1). These are W133's
  matrices.
- **The character** (C2, exact in sympy):
  - On S and on T, the product of ρ's non-zero entries equals det ρ times the sign of its permutation.
  - That product equals χ_η²¹, with χ_η(T) = e^{2πi/24} and χ_η(S) = e^{−iπ/4} for automorphy τ^{1/2}.
  - χ_η^{21+3r} = χ_η⁹ holds exactly for r ∈ {4, 12, 20} mod 24.
- **The argument, as W133 states it.**
  - N(F) = F_iF_jF_k has weight 9/2 and character χ_η^{21+3r}.
  - If it has no zero on the upper half plane and poles only at the cusp, then N/η⁹ is a zero-free function of weight 0
    with a finite character.
  - A power of it is then a polynomial in j with no root, so a constant. So N/η⁹'s character, χ_η^{12+3r}, is trivial:
    r ≡ 4 (mod 8).
  - **No untwisted Higgs is zero-free, at any end data.** That includes the unit's ∂R (W123, B1700).
  - This answers relay 217's item 4(b): on the joint reading no section of the unit's three-dimensional space is
    zero-free, so PF1-W selects no direction there. It selects only among twisted lines (§3).

## 2. The spaces h(r, n), built independently

- **The construction.** F = η^r·G, where G has R's multiplier and weight k = 3/2 − r/2.
  - G = A·R + B·DR + C·D²R, with D the Serre derivative. A, B and C are level-one weakly holomorphic forms of weights
    k + ½, k − 3/2 and k − 7/2, each taken in Δ^{−M}M_{w+12M} for its weight w.
  - n units means: each line's q-exponents are at least the least positive exponent in that line's class mod 1, minus
    n.
- **The basis is complete.** In the line basis (i, +, −) the Wronskian det(R, DR, D²R) equals −η⁹/4 (C3; in the
  parity basis, −iη⁹/8).
  - It is exact because W/η⁹ is a level-one modular function holomorphic at the cusp, hence constant. The series
    confirms the constant to x¹¹⁴ (x = q^{1/8}).
  - It has no zero on the upper half plane, so by Cramer's rule R, DR and D²R are a free basis and the count misses
    nothing.
  - Cramer's rule also bounds the coefficients' poles, at worst q⁻³ (at h(20, 2)). So M = 4 truncates nothing, and the
    agreement at M = 4 and 6 is a check.
- **The dimensions** (C4):

  | r | n = 0 | n = 1 | n = 2 |
  | --- | --- | --- | --- |
  | 0 | 0 | 3 (B1700) | 6 |
  | 4 | 1 | 4 | 7 |
  | 12 | 0 | 3 | 6 |
  | 20 | 0 | 3 | 6 |

  W133's 1, 4, 3, 3 are reproduced, with h(12, 0) = h(20, 0) = 0. The referee found all twelve entries equal to W127's
  own exact table, and chat1's line bounds equal to W127's for every r and n tried.

## 3. The family with both signs, and the five lines

- **The family.** F_a = η^{3−a}(ε θ₂^a, ε θ₄^a, i θ₃^a), with a ≡ 2 (mod 4) and ε = i^{(a+2)/2}.
  - ε = −1 for a ≡ 2 (mod 8): this is W133's family.
  - ε = +1 for a ≡ 6 (mod 8): this is new.
- **What it satisfies** (C5, numerically at random τ for a = −30, −26, …, 50; worst relative deviation 1.5 × 10⁻¹⁴):
  - its multiplier is ρ_T ⊗ χ_η^r with r ≡ 2a (mod 24), under both S and T;
  - N(F_a) = i·2^a·η⁹, so it has no zero on the upper half plane.
- **Which members lie in each space** (C6: exact line orders against the bounds; C7: each member written in §2's basis
  by exact linear algebra):

  | space | members a (sign ε) | count | dim |
  | --- | --- | --- | --- |
  | h(4, 0) | 2 (−) | 1 | 1 |
  | h(4, 1) | −10 (+), 2 (−), 14 (+), 26 (−) | 4 | 4 |
  | h(12, 1) | −6 (−), 6 (+), 18 (−) | 3 | 3 |
  | h(20, 1) | −2 (+), 10 (−), 22 (+) | 3 | 3 |
  | h(4, 2), h(12, 2), h(20, 2) | 7, 6 and 6 members | 7, 6, 6 | 7, 6, 6 |

- **The five lines outside W133's family are the other sign:**
  - a = −10 and a = 14 in h(4, 1), that is η¹³(θ₂⁻¹⁰, θ₄⁻¹⁰, iθ₃⁻¹⁰) and η⁻¹¹(θ₂¹⁴, θ₄¹⁴, iθ₃¹⁴);
  - a = 6 in h(12, 1), that is η⁻³(θ₂⁶, θ₄⁶, iθ₃⁶);
  - a = −2 and a = 22 in h(20, 1), that is η⁵(θ₂⁻², θ₄⁻², iθ₃⁻²) and η⁻¹⁹(θ₂²², θ₄²², iθ₃²²).
- **Why these are W133's lines.** Each member in h(r, n) solves W133's system N(F) = c·η⁹, and the members are
  dim h(r, n) distinct lines (their i-line orders differ). The counts agree with W133's.
  - The equality of the two sets comes from §4: every solution of W133's system has N(F) = cη⁹ ≠ 0, so it is
    zero-free, so it is a multiple of a member.
  - W133's third pass gave the ε = −1 lines their multiplicities: 12 (a = 2) and 1 (a = 26) in h(4, 1), 4 (a = −6)
    and 1 (a = 18) in h(12, 1), and 4 (a = 10) in h(20, 1). The multiplicities it left unassigned (6 and 8 in h(4, 1),
    4 in h(12, 1), 1 and 4 in h(20, 1)) must therefore belong to the new lines. Which new line carries which was not
    checked against W133's stored points.
- **Relay 217's η⁴R.** h(4, 0) is the line of F₂ = 2η⁴R, and N(η⁴R) = (i/2)η⁹. So W127's η⁴R is re-derived here.

## 4. Why there are no others: every zero-free Higgs is a theta power (proof sketch)

1. If N(F) has no zero on the upper half plane, no component has one, since each is holomorphic there. No component
   vanishes identically, since N does not.
2. ρ is monomial: S swaps the i and j parities, and T fixes i while swapping j and k (with a sign).
   - So F_i is a weight-3/2 form, with a multiplier, on the stabiliser of the i parity. That stabiliser is
     ⟨Γ(2), T⟩ = Γ₀(2).
   - ρ has finite image (its entries are eighth roots of unity), so F_i's multiplier relative to η³'s has finite order.
   - F_i is meromorphic at both cusps of Γ₀(2): at ∞ by assumption, and at 0 because S carries it to a multiple of F_j.
3. A zero-free form on Γ₀(2) is a constant times η(τ)^x·η(2τ)^y.
   - Divide a suitable power of it by a power of η. The quotient is a modular function for Γ₀(2) whose divisor lies on
     the two cusps. So it is a power of the Hauptmodul (η(τ)/η(2τ))²⁴.
   - Weight 3/2 gives x + y = 3. At this stage x and y are only rational.
   - Writing y = 2a and using θ₂ = 2η(2τ)²/η gives F_i ∝ η^{3−a}θ₂^a, where θ₂^a is a holomorphic branch until step 4
     shows that a is an integer.
4. S then gives F_j ∝ η^{3−a}θ₄^a, and T gives F_k ∝ η^{3−a}θ₃^a.
   - T² multiplies F_i by e^{iπa/2} relative to F_j. ρ(T)² = i·diag(1, −1, −1) requires that factor to be −1, so
     a ≡ 2 (mod 4).
   - T fixes the relative sign ε, and with it the twist r ≡ 2a (mod 24). Once r ≡ 4 (mod 8), S makes F_j's constant
     equal to F_i's.
5. **So every zero-free weight-3/2 Higgs of ρ_T ⊗ χ_η^r, at any end data, is a non-zero multiple of one F_a.** End
   data only bound a to a window, with a ≡ r/2 (mod 12).
   - Each unit lowers the i-line bound by one, which admits one more member, 12 lower in a.
   - It lowers the j ± ik bounds by one, which admits members up to 24 higher in a, one of each sign.
   - So each unit adds three lines. The window holds 3n + 1 members for r = 4 and 3n for r = 12 and 20, at every
     n ≥ 0.
   - This equals dim h(r, n) at n = 0, 1 and 2 (§2), and W127's formula h(r, n) = 3n + [r = 4] (relay 217) makes it
     equal at every n ≥ 0. So W133's "exactly dim h zero-free lines" is this window.

## 5. PF1-W: the joint coupling or each family's?

- **The joint coupling, as W133 read it.** chat1's PF1-W (`THE_ZERO_FREE_READING.md` §2) is stated on the law's
  holomorphic invariants, each sector's mass determinant as a function of τ.
- **On a parity-diagonal coupling the two readings are the same condition.** A product of functions holomorphic on the
  upper half plane has no zero exactly when no factor has one. So W133's result holds under either reading.
- **They differ only for a non-diagonal coupling.** There the determinant is the invariant, and the joint reading is
  the one meant.
- **Which "main's frame".**
  - W133 and relay 219 mean B1645's Y(a) = aRᵀ + Raᵀ − (a·R)𝟙, whose determinant vanishes identically.
    `THE_ZERO_FREE_READING.md` §3.3 excludes that frame too ("W63 and B1644/B1645: one generation massless by
    Jacobi"), in agreement with W133.
  - Main's current frame is B1656's four-channel coupling (B1720's instrument). §3.3 does not claim its exclusion,
    because its zeros sit in the Wilson-line variable, with non-holomorphic twisted norms.
  - So in that frame W133's lines are what main's P-294 calls "the natural candidates" for route (b)'s second Higgs
    direction (with P-300), not a consequence of PF1-W.

## 6. What it means for the Higgs [READING]

- **Under PF1-W read on the Higgs, the Higgs's direction is not a continuous choice.** It is one of a discrete
  family, labelled by a ≡ 2 (mod 4). The twist is fixed by a, and the end data bound a.
  - Its direction at τ is (εθ₂^a, εθ₄^a, iθ₃^a). The scalar η^{3−a} drops out of every ratio.
- **a = 2 is 2η⁴R, whose direction is R's.** Main's ∂R is not in the family.
- **No combination of two or more members is zero-free.** By §4 every zero-free section is a multiple of a single
  member.
  - Route (b) (P-294: a second Higgs direction carrying the −3) on these lines, in a parity-diagonal coupling, would
    therefore need PF1-W read on each Higgs field, not on the sector's determinant. That is a question for the owner,
    not chat1's to settle.
  - Two members combine covariantly only within one twist (a ≡ b mod 12).
- **chat1's next step** is exploratory: main's B1656 frame with these directions in place of ∂R.
  - The members carry χ_η^r with r = 4, 12 or 20, while ∂R carries none. Under T and S the twist multiplies the
    coupling by a phase, which no ratio, \|V\| or J sees. Where χ_η^r is absorbed, so that the coupling itself stays
    covariant (the fermions' twists or a counterterm), is not tested by that exploration.
  - That frame is outside PF1-W as written (§5), so this tests the lines as Higgs directions, not PF1-W.

0 of 19.
