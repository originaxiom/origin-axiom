"""B1856 -- the level-5 Weil representation facts reproduce on main's code."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_weil5_check_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "weil5_check.py")], capture_output=True, text=True, check=True, timeout=300).stdout
    assert out == (HERE / "weil5_check_run.txt").read_text(encoding="utf-8")
    assert "120 of 120 elements" in out and "0 clashes" in out and "= +-<LR>: True" in out and "(LR)^1" in out


def test_the_charge_premise_splits_by_the_sign():
    """B1862 (the advisor seat's audit, E3): rho(-I) is the parity operator, not a scalar on C^5; of the rung-invisible
    defects 338 have E = +I and 305 have E = -I. Computed here, not read from the transcript."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1856_parity_split", HERE / "parity_split.py")
    ps = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ps)
    assert ps.check_against_the_representation() < 1e-12
    Par = ps.parity_operator()
    assert Par != [[1 if x == z else 0 for z in range(5)] for x in range(5)]          # not a scalar on C^5
    assert sum(Par[x][x] for x in range(5)) == 1                                       # trace = dim even - dim odd = 3 - 2
    total, plus, minus = ps.split()
    assert (total, len(plus), len(minus)) == (42768, 338, 305)
    assert (6,) in plus and (6,) not in minus
    out = subprocess.run([sys.executable, "-B", str(HERE / "parity_split.py")], capture_output=True, text=True, check=True, timeout=300).stdout
    assert out == (HERE / "parity_split_run.txt").read_text(encoding="utf-8")         # integers only: no float is compared as text
