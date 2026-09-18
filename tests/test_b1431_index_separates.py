"""B1431 lock -- the 3D index separates the object from its sibling on the full class collection.

B1428 measured the (0,0) class and reported a collapse; the collapse is real but it is an identity on an
index-2 sublattice that contains (0,0). These assertions pin the separation, the structure theorem that
explains the collapse, and the census pairs the collection separates but (0,0) merges -- the last of which
is what shows the collection is strictly sharper rather than merely different.
"""
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1431_the_index_separates_the_sibling" / "verification"


def _run(script, timeout=2400):
    r = subprocess.run([sys.executable, str(script.name)], capture_output=True, text=True,
                       timeout=timeout, cwd=V)
    assert r.returncode == 0, (r.stdout + r.stderr)[-900:]
    return r.stdout


@pytest.mark.slow
def test_the_structure_theorem_holds_and_explains_the_collapse():
    """I_m003(g) = I_m004(Ag) with det A = 1 -- but A does not map H1 onto H1"""
    out = _run(V / "step12_proof.py")
    assert "determinant of the matrix: 1" in out, out[-500:]
    assert "169 agree, 0 disagree" in out, out[-500:]


@pytest.mark.slow
def test_the_separating_classes_are_exhibited_in_both_directions():
    """step16 is the driver that lists the witnesses; compare.py only dumps the raw class table"""
    out = _run(V / "step16_final.py")
    assert "classes of m004 absent from m003" in out, out[-700:]
    assert "classes of m003 absent from m004" in out, out[-700:]
    # both lists must be NON-EMPTY -- an empty list would mean no separation, which is the whole question
    for marker in ("classes of m004 absent from m003", "classes of m003 absent from m004"):
        tail = out.split(marker, 1)[1].lstrip("\n -")
        assert tail and not tail.startswith("---"), "%s: the list is empty" % marker
    assert "RETRIANGULATION INVARIANCE" in out.upper(), "the separating classes were not re-checked"


def test_b1428_points_at_its_correction():
    """the record's convention: a corrected arc names its correction rather than being silently rewritten"""
    f = ROOT / "frontier" / "B1428_the_3d_index_computed"
    assert (f / "ADDENDUM_2026-09-18_THE_FULL_COLLECTION_SEPARATES.md").exists()
    t = (f / "FINDINGS.md").read_text()
    assert "ADDENDUM_2026-09-18_THE_FULL_COLLECTION_SEPARATES.md" in t, (
        "B1428's own text does not point at the addendum that corrects its emphasis")
