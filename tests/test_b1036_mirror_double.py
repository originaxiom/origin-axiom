"""B1036 locks — the mirror-double (sealed a10ae240). The heavy compute is banked via its
logged record; the locks re-verify the light invariants + the artifacts."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1036_mirror_double"


def test_the_record_script_exists_with_its_gates():
    s = (ARC / "b1036_final.py").read_text(encoding="utf-8")
    # the load-bearing gates are in the source:
    assert "MV vs double-Fox MISMATCH" in s or "cross-gate" in s
    assert "V1 CONTROL FAILED -- HALT" in s
    assert "banked gate V(" in s
    # the halted routes remain as process record:
    assert (ARC / "b1036_v3_pairing.py").exists()
    assert (ARC / "b1036_v3b_pairing.py").exists()


def test_findings_carry_the_verdicts_and_fences():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "h¹(dbl; 27) = 5, against the solo 3." in flat or "= 5, against the solo 3" in flat
    assert "2/2/1" in flat
    assert "rank(r) = 1 per block" in flat
    assert "agrees on every block" in flat
    assert "support is EMPTY" in flat
    assert "O2 restated" in flat
    assert "candidate, NOT a generations theorem" in flat
    assert "5 = 2+2+1, not 3" in flat
    assert "h¹(M; ad) = 6" in flat
    assert "named residual" in flat  # the scope fence on the unrun V-valued sector
    assert "NOT REALIZED" in flat    # the existence prior scored honestly


def test_verdict_and_seal():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1036" and v["verdict"] == "PROVED"
    c = v["claim_one_line"]
    assert "GAINS CLASSES, NOT THE SYMMETRIC PAIRING" in c
    assert "5, not 3" in c
    assert "h1(M; ad) = 6" in c
    for dep in ("B632", "B598", "B308", "B961"):
        assert dep in v["depends_on"]
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1036_mirror_double/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("a10ae240")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1)


def test_the_logged_record_numbers():
    """The final run's log is archived in-arc; the headline numbers are locked from it."""
    log = (ARC / "b1036_final_output.txt").read_text(encoding="utf-8")
    assert "V4 = 5; V5 = 6" in log
    assert "PRESENT cells = 0" in log
    assert log.count("V1 seam-gauge control: PASS") == 3
    assert log.count("cross-gate double-Fox h1 = 2") == 2
    assert "cross-gate double-Fox h1 = 1" in log
