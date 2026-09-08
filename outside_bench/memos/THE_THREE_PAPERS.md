# MEMO 181 — THE THREE PAPERS ARRIVED: THE FENCE COMES OFF, `1/7` IS CONFIRMED TWICE, AND THE "1" IS IDENTIFIED

**Banked 2026-09-08 · outside bench (lane 1B).** The owner supplied the three papers memo 177's
head note and `fetch/FETCH_REQUEST_CEFF.md` asked for. Read under the owner's standing rule —
***"papers are old, dont rely on them, verify all"*** — so every claim below is checked against
this bench's own computations, not adopted.

**The three:**
* **[HJNP]** S. Harichurn, M. Jagadale, D. Noshchenko, D. Passaro, *"`c_eff` from Surgery and
  Modularity"*, arXiv:2508.10087v2, 50 pp., Aug 2025.
* **[Park]** S. Park, *"Large color `R`-matrix for knot complements and strange identities"*,
  arXiv:2004.02087v2, 27 pp., Jul 2020.
* **[GJ]** S. Gukov, M. Jagadale, *"`c_eff` for 3d `N=2` theories"*, arXiv:2308.05360v1, 18 pp.,
  Aug 2023.

---

## 1. The fence on memo 177 comes off

> **Neither [HJNP] nor [GJ] contains the Legendre law of memo 177 §3, or the hyperbolic ceiling
> of §5.**

[HJNP]'s scope is **Brieskorn spheres `Σ(s,t,rst±1)`** — obtained by `1/r` surgery on **torus
knots** — plus negative-definite plumbed manifolds. **The words "figure-eight", "`4₁`" and
"hyperbolic" do not appear anywhere in the paper.** [GJ]'s worked examples are `Σ(2,3,5)` and
`Σ(2,3,7)` and numerical estimates for `T[Σ(s,t,st−1)]`, all Seifert.

Memo 177's *"novelty unknown"* head note is therefore **lifted**, with these two cited.

## 2. Their definition is my estimator, exactly

[HJNP] Definition 1:

```
   c_eff(P(q)) := (3 / 2 pi^2)  limsup_{n -> inf}  (log|a_n|)^2 / n
```

This is **identical** to the estimator used in memos 174–180 (`c_eff = 3A²/(2π²)` for
`log a_n = A√n`). Their eq (13), `a_n ~ Re exp(√(2π²c_eff n/3) + 2πiωn)`, is the same Cardy form.
Their Definition 1 is described as *"a slightly revised definition from [GJ]"* — and that
revision is exactly what §3 below turns out to be about.

## 3. `1/7` confirmed twice, and the two literature values reconciled

[GJ] eq (54): **`Ẑ(Σ(2,3,7);q) = q^{−1/2} F₀(q) = q^{−1/2} Σ_{n≥0} q^{n²}/(q^{n+1})_n`** — the
same order-7 mock theta function my assembly reproduced termwise to `q³⁰⁰⁰` (memo 177 §1).

The two papers print **different numbers** for it, and both are right:

| source | value for `Σ(2,3,7)` | what it is |
|---|---|---|
| [HJNP] eq (9), `m=1, l=0` | `24/(4·2·3·7) = **1/7**` | the bare `Ẑ` `q`-series |
| [GJ] eq (55) | `**8/7**` | the **half-index**, which carries an extra `q^{−1/24}` |
| **this bench, measured** | **`0.1428571`** on 120 000 coefficients | the bare series |

**The reconciliation, checked on both of [GJ]'s worked examples:**

```
   [GJ] half-index c_eff  =  24 * A   where  Z ~ qtilde^{-A}
   Sigma(2,3,5):  A = 1/24 + 1/120 = 1/20   ->  24A = 6/5   =  1 + 1/5   [HJNP] eq (9): 1/5
   Sigma(2,3,7):  A = 1/21                  ->  24A = 8/7   =  1 + 1/7   [HJNP] eq (9): 1/7
```

> ### `[GJ] half-index c_eff  =  1 + [HJNP] c_eff`, and **the `1` is the universal `q^{−1/24}` prefactor.**

Because `q̃^{−1/24}` alone gives `24·(1/24) = 1`. Both identities are exact, on both examples.

**So three independent computations — [HJNP]'s modular eq (9), [GJ]'s mock-modular asymptotics,
and this bench's coefficient fit — give one number, once the conventions are lined up.** My
`1/7` was measured from GM's `F_{4₁}` recursion and Thm 1.2, a route neither paper uses.

## 4. What that does to GC-6's "six versus one"

Memo 178 argued that GC-6's substituted `η⁻¹` *is* the object, because `4₁`'s colored Jones tail
is `(q;q)_∞`. That stands, and is now **sharper and more general**:

> **The `1` is not a feature of the figure-eight. It is the universal `q^{−1/24}` prefactor
> carried by every half-index** — one free boson's worth, present for `Σ(2,3,5)`, `Σ(2,3,7)`, and
> the figure-eight alike.

GC-6 wrote *"the object's abelian `T[4₁]` supplies one"*. The literature's own arithmetic says the
same `1` appears for every `T[M₃]` of this type. **`L154`'s gap is `6 = 1 + 5`**: the boundary
needs five units beyond the universal one, and what varies between manifolds is the `1/5`, `1/7`,
… part — which for `Σ(s,t,p)` is `24m²/(4stp)` and for a hyperbolic surgery on `4₁` is memo 177's
Legendre transform.

## 5. Their `c_eff ≤ 1` is a different theorem from my ceiling

