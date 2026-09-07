# MEMO 174 — THE OBJECT'S BOUNDARY c_eff, MEASURED FOR THE FIRST TIME

**Banked 2026-09-07 · outside bench (lane 1B).** Certificate `certificates/zhat_ceff.py`.
Source: Gukov–Manolescu **arXiv:1904.06057v2**, owner-supplied, read on-bench. Gate 5 untouched.

**GC-6 ran its `c_eff` estimator on `(E₆)₁` and on `η⁻¹` and never on the object.** This runs it on
the object.

---

## 1. WHAT WAS COMPUTED

**Prop 4.8 implemented from the paper** for `Σ(2,3,7)` — the `+1` surgery on `4₁`:
`p = b₁b₂b₃ = 42`, `α = [1, 13, 29, 41]`, signs `[−,−,−,+]`, `Ψ̃^(a)_p = Σ ψ^(a)_{2p}(n) q^{n²/4p}`.

> **Result: coefficients all `±1`, exponents `n²/168` — quadratically sparse. A false theta.
> `c_eff = 0`.**

**Ramanujan's order-7 mock theta `F₀(q) = Σ_{n≥0} q^{n²}/(q^{n+1};q)_n` implemented independently**,
for the mirror `−Σ(2,3,7)` — the `−1` surgery:

| | first twelve coefficients |
|---|---|
| **computed here** | `1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2` |
| **paper, eq (12)** | `1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2` |
| | **MATCH** |

**The paper's equation is reproduced exactly from a formula that does not mention it.** That is the
verification, and it licenses everything below.

---

## 2. THE MEASUREMENT

GC-6's own estimator, calibrated beforehand (`η⁻¹ → 0.975` vs 1; Rogers–Ramanujan `→ 0.388` vs 2/5),
run on `F₀(q)` to `N = 6000`:

| n | 500 | 1000 | 1500 | 2000 | 3000 | 4000 | 5000 | 5900 |
|---|---|---|---|---|---|---|---|---|
| `c_eff(n)` | .130633 | .133639 | .135307 | .136311 | .137505 | .138219 | .138706 | .139035 |

Fitting the estimator's own `O(n^{-1/2})` bias, `c_eff(n) = c_∞ − k/√n`:

> ## **`c_∞ = 0.142410`,  and  `1/7 = 0.142857`  — agreement to 0.3%.**

`1/6 = 0.1667` is off by 17%, `1/8 = 0.125` by 12%. **The object's boundary series is an order-7 mock
theta and its effective central charge measures `1/7`.**

---

## 3. THE TENSION, STATED RATHER THAN SMOOTHED

The paper writes the same series as `Ẑ₀ = −q^{−1/2}(1 + q + q³ + …)`. For a genuine character
`χ = Tr q^{L₀ − c/24}` the prefactor is `Δ = h_min − c/24`, and since `c_eff = c − 24h_min` this
forces **`c_eff = −24Δ = 12`**.

> **Growth says `1/7`. The prefactor says `12`. They disagree by a factor of 84.**

**That disagreement is a result, not noise.** A **mock** modular form has a shadow; its coefficient
asymptotics are not a true character's. So reading a `c_eff` off mock-theta growth and reading one
off the prefactor are **two different quantities** — which is the same category of error memo 171
charged against GC-6, appearing again one level down. **Neither number is here asserted to be "the"
`c_eff` of the object's boundary algebra.**

---

## 4. WHERE THIS LEAVES σ

| quantity | value |
|---|---|
| target, `c((E₆)₁) = 78/13` | **6** |
| object-side, growth of the mock theta | **1/7 ≈ 0.143** |
| object-side, mirror orientation (false theta) | **0** |
| object-side, prefactor reading of the same series | **12** |
| GC-6's substitute (`η⁻¹` free boson) | 1 |

**Every one of these is a different number, and GC-6's `1` is the only one that was never measured on
the object.** The honest state: **the object's boundary series has been measured for the first time,
and the measurement does not give 6 by any of the three readings.**

**And the two orientations differ** — false theta one way (`c_eff = 0`), mock theta the other
(`c_eff = 1/7`). **For an amphichiral manifold `M ≅ −M`, both readings would have to hold at once.**
`m004` is amphichiral; these surgeries are not. **Flagged as the sharpest thing here and NOT claimed
as a result.**

---

## 5. FENCES

- These are **surgeries on `4₁`**, not the cusped complement. The bridge concerns the complement.
- `Σ(2,3,7)` is **Seifert-fibered, not hyperbolic**. Eq (13) gives a genuinely hyperbolic case
  (`S³_{−1/2}(4₁)`) whose coefficients have **mixed signs**, so the growth estimator does not apply
  to it as written — **that computation is not done here.**
- `1/7` is a **fit to a bias model**, 0.3% from the rational. Suggestive, not proved.
- `c_eff` from growth and `c` from the prefactor are **not shown to be the same object's data**; §3
  is the honest reason.
