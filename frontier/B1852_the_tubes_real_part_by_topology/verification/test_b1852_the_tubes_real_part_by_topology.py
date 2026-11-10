"""B1852 -- the fixed fibres' involution classes reproduce exactly: m004 both Re 1/2 (B1847's control), L^6RLR opposite."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_classes_reproduce():
    out = subprocess.run([sys.executable, "-B", str(HERE / "fixed_fibre_classes.py")], capture_output=True, text=True,
                         check=True, timeout=600).stdout
    assert out == (HERE / "fixed_fibre_classes_run.txt").read_text(encoding="utf-8")
    lines = out.splitlines()
    assert "both at Re tau = 1/2" in lines[0] and "m004" in lines[0]
    assert "opposite classes" in lines[1] and "L^6RLR" in lines[1]
    assert "0 + 6.15(15) i" in lines[-1]


def test_the_family_addendum_output():
    t = (HERE / "addendum_k_family_run.txt").read_text(encoding="utf-8")
    assert t.count("opposite classes") == 5 and "systole 0.18521828" in t and "the Mobius image" in t and "HOLDS" in t


def test_the_apex_real_part_exact():
    """The correction of 2026-11-10: L^6RLR's apex is sqrt(40/3) i at Re 0; Re 1/2 is L^5RLR's."""
    out = subprocess.run([sys.executable, "-B", str(HERE / "apex_real_part.py")], capture_output=True, text=True,
                         check=True, timeout=600).stdout
    assert out == (HERE / "apex_real_part_run.txt").read_text(encoding="utf-8")
    lines = out.splitlines()
    assert "40/3" in lines[0] and lines[0].rstrip().endswith("[0]")
    assert "119/12" in lines[1] and lines[1].rstrip().endswith("[1/2]")
    assert all(l.rstrip().endswith("[0]") for l in lines[2:5])
