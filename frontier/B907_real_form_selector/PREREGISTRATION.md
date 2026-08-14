# B907 PREREGISTRATION — the real-form selector (J1; sealed before compute)

**Date sealed:** 2026-08-05 · **Seat:** cc (banking; joint cell with the solo seat's
W3) · **Status:** SEALED BEFORE COMPUTE

## The question

The second-measurement wall is COMPLEX in the split form e₆(6): γ real, a imaginary,
at all three Galois roots (B892/B893; the solo seat's sealed §XXXVII, met). B901
sharpened the stakes: no real symmetry of the split frame can carry c into θ — the
transfer channel is the complexification. The solo seat's W3 and value-layer V3(ii)
give the same cell from two more directions: WHICH REAL FORMS of E₆ make the wall
REAL? A form that does would (a) be layer 8's front door, (b) fix the canonical
Hermitian norm that scales the 15 flavor atoms — the value layer's gate, (c) answer
whether the object's measurement chain SELECTS a real form.

## The operation (MB12-checked: non-trivial, can pass, can fail)

The five real forms of E₆ correspond to the five Cartan involutions θ_r up to
conjugacy, with maximal compact subalgebras: sp(4) (36, split e₆(6)); su(6)⊕su(2)
(38, e₆(2)); so(10)⊕u(1) (46, e₆(−14)); f₄ (52, e₆(−26)); e₆ itself (78, compact).
For each form:

1. Construct an explicit involution θ_r in the built frame whose fixed subalgebra
   has the form's dimension and type (verified by dimension + derived structure +
   Killing signature — three gates per form), chosen C-compatibly where possible
   (θ_r stabilizing the measurement torus C or its relevant subspace; if no
   C-stable representative exists in a conjugacy class, that form's cell reads the
   obstruction itself as its result — recorded, not skipped).
2. Under the form's conjugation σ_r = θ_r ∘ σ_split, recompute the wall tower's
   reality: the signs of γ² and a² as seen in the form's real frame at each of the
   three Galois roots (exact where the tower permits, 35-digit certified otherwise).
3. The wall is REAL in form r iff both γ and a are σ_r-real on some branch at some
   root (recorded per root — Galois uniformity is a finding, not an assumption).

## The two-outcome criteria

- **OUTCOME A — THE SELECTOR SELECTS:** exactly ONE of the four non-split forms
  makes the wall real (the split form is already banked complex). The selected
  form is the result.
- **OUTCOME B — NO SELECTION:** zero, or two or more, non-split forms make the
  wall real.
- **UNSTABLE:** any form where no C-compatible involution representative can be
  constructed AND the obstruction computation itself fails to certify (the cell
  then narrows to the certifiable forms and says so explicitly).

Both outcomes are live: A fails if reality is generic across forms or impossible
outside further complexification; B fails exactly when A holds.

## The disclosed prior (stated, then the cell decides — B890's lesson)

**Lean A, selected form e₆(−14), confidence low-moderate.** Reason (structural,
noticed at design time): e₆(−14)'s maximal compact subalgebra is so(10)⊕u(1) —
**exactly the FMT's first-measurement centralizer type (dim 46, the banked z(x₁))**.
If the first measurement's centralizer is the fixed algebra of the form's Cartan
involution, the first breaking IS the form's compact/noncompact split — and the
wall tower's reality flips accordingly. No computation behind this beyond the
dimension/type match; the cell decides.

## What this cell does NOT decide (pre-stated)

Physics identification of the selected form (Gate 5 — no "the physical real form
is…" claim); the Hermitian-norm/value-table computation (V3(ii) — a SEPARATE cell
gated on this one's outcome); mechanism-hood of anything.

## Files (to be produced AFTER sealing)

- `real_form_selector.py` → `results.json` (five forms × three gates × the
  reality table per root)
- `FINDINGS.md` with the verdict under these criteria verbatim
- Locks: `tests/test_b907_selector.py` (seal-integrity lock first, results locks
  at banking)
