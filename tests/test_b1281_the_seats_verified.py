"""B1281 — the seats verified: the other seats' load-bearing chirality statements re-derived with this branch's code
(parity of the fixed-point counts, the Lefschetz numbers, the three lifts of the inversion to E6, the theta-odd
region-swap theorem with its failing control, m202's invariants when SnapPy is present)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1281_the_seats_verified" / "verification"))


def test_the_seats_statements_rederived(capsys):
    import seats_verified as S
    out = S.main()
    text = capsys.readouterr().out
    assert out['ok']
    assert out['fix'] == [0, 0, 4, 4, 0, 0, 0, 0] and out['L'] == [0, 0, 2, 2, 2, 2, 0, 0]
    assert out['table'][(1, -1)] == 3 and set(out['table'].values()) == {0, 1, 2, 3, 4}
    assert out['lifts']['inner2'][1:] == (38, [5, 1]) and out['lifts']['inner3'][1:] == (24, [2, 2, 2]) and out['lifts']['outer'][2] == 52
    res, control, torus = out['region']
    assert all(r == (0, 0) for r in res) and control == 1 and torus == 0
    if out['snappy'] is not None:
        assert out['snappy']['m202']['cusps'] == 2 and out['snappy']['m202']['sym_order'] == 12 and not out['snappy']['m202']['amphicheiral']
        assert out['snappy']['m004']['amphicheiral'] and out['snappy']['m004']['sym_order'] == 8
    assert "SELFTEST: PASS" in text
