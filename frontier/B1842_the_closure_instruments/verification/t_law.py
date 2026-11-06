"""B1842's C-T control, made genuine (Review 76's R76-3; data-free). The old C-T compared yukawas_exact at (tau, (a, b))
with yukawas_exact at (tau + 1, (a, b - a)) -- but yukawas_exact reduces tau by T-steps (b -> b + a) first, so both calls
had identical inputs: a tautology. The genuine T-law runs the theta machinery (the Higgs, the sector twists, the
residues) at the UNREDUCED tau + 1; the torus's geometry and the twisted norms are the torus's own (B1667's voronoi needs
a reduced tau; the fundamental-domain integral is T-invariant by construction), so the test runs at delta = inf, where
no norm enters. Result: the singular values are T-invariant to machine precision; the matrices are NOT equal up to
phases (|Y| entrywise differs by about 8 %), i.e. T acts on the generations by a non-diagonal unitary."""
import sys, math, pathlib
from fractions import Fraction as F
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_card_instrument as X


def yukawas_unreduced(re_t, im_t, a, b, sectors=("up", "down", "lep", "nu")):
    M = X.mods(); ee, B = M["ee"], M["B"]
    tau = complex(re_t, im_t); a, b = F(a), F(b)
    rd = ee.higgs(tau)
    w = float(a) * tau + float(b)
    Y = {}
    for sec in sectors:
        ql, qr = X.CHARGES[sec]
        x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau)
        N = {s: (1.0 if abs(R[s]) > 1e-12 else 0.0) for s in B.UNITS}
        u = {s: (math.sqrt(N[s]) * R[s] if N[s] > 0 else 0) for s in B.UNITS}
        Y[sec] = {rn: B.coupling(H, B.weighted_M(u)) for rn, H in rd.items()}
    return Y


def t_law(points=((0.31, 2.9, F(1, 3), F(1, 4)), (-0.2, 3.1, F(2, 5), F(3, 10)))):
    sv = 0.0; ent = 0.0; taut = 0.0
    for (re_t, im_t, a, b) in points:
        Y1, _ = X.yukawas_exact(re_t, im_t, a, b, math.inf)
        Yt, _ = X.yukawas_exact(re_t + 1, im_t, a, (b - a) % 1, math.inf)
        Y2 = yukawas_unreduced(re_t + 1, im_t, a, (b - a) % 1)
        for sec in X.CHARGES:
            for rn in ("S", "St"):
                s1 = np.linalg.svd(Y1[sec][rn], compute_uv=False)
                s2 = np.linalg.svd(Y2[sec][rn], compute_uv=False); st = np.linalg.svd(Yt[sec][rn], compute_uv=False)
                sv = max(sv, float(np.max(np.abs(s1 - s2) / s1[0]))); taut = max(taut, float(np.max(np.abs(s1 - st) / s1[0])))
                ent = max(ent, float(np.max(np.abs(np.abs(Y1[sec][rn]) - np.abs(Y2[sec][rn]))) / float(np.max(np.abs(Y1[sec][rn])))))
    return sv, ent, taut


if __name__ == "__main__":
    sv, ent, taut = t_law()
    print(f"the old C-T (both calls reduced to identical inputs): {taut:.1e} (a tautology)")
    print(f"the genuine T-law, singular values (unreduced theta machinery at tau + 1): {sv:.1e} -> {'HOLDS' if sv < 1e-10 else 'FAILS'}")
    print(f"the genuine T-law, |Y| entrywise: {ent:.1e} -> the matrices are related by a non-diagonal unitary, not by phases")
