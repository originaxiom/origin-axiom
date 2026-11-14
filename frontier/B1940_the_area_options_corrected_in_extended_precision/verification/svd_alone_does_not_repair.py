"""The same T-check with the frame's 3x3 SVDs done in mpmath at 50 digits (entries as the frame computes them)."""
import sys, pathlib, time
import numpy as np, mpmath as mp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"
sys.path.insert(0, str(EB)); sys.argv = ["x"]
import fiber_grid_t90 as G
COV = G.C
mp.mp.dps = 50
_np_svd = np.linalg.svd
def mp_svd(A, full_matrices=True, compute_uv=True, **kw):
    A = np.asarray(A)
    if A.shape != (3, 3):
        return _np_svd(A, full_matrices=full_matrices, compute_uv=compute_uv)
    M = mp.matrix([[mp.mpc(complex(A[i, j])) for j in range(3)] for i in range(3)])
    U, S, Vh = mp.svd_c(M)
    order = sorted(range(3), key=lambda i: -S[i])
    s = np.array([float(S[i]) for i in order])
    if not compute_uv: return s
    Un = np.array([[complex(U[i, j]) for j in order] for i in range(3)]); Vn = np.array([[complex(Vh[j, k]) for k in range(3)] for j in order])
    return Un, s, Vn
class _LA: pass
COV.np = type(sys)("np_shim"); COV.np.__dict__.update(np.__dict__); COV.np.linalg = type(sys)("la_shim"); COV.np.linalg.__dict__.update(np.linalg.__dict__); COV.np.linalg.svd = mp_svd
KW = ["up|L_2|St", "down|L_2|S", "ckm|L_2|St|S"]
for y in [6, 9, 12, 15, 20, 30, 45]:
    t0 = time.time(); rows = []
    for x in (0.13, 1.13, -0.31):
        f = G.fbar_t90(complex(x, y)); rows.append(np.concatenate([np.array(f[k]) for k in KW]))
    rows = np.array(rows)
    td = np.max(np.abs(rows[0] - rows[1]) / np.maximum(np.abs(rows[0]), 1e-300)); xd = np.max(np.abs(rows[0] - rows[2]) / np.maximum(np.abs(rows[0]), 1e-300))
    print("y %5.1f  T-check %.1e  x-variation %.1e  W- seven: %s  (%.0f s)" % (y, td, xd, " ".join("%.4g" % v for v in rows[0]), time.time() - t0), flush=True)
