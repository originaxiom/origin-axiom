"""B297 lock -- the seam-arc wall map v4 (through B296). Consolidates B286-B296: the five walls re-examined through
the seam, the structural theorem relocated to the seam (selective for own structure, catalogue for SM-values), and
the matter map (1 of 3 forced). FIREWALLED; nothing to CLAIMS.md. (Reproducer: python frontier/B297_consolidation_v4/wall_map_v4.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B297_consolidation_v4" / "wall_map_v4.py"
_spec = importlib.util.spec_from_file_location("b297", _PATH)
b297 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b297)


def test_wall_map_v4_consistent():
    assert b297.consistency()
    assert len(b297.WALLS) == 5 and len(b297.SEAM_ARC) == 11


def test_wall3_relocated_to_seam():
    assert b297.WALLS[3]["status"] == "OPEN->MECHANISM-AT-SEAM"          # chirality mechanism at the seam, sign free


def test_structural_theorem_and_matter_map():
    assert "SELECTIVE" in b297.STRUCTURAL_THEOREM and "CATALOGUE" in b297.STRUCTURAL_THEOREM
    assert b297.MATTER_MAP["CP_magnitude_pi_6"].startswith("BULK")
    assert b297.MATTER_MAP["CP_sign_exists"].startswith("SEAM")
    assert b297.MATTER_MAP["which_CP_sign"].startswith("EXTERNAL")


def test_crux_and_stop_gates():
    assert b297.CRUX["name"] == "input-E6 = output-E6"
    assert len(b297.STOP_GATES) == 5
