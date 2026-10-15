"""W91 post hoc (labelled; after the read-out): U5 failed as worded (worst 2.99). The diagnosis to test: the object uses
w = psi1 tau - psi2, so its characteristic carries -k psi2, while U5 chose the fixed lines and c from (a, b) as the
scratch check of relay 127 did, where the characteristic carried +k psi2. So U5 tested the line (a, -b). Here U5's
computation is repeated with psi = (a/N, -b/N) for each fixed (a, b), nothing else changed.

Run: python3 the_twisted_coupling_vector_posthoc.py  ->  the_twisted_coupling_vector_posthoc.json beside it.
"""
import itertools
import json
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import mpmath as mp

import the_twisted_coupling_vector as W91

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_twisted_coupling_vector_posthoc.json"


def main():
    worst, cases, rows = 0, 0, []
    for wd, N in (("LLRLLRRLRR", 9), ("LLLLRLRRRLRR", 11)):
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
                r = [V0g[n][u] / ((C * taus[n] + D) * V0[n][u2]) for n in range(2)]
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
            psi = (Fr(a, N), Fr(-b, N))                      # the sign matched to w = psi1 tau - psi2
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
                worst = max(worst, tdep, err)
                rows.append({"thread": wd, "N": N, "line (a, b)": [a, b], "sector": name, "c": c,
                             "tau-dependence": float(tdep), "law error": float(err)})
                cases += 1
            done += 1
            if done == 2:
                break
    out = {"status": "W91 post hoc (labelled): U5 with the line's sign matched to the object's convention",
           "cases": cases, "worst": float(worst), "law holds to 1e-30": bool(worst < 1e-30), "rows": rows}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("written", OUT.name, "worst", float(worst))


if __name__ == "__main__":
    main()
