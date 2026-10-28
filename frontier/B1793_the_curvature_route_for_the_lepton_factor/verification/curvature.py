"""P-397, the curvature route (data-free): B1656's channel norms c_s with a zero-net-degree hypercharge curvature on the fibre.
A pair kernel K_s of a sector is a section of L_x (x) L_y, charge Q = q_L + q_R (down +3, leptons +3, up -3), so a hermitian
metric deformed by a periodic potential phi (curvature dd^c(Q phi), zero net degree) weights its norm by exp(-Q phi).  The
weighted c_s replaces B1656's cA in B1726's compute() pipeline (Higgs DR, L_max, readings S for down and leptons); everything
else is the instrument's.  Reports R2 = (m2/m3)_e/(m2/m3)_d and R1 = (m1/m3)_d/(m1/m3)_e against the profile and eps.
    python3 -B curvature.py"""
import sys, json, math, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
from numpy.polynomial.legendre import leggauss
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
M = C._modules(); B, te, col = M["B"], M["te"], M["col"]


def lattice(z, t):
    y1 = z.imag / t.imag; x1 = z.real - y1 * t.real; return x1, y1


PROFILES = {
    "cos2pi_x1": lambda x1, y1: np.cos(2 * np.pi * x1),
    "cos4pi_x1": lambda x1, y1: np.cos(4 * np.pi * x1),
    "cos2pi_y1": lambda x1, y1: np.cos(2 * np.pi * y1),
    "cos4pi_y1": lambda x1, y1: np.cos(4 * np.pi * y1),
    "asym": lambda x1, y1: np.cos(2 * np.pi * x1) + 0.5 * np.sin(4 * np.pi * x1 + 0.3) + 0.5 * np.cos(2 * np.pi * y1 + 0.7),
}


def cA_w(x, y, t, R, Q, prof, eps_amp, eps=1e-5, nth=96, ns=64):
    """B1656's cA with the integrand weighted by exp(-Q eps_amp phi(z)); the subtraction uses the weight at z = 0, since
    near the pole |K_s|^2 ~ 1/|z|^2 and the divergence is 2 pi W(0) log(1/eps); the disc's constant term likewise times W(0)"""
    A0 = B.a0_of(x, y, t, R)
    W = (lambda z: np.exp(-Q * eps_amp * PROFILES[prof](*lattice(z, t)))) if eps_amp else (lambda z: np.ones_like(np.abs(z)))
    W0 = float(np.real(W(np.array([0j])))[0])
    br = B.vangles(t); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = {s: 0.0 for s in B.UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a); wt = 0.5 * (b - a) * wg
        hi = np.log(B.rmax_np(th, t)); lo = math.log(eps)
        sg = 0.5 * (hi - lo)[:, None] * xs[None, :] + 0.5 * (hi + lo)[:, None]; w2 = 0.5 * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg); z = rr * np.exp(1j * th)[:, None]; P = B.pairs(x, y, z, t); Wz = np.real(W(z))
        for s in B.UNITS:
            if abs(R[s]) > 1e-12: tot[s] += np.sum(wt[:, None] * w2 * Wz * np.abs(P[s] / R[s]) ** 2 * rr ** 2)
    return {s: (float(tot[s] - 2 * np.pi * W0 * math.log(1 / eps) + np.pi * eps ** 2 * W0 * abs(A0[s]) ** 2) if abs(R[s]) > 1e-12 else None) for s in B.UNITS}


def ratios(re_t, im_t, a, b, prof, eps_amp, c_fn):
    import mpmath as mp
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))
    out = {}
    for sec, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        ql, qr = B.SIXY[lf], B.SIXY[rf]; Q = ql + qr
        x, yy = B.sector_twists(w, t, ql, qr); R = B.residues(x, yy, t); c = c_fn(x, yy, t, R, Q, prof, eps_amp)
        # the cut norm is 2 pi W(0) L + c (the referee's correction, 2026-10-28): the cusp's log term carries the weight at z = 0
        W0 = float(np.exp(-Q * eps_amp * PROFILES[prof](*lattice(np.array([0j]), t)))[0]) if eps_amp else 1.0
        u = {s: (math.sqrt(2 * math.pi * W0 * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * W0 * L + c[s] > 0 else 0) for s in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
        out[sec] = (float(sv[1] / sv[0]), float(sv[2] / sv[0])); out[sec + "_Q"] = Q
    R2 = out["lep"][0] / out["down"][0]; R1 = out["down"][1] / out["lep"][1]
    return R2, R1, out


if __name__ == "__main__":
    res = {}
    # control: eps = 0 with the weighted routine equals B1726's own compute() (the instrument)
    for (a, b) in ((Fr(2, 5), Fr(1, 10)), (Fr(2, 5), Fr(23, 30))):
        for im_t in (3.0, 6.0):
            ref = C.compute(0.3, im_t, a, b)
            R2r = ref["lep|L_max|S"][0] / ref["down|L_max|S"][0]; R1r = ref["down|L_max|S"][1] / ref["lep|L_max|S"][1]
            R2, R1, _ = ratios(0.3, im_t, a, b, "cos2pi_x1", 0.0, cA_w)
            print("control (%s, %s) Im tau %g: instrument R2 %.6f R1 %.6f | weighted routine at eps 0: R2 %.6f R1 %.6f" % (a, b, im_t, R2r, R1r, R2, R1), flush=True)
            res["control|%s|%s|%g" % (a, b, im_t)] = [R2r, R1r, R2, R1]
            for prof in PROFILES:
                for e in (0.05, 0.1, 0.2):
                    R2, R1, o = ratios(0.3, im_t, a, b, prof, e, cA_w)
                    res["%s|%s|%g|%s|%g" % (a, b, im_t, prof, e)] = [R2, R1]
                    print("  (%s, %s) Im tau %g  %-10s eps %.2f   R2 %.5f  R1 %.5f" % (a, b, im_t, prof, e, R2, R1), flush=True)
    json.dump(res, open(HERE / "curvature.json", "w"), indent=1)
    print("curvature exit 0")
