"""B1627 -- GENESIS v1.37 carries W45/W46's scope sentence under FK11 and the owner's FK10 ruling; amend --check passes; the
lead-debt arc baseline is 83 or lower."""
import pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_genesis_v1_37_and_the_ratchet():
    g = ROOT.joinpath("GENESIS.md").read_text(encoding="utf-8")
    assert int(g.split("**Version 1.")[1].split()[0]) >= 37
    assert "the triplet's four-dimensional index is n times the fibre's index" in g and "keep FK10 open" in g
    assert subprocess.run([sys.executable, str(ROOT / "frontier" / "B1627_the_cusp_unit_kept_open" / "adoption" / "amend.py"), "--check"]).returncode == 0
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import lead_debt
    assert lead_debt.ARC_STALE_BASELINE <= 83
