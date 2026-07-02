"""B363 -- the seam's lift anatomy: one-sided twists all dark; the committed scan artifact."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B363_seam_lift_anatomy')


def test_one_sided_twist_scan_all_dark():
    scan = json.load(open(os.path.join(HERE, 'lift_torus_scan.json')))
    assert len(scan) == 225
    assert all(v < 1e-6 for v in scan.values())          # 0/225 bright: one-sided twists never light the seam


def test_canonical_origin_dark():
    scan = json.load(open(os.path.join(HERE, 'lift_torus_scan.json')))
    assert scan["0,0"] < 1e-10                            # the canonical point itself
