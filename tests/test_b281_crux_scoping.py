"""B281 lock -- scoping of the CRUX (input-E6 = output-E6). The geometric level is SETTLED in-sandbox: every simple
type gives dim H^1 = rank on 4_1, so E6 is NOT geometrically distinguished (the 3d-3d input is free). The
physics-forcing level is NOT in-sandbox (needs T[4_1;E6]) = the R6 specialist gate. FIREWALLED; nothing to CLAIMS.md.
(Heavy probe reproduced by sage-python crux_geom_probe.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B281_crux_scoping" / "crux_verdict.py"
_spec = importlib.util.spec_from_file_location("b281", _PATH)
b281 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b281)


def test_geometry_does_not_distinguish_e6():
    assert b281.EVERY_TYPE_GIVES_RANK            # input type geometrically free


def test_crux_not_settleable_in_sandbox():
    assert not b281.SETTLEABLE_IN_SANDBOX        # TRUE-route is the specialist/tool gate
    assert b281.verdict()


def test_four_levels_present():
    assert len(b281.LEVELS) == 4                 # combinatorial / geometric / arithmetic / physics-forcing
