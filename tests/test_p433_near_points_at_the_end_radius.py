"""P-433 -- the near-point exponents at the canonical end radius, by the record's four-channel machinery (B1691's S248
correction): near omega the k = -1/2 mod 6 row becomes (eps, eps^3); B1806's f2 = 0 rows give a flat nonzero m2/m3 at i."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
F = next((ROOT / "frontier").glob("B1691_*")) / "verification" / "correction_s248" / "near_points_finite_L_main.json"


def test_omega_row_at_the_end_radius():
    r = json.loads(F.read_text(encoding="utf-8"))
    for k in ("omega 23/2", "omega 11/2"):
        for L in ("L=0.65", "L=2.5"):
            assert abs(r[k][L]["m2 slopes"][-1] - 1.0) < 0.02 and abs(r[k][L]["m1 slopes"][-1] - 3.0) < 0.02
    assert abs(r["omega 15/2"]["L=2.5"]["m1 slopes"][-1] - 2.0) < 0.02


def test_b1806_rows_at_the_end_radius():
    r = json.loads(F.read_text(encoding="utf-8"))
    for k in ("i 15/2, f2 = 0", "i 23/2, f2 = 0"):
        assert abs(r[k]["L=2.5"]["m2 slopes"][-1]) < 0.01 and float(r[k]["L=2.5"]["m2/m3"][-1]) > 0.02
        assert abs(r[k]["L=2.5"]["m1 slopes"][-1] - 2.0) < 0.02
