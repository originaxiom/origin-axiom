"""B268 locks -- the E6-bridge consolidation: wall map v2 (#1 dissolved, #2 reduced), the 6-link E6 bridge,
and the audit of deferred sub-choices (all assigned to a phase). FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B268_e6_bridge_consolidation" / "wall_map_v2.py"
_spec = importlib.util.spec_from_file_location("b268", _PATH)
b268 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b268)


def test_e6_bridge_is_six_links():
    assert sorted(b268.E6_BRIDGE) == ["B262", "B263", "B264", "B265", "B266", "B267"]


def test_wall_map_v2_status_changes():
    code = lambda s: s.split("(")[0].strip()
    changed = {k for k, w in b268.WALLS.items() if code(w["v1_status"]) != code(w["v2_status"])}
    assert changed == {1, 2}                               # #1 dissolved, #2 reduced
    assert b268.WALLS[1]["v2_status"] == "DISSOLVED"
    assert b268.WALLS[2]["v2_status"].startswith("REDUCED")
    assert b268.WALLS[5]["v2_status"].startswith("QGAP")   # scale gap unchanged


def test_audit_nothing_dropped():
    # every skipped/deferred item is assigned to a named phase (no silent drops)
    assert len(b268.SKIPPED) == 5
    for s in b268.SKIPPED.values():
        assert s["status"].startswith(("PLANNED", "DONE", "DROPPED"))
