"""B1789 -- the lepton factor c = 3 is not derived in B1656's frame.  On the slope-2/5 family the frame's R2 stays near 1 at
the band and -> 1 at height; R1 at the band spans about 0.36-2.95, so 9 D_frame spans about 6.7-13.2 (exact c = 3 does not imply
D = 9 there); the net-flux exclusion's arithmetic."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1789_the_lepton_factor_not_derived_in_the_frame" / "verification"


def test_the_band_spread():
    d = json.loads((V / "d_frame_band.json").read_text(encoding="utf-8"))["B1786"]
    assert d["rows"] == 7500
    r2 = d["R2_quantiles_0_1_10_50_90_99_100"]; r1 = d["R1_quantiles"]; nd = d["nine_D_quantiles"]
    assert 0.8 < r2[0] and r2[-1] < 1.2                     # R2 near 1 everywhere on the family
    assert r1[0] < 0.4 and r1[-1] > 2.5 and d["R1_above_2"] == 161
    assert nd[2] < 9 < nd[4] and nd[2] < 10.58 < nd[4]      # 9 D_frame's 10-90% range straddles 9 and 10.58


def test_r2_tends_to_one_at_height():
    lines = json.loads((V / "r_twofifths.json").read_text(encoding="utf-8"))      # b -> [[Im tau, R2, R1], ...]
    assert len(lines) == 6
    for b, rows in lines.items():
        y, r2, r1 = rows[-1]
        assert y == 8.0 and abs(r2 - 1) < 1e-4 and abs(r1 - 1) < 1e-3, b


def test_no_net_flux_keeps_one_zero_mode_per_field():
    charges = (1, -4, 2, -3, 6, 3)
    ok = [n for n in range(-12, 13) if all(abs(1 + q * n) == 1 for q in charges)]
    assert ok == [0]
