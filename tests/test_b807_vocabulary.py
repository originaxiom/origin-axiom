"""B807 — locks the orthogonality verdict against the SEALED thresholds."""
import importlib.util
import json
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B807_vocabulary_unification"
P_FLOOR, TOP5_CEIL = 60, 0.50          # sealed in prereg 40b7ff01274b4c01, not adjustable


def _m():
    spec = importlib.util.spec_from_file_location("b807", ARC / "joint.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_sealed_thresholds_are_unchanged():
    """If these ever move, the verdict was re-derived against different goalposts."""
    m = _m()
    assert m.P_FLOOR == P_FLOOR and m.TOP5_CEIL == TOP5_CEIL


def test_faces_and_motifs_are_orthogonal_not_redundant():
    m = _m()
    faces, motifs = m.load()
    pairs, both = m.joint(faces, motifs)
    P = len(pairs)
    tot = sum(pairs.values())
    top5 = sum(c for _, c in pairs.most_common(5)) / tot
    assert P >= P_FLOOR, f"populated pairs {P} fell below the sealed floor {P_FLOOR}"
    assert top5 <= TOP5_CEIL, f"top-5 share {top5:.3f} exceeded the sealed ceiling {TOP5_CEIL}"
    # the corroborator: near-zero mutual information => face tells you ~nothing about motif
    assert m.mutual_information(pairs) < 0.20


def test_zero_overlap_between_the_two_vocabularies_is_by_design():
    """The premise B806 found and B807 explains: no face is a motif, and that is correct."""
    m = _m()
    faces, motifs = m.load()
    face_names = {f for fs in faces.values() for f in fs}
    motif_names = {mo for ms in motifs.values() for mo in ms}
    assert face_names and motif_names
    assert not (face_names & motif_names), "an overlap appeared -- the axes have been conflated"


def test_observer_is_a_third_axis_touching_every_motif():
    m = _m()
    faces, motifs = m.load()
    hits, fc, mc = m.observer_spread(faces, motifs)
    assert len(hits) > 40
    assert len(mc) == 18, f"observer must cut across ALL motifs, touched {len(mc)}"
    assert len(fc) >= 4
