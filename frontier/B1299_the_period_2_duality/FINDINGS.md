# B1299 — THE PERIOD-2 DUALITY, VERIFIED, AND ITS ONE HOLE: sm:B1280's Theorem 1 holds on main's own points, B1267's "rigid" is scoped to the generic locus, and the θ-odd germ's symmetry pairing fails at the subregular point on exactly one direction — the V₁₀ of the 42 — now L204

*MASTERPLAN v3.1 Phase 1, second harvest arc. DESIGN sealed before computation (`DESIGN.sha256`, `71b6ed8f…`). Sources read in
full: sm:B1280 §1–§4 and its L207, sm:B1281 §(a) (@ 87a9004a), main's B1267/B71/B1256, B1298's exact signs. The seat's
22-minute probe re-run in the pinned worktree; every seat claim re-checked with main's own parametrisation and the B1297/B1298
engines. HARVEST_LEDGER rows 8–10. Date 2026-09-08.*

## The sentence

**The period-2 isometry is charge conjugation on the SL(3) components too.** On B71's W1 and W2 the peripheral pair obeys
`λ = μ^{±3}` exactly (`[A,B] = c μ³` on W1, `[A,B] μ³ = c` on W2 with `|c − 1| ≤ 1.6·10⁻¹³` at 50 of main's own points), so
cusp-fixed vectors exist only on the curve `K = {μ has an eigenvalue in μ₃}`, which is the branch locus of Lawton's trace
coordinates; there the second sheet `(Aᵀ, Bᵀ) = τ*ρ*` coincides with ρ, hence `V ≅ τ*V*` and `h¹(V) = h¹(V*)` on every cusped
cyclic cover — the SM-derivation seat's Theorem 1, VERIFIED. Off K the components are rigid (a₁ = 0), t₀ = 0 and the index is
0; on K, h¹ = 1 — so main's B1267 headline "rigid, no modes" is true generically and false on K (sm:B1281's refinement,
applied at source). **The one hole:** at the SUBREGULAR sl₂ point (B1256's I-25 candidate) the outer involution θ′ fixes
sp(8) = V₂V₆V₁₀V₁₄ and negates the 42 = V₄V₈V₁₀V₁₆, while the inversion acts by B1298's exact `(−1)^{k/2+1}`: they agree on
seven of the eight tangent directions and disagree on EXACTLY ONE, the V₁₀ inside the 42 — the seat's L207, verified exactly,
and registered on main as **L204**, the whole remaining flat-sector chirality question on m004 itself.

## 0. Pre-registration and outcome (DESIGN §3)

| prediction | outcome |
|---|---|
| Q1 c = 1 to ≤ 1e−9 on main's W1/W2; ninth-trace identity; a₁ = t₀ = I = 0 off K | **PASS** on the registered criterion: `|c − 1| ≤ 1.6·10⁻¹³`, `|tr[Aᵀ,Bᵀ] − tr[B,A]| ≤ 2.1·10⁻¹⁴`, 50 points (25 per component, B1267's full grid), a₁ = 0, t₀ = 0, I = 0 at all. **Two honest notes:** (i) the FIRST run tested zero points (mistyped fibred relators filtered everything) and printed PASS on an empty set — an E67-shaped vacuity caught by adding `assert len(rows) ≥ 20` before any number was read; (ii) the script's own extra criterion (non-scalar part of `[A,B]μ^{∓3}` vs the monodromy solve's residual) is numerical consistency, not the DESIGN's: unpolished realisations gave 1.9·10⁻⁸ (kept: `b1299_w1w2_main_unpolished.out`), polished ones ≤ 3.2·10⁻⁹ wherever the realisation is at 10⁻⁹ or better and 1.5·10⁻⁶ at the one point realised to 5·10⁻⁸ — tracking the realisation residual as an identity must. |
| Q2 subregular decomposition V₂V₄V₆V₈V₁₀²V₁₄V₁₆, 27 = 13+9+5, exactly one mismatch (V₁₀ of the 42) | **PASS** (`b1299_subregular.py`, exact on B1296's E₆): labels (2,2,2,0,2,2) in Bourbaki order; mismatch set = [(10, "42")] |
| Q3 disposition | sm:B1280 Thm 1 VERIFIED; B1267 corrected at source; L204 registered |

## 1. Theorem 1 on main's own points (`b1299_w1w2_main.py`)

B71's parametrisation `W1(p,q) = (1,q,q,1,p,1,1,p)`, `W2(p,q) = (p,1,1,q,1,q,p,1)` on B1267's grid `{1.7, 2.3, 2.7, 3.3, 4.1}²`;
realisations polished to residual ≤ 5.4·10⁻¹⁰ at 49 points and 5.3·10⁻⁸ at one; monodromy `t` and the genuine meridian `μ = w⁻¹t` (w = a, B71's convention
`φ: a ↦ a²b, b ↦ ab`); the B1297 numeric engine on the fibred presentation `⟨a, b, t | t a t⁻¹ (a²b)⁻¹, t b t⁻¹ (ab)⁻¹⟩` with
peripheral words `μ = a⁻¹t`, `λ = [a, b]`. At every point: `(a₀, a₁, a₂) = (0, 0, 0)`, `(t₀, t₁) = (0, 0)`, `r₁ = r₁* = 0`,
`I = 0` for V and V* alike. The seat's `chirality_probe_w1w2.py` re-run here on its K-locus points: `N = 0 for all (ζ, n)`
(receipt `sm_b1280_chirality_probe_w1w2_rerun.txt`).

## 2. The hole, exactly (`b1299_subregular.py`)

| direction | part | θ′ | ι* (B1298) | |
|---|---|---|---|---|
| V₂ | sp(8) | + | + | |
| V₄ | 42 | − | − | |
| V₆ | sp(8) | + | + | |
| V₈ | 42 | − | − | |
| **V₁₀** | **42** | **−** | **+** | **the hole** |
| V₁₀ | sp(8) | + | + | |
| V₁₄ | sp(8) | + | + | |
| V₁₆ | 42 | − | − | |

The C₄ content of sp(8) under its principal sl₂ (exponents 1, 3, 5, 7 → V₂V₆V₁₀V₁₄, dim 36) is cited representation theory,
checked by dimension against the complement (42); the subregular decomposition itself is computed from the weighted
Dynkin labelling on the 72 roots (h-eigenvalue multiset) and the 27 (13 + 9 + 5 = B1256's row).

## 3. What changes on main
- **B1267 FINDINGS:** dated addendum — "rigid" holds off K; on K, h¹ = 1 and the index is still 0 by the period-2 duality (E53
  corrected at source).
- **L204 registered** (mirrors sm:L207): the subregular point's unpaired V₁₀ ⊂ 42; the computation priced (~a day: the
  subregular E₆ local system's H¹ with 27 coefficients along that direction); prior 15 %. If N ≠ 0 there, I-25 becomes
  load-bearing for chirality, not only for typing.
- **HARVEST_LEDGER rows 8–10;** hints H-B1299-K, H-B1299-HOLE.
- The masterplan head stands: every flat-sector direction on m004 is symmetry-paired except one, and that one is named.

## 4. Seat credits (the seat speaks first)
- **sm:B1280 Theorem 1** (2026-09-06): *"the elliptic SL(3) components W1, W2 are vector-like on every cusped cover (their
  cusp-fixed curve is the branch locus of the trace coordinates, where every representation is its own dual pulled back by
  the period-2 isometry)"* — VERIFIED: the identity c = 1 on main's own points, the ninth-trace identity, the off-K
  rigidity and index with independent code; the K-locus solve is the seat's, re-run here. Its E70 lesson (an
  anti-homomorphic Sym^n masked by symmetry) is already a standing control in main's engine (B1297 checks the homomorphism
  property) and in B1267's own `sym` (transposed on purpose).
