"""B1020/B1021/B1022 — locks for the admissibility ledgers, the receipt, and the publication."""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_kind_table_exists_with_the_binding_corollary():
    t = (ROOT / "docs" / "KIND_TABLE.md").read_text(encoding="utf-8")
    flat = " ".join(t.lower().replace("*", "").split())
    assert "coupling channel" in flat and "mixing" in flat
    assert "does not seal" in flat, "the inadmissible-pair clause is the table's teeth"
    assert "-2.3" in t.replace("\u2212", "-"), "B856's exclusion must stay row 1 of the lane's ledger"
    req = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    assert "KIND_TABLE.md" in req, "R5/R2 must point at the ledgers"


def test_the_cell9_receipt_chain_holds():
    d = json.loads((ROOT / "frontier" / "B1021_cell9_receipt" / "harvested" /
                    "cell9_rung1_v3_7.0720.json").read_text())
    assert d["prereg"] == "169e9042"
    assert d["r_refined"].startswith("7.07200418587520500073719418")
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert "169e9042" in ledger
    manifest = (ROOT / "frontier" / "B1021_cell9_receipt" / "HARVEST_HASHES.txt").read_text()
    assert "cell9_rung1_v3_7.0720.json" in manifest


def test_the_phase1_publication_matches_its_seal():
    """The hash-first protocol's whole point, kept executable."""
    content = (ROOT / "frontier" / "B1022_functor_phase1" / "PHASE1_CORPUS.md").read_bytes()
    h = hashlib.sha256(content).hexdigest()
    assert h == "50d4bdd9be033808db9f5d4b97cb99b8953b7cc9ef6f3ace56e22a4cc4720a7c", (
        "the published Phase-1 content no longer matches the digest sealed at 4b3cbfdc -- "
        "any edit after sealing voids the protocol; a correction goes through Phase 2, not here")


def test_the_phase1_claims_are_not_upgraded():
    v = json.loads((ROOT / "frontier" / "B1022_functor_phase1" / "arc_verdict.json").read_text())
    assert "NOTHING HERE UPGRADES C1-C12" in v["claim_one_line"]


def test_b709_is_fenced_not_retracted():
    f = (ROOT / "frontier" / "B709_turok_marriage_adjudication" / "FINDINGS.md").read_text()
    assert "FENCE (2026-08-10" in f and "B813" in f
    assert "do NOT upgrade" in f, "the original firewall clause must survive the fence"
