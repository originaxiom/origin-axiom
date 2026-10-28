"""Referee B1799, check 3 ('nowhere else'): det Y_D = 4 det S det M tr(eps S M^T) (B1659).  r5 scanned det M; here the
third factor, the pairing tr(eps S M^T), for the Dirac L nu^c over (a, b) in [0, 1/3)^2 at tau = 0.37 + 2.2i, readings S
and S~, horocycle L_max (M carries L through u_s = sqrt(2 pi L + c_s) R_s); zeros by phase winding, then refined by Newton
with the full spectrum checked at the root.  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
T = complex(0.37, 2.2); NA = 36
H = SP.higgs(T); LS = SP.Ls_at(2.2)


def trs(a, b):
    w = a * T + b; x, y = B.sector_twists(w, T, -3, 0); R = B.residues(x, y, T); c = B.cA(x, y, T, R); L = LS["L_max"]
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    M = B.weighted_M(u); out = []
    for rn in ("S", "St"):
        Y = B.coupling(H[rn], M); sv = np.linalg.svd(Y, compute_uv=False)
        out.append((complex(np.trace(B.EPS @ H[rn] @ M.T)), sv[2] / sv[0], np.linalg.norm(H[rn]) * np.linalg.norm(M)))
    return out


def task(job):
    i, j = job; return (i, j, trs(i / (3 * NA), j / (3 * NA)))


def windings(G):
    out = []
    for i in range(G.shape[0] - 1):
        for j in range(G.shape[1] - 1):
            loop = [G[i, j], G[i + 1, j], G[i + 1, j + 1], G[i, j + 1], G[i, j]]
            wnd = sum(np.angle(loop[k + 1] / loop[k]) for k in range(4)) / (2 * np.pi)
            if abs(wnd) > 0.5: out.append((i, j))
    return out


if __name__ == "__main__":
    import multiprocessing as mpc
    with mpc.get_context("fork").Pool(6) as pool:
        res = pool.map(task, [(i, j) for i in range(NA + 1) for j in range(NA + 1)], chunksize=8)
    for k, rn in enumerate(("S", "St")):
        G = np.zeros((NA + 1, NA + 1), complex); light = np.zeros(G.shape)
        for i, j, o in res: G[i, j] = o[k][0] / o[k][2]; light[i, j] = o[k][1]
        cells = windings(G)
        print("reading %s: %d cells with a zero of tr(eps S M^T); grid min |tr|/(|S||M|) %.2e; grid min sigma3/sigma1 %.2e" % (rn, len(cells), np.abs(G).min(), light.min()))
        for (i, j) in cells[:4]:
            a, b = (i + 0.5) / (3 * NA), (j + 0.5) / (3 * NA); h = 1e-6
            for _ in range(12):
                f = lambda a_, b_: trs(a_, b_)[k][0]
                F = f(a, b); Fa = (f(a + h, b) - F) / h; Fb = (f(a, b + h) - F) / h
                st = np.linalg.solve(np.array([[Fa.real, Fb.real], [Fa.imag, Fb.imag]]), -np.array([F.real, F.imag])); a, b = a + st[0], b + st[1]
            o = trs(a, b)[k]
            print("   root (a, b) = (%.8f, %.8f): |tr|/(|S||M|) %.1e, Dirac sigma3/sigma1 %.1e" % (a, b, abs(o[0]) / o[2], o[1]))
    print("r10 exit 0")
