"""P-417's first gate, doc-facts: a stale present-tense fact on a front page fails; a historical mention does not."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import doc_facts


def _tree(tmp_path, readme):
    (tmp_path / "GENESIS.md").write_text("# GENESIS\n\n**Version 1.59 · 2026-10-28 · canonical.**\n", encoding="utf-8")
    (tmp_path / "README.md").write_text(readme, encoding="utf-8")
    return tmp_path


def test_doc_facts_fails_on_a_stale_present_tense_version(tmp_path):
    root = _tree(tmp_path, "> **State.** `GENESIS.md` is at v1.14. More text.\n")
    problems = doc_facts.check(root, ["README.md"])
    assert problems and "is at v1.14" in problems[0] and "v1.59" in problems[0]


def test_doc_facts_passes_history_and_the_current_version(tmp_path):
    root = _tree(tmp_path, "GENESIS v1.14 (B1482) was the sign.\n`GENESIS.md` was at v1.14 then.\n`GENESIS.md` is at v1.59.\n")
    assert doc_facts.check(root, ["README.md"]) == []


def test_doc_facts_on_the_repository():
    assert doc_facts.check() == [], doc_facts.check()
