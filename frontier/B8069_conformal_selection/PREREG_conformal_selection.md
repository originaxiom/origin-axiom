# PREREG — B8069: how much does affine isotropy pin down inside the Stein cone?

**Sealed before the compute is read.** Reproducer: `conformal_selection.py`.

## The question

B527 established two things and left one open:

- **established** — the Stein-compatible metrics on `E_s = ker ℓᵀ` form a full **6-dimensional**
  cone `𝓒 = 𝓛⁻¹(PSD(3))`, not polyhedral, with a continuous `ℝP²` family of extreme rays.
  *Stein compatibility alone cannot select a metric.*
- **established** — the affine tetrahedral metric `S_aff = ½AᵀA` lies in the **interior** of `𝓒`,
  so its distinction comes "entirely from the separate **affine-isotropy** requirement
  (`‖[e_i]−[e_j]‖² = const`), **not** from Stein evolution."
- **open** — B527 never asked how large the affine-isotropy locus *is*. It showed `S_aff`
  satisfies isotropy; it did not ask whether anything else does.

**The question:** what is the dimension of

> `𝓘 = { S ∈ Sym(E_s) : the four letters are equidistant }` , and of `𝓘 ∩ 𝓒`?

## Why it matters, stated before the answer is known

Isotropy is 6 pairwise distances forced equal — at most 5 independent linear conditions on the
6-dimensional `Sym(3)`. So the generic expectation is `dim 𝓘 = 1`: a single **ray**. A ray is a
metric **up to positive scale**.

If that is what comes out, then Stein + isotropy determine the metric uniquely up to scale, and
the one undetermined parameter is exactly the overall scale — which **B167 proves cannot come
from inside** (conserved ⟹ no internal scale; doors 1–3 shut, door 4 external). The two results
would then compose into a single positive statement rather than two absences.

## Declared outcomes — all live, no preferred result

| `dim 𝓘` | reading |
|---|---|
| **1** | isotropy cuts the 6-cone to a single ray. Metric determined **up to scale**; the residue is exactly one positive number. This is a **conformal** structure, and it composes with B167. |
| **0** | no metric is isotropic — then `S_aff` is not isotropic in `E_s` and B527's characterisation of it needs correction. Report as a correction to B527. |
| **2 or more** | isotropy underdetermines: more than scale is free. The extra freedom must be named and counted, and "the object determines a conformal structure" is **false**. |
| `𝓘 ∩ 𝓒 = ∅` | the isotropic ray is not Stein-compatible — B527's interior claim would be contradicted. Stop and recheck. |

Also recorded before reading: **the signature** of the Lorentzian completion on the isotropic
ray. Claiming `(3,1)` only counts if it is `(3,1)` on the *selected* ray, not merely at `S_aff`.

## Controls, which run before any result is read

1. **`S_aff` reproduces as Stein-interior** — driver eigenvalues all `> 0` (B527 reports
   `[0.086, 0.273, 0.387]`). If not, the setup differs from B527 and nothing may be read.
2. **`S_aff` actually satisfies the isotropy equations** as I have written them. If my equations
   reject the metric B527 built to satisfy them, my equations are wrong, not B527.
3. **Non-vacuity / falsifiability:** a *deliberately perturbed* letter configuration must give a
   **different** `dim 𝓘`. If every configuration gives the same dimension, the instrument is
   measuring nothing and the result is void.
4. **Rank is computed, not assumed** — the count of independent isotropy conditions is read off
   a rank, with the singular values printed, not inferred from "6 pairs, 5 equations".

## Banned in the write-up (THE_RULE, carried forward)

"X is impossible" with no class named · a type named from a dimension alone · "exhaustive"
applied to a sample · a negative before the detector has found the thing somewhere else ·
any claim that a number matches physics without the comparison being computed in the script.

**Required:** the class covered · what lies outside it · the control and where it appears ·
what would falsify the conclusion.

## Scope limit, stated in advance

This is a statement about **`M_*` on `E_s`** — a 4-letter substitution/transfer operator and its
stable space. It is **not** a claim about spacetime, and the word "Lorentzian" here means
*signature* `(3,1)`, nothing more. No physical identification is asserted (Gate 5).
