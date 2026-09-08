# MEMO 175 — THE HYPERBOLIC CASE MEASURED: `c_eff` IS SET BY THE GOLDEN RATIO, AND IT IS NOT 6

**Banked 2026-09-08 · outside bench (lane 1B).** Certificate `certificates/hyperbolic_ceff.py`.
Source: Gukov–Manolescu **arXiv:1904.06057v2** eq (11), (13), owner-supplied, read on-bench.
Gate 5 untouched.

Equation (13) is `Ẑ₀(S³_{−1/2}(4₁))` — the authors call these *"the first computations of `Ẑ_a(q)`
for hyperbolic manifolds in the literature."* **Its coefficients have mixed signs**, so the Cardy
estimator cannot be run on it. This decomposes it instead.

---

## 1. THE DECOMPOSITION — found here, and it reproduces every published coefficient

> **`Ẑ₀(S³_{−1/2}(4₁)) = Σ_k [ Ξ_k at q^{s_k} ] − [ Ξ_k at q^{s_k + (2k−1)} ]`,  `s_k = 3k(k−1)/2`**

where `Ξ_k` is the `k`-th coefficient of `Ξ` in eq (11) — a symmetric Laurent polynomial in `q`.

| | |
|---|---|
| `Ξ_k` | `[1]`, `[2]`, `[1,3,1]`, `[2,2,5,2,2]` |
| `Ξ_k` sums | **1, 2, 5, 13** = `F(2k−1)`, odd-indexed Fibonacci |
| `s_k` | 0, 3, 9, 18, 30, 45, 63 |
| shift | 1, 3, 5, 7, 9, 11, 13 |

> **All ten published coefficients of eq (13) are reproduced exactly.**

The mixed signs are not noise: **each `F_K` block appears once positive and once negated, displaced
by an odd shift.** The hyperbolic `Ẑ` is `F_K`'s own coefficients, laid down in ± pairs at quadratic
positions.

## 2. THE GROWTH, IN CLOSED FORM

Block `k` carries mass `F(2k−1) ~ φ^{2k}/√5` at position `s_k ~ 3k²/2`. So `k ~ √(2n/3)` and
`log|a_n| ~ 2 log φ · √(2n/3)`. Matching the Cardy form `log a_n ~ 2π√(c_eff·n/6)`:

> # **`c_eff = 4 (log φ)² / π² = 0.093849687`**

**The effective central charge of the object's hyperbolic boundary series is set by the golden
ratio.** `log φ` is transcendental (`φ` is algebraic, `≠ 0,1`), so there is no reason to expect
`c_eff` rational. *(`3/32 = 0.09375` sits 1.0e-4 away; **not** claimed as an identity.)*

## 3. EVERY MEASUREMENT ON THE OBJECT'S SIDE, AND THE TARGET

| | `c_eff` |
|---|---|
| **target** `c((E₆)₁) = 78/13` | **6** |
| **HYPERBOLIC** `S³_{−1/2}(4₁)`, eq (13) — *this cell* | **0.0938** |
| Brieskorn `−Σ(2,3,7)`, eq (12), mock theta | 0.1424 (≈ 1/7) |
| Brieskorn `Σ(2,3,7)`, Prop 4.8, false theta | 0 |
| GC-6's substitute (`η⁻¹` free boson) — **never measured on the object** | 1 |

**The hyperbolic case — the only one that bears on the bridge — is 64× below the target.**

## 4. THE STRUCTURAL POINT, WHICH MATTERS MORE THAN THE NUMBER

**A rational CFT has rational `c_eff`.** The measured hyperbolic value is golden-ratio-determined
and shows no sign of rationality. `(E₆)₁` is rational with `c = 6`.

> **So the object's hyperbolic boundary series is not the character of a rational CFT, and `(E₆)₁`
> cannot be what it attaches to.** That is `B1064`'s O3 reached from the other side — by measuring the
> object rather than by arguing about its action — and the paper's *"non-strongly-finite for
> hyperbolic Y"* now carries a number.

**σ = 1 is not supported by anything measured here.** Four readings of the object's own boundary
data — 0.0938, 0.1424, 0, and the discarded prefactor 12 — and **none is 6**.

## 5. FENCES

- **The decomposition is fitted to ten coefficients (three blocks) and matches all ten.** Exact on
  what exists, **unverified beyond it** — the `Ξ₄` placement at `q^18…q^22` is a **prediction with no
  data behind it.**
- **The growth is an asymptotic estimate from that pattern**, not a proved asymptotic.
- These are **surgeries** on `4₁`, not the cusped complement itself.
- `c_eff` is not `c`. Memo 174 §3's tension between growth and prefactor readings is **unresolved**
  and applies here too.
- **Nothing here proves σ ≠ 1.** It reports that every measurement made on the object's own boundary
  data lands far from the value the bridge needs.
