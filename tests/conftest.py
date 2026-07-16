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


@pytest.fixture(autouse=True)
def _restore_mpmath_precision():
    saved = mp.mp.dps
    yield
    mp.mp.dps = saved
