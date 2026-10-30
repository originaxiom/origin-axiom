"""'Never at i or omega: stationary for every parameter but never minima' -- the draft computed the Hessian there at ONE
parameter point (mu^2 = 0.5, lambda v = 0.3, primary convention).  Here: every point of the primary grid (3 mu^2 x 3 lambda v,
m0^2 = 0.01 mu^2) and the cusp convention, menus Z and H, n = 1..8, at the four symmetric configurations; double precision,
the draft's numpy Model with the cancellation-free F, central differences (h = 1e-4) in the draft's affine chart.
-> t_sympoints.json"""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import numpy as np
import model as M, search as Sr
from t_runaway_stable import stable_F
M.Ffun = stable_F; Sr.Ffun = stable_F
from search import Model, make_copies
from model import frame_at, chart, PMAT, LINV

w = complex(-0.5, np.sqrt(3) / 2)
ev, U = np.linalg.eig(PMAT @ LINV)
PTS = [("i", 1j, np.array([1, -1, 0]) / np.sqrt(2))] + [("omega_%d" % k, w, U[:, k]) for k in range(3)]


def hess(model, tau0, S0, h=1e-4):
    e1, e2 = frame_at(S0)
    f = lambda x: model.V(*chart(x, tau0, S0, e1, e2))
    H = np.zeros((6, 6)); f0 = f(np.zeros(6))
    g = np.zeros(6)
    for a in range(6):
        xp = np.zeros(6); xp[a] = h; xm = -xp
        H[a, a] = (f(xp) - 2 * f0 + f(xm)) / h ** 2; g[a] = (f(xp) - f(xm)) / (2 * h)
        for b in range(a + 1, 6):
            vals = []
            for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                x = np.zeros(6); x[a] = sa * h; x[b] = sb * h; vals.append(f(x))
            H[a, b] = H[b, a] = (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h * h)
    return np.linalg.eigvalsh(H), g


rows = []; nmin = 0; total = 0
for tnorm, snorm, grid in (("N", "sup", [(m, l) for m in (0.3, 0.5, 0.8) for l in (0.1, 0.3, 1.0)]), ("cusp", "cusp", [(0.5, 0.3)])):
    for menu in ("Z", "H"):
        for n in range(1, 9):
            for mu2, lv in grid:
                model = Model(make_copies(n, menu, tnorm, snorm), mu2, 0.01 * mu2, lv)
                for name, tau, S in PTS:
                    e, g = hess(model, tau, S)
                    emax = max(abs(e)); neg = int(np.sum(e < -1e-6 * emax)); zero = int(np.sum(abs(e) <= 1e-6 * emax))
                    is_min = (neg == 0)
                    total += 1; nmin += is_min
                    rows.append(dict(tnorm=tnorm, menu=menu, n=n, mu2=mu2, lv=lv, point=name, n_negative=neg, n_zero=zero,
                                     min_eig=float(e[0]), max_eig=float(e[-1]), grad_inf=float(np.max(np.abs(g))), minimum_candidate=bool(is_min)))
out = dict(rows=rows, total=total, n_without_negative_direction=nmin,
           candidates=[r for r in rows if r["minimum_candidate"]])
(HERE / "t_sympoints.json").write_text(json.dumps(out, indent=1))
print("symmetric configurations checked:", total, " without a negative Hessian direction:", nmin)
for r in out["candidates"][:20]:
    print("  ", r)
