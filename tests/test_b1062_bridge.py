"""B1062 locks -- the bridge cell: the gate, the fields, the negatives, the seal."""
import pathlib, hashlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1062_bridge_cell"


def test_seal_and_addendum_hashes():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("ad8d60f1"), h
    a = hashlib.sha256((ARC / "ADDENDUM_PRECOMPUTE_2026-08-13.md").read_bytes()).hexdigest()
    assert a.startswith("1b110f0a"), a


def test_block_logs_pin_the_numbers():
    b1 = (ARC / "b1062_v2_block1.log").read_text()
    assert "h0(M;27) = 1   h0(T^2;27) = 3" not in b1  # that was B1043's; guard against log mixup
    assert "geometric field contains sqrt(-3): True" in b1
    b3 = (ARC / "b1062_v2_block3.log").read_text()
    assert "eliminant factors (deg, mult): [(1, 2), (2, 1), (8, 1)]" in b3
    bat = (ARC / "b1062_verify_battery.log").read_text()
    assert "matches banked m004 monodromy [[2,1],[1,1]] up to conjugacy (tr 3 = 3, det 1 = 1): True" in bat
    assert "KILL VERIFIED INDEPENDENTLY" in bat
    n2 = (ARC / "b1062_v2_block2n.log").read_text()
    assert "m=1: distinct traces 1161" in n2 and "max/box 2" in n2
    assert "m=3" in n2 and "max/box 106" in n2
    v13 = (ARC / "b1062_v1_v3.log").read_text()
    assert "in the label set: False" in v13     # the tones excluded
    assert "intersection: []" in v13            # the band counts empty


def test_findings_ledger_discipline():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "CONTROL-EXHIBITED" in f
    assert "NOT gap labels" in f or "are NOT labels" in f
    assert "membership in a dense module" in f.lower() or "dense module" in f
    assert "SUPERSEDED" in f                     # block 2's spurious m=3 line
    assert "would have been WRONG" in f          # the spurious-component honesty
    assert "PROVED" in f
