"""B1795 -- the doublet-triplet split at the canonical end (sealed 24b9e468d; outputs committed unread at 195d74e2f).  The
committed run: the controls hold; no line has an exact det M zero for either vector-like pair (S1, S1' hold; S2 fails);
S3 fails as sealed; the sealed instrument's hash; the post hoc pair comparison."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1795_the_doublet_triplet_split_at_the_canonical_end"
V = A / "verification"


def test_the_sealed_instrument():
    h = hashlib.sha256((V / "split.py").read_bytes()).hexdigest()
    assert h == "95d1593d6395b5965bd5409a6bd1cf8fbf7ca72a087e50c74a4250c7abceeca0"
    assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")


def test_the_cells():
    c = json.loads((V / "split.json").read_text(encoding="utf-8"))["cells"]
    assert c["C1_control_dev_le_1e-9"] and c["C2_order5_identity_le_1e-9"]
    assert c["S1_DECISIVE_no_line_with_exact_detM_H_zero"] and c["S1p_no_line_with_exact_detM_D_zero"]
    assert not c["S2_split_some_line_detM_H_zero_detM_D_not"] and not c["S3_DECISIVE_no_light_Higgs_pair_at_the_strip_ge_1e-3"]
    rows = [l for l in (V / "split_rows.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(rows) == 858


def test_the_posthoc_read():
    run = (V / "posthoc" / "pair_compare_run.txt").read_text(encoding="utf-8")
    assert "strip, the six's carriers    rows    6" in run and "pair_compare exit 0" in run
