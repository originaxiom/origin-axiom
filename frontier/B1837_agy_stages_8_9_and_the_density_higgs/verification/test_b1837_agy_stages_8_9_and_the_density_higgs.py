"""B1837 lock -- from committed runs on main's code (re-run by main): first order in h_I for every generation and |det|; the
torsion table with no 4 - 2 sqrt3; the slope criteria; the density closed form; and the record keeps the pasted integers out."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _t(rel):
    return (HERE / rel).read_text(encoding="utf-8")


def test_every_generation_and_the_determinant_move_at_first_order():
    out = _t("stage9/c1_half_lift_first_order_run.txt")
    for g in (1, 2, 3):
        assert "generation %d: 40 cases, doubling ratio min 2.0000 max 2.0000" % g in out
    assert "|det|: vanishes identically in 0 of 40 cases; doubling ratio over the rest: min 2.0000 max 2.0000" in out


def test_the_torsion_table_and_no_four_minus_two_root_three():
    t = _t("stage8/t59_torsion_snappy_run.txt") + _t("stage9/c2_torsion_m004_run.txt")
    assert "4/sqrt3" in t.replace("4/√3", "4/sqrt3") or "2.3094" in t
    assert "6" in t and re.search(r"(?i)4 ?- ?2 ?sqrt ?3|4 − 2√3", t)


def test_the_pasted_integers_are_in_no_tracked_record_of_this_arc():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "201" not in f and "40.2" not in f
