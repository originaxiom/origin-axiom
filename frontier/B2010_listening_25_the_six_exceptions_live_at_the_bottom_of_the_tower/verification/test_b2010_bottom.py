"""B2010's lock: the exporter reruns; the committed GAP run holds E1, E2 and the quotient C3 x S3 at every level."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_export_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "export_perms.py")], capture_output=True, text=True, timeout=900).stdout
    (HERE / "perms.json").unlink(missing_ok=True)
    assert out == (HERE / "export_perms_run.txt").read_text()


def test_bottom():
    t = (HERE / "bottom_run.txt").read_text()
    assert t.count("E1: the six exceptions are trivial on the kernel: True (6 exceptions)") == 3
    assert t.count("E2: every irreducible non-trivial on the kernel has m = m': True") == 3
    assert t.count("the quotient has order 18, structure C3 x S3") == 3
    assert re.findall(r"of which non-trivial on it (\d+)", t) == ["0", "66", "380"]
