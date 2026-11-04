"""chat1, 2026-10-28: THE EXACT END, the data-free half of the relay's question 2 (THE CLASS AND THE END, 422cd8ecd).
Committed before its one run, with its expectations stated here. No data are read or compared.

The frame takes the end only through 2 pi L + c_s, the small-cut norm of the channel kernel K_s = P_s / R_s (B1656's cA,
B1726's compute()). B1667 computed the exact norm over the Dirichlet cell minus each canonical horoball, but only for
B1654's untwisted kernels. This script computes the exact norms of the frame's twisted kernels over the same regions (B1667's
own geometry: its accessory parameter, Frobenius series, horocycle radius and Dirichlet cell, imported unchanged), at four of
the six's rows. It then recomputes the frame's six ratios with the exact norms in place of 2 pi L + c_s.

Expectations, stated before the run:
  C0 (control), at tau = 0.25 + 3.0i: L_max, L_2 and B1667's untwisted N_max, N_2 reproduce B1667's committed json to
     1e-6 (relative).
  C1, at L_2: the twisted exact norms agree with 2 pi L_2 + c_s to within 1% in every channel, sector and row.
  C2 (read-out), at L_max: the exact norms lie below 2 pi L_max + c_s, by roughly the untwisted kernels' 5-18%; the
     channel spread changes by a few per cent; the frame's six log ratios move by less than 0.1 (the measure's 10% floor).
     If any of the six moves by more than 0.1 in ln at any row, the chi2_six recomputation (a look) is warranted, and it is
     sealed separately.
Rows (|Re tau| <= 1/2, as B1667's Dirichlet cell needs; T: (tau, a, b) -> (tau + 1, a, b - a) maps each to the original):
  R1 (2/5, 23/30) at 0.269 + 3.037i    B1786's best row
  R2 (2/5, 7/30)  at -0.237 + 3.023i   the horocycle test's L_max optimum, (2/5, 5/6) at 0.763 + 3.023i, moved by T^-1
  R3 (2/5, 1/10)  at 0.3145 + 3.0345i  P-373's continuous optimum on the order-10 class
  R4 (2/5, 4/25)  at 0.5 + 3.03i
The readings: (S~, S, S), the six's, and every reading per sector for the ratios.
Run:  python3 -B exact_end.py <main_checkout>        (main at 680d29e1c or later; B1667's and B1726's files unchanged)"""
import sys, json, math, pathlib, importlib.util, time
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
_spec = importlib.util.spec_from_file_location("b1667", ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py")
C = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(C)
M = K._modules(); B, te = M["B"], M["te"]
A25 = Fr(2, 5)
ROWS = [("R1", complex(0.269, 3.037), Fr(23, 30)), ("R2", complex(-0.237, 3.023), Fr(7, 30)),
        ("R3", complex(0.3145, 3.0345), Fr(1, 10)), ("R4", complex(0.5, 3.03), Fr(4, 25))]
CONTROL = complex(0.25, 3.0)


def geometry(tau, c):
    """B1667's point(), the geometric part: L_max, L_2 and the Frobenius series that define the horoball."""
    lat, z0, Aa, Ab = C.monodromy(tau, c)
    P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0); lam = abs(lam.real)
    mc8 = C.min_c(Ra, Rb, 8)
    al, be = C.frobenius(lat, c)
    ib = [float(C.local_B(lat, c, z0, g, lam, al, be, e)) for e in (0.1, 0.05)]
    L_max = (2 * np.pi / lam) * (1.0 / mc8 - ib[1]); L_2 = np.pi - (2 * np.pi / lam) * ib[1]
    return {"al": al, "be": be, "L_max": float(L_max), "L_2": float(L_2), "cusp_area": float(lam * mc8)}


def twisted_norms(tau, al, be, Lh, x, y, R, nth=96, ns=64):
    """B1667's horoball_norms with the frame's twisted kernel |P_s / R_s|^2 as the integrand (same cell, horoball and
    quadrature)."""
    from numpy.polynomial.legendre import leggauss
    br, rmaxf = C.voronoi(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns)
    tot = {s: 0.0 for s in B.UNITS}; margin = np.inf
    for a_, b_ in zip(br[:-1], br[1:]):
        th = 0.5 * (b_ - a_) * xg + 0.5 * (b_ + a_); wt = 0.5 * (b_ - a_) * wg
        rmax = rmaxf(th)
        rh = [C.horocycle_radius(al, be, Lh, t_, min(0.95, 1.1 * rm)) for t_, rm in zip(th, rmax)]
        if any(v is None for v in rh):
            raise RuntimeError("the horocycle does not close inside the cell at tau = %s" % tau)
        rh = np.array(rh, dtype=float); margin = min(margin, float(np.min(rmax - rh)))
        s_hi = np.log(rmax); s_lo = np.log(np.minimum(rh, rmax))
        s = 0.5 * (s_hi - s_lo)[:, None] * xs[None, :] + 0.5 * (s_hi + s_lo)[:, None]
        wsr = 0.5 * (s_hi - s_lo)[:, None] * ws[None, :]
        rr = np.exp(s); z = rr * np.exp(1j * th)[:, None]
        P = B.pairs(x, y, z, tau)
        for sc in B.UNITS:
            if abs(R[sc]) > 1e-12:
                tot[sc] += float(np.sum(wt[:, None] * wsr * np.abs(P[sc] / R[sc]) ** 2 * rr ** 2))
    return tot, margin


