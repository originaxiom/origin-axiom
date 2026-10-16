"""B1421 lock -- the completeness sweep's measured facts.

(1) the identification ledger's irreducible input count, recomputed by B1266's method on today's rows: 8 sources,
    so 4 axioms + 8 = 12 free inputs for a physical reading -- the number the paper now states;
(2) the control: restricted to B1266's own ten rows the method reproduces its published partition (the 2-cycle
    I-10/I-11 is one source, and I-13/I-18/I-23 are one source);
(3) the orphan-map summary records the propagation measurement;
(4) the paper carries the twelve.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "frontier" / "B1421_the_completeness_sweep" / "verification"


def _run():
    r = subprocess.run([sys.executable, str(D / "identification_recount.py")],
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-1500:]
    return r.stdout


def test_twelve_irreducible_inputs():
    # [Review 64, 2026-10-16] the live ledger, not the B1421-era one: S133 (GENESIS v1.47) added I-31 to I-34, and the
    # price became 4 axioms + 9 irreducible sources = 13. This lock went stale then, because S133's landing suite was
    # selective and did not reach it; Review 64's full suite found it. The test name keeps the arc's original count.
    out = _run()
    m = re.search(r"irreducible sources: (\d+)\s+free inputs = 4 axioms \+ \d+ = (\d+)", out)
    assert m, out
    assert int(m.group(1)) == 9 and int(m.group(2)) == 13


def test_the_method_reproduces_b1266s_partition():
    out = _run()
    assert "'I-10', 'I-11'" in out                                  # a 2-cycle is ONE source, not two
    assert re.search(r"source: \['I-13',[^\]]*'I-18', 'I-23'", out)  # the listener map's three rows are one source
    assert "source: ['I-6']" in out and "source: ['I-26', 'I-34']" in out and "source: ['I-31']" in out   # Review 64: the live ledger


def test_orphan_map_summary_present():
    s = (D / "orphan_map_summary.txt").read_text()
    assert "orphaned 524" in s
    assert "absent from the generated views as well: 0" in s


def test_the_paper_states_the_twelve():
    t = (ROOT / "papers" / "P3_THE_PAPER" / "main.tex").read_text()
    assert "four for the structure" in t and "twelve" in t
