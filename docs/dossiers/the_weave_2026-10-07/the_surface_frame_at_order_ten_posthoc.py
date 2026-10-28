#!/usr/bin/env python3
"""W171 POST HOC (labelled; written after the read-out of W171's one run, where K2 failed as worded). K2 again, at the
same lines, elements, points and precision, with two corrections found at the read-out:

  1. The law's sign. The rule took W91 post hoc 2's form exp(-2 pi i c Q / N). Relay 133's item 5 had already noted
     that chat1's law as written is the eps = -1 case. Read out, the up sector returns with 0.7 turns where that form
     says 0.3 on every eps = +1 row, and agrees on the two eps = -1 rows. So here the law is exp(2 pi i eps c Q / N),
     the per-field law's form with q_H absent.
  2. The "never 1" test. It was applied to cycle products, and a 2-cycle with chi = -1 has product 1 (28 rows, down
     and leptons). The character is tested instead: each 1-cycle and the identity channel give chi itself, and each
     cycle product is compared with chi^length.

The prediction, fixed before this script's run: on all 108 rows the cycle products equal exp(2 pi i eps c Q / N) to
the power of the cycle's length, and the identity channel equals exp(2 pi i eps c Q / N), to 1e-30, tau-independent;
and no row's character equals 1.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_surface_frame_at_order_ten_posthoc.py
"""
import contextlib
import io
import json
import sys
import time
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_surface_frame_at_order_ten as W171      # noqa: E402

W91, N, T10, REF = W171.W91, W171.N, W171.T10, W171.REF
OUT = HERE / "the_surface_frame_at_order_ten_posthoc.json"


def law_eps(eps, c, Q):
    return mp.exp(2j * mp.pi * eps * c * Q / N)


def part_K2_eps(chosen):
    mp.mp.dps = 60
    rows, worst, worst_t, any_one, old_misses = [], mp.mpf(0), mp.mpf(0), False, 0
    for w, pick in chosen.items():
        a, b = w
        if gcd(a, N) == 1:
            g, (eps, c) = T10, W171.keeps(w, T10, N)
        else:
            g, (eps, c) = pick
        A, B, C, D = g
        if C == 0:
            taus = [mp.mpc("0.1", "1.1"), mp.mpc("0.3", "0.9")]
        else:
            base = mp.mpf(-D) / C
            taus = [base + 1j / mp.mpf(abs(C)), base + (mp.mpf("0.3") + 1.2j) / mp.mpf(abs(C))]
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
        psi = (Fr(a, N), Fr(-b, N))
        Rt = [W91.ev_generator(REF[0], REF[1], psi, t, need) for t in taus]
        Rg = [W91.ev_generator(REF[0], REF[1], psi, x, need) for x in gt]
        for name, (qL, qR) in W91.SECTORS.items():
            Q = qL * qL + qR * qR
            chi_law = law_eps(eps, c, Q)
            Vt = [W91.ev_generator(qL + qR, qL - qR, psi, t, need) for t in taus]
            Vg = [W91.ev_generator(qL + qR, qL - qR, psi, x, need) for x in gt]
            zero = set().union(*(W171.zero_channels([V]) for V in Vt + Vg))
            chi = {u: [Vg[n][u] / Vt[n][pi[u]] / (V0g[n][u] / V0[n][pi[u]]) for n in range(2)]
                   for u in ("i", "j", "k") if u not in zero and pi[u] not in zero}
            tdep = max((abs(v[0] - v[1]) for v in chi.values()), default=mp.mpf(0))
            seen, err, cyc, chars = set(), mp.mpf(0), [], []
            for u in ("i", "j", "k"):
                if u in seen:
                    continue
                x, ln, p, ok = u, 0, mp.mpc(1), True
                while x not in seen:
                    seen.add(x)
                    if x in chi:
                        p *= chi[x][0]
                    else:
                        ok = False
                    x = pi[x]
                    ln += 1
                if not ok:
                    cyc.append({"length": ln, "untested: an identically zero channel": True})
                    continue
                err = max(err, abs(p - chi_law ** ln))
                if ln == 1:
                    chars.append(p)
                cyc.append({"length": ln, "turns": float(mp.arg(p) / (2 * mp.pi) % 1)})
            chi1 = [(Vg[n]["1"] / Vt[n]["1"]) / (Rg[n]["1"] / Rt[n]["1"]) for n in range(2)]
            tdep = max(tdep, abs(chi1[0] - chi1[1]))
            err = max(err, abs(chi1[0] - chi_law))
            chars.append(chi1[0])
            one = any(abs(z - 1) < 1e-3 for z in chars)
            any_one |= one
            old = abs(chi1[0] - mp.exp(-2j * mp.pi * c * Q / N)) > 1e-30
            old_misses += old
            worst, worst_t = max(worst, err), max(worst_t, tdep)
            rows.append({"line (a, b)": list(w), "element": list(g), "eps": eps, "c": c, "sector": name,
                         "identically zero channels": sorted(zero), "cycles": cyc,
                         "character turns (identity channel)": float(mp.arg(chi1[0]) / (2 * mp.pi) % 1),
                         "eps-law turns": float((eps * c * Q / N) % 1), "law error": float(err),
                         "tau-dependence": float(tdep), "character equal to 1": bool(one),
                         "the rule's form (eps = -1 case) misses": bool(old)})
    return {"rows": rows, "worst law error": float(worst), "worst tau-dependence": float(worst_t),
            "some character equal to 1": bool(any_one), "rows the rule's form misses": int(old_misses),
            "holds": bool(worst < 1e-30 and worst_t < 1e-30 and not any_one)}


def main():
    t0 = time.time()
    out = {"status": "POST HOC (labelled), after W171's read-out; K2 with the eps-law and the character tested"}
    _K1, chosen = W171.part_K1()
    out["K2 post hoc"] = part_K2_eps(chosen)
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("K2 post hoc holds", out["K2 post hoc"]["holds"], "seconds", out["seconds"])


if __name__ == "__main__":
    main()
