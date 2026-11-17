"""B1951's lock: the Weil centre's dictionary, from weil_centre.py's own printed lines (the script is run here)."""
import re, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = subprocess.run([sys.executable, "-B", str(HERE / "weil_centre.py")], capture_output=True, text=True, timeout=300).stdout


def test_the_group_the_parity_and_the_commutant():
    assert "has 120 elements" in OUT and "eigenvalues [-1, -1, 1, 1, 1]" in OUT
    assert "D2: the commutant of rho has dimension 2 (I and P)" in OUT
    assert "values [-2, -2, -2, 3, 3]" in OUT and "trace 0" in OUT


def test_one_generation_exactly():
    rows = set(re.findall(r"D5: Lambda\^(\d): 6Y = ([+-]\d), (\d) states .*: (\w+)", OUT))
    assert rows == {("0", "+0", "1", "singlet"), ("2", "-4", "3", "u"), ("2", "+1", "6", "Q"), ("2", "+6", "1", "e"), ("4", "-3", "2", "L"), ("4", "+2", "3", "d")}
    assert "D6: 16 states; sum 6Y = 0; sum (6Y)^3 = 0" in OUT and "D7: Lambda^1: 6Y = [-2, 3]" in OUT


def test_the_plant_and_the_rival_primes():
    assert "dimensions [1, 2, 2], not 3 + 2" in OUT                      # rho(T)'s split is another split
    splits = dict(re.findall(r"CONTROL p = +(\d+): .*; split (\d+ \+ \d+);", OUT))
    assert splits == {"3": "2 + 1", "5": "3 + 2", "7": "4 + 3", "11": "6 + 5", "13": "7 + 6"}
    assert OUT.count("commutant dimension 2") == 5