[HJNP] §6 proves `c_eff ≤ 1` for **negative-definite plumbed** manifolds, via Prop. 6: the
coefficients of `Ẑ_a` are bounded by a **polynomial** in `j` (Lemma 5 bounds the lattice-point
count `|D_j| ≤ (4λ_max C_a j)^s`). My `sup c_eff = 1` is over **hyperbolic surgeries on `4₁`**,
which are not plumbed at all, and is **approached, not bounded away from** — the two are different
statements about different classes that happen to share the number. **Recorded as a coincidence,
not a connection.**

## 6. Two things in [HJNP] worth carrying

* **Their Theorem 1:** the regularised `+1/r`-surgery formula and the expected form (9) are
  **generically incompatible**, first failing at `Σ(3,4,13)` where they find `m = 3√(13/5)`,
  which is not a Chern–Simons invariant of any flat connection. So **eq (9) is itself under
  attack in its own paper** — my `1/7` sits in the regime they say works (`Σ(2,3,5)` and
  `Σ(2,3,7)` are the two cases they cite as confirmed).
* **An orientation-label discrepancy between papers, flagged because memo 173 was retracted partly
  over orientation:** GM eq (175) writes `Ẑ₀(−Σ(2,3,7)) = −q^{−1/2}F₀(q)`; [GJ] eq (54) writes
  `Ẑ(Σ(2,3,7);q) = q^{−1/2}F₀(q)`. Same series, opposite orientation label. Not resolved here;
  recorded so it is not tripped over again.

## 7. [Park] delivers `F_{5₂}` — and breaks an assumption of mine

[Park] §4.4 gives `F⁺_{m(5₂)}(x,q) = x^{1/2}Σ_j f_j(q)x^j` explicitly: closed forms for `f₀` and
`f₁`, `f₂` and `f₃` as `ℚ(q)`-combinations of them, and the **quantum `Â`-polynomial** (eq 32)
in full.

**Verified here:** his closed forms
`f₀ = −q⁻¹Σ_j(−1)^j q^{j(j+1)/2}` and `f₁ = −q⁻¹Σ_j(−1)^j q^{j(j+1)/2}(1−q^{j+1})/(1−q)`
reproduce his printed expansions exactly.

**And the assumption it breaks.** [Park] opens §4.4 with: *"For any non-fibered knot `K` with
non-monic Alexander polynomial, the power series expansion of `1/Δ_K(x)` has non-integer
coefficients, meaning that `F_K`, as a power series in `x`, should have coefficients which are
**not any more Laurent polynomials but power series in `q`**."*

`5₂` is non-fibered, `Δ = 2t−3+2t⁻¹` is non-monic — so **its blocks are infinite `q`-series, not
finite-width Laurent polynomials.** Every one of `f₀,f₁,f₂` starts at `q⁻¹` and runs upward
forever.

> **Memo 177 addendum 2's criterion — *"`c_eff > 0` iff the blocks `Ξ_k` widen without bound"* —
> is ill-posed for non-fibered knots.** It was formulated on `4₁` (fibered, finite blocks) and
> torus knots (monomial blocks), and `5₂` is neither. The block half-width `⌊(k−1)²/4⌋` that
> gives GM's `c = −1/16` has no analogue here; `5₂`'s blocks are bounded **below** at `q⁻¹`, which
> would give `c = 0` and a completely different slope window.

That is a real limitation of the framework, found by the paper arriving, and it is recorded before
any `5₂` number is claimed.

## 8. A transcription error of mine, caught by a control

I transcribed [Park]'s eq (32) and solved it for `f₂` and `f₃`. **`f₂` matched his printed
`ℚ(q)`-coefficients exactly; `f₃`'s `f₀`-coefficient differed from his by exactly `−q⁶`,
denominators identical.** Deciding it against his printed `f₃` series — `2 + q − 2q² − 2q³ − 3q⁴
+ 2q⁶ + 4q⁷ + 4q⁸ + 2q⁹ − 3q¹¹` — **his formula reproduces it and mine does not.** The error is
mine.

Localised: the residual of my `n=3` equation on his verified `f₀…f₃` is exactly `Q²⁶·f₀` with the
`f₁` coefficient vanishing — so a **single monomial at `x`-degree 3**, in `a₁`, `a₂` or `a₃`. My
typed transcription matches the PDF's text layer character for character, so it is either an
extraction artefact or a misprint. **Which of the three is not yet determined**, and no `5₂`
result is claimed until it is.

## 9. Status after the three papers

| item | before | after |
|---|---|---|
| memo 177's novelty fence | *"novelty unknown"* | **lifted** — the law and the hyperbolic ceiling are in neither paper |
| my `1/7` for `Σ(2,3,7)` | measured, unchecked | **confirmed twice**, by [HJNP] eq (9) and [GJ] eq (55) once conventions are matched |
| the `1` in GC-6's "6 vs 1" | identified as `4₁`'s tail (memo 178) | **identified as the universal `q^{−1/24}`** — same conclusion, wider scope |
| `c_edge` criterion (add. 2) | "blocks widen" | **ill-posed for non-fibered knots**; `5₂` has infinite blocks |
| `F_{5₂}` | unobtainable | **in hand**, pending one localised transcription fix |
| Thm 1.3 (torus knots), unverified per memo 180 | unverified | still unverified |

## 10. Fences

* Nothing here is adopted on the papers' authority. Every comparison above is against a number
  this bench computed.
* The `c_eff ≤ 1` coincidence between [HJNP] §6 and memo 177 §5 is **recorded, not interpreted**.
* No `5₂` result is claimed. The transcription error is open.
* Gate 5 untouched; `6` appears only as `c((E₆)₁)`.
