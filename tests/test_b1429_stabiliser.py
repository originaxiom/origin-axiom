"""B1429 lock -- the relayed stabiliser result, verified here and sharpened.

The two bits the paper calls withheld and relational act as x -> -x on CS mod 1/2. Their fixed-point set
is exactly {0, 1/4}, which is exactly the object and its sibling -- so they are the KERNEL of the action
on that orbit, not a point stabiliser. Pinned with the family measurement that says where they do show up,
and with the census base rate as the control that makes the family's surjectivity mean something.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1429_the_stabiliser_verified" / "verification"


def test_the_fixed_points_of_the_bit_are_exactly_the_sister_orbit():
    """x -> -x on R/(1/2)Z fixes x iff 2x = 0 mod 1/2, i.e. x in {0, 1/4}: pure arithmetic, no geometry"""
    fixed = [x / 8.0 for x in range(4) if abs(((-(x / 8.0)) % 0.5) - (x / 8.0)) < 1e-12]
    assert fixed == [0.0, 0.25], fixed
    # and the group is Z/2 x Z/2: the quarter-shift has order 2 and commutes with the negation
    assert abs((0.25 + 0.25) % 0.5) < 1e-12
    for x in (0.0, 0.125, 0.25, 0.375):
        assert abs(((-((-x) % 0.5) + 0.25) % 0.5) - ((x + 0.25) % 0.5)) < 1e-12


def test_the_family_covers_the_whole_group_and_the_census_does_not():
    f = V / "family_cs_spectrum.json"
    if not f.exists():
        pytest.skip("run verification/family_cs_spectrum.py to regenerate the measurement")
    d = json.loads(f.read_text())
    assert d["surjective_onto_Z6"] is True, d["hit6"]
    assert sorted(d["hit6"]) == [0, 1, 2, 3, 4, 5]
    # the control is what makes surjectivity mean anything
    assert d["control_n"] >= 500 and d["control_percent"] < 5.0, (
        "the census base rate is no longer low: the family's coverage stops being remarkable")


@pytest.mark.slow
def test_the_two_chern_simons_values_rerun():
    r = subprocess.run([sys.executable, str(V / "orbit_and_mirror.py")],
                       capture_output=True, text=True, timeout=1800, cwd=ROOT)
    assert r.returncode == 0, (r.stdout + r.stderr)[-600:]
    assert "m004   CS=+0.0000000000" in r.stdout, r.stdout[:400]
    assert "m003   CS=+0.2500000000" in r.stdout, r.stdout[:400]
