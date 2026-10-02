#!/usr/bin/env python3
"""A search for the boundary-parabolic points of the rank-three branch: homotopies from many starting points
(s, phase) of the branch.  usage: search_parabolic.py <slice> <of>   -> parabolic_search_<slice>.json"""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import branch_obstruction as bo, branch_follow as bf, triplet_spectrum as ts, branch_parabolic as bp
from mpmath import mp, mpf, mpc, nstr, exp, pi, norm, zeros, inverse, eye, svd_c, log, det
mp.dps = 60
bp.print = lambda *a, **k: None
STARTS = [(mpf(s), k) for s in ("0.1", "0.2", "0.3", "0.45") for k in range(8)]
def invariants(R):
    tr = lambda m: m[0, 0] + m[1, 1] + m[2, 2]
    lam = R[1] * R[2] * inverse(R[1]) * inverse(R[2]); c1, c2, c3 = bp.coeffs(R[3]); t0 = c1 / 3
    return dict(tr_x=nstr(tr(R[1]), 30), tr_y=nstr(tr(R[2]), 30), tr_xy=nstr(tr(R[1] * R[2]), 30), tr_xinv=nstr(tr(inverse(R[1])), 30), tr_longitude=nstr(tr(lam), 30),
                rank_longitude_minus_1=sum(1 for sv in svd_c(lam - eye(3), compute_uv=False) if abs(sv) > mpf(10) ** (-12)),
                rank_meridian_minus_scalar=sum(1 for sv in svd_c(R[3] - t0 * eye(3), compute_uv=False) if abs(sv) > mpf(10) ** (-12)), t0=nstr(t0, 30), algebra_dimension=bf.burnside(R),
                residual=nstr(norm(bo.G(R, {g: zeros(3) for g in (1, 2, 3)})), 3), f=[nstr(abs(c), 3) for c in bp.f(R)])
def spectra(R):
    c1, c2, c3 = bp.coeffs(R[3]); Tn = R[3] / (c1 / 3); z4 = exp(2j * pi / 4); out = {}
    for (i, j) in itertools.product(range(4), repeat=2):
        try:
            E, tau = ts.monodromy_on_H1({1: z4 ** i * R[1], 2: z4 ** j * R[2]}, Tn)
            big = max(E, key=lambda e: abs(log(e))); out["%d,%d" % (i, j)] = dict(nearest_to_one=nstr(min(abs(e - 1) for e in E), 3), e_plus_inverse=nstr(big + 1 / big, 25), abs_log=nstr(abs(log(big)), 15))
        except AssertionError as ex: out["%d,%d" % (i, j)] = dict(error=str(ex)[:60])
    return out
if __name__ == "__main__":
    sl, of = int(sys.argv[1]), int(sys.argv[2]); recs = []
    for n, (s, k) in enumerate(STARTS):
        if n % of != sl: continue
        phase = exp(2j * pi * k / 8); rec = dict(s=nstr(s, 3), phase_index=k)
        try:
            R, R0 = ts.branch_rep(s, phase); f0 = bp.f(R); Rp = R; K = 24
            for k in range(1, K):                                  # the homotopy, stopping one step short of the target
                Rp, nb = bp.solve(Rp, [(1 - mpf(k) / K) * c for c in f0])
                assert nb < mpf(10) ** (-30), "not converged at step %d: %s" % (k, nstr(nb, 3))
            for _ in range(40):                                    # the target itself: convergence there can be linear
                Rp, nb = bp.solve(Rp, [mpc(0), mpc(0)], iters=6)
                if nb < mpf(10) ** (-45): break
            assert nb < mpf(10) ** (-25), "target not reached: %s" % nstr(nb, 3)
            rec.update(found=True, invariants=invariants(Rp), spectra=spectra(Rp))
            rec["matrices"] = {name: [[[nstr(Rp[g][i, j].real, 55), nstr(Rp[g][i, j].imag, 55)] for j in range(3)] for i in range(3)] for g, name in ((1, "x"), (2, "y"), (3, "t"))}
        except (AssertionError, ZeroDivisionError) as ex: rec.update(found=False, why=str(ex)[:100])
        recs.append(rec); print(rec["s"], k, rec["found"], rec.get("invariants", {}).get("tr_x", rec.get("why")), rec.get("invariants", {}).get("algebra_dimension"), flush=True)
        json.dump(recs, open(HERE / ("parabolic_search_%d.json" % sl), "w"), indent=1)
