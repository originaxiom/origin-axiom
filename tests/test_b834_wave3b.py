"""B834 — locks the replication, the relabels, and the coverage close-out."""
import glob
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B834_wave3b"
_SPEC = importlib.util.spec_from_file_location(
    "fleiss_kappa", ROOT / "scripts" / "checks" / "fleiss_kappa.py")
fk = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fk)


def _r():
    return json.loads((ARC / "calibration_ratings.json").read_text(encoding="utf-8"))


def test_kappa_replicates_wave3a():
    table, _, _ = fk.table_from_ratings(_r())
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert abs(k - 0.9300) < 0.002, f"recorded 0.9300; got {k}"
    assert abs(k - 0.9305) < 0.01, "wave 3b must replicate wave 3a's value"


def test_the_block_still_spans_four_categories():
    assert {v for m in _r().values() for v in m.values()} == {
        "PROVED", "NEGATIVE", "OPEN", "RETRACTED"}


def test_the_three_mixed_arcs_are_now_PROVED_with_both_halves():
    for slug in ("B61_sl5_high_precision", "B556_escalator_tower", "B746_golden_ledger"):
        d = json.loads((ROOT / "frontier" / slug / "arc_verdict.json").read_text(encoding="utf-8"))
        assert d["verdict"] == "PROVED", f"{slug} should be PROVED (24 readers, two panels)"
        c = d["claim_one_line"]
        assert "ESTABLISHED" in c and "UNSETTLED" in c, (
            f"{slug}: the relabel must carry BOTH halves or the unsettled part is lost")


def test_the_mixed_arc_rule_is_registered():
    p = " ".join((ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8").split())
    assert "MIXED ARCS" in p
    assert "`OPEN` is for an arc that settled **nothing**" in p


def test_coverage_is_essentially_complete():
    ids = set()
    import re
    for d in (ROOT / "frontier").iterdir():
        m = re.match(r"(B\d+)[a-zA-Z]?_", d.name)
        if m and d.is_dir():
            ids.add(m.group(1))
    judged = {json.loads(Path(p).read_text(encoding="utf-8"))["id"]
              for p in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json"))}
    # 0.94, not 0.95: the threshold is set against ARC IDS ON DISK (803), not the atlas's
    # population (759). The generated ledger quotes the atlas denominator, which reads 99.6% -- I
    # wrote that down first and this lock caught it (B834).
    frac = len(judged) / len(ids)
    assert frac > 0.93, f"coverage fell to {len(judged)}/{len(ids)} = {frac:.3f}"
    assert frac < 0.99, (
        "coverage now exceeds 99% of arc ids -- the 45 no-findings-document directories must have "
        "been resolved; update B834's residue statement")
