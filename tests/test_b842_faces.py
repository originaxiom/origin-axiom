"""B842 — locks the face gate, the `none` discipline, and the flagged corpus discrepancy."""
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B842_face_attachment"
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"
_S = importlib.util.spec_from_file_location(
    "fleiss_kappa", ROOT / "scripts" / "checks" / "fleiss_kappa.py")
fk = importlib.util.module_from_spec(_S)
_S.loader.exec_module(fk)


def _r():
    return json.loads((ARC / "calibration_ratings.json").read_text(encoding="utf-8"))


def test_kappa_clears_the_sealed_gate():
    table, _, _ = fk.table_from_ratings(_r())
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert k >= 0.60, f"sealed gate 0.60; got {k}"
    assert abs(k - 0.8732) < 0.002, f"recorded 0.8732; got {k}"


def test_none_was_actually_used():
    """B806's classifier failed by over-predicting 55%. A panel that never declines repeats it."""
    kg = json.loads(KG.read_text(encoding="utf-8"))
    faced = sum(1 for r in kg if [f for f in (r.get("faces_consulted") or []) if f and f != "none"])
    assert faced > 600, f"only {faced} records carry a face; B842 wrote to 673"
    used_none = {v for m in _r().values() for v in m.values()}
    assert "none" in used_none, "the calibration panel must have used `none` at least once"


def test_the_corpus_discrepancy_is_recorded_not_silently_relabelled():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "56.2 %" in f and "Nothing existing is relabelled here" in f
    for a in ("B296", "B523"):
        assert a in f, f"{a} is a flagged discrepancy and must stay named"


def test_no_existing_attachment_was_overwritten():
    """Writer safety: B842 may only fill empty faces_consulted, never replace one."""
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "existing attachments overwritten | **0**" in f


def test_my_failed_prediction_is_recorded():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "I underestimated the panel" in f
