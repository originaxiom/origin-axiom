"""What the deep-cusp law's leading order says about depth (chat1; arithmetic on the 19:41 per-field cusp law; the
data's six log-ratios are used, so this is a scoreboard, not a test)

The 19:41 law (refined post hoc, confirmed out of sample at excluded orders; twisted_units_seal.py's tower_law): on a
thread reaching height y, in C1 and the E4 cells, ln(m_i/m_3) = -2 pi y e_i + O(1), the O(1) offsets measured at 2-25
in ln on the towers. Per sector, e_2 = D-(d_L) + D-(d_R) and e_1 = Di(d_L) + Di(d_R), with d_f = dist(q_f lb / N) in
[0, 1/2] for the sector's two fields. From the law's unit exponents and shifts, by hand and checked below against the
law's own code:
  D-(d) = 1/2 (d <= 1/4), 3/4 - d (d >= 1/4);   Di(d) = 3/4 + d (d <= 1/4), 1 (d >= 1/4),
so e_2 lies in [1/2, 1] and e_1 in [3/2, 2] in every sector. Two read-outs at leading order (offsets ignored):
  (1) the depth each observed ratio needs on its own, y = -ln(ratio) / (2 pi e) over e's allowed range;
  (2) W66's predicate as W88 used it (z on ln ratio, a = 0.10), with one common depth fitted and every field's d free
      (a superset of every charge assignment, line and order).
The offsets move the needed depths by roughly 0.16-8, so neither read-out is decisive at shallow depth: the computed
masses (T-low, the replication, the mid-height scan) are what decide there.
Usage: python3 -B deep_law_pattern.py > deep_law_pattern_run.txt
"""
import itertools, json, math, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units")

PU = {"F_i": (Fr(-7, 8), Fr(7, 8), Fr(3, 8)), "F+": (Fr(1, 8), Fr(-1, 8), Fr(3, 8)), "F-": (Fr(1, 8), Fr(7, 8), Fr(-5, 8))}
dist = lambda x: min(x % 1, 1 - x % 1)


def g(u, al):                                    # the law's growth, as in tower_law()
    pe, pp, pm = PU[u]; s2 = dist(al + Fr(1, 2)) ** 2 - Fr(1, 4); s34 = dist(al) ** 2
    return max(0, -(pe + s2), -(pp + s34), -(pm + s34))


def Dm(d): return Fr(1, 2) if d <= Fr(1, 4) else Fr(3, 4) - d
def Di(d): return Fr(3, 4) + d if d <= Fr(1, 4) else Fr(1)


# check the closed forms against the law's own code on a fine grid
bad = 0
for k in range(0, 1001):
    al = Fr(k, 2000)
    d = dist(al)
    bad += (g("F-", al) - g("F+", al) != Dm(d)) + (g("F_i", al) - g("F+", al) != Di(d))
print(f"closed forms D-(d), Di(d) against the law's code on 1001 points: {bad} mismatches")

hz = json.load(open(os.path.join(TU, "received_HZ2021_running_masses_MZ.json")))
MV, MS = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
SEC = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
data = {}
for s, (f1, f2, f3) in SEC.items():
    data[s] = [(math.log(MV[f1] / MV[f3]), math.hypot(MS[f1] / MV[f1], MS[f3] / MV[f3])),
               (math.log(MV[f2] / MV[f3]), math.hypot(MS[f2] / MV[f2], MS[f3] / MV[f3]))]


def best_fit(dset):
    """minimum over the fields' d (Q shared by up and down) and one common kappa = 2 pi y, of W66's chi^2 on ln ratio"""
    best = (float("inf"), None, None)
    for dQ, du, dd, dL, de in itertools.product(dset, repeat=5):
        e = {"up": (Di(dQ) + Di(du), Dm(dQ) + Dm(du)), "down": (Di(dQ) + Di(dd), Dm(dQ) + Dm(dd)),
             "lepton": (Di(dL) + Di(de), Dm(dL) + Dm(de))}
        rows = [(float(e[s][i]), data[s][i][0], math.hypot(data[s][i][1], 0.10)) for s in SEC for i in (0, 1)]
        kappa = -sum(ei * li / sd ** 2 for ei, li, sd in rows) / sum(ei * ei / sd ** 2 for ei, li, sd in rows)
        chi = sum(((-kappa * ei - li) / sd) ** 2 for ei, li, sd in rows)
        if chi < best[0]:
            best = (chi, kappa, (dQ, du, dd, dL, de))
    return best


print("(1) the depth each observed ratio needs on its own at leading order, y = -ln(ratio) / (2 pi e):")
for sname in SEC:
    for i, (lo, hi) in ((0, (1.5, 2.0)), (1, (0.5, 1.0))):
        l = data[sname][i][0]
        print(f"  {sname:6s} m{i + 1}/m3 (ln = {l:+.2f}): y in [{-l / (2 * math.pi * hi):.2f}, {-l / (2 * math.pi * lo):.2f}]")
print("(2) one common depth, W66's chi^2 at leading order (threshold 12.592):")
for N in (9, 11, 12):
    dset = sorted({dist(Fr(r, N)) for r in range(N)})
    chi, kappa, ds = best_fit(dset)
    print(f"  N = {N}: best chi^2 {chi:.1f} at y = {kappa / (2 * math.pi):.3f}; fields' d (Q, u, d, L, e) = {[str(x) for x in ds]}")
grid = [Fr(k, 40) for k in range(21)]
chi, kappa, ds = best_fit(grid)
print(f"  any order (d on a grid of 1/40): best chi^2 {chi:.1f} at y = {kappa / (2 * math.pi):.3f}")
print("for reference: the modular surface's floor is y = 0.866; the shallowest thread, LR, reaches 1.118 and closes no line; T-low reaches 1.537 to 2.766")
