# Physical bridge audit — 2026-09-05

Base repository: **`f06d34054899e8c23672b836a7c534af77cbd35d`**.
Work is local on `audit/physical-bridge-2026-09-05`; no upstream merge or push.

**Outcome:** a verified defect in the original crossing instrument, a corrected
boundary-value solver, and an executable conditional gauge-and-mass calculation
using the banked exotic multiplets. This is progress toward a physical theory,
**not a completed theory of everything or a newly successful empirical prediction**.

- [Audit and programme history](AUDIT.md): what survives, what changed, what was checked.
- [Physical model and its exact assumptions](PHYSICAL_MODEL.md): action, spectrum,
  threshold requirement, mass mechanism, and next falsifiable task.
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
physical interpretation has been proved. Start with the exact mass requirement
in PHYSICAL_MODEL.md and its list of existing sources. A new mass mechanism must
emit its parameters before a fresh empirical comparison; matching the requirement
by choosing masses is an inverse fit. Preserve the original B915 seal and results.
