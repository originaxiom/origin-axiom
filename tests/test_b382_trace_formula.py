"""Locks for B382 leg 1 — the phase-ratio law (banked trace_formula.json)."""

import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B382_why_one_twelfth")
R = json.load(open(os.path.join(HERE, "trace_formula.json")))


def test_phase_ratio_law_on_domain():
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        assert R[w]["pure_phase"] is True and R[w]["quadratic"] is True


def test_domain_boundary_words_fail_as_classical():
    for w in ("1,3", "3,1"):
        assert R[w]["pure_phase"] is False


def test_universal_linear_part():
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        assert R[w]["Q"][3] == 7 and R[w]["Q"][4] == 8


CAN = json.load(open(os.path.join(HERE, "canonical_check.json")))


def test_leg2_canonical_linear_part_vanishes():
    for w, r in CAN.items():
        assert r["quadratic"] is True and r["Q"][3:] == [0, 0]


def test_leg2_quadratic_parts_match_theta():
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        assert CAN[w]["Q"][:3] == R[w]["Q"][:3]


def test_leg2_closed_form_fit():
    # Q_quad = 2^-1 * v^T J (gamma-I)^-1 v  and s = -2^-1, alpha decoded exactly
    from math import gcd
    for w in ("1,0", "0,1", "1,1", "2,1", "2,3"):
        (g00, g10), (g01, g11) = R[w]["gamma_cols"]
        g = [[g00, g01], [g10, g11]]
        det = ((g[0][0]-1)*(g[1][1]-1) - g[0][1]*g[1][0]) % 15
        assert gcd(det, 15) == 1
        di = pow(det, -1, 15)
        mi = [[(g[1][1]-1)*di % 15, -g[0][1]*di % 15],
              [-g[1][0]*di % 15, (g[0][0]-1)*di % 15]]
        JM = [[mi[1][0] % 15, mi[1][1] % 15], [-mi[0][0] % 15, -mi[0][1] % 15]]
        A, B, C = R[w]["Q"][:3]
        assert (8*JM[0][0]) % 15 == A
        assert (8*(JM[0][1]+JM[1][0]) + 7) % 15 == B
        assert (8*JM[1][1]) % 15 == C
