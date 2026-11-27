#!/usr/bin/env python3
"""SM-R612, post hoc (written after the sealed run read its output; disclosed on the page).  The sealed run.py marks a
mass as zero only when a singular value is exactly 0.  Two of its rows instead carry a lightest singular value at
machine zero (about 1e-16 of the heaviest), so their ln(m1/..) entries are rounding noise: PL5 (the T-law at delta = inf),
the end delta = inf, tau's Jacobian at delta = inf and, suspected, the Higgs menu's R.  This script prints the singular
values there (data-free: the frame's own ratios only) and re-reads those rows on the m2/m3 entries alone.
    python3 -B posthoc_numerical_zeros.py MAIN_CHECKOUT"""
import sys, math, pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run as R

ZERO = 1e-12          # a lightest/heaviest ratio below this is read as a numerical zero


def svs(Ys):
    return {s: np.linalg.svd(Ys[s], compute_uv=False) for s in R.SECS}


def main():
    R.load(sys.argv[1]); a, b = R.BASE_LINE
    for t in R.TAUS:
        k = "%.2f%+.2fi" % (t.real, t.imag)
        base = svs(R.frame(t, a, b, end="inf", raw=True))
        timg = svs(R.frame(t + 1, a, (b - a) % 1, end="inf", unreduced=True, raw=True))
        e4 = svs(R.frame(t, a, b, raw=True))
        for lab, S in (("delta=inf", base), ("delta=inf at T", timg), ("E4", e4)):
            print("%s %-15s m1/m3: %s" % (k, lab, " ".join("%s %.1e" % (s, S[s][2] / S[s][0]) for s in R.SECS)))
        d23 = max(abs(math.log(base[s][1] / base[s][0]) - math.log(timg[s][1] / timg[s][0])) for s in R.SECS)
        print("%s PL5 re-read on ln(m2/m3) only: max dev %.1e -> %s" % (k, d23, R.verdict(d23)))
        for h in R.HIGGS_MENU:
            S = svs(R.frame(t, a, b, higgs=h, raw=True))
            print("%s Higgs %-4s m1/m3: %s | lepton/down m2/m3 equal to %.1e" % (
                k, h, " ".join("%s %.1e" % (s, S[s][2] / S[s][0]) for s in R.SECS),
                abs(S["lep"][1] / S["lep"][0] - S["down"][1] / S["down"][0])))
        # the end menu with delta = inf kept on ln(m2/m3) only
        vs = []
        for e in R.ENDS:
            S = svs(R.frame(t, a, b, end=e, raw=True)); vs.append([math.log(S[s][1] / S[s][0]) for s in R.SECS])
        print("%s end menu on the three ln(m2/m3): %d images of 7" % (k, R.image_count(vs, [0, 1, 2])))
        # tau's Jacobian at delta = inf on ln(m2/m3) only
        def f(p):
            S = svs(R.frame(complex(p[0], p[1]), a, b, end="inf", raw=True))
            return np.array([math.log(S[s][1] / S[s][0]) for s in R.SECS])
        j = R.jac_both(f, np.array([t.real, t.imag]), [1e-3, 1e-3])
        print("%s tau at delta = inf, ln(m2/m3) only: rank %s, sv %s" % (k, j["rank"], " ".join("%.1e" % x for x in j["sv_h2"])))


if __name__ == "__main__":
    main()
