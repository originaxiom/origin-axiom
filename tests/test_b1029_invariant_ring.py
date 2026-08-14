"""B1029 locks — the invariant ring of the frame action (Lane III-1, sealed 9a46975f)."""
import importlib.util
import json
import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1029_invariant_ring"


def _cells():
    spec = importlib.util.spec_from_file_location("b1029_cells", ARC / "b1029_cells.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _flat(p: Path) -> str:
    t = p.read_text(encoding="utf-8")
    return " ".join(t.replace("**", "").replace("−", "-").split())


def test_v1_the_action_derived():
    m = _cells()
    r = m.v1_the_action()
    assert all(r.values()), r
    # the discriminating fact: reversal acts on VALUES exactly as conjugation does,
    # hence theta = c*r is the value-kernel.
    assert any("reversal = the SAME" in k for k in r)
    assert any("theta = c*r acts TRIVIALLY" in k for k in r)


def test_v2_invariants_and_closures():
    m = _cells()
    r = m.v2_invariants()
    assert all(r.values()), r
    phi = (1 + sp.sqrt(5)) / 2
    # independent re-derivation of the two closure identities (not trusting the cell):
    tones = [sp.Integer(0), 1 / (2 * phi), sp.Rational(1, 2), phi / 2, sp.Integer(1)]
    assert sp.simplify(sum(tones) - phi**2) == 0
    assert sp.simplify(1 / (phi * sp.sqrt(5)) + phi / sp.sqrt(5) - 1) == 0


def test_v3_prices_under_the_sealed_cap():
    m = _cells()
    r = m.v3_relational()
    assert all(r.values()), r
    # the prices themselves, re-derived: log2(C(3,2)) and log2(6-2), both under 3.0
    assert float(sp.log(sp.binomial(3, 2), 2)) < 3.0
    assert sp.simplify(sp.log(4, 2) - 2) == 0


def test_findings_carry_the_verdict_and_the_correction():
    flat = _flat(ARC / "FINDINGS.md")
    assert "SHELF DELIVERED" in flat
    assert "value-kernel of the frame action" in flat
    assert "ONE COORDINATE: sign(arg h)" in flat or "one sign" in flat.lower()
    assert "1.585 bits" in flat and "2.0 bits" in flat
    # no-data-contact is load-bearing (this arc must never touch measured values):
    assert "No data contact" in flat or "no data contact" in flat
    # the house correction record (first compute printed EMPTY/blocked):
    assert "Correction recorded" in flat
    # the scope fence on the placement theorem:
    assert "sealed inventory" in flat


def test_verdict_json():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1029" and v["verdict"] == "PROVED"
    assert "VALUE-KERNEL" in v["claim_one_line"].upper()
    for dep in ("B1024", "B1026", "B1011", "B856"):
        assert dep in v["depends_on"]
    assert "SHELF DELIVERED" in v["claim_one_line"]
    assert "NO DATA CONTACT" in v["claim_one_line"].upper()


def test_prereg_seal_intact():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1029_invariant_ring/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("9a46975f")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1), "sealed prereg must remain byte-identical"
