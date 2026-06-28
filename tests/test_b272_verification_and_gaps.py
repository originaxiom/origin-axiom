"""B272 locks -- the adversarial verification pass: 8 claims independently re-confirmed, 3 framing overclaims
corrected, the extended gap map (input-E6=output-E6 is the CRUX; family replication + SM matter are real walls
ABSENT from the 5-wall map; the Lambda-sign). FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B272_verification_and_gaps" / "verification_and_gaps.py"
_spec = importlib.util.spec_from_file_location("b272", _PATH)
b272 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b272)


def test_confirmed_and_corrections_counts():
    assert len(b272.CONFIRMED) == 8         # independently re-derived
    assert len(b272.CORRECTIONS) == 3       # B265 (EXIST->expected), B267 (framing), B266 (q=4)


def test_crux_is_input_equals_output_e6():
    crux = [k for k, g in b272.GAPS.items() if g["kind"] == "CRUX"]
    assert crux == ["input-E6 = output-E6"]


def test_missing_walls_flagged():
    absent = {k for k, g in b272.GAPS.items() if g["in_5wall"] == "ABSENT"}
    assert absent == {"family replication (3 generations)", "SM matter content / E6->SM breaking"}
    assert "cosmological-constant SIGN" in b272.GAPS   # Lambda-sign separate from the 122-order magnitude
