"""B2011's lock: symbolic.py is rerun and must reproduce its committed run; the slower runs (c60_levels, honeycomb, ingredients,
halving243_exact: minutes to an hour) are read from their committed outputs. Each check fails if a verdict line flips, if
the unpaired count at mod 135 moves off 10, if the honeycomb law stops dividing W+'s polynomial at any level, or if any
rung of the ingredient table from mod 9 to mod 6561 loses a check."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_symbolic_rerun():
    out = subprocess.run([sys.executable, "-B", str(HERE / "symbolic.py")], capture_output=True, text=True, timeout=600).stdout
    assert out == (HERE / "symbolic_run.txt").read_text()
    assert "off-diagonal all zero: True" in out and "equals (4s + 6)/(s + 6) with s = x + y + z: True" in out
    assert "node (3, 3, 3): ratio 14/5" in out and "limit as s -> infinity: 4" in out
    lines = [l for l in out.splitlines() if l.startswith("B4")]
    assert len(lines) == 2 and "lowest degree 3" in lines[0] and lines[0].endswith("True; its negative: False")


def test_c60_levels():
    t = (HERE / "c60_levels_run.txt").read_text()
    assert "mod 135, orbit of (3,3,3): 2880 points; C fixes 3; neutral dimension 962, charged (q = 1) dimension 959" in t
    assert "degree of gcd(p_neutral(2x)/2^d, S): 949 of the charged 959" in t and "charged left unpaired: degree 10;" in t
    assert "onto the mod-27 orbit: True" in t and "A1: the charged unpaired part equals" in t and t.count(": True") >= 4
    assert re.search(r"A1: .*: True", t) and re.search(r"A2: gcd == x\^2 \(x - 2\)\(x \+ 2\): True", t)
    orders = dict(re.findall(r"A6: mod (\d+): \[C\^-1, sigma\]\^3 has order (\d+)", t))
    assert orders == {"27": "1", "81": "1", "243": "3"}
    assert re.search(r"A7: P6 divides p_neutral at mod 81: True \(multiplicity 2\).*difference 0\.0", t)


def test_honeycomb():
    t = (HERE / "honeycomb_run.txt").read_text()
    diffs = [float(d) for d in re.findall(r"difference ([\d.e+-]+)", t)]
    assert len(diffs) == 5 and max(diffs) < 1e-12
    assert t.count("over Z: f divides W+'s characteristic polynomial with multiplicity") == 4
    assert all(int(m) >= 1 for m in re.findall(r"with multiplicity (\d+)", t))
    assert "f divides W+'s characteristic polynomial: [True, True, True]" in t
    assert "isomorphism with L and R: 3 of 648" in t and "L^2 and R^2 commute: True" in t
    assert "orders of L^2, R^2: 18, 18; the group they generate has order 324" in t


def test_ingredients():
    t = (HERE / "ingredients_run.txt").read_text()
    for k in range(2, 9):
        m = re.search(r"A5 k = %d \(mod \d+\): \|S_k\| = (\d+); 8 \* 3\^\(2k-4\) = (\d+);.*components of L and R: (\d+); contains \(3,3,3\): True" % k, t)
        assert m and m.group(1) == m.group(2) and m.group(3) == "1", k
    assert t.count("every move exchanges them: True; main's six moves = the seat's six: True") == 7
    assert len(re.findall(r"C fixes 3, of which in O\+: 3", t)) == 6 and "C fixes 2, of which in O+: 1" in t
    assert t.count("gamma + 1 under C on O-: True; under s2s3, s3s1, s1s2: True, True, True; around each point of O+ the gamma values are 0,0,1,1,2,2: True") == 6
    assert t.count("J_k a bijection of O-: True; commutes with all six s_i s_j: True; J_k C = tau C J_k: True") == 5


def test_halving_243_exact():
    t = (HERE / "halving243_exact_run.txt").read_text()
    assert "mod 243, orbit of (3,3,3): 5832 points; C fixes 3; neutral dimension 1946, charged (q = 1) dimension 1943" in t
    assert "p_neutral(2x) / 2^d == (x^2 - 9) x S(x) exactly over Z: True" in t
