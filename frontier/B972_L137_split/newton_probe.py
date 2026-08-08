#!/usr/bin/env python3
"""B972 SCOUT -- per-prime p-adic Newton analysis of a cubic under the ONLY
freedom a pencil cubic has: reparameterising the pencil, t -> t/c, c in Q*.

Coefficient of s^d picks up a^(3-d) b^d for c = a/b, so the p-adic valuation
vector (v_p(a_3),...,v_p(a_0)) is transformed by w_d = v_p(a_d) + (3-d)*g,
g = v_p(a) - v_p(b) in Z, then the content (the min) is divided out.  g may
be chosen INDEPENDENTLY for each prime, since c ranges over all of Q*.

Consequences computed here:
  - which primes can be pushed out of BOTH extreme coefficients,
  - which primes can be made to vanish from the polynomial entirely,
  - whether the WHOLE B947 pattern can be dialled on/off by choosing c.
"""
import itertools
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
G = range(-10, 11)          # the tilt range scanned per prime


def prime_set(co):
    S = set()
    for c in co:
        if c != 0:
            S |= set(int(q) for q in sp.factorint(abs(int(c))))
    return sorted(S)


def valvec(co, p):
    return [sp.multiplicity(p, abs(int(c))) if c != 0 else 10**9 for c in co]


def loc(v, g):
    """where p sits after tilt g: (in lead, in mid, in const)."""
    w = [v[0], v[1] + g, v[2] + 2 * g, v[3] + 3 * g]
    m = min(w)
    w = [x - m for x in w]
    return (w[0] > 0, any(x > 0 for x in w[1:3]), w[3] > 0)


def analyse(co, name):
    co = [sp.Integer(c) for c in co]
    rows = {}
    for p in prime_set(co):
        v = valvec(co, p)
        states = {g: loc(v, g) for g in G}
        rows[p] = {
            "val_d3210": [int(x) for x in v],
            "reachable_states": sorted(set(states.values())),
            "can_avoid_both_extremes": any((not a) and (not c) for a, b, c in states.values()),
            "can_vanish_entirely": any((not a) and (not b) and (not c) for a, b, c in states.values()),
            "forced_into_an_extreme": not any((not a) and (not c) for a, b, c in states.values()),
        }
    return {"name": name, "primes": rows}


def best_normalisation(co, name):
    """Choose g_p independently per prime to try to SATISFY the B947 pattern."""
    co = [sp.Integer(c) for c in co]
    P = prime_set(co)
    per = {}
    for p in P:
        v = valvec(co, p)
        per[p] = sorted(set(loc(v, g) for g in G))
    best = None
    n_hold = 0
    total = 1
    for p in P:
        total *= len(per[p])
    for combo in itertools.product(*[per[p] for p in P]):
        lead = [p for p, s in zip(P, combo) if s[0]]
        mid = [p for p, s in zip(P, combo) if s[1]]
        const = [p for p, s in zip(P, combo) if s[2]]
        midonly = [p for p in mid if p not in lead and p not in const]
        holds = len(lead) <= 2 and len(const) <= 2 and len(midonly) >= 1
        if holds:
            n_hold += 1
            if best is None:
                best = {"P_lead": lead, "P_mid_only": midonly, "P_const": const}
    return {"name": name, "n_state_combinations": total,
            "n_combinations_satisfying_B947_pattern": n_hold,
            "an_example_that_holds": best,
            "PATTERN_IS_REACHABLE_BY_RENORMALISATION": n_hold > 0}


FAMS = [
    ([500716339200, -159667200, -28224, 1], "mu  @ B866's own pencil parameter t"),
    ([500716339200, -2075673600, -4769856, 2197], "mu  @ B941/B947's rho = 13t"),
    ([2771822592000, 3033676800, -56402640, -6859], "kappa @ B910's pencil parameter s"),
    ([824843587681, -27609909080832, 264084438122496, -760840571584512], "V hierarchy (VALUE)"),
    ([5308416, 9123840, 5077008, 908209], "d_S twist (VALUE)"),
]

OUT = {"newton": [], "reachability": []}
for co, nm in FAMS:
    a = analyse(co, nm)
    OUT["newton"].append(a)
    print(f"=== {nm}")
    for p, d in a["primes"].items():
        print(f"   p={p:<8} v(d=3,2,1,0)={str(d['val_d3210']):<20} "
              f"forced_into_an_extreme={d['forced_into_an_extreme']} "
              f"can_vanish={d['can_vanish_entirely']}")
    b = best_normalisation(co, nm)
    OUT["reachability"].append(b)
    print(f"   --> pattern reachable by renormalisation: "
          f"{b['PATTERN_IS_REACHABLE_BY_RENORMALISATION']} "
          f"({b['n_combinations_satisfying_B947_pattern']}/{b['n_state_combinations']} states)")
    if b["an_example_that_holds"]:
        print(f"       example: {b['an_example_that_holds']}")
    print()

(HERE / "newton_probe_out.json").write_text(json.dumps(OUT, indent=1) + "\n")
