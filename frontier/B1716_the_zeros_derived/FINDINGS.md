# B1716 — THE FRAME'S EXACT ZEROS, DERIVED (P-262, P-268; no data): det M = ¼ Σ c_s R_s², INDEPENDENT OF L, BECAUSE THE RESIDUE MATRIX HAS RANK ONE FOR EVERY TWIST; B1701's 0 : 1 : 1 IS A SIGNED CROSS PRODUCT; AND THE FIRST GENERATION IS EXACTLY MASSLESS, FOR EVERY HIGGS, WHEN THE LEFT TWIST HAS EXACT ORDER 4 AND THE RIGHT TWIST ORDER ≤ 2 — A LAW THAT PREDICTED UNSEEN LINES

**Verdict: PROVED** (identities checked to machine precision; the law checked on every line of order 1–12; its analytic
proof sketched, not written). cc (main), 2026-10-22. No physical quantity. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /det(erminant)? law|matter defect|det M|rank one|cross product|0 : 1 : 1|protection/ (full text): 50 of 1490 arcs on main match (NEGATIVE 10, OPEN 4, PROVED 35, no verdict file 1)`. Four arcs bear on it:
- B1659 (det Y = 4 det S det M tr(εSMᵀ), sealed);
- B1642 (the antisymmetric pairing, Y = [v]_×);
- B1701 (the line-tied 0 : 1 : 1, computed and not derived; P-262);
- B1703 (the protection rule, leading order).

B1712's read-out found the order-12 zero, and P-268's law was committed before B1713's output was read (`5063a0f9d`).
**Literature:** the theta functions' quasi-periodicity and duplication formulae; standard.

## 1. The checks (`verification/the_zeros_derived.py`)

| | statement | result |
|---|---|---|
| **Z1** | det(Σ_s u_s E_s*) = ¼ Σ_s u_s², for the four-channel matter's dual basis | 5.5 × 10⁻¹⁷ (50 random complex u) |
| **Z2** | the 2 × 2 residue matrix of `bil` has rank one for every twist pair, so Σ_s R_s² = 0 | 5.8 × 10⁻¹⁶ (40 random twists and τ) |
| **Z3** | Y_ab = Σ_s m_s [C_a⁻¹ S C_b]_s, the bilinear pairing of M's channel weights with a quaternion (CᵀεS = εC⁻¹S on SU(2)) | 3.2 × 10⁻¹⁶ (50 random S, m) |
| **Z4** | for S a unit C_p with m_p = 0, diag(±1)·Y is antisymmetric, so the spectrum is (‖w‖, ‖w‖, 0) for any complex m | antisymmetry exact; spectrum to 7.5 × 10⁻¹⁶ |
| **Z5** | on B1701's 27 tied lines the tied channel's residue vanishes (two τ, three sectors) | ≤ 1.3 × 10⁻¹⁵ |
| **Z6** | on every line of order 1–12 (two τ), D = Σ c_s R_s² vanishes exactly where the law says | **798 of 798** line-sectors agree; D ≤ 6.5 × 10⁻¹⁴ where the law predicts a zero, ≥ 1.9 × 10⁻⁴ everywhere else |

## 2. What follows

**Z1 and Z2 give the frame's determinant.**
- det M = ¼ Σ_s c_s R_s², independent of the end's L.
- ‖M‖² grows like L, so the first generation falls like 1/L at large L.
- That is why B1703's "protection" (R₁ = 0) is a leading-order statement, and why the canonical end, where L is of order
  one, lifts it (B1711).

**Z3–Z5 derive B1701's 0 : 1 : 1.**
- With S = C_{p*}, the diagonal of Y is ±m_{p*}, and the pairs of off-diagonal entries make diag(1, −1, 1)·Y antisymmetric.
- On a tied line R_{p*} = 0, so m_{p*} = 0 and Y is a signed cross-product matrix [w]_×.
- [w]_×ᴴ[w]_× = ‖w‖²I − w wᴴ, so the spectrum is (‖w‖, ‖w‖, 0) for every τ, L and sector.
- This is B1642's [v]_× mechanism again, now in the twisted frame. P-262's first half is done. The residue law behind
  R_{p*} = 0 (by duplication, the rank-one residue factors into thetas at the Higgs's twist 3w and at δw) is sketched, not
  written.

**Z6 is P-268's law.**
- A field's two theta components carry the characteristics a and a + ½. When the left twist has exact order 4,
  a ≡ ±¼ (or the same in the second slot), and the involution u ↦ −u exchanges the two components.
- When the right twist is 2-torsion, the involution fixes each of its components up to sign.
- So P_{s·q}(u) ∝ P_s(−u) for a fixed unit q. The channels pair with equal regularised norms and residues in the ratio
  ±i, and D cancels.
- The law was read from order 12 and committed before B1713's output was read. It predicted every order-4 line massless
  in all three sectors and nothing else on orders 1–7, and that held (B1713 §3).

## 3. Scope

- B1656's four-channel coupling at B1667's canonical end.
- The law's analytic proof is a sketch: the involution's action on the denominators and phases is not written out. The
  checks are numerical, at machine precision.

## Files

- `verification/the_zeros_derived.py` → `the_zeros_derived.json`, `the_zeros_derived_run.txt`.
- `verification/b1656_funcs.py` (B1656's functions, verbatim).
- The lock: `tests/test_b1716_the_zeros_derived.py`.

> *Dated correction 2026-10-22 (the math referee's audit, S188; RETRACTIONS row 44).*
> 1. **The converse is scoped.** "D vanishes exactly where the law says, on every line of order 1–12" was checked at two τ off
>    the CP lines.
>    - Off Re τ = 0 it holds as stated.
>    - **On Re τ = 0 there is a second family the law does not name.** On the 16 order-12 lines with 12α odd (α ∈ {1/12, 1/4,
>      5/12}), the up and down quarks have D = 0 (∣D∣/scale 4 × 10⁻¹⁵ to 5 × 10⁻¹⁴), against 0.19–0.26 at Re τ = ½ and
>      0.37. B1713's stored output agrees: m₁/m₃ < 10⁻¹² at every Re τ = 0 grid point on those lines.
>    - Within the census there is no other such zero. Its explanation is open (P-292); the rectangular torus's reflection
>      symmetry is the likely source.
> 2. **The "if" direction's phases, worked out by the audit.**
>    - A right twist of order ≤ 2 has b_y ∈ ℤ, so Δ = I.
>    - A left twist of exact order 4 in the b-slot gives Π = ±diag(1, −1) = ∓i·QI. In the a-slot it gives Π = ±i·j
>      (b_x ∈ ℤ) or ±i·k (b_x ∈ ½ + ℤ).
>    - So λ = ±i always, λ² = −1, and c_s = c_s′, since the parallelogram and the ε-disc are centrally symmetric and
>      a0 ↦ −a0.
>    - The "if" direction is therefore proved, with Z6 as its numerical confirmation. The same argument would cancel D for
>      a left twist of order ≤ 2 with a right twist of exact order 4, which these charges cannot produce (q_R/q_L is even).
> 3. **"det M = ¼ Σ c_s R_s², independent of L" holds when no channel is clipped.** The instruments set u_s = 0 when
>    2πL + c_s ≤ 0. On the grids used, the smallest 2πL_max + c_s is 1.24, so nothing is clipped. The zero law survives
>    clipping, since paired channels have equal c and are clipped together.
> 4. **B1701's 0 : 1 : 1 is derived given Z5.** R_{p*} = 0 on the tied lines is numerical, and its residue law is sketched
>    (P-262).
