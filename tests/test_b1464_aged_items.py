"""B1464 -- the aged items paid and the seal gates read every seal."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1464_the_aged_items_paid_and_the_seal_gates_read_every_seal")
sys.path.insert(0, os.path.join(ROOT, "scripts", "gates")); sys.path.insert(0, os.path.join(ROOT, "scripts", "checks")); import gates


def test_the_seal_census_live():
    r = subprocess.run([sys.executable, os.path.join(A, "verification", "seal_census.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "VERDICT seal-census: PASS" in r.stdout, r.stdout[-400:] + r.stderr[-400:]
    d = json.load(open(os.path.join(A, "verification", "seal_census.json")))
    assert d["rows_both_shapes"] >= 46 and d["distinct_sealed_paths_with_digest"] >= 46 and d["with_neither"] == d["baseline"] == 41


def test_the_new_gates_are_registered_with_failing_paths():
    reg = json.load(open(os.path.join(ROOT, "tests", "GATE_CONTROLS.json")))
    for g in ("seal-ledger-current", "pretense-phrases", "seal-provenance", "seal-digests"):
        assert g in gates.GATES and g in reg, g
    assert len(gates.SEAL_PROVENANCE_BASELINE) == 41 and gates.PRETENSE_BASELINE == 0


def test_the_dispositions_are_on_the_record():
    t = open(os.path.join(ROOT, "docs", "REPRESENTATION_TRIAGE.md")).read(); assert "| B804 | PENDING |" in t
    c = json.load(open(os.path.join(ROOT, "docs", "CHAIN_COVERAGE.json"))); assert "MACHINE-READ since B1464" in c["_criterion"]
    term = open(os.path.join(ROOT, "TERMINOLOGY.md")).read(); assert "by an external audit, B1233" not in term
    import representation_sweep as rsw; assert rsw.SHORT_CLAIM_INDEG == 2
