"""STEP A v2 -- the mass map's rank at the symmetric configurations (data-free): python3 -I analysis_points.py
At (i, (1,-1,0)/sqrt2) and (omega, eigenvectors of P L^-1) the stabiliser acts on the whole tangent space without a fixed
vector, so every smooth invariant function -- each heavy eigenvalue among them -- is stationary: the RAW Jacobian should
vanish.  (A first version used d(log m^2), which is singular where a singlet vanishes -- E6(i) = 0, E4(omega) = 0 make some
heavy states massless there -- and read those log-singularities as rank; it is kept as analysis_points_logjac_superseded.)"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
import mpmath as mp
import step_a_v2 as S
from search import Model, make_copies
from model import PMAT, LINV
mp.mp.dps = S.DPS
w = mp.mpc(mp.mpf(-1) / 2, mp.sqrt(3) / 2)          # omega at full precision
ev, U = np.linalg.eig(PMAT @ LINV)
out = {}
for menu in ("Z", "H"):
    for n in (2, 4, 8):
        model = Model(make_copies(n, menu), 0.5, 0.005, 0.3)
        rows = []
        for name, tau, Sv in [("i", 1j, np.array([1, -1, 0]) / np.sqrt(2))] + [("omega_%d" % k, w, U[:, k]) for k in range(3)]:
            m = S.MPModel(model, mp.mpc(tau), Sv)
            h = mp.mpf("1e-12"); z = [mp.mpf(0)] * 6
            e0 = m.eigs(z); scale = max(abs(x) for x in e0)
            J = mp.matrix(len(e0), 6)
            for a in range(6):
                xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
                ep, em = m.eigs(xp), m.eigs(xm)
                for i in range(len(e0)):
                    J[i, a] = (ep[i] - em[i]) / (2 * h) / scale            # raw, scaled by the largest eigenvalue
            sv = S.svals(J)
            # control: the same Jacobian just off the point (tau shifted by 0.01 + 0.02i) is not small
            m2 = S.MPModel(model, mp.mpc(tau) + mp.mpc("0.01", "0.02"), Sv)
            J2 = mp.matrix(len(e0), 6); e2 = m2.eigs(z); sc2 = max(abs(x) for x in e2)
            for a in range(6):
                xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
                ep, em = m2.eigs(xp), m2.eigs(xm)
                for i in range(len(e2)):
                    J2[i, a] = (ep[i] - em[i]) / (2 * h) / sc2
            sv2 = S.svals(J2)
            n_massless = sum(1 for x in e0 if abs(x) < 1e-20 * scale)
            # the smooth invariants (a^2, d^2, b^2) per copy: their raw Jacobian (eigenvalues are not differentiable where a
            # copy's two singlets both vanish at zero mixing -- a cone: E4(omega) = 0 kills both singlets of copy 4)
            def inv(x):
                t_, S_ = m.point(x); A_, D_, W_ = m.pieces(t_)
                return [v for a2, d2, ww in zip(A_, D_, W_)
                        for v in (a2, d2, m.lv ** 2 * abs(sum(S_[j] * ww[j] for j in range(3))) ** 2)]
            i0 = inv(z); sci = max(abs(v) for v in i0); Ji = mp.matrix(len(i0), 6)
            for a in range(6):
                xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
                ip, im_ = inv(xp), inv(xm)
                for i in range(len(i0)):
                    Ji[i, a] = (ip[i] - im_[i]) / (2 * h) / sci
            svi = S.svals(Ji)
            # a copy's charged eigenvalues are not differentiable where disc = (a^2 - d^2)^2 + b^2 (...) = 0: a^2 = d^2, b = 0
            cone = [c for c in range(n) if abs(i0[3 * c] - i0[3 * c + 1]) <= 1e-12 * sci and i0[3 * c + 2] < 1e-20 * sci]
            rows.append(dict(point=name, max_sval_raw=float(sv[0]), rank_raw_1e9=sum(1 for v in sv if v > 1e-9),
                             massless_heavy_states=n_massless, control_off_point_max_sval=float(sv2[0]),
                             invariants_max_sval_raw=float(svi[0]), invariants_rank_1e9=sum(1 for v in svi if v > 1e-9),
                             copies_degenerate_a_eq_d_at_zero_mixing=cone,
                             control_off_point_rank=sum(1 for v in sv2 if v > 1e-9)))
        out["%s_n%d" % (menu, n)] = rows
        print(menu, n, [(r["point"], "eig-rank %d (%.1e)" % (r["rank_raw_1e9"], r["max_sval_raw"]),
                         "inv-rank %d (%.1e)" % (r["invariants_rank_1e9"], r["invariants_max_sval_raw"]),
                         "cone copies %s" % r["copies_degenerate_a_eq_d_at_zero_mixing"],
                         "off-point rank %d" % r["control_off_point_rank"]) for r in rows], flush=True)
(HERE / "analysis_points.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
