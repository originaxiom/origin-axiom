#!/usr/bin/env python3
"""W113, POST HOC (written after the one run's read-out; labelled): why did a few roots fail cell T1?

The run's T1 found, on each tuned variety, a few real roots that were not "pure and non-degenerate" (2 of 142, 1 of
88, 5 of 143 and 4 of 139), and the script did not record which test each failed.  This check replays T1 exactly
(the same spaces, the same random lines from seed 1134, in the same order) and records, for every root, the spread
of det Y / eta^(6k) across the three tau, the ratio m_min / m_max at tau_0, and the size of the root's coefficient
vector.  It changes no cell of the run.  Output: the_strong_angle_posthoc.json.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_strong_angle as SA  # noqa: E402

mp.mp.dps = 30


def replay(S, rb, typ, k, rt, U0, E0):
    m, a = SA.M_ETA[typ], SA.A_CHAR[typ]
    p0 = m + a // 3
    ser = []
    for B in rb:
        ser.append([[[sum((x * SA.mon_series(mon)[p] for mon, x in B[i][j].items()), Fraction(0))
                      for p in range(p0 + 1)] for j in range(3)] for i in range(3)])

    def alpha_at(c):
        E = [[[sum((c[b] * ser[b][i][j][p] for b in range(len(rb))), Fraction(0)) for p in range(p0 + 1)]
              for j in range(3)] for i in range(3)]
        tot = Fraction(0)
        for perm in SA.itertools.permutations(range(3)):
            sign = 1
            for x in range(3):
                for y in range(x + 1, 3):
                    if perm[x] > perm[y]:
                        sign = -sign
            A_, B_, C_ = E[0][perm[0]], E[1][perm[1]], E[2][perm[2]]
            for p1 in range(p0 + 1):
                if A_[p1] == 0:
                    continue
                for p2 in range(p0 + 1 - p1):
                    if B_[p2] == 0:
                        continue
                    tot += sign * A_[p1] * B_[p2] * C_[p0 - p1 - p2]
        return tot

    rows = []
    for line in range(50):
        c0 = [Fraction(int(x)) for x in rt.integers(-9, 10, size=len(rb))]
        dd = [Fraction(int(x)) for x in rt.integers(-9, 10, size=len(rb))]
        vals = [alpha_at([c0[b] + s * dd[b] for b in range(len(rb))]) for s in range(4)]
        co = SA.cubic_exact(vals)
        while co and co[-1] == 0:
            co.pop()
        if len(co) < 2:
            continue
        big = max(abs(x) for x in co)
        roots = mp.polyroots([mp.mpf((x / big).numerator) / (x / big).denominator for x in reversed(co)],
                             maxsteps=2000, extraprec=120)
        for s in roots:
            if abs(mp.im(s)) > mp.mpf(10) ** -15:
                continue
            s = mp.re(s)
            c = [mp.mpf(c0[b].numerator) / c0[b].denominator + s * mp.mpf(dd[b].numerator) / dd[b].denominator
                 for b in range(len(rb))]
            norm = mp.sqrt(sum(x * x for x in c))
            if norm < mp.mpf(10) ** -20 * mp.sqrt(sum(x * x for x in c0) + 1):
                continue
            W = [[{} for _ in range(3)] for _ in range(3)]
            for b, B in enumerate(rb):
                for i in range(3):
                    for j in range(3):
                        for mon, x in B[i][j].items():
                            W[i][j][mon] = W[i][j].get(mon, 0) + c[b] * (mp.mpf(x.numerator) / x.denominator)
            rs, mins = [], []
            for tau in SA.GENERIC5[:3]:
                u, eta = SA.u_mp(tau), SA.eta_mp(tau)
                Y = mp.matrix([[sum((x * u[0] ** mo[0] * u[1] ** mo[1] * u[2] ** mo[2]
                                     for mo, x in W[i][j].items()), mp.mpc(0)) / eta ** m
                                for j in range(3)] for i in range(3)])
                rs.append(mp.det(Y) / eta ** (6 * k))
                sv = mp.svd_c(Y, compute_uv=False)
                svs = sorted(float(abs(sv[i])) for i in range(3))
                mins.append(svs[0] / svs[2])
            spread = float(max(abs(x - rs[0]) for x in rs) / abs(rs[0])) if rs[0] != 0 else float("inf")
            cn = np.array([float(x) for x in c])
            cn = cn / np.linalg.norm(cn)
            _, svn = SA.svd_sorted(S.Y(U0, E0, cn))
            ratio_double = float(svn[0, 0] / svn[0, 2])
            ok = spread < 1e-12 and ratio_double > 1e-10
            rows.append({"line": line, "s": float(s), "spread": spread,
                         "m_min/m_max at the three tau (30 digits)": mins,
                         "m_min/m_max at tau_0 (double, the run's test)": ratio_double, "passed in the run": ok})
    return rows


def main():
    out = {"label": "POST HOC, after the read-out", "of": "the_strong_angle.py, cell T1"}
    U0, E0 = SA.u_eta_np(np.array([SA.GENERIC5[0]]))
    rt = np.random.default_rng(1134)
    for typ in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        k = SA.K_TUNED[typ]
        basis, d = SA.space(typ[0], typ[1], k)
        _, rb = SA.real_basis(basis, d)
        S = SA.Sector(rb, SA.M_ETA[typ], f"{SA.NAME[typ]} k={k}")
        rows = replay(S, rb, typ, k, rt, U0, E0)
        failed = [r for r in rows if not r["passed in the run"]]
        out[f"{SA.NAME[typ]} k={k}"] = {"real roots": len(rows), "failed in the run": len(failed),
                                        "the failed roots": failed,
                                        "largest spread among the passed": max((r["spread"] for r in rows
                                                                                if r["passed in the run"]),
                                                                               default=None)}
        print(SA.NAME[typ], k, len(rows), len(failed), flush=True)
    (HERE / "the_strong_angle_posthoc.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("written the_strong_angle_posthoc.json")


if __name__ == "__main__":
    main()
