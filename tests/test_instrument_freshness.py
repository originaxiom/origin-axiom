"""THE LOCK THAT WATCHES THE OTHER LOCKS (B1054, Review 1).

Every arc lock in this repository asserts over its arc's committed `results.json`. That file is a
cache written at banking time, and a consolidation window's whole job is to edit the files those
instruments measure. So an instrument can go red at the branch tip while its lock stays green --
not by oversight, but because the lock reads the cache rather than the instrument.

That is not hypothetical. At `5b26e51`, on a pristine worktree, `pytest` returned 46 passed / 0
failed across six arcs' locks while all six instruments re-ran RED: B1042, B1043, B1046, B1047,
B1049, B1052. Every one of them shipped a `results.json` claiming green.

This test re-runs the instruments and asserts they are green for real. It is slow by nature
(~5m20s for 26 instruments, measured) which is why it lives in the suite and not in the per-push
gates -- the suite is also exactly where the blind spot was.
"""
import importlib.util as ilu
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = ilu.spec_from_file_location("_ifresh", ROOT / "scripts/checks/instrument_freshness.py")
IF = ilu.module_from_spec(_spec)
_spec.loader.exec_module(IF)


@pytest.mark.slow
def test_every_arc_instrument_re_runs_green():
    """A cached green is not a green. Re-run them and read the real state."""
    bad = IF.sweep()
    assert bad == [], "instruments that do not re-run green:\n" + "\n".join(
        f"  {a:8} {k:12} {d}" for a, k, d in bad)


def test_the_sweeper_can_see_the_arcs_it_is_supposed_to_watch():
    """FAIL-CLOSED: a sweeper that finds nothing to sweep is the state this exists to prevent."""
    found = list(IF.instruments())
    assert len(found) >= 20, f"only {len(found)} instruments discovered"
    ids = {n for n, _, _ in found}
    for n in (1042, 1043, 1046, 1047, 1049, 1052, 1054):
        assert n in ids, f"B{n} -- one of the six that were silently red -- is not being watched"
