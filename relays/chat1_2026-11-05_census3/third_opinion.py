"""The web seat, 2026-11-05: a third opinion of B1839's census (cc's ask 2, P-687). Data-free.

Recomputes B1839's exact twisted norms at 3 apexes x 3 levels x 5 Higgs-twist classes with this seat's own code, and
compares them with the census's norms.npz. Imported: B1667's sealed instrument (the accessory solve, the Frobenius series,
the horocycle radius, the Dirichlet cell) and the frame's pairing module (only to read each channel's two multipliers
and, as a control, the pairing itself at six sample points). Not imported: B1839's census.py, B1838's
exact_end_web_seat.py, or this seat's own exact_end.py.

Independent here:
  - the accessory parameter, re-solved by Newton (B1667's solve_accessory) from the census's value, at each apex;
  - the kernel: K_s(z) = e^{2 pi i alpha z} theta1'(0) theta1(z + v) / (theta1(z) theta1(v)), v = alpha tau - beta, with
    (alpha, beta) the channel's measured character (alpha taken in (-1/2, 1/2]), theta1 by its own q-series; by L1
    (THE HIGGS-TWIST LAW) it is the residue-1 kernel P_s/R_s, which the control checks;
  - the quadrature: Gauss-Legendre per cell edge in theta and in log r between the horocycle and the cell's edge, at
    (96, 64) and (128, 96) nodes (the census uses (40, 28)).
The selection is fixed before the census is read:
  - apexes: the reduced apexes of least, median and greatest Im tau (the census's accessory.jsonl);
  - levels: delta = 0.0, 0.5 and 4.0;
  - classes: from the class indices 0, 42, 85, 127 and 169, each moved forward to the first class whose representative
    line is not on the family's slope (2/5, 3/5); each class also by a second representative of this seat's choosing,
    (k1/3, k2/3) for the class key (k1, k2), which the Higgs-twist law says gives the same norms.

    python3 third_opinion.py <main checkout with B1839's census outputs>
"""
import contextlib
import importlib.util
import io
import json
import math
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT = pathlib.Path(sys.argv[1]).resolve()
V = ROOT / "frontier" / "B1839_the_end_card" / "verification"
FAMILY = (Fr(2, 5), Fr(3, 5))
UNITS = ("1", "i", "j", "k")
DSEL = (0.0, 0.5, 4.0)
CSTART = (0, 42, 85, 127, 169)
ZS = np.array([0.11 + 0.07j, -0.19 + 0.13j, 0.07 - 0.21j, 0.23 + 0.31j, -0.29 - 0.17j, 0.37 + 0.05j])


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


