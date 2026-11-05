"""The web seat, 2026-11-05: POST HOC to third_opinion.py (2ea0a65be -> 5b16310e6), written after its read-only referee found
that its comparison ran at this run's recomputed L_max + delta, not at the census's stored L_max + delta. Data-free.

The pre-registered run recomputed L_max from the stored accessory parameter and put the horocycle there; at apex 222 that
differs from the census's stored L_max by 1.7e-12, which moves the norms by dN/dL * dL / N ~ 1e-11. Here the horocycle is
put at the census's own level, stored L_max + delta (B1839's census used G["L_max"] + delta with G recomputed on its own
machine, equal to the stored value there).
  (A) the pre-registered selection again (apexes 0, 111, 222 by Im tau, all n = 0; delta 0, 0.5, 4; the same five
      classes), this seat's (128, 96) against norms.npz;
  (B) an extension fixed by position, post hoc: the n = 1 apexes of least, median and greatest Im tau (the T^-1 reduction's
      path, absent from (A)) at delta 0, 0.5, 4 and 10, and delta 10 at (A)'s apexes; the same classes;
  and, per apex, this run's recomputed L_max against the stored.
Imports third_opinion.py's own functions unchanged (its kernels, quadrature and selection rule).

    python3 third_opinion_posthoc.py <main checkout with B1839's census outputs>      (main at 5baef4153)
"""
import contextlib
import io
import json
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "third_opinion.py").read_text().split('if __name__ == "__main__":')[0]
exec(compile(SRC, str(HERE / "third_opinion.py"), "exec"))


def geometry_from_stored(rec):
    tau = complex(*rec["tau"]); c = complex(*rec["c"])
    with contextlib.redirect_stdout(io.StringIO()):
        lat, z0, Aa, Ab = C.monodromy(tau, c)
        P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
        g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0)
        lam = abs(lam.real); mc8 = C.min_c(Ra, Rb, 8)
        al_, be_ = C.frobenius(lat, c)
        imB = float(C.local_B(lat, c, z0, g, lam, al_, be_, 0.05))
    return tau, al_, be_, (2 * np.pi / lam) * (1.0 / mc8 - imB)


def compare(acc, arr, D, reps, cls, apexes, deltas, label):
    worst, rows = 0.0, 0
    for ai in apexes:
        rec = acc[ai]; n = rec["n"]
        tau, al_, be_, Lrec = geometry_from_stored(rec)
        print("  apex %3d tau %+.4f%+.4fi (n %d): this run's L_max - stored %+.1e" % (ai, tau.real, tau.imag, n, Lrec - rec["L_max"]))
        for q in cls:
            a, b = LINES[reps[q]]; b = (b + n * a) % 1
            Ks, _ = channel_kernels(a, b, tau)
            for d in deltas:
                j = D.index(d); N2 = norms(Ks, tau, al_, be_, rec["L_max"] + d, 128, 96); cen = arr[ai, q, j]
                for u, s in enumerate(UNITS):
                    if Ks[s] is None or cen[u] == 0:
                        continue
                    worst = max(worst, abs(N2[s] / cen[u] - 1)); rows += 1
    print("  %s: %d channel values; largest relative difference to norms.npz %.1e" % (label, rows, worst))


if __name__ == "__main__":
    idx = json.loads((V / "norms_index.json").read_text())
    arr = np.load(V / "norms.npz")["norms"]
    acc = sorted([json.loads(l) for l in (V / "accessory.jsonl").read_text().splitlines() if l.strip()], key=lambda r: r["apex"])
    D = idx["DELTAS"]; reps = idx["class_rep_line"]
    order = sorted(range(len(acc)), key=lambda i: acc[i]["tau"][1])
    A_apex = [order[0], order[len(order) // 2], order[-1]]
    cls = []
    for c0 in CSTART:
        k = c0
        while LINES[reps[k]][0] % 1 in FAMILY or k in cls:
            k = (k + 1) % len(reps)
        cls.append(k)
    n1 = [i for i in order if acc[i]["n"] == 1]
    B_apex = [n1[0], n1[len(n1) // 2], n1[-1]]
    print("POST HOC THIRD OPINION at the census's own levels (stored L_max + delta); classes %s; n = 1 apexes: %d of %d" % (cls, len(n1), len(acc)))
    print("(A) the pre-registered selection, apexes %s, delta (0, 0.5, 4)" % A_apex)
    compare(acc, arr, D, reps, cls, A_apex, (0.0, 0.5, 4.0), "(A)")
    print("(B) extension: n = 1 apexes %s at delta (0, 0.5, 4, 10); and delta 10 at %s" % (B_apex, A_apex))
    compare(acc, arr, D, reps, cls, B_apex, (0.0, 0.5, 4.0, 10.0), "(B1) n = 1 apexes")
    compare(acc, arr, D, reps, cls, A_apex, (10.0,), "(B2) delta 10 at (A)'s apexes")
    print("third_opinion_posthoc exit 0")
