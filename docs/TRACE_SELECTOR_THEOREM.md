# A conditional trace selector theorem

**Status:** formalization of conditional claim **C5** (`../CLAIMS.md`). This is
not a promotion to `proven`. It packages the B38-B47 frontier campaign into one
bounded statement:

```text
T1 -> S1 -> I=1/4 -> lambda/h=1
```

where **T1** is an explicit assumption, not a derived theorem.

**One line:** once the half-step trace lift and projective quotient are accepted,
the coupling selector is forced only if the primitive projective tangent return
inherits the original arithmetic persistence filters. That inheritance is the
remaining object to justify.

---

## 1. Inputs already available before T1

The selector theorem rests on the existing governed chain:

```text
A1-A6 -> A=LR                         (C1; conditional uniqueness)
exchange / half-step -> F=LP, F^2=A   (frontier B14, B16, B19)
F trace lift -> trace map T_F         (frontier B18)
central-sign quotient -> projective return data (frontier B28-B31)
```

These steps do **not** select `I=1/4`. B30-B31 show that the projective quotient
is natural for lift-independent `PSL` trace data, but primitive projective return
alone leaves the one-parameter family

```text
I = c^2 - 1
```

free. That is why the selector is not already proven.

---

## 2. The missing rule

The missing rule isolated by B32 and B40 is:

```text
S1: the primitive projective return linearization reproduces the original
    A-sector t^2 - 3t + 1.
```

B38-B47 move the gap one level deeper by identifying a cleaner sufficient
condition:

```text
T1: the primitive projective tangent return inherits the original arithmetic
    persistence filters.
```

Here "original filters" means the same kind of arithmetic filters used in the
conditional uniqueness theorem for `A`: integer hyperbolic trace with minimal
positive hyperbolic trace, equivalently the tangent analogue of torsion-one
closure. T1 is motivated by filter reuse, but it is not derived from A1-A7 plus
exchange.

---

## 3. The calculation

On the primitive projective return family, the tangent quadratic is

```text
q_c(t) = t^2 - mu(c) t + 1
mu(c) = 4c^2 - 2 = 4I + 2.
```

If T1 applies, then the minimal positive integer hyperbolic trace is selected:

```text
mu = 3.
```

Substituting into `mu=4I+2` gives

```text
I = (3 - 2)/4 = 1/4.
```

The same value follows from the tangent torsion-one route:

```text
|det(M-Id)| = |2 - mu| = 1
positive hyperbolic branch -> mu=3.
```

The selected tangent quadratic is therefore

```text
q_c(t) = t^2 - 3t + 1,
```

which is exactly the `A` characteristic polynomial. That is S1.

The Fibonacci Hamiltonian normalization used by B25 is dimensionless:

```text
I = (lambda/h)^2 / 4.
```

So `I=1/4` gives

```text
(lambda/h)^2 = 1
lambda/h = 1        (positive coupling branch)
```

This is the strongest current route to `lambda/h=1`. It is conditional on T1.

---

## 4. The theorem

> **Theorem (conditional trace selector).**
> Given the conditional record core, the exchange/half-step structure, the
> functorial half-step trace lift, the central-sign projective quotient, and T1,
> the primitive projective tangent return selects the `A` quadratic sector
> `t^2 - 3t + 1`. Equivalently, it selects `I=1/4`, hence dimensionless
> `lambda/h=1` under the B25 Fibonacci Hamiltonian normalization.

This theorem is exact under its assumptions. Its open point is not the algebra
after T1; it is whether T1 is natural, standard, derivable, or inserted.

---

## 5. Lucas hierarchy control

B29 also records an exact hierarchy under the broader projective half-return
matching criterion. Matching even powers `F^n` gives

```text
char(F^n) = t^2 - L_n t + 1
I = (L_n - 2)/4
(lambda/h)^2 = L_n - 2
```

with first values

```text
1, 5, 16, 45, 121, 320, ...
```

The `lambda/h=1` surface is the primitive first member of this hierarchy. The
hierarchy is exact algebra, but it is not by itself a physical spectrum or a
derivation of T1.

---

## 6. What this establishes

**Does:**

- Replaces the vague question "why `lambda/h=1`?" with one precise dependency:
  justify T1.
- Shows that if T1 is accepted, the algebra forces `I=1/4` and `lambda/h=1`.
- Explains why B38, B43, B44, and B45 all recover the same value: each is a
  route that reapplies original arithmetic persistence filters to the tangent
  return.
- Provides a clean external-review target: is T1 a theorem, a known naturality
  principle, or an extra axiom?

**Does not:**

- Derive T1 from A1-A7 plus exchange.
- Promote `lambda/h=1` to a proven claim.
- Turn the Fibonacci spectrum anchor into a physical prediction.
- Prove an exact Hausdorff dimension.
- Derive matter, gauge structure, spacetime, gravity, or awareness.

---

## 7. Evidence and reproduction

Primary probes:

```bash
python frontier/B38_tangent_return_arithmetic_filter/probe.py
python frontier/B40_filter_reuse_audit/probe.py
python frontier/B47_s1_verdict_ledger/probe.py
```

Supporting controls:

```bash
python frontier/B25_fibonacci_spectrum_anchor/probe.py
python frontier/B26_lambda1_derivation_attempt/probe.py
python frontier/B28_projective_quotient_legitimacy/probe.py
python frontier/B29_hierarchy_normalization_controls/probe.py
python frontier/B30_projective_state_space/probe.py
python frontier/B31_primitive_projective_return_selector/probe.py
python frontier/B32_selector_axiom_audit/probe.py
python frontier/B37_operational_feedback_quarantine/probe.py
```

The full test suite remains the guardrail for the proven core:

```bash
python -m pytest -q
```
