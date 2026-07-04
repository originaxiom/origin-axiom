import json, os
HERE=os.path.join(os.path.dirname(__file__),"..","frontier","B422_mirror_frame")
def test_z2_no_frame():
    R=json.load(open(os.path.join(HERE,"mirror_frame.json")))
    assert R["golden_overlap"]=="0" and R["golden_mirror_overlap"]=="0"
    assert R["frame_exists"] is False
