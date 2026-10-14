"""Replica of post_hoc_omega.py's frame construction (lines 34-60, copied), evaluated at further tau:
which tau (if any) makes R an eigenline of rho(RL) in each sign class. argv[1] = main's extracted frontier."""
import json, math, os, sys, pathlib, importlib.util
import numpy as np
FRONT = pathlib.Path(sys.argv[1]); os.environ["OA_FRONTIER"] = str(FRONT)
spec = importlib.util.spec_from_file_location("cp", FRONT / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
TB = cp.TB
AL = cp.restrict(cp.W.ML, TB); AR = cp.restrict(cp.W.MR, TB)
A_RL = cp.restrict(cp.W.MR @ cp.W.ML, TB)

def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])

# --- copied from post_hoc_omega.py (frame construction), unchanged
SYM = []
for a in range(3):
    for b in range(a, 3):
        E = np.zeros((3, 3), dtype=complex); E[a, b] = 1; E[b, a] = 1; SYM.append(E)
SYMM = np.array([E.flatten() for E in SYM]).T
phi = lambda A: np.array([np.linalg.lstsq(SYMM, (A.T @ E @ A).flatten(), rcond=None)[0] for E in SYM]).T
PL, PR = phi(AL), phi(AR); Bf = None
for lL in np.linalg.eigvals(PL):
    for lR in np.linalg.eigvals(PR):
        _, s, Vh = np.linalg.svd(np.vstack([PL - lL * np.eye(6), PR - lR * np.eye(6)]))
        if s[-1] < 1e-9 and Bf is None:
            Bm = sum(c * E for c, E in zip(Vh[-1].conj(), SYM)); Bf = Bm / np.linalg.svd(Bm, compute_uv=False)[0]
sig = lambda w: float(abs(w @ Bf @ w) / np.vdot(w, w).real)
def axis(A):
    ev, V = np.linalg.eig(A)
    return max((V[:, k] for k in range(3)), key=sig)
fL, fR = axis(AL), axis(AR)
_, _, Vh3 = np.linalg.svd(np.vstack([fL.conj(), fR.conj()])); f3 = Vh3[-1].conj()
fr = [f / np.sqrt(f @ Bf @ f) for f in (fL, fR, f3)]
signs = [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]
# --- end of copy
w = complex(-0.5, math.sqrt(3) / 2)
out = {}
for sg in signs:
    row = {}
    for n in (-3, -2, -1, 0, 1, 2, 3):
        R = R_np(w + n); RB = sum(sg[u] * R[u] * fr[u] for u in range(3)); RB = RB / np.linalg.norm(RB)
        row[f"omega{n:+d}"] = round(float(abs(np.vdot(RB, A_RL @ RB))), 12)
    out[str(sg)] = row
print(json.dumps(out, indent=1))
