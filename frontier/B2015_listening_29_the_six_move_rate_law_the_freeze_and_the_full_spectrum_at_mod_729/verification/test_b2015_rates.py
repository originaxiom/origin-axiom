"""B2015's lock: the committed runs are read (rate_law about nine minutes; spectrum729 about two hours). Fails if a level's
value moves off 2 sqrt(5 + 4 cos(pi/M)) by more than 1e-12, a factor stops dividing, the new fibre's top moves or reaches
5.919, or a single charged eigenvalue at mod 729 goes unmatched."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def test_rate_law():
    t = (HERE / "rate_law_run.txt").read_text()
    diffs = [float(x) for x in re.findall(r"difference ([\d.e+-]+)", t)]
    assert len(diffs) == 5 and max(diffs) < 1e-12
    assert t.count("divides charpoly(W) over Z with multiplicity") == 4 and "modulo three 62-bit primes: [True, True, True]" in t
    m = re.search(r"the new fibre's largest eigenvalue ([\d.]+)", t); top = float(m.group(1))
    assert abs(top - 5.672086410291) < 1e-9 and top < 5.9190440049
    assert "its multiplicity on the whole orbit (to 1e-8): 2, on the new fibre: 0" in t


def test_full_spectrum_729():
    t = (HERE / "spectrum729_run.txt").read_text()
    m = re.search(r"matched one to one: (\d+) against (\d+); largest difference ([\d.e+-]+); pairs within 1e-7: (\d+) of (\d+)", t)
    assert m and m.group(1) == m.group(2) == m.group(4) == m.group(5) == "17495" and float(m.group(3)) < 1e-10
