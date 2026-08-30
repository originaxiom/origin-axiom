"""B1212 — two replies. The locks pin what was VERIFIED and what stays the owner's."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1212_two_replies"


def _res():
    return json.loads((ARC / "b1212_results.json").read_text(encoding="utf-8"))


def test_codexs_certificate_reruns_on_this_bench():
    """Verify-don't-trust: the harvested certificate must run here from its own committed inputs."""
    p = subprocess.run([sys.executable, str(ARC / "verification" / "r024_lepton_character_datum.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert p.returncode == 0, p.stderr[-400:]
    out = p.stdout
    assert "PASS" in out
    assert "coarse_character_ec=0" in out and "coarse_character_l=0" in out
    assert "frame_level_lepton_pair=UNDETERMINED" in out
    assert "b1208_three_way_fork=UNRESOLVED" in out


def test_the_fork_stays_open_and_the_P3_row_does_not_move():
    """The temptation with an equal-characters result is to read it as branch (a). Coarse equality
    is not tensor identity, and the arc must keep saying so."""
    r = _res()["leg_1_codex_r024"]
    assert r["b1208_fork"] == "UNRESOLVED"
    assert r["frame_level_lepton_pair"] == "UNDETERMINED"
    assert r["p3_row"].startswith("stands at dim 1")
    assert any("independence" in s for s in r["not_banked"])
    assert r["coarse_character_ec"] == 0 and r["coarse_character_l"] == 0


def test_the_d2_confirmation_carries_its_provenance():
    """The PROVISIONAL was lifted by the owner on 2026-08-29. What this locks is not the decision --
    that is the owner's -- but that the decision was ASKED FOR and its words recorded, rather than
    inferred from a continue-token. That inference is the failure this whole thread corrected."""
    d = _res()["leg_2_cloud_d2"]
    assert d["payment_status"].startswith("CONFIRMED")
    c = d["owner_confirmation"]
    assert c["words"], "the confirmation must carry the owner's own words"
    assert "binary" in c["asked_as"]
    assert "NOT ESTABLISHED" in c["effect"], (
        "confirming the payment must not silently promote SCOPE-1b")


def test_scope_1b_is_recorded_as_not_established():
    """Amendment 1's whole content: the ladder being the realized history is a SEPARATE premise and
    an unpaid one. If it ever reads as established, the split was pointless."""
    a = _res()["leg_2_cloud_d2"]["amendment_1"]
    assert a["status"] == "UPHELD"
    assert "NOT ESTABLISHED" in a["effect"]