- **sm:B1281 refinement 1** (2026-09-07): *"'W1 and W2 are rigid — h¹ = 0, no modes' is true at generic points and false
  on the curve K"* — VERIFIED and APPLIED at source.
- **sm:L207** (2026-09-06): *"exactly one unpaired direction, the V₁₀ of the 42 (θ′ = −1, ι* = +1)"* — VERIFIED exactly with
  B1298's signs; REGISTERED as L204 with the seat's number cited.

## 5. Fences
The K-locus computation (Newton in matrix space) is the seat's, not re-implemented: rule 4's receipt is the re-run. The
"linearisation" step of Theorem 1(c) (same character + irreducible ⇒ conjugate) is standard and adopted. No count of
generations is made; I-26 conditions every reading of h¹. The subregular hole is a symmetry statement (the pairing is not
forced), not a value of N(27): that is L204's computation.

## 6. Reproduction
`verification/`: `b1299_subregular.py` (seconds, exact), `b1299_w1w2_main.py` (~4 min; writes `b1299_w1w2_main.json`,
`.out`), `b1299_w1w2_main_unpolished.out` (the first-precision run, kept), `sm_b1280_chirality_probe_w1w2_rerun.txt`
(the seat's probe, ~22 min, receipt); `tests/test_b1299_the_period_2_duality.py` runs the subregular script in a scratch
cwd and pins the rest.
