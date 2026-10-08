"""B1618 -- THE WEIGHTED CELL AT OMEGA: the sealed instrument unchanged; degenerate Dirac masses at every phase; U a 3-cycle."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1618_the_weighted_cell_at_omega"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 434782554: ")
    assert hashlib.sha256(open(ARC / "verification" / "weighted_at_omega.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "weighted_at_omega.json"))
    dirac = d["Q1_Q2"]["Dirac T-bar(x)T"]
    assert dirac["inner_fixed_dim"] == 3 and dirac["U_preserves_it"] and dirac["eigen_phases_24ths"] == [0, 8, 16] and dirac["every_spectrum_degenerate"]
    assert d["Q1_Q2"]["Majorana Sym2 T"]["inner_fixed_dim"] == 0
    assert d["Q3"]["U_is_a_3_cycle_on_the_lines"]
