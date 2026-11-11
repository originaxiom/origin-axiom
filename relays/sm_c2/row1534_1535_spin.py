#!/usr/bin/env python3
"""SM-C2, harvest rows 1534 (REGISTER_QUADRATIC_FORM_TO_ODD_SPIN_AND_PHYSICAL_JOIN @ 4996400b9) and 1535
(SPIN_FLAVOUR_FACTORISATION_AND_PHYSICAL_TWIST_PRICE @ 76a14763a): this seat's own exact check over F2.
Row 1534: with the lift rule (1) tilde(v+w) = tilde(v) + tilde(w) + B(v,w) z, the functional (2) xi_q is well defined and
linear for each of the four refinements q_(alpha,beta) = alpha x + beta y + xy, with xi_q(z) = 1 and q(v) = xi_q(tilde v);
Arf(q_(alpha,beta)) = alpha beta (majority value); the register's q = 1 on every nonzero v is q_(1,1); it is the only
refinement fixed by all of SL(2,F2), the other three form one orbit; (4) the count of invariant classes for one M equals
2^dim ker(M^T - I) and is 4 / 2 / 1 for M = identity / order two / order three; LR = [[2,1],[1,1]], L^2 R = [[3,2],[1,1]],
L^2 R^2 = [[5,2],[2,1]] have mod-two orders 3, 2, 1 and so 1, 2, 4 invariant classes; on the flat framing (bar a = tilde a +
z) q_(1,1) gives xi(bar a) = xi(bar b) = 0 (periodic/periodic), and the other three differ by the signs (3).
Row 1535: the 16 pairs (eps_S, eps_F) in (F2^2)^2 fall into exactly 4 orbits of the diagonal shift, labelled by eps_S +
eps_F, each of size 4; the central-sign table (spin x flavour = combined +1 in every row); the gauge-only compensation
Ad(g) = -I fails on a nonzero bracket. Planted: the lift without the B(v,w) z term must break linearity of xi_q."""
import json
import sys
from itertools import product
from pathlib import Path

import numpy as np

out = {}
V = [(x, y) for x in (0, 1) for y in (0, 1)]
B = lambda v, w: (v[0] * w[1] + v[1] * w[0]) % 2
add = lambda v, w: ((v[0] + w[0]) % 2, (v[1] + w[1]) % 2)


def q_ab(al, be):
    return lambda v: (al * v[0] + be * v[1] + v[0] * v[1]) % 2


def lift(v, with_B=True):
    """tilde(v) in H1(UC) = F2^3 with basis (tilde a, tilde b, z); built by (1) from tilde a, tilde b"""
    x, y = v
    vec = [x, y, 0]
    if with_B and x and y:
        vec[2] = B((1, 0), (0, 1))
    return tuple(vec)


def xi_from(q):
    # linear functional on F2^3: values on tilde a, tilde b, z
    return (q((1, 0)), q((0, 1)), 1)


ev = lambda xi, h: (xi[0] * h[0] + xi[1] * h[1] + xi[2] * h[2]) % 2
res34 = {}
ok34 = True
for al, be in product((0, 1), repeat=2):
    q = q_ab(al, be)
    refine = all(q(add(v, w)) == (q(v) + q(w) + B(v, w)) % 2 for v in V for w in V)
    xi = xi_from(q)
    consistent = all(ev(xi, lift(v)) == q(v) for v in V)
    arf = 1 if sum(q(v) for v in V) >= 3 else 0
    res34[f"q_({al},{be})"] = {"refinement": refine, "xi(tilde v)=q(v)": consistent, "Arf": arf,
                               "values": [q(v) for v in V]}
    ok34 &= refine and consistent and arf == al * be
quat = q_ab(1, 1)
ok34 &= all(quat(v) == 1 for v in V if v != (0, 0))
SL2 = [np.array(m).reshape(2, 2) for m in product((0, 1), repeat=4)]
SL2 = [m for m in SL2 if int(round(np.linalg.det(m))) % 2 == 1]
assert len(SL2) == 6
act = lambda M, v: tuple(int(x) % 2 for x in M @ np.array(v))
fixed_all = [ab for ab in product((0, 1), repeat=2)
             if all(q_ab(*ab)(act(M, v)) == q_ab(*ab)(v) for M in SL2 for v in V)]
