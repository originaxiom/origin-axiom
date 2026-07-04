"""Locks for B416 TW2 -- the golden-Anosov destination, no SM."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B416_tw2_dynamics")


def test_void_jacobian_golden():
    R = json.load(open(os.path.join(HERE, "track_dynamics.json")))
    eigs = sorted(R["void_jacobian_eigs"])
    exp = sorted(R["banked_phi4_phi-4_1"])
    assert all(abs(a - b) < 1e-3 for a, b in zip(eigs, exp))


def test_trivial_coordinate_symmetry():
    R = json.load(open(os.path.join(HERE, "track_dynamics.json")))
    assert R["dynamical_symmetry_group_order"] == 1
