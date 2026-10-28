"""Referee B1799, check 1(c)/3: does det M vanish off the census?  D = sum c_s R_s^2 is a complex, real-analytic function of
the line (a, b) at fixed tau (and, for nucnuc, of tau alone); its zeros are generically isolated points, which a census of
torsion lines at three tau cannot see.  Located by the phase winding of D around each grid cell.
  (A) LL (-3, -3) and Lnuc (-3, 0) over (a, b) in [0, 1/3)^2 (so -3w covers the torus once) at tau = 0.37 + 2.2i;
  (B) nucnuc (0, 0) over tau in [-0.5, 0.5] x [1.3, 3.5].
Read-only; B1795's split.py path (B1723's b1656_funcs)."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
HERE = pathlib.Path(__file__).resolve().parent
NA = 36


def D_of(t, a, b, ql, qr):
    w = a * t + b; x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    vals = [abs(v) for v in c.values() if v is not None]
    D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None)
    return [D.real, D.imag, abs(D) / (max(vals) * B.nR2(R))]


def taskA(job):
    i, j = job; t = complex(0.37, 2.2); a, b = i / (3 * NA), j / (3 * NA)
    return (i, j, D_of(t, a, b, -3, -3), D_of(t, a, b, -3, 0))


def taskB(job):
    i, j, re_t, im_t = job; return (i, j, D_of(complex(re_t, im_t), 0.0, 0.0, 0, 0))


def windings(G):
    """G: complex array (n, m) on a grid; returns the cells (i, j) with non-zero winding around their boundary"""
    out = []
    for i in range(G.shape[0] - 1):
        for j in range(G.shape[1] - 1):
            loop = [G[i, j], G[i + 1, j], G[i + 1, j + 1], G[i, j + 1], G[i, j]]
            wnd = sum(np.angle(loop[k + 1] / loop[k]) for k in range(4)) / (2 * np.pi)
            if abs(wnd) > 0.5: out.append((i, j, int(round(wnd))))
    return out


if __name__ == "__main__":
    import multiprocessing as mpc
    with mpc.get_context("fork").Pool(6) as pool:
        resA = pool.map(taskA, [(i, j) for i in range(NA + 1) for j in range(NA + 1)], chunksize=8)
        re_g = np.linspace(-0.5, 0.5, 41); im_g = np.linspace(1.3, 3.5, 23)
        resB = pool.map(taskB, [(i, j, re_g[i], im_g[j]) for i in range(len(re_g)) for j in range(len(im_g))], chunksize=8)
    GL = np.zeros((NA + 1, NA + 1), complex); GD = np.zeros_like(GL); nL = np.zeros(GL.shape); nD = np.zeros(GL.shape)
    for i, j, dl, dd in resA:
        GL[i, j] = dl[0] + 1j * dl[1]; GD[i, j] = dd[0] + 1j * dd[1]; nL[i, j] = dl[2]; nD[i, j] = dd[2]
    GB = np.zeros((41, 23), complex); nB = np.zeros(GB.shape)
    for i, j, d in resB: GB[i, j] = d[0] + 1j * d[1]; nB[i, j] = d[2]
    json.dump({"LL": [[GL[i, j].real, GL[i, j].imag, nL[i, j]] for i in range(NA + 1) for j in range(NA + 1)],
               "Lnuc": [[GD[i, j].real, GD[i, j].imag, nD[i, j]] for i in range(NA + 1) for j in range(NA + 1)],
               "nucnuc_tau": [[float(re_g[i]), float(im_g[j]), GB[i, j].real, GB[i, j].imag, nB[i, j]] for i in range(41) for j in range(23)]},
              open(HERE / "r5_scan.json", "w"))
    for nm, G, n in (("LL", GL, nL), ("Lnuc", GD, nD)):
        cells = windings(G)
        print("(A) %s at tau = 0.37 + 2.2i over (a, b) in [0, 1/3)^2, grid step 1/%d: %d cells with a zero of D (winding)" % (nm, 3 * NA, len(cells)))
        for i, j, wnd in cells[:12]:
            print("    cell a in [%.4f, %.4f], b in [%.4f, %.4f], winding %+d, least Dn at its corners %.2e" % (i / (3 * NA), (i + 1) / (3 * NA), j / (3 * NA), (j + 1) / (3 * NA), wnd, n[i:i + 2, j:j + 2].min()))
    cells = windings(GB)
    print("(B) nucnuc over tau in [-0.5, 0.5] x [1.3, 3.5] (41 x 23): %d cells with a zero of D; Dn range %.2e - %.2e" % (len(cells), nB.min(), nB.max()))
    for i, j, wnd in cells[:12]:
        print("    cell Re tau in [%.3f, %.3f], Im tau in [%.3f, %.3f], winding %+d" % (re_g[i], re_g[i + 1], im_g[j], im_g[j + 1], wnd))
    print("r5 exit 0")
