"""B1631 -- GENESIS v1.39 tags the cusp's unit (amend --check); the audit's sweep found 27 of 27 instruments reproducing
identically; the independent verifiers' scripts are archived."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = ROOT / "frontier" / "B1631_the_cusp_unit_tagged_and_the_negatives_audited"


def test_the_unit_tagged_and_the_audit_recorded():
    g = ROOT.joinpath("GENESIS.md").read_text(encoding="utf-8")
    assert int(g.split("**Version 1.")[1].split()[0]) >= 39 and "THE CUSP'S UNIT, A TAGGED WORKING POSTULATE" in g
    assert subprocess.run([sys.executable, str(ARC / "adoption" / "amend.py"), "--check"]).returncode == 0
    sweep = json.loads((ARC / "verification" / "audit_sweep.json").read_text())
    assert len(sweep) == 27 and all(r["rc"] == 0 for r in sweep)
    assert all(o["status"] == "IDENTICAL" for r in sweep for o in r["outputs"])
    for d in ("b1618_b1621", "b1628_b1629", "b1630"):
        assert list((ARC / "verification" / "independent" / d).glob("*.py")), d
