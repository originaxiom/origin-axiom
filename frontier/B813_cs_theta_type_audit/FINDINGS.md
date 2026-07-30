# B813 — L110 Cells 0–1: the CS ↔ θ_QCD dictionary is refuted ON TYPE, with a stated mechanism

cc banking seat, 2026-07-30. **Pre-registration: the L110 execution plan, written and circulated
BEFORE any literature was retrieved**, declaring Cell 1's two outcomes. **Gate 5 absolute — nothing
here is a physics claim; this is a type audit.**

## The ordering, which is the point

The plan's single methodological commitment was **the literature gate runs first, before any
falsifier is declared** — inverting B804, where a falsifier was sealed and then found to be
**excluded by a theorem nobody had retrieved**. That rule is in `PRACTICES`:

> *A bounded falsifier declared before its governing theorem is retrieved is not yet known to be a
> falsifier.*

Cell 0 ran first. **It reached Cell 1's answer**, which is what a literature gate is for.

## Cell 0 — what was retrieved

**The object side.** For a complete finite-volume hyperbolic 3-manifold the complex volume is

> `Vol_ℂ(M) = Vol(M) + i·CS(M) ∈ ℂ/2π²iℤ` (closed) or **`ℂ/π²iℤ` (with boundary — m004's case)**

with `CS(M) := π²·cs(M)`. The universal **Cheeger–Chern–Simons class** lives on
`H₃(PSL(2,ℂ)^δ; ℤ)` (Neumann), valued in `ℂ/4π²ℤ` for SL(n,ℂ) representations. **The connection is
the geometric holonomy — flat, fixed by the hyperbolic structure, in PSL(2,ℂ).**

**The physics side.** From nLab, the Yang–Mills action is
`(1/g²)∫_X F∧⋆F + iθ∫_X F∧F`, and **θ is a coefficient prefactoring the topological term** — *"a
free parameter of the theory"*, explicitly **not dependent on spacetime geometry**.

**The bridge that genuinely exists**, and it is not the one wanted:

> `∫_M tr(F_A ∧ F_A) = ∫_{∂M} tr(A ∧ dA + (2/3) A ∧ A ∧ A)`

The 4d topological term **is** the boundary integral of a Chern–Simons form — but of the
**dynamical gauge connection A**. Correspondingly the θ-vacuum wavefunctional is
`Φ_θ(A) = e^{iθW(A)} Ψ₀(A)`, with `W(A)` the CS form of that dynamical colour field, shifting by an
**integer** under large gauge transformations and θ the phase conjugate to that winding number.
Historically the 3d CS term entered 4d physics exactly here — *"in the Schrödinger-picture
description of the vacuum angle of quantized 4-dimensional non-Abelian gauge theories."*

## Cell 1 — the type audit. **F1 FIRES.**

| | `CS(m004)` | `θ_QCD` |
|---|---|---|
| kind of object | a **computed invariant** of one manifold | a **free coupling** of the theory |
| built from | the **flat geometric holonomy**, fixed by hyperbolic structure | nothing geometric — it is an input |
| group | **PSL(2,ℂ)** | **SU(3)** colour |
| value in | `ℂ/π²iℤ` (cusped case) | `ℝ/2πℤ` |
| role in the formula | — | the **coefficient** in `e^{iθW(A)}` |

**The refutation is a role collision, not a missing link.** In `e^{iθW(A)}` the Chern–Simons object
already occupies the **functional** slot — and it is a functional of the *dynamical colour field*.
A dictionary asserting `CS(m004) = θ_QCD` would place a Chern–Simons quantity in the **coefficient**
slot of the very expression whose functional slot a Chern–Simons quantity already fills.

**Three independent mismatches, any one sufficient:**

1. **Kind** — a fixed invariant cannot be a free coupling. θ is an *input* to the theory; `CS(m004)`
   is an *output* of a manifold.
2. **Group** — PSL(2,ℂ) geometric holonomy versus SU(3) colour. The same shape as **B736's
   equivariance wall**: no equivariant map between representations with unrelated structure groups.
3. **Slot** — coefficient versus functional, in one expression.

**This is exactly the outcome the plan pre-stated as expected**, and it now has a *stated mechanism*
rather than an absence — which is what B812 found the physics surface mostly lacks.

## What is closed, and what is not

**Closed:** the direct `CS(m004) = θ_QCD` identification. B812's most advanced target now has a
**reason**, not a gap. `L110` is dispositioned at Cell 1 without reaching Cells 2–3, and the
obligation set is not needed.

**Not closed, and stated so it is not over-read:** this refutes *the direct identification*. It does
**not** prove that no construction relates hyperbolic geometry to a gauge-theory θ-parameter — only
that the obvious one is a type error. Any future attempt must first supply a construction making
m004 **the spatial slice** *and* the geometric PSL(2,ℂ) holonomy **the colour field**. Both look
untenable; **both are now checkable statements rather than impressions.**

**A recorded negative:** the searches surfaced **no** work placing gauge theory on a *hyperbolic*
3-manifold slice in a way that ties θ to the slice's geometry — one search returned explicitly that
the results *"don't specifically address hyperbolic geometry aspects."* Consistent with B812's
finding that no registered lead covered this map.

## Honest limits of the sources

Cell 0 used **textbook- and reference-level statements** (nLab; the standard Stokes relation; the
Neumann abstract for the PSL(2,ℂ) target), not primary papers read end to end. **For a type audit
that is the appropriate level** — establishing that θ is a coupling and `W(A)` a functional of the
dynamical field needs no research paper. It would **not** suffice for Cells 2–3, which are not
reached.

**Sources:** [complex volume (nLab)](https://ncatlab.org/nlab/show/complex+volume) ·
[theta angle (nLab)](https://ncatlab.org/nlab/show/theta+angle) ·
[Neumann, *Extended Bloch group and the Cheeger–Chern–Simons class*](https://arxiv.org/abs/math/0307092) ·
[*The volume and Chern–Simons invariant of a representation*](https://arxiv.org/abs/0710.2049) ·
[*Strong CP problem, theta term and QCD topological properties*](https://arxiv.org/html/2510.03059v1)

`tests/test_b813_type_audit.py`
