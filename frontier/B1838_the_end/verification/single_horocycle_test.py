"""P-421, test (c), data-free: is there ONE horocycle whose EXACT norms equal the small-cut weights 2 pi L_max + c_s in every
channel and sector at once? Per row, sector and channel s: solve N_s(Lh) = 2 pi L_max + c_s for Lh (the exact horoball norm
of the twisted kernel, the web seat's instrument with B1667's geometry, unchanged); report the spread of those Lh. A spread
far above the quadrature's own error means the candidate's weights are the norm of no horoball cut. Frame quantities only."""
import importlib.util, math, sys, pathlib
import numpy as np
SEAT = pathlib.Path(__file__).resolve().parent   # exact_end_web_seat.py: the web seat's instrument at 4aa66ca45, byte-faithful
MAIN = str(pathlib.Path(__file__).resolve().parents[3])
sys.argv = [sys.argv[0], MAIN]
spec = importlib.util.spec_from_file_location("ee", SEAT / "exact_end_web_seat.py"); ee = importlib.util.module_from_spec(spec); spec.loader.exec_module(ee)
C, B, K = ee.C, ee.B, ee.K
c = C.track(ee.CONTROL); c, _ = C.solve_accessory(ee.CONTROL, c); tau_prev = ee.CONTROL
for name, tau, b in [r for r in ee.ROWS if r[0] in ("R3", "R1")]:
    c, _ = C.newton_walk(tau_prev, c, tau); tau_prev = tau
    G = ee.geometry(tau, c); w = float(ee.A25) * tau + float(b)
    Ls = [G["L_max"] + d for d in (0.0, 0.25, 0.5, 0.75, 1.0)]
    allL = []; qerr = 0.0
    for sec, (lf, rf) in K.SECT.items():
        x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau); cs = B.cA(x, yy, tau, R)
        N = {s: [] for s in B.UNITS}
        for Lh in Ls:
            Nx, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R)
            for s in B.UNITS: N[s].append(Nx[s])
        # quadrature check at L_max: a finer grid
        Nf, _ = ee.twisted_norms(tau, G["al"], G["be"], Ls[0], x, yy, R, nth=144, ns=96)
        sol = {}
        for s in B.UNITS:
            if cs[s] is None or abs(R[s]) < 1e-12: continue
            qerr = max(qerr, abs(Nf[s] - N[s][0]) / abs(N[s][0]))
            target = 2 * math.pi * G["L_max"] + cs[s]
            Lh_s = float(np.interp(target, N[s], Ls)) if N[s][0] <= target <= N[s][-1] else None
            sol[s] = Lh_s
            if Lh_s is not None: allL.append(Lh_s)
        print("%s %-4s L_max %.4f ; level where exact = small-cut, per channel: %s" % (name, sec, G["L_max"],
              {s: (None if v is None else round(v, 4)) for s, v in sol.items()}), flush=True)
    print("%s: over every channel and sector, the solved levels span %.4f .. %.4f (spread %.4f); quadrature relative error at L_max %.1e" % (
        name, min(allL), max(allL), max(allL) - min(allL), qerr), flush=True)
