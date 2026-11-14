"""A lock compares a number as a number (Review 80, 2026-11-12; main's word in its third folder for the builder, section 7).

Four locks compared, as text, a float or a signed zero that a process printed, and failed on a machine that had not made
the kept transcript.  The comparison they now make is `scripts/checks/printed_numbers.py`; these tests hold what it calls
the same and what it does not."""
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _pn():
    spec = importlib.util.spec_from_file_location("printed_numbers_under_test", ROOT / "scripts" / "checks" / "printed_numbers.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_four_lines_that_failed_on_another_machine_are_the_same():
    """each pair is the line a lock kept and the line this machine printed, as the failing locks showed them"""
    pn = _pn()
    for kept, got in (
            ("the commutator has entries of size at most 8.4e-16 of the product", "the commutator has entries of size at most 6.1e-16 of the product"),
            ("w equals the product up to sign 8.5e-15; control", "w equals the product up to sign 2.5e-14; control"),
            ("S_T^2 = +0+1i times 1; S_T^4 = -1+0i times 1; S_T^8 = +1-0i times 1", "S_T^2 = -0+1i times 1; S_T^4 = -1-0i times 1; S_T^8 = +1+0i times 1"),
            ("kappa(a,c) = -2.00000000+0.00000000j", "kappa(a,c) = -2.00000000-0.00000000j")):
        assert kept != got and pn.same(got, kept), pn.differences(got, kept)


def test_what_is_not_the_same():
    pn = _pn()
    for kept, got, what in (
            ("200 random 3x3 matrices: 200 commute", "200 random 3x3 matrices: 199 commute", "a count"),
            ("a group of order 96; its scalars: 4", "a group of order 97; its scalars: 4", "an order"),
            ("S_T^2 = +0+1i times 1", "S_T^2 = +0-1i times 1", "the sign of a number that is not zero"),
            ("S_T^2 = +0+1i times 1", "S_T^2 = +1+0i times 1", "which part is zero"),
            ("kappa(a,c) = -2.00000000+0.00000000j", "kappa(a,c) = +2.00000000+0.00000000j", "the sign of the real part"),
            ("kappa(a,c) = -2.00000000+0.00000000j", "kappa(a,c) = -2.00000100+0.00000000j", "the seventh digit"),
            ("up to sign 8.5e-15; control", "up to sign 8.5e-05; control", "a residual that is no residual"),
            ("up to sign 8.5e-15; control", "up to sine 8.5e-15; control", "a word"),
            ("the ratio is 1.204", "the ratio is 1.257492", "a ratio"),
            ("orbits: [((0, 0),), ((0, 1), (1, 0), (1, 1))]", "orbits: [((0, 0),), ((0, 1), (1, 1), (1, 0))]", "an order of pairs"),
            ("three numbers: 1 2 3", "three numbers: 1 2", "a number that is missing"),
            ("equivalent to T at m = [15]", "equivalent to T at m = [15.5]", "a whole number that is not one")):
        assert not pn.same(got, kept), what
        assert pn.differences(got, kept), what


def test_what_it_reads_as_a_number_and_what_it_leaves_as_text():
    pn = _pn()
    numbers = lambda t: [v for k, v in pn.parts(t) if k == "number"]
    assert numbers("at most 8.4e-16 of 200 in 3x3") == [8.4e-16, 200.0]           # "3x3" is a word
    assert numbers("+1-0i and 2.5j and v1.66 and B1849 and c66c8ccae") == [1.0, 0.0, 2.5]      # a version, an arc's number and a commit are words
    assert numbers("S_T^2 = -0+1i") == [2.0, 0.0, 1.0]
    assert pn.parts("a -0 b")[0] == ("text", "a ") and pn.parts("a -1 b")[0] == ("text", "a -") and pn.parts("a -3e-17 b")[0] == ("text", "a ")
    assert pn.same("x = -0.0", "x = 0.0") and pn.same("x = -0.0", "x = +0.0")       # a zero carries no sign
    assert pn.same("x = 1e-300", "x = -1e-12") and pn.same("the residual is -3.1e-17", "the residual is 2e-17")
    assert not pn.same("x = -1e-3", "x = 1e-3") and not pn.same("x = -2", "x = 2")  # the sign of a number that is not small is compared
    assert pn.SMALL == 1e-9 and pn.CLOSE == 1e-9
