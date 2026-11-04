"""Main's own check (2026-11-04): with B1656's a0_of (b1656_funcs, B1691's correction folder), is a0's oddness between
sectors the same fact as its oddness under w -> -w? Checks a0_up(w) = -a0_down(w), a0_lep(w) = a0_down(w),
a0_up(w) = a0_down(-w), a0_down(-w) = -a0_down(w), on lines off slopes 2/5 and 3/5, at two tau, all four channels."""
import sys, pathlib
ROOT = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"))
import b1656_funcs as B
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
def a0(line, tau, s, w_sign=1):
    w = w_sign * B.line_w(line[0], line[1], tau); x, y = B.sector_twists(w, tau, *SECT[s]); R = B.residues(x, y, tau)
    return B.a0_of(x, y, tau, R)
worst = {k: 0.0 for k in ("up+down", "down-lep", "up(w)-down(-w)", "down(w)+down(-w)")}; n = 0
for tau in (complex(0.13, 2.2), complex(0.37, 1.7)):
    for line in ((1/7, 2/7), (1/3, 1/6), (3/10, 1/5), (5/11, 2/11)):
        u, d, l = a0(line, tau, "up"), a0(line, tau, "down"), a0(line, tau, "lepton"); dm = a0(line, tau, "down", -1)
        for k in B.UNITS:
            if None in (u[k], d[k], l[k], dm[k]): continue
            sc = max(1.0, abs(d[k])); n += 1
            worst["up+down"] = max(worst["up+down"], abs(u[k] + d[k]) / sc)
            worst["down-lep"] = max(worst["down-lep"], abs(d[k] - l[k]) / sc)
            worst["up(w)-down(-w)"] = max(worst["up(w)-down(-w)"], abs(u[k] - dm[k]) / sc)
            worst["down(w)+down(-w)"] = max(worst["down(w)+down(-w)"], abs(d[k] + dm[k]) / sc)
print(n, "channel values;", {k: "%.1e" % v for k, v in worst.items()})
