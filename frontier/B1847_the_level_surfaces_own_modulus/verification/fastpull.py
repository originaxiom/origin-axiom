"""A vectorised pullback (every point of a batch at once) for oa_harm.Group: same moves, same max-height rule, same exact
chi tracking; checked against the per-point pullback on random points."""
import numpy as np


def pullback_batch(G, Z, T, itmax=500, chunk=2000):
    Z = np.asarray(Z, dtype=complex).copy(); T = np.asarray(T, dtype=float).copy()
    lat = G.lat
    a, b, c, d = G.MA.T
    MC = np.asarray(G.MC, dtype=float)
    chi = np.zeros(len(Z))
    def reduce(Z, chi):
        X = np.vstack([Z.real, Z.imag]); n = np.round(lat.Minv @ X)
        Z = Z - (n[0] * lat.w1 + n[1] * lat.w2)
        return Z, chi - (n[0] * lat.c1 + n[1] * lat.c2)
    Z, chi = reduce(Z, chi)
    active = np.ones(len(Z), bool)
    for _ in range(itmax):
        idx = np.where(active)[0]
        if len(idx) == 0:
            break
        for k0 in range(0, len(idx), chunk):
            ii = idx[k0:k0 + chunk]
            z = Z[ii]; t = T[ii]
            w = c[None, :] * z[:, None] + d[None, :]
            D = np.abs(w) ** 2 + np.abs(c)[None, :] ** 2 * t[:, None] ** 2
            tn = t[:, None] / D
            j = np.argmax(tn, axis=1)
            r = np.arange(len(ii))
            imp = tn[r, j] > t * (1 + 1e-12)
            jj = j[imp]; rr = r[imp]
            wz = w[rr, jj]; Dz = D[rr, jj]
            zn = ((a[jj] * z[rr] + b[jj]) * np.conj(wz) + a[jj] * np.conj(c[jj]) * t[rr] ** 2) / Dz
            Z[ii[rr]] = zn; T[ii[rr]] = tn[rr, jj]; chi[ii[rr]] += MC[jj]
            active[ii[~imp]] = False
        Z, chi = reduce(Z, chi)
    return Z, T, chi
