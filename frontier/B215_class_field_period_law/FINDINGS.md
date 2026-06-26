# B215 — the class-field period law (the conductor-split closed form)

**Date:** 2026-06-26. **Status:** the closed form for B214's conductor-split — **found and verified exact for
conductors `f ∈ {2,3,4}`**, with a sharply-characterized open boundary at higher 2-powers (`f=8`). Firewall:
standalone quantum-topology / arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V218**.

## The law

B214: the WRT period of the conjugacy class of a hyperbolic `γ ∈ SL(2,ℤ)` (trace `t`, `D=t²−4=f²D₀`,
conductor `f`) is `lcm(t−2, t+2)` on the principal class and **splits** at `f>1`. The split factor
`d(γ)=lcm(t−2,t+2)/period` is a class invariant. **The closed form:**

```
  P(γ) = lcm(t−2, t+2) / d(γ),     d(γ) = max{ d' | f : γ ≡ ±I  (mod d') }.
```

`d(γ)` is the **scalar-reduction depth** of the class — how deep `γ` reduces to the center `±I`. The SL(2,ℤ)
conjugacy classes of trace `t` are the **ideal classes of the order `ℤ[λ]` of conductor `f`** (Latimer–Macduffee
= the repo's **B92**), so the period reads the *form class* via its scalar depth in the conductor —
`B204 → B214 → B92`.

## Verified exact for f ∈ {2,3,4}

Every conjugacy class at `t = 6, 7, 10, 11, 14, 22`; the scalar-depth `d` ranges over *all* divisors of `f`:

| t | D | f | classes: (d, period) | mechanism |
|---|---|---|---|---|
| 6 | 32 | 2 | (1, 8), (2, 4) | `(2,2)≡I mod 2 → d=2` |
| 7 | 45 | 3 | (1, 45), (3, 15) | `(RL)²≡−I mod 3 → d=3` |
| 10 | 96 | 2 | (1, 24), (2, 12) | |
| 14 | 192 | 4 | (1, 48), (2, 24), (4, 12) | a class `≡I mod 4 → d=4` |

## The boundary (named, open)

At **`f = 8`** (`t=18`, `D=320` — the golden field `ℚ(√5)` with conductor 8) the scalar-depth law is
**incomplete**:
- the `≡I mod 4` class splits by `d=4` exactly as the law predicts (period 20 = 80/4) ✓;
- but **two order-2-mod-2 classes split by an extra factor 2** (period 40, not the law's 80) — `γ` is *not*
  scalar mod 2, so `d_scalar=1`, yet the period halves.

A naive "order-2 ⟹ split by 2" rule is **refuted**: at `f=2` (t=6) the order-2-mod-2 class `(4,1)` has `d=1`,
while at `f=8` the order-2-mod-2 classes have `d=2`. So the higher-2-power split is a genuinely finer **2-adic**
phenomenon (the depth of `γ` in the metaplectic/congruence filtration of the conductor), **NEEDS-SPECIALIST**.

## Honest status / tiers
- the law `d = max{d'|f : γ≡±I mod d'}`: **`[num, exact-verified for f∈{2,3,4}]`** (all classes, t=6,7,10,11,14,22).
- the `f=8` (and higher 2-power) refinement: **open / NEEDS-SPECIALIST** (a named, characterized boundary).
- Novelty UNCHECKED: indefinite-form Gauss-sum period theory is classical; this scalar-depth closed form is the
  candidate-new piece — do not claim (prior-art unrun).

## Reproduction
- `python period_class.py` — the law verified on f∈{2,3,4} (t=6,7,10,14) + the f=8 boundary pointer. (pyenv)
- `tests/test_b215_class_field_period_law.py` — 3 locks (the law for f∈{2,3,4} + the f=8 boundary are load-bearing).

## Next (L39 residual)
The **Borromean-surgery bridge** (L31): different classes = different filling slopes on the Borromean parent — does
the surgery-coefficient structure reproduce `d(γ)`? (Funar caveat: the signal lives only at conductor `f>1`.) And
the **2-adic refinement** of `d` at `f≥8` (the named boundary).
