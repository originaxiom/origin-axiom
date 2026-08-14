# B852 — B451's instrument could not have found a phase transition: a demonstration, not a preregistered test

cc banking seat, 2026-08-02. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 0. THIS ARC IS NOT PREREGISTERED, AND THE REASON MATTERS

B849 and B850 were sealed before computing. **This one was not**, and it must not be dressed as if
it were: **the numerics were run exploratorily in scratch first**, and only then written up. A
preregistration authored after seeing results is worse than none — it manufactures the appearance
of a commitment that was never made.

**So the arc's trustworthiness rests on a different footing, and it must be the stated one:
an exact positive control.** The doubling map has a closed-form pressure `P(s) = (1−s)·log 2`, and
the discretisation reproduces it to **1.3×10⁻¹⁵**. That is a check the numbers either pass or fail
independently of anyone's expectations, which is what an unsealed arc has to lean on.

**The two-outcome discipline is preserved in a weaker form:** each claim below is one a control
could have contradicted, and the controls are reported whether or not they cooperated.

## 1. What is being demonstrated

The incoming bundle diagnoses a systematic bias — *"five times the hyperbolic/finite/arithmetic
version of a structure was computed when the content lived in the parabolic/infinite/dynamical
one"* — and names B451 as one instance: *"B451's **horseshoe** — uniformly hyperbolic, analytic
pressure"* against *"the **parabolic** cusp dynamics."*

**That is a diagnosis. This arc turns it into a demonstration**, because the difference between
"we computed the wrong model" and "the model we computed was structurally incapable of the answer"
is the difference between an oversight and a dead instrument.

## 2. Method

Transfer operator `(L_s f)(x) = Σᵢ |ψᵢ′(x)|^s f(ψᵢ(x))` over inverse branches, discretised by
barycentric Chebyshev collocation; `P(s) = log ρ(L_s)`.

| model | dynamics | indifferent fixed point? |
|---|---|---|
| **doubling** `T(x) = 2x mod 1` | uniformly hyperbolic — **the B451 class** | no |
| **Gauss** `T(x) = 1/x mod 1` | expanding, infinitely many branches | no |
| **Farey** `x/(1−x)`, `(1−x)/x` | **parabolic**, `F′(0) = 1` | **yes, at 0** |

**Gauss is Farey's jump transformation** — the *same* continued-fraction dynamics with the
parabolic point induced away. That pairing is the arc's control, and it is not a free choice: it
isolates the parabolic point as the only difference.

## 3. Results

**Positive control — doubling map against its closed form:**

| s | computed | exact `(1−s)log2` | error |
|---|---|---|---|
| 0.2 | +0.554517744448 | +0.554517744448 | 1.3e−15 |
| 1.0 | −0.000000000000 | +0.000000000000 | 3.3e−16 |
| 2.0 | −0.693147180560 | −0.693147180560 | 3.3e−16 |

**Worst error 1.3×10⁻¹⁵ — control PASSES.**

**Analyticity of the hyperbolic case:** second differences of `P` at s = 0.6, 0.9, 1.0, 1.1, 1.4
are **10⁻⁹–10⁻¹⁰** — numerically zero. No kink anywhere, including at s = 1 where the parabolic
model transitions.

**The three models at s = 1.0, 1.2, 1.5:**

| model | P(1.0) | P(1.2) | P(1.5) | plateau at 0? |
|---|---|---|---|---|
| doubling (hyperbolic) | +0.000000 | −0.138629 | −0.346574 | **no** |
| Gauss (expanding) | −0.011973 | −0.422414 | −0.925429 | **no** |
| **Farey (parabolic)** | **+0.000022** | **−0.000622** | **−0.000776** | **YES** |

**Grid convergence, which is what makes the plateau a result rather than a rounding artifact:**
for s < 1 the Farey values are *identical to five decimals* across n = 32, 48, 64
(s=0.2: 0.53660; s=0.5: 0.31124; s=0.8: 0.10570). For s ≥ 1 the residuals **shrink toward zero**
with n (s=1.2: −1.4e−3 → −6.2e−4 → −3.3e−4). **The plateau sharpens under refinement; the
positive branch does not move.**

## 4. What this establishes

> **A uniformly hyperbolic system's pressure is analytic, so it has no phase transition — and
> B451 computed a horseshoe. Its "no transition" was guaranteed by the choice of model, not
> discovered about the object.**

The instrument was not merely pointed at the wrong thing; **it was incapable of the answer.**

**And a structural echo, arrived at independently.** Gauss = Farey with the parabolic point induced
away, and the transition **vanishes**. That is the same shape as B737-P2's *"Dehn filling removes
the cusp ⇒ destroys exactly this"* — two unrelated routes to the same statement about where the
mechanism lives. The corpus reached it via scattering theory; this reaches it via thermodynamic
formalism on an interval map.

## 5. What this does NOT establish — and this is the load-bearing limitation

- **It does NOT show m004's transition is at s = 1, or at the programme's β = 1 / s = 2.** The
  Farey map is a **model of a parabolic point**, not m004's cross-section. m004's actual
  cross-section requires a complex continued-fraction algorithm over **ℤ[ω]** (Hurwitz-type), which
  is a real build and is **not** attempted here. **Any reading of "the transition is at 1" as a
  statement about the object would be exactly the numerology this programme exists to refuse.**
- **It does not establish genericity either way.** One parabolic model was tested. Whether the
  transition's *location* is universal across parabolic maps, or carries the cusp's data, is
  **untested** — and that is precisely the question that would decide whether this route can say
  anything object-specific.
- **It does not re-open B451.** B451's escape rate and spectral gap are results about the horseshoe
  and stand as such; what is refuted is any reading of them as evidence against a transition.
- **Nothing reaches `CLAIMS.md`.**

## Carried forward

1. **The ℤ[ω] continued-fraction cross-section** — the only route from this demonstration to a
   statement about m004. Priced, not attempted.
2. **Genericity of the transition location** across parabolic models — untested, and it decides
   whether this route can ever be object-specific. Given B850 and §3.3, **generic is the way to
   bet.**
3. This arc's unsealed status should not be repeated: the remaining T-items (T3 finite-size
   scaling, T5 the cascade count, T7 exponents) get sealed before compute.

`tests/test_b852_pressure.py`
