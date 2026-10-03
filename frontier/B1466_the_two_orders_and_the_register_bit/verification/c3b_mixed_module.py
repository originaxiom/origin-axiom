#!/usr/bin/env python3
"""B1466 C3b (post-run, disclosed in the seal as the follow-up if P4 failed): the mixed deformation of S = A (+) 1 along
c1 + c2 followed to an exact flat module, at q0 and q0', and its class index.  Second order from the series (psi solving
d1 psi = -ob), then Gauss-Newton on the relator at a finite eps, minimal-norm steps; the module's commutant dimension (1 =
irreducible), its distance from W, W' and S by traces, and I by main's instrument."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import two_orders as TO
from two_orders import jo, ix, REL, PHI, TOL
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, sqrt, svd_c, nstr, norm, lu_solve
mp.dps = 60


def lstsq_min_norm(J, r):
    """minimal-norm x with J x ~ r (J wide, rank-deficient), by SVD"""
    U, S, Vh = svd_c(J)
    k = sum(1 for i in range(len(S)) if abs(S[i]) > TOL * max(1, abs(S[0])))
    x = zeros(J.cols, 1)
    for i in range(k):
        x += (U[:, i].H * r)[0] / S[i] * Vh[i, :].H
    return x, k


def relator_vec(g):
    R = jo.word(REL, g) - eye(5); return matrix([R[a, b] for a in range(5) for b in range(5)])


def jacobian(g):
    """d(relator)/d(entries of rho(m), rho(n)): 25 x 50, by the first-order series"""
    cols = []
    for k in "mn":
        for i in range(5):
            for j in range(5):
                # perturb entry (i, j) of rho(k): rho(k) -> rho(k) + h E_ij  =  rho(k)(1 + h rho(k)^-1 E_ij)
                E = zeros(5, 5); E[i, j] = 1; phi = {"m": zeros(5, 5), "n": zeros(5, 5)}; phi[k] = inverse(g[k]) * E
                M0, M1, M2 = TO.series_word(REL, g, phi); cols.append([M1[a, b] for a in range(5) for b in range(5)])
    J = matrix(25, 50)
    for j, c in enumerate(cols):
        for i in range(25): J[i, j] = c[i]
    return J


def commutant_dim(g):
    rows = []
    for k in "mn":
        for i in range(5):
            for j in range(5):
                row = [mpc(0)] * 25
                for a in range(5):
                    row[i * 5 + a] += g[k][a, j]; row[a * 5 + j] -= g[k][i, a]
                rows.append(row)
    U, S, Vh = svd_c(matrix(rows), full_matrices=True)
    return sum(1 for i in range(25) if abs(S[i]) < TOL * max(1, abs(S[0]))), nstr(abs(S[25 - 2]), 4), nstr(abs(S[25 - 1]), 4)


def traces(g, words=("m", "n", "mn", "mN", "mmn", "mnn", "mnmN")):
    return {w: nstr(sum(jo.word(w, g)[i, i] for i in range(5)), 12) for w in words}


def run_point(q, mu, label, eps=mpf("0.1")):
    g = jo.ballas(q, mu); S = TO.blockS(g)
    reps_up, _, _ = jo.cocycles(g); reps_dn, _, _ = TO.cocycles_down(g)
    c1 = {"m": matrix([reps_up[0][i] for i in range(4)]), "n": matrix([reps_up[0][4 + i] for i in range(4)])}
    c2 = {"m": matrix([[reps_dn[0][i] for i in range(4)]]), "n": matrix([[reps_dn[0][4 + i] for i in range(4)]])}
    Sinv = {k: inverse(S[k]) for k in "mn"}; N1 = {k: zeros(5, 5) for k in "mn"}; N2 = {k: zeros(5, 5) for k in "mn"}
    for k in "mn":
        for i in range(4): N1[k][i, 4] = c1[k][i]; N2[k][4, i] = c2[k][0, i]
    phi = {k: Sinv[k] * (N1[k] + N2[k]) for k in "mn"}
    # second order: psi with d1 psi = -ob
    D = TO.d1_matrix(S); M0, M1, M2 = TO.series_word(REL, S, phi); ob = matrix([M2[a, b] for a in range(5) for b in range(5)])
    psi_vec, rk = lstsq_min_norm(D, -ob)
    psi = {"m": matrix(5, 5), "n": matrix(5, 5)}
    for k_i, k in enumerate("mn"):
        for i in range(5):
            for j in range(5): psi[k][i, j] = psi_vec[k_i * 25 + i * 5 + j]
    M0, M1, M2 = TO.series_word(REL, S, phi, psi); second_order_residual = norm(matrix([M2[a, b] for a in range(5) for b in range(5)]))
    # the start at finite eps, then Gauss-Newton on the 50 entries
    g_eps = {k: S[k] * (eye(5) + eps * phi[k] + eps * eps * psi[k]) for k in "mn"}
    hist = []
    for it in range(40):
        r = relator_vec(g_eps); hist.append(nstr(norm(r), 3))
        if norm(r) < mpf(10) ** (-45): break
        J = jacobian(g_eps); dx, k = lstsq_min_norm(J, -r)
        for k_i, kk in enumerate("mn"):
            for i in range(5):
                for j in range(5): g_eps[kk][i, j] += dx[k_i * 25 + i * 5 + j]
    out = dict(label=label, eps=str(eps), second_order_residual=nstr(second_order_residual, 4), newton_residuals=hist[:6] + (["..."] if len(hist) > 6 else []) + hist[-1:],
               relator_residual=nstr(norm(relator_vec(g_eps)), 4))
    out["distance_from_S"] = nstr(max(norm(g_eps[k] - S[k]) for k in "mn"), 6)
    cd, kept, dropped = commutant_dim(g_eps); out["commutant_dim"] = cd; out["commutant_gap"] = (kept, dropped)
    W = jo.ext(g, c1); Wd = TO.ext_down(g, c2)
    out["commutant_dim_W_Wprime_S"] = [commutant_dim(W)[0], commutant_dim(Wd)[0], commutant_dim(S)[0]]
    out["traces_mixed"] = traces(g_eps); out["traces_S"] = traces(S)
    # the extension classes survive? the invariant subspaces: dim of the fixed vectors of the module and of its dual (sub 1 / quotient 1)
    def fixed_dim(M):
        rows = []
        for k in "mn":
            A = M[k] - eye(5)
            for i in range(5): rows.append([A[i, j] for j in range(5)])
        U, Sv, Vh = svd_c(matrix(rows), full_matrices=True); return sum(1 for i in range(5) if abs(Sv[i]) < TOL)
    out["invariant_line_(sub 1)"] = fixed_dim(g_eps); out["dual_invariant_line_(quotient 1)"] = fixed_dim(jo.dualrep(g_eps))
    out["same_for_W_Wprime_S"] = [(fixed_dim(M), fixed_dim(jo.dualrep(M))) for M in (W, Wd, S)]
    h, T = jo.fibred(g_eps); I, a, b = ix.index(PHI, h, T)
    out["I_mixed"] = dict(I=int(I), h0=a["h0"], h1=a["h1"], interior=a["interior"], h0_dual=b["h0"], h1_dual=b["h1"], interior_dual=b["interior"], gap=(nstr(a["gaps"][1][0], 4), nstr(a["gaps"][1][1], 4)))
    return out


def main():
    s2 = sqrt(mpf(2)); res = []
    for q, mu, label in ((17 + 12 * s2, mpc(-1), "q0 = 17 + 12 sqrt2, mu = -1"), (17 - 12 * s2, mpc(-1), "q0' = 17 - 12 sqrt2, mu = -1")):
        for eps in (mpf("0.1"), mpf("0.02")):
            r = run_point(q, mu, label, eps); res.append(r); print(json.dumps(r, indent=1, default=str), flush=True)
    json.dump(res, open(HERE / "c3b_mixed_module.json", "w"), indent=1, default=str)

if __name__ == "__main__":
    main()
