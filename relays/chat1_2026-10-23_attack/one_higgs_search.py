#!/usr/bin/env python3
"""ONE-HIGGS SEARCH (a module; data enter only through the targets passed in).  sm_search.py generalised to either
reading of one Higgs direction h on stored channel weights (B1736's closed form; c = 3 on the leptons; PRECISION_BAR's
chi2 on the natural logs of the six ratios and |V_us|, |V_cb|, |V_ub|):
  up_conj = True   the Standard Model's reading (up sees conj h, down and leptons h) - it reproduces sm_search.py;
  up_conj = False  one holomorphic direction read S in every sector (THE_NEXT_ATTACK's A1).
The direction grid is sm_search's HS (tube coordinates around the null conic plus 4 000 random directions, the same
seeds).  Added for a calibration against random targets: model_logs (the nine logs on a set of directions, computed once
per row) and chi2_many (every target's minimum chi2 over those directions, by one matrix product per chunk)."""
import contextlib, importlib.util, io, math, pathlib, sys
import numpy as np
from scipy.optimize import least_squares

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("sms", HERE / "sm_search.py"); sms = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(sms)
sys.argv = _argv
F1, F2, F3, LC, Ybatch, HS, vec, tube = sms.F1, sms.F2, sms.F3, sms.LC, sms.Ybatch, sms.HS, sms.vec, sms.tube


def model_logs(Uh, H, up_conj):
    """The nine logs (N, 9) and the CKM moduli (N, 3, 3) for directions H (N, 3; any norm)."""
    H = H / np.linalg.norm(H, axis=1)[:, None]
    Uu, su, _ = np.linalg.svd(Ybatch(Uh[0], np.conj(H) if up_conj else H)); Ud, sd, _ = np.linalg.svd(Ybatch(Uh[1], H))
    se = np.linalg.svd(Ybatch(Uh[2], H), compute_uv=False)
    L = np.empty((len(H), 9))
    for j, sv in enumerate((su, sd, se)):
        L[:, 2 * j] = np.log(np.maximum(sv[:, 1] / sv[:, 0], 1e-300)); L[:, 2 * j + 1] = np.log(np.maximum(sv[:, 2] / sv[:, 0], 1e-300))
    L[:, 4] += LC; L[:, 5] -= LC
    V = np.abs(np.einsum("nji,njk->nik", np.conj(Uu[:, :, ::-1]), Ud[:, :, ::-1]))
    L[:, 6] = np.log(np.maximum(V[:, 0, 1], 1e-300)); L[:, 7] = np.log(np.maximum(V[:, 1, 2], 1e-300)); L[:, 8] = np.log(np.maximum(V[:, 0, 2], 1e-300))
    return L, V


def nine_batch(Uh, H, T, SIG, up_conj):
    L, V = model_logs(Uh, H, up_conj)
    return L, np.sum(((L - T) / SIG) ** 2, axis=1), V


def grid_logs(Uh, up_conj, H=None):
    H = HS if H is None else H
    return np.concatenate([model_logs(Uh, H[a:a + 28200], up_conj)[0] for a in range(0, len(H), 28200)])


def chi2_many(L, R, SIG, chunk=8000):
    """For targets R (K, 9): each target's minimum chi2 over the directions whose logs are L (N, 9), and its argmin."""
    W = 1.0 / SIG ** 2
    l2 = (L * L * W).sum(1); r2 = (R * R * W).sum(1); LW = L * W
    best = np.full(len(R), np.inf); arg = np.zeros(len(R), dtype=int)
    for a in range(0, len(L), chunk):
        C = l2[a:a + chunk, None] - 2.0 * (LW[a:a + chunk] @ R.T) + r2[None, :]
        i = np.argmin(C, axis=0); v = C[i, np.arange(len(R))]
        u = v < best; best[u] = v[u]; arg[u] = i[u] + a
    return np.maximum(best, 0.0), arg


def refine(Uh, x0, T, SIG, up_conj):
    def res(x):
        L, _, _ = nine_batch(Uh, vec(x)[None], T, SIG, up_conj); return (L[0] - T) / SIG

    def jac(x):
        e = 1e-7 * max(1.0, float(np.linalg.norm(x)))
        X = np.repeat(x[None], 7, axis=0); X[1:] += e * np.eye(6)
        L, _, _ = nine_batch(Uh, X[:, :3] + 1j * X[:, 3:], T, SIG, up_conj); R = (L - T) / SIG
        return ((R[1:] - R[0]) / e).T
    try:
        r = least_squares(res, x0, jac=jac, method="trf", max_nfev=400, xtol=1e-10, ftol=1e-10)
        return float(np.sum(r.fun ** 2)), r.x
    except Exception:
        return None


def search(Uh, extra, T, SIG, up_conj, H=None, n_extra=4, chis=None):
    """sm_search.search with the reading as a parameter; chis (optional) is the grid's chi2 for T if already computed.
    Returns (the grid's minimum chi2, (the refined minimum chi2, its 6-vector x))."""
    H = HS if H is None else H
    if chis is None:
        chis = np.empty(len(H))
        for a in range(0, len(H), 28200):
            chis[a:a + 28200] = nine_batch(Uh, H[a:a + 28200], T, SIG, up_conj)[1]
    order = np.argsort(chis); keep = []
    for idx in order:
        if all(abs(np.vdot(H[j], H[idx])) < math.cos(0.05) for j in keep):
            keep.append(int(idx))
        if len(keep) == 8:
            break
    ex = [q for q in extra] + [np.conj(q) for q in extra]
    if n_extra is not None and len(ex) > n_extra:
        ce = nine_batch(Uh, np.array(ex), T, SIG, up_conj)[1]
        ex = [ex[i] for i in np.argsort(ce)[:n_extra]]
    best = (float(chis[order[0]]), np.concatenate([H[order[0]].real, H[order[0]].imag]))
    for h in [H[j] for j in keep] + ex:
        o = refine(Uh, np.concatenate([h.real, h.imag]), T, SIG, up_conj)
        if o is not None and o[0] < best[0]:
            best = o
    return float(chis[order[0]]), best
