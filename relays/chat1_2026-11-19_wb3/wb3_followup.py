#!/usr/bin/env python3
"""W-B3-F: the follow-up to W-B3's run, which stopped in the plain-a0 variant (card W-B3, "After the run", 652cd48af,
committed before this script). Data-free, as the run. It imports the run's functions unchanged and computes only what
the run did not reach.

    python3 -I -u wb3_followup.py <a checkout of main>

  F1  C4 as written: the first two points at height 30, c = +2, at 90 and 110 digits; every |V| entry within 1e-15.
  F2  the plain variant, guarded, at c = -2 and +2, heights 6 and 30: per point, which sectors' couplings vanish (every
      weight zero); the pairs over the points where up and down both survive; the leptons where leptons and down do.
  F3  the run's verdicts for C0, X3 and X4, read off its printed output by the card's rules.
"""
import pathlib
import re
import sys
import time

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wb3_run as R  # noqa: E402  (the run's functions; its main is not called)

T0 = time.time()
say = R.say


def f1():
    worst = 0.0
    L, _ = R.end_value(6.0)
    for a, b in R.POINTS[:2]:
        A = {}
        for extra in (0, 20):
            mp.mp.dps = int(30 + 2 * 30) + extra
            ALG = R.setup()
            t = mp.mpc(R.f2m(R.X_RE), 30)
            res, _, _ = R.point_table(t, mp.mpf(30), a, b, 2, mp.mpf(L), R.triplet(t), ALG, "cov")
            A[extra] = res
        for k in R.PAIRS:
            worst = max(worst, max(abs(A[0][k][2][i][j] - A[20][k][2][i][j]) for i in range(3) for j in range(3)))
    return worst


def f2(c, y, L):
    mp.mp.dps = int(30 + 2 * y)
    ALG = R.setup()
    t = mp.mpc(R.f2m(R.X_RE), y)
    S3 = R.triplet(t)
    acc = {k: [] for k in R.PAIRS}
    lep = {"S": [], "St": []}
    vanish = {s: 0 for s in R.SECT}
    for a, b in R.POINTS:
        Y, alive = {}, {}
        for sec in R.SECT:
            Mw, _ = R.sector(t, mp.mpf(y), a, b, sec, c, mp.mpf(L), ALG, "plain")
            alive[sec] = any(Mw[i, j] != 0 for i in range(2) for j in range(2))
            vanish[sec] += not alive[sec]
            Y[sec] = R.couplings(Mw, S3, ALG) if alive[sec] else None
        if alive["up"] and alive["down"]:
            Uo = {(s, r): R.U_of(Y[s][r]) for s in ("up", "down") for r in ("S", "St")}
            for ru, rd in R.PAIRS:
                V = Uo[("up", ru)].H * Uo[("down", rd)]
                A = [[float(abs(V[i, j])) for j in range(3)] for i in range(3)]
                acc[(ru, rd)].append((min(A[k][k] for k in range(3)),
                                      max(A[i][j] for i in range(3) for j in range(3) if i != j)))
        if alive["lep"] and alive["down"]:
            for r in ("S", "St"):
                Ul, Ud = R.U_of(Y["lep"][r]), R.U_of(Y["down"][r])
                pat = lambda W: max(min(abs(float(abs(W[i, j])) - 1), float(abs(W[i, j])))
                                    for i in range(3) for j in range(3))
                sl = sorted(float(v) for v in mp.svd_c(Y["lep"][r], compute_uv=False))
                sd = sorted(float(v) for v in mp.svd_c(Y["down"][r], compute_uv=False))
                spec = max(abs(sl[k] / sl[2] - sd[k] / sd[2]) for k in range(3)) if sl[2] > 0 and sd[2] > 0 \
                    else float("nan")
                lep[r].append((pat(Ul.H * Ud), pat(Ul.H * R.U_of(Y["down"][r].T)), spec))
    return acc, lep, vanish


