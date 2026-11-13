"""B1915's lock. It recomputes the orbits (the module writes nothing on import), checks each count, plants the orientation
read from the determinant alone, and holds the page to the run."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_hand_rows as W
PAGE = " ".join((HERE.parent / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_maps_and_the_mirror_between_the_sides():
    assert W.res["maps_found"] == 176 and W.res["maps_between_the_sides"] == 88
    assert W.res["D_is_a_map_between_the_sides"]


def test_one_bit_under_every_map_two_under_the_orientation_keeping_ones():
    assert len(W.every) == 2 and len(W.keeping) == 4
    for orb in W.every:
        assert len(orb) == 4 and {p[0] for p in orb} == {"+", "-"}
    for orb in W.keeping:                     # the side is absorbed: each class holds one placement on each side
        assert len(orb) == 2 and {p[0] for p in orb} == {"+", "-"} and len({p[1] for p in orb}) == 1


def test_the_plant_changes_the_count():
    assert len(W.planted) == 1 != len(W.every)


def test_the_page_is_the_run():
    run = (HERE / "the_hand_rows_run.txt").read_text(encoding="utf-8")
    assert "maps found (entries <= 9): 176, of them between the two sides: 88; D among them: True" in run
    for s in ("176", "88", "two orbits", "four", "one forward and one backward"):
        assert s in PAGE, s
