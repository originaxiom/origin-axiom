"""B1293 — seat harvest: the load-bearing claims are re-computed, not accepted."""
import json, subprocess, sys
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1293_seat_harvest_2026-09-06"


def _mod():
    sys.path.insert(0, str(ARC / "verification"))
    try:
        import harvest
        return harvest
    finally:
        sys.path.pop(0)


def test_it_reproduces_by_RUNNING():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "harvest.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
    assert r.stdout.rstrip().endswith("SELFTEST: PASS")


def test_fc_R68_counts_reproduce():
    m = _mod()
    assert len(m.ROOTS) == 72 and len(m.W27) == 27
    assert 51840 // 1296 == 40


def test_fc_R68_labelling_gives_9_9_9():
    m = _mod()
    assert sorted(m.grade3((1, 0, 2, 2, 0, 2)).values()) == [9, 9, 9]
    assert sorted(m.grade3((1, 0, 0, 1, 1, 2)).values()) == [9, 9, 9]


def test_the_CALIBRATION_9_9_9_is_common_not_rare():
    """The point of the control: R68's content is the g-stability, NOT the partition."""
    import itertools, collections
    m = _mod()
    shapes = collections.Counter()
    for c in itertools.product(range(3), repeat=6):
        if any(c):
            shapes[tuple(sorted(m.grade3(c).values(), reverse=True))] += 1
    assert shapes[(9, 9, 9)] == 178, shapes[(9, 9, 9)]
    assert shapes[(9, 9, 9)] == max(shapes.values()), "9+9+9 is the MOST COMMON shape"
    txt = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "wrong number" in txt


def test_the_SM_seats_zL_is_an_A1A5_involution():
    """15+12 split of the 27 with a dim-38 centralizer = SU(2)xSU(6), i.e. (2,6bar)+(1,15)."""
    import itertools, collections
    m = _mod()
    dims = set()
    for c in itertools.product(range(2), repeat=6):
        if not any(c):
            continue
        p = collections.Counter(int(sum(c[i] * m.simple_coords(w)[i] for i in range(6))) % 2
                                for w in m.W27)
        if sorted(p.values()) != [12, 15]:
            continue
        even = sum(1 for r in m.ROOTS
                   if int(sum(c[i] * m.simple_coords(r)[i] for i in range(6))) % 2 == 0)
        dims.add(6 + even)
    assert 38 in dims, dims
    assert 3 + 35 == 38 and 78 - 38 == 40


def test_codex_is_recorded_as_having_nothing_new():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    c = v["claim_one_line"]
    assert "R040" in c and "ALREADY HARVESTED" in c


def test_priority_and_fences_are_recorded_not_softened():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "before main's B1290" in t                 # fc got there first; say so
    assert "harvest, not verification" in t.lower() or "NOT verified here" in t
    assert "other 39" in t                            # fc's own fence on I-14 is carried


def _plain(path):
    """Markdown text as one whitespace-normalised line: quoted prose here carries emphasis
    markers and hard-wraps, and matching raw text reddens on both (twice, in this file)."""
    import re
    return re.sub(r"\s+", " ", re.sub(r"[*_`>]", "", path.read_text(encoding="utf-8")))

# --- the framing correction (owner-prompted, 2026-09-06) ------------------------------------

def test_the_9_9_9_calibration_credits_fc_rather_than_correcting_them():
    """fc's R68 says 'not over-read' and 'by construction it is one of them' in the same
    paragraph that presents the partition. B1293's first writing handed that fence back to
    them as a correction. The addendum must withdraw it, and the withdrawal must name why."""
    add = ARC / "ADDENDUM_2026-09-06_I_UNDERSOLD_THE_SEATS.md"
    assert add.exists(), "the correction must live at source, not only in the log"
    t = _plain(add)
    assert "not over-read" in t and "by construction it is one of them" in t
    assert "Withdrawn" in t
    # and the unverified step must be named as owed, not left implicit
    assert "4 → 1" in t and "owed" in t.lower()


def test_the_addendum_states_the_seats_results_FIRST_and_without_hedging():
    t = _plain(ARC / "ADDENDUM_2026-09-06_I_UNDERSOLD_THE_SEATS.md")
    assert "first vacuum of this programme with the Standard-Model group" in t
    assert "before main did" in t or "before main" in t
    # the seats' own fences must still be carried -- correcting the framing must not delete them
    assert "other 39" in t and "closed closing" in t


def test_the_verdict_carries_the_correction_at_source():
    import json as _j
    v = _j.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    c = v["claim_one_line"]
    assert "FRAMING CORRECTED" in c and "UNVERIFIED" in c.upper()
    # the computations must NOT have been withdrawn along with the framing
    assert "120 A2" in c or "40 A2^3" in c or "A1A5" in c


@pytest.mark.slow
def test_fc_collapse_40_to_4_to_1_reproduces_here():
    """The debt B1293 named: R68's actual claim, not its coordinates. Slow (~3 min): builds E8,
    the 120 A2 and 40 A2^3 subsystems, and every A2^3-class order-3 element's action."""
    r = subprocess.run([sys.executable, str(ARC / "verification" / "fc_collapse.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.rstrip().endswith("SELFTEST: PASS")
    assert "{4: 40}" in out, out[-900:]                      # all 40 elements fix exactly 4
    assert "RANDOM order-3 elements" in out                  # the control that corrects my first try
    assert "NEVER 4" in out
