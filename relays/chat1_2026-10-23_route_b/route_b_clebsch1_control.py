#!/usr/bin/env python3
"""POST HOC control, labelled (written after route_b_readout was read; committed before its own run): does the -3 do
the work, or the extra freedom?  Route (b)'s scan with the second direction's Clebsch set to 1 in every sector
(a flavour-blind second direction):
    S_quarks = S_leptons = S(h1) + kappa S(s),
everything else as route_b_scan.py (same base points, directions, kappa grid, horocycles), reading S~ for every sector.
If this control improves the six and nine as much as the Clebsch -3 does, the improvement is the two extra real
parameters, not the Georgi-Jarlskog factor.
    python3 -B route_b_clebsch1_control.py      # writes route_b_clebsch1_control.npz"""
import contextlib, importlib.util, io, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)

if __name__ == "__main__":
    data = np.zeros((len(rbs.BASE), len(rbs.CANDS), len(rbs.RHO), len(rbs.PHI), len(rbs.HORS), 10))
    for ib, (re_t, im_t, a, b) in enumerate(rbs.BASE):
        M = rbs.channels(re_t, im_t, a, b)
        v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
        n1 = np.linalg.norm(v1)
        u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
        dirs = {"h2": u2, "h3": u3}
        for ang in (0, 90, 180, 270):
            dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
        S1 = rbs.S_of(v1)
        for ic, cn in enumerate(rbs.CANDS):
            Ss = rbs.S_of(dirs[cn])
            for ir, rho in enumerate(rbs.RHO):
                for ip, phi in enumerate(rbs.PHI):
                    Sx = S1 + rho * np.exp(1j * phi) * n1 * Ss
                    for ih, which in enumerate(rbs.HORS):
                        data[ib, ic, ir, ip, ih] = rbs.outputs(M, which, Sx, Sx, "St_all")
        print(f"base {ib + 1}/{len(rbs.BASE)} done", flush=True)
    np.savez_compressed(HERE / "route_b_clebsch1_control.npz", data=data)
