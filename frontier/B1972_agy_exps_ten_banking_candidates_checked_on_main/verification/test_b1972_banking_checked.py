"""B1972's lock: the committed runs of main's own checks hold the facts the page states, and each would fail if a fact moved.
Fails if: m000's cover is not m004; a non-abelian quotient of order 6 or 8 appears; the 3-cusp 5-fold cover is not 8^3_4; the
least Kac deletion determinant is not a unique 20; the centralizer dimensions move; the doublet/triplet counts swap; K5 is not
the line (1, 2); or the reproduction table loses an identical output."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
T1 = (HERE / "bank1_topology_run.txt").read_text()
T2 = (HERE / "bank_math_run.txt").read_text()


def test_topology():
    assert "m000: orientable False" in T1 and "m000's 2-fold covers: 1 [(True, 'Z', True)]" in T1
    assert "non-abelian images of pi1(m004) in S_3, by order: {}" in T1
    s5 = re.search(r"in S_5, by order: \{([^}]*)\}", T1).group(1)
    assert set(int(k) for k in re.findall(r"(\d+):", s5)) == {120, 12, 10}
    assert "isometric to 8^3_4: True" in T1
    assert re.search(r"a 10-fold cover: cusps 5 \| H1 Z \+ Z \+ Z \+ Z \+ Z \| type regular", T1)


def test_kac_and_centralizers():
    dets = [int(d) for d in re.findall(r"\((\d+), \(\d, \d\), \(\d, \d\)\)", T2)]
    assert sorted(dets) == [20, 24, 30, 32, 48] and dets.count(20) == 1
    assert "dim Cent(P), Cent(J), Cent(P,J): 21 25 13" in T2 and "[P,J] = 0: True" in T2
    assert "its +1 space has dim 4 (the weak doublets" in T2 and "-P5 has +1 space of dim 6 (the colour triplets)" in T2


def test_anomaly_and_kernels():
    assert "H - V + 29T = 273 for every n16 in 0..10" in T2 and "in [0, 2]" in T2
    assert "M-invariant lines of (Z/5)^2: [(1, 2)]" in T2
    assert "cyclic order-6 subgroups of E[6]: 12 | containing (1,1) [a == b]: 1 | containing (3,3) i.e. (1/2,1/2): 4" in T2
    assert re.search(r"j\(\(2\+i\)/5\) = \(1728\.0", T2)


def test_reproductions():
    s = (HERE / "reproduce_run.txt").read_text()
    rows = [l for l in s.splitlines() if " rc=" in l]
    assert len(rows) == 16 and all("rc=0" in l for l in rows)
    assert sum("IDENTICAL" in l for l in rows) == int(re.search(r"IDENTICAL: (\d+) of 16", s).group(1))
