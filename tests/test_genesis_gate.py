"""The gate `genesis-cited` (WORKING_RULES, the rule of 2026-10-02 on the foundations): it passes on the repository and
fails four ways on a planted one."""
import importlib.util, os, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("gates", os.path.join(ROOT, "scripts", "gates", "gates.py"))
gates = importlib.util.module_from_spec(spec); spec.loader.exec_module(gates)


def plant(tmp_path, genesis=None, drop_pointer=None, extra=None):
    for rel in gates.GENESIS_POINTERS:
        f = tmp_path / rel; f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("# a page\n" + ("" if rel == drop_pointer else "Foundations: `GENESIS.md` is canonical.\n"))
    if genesis is not None: (tmp_path / "GENESIS.md").write_text(genesis)
    for rel, text in (extra or {}).items():
        f = tmp_path / rel; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text)
    return gates.genesis_problems(tmp_path)


GOOD = "# GENESIS\n\n**Version 9.9 · a date · canonical.**\n\n| SE1 | the criterion |\n| FK2 | a fork |\n\n## 10. Version log\n\n- **v9.9 · a date · an arc.**\n"


def test_the_repository_passes():
    assert gates.genesis_problems() == []
    assert "genesis-cited" in gates.GATES and gates.gate_genesis_cited()[0] is True


def test_a_good_plant_passes(tmp_path):
    assert plant(tmp_path, GOOD) == []


def test_it_fails_four_ways(tmp_path):
    assert plant(tmp_path / "a") == ["GENESIS.md is missing"]
    assert any("no entry in its version log" in b for b in plant(tmp_path / "b", GOOD.replace("- **v9.9 ·", "- **v9.8 ·")))
    assert any("README.md does not point" in b for b in plant(tmp_path / "c", GOOD, drop_pointer="README.md"))
    bad = plant(tmp_path / "d", GOOD, extra={"frontier/B1460_planted/FINDINGS.md": "A result about SE1 and about GAP7.\n"})
    assert any("GAP7" in b and "SE1" not in b for b in bad)


def test_an_arc_before_the_rule_is_not_read(tmp_path):
    assert plant(tmp_path, GOOD, extra={"frontier/B1400_old/FINDINGS.md": "GAP7 and FK99.\n"}) == []


def test_the_page_defines_what_it_is_cited_for():
    g = open(os.path.join(ROOT, "GENESIS.md")).read()
    ids = set(gates.GENESIS_ID_RE.findall(g))
    assert {"PF1", "PF2", "PF3", "GM1", "GM4", "GM5c", "SE1", "SE2", "T-ROOT", "F-FC", "F-CI", "F-HE", "F-AP", "F-MC", "FK1", "FK11", "GAP1", "GAP5"} <= ids
    assert "**Version 1.1 ·" in g or "**Version 1." in g or "**Version 2." in g
