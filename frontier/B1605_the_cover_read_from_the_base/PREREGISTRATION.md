# B1605 — PREREGISTRATION: THE COVER READ FROM THE BASE — the 29 threads whose forced kernels B1604's audit found unreliable at 40 digits, re-read through a Reidemeister–Schreier presentation of the cover and the thread's polished holonomy, with the four's relator residual and the Euler constraint as acceptance

cc (main), 2026-10-08, after S84. A weave arc by inheritance (B1602's population, the part main could not read). The
instrument never triangulates the cover: π₁ of the forced cover is presented by Reidemeister–Schreier from the thread's
own SnapPy presentation and the permutation action on the sheets — Schreier generators t_i g t_{i·g}⁻¹ (short words in
the base generators), one rewritten base relator per sheet (each of the base relator's length), the cusps as the
stabiliser sublattices of the base cusp group on the sheets — and the holonomy is the thread's *polished* holonomy
(SnapPy's Newton-refined shapes, here 200 bits) on those words; B1492's stacked instrument then runs unchanged at 40
digits. **Sealed with the runs launched seconds before and no output read**; the instrument's hash is on
`ARTIFACT_HASHES.txt`. No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /Reidemeister|Schreier|polished holonomy|transversal|stabiliser|cover presentation/: 20 of 1377 arcs on main match (NEGATIVE 2, PROVED 18)`
— B1494 (companions by Smith form and `cover(perms)`), B1497 (`low_index_subgroups` → coset tables → covers), B1602
(the forced kernels), B1604 (the audit; `tiers.json`). **Seen before the seal, as validation on clean covers:** on −LR's
forced cover the Schreier presentation has 13 generators, 12 relators of length ≤ 7, four cusps of three sheets with
stabiliser bases ((−1, 0), (0, −3)), the four's relator residual 3.9 × 10⁻⁵² at 300 bits, 16 sign characters, and the
trivial character reads (h¹, r¹, n) = (4, 4, 0) as SnapPy's cover did (B1602); the full validations on ±LR (every member
and reading against B1602's 24 × (1, 0, 1) and 6 × (4, 0, 4)) are running and will be reported as V1. **Literature:**
Reidemeister–Schreier (standard); SnapPy's `polished_holonomy` (its SL(2) lift fails on threads with torsion in H₁ —
the PSL polish is used, normalised to determinant one; the four is blind to the lift's sign).

## Disclosed

Population: the 29 threads with at least one unreliable forced kernel in `B1604/verification/tiers.json` (19 of odd
trace — every length-eight odd-trace thread, −LLLRLR, ±LLRLRR — and 10 of even trace), every forced kernel of each
(the reliable kernels of those threads re-read too, as a further control). Acceptance per kernel: the four's relator
residual < 10⁻³⁰ and χ = 0 at every sign character; a kernel failing either is reported as unread, not as a result.
Numerical ranks at 40 digits with B1492's tolerance; sign characters only; the run parallel over three workers.
Not blind to B1602's (withdrawn) readings on these covers.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **V1** | on ±LR the Schreier read reproduces B1602 member for member: +LR 24 × (1, 0, 1) reading (−1, −1); −LR 6 × (4, 0, 4), every class (0, −3) | 90% |
| **R1** | every re-read kernel passes acceptance (residual < 10⁻³⁰, χ = 0 everywhere) | 80% |
| **R2** | no odd-trace thread among the 19 carries a member on its forced A₄ kernel — the seat's census extended to length eight at order two, ±LR alone | 65% |
| **R3** | of the 10 even-trace threads, the carrier/non-carrier status B1602 recorded at 40 digits changes on at least one | 50% |
| **R4** | no new kind of reading beyond B1603's six on reliable covers | 60% |

**Reading rules.** V1 false: the instrument is wrong and nothing below is read. R2 false at a thread: a carrier on
odd trace beyond ±LR, named, with its readings — and this time certified by the residual and χ = 0; the question of
what admits a thread reopens with it. R2 true: the root's pair is alone on odd trace to length eight at order two.

## Instruments

`verification/schreier_cover.py`; hashes in `ARTIFACT_HASHES.txt`.
