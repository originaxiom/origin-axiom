"""B1472 -- six of the lane's claims read against main: the three cells re-checked from their stored results, and the two
dated facts the readings rest on (B98's polynomial; B1224's own derivation) asserted on the files themselves."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1472_six_of_the_lanes_claims_read_against_main", "verification")


def test_cells_stored():
    d = json.load(open(os.path.join(V, "cells.json")))
    a = d["A_sign_law"]; assert a["n_closed"] == 150 and a["n_cusped"] == 150 and a["max_closed"] < 1e-12 and a["max_cusped"] < 1e-12
    b = d["B_L194_200"]; assert b["zero"] == 200 and b["quarter"] == 0 and b["other"] == 0 and b["errors"] == 0
    c = d["C_bianchi_covolumes"]
    assert abs(float(c["index_PSL"]) - 12) < 1e-6 and abs(float(c["index_PGL"]) - 24) < 1e-6 and abs(float(c["gieseking_over_PGL"]) - 12) < 1e-6
    assert c["L_chi_minus3_2"].startswith("0.7813024128")


def test_the_dated_facts_are_on_the_files():
    b98 = open(os.path.join(ROOT, "frontier", "B98_geometric_jacobian", "FINDINGS.md"), encoding="utf-8").read()
    assert re.search(r"t\s*\^?\s*2\s*[-−]\s*5\s*t\s*\+\s*1", b98) or "5 t + 1" in b98
    b1224 = open(os.path.join(ROOT, "frontier", "B1224_amphichiral_cs_torsion", "FINDINGS.md"), encoding="utf-8").read()
    assert "2-torsion" in b1224 and ("CS ≡ −CS" in b1224 or "CS = −CS" in b1224)
    b742 = open(os.path.join(ROOT, "frontier", "B742_negatives_hunt_p1", "FINDINGS.md"), encoding="utf-8").read()
    assert b742.count("| **RECONFIRMED**") == 30 and b742.count("| **REVIVED**") == 2


def test_covolume_live():
    from mpmath import mp, mpf, zeta, pi
    mp.dps = 30
    L = (zeta(2, mpf(1) / 3) - zeta(2, mpf(2) / 3)) / 9
    vol_psl = mpf(3) ** mpf("1.5") * zeta(2) * L / (4 * pi ** 2)
    assert abs(vol_psl - mpf("0.1691569344016089375")) < 1e-15
    assert abs(mpf("2.0298832128193072500") / vol_psl - 12) < 1e-9
