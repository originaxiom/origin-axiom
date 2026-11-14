"""B1936's lock: the frame's level-5 charges put every matter field at an even exterior degree and the Higgs at an odd
one (conjugates at 5 - k); under the parity premise the Higgs reading is (up S~, down S, leptons S) for both signs of
the hypercharge convention; planted faults (a wrong charge; the opposite parity rule) fail. It writes nothing."""
import subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def run(name):
    return subprocess.run([sys.executable, "-B", str(HERE / name)], capture_output=True, text=True).stdout


def test_the_degrees_and_the_kept_runs():
    out = run("degrees.py"); assert out == (HERE / "degrees_run.txt").read_text()
    assert "expectation met for every field and its conjugate: True" in out
    out2 = run("higgs_by_parity.py"); assert out2 == (HERE / "higgs_by_parity_run.txt").read_text()
    assert out2.count("{'up': 'S~', 'down': 'S', 'lep': 'S'}") == 2


def test_planted_faults_fail():
    src = (HERE / "higgs_by_parity.py").read_text()
    wrong_rule = src.replace('"S" if kh % 2 == mp else "S~"', '"S~" if kh % 2 == mp else "S"')
    out = subprocess.run([sys.executable, "-B", "-c", wrong_rule], capture_output=True, text=True).stdout
    assert "{'up': 'S', 'down': 'S~', 'lep': 'S~'}" in out              # the opposite rule gives the other world
    wrong_charge = src.replace('"L": -3', '"L": -2')
    r = subprocess.run([sys.executable, "-B", "-c", wrong_charge], capture_output=True, text=True)
    assert r.returncode != 0 and "not in one parity class" in r.stderr  # a wrong charge breaks matter's parity class
