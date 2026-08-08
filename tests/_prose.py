"""Shared prose normaliser for markdown assertions.

Banked lesson (hit four times on 2026-08-08): markdown findings are hard-wrapped
AND carry inline markers ('>' blockquote, '*' emphasis) that land mid-sentence
once whitespace is collapsed -- and a probe with capitals silently fails against
lowercased text. `contains()` removes every one of those failure modes.
"""
import re


def norm(path):
    t = path.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^\s*>\s?", "", t)   # blockquote markers
    t = t.replace("*", "").replace("`", "")
    return " ".join(t.split())


def contains(path, *probes):
    """Case-insensitive, marker-insensitive, wrap-insensitive substring check.

    NOTE: always call as `assert contains(...)`. The helper asserts internally,
    but a bare call leaves the test body assertion-free, which the `test-vacuity`
    gate correctly flags as unconditionally passing.
    """
    t = norm(path).lower()
    missing = [p for p in probes if p.lower() not in t]
    assert not missing, f"missing from {path.name}: {missing}"
    return True
