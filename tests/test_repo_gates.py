"""Suite lock for the automated repository gates (GOVERNANCE §11).

Running these with the full suite makes every merge enforce the governance invariants.
The decadal-review counter is surfaced, not enforced (a due review must not break tests).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "gates"))

import gates  # noqa: E402


def test_all_gates_pass():
    results = gates.run_all()
    failures = {name: detail for name, (ok, detail) in results.items() if not ok}
    assert not failures, failures


def test_review_counter_readable():
    n, due = gates.review_status()
    # n is None only before the ledger exists; after seeding it must count
    assert n is None or n >= 0
    if due:
        import warnings
        warnings.warn(f"decadal repo review DUE ({n} merges since last review)")
