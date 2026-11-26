"""B2014's lock: walks.py's S1 to S3 (seconds) are rerun from its source up to the S5 block and must reproduce the committed
lines with the timings stripped; S5 (about eight minutes), the GAP runs (S4, S6) are read from their committed outputs. Each
check fails if a commutator gains an entry, a sector law moves, the sister census or the halving on (3,3,15) changes, an
exceptional value moves off 6, -6, 0, or a fixed-point mismatch appears."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
strip = lambda t: [re.sub(r"\s+\[\d+ s\]$", "", l) for l in t.splitlines()]


def test_s1_to_s3_rerun():
    src = (HERE / "walks.py").read_text().split("# S5")[0]
    out = subprocess.run([sys.executable, "-B", "-c", src.replace("__file__", repr(str(HERE / "walks.py")))], capture_output=True, text=True, timeout=600).stdout
    got = strip(out); want = strip((HERE / "walks_run.txt").read_text())[:len(got)]
    assert got == want and len(got) == 20, (len(got), got[:3])
    assert sum("[W+, W-] has 0 non-zero entries; C W+ C^-1 - W+ has 0; W+ + W- equals the six-move sum: True; W- = W+ transposed: True" in l for l in got) == 4
    s2 = [l for l in got if l.startswith("S2")]
    for l in s2:
        a, b = [float(x) for x in re.findall(r"H\| = ([\d.e+-]+)", l)]
        q = int(re.search(r"q = (\d)", l).group(1)); plus = "W+" in l
        if q == 0:
            assert a < 1e-12 and b < 1e-12
        else:
            assert (b < 1e-12 and a > 0.5) if plus else (a < 1e-12 and b > 0.5), l
    assert "orbits (size, least point): [(72, (3, 3, 15)), (72, (3, 3, 12)), (72, (3, 3, 3)), (12, (0, 9, 9)), (8, (9, 9, 9)), (6, (0, 0, 9)), (1, (0, 0, 0))]" in out
    assert "C fixes 0; neutral dimension 24, charged 24; p_neutral(2x)/2^d == S(x) exactly: True; x S_(3,3,15)(x) == (x^2 - 9) S_(3,3,3)(x): True" in out


def test_s5_fixed_points():
    t = (HERE / "walks_run.txt").read_text()
    m = re.search(r"mismatches with mod 27\): (\{.*\})", t).group(1)
    d = eval(m)
    assert set(d) == {4, 5, 6, 7, 8} and all(v[1] == 0 for v in d.values()) and all(d[k][0] == 1200 for k in (4, 5, 6, 7)) and d[8][0] == 200


def test_s4_values():
    t = (HERE / "reps_gap_run.txt").read_text()
    assert "irreducible representations: 19" in t
    assert "count with m != m': 6; of them with a C-neutral line: 3; their neutral values: ['-6', '0', '6']" in t
    assert "isomorphic to Sym(4): True; sign of C's image 1, of sigma's image -1" in t


def test_s6_order():
    t = (HERE / "order_gap_run.txt").read_text()
    assert "mod 2187: 472392 points; |G7| = 251048476872 = 2^3 * 3^22; equals 24 * 3^21: True" in t
