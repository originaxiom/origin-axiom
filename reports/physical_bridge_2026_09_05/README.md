# Physical bridge audit — 2026-09-05

Base repository: **`f06d34054899e8c23672b836a7c534af77cbd35d`**.
Work is local on `audit/physical-bridge-2026-09-05`; no push. Upstream through
8f83b5c8 has been merged and independently audited: [first landing](UPSTREAM_AUDIT.md),
[second landing](UPSTREAM_SECOND_AUDIT.md). Original baseline totals remain
pinned to f06d3405; they are not a certificate for this updated branch.

The [third upstream audit](UPSTREAM_THIRD_AUDIT.md) checks fetched B1259 at
9a79adfd without merging that window: its true element lemma does not certify
a theorem about all enhancement strata. Exact subgroup controls preserve
B1084's geometry and expose the quantifier gap; no chiral matter is derived.
Its first exporter failure and separately sealed successful rerun are retained.

**Latest physical result:** [R9's leading infrared alignment logarithm](INFRARED_ALIGNMENT.md)
favors the neutral orientation in the stated weak-coupling limit. Exact
all-complex-field traces give 6 gW^2 gY^2+16 y^4, or 23/80 at the chosen
reference couplings; log(epsilon) is negative. The charged pair that was
flat in R8 gets a positive leading-log restoring contribution. The
complete light-Higgs invariant basis retains an allowed finite alignment
term, so **finite matching is still required** before either earlier
parameter point has a full vacuum-selection verdict. This is conditional
progress in the chosen action, not source-derived physics or a TOE.

**The preceding result:** [R8's leading broken-vacuum theory](BROKEN_VACUUM.md)
is computed over all 19 physical light fields, including heavy exchange and
the complete light quantum curvature. Neutral minima preserve actual color
and electromagnetism, but charge-breaking minima have equal leading energy.
The neutral full fermion matrix has rank 27 at the evaluated backgrounds:
the rank-16 leading light projection must not erase its smaller seventeenth
light mass. Three physical scalar zeros remain at the neutral minimum at
this order. This is a conditional leading EFT, **not** vacuum selection,
a complete quantum vacuum, pole matching or a TOE.

R7's [priced Higgs extension](HIGGS_SECTOR.md) and its quantum feedback are
the inputs. R8's predeclared small-coupling family reduces the normal shifts
and verifies all-component force scaling; it is not RG running or a physical
scale derivation. [Full output](broken_vacuum_first_run.json) and
[captured checks](BROKEN_VACUUM_CHECKS.txt) are retained.

The earlier [one-loop angular result](QUANTUM_VACUUM.md) and
[complete leading normal shifts](QUANTUM_SHIFT.md) remain verified. Their
conditional scope and positive results are not erased by the new model's
remaining problems. No globally selected vacuum or completed TOE is claimed.

The [recovered-steps receipt](RECOVERED_PHYSICAL_STEPS.md) preserves the
old/new-result sweep: 14-to-12 is an existing conditional reduction, the
spin/beat closure is verified, and the 122-order alleged failure was withdrawn.
Do not turn a remaining selection question into an absence of these results.

**Earlier outcome:** a verified defect in the original crossing instrument, a corrected
boundary-value solver, and an executable conditional gauge-and-mass calculation
using the banked exotic multiplets. This is progress toward a physical theory,
**not a completed theory of everything or a newly successful empirical prediction**.

R4 now adds an [explicit scalar action and vacuum](VACUUM_MODEL.md): a verified
classical minimum with the SM gauge algebra, actual mixed fermion masses, and
a full Hessian exposing eleven non-gauge scalar zero modes. The action and
its parameters remain chosen inputs; its low-energy spectrum is not R2's.
The same potential also admits a verified non-SM classical minimum. The
latest combined focused run has **107 passed, 3 failed**, including the eight
new R9 tests, all R8 tests, the five B1255 tests, G2/export controls, four original B1084
locks and three B1105 scope checks. Failures are the preserved original G2
exporter test and the two R7 small-step controls; their separately sealed
repairs pass. Archive and publication-gate failures remain
explicit in [FAILURES.md](FAILURES.md); no full-suite green is claimed.

- [Audit and programme history](AUDIT.md): what survives, what changed, what was checked.
- [Physical model and its exact assumptions](PHYSICAL_MODEL.md): action, spectrum,
  threshold requirement, mass mechanism, and next falsifiable task.
- [Vacuum and complete fluctuation audit](VACUUM_MODEL.md): what the potential
  really supplies, versus merely drawing a subgroup chain.
- [Original design](PREREGISTRATION.md), [post-result extension](EXTENSION_1.md),
  [preserved failures](FAILURES.md), and [artifact hashes](ARTIFACT_HASHES.txt).
- Successful numerical outputs: [crossing and thresholds](results_first_run.json),
  [common-UV-mass check](mass_results_rerun_1.json).

`mass_results_first_run.json` is an intentionally retained **incomplete failed
serialization**, not a usable result. The successful rerun has a different name.

## Reproduce

From the repository root, using the audited Python 3.12 environment:

```sh
python3.12 -m pytest tests/test_physical_bridge_gauge_running.py tests/test_physical_bridge_mass_match.py tests/test_physical_bridge_legacy_audit.py -q -p no:randomly
python3.12 -m pytest tests/test_physical_bridge_vacuum.py tests/test_physical_bridge_vacuum_orientation.py -q -p no:randomly
python3.12 -m pytest tests/test_physical_bridge_upstream.py tests/test_physical_bridge_quantum_vacuum.py tests/test_physical_bridge_quantum_derivative.py -q -p no:randomly
python3.12 -m pytest tests/test_physical_bridge_quantum_result.py -q -p no:randomly
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge_broken_vacuum.py -q -p no:randomly
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge_infrared_alignment.py -q -p no:randomly
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge*.py tests/test_b1255_generation_type.py -q -p no:randomly
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.broken_vacuum --output /tmp/oa-broken-vacuum-new-run.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.infrared_alignment --output /tmp/oa-infrared-alignment-new-run.json
python3.12 -m reports.physical_bridge_2026_09_05.vacuum --output /tmp/oa-vacuum-new-run.json
python3.12 -m reports.physical_bridge_2026_09_05.vacuum_orientation --output /tmp/oa-vacuum-orientation-new-run.json
python3.12 -m reports.physical_bridge_2026_09_05.run_audit --output /tmp/oa-crossing-new-run.json
python3.12 -m reports.physical_bridge_2026_09_05.mass_match --input /tmp/oa-crossing-new-run.json --output /tmp/oa-mass-new-run.json
python3.12 -m pytest tests/test_b1098_nonabelian_hatch.py -q -p no:randomly
OA_SLOW=1 python3.12 -m pytest tests/test_reproduce_runners_live.py -q -p no:randomly -k heavy_runner_full_live
```

The numerical runners refuse to overwrite an existing output. Choose new paths
if those names are already present. The full baseline suite is recorded separately
from these focused checks; a partial run is never reported as green.

## Continuation contract

Do not restart by assuming either that the program has no dynamics or that its
physical interpretation has been proved. Continue from INFRARED_ALIGNMENT.md:
the full leading light potential, neutral/charged minima, actual stabilizers,
all spectra and phase/anomaly control are computed, not queued. The leading
infrared orientation logarithm and charged-pair lifting are now computed too.
Next evaluate the finite hard alignment term for the existing action,
including field-dependent normal response and triplet relaxation; use
R9's logarithm as an independent control. Uncomputed matching is not
intrinsic arbitrariness once the UV action/prescription is fixed.
Retain the smaller seventeenth light fermion mass when improving matching.
The action and its inputs remain to be derived. PHYSICAL_MODEL.md's exact mass
requirement applies to its own earlier spectrum, not automatically to R4.
A new mass mechanism must emit its parameters before a fresh empirical comparison;
matching by choosing masses is an inverse fit. Preserve all seals and first runs.
