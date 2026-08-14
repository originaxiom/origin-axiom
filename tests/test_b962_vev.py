"""B962 locks — the VEV scouting result and the three things it moves."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B962_vev_scout"


def test_the_missing_VEV_is_universal_not_our_defect():
    assert contains(CELL / "FINDINGS.md",
                    "the vev direction is always an input",
                    "nobody's object supplies one",
                    "the same gap every gut has")


def test_the_route_provably_stops_one_step_short():
    """27 VEVs cannot break SU(5) -> SM: no 24 in the branching."""
    assert contains(CELL / "FINDINGS.md",
                    "27 vevs can never break su(5)",
                    "there is no 24",
                    "stops one step short")


def test_B955_is_amended_not_quietly_kept():
    assert contains(CELL / "FINDINGS.md", "must be amended")


def test_the_F4_obstruction_is_the_generic_VEV():
    assert contains(CELL / "FINDINGS.md",
                    "the generic vev's stabilizer is f",
                    "measure zero",
                    "two vevs are forced")


def test_no_canonical_choice_and_the_arithmetic_exception():
    assert contains(CELL / "FINDINGS.md",
                    "transitive on triples of orthogonal primitive idempotents",
                    "exists only if the space is a point",
                    "cubic étale algebras",
                    "l138")


def test_the_certified_and_uncertified_nulls_are_distinguished():
    assert contains(CELL / "FINDINGS.md",
                    "certified null", "all 39 citers read individually",
                    "not certified", "mathscinet unreachable")


def test_the_do_not_cite_list_is_recorded():
    assert contains(CELL / "FINDINGS.md", "do not cite", "buccella")
