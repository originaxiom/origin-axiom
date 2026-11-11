#!/usr/bin/env python3
"""SM-C1, harvest row 1465 (PARALLEL_PHASE_CHIRAL_KERNEL_AND_LIGHT_RUNNING @ 1a4791de8): this seat's own check of
(7) the cusp pole bound (derived from the stated L2 integrand r^(a-2p-1)|log r|^(a-2)), (9) line dimensions on an
elliptic curve, the table N_j(L), j = 0..4, and the gauge/H3 counts, the order-seven roster 2(10+10bar)+4(5+5bar), the
dimensions 92 + 12 kappa and 12, the light beta coefficients (10, 4+2kappa, 1+3kappa) and (h21, h31), and the zero-Wilson
control. Lines: L ranges over {O, eta, X7} (eta of order two, X7 a unitary flat line of order seven); eta^2 = O.
Planted: the compact bound b(a) = floor(a/2) for every a must change the table and be caught."""
import json
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path


def bound_from_integrand(a):
    """the largest pole order p with r^(a-2p-1)|log r|^(a-2) integrable at r = 0: need a-2p-1 > -1, or a-2p-1 = -1 and
    a-2 < -1"""
    best = None
    for p in range(-20, 21):
        e = a - 2 * p - 1
        if e > -1 or (e == -1 and a - 2 < -1):
            best = p if best is None else max(best, p)
    return best


def bound_claimed(a):
    return math.floor(a / 2) if a <= 0 else math.ceil(a / 2) - 1


LINES = ["O", "eta", "X7"]
def mult(x, y):            # the group of lines {O, eta} x <X7> restricted to what occurs: we track (eta-part, X7-power)
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 7)
REP = {"O": (0, 0), "eta": (1, 0), "X7": (0, 1)}
def trivial(F):
    return F == (0, 0)
def power(F, n):
    return ((F[0] * n) % 2, (F[1] * n) % 7)


def h0(a, L, bound):
    """h0_L2(S^a L) = h0(X, eta^a L (b(a) p)) with H(d, F)"""
    d = bound(a)
    F = mult(power(REP["eta"], a), L)
    if d < 0:
        return 0
    if d == 0:
        return 1 if trivial(F) else 0
    return d


def inv(L):
    return ((-L[0]) % 2, (-L[1]) % 7)


def N(j, L, bound):
    return h0(j + 2, inv(L), bound) + h0(j + 1, L, bound) + h0(1 - j, L, bound)


def gauge(j, L, bound):
    return h0(-j, L, bound)


def H3(j, L, bound):
    return h0(-j, inv(L), bound)


out = {"pole_bound": {}, "table": {}, "planted": {}}
out["pole_bound"] = {str(a): [bound_from_integrand(a), bound_claimed(a)] for a in range(-6, 8)}
pb_ok = all(v[0] == v[1] for v in out["pole_bound"].values())
CLAIM = {0: {"O": 1, "eta": 2, "X7": 0}, 1: {"O": 3, "eta": 1, "X7": 1}, 2: {L: 2 for L in LINES},
         3: {L: 3 for L in LINES}, 4: {L: 4 for L in LINES}}
# the item: j=0: delta(L) + 2 delta(eta L); j=1: 1 + 2 delta(L)
tab_ok = True
for j in range(5):
    row = {}
    for Ln in LINES:
        L = REP[Ln]
        row[Ln] = {"N": N(j, L, bound_claimed), "gauge": gauge(j, L, bound_claimed), "H3": H3(j, L, bound_claimed)}
        tab_ok &= row[Ln]["N"] == CLAIM[j][Ln] and row[Ln]["gauge"] == row[Ln]["H3"]
        tab_ok &= row[Ln]["gauge"] == (1 if (j == 0 and Ln == "O") else 0)
        tab_ok &= N(j, L, bound_claimed) == N(j, inv(L), bound_claimed)
    out["table"][str(j)] = row
# the roster at the order-seven character: every nonzero charge |q| <= 6 gives L of order seven
order7 = all(math.gcd(2 * q, 7) == 1 for q in range(-6, 7) if q != 0)
X7 = REP["X7"]
kappa = {sp_: N(0, REP["O"], bound_claimed) if sp_ == "trivial" else None for sp_ in ("trivial",)}
mult_10 = N(2, X7, bound_claimed)                                           # 5_b = V2
mult_5 = N(1, X7, bound_claimed) + N(3, X7, bound_claimed)                  # 10_b = V1 + V3
singlets = sum(N(j, REP["O"], bound_claimed) for j in (1, 2, 3, 4))         # 24_b = V1 + V2 + V3 + V4, L = O
mixed_24 = N(0, X7, bound_claimed)                                          # charge +-5 directions of 24_g
dims_ok = (3 + 7 == 10) and (3 + 5 + 7 + 9 == 24)
out["roster"] = {"order7_for_all_nonzero_charges": order7, "mult_10": mult_10, "mult_5": mult_5,
                 "gauge_singlets_from_24b": singlets, "mixed_24g_charge5": mixed_24, "principal_dims_ok": dims_ok}
res = {}
for spin, eta_triv in (("trivial", True), ("nontrivial", False)):
    # kappa = N_0 on the charge-zero directions = delta(O) + 2 delta(eta), delta(eta) = 1 iff the spin line is trivial
    kap = 1 + (2 if eta_triv else 0)
    chiral_dim = mult_10 * 20 + mult_5 * 10 + 12 * kap + singlets
    T = {"10": Fr(3, 2), "5": Fr(1, 2)}
    complete = mult_10 * 2 * T["10"] + mult_5 * 2 * T["5"]
    b = [complete + 0, complete + 2 * kap - 6, complete + 3 * kap - 9]
    res[spin] = {"kappa": kap, "chiral_dim": chiral_dim, "claimed_chiral_dim": 92 + 12 * kap, "b": [str(x) for x in b],
                 "claimed_b": [10, 4 + 2 * kap, 1 + 3 * kap], "h21_h31": [str(b[1] - b[0]), str(b[2] - b[0])]}
out["beta"] = res
beta_ok = all(r["chiral_dim"] == r["claimed_chiral_dim"] and [Fr(x) for x in r["b"]] == [Fr(y) for y in r["claimed_b"]]
              for r in res.values())
# zero-Wilson control: every L = O
zw = {"mult_5": N(1, REP["O"], bound_claimed) + N(3, REP["O"], bound_claimed), "mult_10": N(2, REP["O"], bound_claimed)}
out["zero_wilson"] = zw
zw_ok = zw == {"mult_5": 6, "mult_10": 2}
ros_ok = order7 and mult_10 == 2 and mult_5 == 4 and singlets == 12 and mixed_24 == 0 and dims_ok
# planted: the compact bound floor(a/2) for every a
compact = lambda a: math.floor(a / 2)
changed = any(N(j, REP[Ln], compact) != CLAIM[j][Ln] for j in range(5) for Ln in LINES)
out["planted"] = {"compact_bound_changes_table": changed,
                  "N_with_compact_bound": {str(j): {Ln: N(j, REP[Ln], compact) for Ln in LINES} for j in range(5)}}
out["checks"] = {"pole_bound": pb_ok, "table": tab_ok, "roster": ros_ok, "beta": beta_ok, "zero_wilson": zw_ok}
out["all_claims_hold_and_plants_caught"] = bool(pb_ok and tab_ok and ros_ok and beta_ok and zw_ok and changed)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: out[k] for k in ("checks", "roster", "beta", "zero_wilson")}, indent=1),
      out["all_claims_hold_and_plants_caught"])
