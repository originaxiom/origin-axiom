"""B283 lock -- scoping the arithmetic-self-generation vein (path-a / metallic WRT tower): it COLLAPSES like the E6
vein. The WRT-period<->arithmetic link is proven (B204), generic to all torus bundles (metallic = diagonal), and
known (Jeffrey 1992); the path-a conjectures are superseded/falsified. FIREWALLED; nothing to CLAIMS.md.
(Heavy genericity probe reproduced by python selfgen_genericity_probe.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B283_selfgen_scoping" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b283", _PATH)
b283 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b283)


def test_vein_collapses():
    assert not b283.METALLIC_IS_SPECIAL
    assert not b283.OBJECT_SPECIFIC_NOVEL_SIGNAL
    assert b283.verdict()


def test_path_a_conjectures_resolved():
    states = {v[0] for v in b283.LEVELS.values()}
    assert "SUPERSEDED" in states and "FALSIFIED" in states     # fundamental-unit + prime-absence
    assert any("KNOWN" in s for s in states)                    # Jeffrey 1992 / Fibonacci trace map


def test_meta_conclusion_both_veins():
    assert "B282" in b283.META and "exhausted" in b283.META
