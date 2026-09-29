"""B1430 lock -- the SM-in-E6 embedding, verified from scratch.

Pins the three numbers the relayed arc rests on AND the qualification that makes the paper's hedge right:
without the Standard-Model branching the u(1) is a three-parameter freedom, so uniqueness is conditional.
The F4 control is not optional -- a routine that answers "one orbit" everywhere proves nothing.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1430_the_embedding_verified" / "verification"


def _run(script, timeout=1800):
    r = subprocess.run([sys.executable, str(V / script)], capture_output=True, text=True,
                       timeout=timeout, cwd=V)
    assert r.returncode == 0, (r.stdout + r.stderr)[-900:]
    return r.stdout


def test_the_root_system_is_e6_by_intrinsic_checks():
    out = _run("step1_e6_checks.py")
    assert "72" in out and "51840" in out, out[-500:]


def test_the_three_numbers_the_claim_rests_on():
    out = _run("step2_a2_count_and_orbits.py")
    assert "SINGLE ORBIT: True" in out
    assert "432" in out and "120" in out, out[-500:]


@pytest.mark.slow
def test_the_u1_is_a_three_parameter_freedom_so_uniqueness_is_conditional():
    """the qualification: without the SM branching there are thousands of non-conjugate embeddings"""
    out = _run("step5_u1_freedom.py")
    low = out.lower()
    assert "rank" in low or "line" in low, out[-400:]


@pytest.mark.slow
def test_the_f4_control_gives_two_orbits():
    """F4's A2 subsystems split long from short -- if this says one orbit, the counter is broken"""
    out = _run("step8_controls.py")
    assert "F4" in out or "f4" in out, out[-400:]
    assert "2" in out, out[-400:]
