"""Locks for B427 -- the twisted exchange trace: base identity, Q-multiplicities, the corrected
projector corollary (C' = sigma_17(C) != C), and the exchange-fixes-sqrt-15 law."""
import json, os, sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B427_cpt_exchange_trace")
sys.path.insert(0, HERE)
import cpt_trace as CT

R = json.load(open(os.path.join(HERE, "cpt_trace.json")))


def test_q_multiplicities():
    m = CT.q_multiplicities()
    assert (m["plus1"], m["minus1"], m["plus_i"], m["minus_i"]) == (57, 56, 56, 56)
    assert m["fixed"] == 1 and m["four_cycles"] == 56


def test_seam_traces_differ_the_q3_step_fails():
    _, _, C, Cp = CT.seam_traces()
    # C = zeta60^4 (= zeta15), C' = zeta60^8 (= zeta15^2): slots 4 and 8, and NOT equal
    assert [i for i, x in enumerate(C) if x] == [4]
    assert [i for i, x in enumerate(Cp) if x] == [8]
    assert C != Cp          # Chat-1's tr(Q^3 A)=tr(Q A) step is false; corollary corrected


def test_exchange_is_galois_and_fixes_sqrt15():
    ks, act = CT.galois_exchange_elements()
    assert ks == [17, 47]
    assert act["on_i"] == "fix"
    assert act["on_sqrt5"] == "flip" and act["on_sqrtm3"] == "flip"
    assert act["on_sqrtm15"] == "fix"   # the physical seam channel is exchange-symmetric
