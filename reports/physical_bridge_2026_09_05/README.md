# Physical bridge audit — 2026-09-05

Base repository: **`f06d34054899e8c23672b836a7c534af77cbd35d`**.
Work is local on `audit/physical-bridge-2026-09-05`; no push. Upstream through
8f83b5c8 has been merged and independently audited: [first landing](UPSTREAM_AUDIT.md),
[second landing](UPSTREAM_SECOND_AUDIT.md). Original baseline totals remain
pinned to f06d3405; they are not a certificate for this updated branch.

**Latest physical result:** the priced [Higgs extension](HIGGS_SECTOR.md) supplies
two actual light doublets and nonzero one-family Yukawa masses at small neutral
VEVs. Its full 294-scalar quantum feedback preserves positive octet/triplet
curvatures, but the Higgs-zero background has negative Higgs masses at the
reference scale and large new singlet shifts. A controlled broken-phase
calculation is required; this is **not** a completed electroweak vacuum.

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
latest combined focused run has **74 passed, 2 failed**, including the five
new upstream tests. Both failures are the preserved R7 small-step controls;
their independently sealed polynomial controls pass. Archive and publication-gate failures remain
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
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge*.py tests/test_b1255_generation_type.py -q -p no:randomly
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
physical interpretation has been proved. Continue from HIGGS_SECTOR.md:
the light sector and its quantum feedback are now computed, not merely queued.
Derive the weak-coupling broken-phase potential, check the electromagnetic
stabilizer, retain every residual mode and test orientation selection before
redoing matching. PHYSICAL_MODEL.md's exact mass
requirement applies to its own earlier spectrum, not automatically to R4.
A new mass mechanism must emit its parameters before a fresh empirical comparison;
matching by choosing masses is an inverse fit. Preserve all seals and first runs.