def higgs(tau):
    av = [complex(te.ev(cc, mp.mpc(tau.real, tau.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    return {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}


def ratios(reading, R, norms):
    u = {s: (math.sqrt(norms[s]) * R[s] if norms.get(s) is not None and norms[s] > 0 else 0) for s in B.UNITS}
    Mw = B.weighted_M(u); out = {}
    for rn, H in reading.items():
        sv = np.linalg.svd(B.coupling(H, Mw), compute_uv=False); out[rn] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return out


def main():
    t0 = time.time(); res = {}
    d = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())
    ref = min((p for p in d["points"] if p["where"] == "grid"), key=lambda p: abs(complex(*p["tau"]) - CONTROL))
    c = C.track(CONTROL); c, r0 = C.solve_accessory(CONTROL, c)
    G = geometry(CONTROL, c)
    Nmax, _ = C.horoball_norms(CONTROL, G["al"], G["be"], G["L_max"]); N2, _ = C.horoball_norms(CONTROL, G["al"], G["be"], G["L_2"])
    dev = max([abs(G["L_max"] / ref["L_max"] - 1), abs(G["L_2"] / ref["L_2"] - 1)]
              + [abs(Nmax[r] / ref["N_max"][str(r)] - 1) for r in (2, 3, 4)] + [abs(N2[r] / ref["N_2"][str(r)] - 1) for r in (2, 3, 4)])
    res["C0"] = {"tau": [CONTROL.real, CONTROL.imag], "ref_tau": ref["tau"], "max_rel_dev": dev, "holds": dev < 1e-6,
                 "L_max": G["L_max"], "L_2": G["L_2"]}
    print("C0 control at %s: max relative deviation from B1667's json %.2e -> %s" % (CONTROL, dev, "HOLDS" if dev < 1e-6 else "FAILS"), flush=True)
    col = M["col"]; tau_prev = CONTROL; rows = []
    for name, tau, b in ROWS:
        c, rr = C.newton_walk(tau_prev, c, tau); tau_prev = tau
        G = geometry(tau, c); rd = higgs(tau); w = float(A25) * tau + float(b)
        Lcol = {"L_max": float(np.interp(tau.imag, [q[0] for q in col], [q[1] for q in col])),
                "L_2": float(np.interp(tau.imag, [q[0] for q in col], [q[2] for q in col]))}
        row = {"row": name, "tau": [tau.real, tau.imag], "line": ["2/5", str(b)], "accessory_residual": rr,
               "L_exact": {"L_max": G["L_max"], "L_2": G["L_2"]}, "L_column": Lcol, "sectors": {}}
        for sec, (lf, rf) in K.SECT.items():
            x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau); cs = B.cA(x, yy, tau, R)
            S = {}
            for h in ("L_max", "L_2"):
                Nx, mg = twisted_norms(tau, G["al"], G["be"], G[h], x, yy, R)
                small = {s: (2 * math.pi * G[h] + cs[s] if cs[s] is not None else None) for s in B.UNITS}
                smallcol = {s: (2 * math.pi * Lcol[h] + cs[s] if cs[s] is not None else None) for s in B.UNITS}
                gap = {s: (Nx[s] / small[s] - 1 if small[s] else None) for s in B.UNITS}
                S[h] = {"exact": Nx, "small_cut": small, "small_cut_column_L": smallcol, "rel_gap": gap, "margin": mg,
                        "ratios_compute_like": ratios(rd, R, smallcol), "ratios_small_cut": ratios(rd, R, small),
                        "ratios_exact": ratios(rd, R, Nx)}
            row["sectors"][sec] = {"c_s": {s: cs[s] for s in B.UNITS}, **S}
        rows.append(row)
        print("%s done (%.0f s): L exact (%.4f, %.4f) against the column's (%.4f, %.4f)" % (
            name, time.time() - t0, G["L_max"], G["L_2"], Lcol["L_max"], Lcol["L_2"]), flush=True)
    res["rows"] = rows
    gaps2 = [abs(v) for r in rows for sec in r["sectors"].values() for v in sec["L_2"]["rel_gap"].values() if v is not None]
    res["C1"] = {"max_abs_rel_gap_L_2": max(gaps2), "holds": max(gaps2) < 0.01}
    print("C1 at L_2: max |exact / small-cut - 1| = %.4f -> %s" % (max(gaps2), "HOLDS" if max(gaps2) < 0.01 else "FAILS"))
    worst = 0.0
    for r in rows:
        for sec, v in r["sectors"].items():
            g = v["L_max"]["rel_gap"]
            print("C2 %s %-4s rel gap at L_max per channel: %s" % (r["row"], sec, {s: (None if g[s] is None else round(g[s], 4)) for s in B.UNITS}))
            for rn in ("S", "St"):
                a0, a1 = v["L_max"]["ratios_compute_like"][rn], v["L_max"]["ratios_exact"][rn]
                dl = [math.log(a1[i] / a0[i]) for i in range(2)]; worst = max(worst, max(abs(x) for x in dl))
                print("   reading %-2s ratios (m2/m3, m1/m3): compute-like %s -> exact %s ; d ln %s" % (
                    rn, ["%.4g" % q for q in a0], ["%.4g" % q for q in a1], ["%+.3f" % q for q in dl]))
    res["C2"] = {"max_abs_dln_ratio_L_max": worst, "look_warranted": worst > 0.1}
    print("C2 the largest |d ln ratio| at L_max, any sector, reading and row: %.3f -> the chi2 look is %s" % (
        worst, "WARRANTED" if worst > 0.1 else "NOT warranted"))
    (HERE / "exact_end.json").write_text(json.dumps(res, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o)))
    print("exact_end exit 0 (%.0f s)" % (time.time() - t0))


if __name__ == "__main__":
    main()
