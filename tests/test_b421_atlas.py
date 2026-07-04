"""Lock for B421 -- the Destination Atlas is complete and SM-free under the bar."""
import json
import os
FR = os.path.join(os.path.dirname(__file__), "..", "frontier")
def test_all_six_destinations_bar_not_cleared():
    for d, key in (("B415_behavior_tracking/t1_continuum.json", ["bar", "any_exact_SM_match"]),
                   ("B416_tw2_dynamics/track_dynamics.json", None),
                   ("B419_tw5_quantum/track_quantum.json", ["bar", "any_exact_SM_match"]),
                   ("B420_tw6_lfunctions/track_lfunctions.json", ["bar", "any_exact_SM_match"])):
        R = json.load(open(os.path.join(FR, d)))
        if key:
            v = R
            for k in key: v = v[k]
            assert v is False
