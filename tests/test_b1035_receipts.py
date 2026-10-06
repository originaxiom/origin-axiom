"""B1035 locks — the receipts and the register."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1035_receipts_and_register"
RECEIPTS = ("CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md", "CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md",
            "CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md")


def _cells():
    spec = importlib.util.spec_from_file_location("b1035_verify", ARC / "b1035_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_v2_v3_all_verify():
    m = _cells()
    assert all(m.v1_theta_receipt().values())
    assert all(m.v2_falsifier_register().values())
    assert all(m.v3_main_register().values())


def test_the_pins_are_the_archived_blobs():
    """Pinned 2026-10-06: the three receipts, byte-exact, each the blob it was on B775's audit branch."""
    m = _cells()
    man = json.loads((ARC / "pinned" / "MANIFEST.json").read_text(encoding="utf-8"))
    pins = {f["path"]: f for f in man["files"]}
    assert sorted(pins) == sorted(RECEIPTS) and man["commit"].startswith("53da05f6")
    checks = m.v0_pinned_receipts()
    assert len(checks) == 3 and all(checks.values())
    # the two digests banked on 2026-08-12, from the branch, are the pins' own
    assert pins["CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md"]["sha256"] == m.H_TH
    assert pins["CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md"]["sha256"] == m.H_A


def test_the_lock_needs_no_ref(monkeypatch):
    """The regression: in a clone that resolves neither B775's audit branch nor its archive tag (sm:B1513's
    fast lane; any shallow or tagless clone) the receipts still verify, from the pins."""
    m = _cells()
    monkeypatch.setattr(m, "BR_CANDIDATES", ("refs/b1035/absent-a", "refs/b1035/absent-b"))
    assert m._source() is None and m.v0_provenance() is None
    assert all(m.v1_theta_receipt().values())
    assert all(m.v2_falsifier_register().values())


def test_a_changed_or_missing_pin_fails(tmp_path, monkeypatch):
    """The control: a pin that is not the archived blob is refused, never read. Phase B is the case
    that matters -- no digest of it was banked, so its content checks were the lock's only hold on it,
    and the edit below passes them."""
    m = _cells()
    for f in (ARC / "pinned").iterdir():
        (tmp_path / f.name).write_bytes(f.read_bytes())
    b = tmp_path / "CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md"
    b.write_bytes(b.read_bytes().replace(b"Phase A is not reworded", b"Phase A is not re-worded", 1))
    assert m.H_A in b.read_text(encoding="utf-8")          # V2's Phase B check still holds on the edit
    monkeypatch.setattr(m, "PIN_DIR", tmp_path)
    assert not all(m.v0_pinned_receipts().values())
    with pytest.raises(AssertionError, match="changed since pinning"):
        m.v2_falsifier_register()
    (tmp_path / "CC3_TO_CC_2026-08-10_THETA_WITHDRAWN.md").unlink()
    with pytest.raises(AssertionError, match="missing"):
        m.v1_theta_receipt()


def test_the_pins_match_the_archive_where_it_is_reachable():
    m = _cells()
    prov = m.v0_provenance()
    if prov is None:
        pytest.skip("neither B775's audit branch nor its archive tag resolves in this clone (shallow or tagless), "
                    "so the pins cannot be compared with the archive here; they are held to their recorded blob "
                    "ids above. To run this check: git fetch origin tag archive/braver-questions@53da05f6")
    assert len(prov) == 3 and all(prov.values())


def test_register_on_main_carries_the_honest_rows():
    t = " ".join((ROOT / "docs" / "FALSIFIER_REGISTER.md").read_text(encoding="utf-8").replace("*", "").split())
    assert "NOT FALSIFIABLE, AND WHY" in t
    assert "Earned confirmations: 1" in t
    assert "cannot be made testable by wording" in t
    assert "WHAT_WOULD_COUNT" in t
    # the two integration hashes:
    assert "f0f336ce" in t and "4ff7fc23" in t


def test_b1021_addendum_closes_the_held_rows():
    a = (ROOT / "frontier" / "B1021_cell9_receipt" / "ADDENDUM_2026-08-12.md").read_text(encoding="utf-8")
    assert "closed by B1035" in a
    assert "f0f336ce" in a and "7ea68d34" in a


def test_verdict():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1035" and v["verdict"] == "PROVED"
    assert "RELAYS ARE UNGATED" in v["claim_one_line"]
    for dep in ("B1021", "B1009", "B999"):
        assert dep in v["depends_on"]
