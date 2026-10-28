"""B1793 -- the curvature route for the lepton factor.  The committed runs: the weighted routine equals the instrument at eps 0;
on (2/5, 1/5) R2 = R1 = 1 for every profile; the realisable-weight scan keeps R2 near 1; no cell reaches R2 and R1 both >= 2.5."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1793_the_curvature_route_for_the_lepton_factor" / "verification"


def test_the_control_and_the_exact_identity():
    run = (V / "curvature_run.txt").read_text(encoding="utf-8")
    for m in re.finditer(r"instrument R2 ([0-9.]+) R1 ([0-9.]+) \| weighted routine at eps 0: R2 ([0-9.]+) R1 ([0-9.]+)", run):
        assert m.group(1) == m.group(3) and m.group(2) == m.group(4)


def test_the_referee_scans():
    r3 = (V / "referee" / "r3_free_lambda_run.txt").read_text(encoding="utf-8")
    assert "REACHABLE" in r3 and all("frac R2 in [2.5,3.5] 0.0000" in l for l in r3.splitlines() if l.strip().startswith("REACHABLE"))
    r4 = (V / "referee" / "r4_band_joint_run.txt").read_text(encoding="utf-8")
    assert all("frac_both>=2.5 0.0000" in l for l in r4.splitlines() if "frac_both" in l)