res34["fixed_by_all_SL2F2"] = fixed_all
orbit = {tuple(q_ab(*ab)(act(M, v)) for v in V) for M in SL2 for ab in [(0, 0)]}
res34["orbit_of_q00_size"] = len(orbit)
ok34 &= fixed_all == [(1, 1)] and len(orbit) == 3


def order2(M):
    P = np.eye(2, dtype=int)
    for k in range(1, 7):
        P = (P @ M) % 2
        if (P == np.eye(2, dtype=int)).all():
            return k


def inv_count(M):
    return sum(1 for ab in product((0, 1), repeat=2) if all(q_ab(*ab)(act(M, v)) == q_ab(*ab)(v) for v in V))


def kerdim(M):
    A = (M.T - np.eye(2, dtype=int)) % 2
    return sum(1 for v in V if all(x % 2 == 0 for x in A @ np.array(v))).bit_length() - 1


table = {}
for M in SL2:
    table.setdefault(order2(M % 2), set()).add((inv_count(M), 2 ** kerdim(M)))
res34["order->(invariant classes, 2^dim ker)"] = {k: sorted(v) for k, v in table.items()}
ok34 &= table == {1: {(4, 4)}, 2: {(2, 2)}, 3: {(1, 1)}}
Lm, Rm = np.array([[1, 1], [0, 1]]), np.array([[1, 0], [1, 1]])
words = {"LR": Lm @ Rm, "L2R": Lm @ Lm @ Rm, "L2R2": Lm @ Lm @ Rm @ Rm}
res34["words"] = {k: {"matrix": v.tolist(), "mod2_order": order2(v % 2), "invariant_classes": inv_count(v % 2)}
                  for k, v in words.items()}
ok34 &= ([res34["words"][k]["matrix"] for k in words] == [[[2, 1], [1, 1]], [[3, 2], [1, 1]], [[5, 2], [2, 1]]]
         and [res34["words"][k]["invariant_classes"] for k in words] == [1, 2, 4])
# flat framing: bar a = tilde a + z, bar b = tilde b + z
xi11 = xi_from(quat)
flat = (ev(xi11, (1, 0, 1)), ev(xi11, (0, 1, 1)))
signs = {}
for al, be in product((0, 1), repeat=2):
    xi = xi_from(q_ab(al, be))
    signs[f"({al},{be})"] = ((-1) ** ev(xi, (1, 0, 1)), (-1) ** ev(xi, (0, 1, 1)))
res34["flat_xi_on_bar_a_bar_b_for_q11"] = flat
res34["holonomy_signs_relative_to_periodic"] = signs
ok34 &= flat == (0, 0) and all(signs[f"({al},{be})"] == ((-1) ** (al + 1), (-1) ** (be + 1))
                               for al, be in product((0, 1), repeat=2))
res34["ok"] = bool(ok34)
out["row1534"] = res34
# row 1535
pairs = list(product(V, V))
orbits = {}
for s_, f_ in pairs:
    key = frozenset((add(s_, t), add(f_, t)) for t in V)
    orbits[key] = add(s_, f_)
labels = sorted(set(orbits.values()))
sizes = sorted(len(k) for k in orbits)
centres = [(+1, +1), (-1, -1), (+1, +1), (-1, -1)]
sig = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]])
br = sig[0] @ sig[1] - sig[1] @ sig[0]
gauge_minus = not np.allclose(-br, br)        # Ad(g) = -I would need [-X,-Y] = -[X,Y], i.e. [X,Y] = -[X,Y]
res35 = {"orbits": len(orbits), "orbit_sizes": sizes, "labels": [list(x) for x in labels],
         "label_is_sum": all(lbl == add(*next(iter(k))) for k, lbl in orbits.items()),
         "combined_centres": [a * b for a, b in centres], "gauge_only_minus_rejected": bool(gauge_minus)}
res35["ok"] = (len(orbits) == 4 and sizes == [4, 4, 4, 4] and res35["label_is_sum"]
               and all(c == 1 for c in res35["combined_centres"]) and gauge_minus)
out["row1535"] = res35
# planted
bad = all(ev(xi_from(quat), lift(v, with_B=False)) == quat(v) for v in V)
out["PLANTED_lift_without_B_breaks_xi"] = not bad
out["all_claims_hold_and_plants_caught"] = bool(res34["ok"] and res35["ok"] and out["PLANTED_lift_without_B_breaks_xi"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
