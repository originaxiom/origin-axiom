"""B2012's lock: the committed runs of main's checks (blind_checks: about 4 minutes; mixed_levels and mixed_posthoc: about
2 minutes) are read; mixed_levels.py's mod-54 part is cheap, so the mod-54 line is rerun here. Each check fails if a
verdict line flips, if an orbit size or an unpaired count moves, or if any of the six pairing-law lines is lost."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_pairing_law():
    t = (HERE / "blind_checks_run.txt").read_text()
    lines = [l for l in t.splitlines() if l.startswith("N1 ")]
    assert len(lines) == 6 and all("pointwise: True" in l for l in lines)
    assert sum(l.endswith("over Z: True  [%s s]" % l.rsplit("[", 1)[1][:-3]) for l in lines) == 5
    assert "modulo three 62-bit primes: [True, True, True]" in lines[5]
    pts = [int(re.search(r": (\d+) points", l).group(1)) for l in lines]
    assert pts == [64, 60, 112, 72, 648, 2880]


def test_other_checks():
    t = (HERE / "blind_checks_run.txt").read_text()
    assert "has 6 points" in t and "their k: {t**2}" in t
    assert "every prime 3 <= p <= 71: True (failures [])" in t
    assert "mod 4: [0, 1, 2]" in t and "mod 9: [0, 1, 2, 4, 5, 7, 8]" in t
    rows = re.findall(r"\((-?\d+), (True|False), (\d+)\)", t.split("N6b:")[1].splitlines()[0])
    assert len(rows) == 15 and all(r[1] == "True" and r[2] == "0" for r in rows)
    assert t.count("[(32, [1152, 1152]), (64, [4608, 4608]), (128, [18432, 18432])]") == 3
    assert t.count("40 distinct points; equals the orbit of (3,3,3) mod 5 (40 points): True") == 2


def test_mixed_levels():
    t = (HERE / "mixed_levels_run.txt").read_text()
    assert "mod 189 = 27 * 7, orbit of (3,3,3): 2016 points" in t and "exactly: False; gcd degree 663 of the charged 671; charged unpaired: degree 8" in t
    assert "mod 54 = 27 * 2, orbit of (3,3,3): 288 points" in t and "exactly: True; gcd degree 95 of the charged 95" in t
    s = (HERE / "mixed_posthoc_run.txt").read_text()
    assert s.count("exactly: True") == 2 and "orbit of (3,3,3): 2592 points" in s


def test_mod54_rerun():
    src = (HERE / "mixed_levels.py").read_text().replace("for N, q in ((54, 2), (189, 7)):", "for N, q in ((54, 2),):")
    out = subprocess.run([sys.executable, "-B", "-c", src.replace("__file__", repr(str(HERE / "mixed_levels.py")))], capture_output=True, text=True, timeout=300).stdout
    assert "exactly: True; gcd degree 95 of the charged 95" in out
