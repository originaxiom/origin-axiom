# B1302 — THE SIBLING m202: WHERE THREE APPEARS — DESIGN (pre-registered; sealed by sha256)

*MASTERPLAN v3.1 Phase 1, third harvest arc. Sources read in full before this file: sm:B1282 + its addendum (@ 87a9004a), fc R72
§4–§6 + R72b/c/d (@ 659487bb), audit R12 / R15 / R18 (`reports/physical_bridge_2026_09_05/` @ 82cd8aaf), main's B1291/B1292,
the chat1 relay §2–§3 (2026-09-08). Setup done before sealing (not predictions): m202 from SnapPy (2 cusps, H₁ = ℤ², vol = 4v₃,
|Isom| = 12, chiral, CS = 1/12, hexagonal cusps), an EXACT holonomy in SL(2, ℤ[ω]) (`m202_exact.py`: tr a = tr b = ω̄, tr ab = √−3,
relator +I, both cusps trace +2), and the automorphism census on SnapPy's holonomy (`m202_census.py`: 180 word pairs of length
≤ 5, 12 distinct H₁-actions = D₆) — the seat's `sibling_germ.py` asserts on this bench at its own step (1) (62/4), while fc's `r72b`
and main's census both give 180/12: recorded as a script environment sensitivity, not a claim failure. Date 2026-09-08.*

## 1. The seats' claims (verbatim ≤ 25 words) and what is verified here

- **sm:B1282:** *"on m202 too, the inversion is the E₆ outer automorphism on the deformation space, so the flat E₆ sector of the
  two-cusped sibling is vector-like near its geometric point."* Its table: h¹(m202; Sym^n) = 2 for every even n ≤ 22 (one class
  per cusp); the inversion (A, B) acts on every slot as the scalar (−1)^{n/2+1}; the order-3 rotations act by (ω, ω̄) on n ≡ 2
  (mod 6) and trivially on n ≡ 4 (mod 6); the cusp-swapping isometries by (1, −1); h¹(m202; 27) = 6 at the geometric point.
- **sm:B1282 addendum:** *"the golden face does not appear in m202's Alexander module"* — Δ_{m202}(t₁, t₂) has seven monomials with
  coefficients ±1; no primitive specialisation (|p|, |q| ≤ 6) is divisible by t² − 3t + 1; Δ(t, t) = −(2t² + 3t + 2).
- **fc R72 §4–§5:** m202's ℤ/6 of cusp-preserving isometries: |Fix| per cusp 1, 3, 4 for r, r², r³; the order-3 element fixes
  three lines cusp-0-to-cusp-1; "3 × (16 ⊕ 10 ⊕ 1) of SO(10)" on the D₅ directions with equal signs (a singular-frame count).
- **audit R12/R15/R18:** the parity argument retained (R12); three proper arcs on m202 derived from H₁(C) = ℤ⁴, H₂(C) = 0 (R15,
  "software geometric witnesses"); "four and one, net three" in the weighted L² complex conditional on R15 (R18).
- **chat1 §2–§3:** the fixed-line law det(A − I) = 2 − tr A over SL(2, ℤ) torsion; "3 does two jobs" (order 3 ⇒ three lines;
  gcd(3, |Out E₆|) = 1 ⇒ inner lift); order 2 fails both (m004), order 3 passes both (m202).

## 2. Pre-registered computations and predictions (each can fail)

- **Q1 (the germ, exact):** with the exact holonomy, `h¹(m202; Sym^k)` for even k ≤ 22 and the induced action of the inversion
  `(a, b) ↦ (a⁻¹, b⁻¹)` and of an order-3 rotation (census class of order 3, e.g. `(a, b) ↦ (a⁻¹b, a⁻¹)`) on each 2-dimensional
  H¹, as exact 2×2 matrices → eigenvalues. PASS = h¹ = 2 for all even k ≤ 22; inversion = scalar (−1)^{k/2+1}; order-3
  eigenvalues (ω, ω̄) for k ≡ 2 (mod 6) and (1, 1) for k ≡ 4 (mod 6). FAIL = any deviation (then sm:B1282's Theorem needs its
  360-bit numerics re-examined; the mod-6 pattern is the first thing to check).
- **Q2 (the index on two cusps):** T-ONE-CUSP-INDEX extended to T = T₁ ⊔ T₂ (`t_k = Σ_i t_k^{(i)}`, r₁ = rank of the restriction
  to both cusps; the same derivation, the annihilator property summed) — implemented as `d2multi.py`, controls: the untwisted
  sector (`h¹(m202; ℂ) = 2`, half lives half dies: r₁ = t₀ = 2) and the two-cusp identities on every sector. Then the cusp-trivial
  characters of H₁ = ℤ² (the peripheral sublattice's index decides how many; expected finite) twisting Sym²: **predicted all
  zero** — the inversion acts as −I on H₁, so ψ∘ι = ψ⁻¹ and J(ψ) = −J(ψ) (T1 + T6, the m004 mechanism again). PASS = all zero
  with identities holding; FAIL = a non-zero index (then the m004 mechanism does not transfer and the sibling is the first
  live index).
- **Q3 (PW's count = the fixed-line count):** SnapPy's 12 isometries' cusp maps: |det(A − I)| per cusp and the law
  det(A − I) = 2 − tr A on each; PASS = the ℤ/6 table (1, 3, 4) per cusp for orders (6, 3, 2) and the law holding; the order-3
  element's three lines are the seat's three; the count 3 is PW's localized count under equal signs — I-26- and PW-conditional
  as fc fences it.
- **Q4 (the golden face):** Δ_{m202}(t₁, t₂) by Fox calculus (`Δ = ∂R/∂a / (t₂ − 1)`), monomial count and coefficients, the 96
  primitive specialisations, divisibility by t² − 3t + 1, and Δ(t, t). PASS = the addendum's statements verbatim.
- **Q5 (the disposition):** if Q1–Q4 pass, sm:B1282 (+ addendum) VERIFIED, fc R72 §4–§5 VERIFIED (their scripts already PASS
  here), audit R12 AGREES / R15–R18 REGISTERED as conditional, chat1 §2 CONFIRMATION, §3 hint recorded; and the **D3
  re-pricing** goes to the owner with these facts: m202 passes both of chat1's tests where m004 fails both; its flat E₆ sector is
  vector-like (Q1) and its twisted index vanishes by the same conjugation (Q2); the 3 is a singular-frame, two-cusped,
  equal-signs count (fc's two named choices); the price is the golden face (Q4). No decision is made in this arc.

## 3. Not done here
No N(27) on m202's singular frame beyond citing fc; no audit R18 recomputation (its hypotheses are recorded, its numbers
are its own); no new identification row (the choices are fc's named ones and I-26/I-28).
