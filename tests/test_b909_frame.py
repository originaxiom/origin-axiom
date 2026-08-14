"""B909 locks: the CMT typing, kappa's identity, the frame dims."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B909_frame_arc")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_cmt_typing_five_pairs():
    r = _res()["cmt_typing"]
    assert len(r["pairs"]) == 5
    assert [p for p, _ in r["pairs"]].count(40039) == 3   # the fully-split prime
    assert (r["dim_z"], r["derived_ge"], r["z_cap_core"], r["center_by_count"]) \
        == (30, 28, 18, 2)


def test_kappa_wall_roots_vs_the_phantom():
    s = sp.Symbol("s")
    kappa = 2771822592000*s**3 + 3033676800*s**2 - 56402640*s - 6859
    # the corrected instrument's first pair is a genuine kappa root
    assert sp.Poly(kappa, s, modulus=40013).ground_roots()
    # the stale septic's "wall prime" 40031 has NO kappa roots -- the catch
    assert not sp.Poly(kappa, s, modulus=40031).ground_roots()


def test_debts_paid_recorded():
    r = _res()
    assert "six-cubic" in json.dumps(r) or "sqrt77" in json.dumps(r)
    assert "SMT-block" in json.dumps(r)
