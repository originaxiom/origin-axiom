#!/usr/bin/env python3
"""POST HOC (labelled; written after the sealed run of first_row.py, prompted by its read-out tm1_W49 at omega, where two of
the four sign classes gave exactly 1/6). Question: at tau = omega, is R (B1645's closed form, mapped into B1612's
coordinates by the units' frame of first_row.py) an eigenline of rho(RL), and which one?  Also at tau = i and near the cusp.
Same instrument as first_row.py: main's banked modules at 60c5470ae, read-only via git archive.
    python3 -B post_hoc_omega.py > post_hoc_omega_run.txt 2>&1      (writes post_hoc_omega.json)
"""
import io, json, math, os, pathlib, subprocess, tarfile, tempfile, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
MAIN = "60c5470ae1747e5bd31a1a889ce38739791e0af3"
ARCS = ["frontier/B1600_the_weave_verified", "frontier/B1610_the_hands_on_the_founding_torsor",
        "frontier/B1611_is_cp_violation_forced_on_the_weave"]
TMP = pathlib.Path(tempfile.mkdtemp(prefix="first_row_posthoc_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", MAIN] + ARCS, check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
os.environ["OA_FRONTIER"] = str(TMP / "frontier")
spec = importlib.util.spec_from_file_location("cp", TMP / "frontier" / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
TB = cp.TB
AL = cp.restrict(cp.W.ML, TB); AR = cp.restrict(cp.W.MR, TB)
A_RL = cp.restrict(cp.W.MR @ cp.W.ML, TB); A_RRL = cp.restrict(cp.W.MR @ cp.W.MR @ cp.W.ML, TB)


def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])


# the invariant form (as in first_row.py, F2) and the units' frame
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
evRL, URL = np.linalg.eig(A_RL)
URL = URL / np.linalg.norm(URL, axis=0)
signs = [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]
out = {"note": "POST HOC, labelled", "RL_eigen_sigma": [sig(URL[:, k]) for k in range(3)]}
for name, t in (("omega", complex(-0.5, math.sqrt(3) / 2)), ("i", 1j), ("4i", 4j), ("8i", 8j)):
    rows = []
    for sg in signs:
        R = R_np(t); RB = sum(sg[u] * R[u] * fr[u] for u in range(3)); RB = RB / np.linalg.norm(RB)
        img = A_RL @ RB
        rows.append({"signs": sg,
                     "eigen_test_|<R,RL R>|": float(abs(np.vdot(RB, img))),
                     "overlaps_with_RL_eigenlines_(sigma)": [[float(abs(np.vdot(URL[:, k], RB)) ** 2), sig(URL[:, k])] for k in range(3)],
                     "eigen_test_|<R,L R>|": float(abs(np.vdot(RB, AL @ RB)))})
    out[name] = rows
(HERE / "post_hoc_omega.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
