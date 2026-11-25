"""B2007's lock: the committed runs hold the layer table and the post hoc matching (GAP needs sage and is not rerun here; the
exporter reruns and its orbits' hash is checked)."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_export_reruns_with_the_same_hash():
    out = subprocess.run([sys.executable, "-B", str(HERE / "export_orbits.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "export_orbits_run.txt").read_text()
    (HERE / "orbits.json").unlink()


def test_layer_table():
    t = (HERE / "gap_layer_run.txt").read_text()
    assert re.findall(r"\|G_k\| = (\d+)", t) == ["216", "1944", "52488", "114791256"]
    steps = re.findall(r"the step's layer \(kernel to mod \d+\): order (\d+); elementary abelian: (True|False)", t)
    assert steps == [("9", "True"), ("9", "True"), ("27", "True"), ("2187", "True")]
    assert t.count("G_k's abelian invariants [2, 3]") == 4
    assert "order 4782969; abelian: False; abelian invariants [27, 81]; exponent 81; nilpotency class 4" in t


def test_halving_729_posthoc():
    p = (HERE / "halving729_posthoc_run.txt").read_text()
    m = re.search(r"half-neutral values (\d+), charged values (\d+), matched within 1e-6: (\d+) \(largest matched difference ([\d.e-]+)\)", p)
    assert m and m.group(1) == m.group(3) == "59" and float(m.group(4)) < 1e-6
