"""B1803 -- Witten's first model with the fillings' full symmetry group (P-409).  The committed runs: the branch links'
symmetry (the period descends to a strong inversion of both components, so the Klein four-group fixes four points); the
period's relative lift p/2 mod 2 on 75 even fillings; Witten's Z/2 x Z/2 solutions, two per twisted character."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1803_witten_first_model_with_the_fillings_full_symmetry_group" / "verification"


def test_the_period_inverts_both_branch_components():
    run = (V / "c1_run.txt").read_text(encoding="utf-8")
    assert run.count("Sym(S^3 - L) = Z/2, order 2") == 4 and "c1 exit 0" in run
    inv = "maps [[[-1, 0], [0, -1]], [[-1, 0], [0, -1]]]  det [1, 1]  extends to S^3: True"
    assert run.count(inv) == 4


def test_the_period_relative_lift_is_half_p_mod_2():
    run = (V / "c2_run.txt").read_text(encoding="utf-8")
    assert "fillings 75, mismatches 0" in run and "MISMATCH" not in run
    for p, rel, e in re.findall(r"m004\((\d+),-?\d+\): \|Hom\| 4, relative lift of P \(axis vs core\) \[(\d)\], p/2 mod 2 = (\d)", run):
        assert int(rel) == int(e) == (int(p) // 2) % 2


def test_two_witten_solutions_per_twisted_character():
    run = (V / "c3_run.txt").read_text(encoding="utf-8")
    assert run.count(": 2 full solutions:") == 3 and "total 6" in run
