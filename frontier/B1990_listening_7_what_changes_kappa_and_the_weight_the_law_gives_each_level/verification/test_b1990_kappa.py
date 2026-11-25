"""B1990's lock: the exact run reruns and holds K1 to K4."""
import pathlib, subprocess, sys, re
HERE = pathlib.Path(__file__).resolve().parent


def test_kappa_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "kappa.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "kappa_run.txt").read_text()
    assert "'L': True, 'R': True" in out and "False" not in out.split("K2")[0]
    assert "K3: tr(a b a^-1 b^-1) = x^2 + y^2 + z^2 - xyz - 2 on SL(2): True" in out
    for line in out.splitlines():
        m = re.match(r"K4: p = +(\d+): cusp \(kappa=-2\) +(\d+) .*\[p\^2 \+ 3\(-1/p\)p \+ 1 = (\d+)\]; nothing \(kappa=2\) +(\d+)", line)
        if m:
            p, c, f, n = map(int, m.groups())
            assert c == f and n == p * p + 1, line
