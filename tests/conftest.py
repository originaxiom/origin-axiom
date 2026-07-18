"""Suite-wide guards (Review 20, 2026-07-16).

The mpmath precision leak class (ERROR_LEDGER E-class candidate; the
known instance is documented in test_b204_metallic_wrt_period.py): any
test that changes the GLOBAL mp.mp.dps at runtime without restoring it
starves every later high-precision lock in the same session (observed:
test_e62_hearing_matrix_gates needs >= 55 dps, failed in-suite, passed
in isolation). Per-file save/restore fixtures existed in five files;
this autouse fixture kills the class in one place: every test runs with
the precision it observes at entry restored on exit, so a leak cannot
cross test boundaries.
"""
import mpmath as mp
import pytest

# The E12 COLLECTION-TIME variant (B666 cell 5, repaired suite-wide by the
# R22-4 module-level-dps sweep): pytest imports every test module before any
# test runs, so a module-level mp.mp.dps assignment leaks to every later import
# and the LAST one in sorted order becomes the global every runtime test sees.
# The autouse fixture below cannot fix that (it restores the already-leaked
# entry value). Per-file repair = save/restore around the import + a per-file
# autouse fixture pinning the runtime dps (the b204 pattern). The hook here is
# the class-wide guard: after collection finishes, the global precision is
# restored to what it was when this conftest was imported (before any test
# module), so a FUTURE module-level assignment cannot silently set the
# suite-wide runtime precision. It does not repair a leaker's own tests --
# those still need their per-file fixture (detector: the import_scan.py sweep
# in frontier/B666_leads_campaign/cell5/).
_COLLECTION_ENTRY_DPS = mp.mp.dps


def pytest_collection_finish(session):
    mp.mp.dps = _COLLECTION_ENTRY_DPS


@pytest.fixture(autouse=True)
def _restore_mpmath_precision():
    saved = mp.mp.dps
    yield
    mp.mp.dps = saved
