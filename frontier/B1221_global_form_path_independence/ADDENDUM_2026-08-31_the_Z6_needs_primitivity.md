# Addendum (2026-08-31) — the ℤ₆ is path-independent but **not normalisation-independent**

**Not an edit. Found by auditing this arc after the owner asked whether our gates are killing
positives — the audit found the opposite problem here: a claim I typed as settled carries an
unstated condition.**

## What this arc proved, and what it assumed

The arc computes the kernel of $Z(\mathrm{SU}(3))\times Z(\mathrm{SU}(2))\times \mathrm{U}(1)_Y$
acting on the 27 and finds **ℤ₆**, concluding correctly that the result is **path-independent** —
SU(5) appears nowhere, so every descent chain yields it.

**But the computation used the integer normalisation $y = 6Y$**, i.e. the *primitive* one, and did
not say so as a hypothesis. Rescaling every charge by $k$:

| k | gcd(k,6) | \|kernel\| |
|---|---|---|
| 1, 5, 7, 11 | 1 | **6** |
| 2, 10 | 2 | 12 |
| 3, 9 | 3 | 18 |
| 4 | 2 | 24 |
| 6 | 6 | 36 |
| 12 | 6 | 72 |

**|kernel| = 6 exactly when gcd(k, 6) = 1** — the primitive normalisation and its unit rescalings,
and nothing else.

## Why this matters, and it is this programme's own no-go that makes it matter

The anomaly conditions are **homogeneous** in the abelian charge — that is banked (B991/B864), and
the paper states it as the reason the hypercharge *normalisation* is **not derivable in principle,
by anyone**. So the scale that makes the charges primitive is **not supplied by the anomaly
computation**. It is a convention — canonical, universally used, and still a convention.

> **The corrected statement.** The global form is $\Z_6$ **given the primitive integral
> normalisation of hypercharge**, and it is path-independent within that. What the construction
> forces is the *kernel of the representation at a fixed normalisation*; what it does not force is
> the normalisation, and the programme has its own theorem saying so.

## What stands and what is fenced

- **Stands:** path-independence (SU(5) is not used), the kernel computation, the MB12 controls, and
  the verdict that the ℤ₆ mechanism is classical rather than new.
- **Fenced:** "the chain forces ℤ₆" now reads "forces ℤ₆ at the primitive normalisation." A referee
  who noticed the homogeneity result two sections earlier would ask exactly this, and the honest
  answer should be in the text rather than in their report.

## The methodological note, since it is the second of its kind today

B1224 recorded a kill condition that used the wrong *observable*. This is the mirror failure: a
computation that used the right observable at an **unstated normalisation**. Both are the same
underlying lapse — **the hypothesis was not fully written down before the test** — and both were
caught only when someone asked whether the machinery was being applied properly.
