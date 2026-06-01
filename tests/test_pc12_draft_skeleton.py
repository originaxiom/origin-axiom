"""Structure checks for the PC12 draft-note skeleton."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKELETON = ROOT / "papers" / "candidates" / "PC12_sl3_metallic_trace_maps" / "DRAFT_NOTE_SKELETON.md"


def test_pc12_skeleton_has_required_theorem_blocks():
    text = SKELETON.read_text(encoding="utf-8")
    required = [
        "Theorem 1 -- Metallic `SL(3)` Trace Map",
        "Theorem 2 -- Commutator Trace-Pair Invariant",
        "Theorem 3 -- Algebraic Entropy",
        "Theorem 4 -- Fixed-Line Splitting Classification",
        "Theorem 5 -- Compact Diagonal `SU(3)` Slice",
    ]
    for marker in required:
        assert marker in text


def test_pc12_skeleton_preserves_non_claims():
    text = SKELETON.read_text(encoding="utf-8")
    required = [
        "No physical interpretation is claimed.",
        "not a gauge theory",
        "not particle/antiparticle physics",
        "does not solve the PC11 T1/S1 selector",
    ]
    for marker in required:
        assert marker in text
