"""The refined per-field cusp law (POST HOC, from pf_towers.py's run): leading exponents of a dressed unit's growth."""
from fractions import Fraction as F
P_UNITS = {"F_i": (F(-7, 8), F(7, 8), F(3, 8)), "F+": (F(1, 8), F(-1, 8), F(3, 8)), "F-": (F(1, 8), F(7, 8), F(-5, 8))}
def dist(x):  # distance to nearest integer
    x = x % 1
    return min(x, 1 - x)
def growth(unit, al):
    pe, pp, pm = P_UNITS[unit]
    s2 = dist(al + F(1, 2)) ** 2 - F(1, 4); s34 = dist(al) ** 2
    return max(0, -(pe + s2), -(pp + s34), -(pm + s34))
def field(q, lb, N):
    al = F(q * lb, N)
    return {u: growth(u, al) for u in P_UNITS}
def sector(qL, qR, lb, N):
    L, R = field(qL, lb, N), field(qR, lb, N)
    m2 = (L["F-"] - L["F+"]) + (R["F-"] - R["F+"])
    m1 = (L["F_i"] - L["F+"]) + (R["F_i"] - R["F+"])
    return float(m2), float(m1)
if __name__ == "__main__":
    SM = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
    for N, lb in ((3, 1), (5, 1), (5, 2), (7, 1)):
        print(N, lb, {s: sector(a, b, lb, N) for s, (a, b) in SM.items()})
