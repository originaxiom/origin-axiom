#!/usr/bin/env python3
"""B1397 -- the cap's generations: the chiral spectrum a flux cap gives in each of the seat's frames.

A cusp capped with a torus T_c carrying a U(1) flux F of degree n (B1395's one finite-energy charge-odd datum; B1396's cap): every
charged sector mu sees (bulk flat bundle on T_c) (x) (flux line bundle)^{<F, mu>}, whose Riemann-Roch index on the torus is
rank x <F, mu> n.  So the cap's net chirality is LINEAR in the charges, N_mu = <F, mu> n for every weight mu, SL(2)_beta doublets
included (the frame's bulk rule is sign(<H, mu>) N on spin-0 sectors and 0 on doublets, B1389).  F must commute with the Standard
Model and with SL(2)_beta's parabolic cusp holonomy: F in span(Y, gamma) in E6, plus E7's U(1) t (F133), plus the SU(3) Cartan of
E8 > E6 x SU(3) (F248).

For each frame and each flux direction: integrality of the indices (the flux lattice), the Standard-Model anomalies, the chiral
exotics, and the net number of generations g (net 10s = net 5bars, vector-like pairs and singlets aside).  Exact rational arithmetic
with B1389's vectors (B1368's, verbatim).
Usage: python3 cap_generations.py"""
import itertools
import sys
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1389_the_full_spectrum" / "verification"))
import full_spectrum as FS                                               # noqa: E402  (the record's E6 vectors)

ALL78 = [r for r in FS.R if r > FS.neg(r)]                               # one root per +- pair, every SL(2)_beta spin
XY = ("3", "2", Fr(-5, 6))                                               # the X,Y bosons' partners (conjugate netted in)
GEN = ("Q", "u^c", "e^c", "d^c", "L")
REP = {("3", "2", Fr(1, 6)): "Q", ("3b", "1", Fr(-2, 3)): "u^c", ("1", "1", Fr(1)): "e^c", ("3b", "1", Fr(1, 3)): "d^c",
       ("1", "2", Fr(-1, 2)): "L"}
CANON = {**REP, XY: "XY"}


def conj(rep):
    return ({"3": "3b", "3b": "3", "1": "1"}[rep[0]], rep[1], -rep[2])


def cap_states(frame, F, n):
    """[(weight, index)]: F = (a, b) for a Y + b gamma, plus c (E7's t, frame F133) or (h1, h2, h3) (E8's SU(3) Cartan, frame F248)"""
    a, b = Fr(F[0]), Fr(F[1])
    q = lambda m: a * FS.dot(FS.Y, m) + b * FS.dot(FS.gamma, m)
    st = []
    if frame in ("F27", "F27+78"):
        st += [(w, q(w) * n) for w in FS.W27]
    if frame == "F133":
        st += [(w, (q(w) + Fr(F[2])) * n) for w in FS.W27]
    if frame == "F248":
        for h in F[2]:
            st += [(w, (q(w) + Fr(h)) * n) for w in FS.W27]
    if frame in ("F78", "F27+78", "F133", "F248"):
        st += [(r, q(r) * n) for r in ALL78]
    return st


def analyse(frame, F, n):
    st = cap_states(frame, F, n)
    integral = all(Fr(x).denominator == 1 for _, x in st)
    out = dict(frame=frame, F=[str(x) if not isinstance(x, tuple) else [str(y) for y in x] for x in F], n=n, integral=integral)
    if not integral:
        return out
    st = [(m, int(x)) for m, x in st]
    an = FS.anomalies(st)
    net = Counter()
    for rep, k in FS.content(st).items():                  # net multiplets per SM representation, each conjugate pair netted once
        if rep in CANON:
            net[rep] += k
        elif conj(rep) in CANON:
            net[conj(rep)] -= k
        else:
            key = max(rep, conj(rep), key=str)
            net[key] += k if key == rep else -k
    named = {CANON.get(r, str(r)): k for r, k in net.items() if k != 0 and r != ("1", "1", Fr(0))}
    gens = [net.get(r, 0) for r in REP]
    g = gens[0] if all(x == gens[0] for x in gens) else None
    exotic = sorted(k for k in named if k not in GEN)
    out.update(anomaly_free=FS.anomaly_free(an), anomalies={k: str(v) for k, v in an.items() if v != 0},
               xy_chiral=net.get(XY, 0) != 0, g=g, exotic=exotic, net=named)
    return out


def g_formula(frame, F, n):
    """the hand formulas (FINDINGS section 2), for F orthogonal to Y (a = 0)"""
    b = Fr(F[1])
    if frame == "F78":
        return 2 * b * n
    if frame == "F27":
        return -Fr(2, 3) * b * n
    if frame == "F27+78":
        return Fr(4, 3) * b * n
    if frame == "F133":
        return (Fr(4, 3) * b + Fr(F[2])) * n
    if frame == "F248":
        return Fr(0)


def minimal_n(frame, F):
    for n in range(1, 73):
        if analyse(frame, F, n)["integral"]:
            return n
    return None


