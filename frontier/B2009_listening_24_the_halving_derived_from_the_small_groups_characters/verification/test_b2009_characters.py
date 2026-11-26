"""B2009's lock: the exporter reruns with its hash; the committed GAP run holds the six exceptions at every level (GAP needs
sage and is not rerun here)."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_export_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "export_perms.py")], capture_output=True, text=True, timeout=900).stdout
    (HERE / "perms.json").unlink(missing_ok=True)
    assert out == (HERE / "export_perms_run.txt").read_text()


def test_six_exceptions():
    t = (HERE / "characters_run.txt").read_text()
    assert re.findall(r"(\d+) irreducible characters; with m != m': (\d+)", t) == [("19", "6"), ("85", "6"), ("399", "6")]
    assert t.count("exceptions with a non-zero C-neutral subspace: 3; sum over all irreducibles of degree * (m - m') = 0; sum of (m - m') * C-neutral dimension = 3") == 3
    blocks = t.split("mod ")[1:]
    rows = [sorted(re.findall(r"degree (\d), m = (\d), m' = (\d), C-neutral dimension (\d)", b)) for b in blocks]
    assert rows[0] == rows[1] == rows[2] and len(rows[0]) == 6
