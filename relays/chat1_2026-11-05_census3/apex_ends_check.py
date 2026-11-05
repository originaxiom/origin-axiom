"""The web seat, 2026-11-05: B1841's four ends at all 223 of B1839's apexes, checked from the census's accessory.jsonl by a
route independent of B1667's min|c| search (cc's P-699 ask 1; committed before accessory.jsonl is on main). Data-free.

At each apex, from the stored accessory parameter (B1667's geometry recomputed from it, as B1841's census.py does):
  - E3's half-period identity: the level of the horocycle through each half-period p with |p| < 0.9,
    L_W(p) = log(1/|p|) - Re g(p) (the Frobenius ratio g, no group search), against the stored L_max; the maximal
    horoball's boundary passes through the half-period it first touches (THE PRINCIPLED ENDS, E3);
  - the stored L_max and L_2 against the recomputed ones;
  - E1 = L_2, E2 = ln 2, E4 = L_2 - pi/2, and their offsets from L_max: delta_2 = ln 2 - L_max against Re g(1/2), and
    delta_4 = L_4 - L_max against pi(1/2 - 2/A_cusp), with A_cusp the stored cusp area;
  - the shortest lattice vector (E2's inradius 1/2 needs it to be 1).

    python3 apex_ends_check.py <main checkout with B1839's accessory.jsonl>
"""
import contextlib
import importlib.util
import io
import json
import math
import pathlib
import sys
from multiprocessing import Pool

import numpy as np

ROOT = pathlib.Path(sys.argv[1]).resolve()
SRC = ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py"
ACC = ROOT / "frontier" / "B1839_the_end_card" / "verification" / "accessory.jsonl"


def load():
    sp = importlib.util.spec_from_file_location("b1667", SRC)
    m = importlib.util.module_from_spec(sp)
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


C = load()


def shortest(t, n=6):
    return min(abs(a + b * t) for a in range(-n, n + 1) for b in range(-n, n + 1) if (a, b) != (0, 0))


def work(rec):
    tau = complex(*rec["tau"]); c = complex(*rec["c"])
    with contextlib.redirect_stdout(io.StringIO()):
        lat, z0, Aa, Ab = C.monodromy(tau, c)
        P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
        g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0)
        lam = abs(lam.real); mc8 = C.min_c(Ra, Rb, 8)
        al, be = C.frobenius(lat, c)
        imB = float(C.local_B(lat, c, z0, g, lam, al, be, 0.05))
    L_max = (2 * np.pi / lam) * (1.0 / mc8 - imB); L_2 = np.pi - (2 * np.pi / lam) * imB
    halves = {"1/2": 0.5, "tau/2": tau / 2, "(1+tau)/2": (1 + tau) / 2, "(tau-1)/2": (tau - 1) / 2}
    LW = {k: float(np.log(1 / abs(v)) - C.g_local(al, be, v).real) for k, v in halves.items() if abs(v) < 0.9}
    kmax = max(LW, key=LW.get)
    A = float(rec["cusp_area"])
    return dict(apex=rec["apex"], tau=tau, L_max=float(rec["L_max"]), L_2=float(rec["L_2"]), A=A,
                dLmax=abs(float(L_max) - rec["L_max"]), dL2=abs(float(L_2) - rec["L_2"]), LWmax=LW[kmax], kmax=kmax,
                reg_half=float(C.g_local(al, be, 0.5).real), short=shortest(tau))


if __name__ == "__main__":
    acc = [json.loads(l) for l in ACC.read_text(encoding="utf-8").splitlines() if l.strip()]
    acc = sorted(acc, key=lambda r: r["apex"])
    with Pool(4) as pool:
        R = pool.map(work, acc, chunksize=1)
    print("B1841's ENDS AT B1839's %d APEXES (data-free; from accessory.jsonl, B1667's instrument unchanged)" % len(R))
    for r in R:
        print("apex %3d tau %+.4f%+.4fi | L_max %.9f, L_W max %.9f at %s, diff %+.1e | recomputed L_max %.1e, L_2 %.1e | "
              "delta_2 %.5f vs Re g(1/2) %.5f | delta_4 %.5f vs pi(1/2 - 2/A) %.5f | delta_1 %.5f | shortest %.9f" % (
                  r["apex"], r["tau"].real, r["tau"].imag, r["L_max"], r["LWmax"], r["kmax"], r["LWmax"] - r["L_max"],
                  r["dLmax"], r["dL2"], math.log(2) - r["L_max"], r["reg_half"], r["L_2"] - math.pi / 2 - r["L_max"],
                  math.pi * (0.5 - 2 / r["A"]), r["L_2"] - r["L_max"], r["short"]))
    print("SUMMARY")
    print("  E3's half-period identity: largest |max_p L_W(p) - L_max| %.1e, median %.1e; contact half-period %s" % (
        max(abs(r["LWmax"] - r["L_max"]) for r in R), float(np.median([abs(r["LWmax"] - r["L_max"]) for r in R])),
        {k: sum(1 for r in R if r["kmax"] == k) for k in sorted(set(r["kmax"] for r in R))}))
    print("  stored against recomputed: L_max %.1e, L_2 %.1e" % (max(r["dLmax"] for r in R), max(r["dL2"] for r in R)))
    print("  delta_2 = ln 2 - L_max: %.5f-%.5f; largest |delta_2 - Re g(1/2)| %.1e" % (
        min(math.log(2) - r["L_max"] for r in R), max(math.log(2) - r["L_max"] for r in R),
        max(abs(math.log(2) - r["L_max"] - r["reg_half"]) for r in R)))
    print("  delta_4: %.5f-%.5f; largest |delta_4 - pi(1/2 - 2/A)| %.1e; delta_1: %.5f-%.5f" % (
        min(r["L_2"] - math.pi / 2 - r["L_max"] for r in R), max(r["L_2"] - math.pi / 2 - r["L_max"] for r in R),
        max(abs(r["L_2"] - math.pi / 2 - r["L_max"] - math.pi * (0.5 - 2 / r["A"])) for r in R),
        min(r["L_2"] - r["L_max"] for r in R), max(r["L_2"] - r["L_max"] for r in R)))
    print("  shortest lattice vector %.9f-%.9f" % (min(r["short"] for r in R), max(r["short"] for r in R)))
