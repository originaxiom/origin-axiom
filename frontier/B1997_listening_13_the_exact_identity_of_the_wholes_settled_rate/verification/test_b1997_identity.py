"""B1997's lock: the exact factor and the closed form rerun and hold."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_identity_reruns():
    for name in ("identify", "closed_form_posthoc"):
        out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=900).stdout
        t = (HERE / (name + "_run.txt")).read_text()
        assert [l.split("  [")[0] for l in out.splitlines()] == [l.split("  [")[0] for l in t.splitlines()]
    t = (HERE / "identify_run.txt").read_text()
    assert "[64, 0, -48, 0, 12, 0, -21, 0, 3, 0, -3, 0, 1]" in t and "irreducible: True" in t
    c = (HERE / "closed_form_posthoc_run.txt").read_text()
    assert "5184 = 72^2: True" in c and "1.91529816473407715555461825615" in c and "-8*(y**3 - 3*y + 1)" in c
