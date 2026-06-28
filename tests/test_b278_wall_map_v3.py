"""B278 locks -- the E6-bridge wall map v3 (through B277): existence closed (B274/B275), wall #4 characterized
(B277), and the input-required walls B272 flagged as missing (family replication, SM matter, Lambda-sign) now
recorded explicitly, with the input-E6=output-E6 CRUX named as the load-bearing stop-gate. FIREWALLED; nothing to
CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B278_consolidation_v3" / "wall_map_v3.py"
_spec = importlib.util.spec_from_file_location("b278", _PATH)
b278 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b278)


def test_consistency():
    assert b278.consistency()


def test_wall_statuses():
    assert b278.WALLS[1]["status"] == "DISSOLVED"
    assert b278.WALLS[2]["status"] == "REDUCED"
    assert b278.WALLS[4]["status"] == "CHARACTERIZED"     # B277 upgraded #4 from OPEN
    assert b278.CRUX["name"] == "input-E6 = output-E6"


def test_missing_walls_now_recorded():
    # the three input-required walls B272 found absent from the map
    assert set(b278.INPUT_REQUIRED_WALLS) == {"family_replication", "sm_matter_breaking", "lambda_sign"}
    assert len(b278.E6_BRIDGE) == 11                       # B262-B267, B273-B277
