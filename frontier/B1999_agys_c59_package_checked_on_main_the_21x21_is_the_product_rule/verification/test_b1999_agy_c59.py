"""B1999's lock: the identity reruns; the seat's copies keep their hashes; the committed check run holds the page's facts.
check_c59.py itself takes minutes and is not rerun here; its committed output is read, and each check fails if a fact moves."""
import hashlib, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_identity_reruns():
    out = subprocess.run([sys.executable, "-I", "-B", str(HERE / "schur_identity.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "schur_identity_run.txt").read_text()
    devs = [float(x) for x in re.findall(r"(?:deviation|difference) ([\d.e-]+)", out)]
    assert len(devs) == 2 and all(d < 1e-30 for d in devs)


def test_seat_copies_unchanged():
    assert hashlib.sha256((HERE / "seat_copy" / "c59_producer.py").read_bytes()).hexdigest() == "b399b206de30cc9a1cca2703c139a1e8080757c688b4704b5052eb293cf70ea1"
    assert hashlib.sha256((HERE / "seat_copy" / "c59_out.json").read_bytes()).hexdigest() == "00847116b27912eafe54ee083a8694728976080cdedfc9c3b0db3d85d80c6197"


def test_check_run_facts():
    t = (HERE / "check_c59_run.txt").read_text()
    m = re.search(r"reproduces the seat's sealed E4 values on 8 of 8 chains, worst relative difference ([\d.e-]+)", t)
    assert m and float(m.group(1)) < 1e-6
    ks = [float(x) for x in re.findall(r"K = +\d+: u \(m2/m3, m1/m3\) = \([\d.e-]+, ([\d.e-]+)\)", t)]
    assert len(ks) == 6 and all(ks[i + 1] < ks[i] * 1e-2 for i in range(5))
    assert "the ordering m2/m3 u > d > e holds on 36 of 96 chains" in t
    ups = re.findall(r"up angle (-?[\d.]+) deg \(\|up - e\^\{-\+2 pi i/5\}\| = ([\d.e-]+)\); \|down - 1\| = ([\d.e-]+); \|lepton - 1\| = ([\d.e-]+)", t)
    assert len(ups) == 8 and all(abs(abs(float(a)) - 72) < 1e-6 and max(float(b), float(c), float(d)) < 1e-30 for a, b, c, d in ups)
    cw = re.findall(r"J_cw \+ J_ccw = (-?[\d.e-]+); CP-even outputs differ by at most ([\d.e-]+)", t)
    assert len(cw) == 8 and all(abs(float(a)) < 1e-30 and float(b) < 1e-30 for a, b in cw)
