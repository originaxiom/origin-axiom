"""P-688 (draft, audit room): THE FROZEN-ROW INSTRUMENT AT THE EXACT END — data-free.

B1835's card instrument (B1726's compute() Yukawa construction, returning the matrices, with the Dirac neutrino L nu^c)
with the end replaced by B1839's: the exact norm of each channel's twisted kernel over B1667's Dirichlet cell minus the
horoball at level L_max(tau) + delta (delta = inf: every channel's weight equal, the cusp limit). The web seat's
instrument (B1838's exact_end_web_seat.py) supplies the geometry, the norms (its twisted_norms, at B1839's (40, 28)),
the Higgs DR at tau and the coupling; tau is reduced to |Re tau| <= 1/2 by T^-1 as B1839 does.

    yukawas_exact(re_t, im_t, a, b, delta, sectors) -> {sector: {"S": Y, "St": Y}}, info
Never evaluates any held-out quantity by itself: it returns matrices; extraction belongs to a sealed card.
Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np

ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
CHARGES = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6), "nu": (-3, 0)}
NTH, NS = 40, 28
_M = {}


def mods():
    if not _M:
        argv = sys.argv; sys.argv = [argv[0], str(ROOT)]
        sp = importlib.util.spec_from_file_location("p688_ee", ROOT / "frontier" / "B1838_the_end" / "verification" / "exact_end_web_seat.py")
        ee = importlib.util.module_from_spec(sp); sp.loader.exec_module(ee); sys.argv = argv
        _M.update(ee=ee, C=ee.C, B=ee.B, solved=[])
    return _M


def accessory(tau):
    M = mods(); C, ee = M["C"], M["ee"]
    if not M["solved"]:
        c = C.track(ee.CONTROL); c, _ = C.solve_accessory(ee.CONTROL, c); M["solved"].append((ee.CONTROL, c))
    t0, c0 = min(M["solved"], key=lambda q: abs(q[0] - tau))
    c, res = C.newton_walk(t0, c0, tau); M["solved"].append((tau, c)); return c, res


def reduce(tau, a, b):
    a, b = Fr(a), Fr(b)
    while tau.real > 0.5: tau, b = tau - 1, (b + a) % 1
    while tau.real < -0.5: tau, b = tau + 1, (b - a) % 1
    return tau, a, b


def yukawas_exact(re_t, im_t, a, b, delta, sectors=("up", "down", "lep", "nu")):
    M = mods(); ee, B = M["ee"], M["B"]
    tau, a, b = reduce(complex(re_t, im_t), a, b)
    key = (round(tau.real, 12), round(tau.imag, 12))
    if key not in M.setdefault("geo", {}):
        c, res = accessory(tau); M["geo"][key] = (ee.geometry(tau, c), ee.higgs(tau), res)
    G, rd, res = M["geo"][key]; w = float(a) * tau + float(b)
    Lh = None if delta == math.inf else G["L_max"] + delta
    Y = {}
    for sec in sectors:
        ql, qr = CHARGES[sec]
        x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau)
        if Lh is None:
            N = {s: (1.0 if abs(R[s]) > 1e-12 else 0.0) for s in B.UNITS}
        else:
            N, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R, nth=NTH, ns=NS)
        u = {s: (math.sqrt(N[s]) * R[s] if N.get(s) is not None and N[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        Y[sec] = {rn: B.coupling(H, Mw) for rn, H in rd.items()}
    return Y, {"tau_reduced": [tau.real, tau.imag], "line_reduced": [str(a), str(b)], "L_max": G["L_max"], "L_2": G["L_2"],
               "L_h": Lh, "accessory_residual": res}


def ratios_of(Y):
    sv = np.linalg.svd(Y, compute_uv=False); return [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