def banked_identity():
    """B1389's own control and two hand values: the full 27 with index 1 is anomaly-free; F78 with F = gamma, n = 1 gives exactly two
    generations; F133 with F = t, n = 1 gives one net generation plus a vector-like (5 + 5bar)"""
    bad = []
    ok, _ = FS.banked_identity()
    if not ok:
        bad.append("B1389's banked identity")
    if len(ALL78) != 36:
        bad.append(("root pairs", len(ALL78)))
    r = analyse("F78", (0, 1), 1)
    if not (r["anomaly_free"] and r["g"] == 2 and not r["exotic"]):
        bad.append(("F78 gamma n=1", r))
    r = analyse("F133", (0, 0, 1), 1)
    if not (r["anomaly_free"] and r["g"] == 1 and not r["exotic"]):
        bad.append(("F133 t n=1", r))
    return bad


def scan():
    """directions F = (a, b[, c or h]) on a rational grid; for each: the minimal n making every index integral, and the analysis there
    and at 2n, 3n.  Checks: anomaly-free iff a = 0 (F orthogonal to Y); X,Y partners chiral iff a != 0; g equals the hand formula
    whenever a = 0; the achievable g per frame."""
    vals = [Fr(x, y) for x in range(-3, 4) for y in (1, 2, 3)]
    vals = sorted(set(vals))
    rows, fails = [], []
    for frame in ("F27", "F78", "F27+78", "F133", "F248"):
        dirs = []
        for a in (Fr(0), Fr(1), Fr(-1, 2)):
            for b in vals:
                if frame == "F133":
                    dirs += [(a, b, c) for c in (Fr(0), Fr(1), Fr(-1), Fr(1, 3), Fr(-2, 3), Fr(2))]
                elif frame == "F248":
                    dirs += [(a, b, h) for h in ((Fr(0), Fr(0), Fr(0)), (Fr(1), Fr(-1), Fr(0)), (Fr(1), Fr(1), Fr(-2)),
                                                 (Fr(1, 3), Fr(1, 3), Fr(-2, 3)), (Fr(2), Fr(-1), Fr(-1)))]
                else:
                    dirs.append((a, b))
        for F in dirs:
            if all(x == 0 for x in (F[0], F[1])) and (len(F) == 2 or (not isinstance(F[2], tuple) and F[2] == 0)
                                                     or (isinstance(F[2], tuple) and all(h == 0 for h in F[2]))):
                continue
            n0 = minimal_n(frame, F)
            if n0 is None:
                fails.append(("no integral n up to 72", frame, F))
                continue
            for k in (1, 2, 3):
                r = analyse(frame, F, n0 * k)
                r["n_min"] = n0
                rows.append(r)
                a0 = F[0] == 0
                if r["anomaly_free"] != a0:
                    fails.append(("anomaly-free iff F orthogonal to Y", r))
                if a0 and r["xy_chiral"]:
                    fails.append(("X,Y chiral with a = 0", r))
                if a0 and (r["g"] is None or r["g"] != g_formula(frame, F, n0 * k)):
                    fails.append(("g formula", r, str(g_formula(frame, F, n0 * k))))
                if a0 and r["exotic"]:
                    fails.append(("exotics with a = 0", r))
    achieved = {}
    for r in rows:
        if r.get("anomaly_free") and r["g"] is not None:
            achieved.setdefault(r["frame"], set()).add(r["g"])
    return rows, fails, {f: sorted(s) for f, s in achieved.items()}


if __name__ == "__main__":
    import json
    bad = banked_identity()
    print("## the banked identity (B1389's controls; F78 gamma n=1 -> 2 generations; F133 t n=1 -> 1):", bad or "passed")
    if bad:
        sys.exit("the banked identity failed")
    print("## the hand cases")
    for frame, F in (("F78", (0, 1)), ("F27", (0, 1)), ("F27+78", (0, 1)), ("F133", (0, 0, 1)), ("F133", (0, 1, Fr(-1, 3))),
                     ("F133", (0, 1, Fr(2, 3))), ("F248", (0, 1, (Fr(1), Fr(-1), Fr(0)))), ("F248", (0, 0, (Fr(1), Fr(1), Fr(-2)))),
                     ("F78", (1, 0)), ("F27+78", (1, 1))):
        n0 = minimal_n(frame, F)
        r = analyse(frame, F, n0)
        print("%-7s F=%-28s n_min=%d  anomaly-free=%-5s X,Y chiral=%-5s g=%-4s exotics=%s  net=%s" % (
            frame, str(tuple(str(x) if not isinstance(x, tuple) else tuple(str(y) for y in x) for x in F)), n0, r["anomaly_free"],
            r["xy_chiral"], r["g"], r["exotic"], r["net"]))
    rows, fails, achieved = scan()
    print("## the scan: %d (frame, direction, n) rows; failures %d" % (len(rows), len(fails)))
    for f in fails[:10]:
        print("   ", f)
    print("## achievable net generations with F orthogonal to Y (per frame, over the scan):")
    for f, s in achieved.items():
        print("   %-7s %s" % (f, s))
    keep = ("frame", "F", "n", "n_min", "integral", "anomaly_free", "xy_chiral", "g", "exotic")
    json.dump(dict(fails=[str(f) for f in fails], achieved={f: [str(x) for x in s] for f, s in achieved.items()},
                   rows=[{k: (str(r[k]) if k == "g" else r[k]) for k in keep if k in r} for r in rows]),
              open(HERE / "cap_generations.json", "w"), separators=(",", ":"), default=str)
    print("DONE")
