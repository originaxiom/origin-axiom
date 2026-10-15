"""W91 post hoc 2 (labelled; after post hoc 1 failed): the second diagnosis. U5 detects the untwisted channel map pi
from the constancy of V0(g tau) / ((C tau + D) V0(tau)), the weight-1 factor of relay 127's scratch, where V was
theta theta. Here V includes 1 / theta_1'(0), so its weight is -1/2 and the factor is (C tau + D)^(-1/2). With the wrong
weight no candidate is constant, so pi can be wrong, and a wrong pi makes chi depend on tau. Here pi is detected with
the weight -1/2 factor; both sign conventions for the line are run (psi2 = +b/N, as U5 did, and -b/N).

Run: python3 the_twisted_coupling_vector_posthoc2.py  ->  the_twisted_coupling_vector_posthoc2.json beside it.
"""
import itertools
import json
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import mpmath as mp

import the_twisted_coupling_vector as W91

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_twisted_coupling_vector_posthoc2.json"


def main():
    worst, cases, rows = {1: 0, -1: 0}, 0, []
    for (wd, N), sgn in itertools.product((("LLRLLRRLRR", 9), ("LLLLRLRRRLRR", 11)), (1, -1)):
        g = (1, 0, 0, 1)
        for ch in wd:
            L = (1, 0, 1, 1) if ch == "L" else (1, 1, 0, 1)
            g = (g[0] * L[0] + g[1] * L[2], g[0] * L[1] + g[1] * L[3], g[2] * L[0] + g[3] * L[2], g[2] * L[1] + g[3] * L[3])
        A, B, C, D = g
        base = mp.mpf(-D) / C
        taus = [base + 1j / mp.mpf(C), base + (mp.mpf("0.3") + 1.2j) / mp.mpf(C)]
        gt = [(A * t + B) / (C * t + D) for t in taus]
        need = Fr(int(45 * mp.log(10) / (2 * mp.pi * min(mp.im(x) for x in taus + gt) / 1.6)) + 1)
        V0 = [W91.ev_generator(0, 0, (Fr(0), Fr(0)), t, need) for t in taus]
        V0g = [W91.ev_generator(0, 0, (Fr(0), Fr(0)), x, need) for x in gt]
        pi = {}
        for u in ("i", "j", "k"):
            best = None
            for u2 in ("i", "j", "k"):
                r = [V0g[n][u] * mp.sqrt(C * taus[n] + D) / V0[n][u2] for n in range(2)]
                if best is None or abs(r[0] - r[1]) < best[0]:
                    best = (abs(r[0] - r[1]), u2)
            pi[u] = best[1]
        done = 0
        for a, b in itertools.product(range(N), repeat=2):
            if gcd(gcd(a, b), N) != 1:
                continue
            wg = ((a * A + b * C) % N, (a * B + b * D) % N)
            if wg not in ((a, b), ((-a) % N, (-b) % N)):
                continue
            c = ((a * (a * B + b * D) - b * (a * A + b * C)) // N) % N
            psi = (Fr(a, N), Fr(sgn * b, N))
            for name, (qL, qR) in W91.SECTORS.items():
                Vt = [W91.ev_generator(qL + qR, qL - qR, psi, t, need) for t in taus]
                Vg = [W91.ev_generator(qL + qR, qL - qR, psi, x, need) for x in gt]
                chi = {u: [Vg[n][u] / Vt[n][pi[u]] / (V0g[n][u] / V0[n][pi[u]]) for n in range(2)]
                       for u in ("i", "j", "k")}
                tdep = max(abs(v[0] - v[1]) for v in chi.values())
                seen, err = set(), 0
                for u in ("i", "j", "k"):
                    if u in seen:
                        continue
                    x, ln, p = u, 0, mp.mpc(1)
                    while x not in seen:
                        seen.add(x)
                        p *= chi[x][0]
                        x = pi[x]
                        ln += 1
                    err = max(err, abs(p - mp.exp(-2j * mp.pi * c * (qL * qL + qR * qR) / N) ** ln))
                worst[sgn] = max(worst[sgn], tdep, err)
                rows.append({"thread": wd, "N": N, "line (a, b)": [a, b], "psi2 sign": sgn, "sector": name, "c": c,
                             "tau-dependence": float(tdep), "law error": float(err)})
                cases += 1
            done += 1
            if done == 2:
                break
    out = {"status": "W91 post hoc 2 (labelled): U5 with the channel map detected at weight -1/2, both line signs",
           "cases": cases, "worst by sign": {str(k): float(v) for k, v in worst.items()},
           "law holds to 1e-30 by sign": {str(k): bool(v < 1e-30) for k, v in worst.items()}, "rows": rows}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("written", OUT.name, json.dumps(out["worst by sign"]))


if __name__ == "__main__":
    main()
