"""E21 GUARD (mechanical) — the SL/PSL centre error class has fired THREE times.

B731's wrong "level (4)" (E21) -> B734's correction -> and on 2026-07-29 BOTH cc and cc3
wrote "PSL(2,Z[w]/4)" for SL(2,Z[w]/4)/{+-I}, which propagated into a LAW_MAP row, a lock,
two FINDINGS, and cc3's masterplan Cell 6 (where it would have made a seat build a degree-6
action and fail the cell for the wrong reason).

Naming the rule did not stop it recurring. Wave 6's lesson applies: only an in-code check
does. This is that check.
"""
import pathlib
import re

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SKIP = {".git", "__pycache__", ".venv", "venv", "node_modules", "legacy",
         "site-packages", "phi_env", "audit", ".tmpwork", "cc2_packets"}

# The fact: |Z(SL(2,Z[w]/4))| = 4 (lambda^2=1 has four solutions), so the TRUE
# |PSL(2,Z[w]/4)| = 960. The order-1920 group is SL(2,Z[w]/4)/{+-I}, an INTERMEDIATE quotient.
_BAD = [
    re.compile(r"1920\s*=\s*\|?PSL\(2\s*,\s*(?:Z|ℤ)\[(?:w|ω)\]\s*/\s*4\)"),
    re.compile(r"\|PSL\(2\s*,\s*(?:Z|ℤ)\[(?:w|ω)\]\s*/\s*4\)\|\s*=\s*1920"),
]


def test_no_file_calls_the_order_1920_group_PSL_mod4():
    offenders = []
    for path in _ROOT.rglob("*"):
        if path.is_dir() or any(p in _SKIP for p in path.parts):
            continue
        if path.suffix not in (".md", ".py", ".txt", ".json"):
            continue
        if path.resolve() == pathlib.Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pat in _BAD:
            if pat.search(text):
                offenders.append(str(path.relative_to(_ROOT)))
                break
    assert not offenders, (
        "E21 recurrence — these call the order-1920 group PSL(2,Z[w]/4). "
        "|PSL(2,Z[w]/4)| = 960; the order-1920 group is SL(2,Z[w]/4)/{+-I}:\n"
        + "\n".join(offenders))


def test_the_centre_really_does_have_order_four():
    """The fact the guard rests on, recomputed so the guard cannot outlive its premise."""
    def rmul(x, y):
        a, b = x; c, d = y
        return ((a * c - b * d) % 4, (a * d + b * c - b * d) % 4)
    R = [(a, b) for a in range(4) for b in range(4)]
    sq1 = [l for l in R if rmul(l, l) == (1, 0)]
    assert sorted(sq1) == [(1, 0), (1, 2), (3, 0), (3, 2)]
    assert len(sq1) == 4
    assert 3840 // len(sq1) == 960          # the TRUE PSL order
    assert 3840 // 2 == 1920                # the intermediate quotient SL/{+-I}
