"""B2017's lock: the committed census (about two minutes) is read. Fails if any level gains or loses an orbit in (a) or (a'),
if the three sisters leave the cusp's leaf or change category, or if the left-out orbits change."""
import pathlib, re, ast
HERE = pathlib.Path(__file__).resolve().parent


def test_census():
    t = (HERE / "census_run.txt").read_text()
    m = re.search(r"orbits in \(a\) or \(a'\), by level: (\{.*\})", t).group(1)
    assert m == "{27: {'a': 2, \"a'\": 1}, 25: [], 5: [], 7: [], 11: [], 13: [], 49: []}"
    blk27 = t.split("mod 27:")[1].split("mod 25:")[0]
    lst = ast.literal_eval(re.search(r"category\): (\[.*?\)\])", blk27).group(1))
    assert sorted((x[2], x[1], x[3], x[4]) for x in lst) == [((3, 3, 3), 0, 3, "a"), ((3, 3, 12), 0, 3, "a"), ((3, 3, 15), 0, 0, "a'")]
    for N, norb in (("27", 118), ("25", 72), ("5", 10), ("7", 15), ("11", 26), ("13", 27), ("49", 149)):
        assert re.search(r"^mod %s: \d+ residues in %d orbits" % (N, norb), t, re.M), N
    assert t.count("left out (above 2400)") == 21
    for blk in t.split("mod ")[1:]:
        if blk.startswith(("25:", "5:", "7:", "11:", "13:", "49:")):
            cats = ast.literal_eval(re.search(r"categories: (\{[^}]*\})", blk).group(1))
            assert not any(k.split()[0] in ("a", "a'", "b") for k in cats), cats
