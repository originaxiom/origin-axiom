#!/usr/bin/env python3
"""THE RELATIONS THE CHAIN FORCES AMONG THE 19: the explicit cubic (B1275) read through the descent's SM
labels (B1252/B1253) -- every operator of the E6 superpotential on the 27, with its coefficient.

RESULT: all 45 operators carry the SAME coupling (|d| = 1 on every component triple): one Yukawa lambda for the
up quarks, the down quarks, the charged leptons and the Dirac neutrinos (SO(10)-type unification y_u = y_d = y_e
= y_nu at the object's scale), the same lambda for the mu-term S H_u H_d and the exotic mass S D Dbar (the
E6SSM structure: mu = m_D = lambda <S>), and the same lambda on the 24 colour-triplet (proton-decay) operators.
With the three generations of Y_3 (B1273) the generation structure is the zero-diagonal |eps_ijk|.  So the
chain reduces the Yukawa block (9 charged masses + 3 Dirac neutrino masses + mu + m_D) to ONE coupling times the
VEV data (v_u^i, v_d^i, <S>) times the diagonal source it lacks -- and forces the relations
m_b = m_tau, m_s = m_mu, m_d = m_e (and m_u : m_c : m_t = the Dirac neutrino masses) at its scale.
"""
from __future__ import annotations
import os, sys, itertools, collections
from fractions import Fraction as F
import importlib.util, pathlib
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'frontier' / 'B1267_spectrum_law_rebuilt' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1275_the_cubic_made_explicit' / 'verification'))
import cubic_explicit as C


def sm_labels():
    spec = importlib.util.spec_from_file_location("sm_sector", ROOT / 'frontier' / 'B1253_generation_count' / 'verification' / 'sm_sector.py')
    sm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sm)
    hy, (one, ten, sixteen), wts = sm.hypercharges()
    NAME16 = {F(1, 6): "Q", F(-2, 3): "u^c", F(1, 3): "d^c", F(-1, 2): "L", F(1): "e^c", F(0): "nu^c"}
    NAME10 = {F(1, 2): "H_u", F(-1, 2): "H_d", F(-1, 3): "D", F(1, 3): "Dbar"}
    lab = {}
    for i in range(27):
        if i in sixteen:
            lab[i] = NAME16[hy[i]]
        elif i in ten:
            lab[i] = NAME10[hy[i]]
        else:
            lab[i] = "S"
    return lab, hy, wts


def main():
    wts, rep = C.load()
    triples, idx, ns = C.solve_cubic(wts, rep)
    assert len(ns) == 1
    v = ns[0]
    scale = min(abs(x) for x in v if x != 0)
    vec = [sp.nsimplify(x / scale) for x in v]
    lab, hy, wts2 = sm_labels()
    assert wts2 == wts
    counts = collections.Counter(lab.values())
    print(f"  the 27 by SM label: {dict(sorted(counts.items()))}")
    ops = collections.defaultdict(list)
    for j, t in enumerate(triples):
        ops[tuple(sorted(lab[i] for i in t))].append(vec[j])
    print("  operator (from the 45 zero-sum triples) : component triples : d-values")
    order = [("H_u", "Q", "u^c"), ("H_d", "Q", "d^c"), ("H_d", "L", "e^c"), ("H_u", "L", "nu^c"), ("H_d", "H_u", "S"), ("D", "Dbar", "S")]
    seen = set()
    for key in order + sorted(k for k in ops if k not in order):
        key = tuple(sorted(key))
        if key in seen or key not in ops:
            continue
        seen.add(key)
        vals = collections.Counter(ops[key])
        print(f"    {' '.join(key):22s} : {len(ops[key]):2d} : {dict(vals)}")
    total = sum(len(v_) for v_ in ops.values())
    all_unit = all(abs(x) == 1 for v_ in ops.values() for x in v_)
    yuk = {k: len(ops[k]) for k in [tuple(sorted(o)) for o in order[:4]]}
    mu = len(ops[tuple(sorted(("H_d", "H_u", "S")))])
    mD = len(ops[tuple(sorted(("D", "Dbar", "S")))])
    exotic = total - sum(yuk.values()) - mu - mD
    print(f"  totals: SM Yukawas {sum(yuk.values())} (6 + 6 + 2 + 2), mu-term {mu}, exotic mass {mD}, colour-triplet operators {exotic}; all coefficients +-1: {all_unit}")
    print("  -> ONE coupling lambda: y_u = y_d = y_e = y_nu (each generation), mu = m_D = lambda <S>; the 24 colour-triplet couplings carry the same lambda")
    ok = all_unit and yuk == {tuple(sorted(("H_u", "Q", "u^c"))): 6, tuple(sorted(("H_d", "Q", "d^c"))): 6, tuple(sorted(("H_d", "L", "e^c"))): 2, tuple(sorted(("H_u", "L", "nu^c"))): 2} and mu == 2 and mD == 3 and exotic == 24 and total == 45
    # the relations against the data, with the accepted running quoted as an INPUT (not sealed, not a crossing)
    print("\n  relations at the object's scale and the low-energy data (running is an accepted-physics input; no crossing sealed):")
    data = {"m_b / m_tau": 4.18 / 1.77686, "m_s / m_mu": 0.093 / 0.10566, "m_d / m_e": 0.00467 / 0.000511, "m_t / m_b": 172.76 / 4.18}
    for k, val in data.items():
        print(f"    {k} (low energy) = {val:.2f}   chain: = 1 at its scale{'  (with tan beta = v_u/v_d free: m_t/m_b = tan beta)' if 't' in k else ''}")
    return ok


if __name__ == "__main__":
    print("=== every operator of the E6 cubic on the 27, labelled by the descent, with its coefficient ===")
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
