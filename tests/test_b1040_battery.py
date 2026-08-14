"""B1040 locks -- the FL-4 battery ledger: the counts, the split, the corollary."""
import pathlib, hashlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1040_fl4_observer_battery"


def test_seal_hash_unchanged():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("e358be1b"), h


def test_ledger_counts():
    led = (ARC / "b1040_ledger.md").read_text()
    assert "ω-essential steps = 0 of 11 decidable" in led
    assert "EXCLUDED: RETRACTED" in led          # S8 stays excluded, never adjudicated
    assert "shared by m003/m004" in led           # B735's banked V2 answer for the B723 rows
    assert "(√−3) = 0" in led or "(√−3) = 0" in led  # the bit-silent ramified door


def test_findings_split_and_corollary():
    # normalize whitespace: locked phrases must survive line-wrapping (the
    # window-read-as-whole species -- match content, not layout)
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "TEMPLATE = FIELD, SELECTION = OBJECT" in f
    assert "the observer cannot carry the trit" in f
    assert "PROVED" in f
    # the sealed mixed-branch discipline: scoped, not wholesale
    assert "not FIELD-SCOPED wholesale" in f and "not OBJECT-CARRYING wholesale" in f
