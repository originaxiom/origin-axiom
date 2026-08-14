"""B827 — locks the single-progress-log invariant and a gate that can still fail."""
import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(g)


def test_there_is_exactly_one_progress_log():
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "audit", "legacy", "node_modules", "__pycache__",
                                    "veins")]
        if "PROGRESS_LOG.md" in filenames:
            found.append(os.path.relpath(os.path.join(dirpath, "PROGRESS_LOG.md"), ROOT))
    assert found == ["PROGRESS_LOG.md"], f"expected one progress log at the root; got {found}"


def test_the_recovered_entries_are_in_the_canonical_log():
    t = (ROOT / "PROGRESS_LOG.md").read_text(encoding="utf-8")
    assert "RECOVERED: 37 entries that were written to a shadow file" in t
    for marker in ("B725 — THE BORN RULE", "B826 — B519's missing verdict"):
        assert marker in t, f"migrated entry missing: {marker}"


def test_the_gate_can_fail_on_a_shadow_file(tmp_path):
    """The check that would have caught B827 on day one."""
    probe = ROOT / "docs" / "PROGRESS_LOG.md"
    assert not probe.exists()
    probe.write_text("# shadow\n", encoding="utf-8")
    try:
        ok, msg = g.gate_log_changelog_paired()
        assert not ok and "shadow progress log" in msg
    finally:
        probe.unlink()
    assert g.gate_log_changelog_paired()[0], "gate must pass again once the shadow is gone"


def test_the_gate_still_checks_the_pairing_rule():
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    fn = src[src.index("def gate_log_changelog_paired"):src.index('CHAIN = "docs/THEOREM_LEDGER.md"')]
    assert "commits ahead of PROGRESS_LOG" in fn, "the same-or-next-PR rule must still be enforced"
    assert "cannot detect that nobody writes it" in fn, "the failure mode must stay documented"
