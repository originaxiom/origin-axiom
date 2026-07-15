"""B601 lock: the pairing law across levels + the trace law.

Failure-enforcing subprocess run of pairing_law_scan.py; asserts: the k=2
machinery gate (the banked golden pair); the spectrum conjugation-closed at
every scanned level with the naive diagonal closed ONLY at kappa = 5; and
the trace law trace(B_odd) = [5|kappa]/phi - [4|kappa] (= -LAW-O of B587)
on the 14-point grid including the discriminating kappa = 16, 20, 24.
"""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B601_pairing_law", "pairing_law_scan.py")


def test_b601_pairing_and_trace_law():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "machinery gate k=2: diagonal = banked golden pair: True" in out
    # spectrum conj-closed everywhere; diag closed only at kappa=5
    scan = [l for l in out.splitlines()
            if l.strip() and l.lstrip()[0].isdigit() and "True" in l]
    assert len(scan) == 7
    for line in scan:
        assert line.rstrip().endswith("True")          # spec conj-closed
    assert scan[0].split()[4] == "True"                # kappa=5 diag closed
    for line in scan[1:]:
        assert line.split()[4] == "False"              # all others not
    assert out.count("[True]") >= 14                   # the trace-law grid
    assert "TRACE LAW FAILED" not in out
    assert "DONE" in out
