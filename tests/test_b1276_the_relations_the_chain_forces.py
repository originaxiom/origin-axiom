"""B1276 — every operator of the E6 cubic on the 27 labelled by the descent; all coefficients +-1 (one coupling)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1275_the_cubic_made_explicit", "B1276_the_relations_the_chain_forces"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


def test_one_coupling_on_all_45_operators(capsys):
    import relations as R
    assert R.main()
    out = capsys.readouterr().out
    assert "totals: SM Yukawas 16 (6 + 6 + 2 + 2), mu-term 2, exotic mass 3, colour-triplet operators 24; all coefficients +-1: True" in out
    for op in ("H_u Q u^c", "H_d Q d^c", "H_d L e^c", "H_u L nu^c", "H_d H_u S", "D Dbar S"):
        assert op in out
