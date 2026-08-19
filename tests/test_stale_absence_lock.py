"""The stale-absence lock (2026-08-19, the ninth bank's sweep made durable).

The sweep found 12 doc claims of absence/openness that newer arcs had overtaken,
16 absences still genuinely current, and 1 ambiguous row. Fixes and stamps landed
in place. This lock keeps them landed: every swept site must still carry its
correction or its dated currency stamp, so no later edit can quietly re-hide a
banked breakthrough or silently drop a verified absence back to unstamped prose.

New absences added after B1082 are governed by the discipline these stamps
exemplify (stamp at write time), not by this lock.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STAMP = "stamp 2026-08-19: still CURRENT as of B1082"

# (file, anchor that must be present) — the 12 fixes
FIXES = [
    ("README.md", "OVERTAKEN on 2026-08-10 by B1019"),
    ("docs/OPEN_LEADS.md", "OVERTAKEN\non 2026-08-10 by B1019"),
    ("docs/THE_FRAMEWORK.md", "CLOSED the same day (2026-08-10) by B1016"),
    ("docs/SM_SPECIFICATION_LEDGER.md", "SEVEN sealed crossings, seven negatives"),
    ("docs/LISTENER_MAP_SPEC.md", "STATUS ADDENDUM"),
    ("docs/LISTENER_MAP_SPEC.md", "LARGELY ANSWERED WITHIN 48 HOURS"),
    ("docs/LISTENER_MAP_SPEC.md", "u3/u6 are the unique pair fixed individually by all 16 Galois"),
    ("docs/OPEN_LEADS.md", "both halves FILLED the\nday after registration"),
    ("docs/LAW_MAP.md", "SCOPE 2026-08-19, B1079's addendum"),
]

# (file, count of currency stamps that must survive) — the 16 stamps as landed
STAMP_COUNTS = [
    ("docs/THE_FRAMEWORK.md", 1),
    ("docs/OPEN_LEADS.md", 4),  # gerbe, L88 symbolic, K021/K022 dictionary, +1 landed in-table
    ("docs/THE_SM_VERDICT.md", 1),
    ("docs/HINT_LEDGER.md", 2),
    ("docs/CROSSING_REQUIREMENTS.md", 1),
    ("docs/KIND_TABLE.md", 1),
    ("CLAIMS.md", 2),
    ("docs/LAW_MAP.md", 3),
    ("docs/THEOREM_LEDGER.md", 1),
    ("docs/THE_FORCED_AND_THE_FREE.md", 1),
    ("docs/LISTENER_MAP_SPEC.md", 1),
]

AMBIGUOUS = ("docs/NOVELTY_SWEEP_LEDGER.md",
             "banking-seat ruling on the sweep's AMBIGUOUS flag")

# The cold-audit corrections that ride the same bank
AUDIT_CORRECTIONS = [
    ("frontier/B1079_wilson_menu/FINDINGS.md", "the golden m = 1 member is TORSION-FREE"),
    ("frontier/B1079_wilson_menu/arc_verdict.json", "W x Galois"),
    ("frontier/B1076_coboundary_sweep/FINDINGS.md", "kernel {I, χ_a}"),
    ("docs/THE_FORCED_AND_THE_FREE.md", "unique ergodicity"),
    ("docs/THE_FORCED_AND_THE_FREE.md", "non-normalisable"),
    ("docs/THE_FORCED_AND_THE_FREE.md", "Gleason"),
]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_fixes_still_landed():
    for rel, anchor in FIXES:
        assert anchor in _read(rel), f"sweep fix lost: {rel} lacks {anchor[:60]!r}"


def test_currency_stamps_survive():
    for rel, n in STAMP_COUNTS:
        got = _read(rel).count(STAMP)
        assert got >= n, f"{rel}: {got} currency stamps, lock requires >= {n}"


def test_total_stamp_floor():
    total = sum(_read(rel).count(STAMP) for rel, _ in STAMP_COUNTS)
    assert total >= 16, f"only {total} currency stamps survive repo-wide; 16 landed"


def test_ambiguity_ruling_recorded():
    rel, anchor = AMBIGUOUS
    assert anchor in _read(rel), "the T-MAGIC ambiguity ruling was removed"


def test_cold_audit_corrections_landed():
    for rel, anchor in AUDIT_CORRECTIONS:
        assert anchor in _read(rel), f"audit correction lost: {rel} lacks {anchor!r}"
