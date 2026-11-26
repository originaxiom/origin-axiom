"""B2016's lock: the committed classifier run is read (the export takes about twelve minutes in GAP); its tallies, the
whole's stabiliser's category and the list of the classes in (a) at mod 27 and 81. Fails if a tally moves, if the whole's
stabiliser leaves (a), or if a class in (a) has C fixing other than three points or rho trivial on H."""
import pathlib, re, ast
HERE = pathlib.Path(__file__).resolve().parent


def test_null_control():
    t = (HERE / "cosets_gap_run.txt").read_text()
    for N, ncl, tally, orders in (("27", 45, {"a": 4, "b": 10, "c": 31}, [3, 9, 12, 36]), ("81", 100, {"a": 8, "b": 28, "c": 64}, [3, 9, 12, 27, 36, 81, 108, 324])):
        blk = t.split("mod %s:" % N)[1].split("mod ")[0]
        assert "%d classes of subgroups" % ncl in blk
        assert "the whole's stabiliser class: category a, |H| = 3" in blk and "C fixes 3, rho trivial on H: False" in blk
        got = ast.literal_eval(re.search(r"categories: (\{[^}]*\})", blk).group(1))
        assert got == tally, got
        a = ast.literal_eval(re.search(r"conjugate to the whole's stabiliser\): (\[.*?\)\])", blk).group(1))
        assert sorted(x[0] for x in a) == orders and all(x[2] == 3 and x[3] is False for x in a) and sum(x[4] for x in a) == 1
    assert "the exported actions: sha256 54f6b96b0bd4f1fc52466bd5f90c4e42cb3f8c3b75ac7c08be138a463e979afa" in t


def test_overgroups_posthoc():
    t = (HERE / "overgroups_join_run.txt").read_text()
    assert "mod 27: (category, H contains a conjugate of C) -> number of classes: {('a', True): 4, ('b', False): 10, ('c', False): 27, ('c', True): 4}" in t
    assert "mod 81: (category, H contains a conjugate of C) -> number of classes: {('a', True): 8, ('b', False): 28, ('c', False): 60, ('c', True): 4}" in t
