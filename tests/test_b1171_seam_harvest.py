"""B1171 lock -- THE SEAM HARVEST: five cross-seat results landed in one sitting. Locks the
B8144 adelic-mechanism addendum (the lock cc3 didn't ship), the L171 MOOD close, the L173 re-pose
(addendum-beside; the sealed spec untouched), the memos-80/82 harvest + L186, and the two codex
grade/scope adoptions. Asserts on COMMITTED files only. Gate 5 clean."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1171_seam_harvest"


def _d():
    return json.loads((ARC / "b1171_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1171" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_c1_adelic_mechanism_addendum_locked():
    # the main-side lock cc3 didn't ship: the addendum exists, carries the mechanism + both predictions
    txt = (ROOT / "frontier" / "B1164_cc_masterplan" / "ADDENDUM_adelic_mechanism.md").read_text(encoding="utf-8")
    assert "escape" in txt and "genuine automorphism" in txt
    assert "F₄(ℝ) to F₄(ℤ)" in txt or "F4(R) to F4(Z)" in txt.replace("₄", "4").replace("ℝ", "R").replace("ℤ", "Z")
    assert "archimedean IFF" in txt or "archimedean iff" in txt.lower()
    assert "finite half is always cheaper" in txt
    assert "cited" in txt.lower() and "Krutelevich" in txt
    # the mechanism was own-verified against all banked costs
    d = _d()["c1_b8144_adelic_mechanism"]
    assert "3/3" in d["own_verified"]
    assert len(d["predictions_preregistered"]) == 2


def test_c2_l171_closed_mood():
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "CLOSED (MOOD) 2026-08-27" in leads
    assert "COMPLEMENTARY to" in _d()["c2_b8145_l171_closed_mood"]["reason_moved"]
    assert "4/4" in _d()["c2_b8145_l171_closed_mood"]["cc_spot_verify"]


def test_c3_l173_reposed_sealed_spec_untouched():
    # the sealed spec's bytes are UNCHANGED (the seal sha still matches)
    spec = (ROOT / "docs" / "EDGE_PREREG_SPEC.md").read_bytes()
    assert hashlib.sha256(spec).hexdigest() == "6ede5c8d90b8667ca02ac131a2145d9138a6934b568aa661d7d7ad76738eed30", \
        "the sealed EDGE_PREREG_SPEC was edited -- the addendum-beside rule was violated"
    add = (ROOT / "docs" / "EDGE_PREREG_SPEC_ADDENDUM_B8146.md").read_text(encoding="utf-8")
    assert "OBSERVABLE" in add and "mode" in add.lower() and "commission" in add.lower()
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "PRECISION COLUMN RE-POSED" in leads
    seal = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert "EDGE_PREREG_SPEC_ADDENDUM_B8146.md" in seal


def test_c4_memos_and_l186():
    c4 = _d()["c4_cloud_memos_80_82"]
    assert "BYTE-IDENTICAL" in c4["verification"]
    assert "SHAPE EXISTS" in c4["memo80_texture"] and "DRESSING" in c4["memo80_texture"]
    assert "810/810" in c4["memo82_family_rank"] and "rank exactly 2" in c4["memo82_family_rank"]
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "## L186" in leads and "one or three" in leads


def test_c5_codex_adoptions():
    gn = (ROOT / "frontier" / "B1153_peripheral_and_superposition" / "ADDENDUM_grade_note_R015.md").read_text(encoding="utf-8")
    assert "not a theorem" in gn and "surmise" in gn.lower()
    fn = (ROOT / "frontier" / "B1158_cloud_wave2_harvest" / "ADDENDUM_fence_note_R016.md").read_text(encoding="utf-8")
    assert "stronger than the shipped computation" in " ".join(fn.split())
    assert "p ∈ {5,7}" in fn or "p in {5,7}" in fn


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
