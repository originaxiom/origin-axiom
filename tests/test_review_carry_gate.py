"""R50 lock -- the review-carry continuity extension (the gate leaked twice while green:
R46-6/7/11 mis-keyed; R48-4..10 silently dropped). Unit-tests _carry_leaks on synthetic text
+ pins the real ledger green."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_mod", ROOT / "scripts" / "gates" / "gates.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_silent_drop_is_caught():
    g = _gates()
    text = (
        "### Action items (Review 48)\n"
        "- [>] R48-4: verify the thing (carried)\n"
        "anchor-commit: `aaaa`\n\n"
        "### Action items (Review 49)\n"
        "- [x] R49-0: something else entirely\n"
        "anchor-commit: `bbbb`\n"
    )
    leaks = g._carry_leaks(text)
    assert any("R48-4" in l for l in leaks), "a silently dropped carry was not caught"


def test_recurring_key_is_continuous():
    g = _gates()
    text = (
        "### Action items (Review 48)\n"
        "- [>] R48-4: verify the thing (carried)\n"
        "anchor-commit: `aaaa`\n\n"
        "### Action items (Review 49)\n"
        "- [ ] R49-1: the R48-4 item, restored and owned\n"
        "anchor-commit: `bbbb`\n"
    )
    assert g._carry_leaks(text) == []


def test_pre_r46_blocks_exempt():
    g = _gates()
    text = (
        "### Action items (Review 35)\n"
        "- [>] R35-2: ancient carry, key never recurs\n"
        "anchor-commit: `aaaa`\n\n"
        "### Action items (Review 36)\n"
        "- [x] R36-0: done\n"
        "anchor-commit: `bbbb`\n"
    )
    assert g._carry_leaks(text) == []


def test_latest_block_carries_are_not_leaks():
    g = _gates()
    text = (
        "### Action items (Review 50)\n"
        "- [>] R50-9: carried into the future, no later block yet\n"
        "anchor-commit: `aaaa`\n"
    )
    assert g._carry_leaks(text) == []


def test_real_ledger_is_continuous_now():
    g = _gates()
    ok, msg = g.gate_review_actions()
    assert ok, f"the real REVIEWS.md has carry leaks or open superseded items: {msg}"
