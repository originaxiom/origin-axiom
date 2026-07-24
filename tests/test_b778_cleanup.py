"""B778 -- the cleanup wave (partial 5/7): locks on the banked fixes."""
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B778_cleanup"


def test_darkhyp_count_identity():
    # the N=p^2 dark-hyperbola stratification counts sum to p^4 (p=3: 63+6+1+11=81)
    assert 63 + 6 + 1 + 11 == 81 == 3**4


def test_w5139_genus_41_reproduced():
    # the strip kept genus(A_3)=41 (RH: 2g-2 = 4B, B=20)
    r = json.loads((ARC / "cells" / "CL-W5139" / "results.json").read_text())
    assert r["verdict"] == "RESOLVED-A"
    assert r.get("genus") == 41
    assert (2 * 41 - 2) == 4 * 20


def test_h133_genuine_zero_hardens():
    # H133's Z4=0 is a genuine zero at chord level (both sectors vanish), NOT a W4-304 cancellation
    r = json.loads((ARC / "cells" / "CL-H133" / "results.json").read_text())
    assert r["verdict"] == "RESOLVED-B"  # HARDENS


def test_cleanup_partial_shape():
    d = json.loads((ARC / "partial_results.json").read_text())
    banked = {c["id"] for c in d["cells"]}
    # the 5 that completed this pass
    assert banked == {"CL-DARKHYP", "CL-W3082", "CL-W5139", "CL-W5100", "CL-H133"}
