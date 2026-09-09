"""B1266 — the 10 unearned rows reduce to 7 irreducible sources; the price is 11, not 14.
(2026-09-07, B1296: I-27 registered -> 11 rows, 8 sources, price 12; the pins below track the live ledger.)"""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1266_the_source_of_input" / "verification" / "sources.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import sources as S
    return S


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_ten_rows_reduce_to_seven_sources():
    S = _mod()
    un, edges, groups = S.sources()
    import json
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    assert len(un) == b["unearned"]            # the rows are the ratchet's rows (14 on 2026-09-09: I-27, I-28, I-29, I-30 since B1266)
    assert len(groups) == 8                    # the irreducible sources: I-27 was the eighth (B1296); I-28, I-29, I-30 are instances (of I-27, I-13, I-27)
    assert S.AXIOMS + len(groups) == 12        # the price against the SM's 19


def test_the_fork_cycle_is_one_source_not_two():
    """A naive transitive closure splits the I-10<->I-11 cycle and reports 8."""
    S = _mod()
    _, _, groups = S.sources()
    fork = [v for v in groups.values() if "I-10" in v]
    assert len(fork) == 1 and sorted(fork[0]) == ["I-10", "I-11"]


def test_a_reference_to_an_EARNED_row_is_not_a_dependency():
    """I-25 cites I-1, which is EARNED — counting it would invent a debt."""
    S = _mod()
    _, edges, _ = S.sources()
    assert edges["I-25"] == []
