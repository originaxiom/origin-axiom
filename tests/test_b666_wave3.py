"""B666 wave-3 locks (artifact-level)."""
import os

_C = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B666_leads_campaign")


def _has(cell, *keys):
    d = os.path.join(_C, cell)
    text = ""
    for f in os.listdir(d):
        if f.endswith((".md", ".txt")):
            text += open(os.path.join(d, f), errors="ignore").read()
    return all(k in text for k in keys)


def test_a2_symmetric_candidate():
    assert _has("cellA2", "slot-symmetric") or _has("cellA2", "SYMMETRIC")


def test_w35_bronze_2t():
    assert _has("cellW35", "2T")


def test_w31_unconditional():
    assert _has("cellW31", "312/312")


def test_w33_targets():
    assert _has("cellW33", "F1") or _has("cellW33", "F₁")
