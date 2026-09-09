"""B1226 -- the beta-odd box, and the E53 lock on the equivalence it broke.

B1012 banked the chain  blind-to-k <=> CS = 0 <=> amphichiral.  B1224 (same day, no test
lock of its own) forces CS into {0, 1/4}, which breaks the second link.  These tests assert
the FACTS -- exhibited counterexamples -- not the sentences that were edited, and they lock
the six reader-facing surfaces against re-asserting the falsified form (E53).
"""
import io
import json
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1226_the_beta_odd_box"


def _cs_class(M):
    v = float(M.chern_simons()) % 0.5
    return 0.0 if min(v, 0.5 - v) < 1e-9 else round(v, 9)


@pytest.mark.parametrize("name,chiral,cs", [
    ("m004", False, 0.0),    # amphichiral, CS = 0     -- the object
    ("m003", False, 0.25),   # amphichiral, CS = 1/4   -- kills  amph => CS=0
    ("m208", True,  0.0),    # CHIRAL,      CS = 0     -- kills  CS=0 => amph
])
def test_counterexamples_are_real(name, chiral, cs):
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold(name)
    assert M.symmetry_group().is_amphicheiral() is not chiral, name
    assert _cs_class(M) == cs, (name, _cs_class(M))


def test_is_isometric_to_mirror_is_not_a_chirality_test():
    """The trap: m208 IS isometric to its mirror, yet is chiral -- the isometry reverses
    orientation.  A seat trusting is_isometric_to would conclude the opposite."""
    snappy = pytest.importorskip("snappy")
    A = snappy.Manifold("m208")
    B = snappy.Manifold("m208"); B.reverse_orientation()
    isos = A.is_isometric_to(B, return_isometries=True)
    assert isos, "m208 does admit isometries to its mirror"
    dets = {I.cusp_maps()[0].det() for I in isos}
    assert dets == {-1}, dets            # all orientation-REVERSING
    assert A.symmetry_group().is_amphicheiral() is False


def test_b1224_torsion_law_holds_on_the_census_sample():
    """B1224's law, which B1226 rests on and which shipped without a lock."""
    snappy = pytest.importorskip("snappy")
    for n in ["m004", "m003", "m136", "m135", "m206", "m207"]:
        M = snappy.Manifold(n)
        assert M.symmetry_group().is_amphicheiral(), n
        assert _cs_class(M) in (0.0, 0.25), (n, _cs_class(M))


def test_cells_recorded_the_break():
    c1 = json.load(open(ARC / "cell1_results.json"))
    assert c1["verdict"]["B1012_equivalence_holds"] is False
    assert c1["verdict"]["amphichiral_implies_CS0"] is False
    assert c1["verdict"]["CS0_implies_amphichiral"] is False


def test_typing_is_not_vacuous_and_box_D_is_the_beta_odd_three():
    c2 = json.load(open(ARC / "cell2_results.json"))
    assert c2["mb12"]["vacuous"] is False
    assert c2["mb12"]["boxes_occupied"] == 4          # a flat count would occupy 1
    assert c2["beta_odd_count"] == 3
    assert sum(b["n"] for b in c2["boxes"].values()) == 28


def test_every_box_D_probe_demanded_a_value():
    c3 = json.load(open(ARC / "cell3_results.json"))
    assert c3["type_matched_probes"] == 0
    assert len(c3["demanded_a_value"]) == c3["n_probes"] == 3
    for pid, d in c3["probes"].items():
        assert d["verdict_in_record"] == "NEGATIVE", pid


FALSIFIED = [
    "blindness to the level *is* amphichirality",
    "CS = 0, forced by amphichirality",
    "≡ 0 ≡ amphichirality",
    "equivalent to amphichirality",
]


def test_no_surface_reasserts_the_falsified_equivalence():
    """E53 lock: the break must stay propagated to every reader-facing surface."""
    bad = []
    for p in sorted((ROOT / "docs").rglob("*.md")) + sorted((ROOT / "papers").rglob("*.tex")):
        txt = io.open(p, encoding="utf-8", errors="ignore").read()
        for f in FALSIFIED:
            if f in txt:
                bad.append(f"{p.relative_to(ROOT)}: {f!r}")
    assert not bad, "falsified equivalence re-asserted:\n  " + "\n  ".join(bad)
