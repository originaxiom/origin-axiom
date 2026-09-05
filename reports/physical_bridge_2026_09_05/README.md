# Physical bridge audit — 2026-09-05

Base repository: **`f06d34054899e8c23672b836a7c534af77cbd35d`**.
Work is local on `audit/physical-bridge-2026-09-05`; no push. Upstream a8fd2460
was subsequently merged and [checked separately](UPSTREAM_AUDIT.md): its
59 focused tests passed. Original baseline totals remain pinned to f06d3405.

**Latest result:** the full [one-loop quantum calculation](QUANTUM_VACUUM.md)
stabilizes the eleven extra angular scalar modes of the conditional SM vacuum.
Independent analytic derivatives confirm the positive masses; exact polynomial
identities prove angular scale independence. This is local perturbative
stabilization, **not** a globally selected vacuum or a completed TOE.

**Earlier outcome:** a verified defect in the original crossing instrument, a corrected
boundary-value solver, and an executable conditional gauge-and-mass calculation
using the banked exotic multiplets. This is progress toward a physical theory,
**not a completed theory of everything or a newly successful empirical prediction**.

R4 now adds an [explicit scalar action and vacuum](VACUUM_MODEL.md): a verified
classical minimum with the SM gauge algebra, actual mixed fermion masses, and
a full Hessian exposing eleven non-gauge scalar zero modes. The action and
its parameters remain chosen inputs; its low-energy spectrum is not R2's.
The same potential also admits a verified non-SM classical minimum. The
current combined audit has **48 passing tests**, plus the separately run
59 upstream tests. Archive and staged publication-gate failures remain
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
physical interpretation has been proved. Continue from QUANTUM_VACUUM.md:
the leading angular lifting is now positive and independently verified. Extend
to the full shifted vacuum/global question and construct the light-Higgs
sector before redoing matching. PHYSICAL_MODEL.md's exact mass
requirement applies to its own earlier spectrum, not automatically to R4.
A new mass mechanism must emit its parameters before a fresh empirical comparison;
matching by choosing masses is an inverse fit. Preserve all seals and first runs.
