"""THE ROAD's lock — every banked node cites a real arc; the states and the
census stay honest; the B8113 correction stays carried."""
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROAD = (ROOT / "docs" / "THE_ROAD.md").read_text(encoding="utf-8")
# hard-wrap-proof matching (the B8109 lesson: a pattern that cannot cross a
# markdown wrap produces false zeros; every phrase assert runs on FLAT)
FLAT = " ".join(ROAD.split())


def test_every_cited_main_arc_exists():
    arcs = {a for a in re.findall(r"B\d{3,4}", ROAD) if not a.startswith("B8")}
    missing = [a for a in sorted(arcs)
               if not glob.glob(str(ROOT / "frontier" / f"{a}_*"))]
    assert not missing, f"THE ROAD cites nonexistent arcs: {missing}"
    assert len(arcs) >= 25, "the map lost its citation density"


def test_the_five_states_present():
    for s in ("[BANKED]", "[NAMED-OPEN", "[PROVEN-FREE", "[SEALED]", "[NEGATIVE"):
        assert s in ROAD, f"state marker {s} missing"


def test_proven_free_is_terminal_doctrine():
    assert "a TERMINAL state, not a failure" in FLAT
    assert ("the choice exists, the chooser does not" in FLAT
            or "the chooser provably does not" in FLAT)


def test_census_and_b8113_carried():
    # Corrected 2026-08-30 from "ten" to "nine" (B1218's sweep): L175 was counted open
    # while B1110 (PROVED) F5 reads "L175 CLOSES". Note what the old assertion was doing --
    # it PINNED the stale count, so the test was holding the error in place rather than
    # catching it. Hence the second assertion below, which checks a fact rather than a
    # string: if L175 is named at all, it must be named as closed.
    assert "nine genuine open nodes (one carrying" in FLAT
    if "L175" in FLAT:
        assert "L175 CLOSES" in FLAT or "L175 (the h = 0 locus) is REMOVED" in FLAT, \
            "L175 is decided by B1110 (PROVED); the map must not re-list it as open"
    assert "three residues" in FLAT
    assert "torsion-to-determinant" in FLAT, "B8113 residue 2 must stay explicit"
    assert "OUTSIDE Pfaff's absolute-convergence abscissa" in FLAT, "residue 3"


def test_freedom_ledger_present():
    assert "THE FREEDOM LEDGER" in FLAT
    assert "External suppliers named" in FLAT
