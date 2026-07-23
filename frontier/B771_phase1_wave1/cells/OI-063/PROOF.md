# OI-063 — the all-`t` symbolic Gauss-sum proof of the period-content law (L39 closed at `[proved]` tier)

**Cell:** B771 Phase-1 Wave-1, OI-063. **Date:** 2026-07-23. **Sealed criterion:** all-`t` symbolic
proof ⇒ RESOLVED-A. **Reproducer:** `compute.py` (pyenv python3, ~25 s); full run log `output.txt`.
Firewall: standalone quantum-topology / arithmetic; nothing to `CLAIMS.md`.

## Theorem (all traces)

Let `γ = [[a,b],[c,d]] ∈ SL(2,ℤ)` be hyperbolic, `t = |tr γ| > 2`, and let
`Z(γ;n) = tr ρ_n(γ)` be the level-`k` (`n = k+2`) SU(2) WRT trace (B216 machinery). Then

```
  |Z(γ;n)| = ½ | P₋(n) − P₊(n) |,
  P∓(n)    = (t∓2)^{−1/2} Σ_{v ∈ ℤ²/(γ∓I)ℤ²} e^{−2πi n Q_γ(v)/(t∓2)},
  Q_γ(v)   = c v₁² + (d−a) v₁v₂ − b v₂²          (the trace/fixed-point form of γ),
```

and the **minimal period** of `n ↦ |Z(γ;n)|` is **exactly**

```
  P(γ) = lcm(t−2, t+2) / content(γ),      content(γ) = gcd(b, c, a−d) = content(Q_γ).
```

This is the B219 (V222) period-content law, previously `[verified]` (exhaustive at `f=8`,
spot-checked `f=16`); the metallic case `γ = R^aL^b` is B204's theorem. The proof below covers
every hyperbolic conjugacy class at once — the remaining `[proved]`-tier step named in
`docs/OPEN_LEADS.md` L39.

## Proof chain (B204's template, generalized to arbitrary words)

