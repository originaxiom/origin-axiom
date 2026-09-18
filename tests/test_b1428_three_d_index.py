"""B1428 lock -- the 3D index of the object, computed here and checked against the literature.

The relay that prompted this offered the DGG 3D index as "a different index on the same objects, and it is
not trivial". Both halves are pinned: the published coefficients (so the instrument is right), and the
m003 = m004 collapse with a separating control (so what it cannot do is recorded too).
"""
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1428_the_3d_index_computed" / "verification"

# Garoufalidis-Hodgson-Hoffman-Rubinstein, Illinois J. Math. 60 (2016) 289-352, pp. 297-298
GHRS_M004 = [1, -2, -3, 2, 8, 18, 18, 14, -12, -52, -106]
GHRS_M009 = [1, -1, -1, 6, 9, 12, -5, -34, -79, -118, -118]


def _series(name, order=12):
    sys.path.insert(0, str(V))
    try:
        import step7_fixed_gluing as drv
    finally:
        sys.path.pop(0)
    return drv.manifold_index(name, order) if hasattr(drv, "manifold_index") else None


def test_the_driver_runs_and_reproduces_the_published_series():
    r = subprocess.run([sys.executable, str(V / "step7_fixed_gluing.py")],
                       capture_output=True, text=True, timeout=1800, cwd=ROOT)
    assert r.returncode == 0, (r.stdout + r.stderr)[-900:]
    out = r.stdout
    # the published head of m004's series, as printed by the driver's control table
    assert "+1 -2*q -3*q^2 +2*q^3 +8*q^4 +18*q^5" in out, "m004 no longer matches the published series"
    assert "m009" in out and "+1 -1*q -1*q^2 +6*q^3 +9*q^4 +12*q^5" in out, "m009 no longer matches GHRS 11.5"


def test_the_index_does_not_separate_the_object_from_its_sibling():
    """the finding: same series on m004 and m003, different H1 -- with m015 as the separating control"""
    r = subprocess.run([sys.executable, str(V / "step7_fixed_gluing.py")],
                       capture_output=True, text=True, timeout=1800, cwd=ROOT)
    assert r.returncode == 0
    assert "['m004', 'm003']" in r.stdout or "['m003', 'm004']" in r.stdout, (
        "m003 and m004 no longer collapse: the finding has changed")
    # vacuity: the pipeline must be able to tell manifolds apart at all
    assert "7 DISTINCT series" in r.stdout, "the index no longer separates the census sample"
    assert "-4*q" in r.stdout, "m015's distinct series (which starts 1 - 4q) is missing"


@pytest.mark.slow
def test_the_tetrahedron_index_controls_hold():
    r = subprocess.run([sys.executable, str(V / "step2_verify_tetra.py")],
                       capture_output=True, text=True, timeout=1800, cwd=ROOT)
    assert r.returncode == 0, (r.stdout + r.stderr)[-900:]
    # the script reports its controls as "failures: N" lines -- read the NUMBERS, do not pattern-match the
    # word (the first version of this assertion tripped on the word "failures" in a line reporting zero).
    import re as _re
    # take EVERY integer on any line that reports failures or disagreements. The first version matched
    # "failures of 1st identity: 0" and captured the 1 of "1st" as a failure count -- an assertion that
    # read the prose instead of the numbers, which is the mistake this whole session keeps finding.
    bad = []
    for line in r.stdout.split("\n"):
        if _re.search(r"failure|disagreement", line, _re.I):
            nums = [int(n) for n in _re.findall(r"(?<![\w.])([0-9]+)(?![\w.])", line)]
            bad += [n for n in nums if n != 0 and "pairs" not in line.lower()]
    assert not bad, "tetrahedron-index controls failed: %s" % bad
    assert "EQUAL through" in r.stdout and "True" in r.stdout, "the pentagon controls did not run"
