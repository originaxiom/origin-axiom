"""The web seat's check for its note on the steepness map (data-free; no measured value is read; exact arithmetic on
B1788's leading-order exponents; nothing on any line's spectrum at finite height).

B1788 (PROVED at leading order in Im tau, conditional on its section 5 hypotheses) gives each sector's singular-value
exponents as functions of the slope alpha alone (generic b): tropical.predict(P[reading], E(q_L alpha, q_R alpha)) returns
(e(m2/m3), e(m1/m3)), with m_k/m_3 ~ exp(-e * 2 pi Im tau), and e(m2/m3) = 1/2 - (||2 q_L alpha|| + ||2 q_R alpha||)/2 in
both readings.  6Y charges: up (1, -4), down (1, 2), leptons (-3, 6).  "Up steeper" at leading order means e_up > e_down,
strictly, for the ratio named (main's filter needs both ratios: s1/s2 up < s1/s2 down / 2 and s0/s2 up < s0/s2 down; at
leading order in Im tau the factor 1/2 is subleading, so the filter's condition becomes both strict inequalities).

(1) The instrument: B1788's tropical e(m2/m3) against its closed form on every slope checked, both readings, three
    sectors (as B1788's domain.py).
(2) The m2/m3 map: for every slope alpha = r/s with s <= 120: the gap e_up - e_down = (||4 alpha|| - ||8 alpha||)/2 and
    the statement 'gap > 0 exactly when ||4 alpha|| > 1/3'; the largest and smallest gap and where they occur; the
    fraction of slopes with gap > 0, = 0, < 0 at each denominator bound, against the measure 1/3, 0, 2/3.
(3) The m1/m3 map by reading, for the four quark reading pairs (up, down) in {S, S~}^2 (B1790's covariant readings): the
    gap e_up(m1/m3) - e_down(m1/m3) on every slope with s <= 120; the fraction of slopes with up steeper.
(4) Both ratios (main's filter's 'up steeper' at leading order) by reading pair: the fraction of slopes, the bits -log2 of
    it, and the list for s <= 12; the count of slopes where both hold under the equal readings (S, S) and (S~, S~).
(5) The slopes the record names: 2/5 (the candidate family's), 1/10, 1/5, 1/8, 3/8, 4/9, 1/7, 2/7, 1/3: their exponents.
(4b) On the slopes where up is steeper in m2/m3: how often up's m1/m3 exponent is above, equal to or below down's.
(6) The mechanism probe: the sum e(m2/m3) + e(m1/m3) for up and down in each reading pair; on how many slopes it is the
    same in up and down.

Usage: python3 steepness_map.py <main checkout>   (main at 2d0419d3c)
"""
import math
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1788_the_closed_form_of_the_exponents" / "verification"))
import tropical as T  # noqa: E402

SEC = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
NMAX = 120


def nd(x):
    x = Fr(x) % 1
    return min(x, 1 - x)


def closed(ql, qr, a):
    return Fr(1, 2) - (nd(2 * ql * a) + nd(2 * qr * a)) / 2


def slopes(nmax):
    return [Fr(r, s) for s in range(1, nmax + 1) for r in range(0, s) if gcd(r, s) == 1]


