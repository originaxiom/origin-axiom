# xB028 — PREREGISTRATION (a second-bench verification; what was already run is declared)

**Seat `xb`, `sep16-branch`, 2026-09-18.**

## P0

Invariant trace fields of closed hyperbolic Dehn fillings. Named mathematics. **No value, nothing to
`CLAIMS.md`. Gate 5 absolute.**

## WHAT WAS ALREADY RUN BEFORE THIS SEAL — declared in full

**This is a verification of an incoming correction, so its checks were run as the correction was
read.** Sealing after the fact would misstate the order:

1. The invariant trace fields of `m004(5,1)`, `m004(6,1)`, `m004(8,1)`, `m004(7,1)` and the Weeks
   manifold `m003(−3,1)` were computed here with a PARI `algdep` instrument under the **xB024 height
   guard**, before this file existed.
2. `tests/test_b288_*.py` was read.

**No prediction below was made before its data.** This arc claims **no** preregistered kill
condition and must not be read as carrying one.

## What the arc does

A seat on the paper lane reported that main's sentence *"of the grid's 78 closed hyperbolic
fillings, zero keep `ℚ(√−3)` and zero are arithmetic"* is **false in its second half** — three
fillings are arithmetic — and that the record corrected itself in **B718** (July) and never
propagated it. That seat was mid-repair (**B1376**) when it stopped.

This arc **verifies what a second bench can verify**, **diagnoses the lock precisely**, and
**does NOT perform the repair**, which is B1376's and whose duplication would be a collision of the
kind this record has already been bitten by.

## Cells

- **A1** — compute the invariant trace field `k = ℚ(tr Γ⁽²⁾)` for the five manifolds, under the
  height guard, with the **Weeks manifold as a positive control** (its field is the cubic of
  discriminant **−23**, a textbook value).
- **A2** — the load-bearing inference, checked independently of arithmeticity: **can any of these
  fields contain `ℚ(√−3)`?**
- **A3** — the lock, diagnosed and **flagged, not repaired**.

## Controls

- **The height guard is absolute:** a field that cannot be determined within the guard is reported
  **UNDETERMINED, never guessed.** This instrument's precision ceiling is SnapPy's quad-double
  holonomy; the lane's 1000-bit polished holonomy is **not** available here and the arc says so.
- **A positive control with a textbook answer** (Weeks, disc −23).

## What this arc may NOT do

It may not repair B288's lock. It may not claim the three fillings arithmetic on its own authority —
**arithmeticity needs the cocompact criterion (invariant quaternion algebra ramified at every real
place), which this arc does NOT compute.** It verifies **trace fields**, which is a necessary
ingredient and not the whole criterion. It supplies no value.
