"""B1504 lock -- THE END'S CHOICE: what the architecture itself fixes at a cusp point.

T1: the order bit is not a property of the oriented manifold (L re-marks LR as RL; b++LR and b++RL are m004 with orientation-preserving
isometries between them).  T2: the lines every isometry of m004 fixes are the meridian and the longitude (the fibre's boundary; the
fillings are S^3 and the Sol torus bundle), and m003's are (1, 0) and its fibre boundary (1, -2).  T3: a finite group of lattice
automorphisms fixes a line iff it has no rotation of order 3, 4 or 6; at a rotated cusp point the self-conjugate sector has no
symmetric completion, so a symmetric completion of the whole theory exists iff no cusp point is rotated, and is then non-chiral."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1504_the_ends_choice"
VER = ARC / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1504_end_choice", VER / "end_choice.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_lattice_lemma_on_every_finite_subgroup():
    rows = _load().lemma()
    assert len(rows) == 26
    assert all(r["rotation"] != r["common_line"] for r in rows)
    assert sum(r["rotation"] for r in rows) == 7


def test_the_puncture_live():
    E = _load()
    out = E.puncture()
    m4, m3 = out["m004"], out["m003"]
    assert sorted((r["orientation"], r["s_m"], r["s_l"]) for r in m4["rows"]) == sorted(
        [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)] * 2)
    assert [tuple(x) for x in m4["common_lines"]] == [(0, 1), (1, 0)] and tuple(m4["fibre_boundary"]) == (0, 1)
    f = m4["fillings_of_the_common_lines"]
    assert f["(1, 0)"]["pi1_generators"] == 0 and f["(1, 0)"]["H1"] == "0"
    assert f["(0, 1)"]["H1"] == "Z" and "flat" in f["(0, 1)"]["solution_type"] and f["(0, 1)"]["fibre_boundary"]
    assert [tuple(x) for x in m3["common_lines"]] == [(1, -2), (1, 0)] and tuple(m3["fibre_boundary"]) == (1, -2)
    f3 = m3["fillings_of_the_common_lines"]
    assert f3["(1, -2)"]["H1"] == "Z/5 + Z" and "flat" in f3["(1, -2)"]["solution_type"]
    assert f3["(1, 0)"]["H1"] == "Z/10"
    assert not m4["rotated"] and not m3["rotated"]
    ob = out["order_bit"]
    assert ob["LR_to_RL_isometries"] == 8 and ob["their_orientations"].count(1) == 4
    assert out["flow_class_sign"]["agree"]


def test_a_rotated_member_live():
    """o10_150725: cusps 0 and 2 are rotated by order 3 (hexagonal, the rotation permutes the three root lines, no line fixed);
    cusp 1 is not, and keeps two fixed lines"""
    import snappy
    d = _load().analyse(snappy.Manifold("o10_150725"), "o10_150725", canonical=True)
    assert d["crosscheck"]["agree"] and d["geometric_check"]["agree"]
    rows = {r["cusp"]: r for r in d["cusp_rows"]}
    for c in (0, 2):
        assert rows[c]["rotation_orders"] == [3] and rows[c]["common_lines"] == [] and rows[c]["rotation_permutes_roots"]
        assert rows[c]["hexagonal"]
    assert not rows[1]["rotated"] and len(rows[1]["common_lines"]) == 2
    assert not d["symmetric_self_dual_completion"]


def test_the_recorded_census():
    r = json.load(open(VER / "end_choice.json"))
    s = r["summary"]
    assert s["members"] == len(r["members"]) and s["arithmetic_family"] == 99
    assert s["crosscheck_failures"] == [] and s["geometric_failures"] == [] and s["lemma_violations"] == []
    assert set(s["rotation_orders_seen"]) <= {3, 6}                                   # B1390: no order 4 at a cusp
    assert s["rotated_all_hexagonal"] and s["rotation_permutes_roots_everywhere"]
    assert s["symmetric_self_dual_completion"] == s["members"] - len(s["with_rotated_points"])
    assert s["frame_chiral_allowed"] == s["symmetric_self_dual_completion"]
    labels = {m["label"] for m in r["members"]}
    assert {"m004", "m003", "cube~3.24"} <= labels
    by = {m["label"]: m for m in r["members"]}
    assert by["cube~3.24"]["rotated_points"] == 2 and not by["cube~3.24"]["symmetric_self_dual_completion"]
    assert by["m004"]["rotated_points"] == 0 and not by["m004"]["g2_chiral_allowed"] and by["m004"]["frame_chiral_allowed"]
    assert r["lemma"]["violations"] == 0
    # with a G2 orientation: allowed on exactly the unrotated members with no orientation-reversing isometry (123); on the 76
    # amphichiral ones the reversing isometries pair lower with upper -- 72 with every stabiliser reversing, 4 with net zero
    unrot = [m for m in r["members"] if m["rotated_points"] == 0]
    chiral = [m for m in unrot if m["orientation_reversing"] == 0]
    amph = [m for m in unrot if m["orientation_reversing"] > 0]
    assert (len(unrot), len(chiral), len(amph)) == (199, 123, 76) and s["g2_chiral_allowed"] == 123
    assert all(m["g2_chiral_allowed"] for m in chiral) and not any(m["g2_chiral_allowed"] for m in amph)
    paired = [m["label"] for m in amph if any(o["stabiliser_orientation_preserving"] for o in m["orbits"])]
    assert len(paired) == 4 and "o10_150685" in paired
    assert {o["weight_with_orientation"] for m in amph for o in m["orbits"] if o["stabiliser_orientation_preserving"]} == {0}


def test_the_findings_and_the_verdict():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    for s in ("Not sealed", "B979", "B1324", "B1083", "three root lines", "fibre's boundary", "never force"):
        assert s in f, s
    v = json.load(open(ARC / "arc_verdict.json"))
    assert v["id"] == "B1504" and v["verdict"] == "PROVED" and "0 of 19" in v["claim_one_line"]