C = load("b1667", ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py")
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
argv0 = sys.argv
sys.argv = [argv0[0], str(ROOT)]
B53 = load("b1753_census", ROOT / "frontier" / "B1753_the_six_on_the_five_ality_lines" / "verification" / "census.py")
sys.argv = argv0
LINES = [(Fr(a), Fr(b)) for a, b in B53._K().lines()]


def theta1(z, tau, n=14):
    q = np.exp(1j * np.pi * tau)
    k = np.arange(n)
    return 2 * np.sum(((-1) ** k) * q ** ((k + 0.5) ** 2) * np.sin((2 * k + 1) * np.pi * np.asarray(z)[..., None]), axis=-1)


def dtheta1_0(tau, n=14):
    q = np.exp(1j * np.pi * tau)
    k = np.arange(n)
    return 2 * np.pi * np.sum(((-1) ** k) * (2 * k + 1) * q ** ((k + 0.5) ** 2))


def kron(alpha, beta, tau):
    v = alpha * tau - beta
    d0, tv = dtheta1_0(tau), theta1(v, tau)
    return lambda z: np.exp(2j * np.pi * alpha * z) * d0 * theta1(z + v, tau) / (theta1(z, tau) * tv)


def channel_kernels(a, b, tau):
    """the down sector's four residue-1 kernels on the line (a, b), with the control against P_s/R_s"""
    w = float(a) * tau + float(b)
    x, y = B.sector_twists(w, tau, 1, 2)
    with contextlib.redirect_stdout(io.StringIO()):
        R = B.residues(x, y, tau)
    P0 = B.pairs(x, y, ZS, tau); P1 = B.pairs(x, y, ZS + 1, tau); P2 = B.pairs(x, y, ZS + tau, tau)
    out, ctrl = {}, 0.0
    for s in UNITS:
        if abs(R[s]) <= 1e-12:
            out[s] = None
            continue
        al = float(np.angle(np.mean(P1[s] / P0[s])) / (2 * np.pi)); be = float(np.angle(np.mean(P2[s] / P0[s])) / (2 * np.pi))
        al = al - round(al)
        K = kron(al, be, tau)
        ctrl = max(ctrl, float(np.max(np.abs(K(ZS) - P0[s] / R[s])) / np.max(np.abs(P0[s] / R[s]))))
        out[s] = K
    return out, ctrl


def norms(Ks, tau, al_, be_, Lh, nth, ns):
    br, rmaxf = C.voronoi(tau); xt, wt = leggauss(nth); xs, ws = leggauss(ns)
    tot = {s: 0.0 for s in UNITS}
    for t0, t1 in zip(br[:-1], br[1:]):
        th = 0.5 * (t1 - t0) * xt + 0.5 * (t1 + t0); wth = 0.5 * (t1 - t0) * wt
        rmax = rmaxf(th)
        rh = np.array([C.horocycle_radius(al_, be_, Lh, t, min(0.95, 1.1 * rm)) for t, rm in zip(th, rmax)], dtype=float)
        s_hi, s_lo = np.log(rmax), np.log(np.minimum(rh, rmax))
        s = 0.5 * (s_hi - s_lo)[:, None] * xs[None, :] + 0.5 * (s_hi + s_lo)[:, None]
        wsr = 0.5 * (s_hi - s_lo)[:, None] * ws[None, :]
        r = np.exp(s); z = r * np.exp(1j * th)[:, None]
        for sc, K in Ks.items():
            if K is not None:
                tot[sc] += float(np.sum(wth[:, None] * wsr * np.abs(K(z)) ** 2 * r ** 2))
    return tot


if __name__ == "__main__":
    idx = json.loads((V / "norms_index.json").read_text())
    arr = np.load(V / "norms.npz")["norms"]
    acc = [json.loads(l) for l in (V / "accessory.jsonl").read_text().splitlines() if l.strip()]
    acc = sorted(acc, key=lambda r: r["apex"])
    D = idx["DELTAS"]; jl = [D.index(d) for d in DSEL]
    order = sorted(range(len(acc)), key=lambda i: acc[i]["tau"][1])
    apexes = [order[0], order[len(order) // 2], order[-1]]
    reps = idx["class_rep_line"]; keys = idx["class_keys"]
    cls = []
    for c0 in CSTART:
        k = c0
        while LINES[reps[k]][0] % 1 in FAMILY or k in cls:
            k = (k + 1) % len(reps)
        cls.append(k)
    print("THIRD OPINION of B1839's census: apexes %s, levels %s, classes %s (norms.npz shape %s)" % (apexes, DSEL, cls, list(arr.shape)))
    worst, conv, ctrl_max, alt_worst = 0.0, 0.0, 0.0, 0.0
    for ai in apexes:
        rec = acc[ai]; tau = complex(*rec["tau"]); n = rec["n"]
        with contextlib.redirect_stdout(io.StringIO()):
            c, res = C.solve_accessory(tau, complex(*rec["c"]))
            lat, z0, Aa, Ab = C.monodromy(tau, c)
            P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
            g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0)
            lam = abs(lam.real); mc8 = C.min_c(Ra, Rb, 8)
            al_, be_ = C.frobenius(lat, c)
            imB = float(C.local_B(lat, c, z0, g, lam, al_, be_, 0.05))
        L_max = (2 * np.pi / lam) * (1.0 / mc8 - imB)
        print("apex %d: tau %.4f%+.4fi (n %d); |c - census c| %.1e, residual %.1e; L_max %.6f against the census's %.6f" % (
            ai, tau.real, tau.imag, n, abs(c - complex(*rec["c"])), float(np.max(np.abs(res))), L_max, rec["L_max"]))
        for q in cls:
            a, b = LINES[reps[q]]; b = (b + n * a) % 1
            Ks, ctrl = channel_kernels(a, b, tau); ctrl_max = max(ctrl_max, ctrl)
            k1, k2 = Fr(keys[q][0]), Fr(keys[q][1])
            Ka, ctrl2 = channel_kernels(k1 / 3, (k2 / 3 + n * k1 / 3) % 1, tau); ctrl_max = max(ctrl_max, ctrl2)
            for j, d in zip(jl, DSEL):
                Lh = L_max + d
                N1 = norms(Ks, tau, al_, be_, Lh, 96, 64)
                N2 = norms(Ks, tau, al_, be_, Lh, 128, 96)
                NA = norms(Ka, tau, al_, be_, Lh, 96, 64)
                cen = arr[ai, q, j]
                row = []
                for u, s in enumerate(UNITS):
                    if Ks[s] is None or cen[u] == 0:
                        row.append("-")
                        continue
                    e = abs(N2[s] / cen[u] - 1); worst = max(worst, e)
                    conv = max(conv, abs(N1[s] / N2[s] - 1))
                    if Ka[s] is not None:
                        alt_worst = max(alt_worst, abs(NA[s] / N1[s] - 1))
                    row.append("%.8g/%.8g" % (N2[s], cen[u]))
                print("    class %3d %s (line %s, %s) delta %.1f: mine/census %s" % (q, keys[q], a, b, d, " ".join(row)))
    print("SUMMARY")
    print("  kernel control (Kronecker against P_s/R_s at six points): largest relative difference %.1e" % ctrl_max)
    print("  this seat's quadrature, (96, 64) against (128, 96): largest relative difference %.1e" % conv)
    print("  this seat (128, 96) against the census's norms.npz: largest relative difference %.1e" % worst)
    print("  a second representative per class, (k1/3, k2/3), against the census's line (96, 64 both): largest %.1e" % alt_worst)