if __name__ == "__main__":
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    SL = slopes(NMAX)
    ex = {}
    mism = 0
    for a in SL:
        for sec, (ql, qr) in SEC.items():
            mu = T.E(ql * a, qr * a)
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu)
                ex[(a, sec, rd)] = (Fr(e2), Fr(e3))
                mism += Fr(e2) != closed(ql, qr, a)
    print("(1) the instrument: B1788's tropical e(m2/m3) against its closed form: %d mismatches in %d (slope, sector, reading) cases, s <= %d"
          % (mism, len(SL) * 6, NMAX))

    print("(2) the m2/m3 map (the reading does not enter):")
    bad = 0; gaps = []
    for a in SL:
        g = ex[(a, "up", "S")][0] - ex[(a, "down", "S")][0]
        assert g == (nd(4 * a) - nd(8 * a)) / 2
        gaps.append((g, a))
        bad += (g > 0) != (nd(4 * a) > Fr(1, 3))
    print("    gap = e_up - e_down = (||4a|| - ||8a||)/2 on every slope; 'gap > 0 exactly when ||4a|| > 1/3' fails on %d of %d slopes" % (bad, len(SL)))
    gmax = max(gaps); gmin = min(gaps)
    print("    largest gap %s at %s (||4a|| = %s); smallest %s at %s (||4a|| = %s)"
          % (gmax[0], ", ".join(str(a) for g, a in gaps if g == gmax[0] and a.denominator <= 8), nd(4 * gmax[1]),
             gmin[0], ", ".join(str(a) for g, a in gaps if g == gmin[0] and a.denominator <= 16), nd(4 * gmin[1])))
    for nb in (12, 30, 60, 120):
        sub = [g for g, a in gaps if a.denominator <= nb]
        print("    s <= %3d: %4d slopes; gap > 0: %.4f, = 0: %.4f, < 0: %.4f" % (
            nb, len(sub), sum(g > 0 for g in sub) / len(sub), sum(g == 0 for g in sub) / len(sub), sum(g < 0 for g in sub) / len(sub)))
    print("    the measure (alpha uniform): ||4a|| is uniform on [0, 1/2], so gap > 0 on 1/3 of slopes, < 0 on 2/3")
    g_ld = [ex[(a, "lep", "S")][0] - ex[(a, "down", "S")][0] for a in SL]
    print("    leptons against down: e_lep - e_down > 0 on %.4f, = 0 on %.4f, < 0 on %.4f of slopes (s <= %d)" % (
        sum(g > 0 for g in g_ld) / len(SL), sum(g == 0 for g in g_ld) / len(SL), sum(g < 0 for g in g_ld) / len(SL), NMAX))

    PAIRS = (("S", "S"), ("St", "S"), ("S", "St"), ("St", "St"))
    print("(3) the m1/m3 map by reading pair (up, down):")
    for ru, rdn in PAIRS:
        g3 = [(ex[(a, "up", ru)][1] - ex[(a, "down", rdn)][1], a) for a in SL]
        print("    (%-2s, %-2s): e_up(m1/m3) - e_down(m1/m3) > 0 on %.4f, = 0 on %.4f, < 0 on %.4f of slopes; range %s to %s" % (
            ru, rdn, sum(g > 0 for g, a in g3) / len(SL), sum(g == 0 for g, a in g3) / len(SL), sum(g < 0 for g, a in g3) / len(SL),
            min(g for g, a in g3), max(g for g, a in g3)))

    print("(4) both ratios ('up steeper' at leading order) by reading pair (up, down):")
    for ru, rdn in PAIRS:
        both = [a for a in SL if ex[(a, "up", ru)][0] > ex[(a, "down", rdn)][0] and ex[(a, "up", ru)][1] > ex[(a, "down", rdn)][1]]
        f = len(both) / len(SL)
        print("    (%-2s, %-2s): %d of %d slopes (%.4f), %s bits; m2/m3 alone %d, m1/m3 alone %d; with s <= 12: %s" % (
            ru, rdn, len(both), len(SL), f, ("%.2f" % -math.log2(f)) if f > 0 else "-",
            sum(1 for a in SL if ex[(a, "up", ru)][0] > ex[(a, "down", rdn)][0]),
            sum(1 for a in SL if ex[(a, "up", ru)][1] > ex[(a, "down", rdn)][1]),
            ", ".join(str(a) for a in both if a.denominator <= 12)))

    print("(5) the slopes the record names (e2, e3) per sector and reading:")
    for a in (Fr(2, 5), Fr(1, 10), Fr(1, 5), Fr(1, 8), Fr(3, 8), Fr(4, 9), Fr(1, 7), Fr(2, 7), Fr(1, 3)):
        print("    %-5s up S %s  up S~ %s  down S %s  down S~ %s  leptons S %s  ||4a|| %s" % (
            a, tuple(str(x) for x in ex[(a, "up", "S")]), tuple(str(x) for x in ex[(a, "up", "St")]),
            tuple(str(x) for x in ex[(a, "down", "S")]), tuple(str(x) for x in ex[(a, "down", "St")]),
            tuple(str(x) for x in ex[(a, "lep", "S")]), nd(4 * a)))

    print("(4b) on the slopes where up is steeper in m2/m3: up's m1/m3 exponent against down's, by reading pair:")
    for ru, rdn in PAIRS:
        st2 = [a for a in SL if ex[(a, "up", ru)][0] > ex[(a, "down", rdn)][0]]
        c = [ex[(a, "up", ru)][1] - ex[(a, "down", rdn)][1] for a in st2]
        print("    (%-2s, %-2s): %d slopes; m1/m3 up steeper %d, tied %d, down steeper %d" % (
            ru, rdn, len(st2), sum(x > 0 for x in c), sum(x == 0 for x in c), sum(x < 0 for x in c)))

    print("(6) the mechanism probe: e(m2/m3) + e(m1/m3), up against down, by reading pair:")
    for ru, rdn in PAIRS:
        same = sum(1 for a in SL if sum(ex[(a, "up", ru)]) == sum(ex[(a, "down", rdn)]))
        diffs = sorted({sum(ex[(a, "up", ru)]) - sum(ex[(a, "down", rdn)]) for a in SL})
        print("    (%-2s, %-2s): the sums equal on %d of %d slopes; the differences take %d values, from %s to %s" % (
            ru, rdn, same, len(SL), len(diffs), diffs[0], diffs[-1]))