def parse_run():
    rows, lep = {}, {}
    pat = re.compile(r"^(cov|plain)\s+c = ([+-]\d)\s+height\s+([\d.]+)\s+up (\S+)\s+down (\S+)\s*: smallest diagonal "
                     r"\|V\| (\S+), largest off-diagonal (\S+)\s+(\S+)")
    pl = re.compile(r"^(cov|plain)\s+c = ([+-]\d)\s+height\s+([\d.]+)\s+leptons against down, reading (\S+)\s*: plain "
                    r"(\S+), transposed (\S+), spectra (\S+)")
    for line in open(HERE / "wb3_run_out.txt"):
        m = pat.match(line)
        if m:
            rows[(m[1], int(m[2]), float(m[3]), m[4], m[5])] = (float(m[6]), float(m[7]), m[8])
        m = pl.match(line)
        if m:
            lep[(m[1], int(m[2]), float(m[3]), m[4])] = (float(m[5]), float(m[6]), float(m[7]))
    return rows, lep


def main():
    if R.MAIN is None:
        sys.exit("give a checkout of main")
    w = f1()
    say("F1 (C4) holds:", w < 1e-15, "| |V| at 20 more digits, two points at height 30, c = +2: %.2e  [%.0f s]"
        % (w, time.time() - T0))
    L, _ = R.end_value(6.0)
    for c in (-2, 2):
        for y in (6.0, 30.0):
            acc, lep, vanish = f2(c, y, L)
            say("F2 plain c = %+d height %4.1f: points where a sector's coupling vanishes: up %d, down %d, leptons %d"
                " (of 24)" % (c, y, vanish["up"], vanish["down"], vanish["lep"]))
            for k in R.PAIRS:
                v = acc[k]
                if v:
                    say("   up %-2s down %-2s over %2d points: smallest diagonal |V| %.4e,"
                        " largest off-diagonal %.4e  %s" % (k[0], k[1], len(v), min(q[0] for q in v),
                                                             max(q[1] for q in v), R.classify([q[0] for q in v])))
                else:
                    say("   up %-2s down %-2s: no point where up and down both survive" % k)
            for r in ("S", "St"):
                v = lep[r]
                if v:
                    say("   leptons against down, reading %-2s, over %2d points: plain %.3e, transposed %.3e,"
                        " spectra %.3e" % (r, len(v), max(q[0] for q in v), max(q[1] for q in v),
                                           max(q[2] for q in v)))
                else:
                    say("   leptons against down, reading %-2s: no point where both survive" % r)
            say("   [%.0f s]" % (time.time() - T0))
    rows, lep = parse_run()
    c0 = [rows[("cov", 0, 6.0, "S", "S")], rows[("cov", 0, 6.0, "St", "St")]]
    c0ok = all(float("%.4g" % g[i]) == wv[i] for g, wv in zip(c0, [(0.9932, 0.1161), (0.9752, 0.2215)])
               for i in range(2))
    say("F3: C0 holds:", c0ok)
    pairs = [("S", "S"), ("St", "St"), ("St", "S"), ("S", "St")]
    x3a = all(rows[("cov", c, 30.0) + p][2] != "ALIGNED" and rows[("cov", c, 30.0) + p][0] < 1e-3
              for c in (2, -2) for p in pairs)
    x3b = all(sum(rows[("cov", c, 6.0) + p][2] == "DERANGED" for p in pairs) == 3
              and rows[("cov", c, 6.0, "St", "St")][2] == "PARTIAL" for c in (2, -2))
    x3c = all(rows[("cov", 2, y) + p][2] == rows[("cov", -2, y) + p][2] for y in (6.0, 30.0) for p in pairs)
    x3d = float("%.3g" % rows[("cov", -2, 6.0, "St", "St")][0]) == 0.125 \
        and float("%.3g" % rows[("cov", 2, 6.0, "St", "St")][0]) == 0.126
    say("F3: X3 holds:", x3a and x3b and x3c and x3d, "| parts: %s %s %s %s" % (x3a, x3b, x3c, x3d))
    x4 = all(lep[("cov", c, y, r)][1] < 1e-10 for c in (2, -2) for y in (6.0, 30.0) for r in ("S", "St"))
    say("F3: X4 holds:", x4)
    say("done  [%.0f s]" % (time.time() - T0))


if __name__ == "__main__":
    main()
