"""B1954's lock: the self-contained checks live, and the stored run for the two that need the remote branches and SnapPy."""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import codex_checks as C
RUN = (HERE / "codex_checks_run.txt").read_text()


def test_the_stored_run():
    assert "36 of 36 found at their cited lines" in RUN and "XA-01 to XA-15 (15)" in RUN and "MISS" not in RUN
    assert "homology Z/3 + Z/15 + Z" in RUN and "= 45" in RUN


def test_the_written_weyl_element_has_order_four():
    assert C.order([4, 3, 5, 0, 1, 2, 6, 7]) == 4
    assert C.order([3, 4, 5, 0, 1, 2, 6, 7]) == 2            # the swap of coordinates 1-3 with 4-6 is an involution


def test_the_central_scalar():
    assert C.central_scalar(3) == [-1] and C.central_scalar(5) == [1]


def test_e8s_charges_under_q():
    ch = C.e8_charges()
    assert sum(v[0] for v in ch.values()) == 240
    assert {k: v[1] for k, v in ch.items() if v[1]} == {"-1": 16, "0": 40, "1": 16}        # the colour singlets are E6's 72 roots: 40 + 16 + 16
    assert set(ch) == {"-4/3", "-1", "-2/3", "-1/3", "0", "1/3", "2/3", "1", "4/3"}