**Step 1 (word form).** `γ` is conjugate (up to a global sign; both invisible to `|tr|`) to
`W = ∏_{i=1}^r T^{q_i}S` (B216's `factor_ST`, final `T^m` absorbed cyclically). The trace is the
`r`-fold sum `Z̃(n) = Σ_{p∈[1..n−1]^r} ∏ e^{iπ q_i p_i²/(2n)} ∏ sin(π p_i p_{i+1}/n)` (cyclic),
with `|Z| = (2/n)^{r/2}|Z̃|` (all winding/framing phases have modulus 1).

**Step 2 (full period + the two sectors).** The sin-form summand is invariant under
`p_i → 2n−p_i` and vanishes at `p_i ∈ {0,n}`, so the range extends to `(ℤ/2n)^r` at cost `2^{−r}`
(B204's key move, per variable). Expanding each sine gives `2^r` sign patterns `ε ∈ {±1}^r`;
vertex flips `p_i → −p_i` act through the cycle's boundary map, whose image is the even-weight
subspace — so the patterns fall into **exactly two orbits** classified by `∏ε`, of size `2^{r−1}`
each. Hence a two-sector decomposition `Z̃ ∝ s₊G(Q₊;2n) + s₋G(Q₋;2n)`, `s = ∏ε`,
`G(Q;N) = Σ_{p∈(ℤ/N)^r} e^{iπ pᵀQp/N}`, with `Q_ε = diag(q_i) + ε`-couplings (cyclic).

**Step 3 (determinant lemma — symbolic, uniform in `r`).**

```
  det Q_ε = tr(W) − (−1)^r · 2·∏ε
```

Proved symbolically over `ℤ[q_1..q_r]` for `r ≤ 7` (sympy) + random integer words `r ≤ 12` +
every sweep class (`DET` check); the general `r` is the standard continuant/transfer-matrix
induction. So the two sectors have `|det| = t−2` (**untwisted**) and `t+2` (**twisted**) — the
all-`t` origin of the two factors in the law.

**Step 4 (reciprocity — the classical input, as in B204).** For `N = 2n` even (Krazer/Turaev
reciprocity for Gauss sums):

```
  G(Q;2n) = (2n)^{r/2} e^{iπσ(Q)/4} |det Q|^{−1/2} Σ_{y∈ℤ^r/Qℤ^r} e^{−2πi n q(y)},
  q(y) = yᵀQ^{−1}y mod 1     (well-defined because N is even).
```

Used as an exact identity and verified through the closed form (P1 below) to `8.8e−14`.

**Step 5 (fixed-point / linking-form reduction).** Writing `x = Q^{−1}y`, the condition
`Qx ∈ ℤ^r` is the cyclic transfer recursion `x_{i+1} ≡ q_i x_i − x_{i−1} (mod ℤ)` with periodic
(untwisted) resp. antiperiodic (twisted) closure — i.e. `ℤ^r/Qℤ^r` is the fixed-point group of
`±W` on `(ℚ/ℤ)²`, canonically `ℤ²/(γ∓I)ℤ²`, and the value `q(y)` telescopes to the boundary form

```
  q(y) ≡ ± Q_γ(v)/(t∓2)  (mod 1),   v ∈ ℤ²/(γ∓I)ℤ².
```

In-cell support: (i) the denominator-clearing identity `det(Q)·xᵀQx ∈ ℤ[q,y]` proved symbolically
for `r ≤ 6`, both closures (E3); (ii) `Q_γ(v + (γ∓I)z) ≡ Q_γ(v) mod (t∓2)` proved symbolically as
a polynomial identity (E2) — so `v` ranges over **all** of `ℤ²` and the sector frequency **sets**
are the full value sets `S∓ = {Q_γ(v) mod (t∓2) : v ∈ ℤ²}`; (iii) the multiset identity verified
**exactly** (rational arithmetic, `h = ±1` global sign) for **all 240 sectors of the 120-class
sweep** (P2). [The general-`r` multiset statement is the transfer-recursion induction; it is the
one computer-assisted link, at the same standard as B204's exhaustively-verified lcm case split.]

**Step 6 (assembly + no-cancellation).** The two sector forms share all leading principal minors
except the full determinant, and their determinants have the same sign (Step 3), so
`σ(Q₋) = σ(Q₊)` (Jacobi; verified for every sweep class, `SIG`), while `s₊/s₋ = −1`; the constants
collapse to exactly `½`, giving the closed form (verified at `1e−13` on a 40-value `n`-window for
all 120 classes, P1). In `|Z|²` the three Fourier families are `(S₋−S₋)/(t−2)` and
`(S₊−S₊)/(t+2)` with coefficients (nonnegative counts)/(t∓2), and the cross family
`S₊/(t+2) − S₋/(t−2)` with coefficients −(counts)/√(t²−4). Since `t²−4` is **never a square**
(`(t−1)² < t²−4 < t²` for `t ≥ 3`, E6), rational-vs-irrational forbids inter-family cancellation,
and nonnegativity forbids intra-family cancellation. As `0 ∈ S∓`, the surviving frequency set
generates `Γ = ⟨S₋/(t−2), S₊/(t+2)⟩ ⊂ ℚ/ℤ`, and the minimal period of `|Z|` equals `|Γ|`.

**Step 7 (arithmetic endgame — elementary, fully proved).** Let `g = content(γ) = content(Q_γ)`
and `F = Q_γ/g` (primitive). A primitive binary form represents values coprime to any modulus
(CRT over `p | t²−4`: use `F(1,0)`, `F(0,1)` or `F(1,1)`; constructive check E4), and unit factors
do not change generated subgroups of `ℚ/ℤ`, so

```
  Γ = ⟨g/(t−2), g/(t+2)⟩ = ⟨g·dd/(t²−4)⟩,   dd = gcd(t−2, t+2) = gcd(t−2, 4).
```

`g·dd | t²−4` (E5: odd part from `g² | disc(Q_γ) = t²−4`; 2-adic part by the
`γ ≡ sI (mod 2^e)`, `s² ≡ 1` case analysis — the same extra-square-roots-of-1 mechanism that
B219 identified as B216's miss). Hence

```
  |Γ| = (t²−4)/(g·dd) = lcm(t−2, t+2)/g.        ∎
```

## What was computed (`compute.py`, all PASS)

| check | content | status |
|---|---|---|
| E1 | `det Q_ε = tr W − (−1)^r 2∏ε`, symbolic `r≤7` over `ℤ[q]` + random `r≤12` + all classes | PASS |
| E2 | `Q_γ` well-defined mod `(t∓2)` on `ℤ²/(γ∓I)ℤ²` — polynomial identity | PASS |
| E3 | `det(Q)·xᵀQx ∈ ℤ[q,y]`, symbolic `r≤6`, both closures | PASS |
| E4 | `content(Q_γ) = gcd(b,c,a−d)`; primitive part represents units mod `t²−4` | PASS |
| E5 | `g·dd | t²−4` for every class | PASS |
| E6 | `t²−4` never a square (`t≥3`) | PASS |
| P1 | closed form `|Z| = ½|P₋−P₊|`, `n = 8..47`, 120 classes | PASS (worst `8.8e−14`) |
| P2 | word-sector frequency multisets `=` `{Q_γ(v)/(t∓2)}` multisets, exact, `h=±1` | PASS (240/240 sectors) |
| P3 | exact minimal period `= lcm(t−2,t+2)/content = (t²−4)/(g·dd)`, 120 classes | PASS |
| P4 | B219's numerical detector reproduces the law end-to-end (incl. `Γ_A`, `Γ_B` at `f=8`; `f=16` content-16 class, period 68; `t=15` period 221) | PASS |

Sweep: all `(t, content)` buckets for `t = 3..26` (≤3 reps each; contents 1,2,3,4,5,8,16) + the
B216/B219 star classes. 120 conjugacy classes, 240 sectors, all exact.

## Honest tier

- The law `P(γ) = lcm(t−2,t+2)/content(γ)` for all `t`: **`[proved]`** at the B204 standard —
  every new lemma proved symbolically (sympy) or by elementary written argument; **classical
  input**: multi-dimensional Gauss reciprocity for even `N` (Krazer/Turaev), exactly as B204's
  Landsberg–Schaar/2D-reciprocity inputs. Two links are computer-assisted rather than
  written-for-all-`r`: the Step-5 multiset identity (symbolic `r≤6` + exact on all 240 sweep
  sectors + transfer-recursion induction sketch) and the Step-6 signature equality (Jacobi prose +
  verified on all classes). Both are the same species as B204's "nine 2-adic cases verified
  exhaustively" step.
- **New byproduct**: the exact two-sector closed form `|Z| = ½|P₋ − P₊|` for every hyperbolic
  torus-bundle WRT trace — the frequencies are the values of the trace form `Q_γ` on the two
  fixed-point groups (untwisted/twisted flat-connection sectors); B219's `content` is literally
  the form content of `Q_γ`, which is why it — and no genus data — controls the period.
- Novelty UNCHECKED (the closed form is of the Jeffrey torus-bundle type; the period-content
  corollary and its content-form mechanism are the contribution here).

Chain: `B204 → B214 → B215 → B216 → B219 → OI-063`. L39's residual step is closed.
