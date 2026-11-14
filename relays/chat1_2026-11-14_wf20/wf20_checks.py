#!/usr/bin/env python3
"""W-F20: what B1936's parity premise needs, made countable. Data-free; this seat's own code; no frame value.

    python3 -I -u wf20_checks.py

DEFINITIONS
  The five matter fields with the frame's 6Y (B1936's degrees.py): Q 1, u^c -4, d^c 2, L -3, e^c 6. Charge class
  c = 2 * (6Y) mod 5 (B1936's degree mod 5). Sectors: up (Q, u^c), down (Q, d^c), leptons (L, e^c); a sector's Higgs
  class is h = -(c_a + c_b) mod 5. A "parity" is a function f: {1, 2, 3, 4} -> {0, 1} that conjugation flips:
  f(k) + f(5 - k) = 1. The rule (B1936's premise): a sector reads S when f(its Higgs class) = matter's parity, else S~.
  Main's charge rule (P-847): the up sector's reading is the conjugate of the down and lepton sectors'.

EXPECTATIONS, written before the run:
  E1  Of the four conjugation-odd parities, exactly two put all five matter fields in one class (they are each other's
      complement). Each gives (up S~, down S, leptons S) for both signs of the hypercharge convention.
  E2  So the outcome does not depend on which conjugation-odd parity is used: B1936's exterior degree is one of the two.
      The premise is equivalent to: holomorphy is a function of the level-5 charge class, and matter's classes are the
      holomorphic ones.
  E3  The other lift. If the Higgs enters as an operator of degree +1 (H, class 1) or -1 (H~, class 4), as the vector of
      SO(10) acts on its spinor Lambda*(C^5), both Higgs components have odd degree. The rule then gives (S~, S~, S~),
      which breaks the charge rule. So the premise also needs the Higgs to be a state of degree 1 or 4, not an operator
      of degree +-1.
  Plant: a "parity" that conjugation does not flip (f = 0 everywhere) fails the conjugation test.
"""
from itertools import product

Y6 = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6}
SECT = {"up": ("Q", "u^c"), "down": ("Q", "d^c"), "lep": ("L", "e^c")}
W_MINUS = {"up": "S~", "down": "S", "lep": "S"}


def say(*a):
    print(*a, flush=True)


def conj_odd(f):
    return all(f[k] + f[5 - k] == 1 for k in (1, 2, 3, 4))


def world(f, sign, higgs_parity=None):
    c = {x: (2 * sign * y) % 5 for x, y in Y6.items()}
    ps = {f[c[x]] for x in c}
    if len(ps) != 1:
        return None
    mp = ps.pop()
    out = {}
    for s, (a, b) in SECT.items():
        h = (-(c[a] + c[b])) % 5
        hp = f[h] if higgs_parity is None else higgs_parity(h)
        out[s] = "S" if hp == mp else "S~"
    return out


fs = [dict(zip((1, 2, 3, 4), bits)) for bits in product((0, 1), repeat=4)]
odd = [f for f in fs if conj_odd(f)]
good = [f for f in odd if world(f, 1) is not None]
say("conjugation-odd parities:", len(odd), "| with matter in one class:", len(good), good)
e1 = len(odd) == 4 and len(good) == 2 and all(world(f, s) == W_MINUS for f in good for s in (1, -1)) and \
    all(good[0][k] + good[1][k] == 1 for k in (1, 2, 3, 4))
for f in good:
    say("  parity", f, "| world, hypercharge sign +1:", world(f, 1), "| sign -1:", world(f, -1))
deg = {k: k % 2 for k in (1, 2, 3, 4)}  # B1936's exterior degree in 0..5
e2 = deg in good
say("E1 holds:", e1, "| E2 (B1936's degree parity is one of them):", e2)
# E3: the operator lift: class 1 -> degree +1, class 4 -> degree -1; both odd
op = world(deg, 1, higgs_parity=lambda h: {1: 1, 4: 1}.get(h, deg[h]))
charge_ok = (op["up"] != op["down"]) and (op["down"] == op["lep"])
e3 = op == {"up": "S~", "down": "S~", "lep": "S~"} and not charge_ok
say("operator lift:", op, "| obeys the charge rule:", charge_ok, "| E3 holds:", e3)
plant = {k: 0 for k in (1, 2, 3, 4)}
say("plant (f = 0) passes the conjugation test:", conj_odd(plant), "| caught:", not conj_odd(plant))
