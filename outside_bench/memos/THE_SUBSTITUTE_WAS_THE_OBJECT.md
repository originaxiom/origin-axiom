# MEMO 178 — GC-6 SUBSTITUTED `η⁻¹` FOR THE OBJECT AND WAS CHARGED FOR IT; THE SUBSTITUTE IS THE OBJECT

**Banked 2026-09-08 · outside bench (lane 1B).**
No new certificate: this reads memo 177's result against a banked corpus claim. The computations
are `certificates/ceff_scaling_law.py` and `certificates/tail_mechanism.py`.
Gate 5 untouched; `c((E₆)₁) = 6` appears only as the comparison target.

---

## 1. The charge, as this bench filed it

`B1190`/GC-6 banked the **Cardy 6-vs-1 growth reading**: *"the boundary needs six cusp-boson
units; the object's abelian `T[4₁]` supplies one"*, and the corpus records it as *"the sharpened
statement of what any bridge must supply"* — `L154` stays one bridge missing.

Memo 174 charged it:

> *"GC-6 ran its `c_eff` estimator on `(E₆)₁` and on `η⁻¹` and never on the object."*
> *"Every one of these is a different number, and GC-6's `1` is the only one that was never
> measured on the object."*

The `1` was `η⁻¹`, the free boson, standing in for `T[4₁]`.

## 2. The charge is discharged, and the reason is better than the charge

Memo 177 §5 measures the object. Over every convergent surgery slope on the figure-eight,

```
   sup_{0 < |p/r| < 4}  c_eff  =  c_edge  =  c_eff( 1/(q;q)_inf )  =  1,
```

approached as `|p/r| → 4⁻` and never attained; the last equality measured at `0.9999879` on
40 000 terms. And addendum 4 supplies *why*: the `k → ∞` limit of `Ξ_k`'s edge sequence is
`2Σ_j q^{j(j+1)}/(q;q)_∞`, whose exponential growth is that of `1/(q;q)_∞` — and

```
   eta(tau)^{-1}  =  q^{-1/24} / (q;q)_inf ,
```

so `η⁻¹` and the object's own block edge differ by `q^{−1/24}`, which does not touch `c_eff`.

> ### GC-6's `η⁻¹` was not a stand-in for the object. Up to a `q`-power it **is** the `k → ∞` edge of the figure-eight's own `F_K` blocks.
>
> The free boson is where the object's boundary growth actually lives, and the reason is that the
> colored Jones tail of `4₁` is exactly `(q;q)_∞` (computed in `tail_mechanism.py` from GM
> eq (166) alone, matched over the whole stable window).

**What is discharged and what is not.** Memo 174's charge — *the number was never measured on
the object* — was correct when filed and is now answered: it has been measured, and it is `1`.
The charge that GC-6's estimator carried uncalibrated bias stands as filed and was addressed
separately in memo 171. **Two different routes, one number.** GC-6 counted cusp bosons in the
abelian sector; memo 177 measures the Cardy exponent of `Ẑ` over surgery slopes. These are not
the same quantity by definition. **That they agree is the content here, and it is not a
tautology.**

## 3. What memo 177 adds to GC-6's reading, and what it takes away

**Adds:**

| | GC-6 | after memo 177 |
|---|---|---|
| the `1` | asserted from a cusp-boson count, `η⁻¹` substituted | **measured**, `0.9999879`, with a mechanism |
| its status | a value | a **supremum**, approached at `\|p/r\| → 4⁻` and **never attained** |
| the slope range | not stated | `\|p/r\| < 4` — beyond it there is no `Ẑ` `q`-series at all |
| why `1` | not answered | the colored Jones tail of `4₁` is `(q;q)_∞`; one free boson's worth |

**Takes away:** GC-6's `1` reads as a property of the object. It is a property of **this knot**.
Addendum 4 shows `c_edge(K) = c_eff(1/Φ_K)` and `Φ_K` is knot-by-knot; addendum 7 narrows which
end of `Φ_K` but does not verify the rule. **The 6-vs-1 gap is a fact about the figure-eight, not
about the route.**

## 4. What that does to `L154`'s "one bridge missing"

It gives the missing bridge a shape it did not have. If the ceiling is `c_eff(1/Φ_K)`, then a
boundary carrying six units needs a knot whose relevant colored Jones end is `(q;q)_∞⁶`. Memo
177 addendum 5 shows such an object **exists and is cheap** on the colored Jones side — the
connected sum of six figure-eights, `Φ = (q;q)_∞⁶`, `c_eff(1/Φ) = 5.999820` measured.

> **`L154`'s gap is no longer "six versus one with nothing in between". It is: does `Ẑ` see the
> tail that the colored Jones already has?**

That is addendum 4 §3's preregistered cell, and its prior is **OUTCOME B** on two computed
obstructions. **This memo does not move that prior.** It only observes that the quantity `L154`
needs is not missing from the knot-theory side — it is missing from the transfer.

## 5. Fences

* `6` enters only as `c((E₆)₁)`, a comparison target. No measured physical value anywhere.
* GC-6's cusp-boson count and memo 177's Cardy exponent are **different quantities that agree**;
  nothing here identifies them.
* The mechanism `c_edge = c_eff(1/Φ_K)` is verified on **one** knot and its end rule is narrowed
  but unverified (addendum 7). Everything in §4 inherits that.
* Memo 171's separate charge against GC-6's estimator bias is untouched and stands.
* This memo asserts no bridge, closes no lead, and promotes nothing to `CLAIMS.md`.
