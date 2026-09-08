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

---

## ADDENDUM (2026-09-08) — HALF THE DECOMPOSITION IS NOW DERIVED; THE OTHER HALF IS WRONG AS I GUESSED IT

Memo 175 §5 flagged the decomposition as *"fitted to ten coefficients… unverified beyond it."*
Attempted to derive it from **Theorem 1.2** and **formula (1)**:

> `Ẑ_a(Y_{p/r}) = ε q^d · L^{(a)}_{p/r}[(x^{1/2r} − x^{−1/2r}) F_K(x,q)]`,
> `L^{(a)}_{p/r} : x^u q^v ↦ q^{−u²r/p} q^v` when `ru − a ∈ pℤ`, else `0`.

### DERIVED — the shift `2k−1`

The factor `(x^{1/2r} − x^{−1/2r})` pairs each `F_K` block with **opposite sign** at two `x`-powers
differing by `1/r`. Under `L` those land at quadratic positions, and for `r = 1, p = −1` (the −1
surgery, eq 12) the two powers are `u = k` and `u = k−1`, giving `q^{k²}` and `q^{(k−1)²}`:

> **shift `= k² − (k−1)² = 2k−1` = 1, 3, 5, 7, 9 — exactly the shift found empirically.**

**So the ± pairing and the odd shift are consequences of the surgery formula, not a coincidence of
the fit.** That half of memo 175 §1 is now a derivation.

### NOT DERIVED — the positions, and my guess is refuted by the data

For `r = 2` (the −1/2 surgery, eq 13) the selection rule `2u − a ∈ ℤ` **kills every term at `a = 0`**,
so the label must be a half-integer. Taking `u = k−1/4` and `k−3/4` keeps the shift correct but gives
positions

| k | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| my derivation | 0 | 3 | **10** | 21 | 36 |
| the fit `3k(k−1)/2` | 0 | 3 | **9** | 18 | 30 |

**They agree at `k = 1, 2` and diverge at `k = 3` — and the `k = 3` block is IN the published data,
at `q⁹, q¹⁰, q¹¹`.** So **9 is right and my convention reading is wrong.** Reported as a failed
derivation, **not patched to fit.**

**What would settle it:** §6.8's explicit `ε`, `d` and the Spin^c labelling for **rational** surgeries
— the conventions I could not pin from the passages read.

### WHAT THIS DOES TO §2's `c_eff`

**Nothing yet, and that is worth stating.** The growth `c_eff = 4(log φ)²/π²` depends on the positions
`s_k ~ 3k²/2` — the half that is **not** derived. Under my (refuted) alternative `s_k ~ 2k²` the
constant would shift to `4(log φ)²/π² · (3/4)`, i.e. `≈ 0.0704`. **Both are of order 0.1 and neither is
6**, so §3's conclusion is unaffected — but **the specific value 0.0938 is only as good as the fitted
positions, and should be quoted with that attached.**
