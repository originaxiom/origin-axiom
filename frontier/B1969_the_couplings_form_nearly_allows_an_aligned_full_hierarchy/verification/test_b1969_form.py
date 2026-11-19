"""B1969's lock: the determinant identity holds exactly (re-run); the kept feasibility run holds no counterexample and its
least distance is 0.346 at reality 0.003; the scripts are the ones hashed before their runs."""
import sys, pathlib, re, hashlib, subprocess
HERE = pathlib.Path(__file__).resolve().parent


def test_the_determinant_identity():
    out = subprocess.run([sys.executable, str(HERE / "determinant.py")], capture_output=True, text=True, cwd=HERE).stdout
    assert out.strip() == "det Y - (h.h)(w^2 + u.u)(u.h) = 0"


def test_the_feasibility_run():
    t = (HERE / "feasibility_run.txt").read_text()
    best = [float(v) for v in re.findall(r"best ([0-9.]+);", t)]
    assert len(best) == 8 and min(best) > 0.3 and "COUNTEREXAMPLE" not in t
    assert "r 0.003: best 0.346" in t


def test_the_scripts_are_the_ones_hashed():
    md = (HERE / "EXPECTATIONS_HASHED.md").read_text()
    for name in ("full_hierarchy.py", "feasibility.py"):
        h = re.search(r"\| `%s` \| `([0-9a-f]{64})` \|" % re.escape(name), md).group(1)
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == h, name
