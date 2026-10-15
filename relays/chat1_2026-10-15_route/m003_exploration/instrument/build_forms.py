"""LIFT (sealed: PREREGISTRATION_LIFT.md), chat1, 2026-10-15: does main's boundary-class lift (B1654) survive in the
thread frame's rank-two cells, and how large is it?

B1654 (main, PROVED): under the canonical end condition P4 the residue triplet of B1644's coupling becomes
u_r = sqrt(2 pi L + c_r(tau)) R_r, L = log(1/eps), with c_r the finite part of the channel-r boundary class's norm; under
C0's P4' (equal framed data) u = R and the zero stays. Here R -> u in the thread frame's coupling,
G(X, Y; v) = (v.Y)X + (v.X)Y - (X.Y)v, evaluated pointwise along each thread's closed geodesic:
  - c~_r = c_r - pi log Im tau (the cutoff in the unit-area coordinate; modular covariant: S and T permute the channels,
    and the common shift drops); c_r by main's own route-A code, read from main at 1d2dac43d, on a Chebyshev grid, and
    checked against the closed form c_r = -4 pi log|theta_r(0|tau)| - 2 pi ln(pi/2) (found by the pre-seal reviewer;
    evaluated here by mpmath's jtheta, a second route);
  - W72's R is -2 pi times B1654's (units i, j, k <-> channels th2, th4, th3), so delta = c~ o R in W72's basis with
    c~ ordered (c~_2, c~_4, c~_3);
  - u / sqrt(2 pi L) = R + eps delta + O(eps^2), eps = 1/(4 pi L), so the first-order lift of a rank-two cell is
    kappa = |u0^H (A Y_delta B^T) v0| / sigma_max(A Y_R B^T), u0 and v0 the null pair of A Y_R B^T; and m1/m3 -> eps kappa.
Cells: C1 = (3/2, 3/2) h 5/2; C2 = (3/2, 7/2) h 9/2 and C3 = (-1/2, 7/2) h 5/2 under the completions E4.F (c = 0),
theta^2 (c = beta) and H-ORTH; every Lyndon word of length 2..8; masses K_L^-1/2 Y (K_R^-1/2)^T.

Run once:  python3 -B lift_cells.py > lift_cells_run.txt 2>&1   (writes lift_cells.json beside itself)
"""
import importlib.util, io, json, math, os, pathlib, subprocess, sys, tarfile, tempfile, time
from fractions import Fraction
import numpy as np
import mpmath as mp
from numpy.polynomial import chebyshev as Ch
from scipy.stats import spearmanr

t0 = time.time()
HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path("<repo>")
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
MAIN = "1d2dac43d443538769fbf04ea393079623346f65"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="lift_sm_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
# main's B1654 route A (thetas, cA, R_A), unchanged, read from main and loaded as a module
src = subprocess.run(["git", "-C", str(REPO), "show",
                      f"{MAIN}:frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.py"],
                     check=True, capture_output=True, text=True).stdout
(TMP / "b1654_routeA.py").write_text(src[:src.index("# ---------------------------------------------------------------- route B")])
spec = importlib.util.spec_from_file_location("b1654_routeA", TMP / "b1654_routeA.py")
BA = importlib.util.module_from_spec(spec); spec.loader.exec_module(BA)
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS))
os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402
SU, RC = SY.SU, SY.RC
mp.mp.dps = 40
out = {"sm_seat_commit": SMC, "main_commit": MAIN, "status": "LIFT, sealed (PREREGISTRATION_LIFT.md); one run"}
print("modules loaded", round(time.time() - t0, 1), file=sys.stderr, flush=True)
K32, K72, KM12 = Fraction(3, 2), Fraction(7, 2), Fraction(-1, 2)
UNIT8 = {l: SY.E8[l] - 8 for l in SY.LINES}


def save():
    (HERE / "lift_cells.json").write_text(json.dumps(out, indent=1, default=lambda z: [z.real, z.imag]
                                                     if isinstance(z, complex) else str(z)) + "\n")


# ------------------------------------------------------------------ the forms (as theta2_completion.py builds them)
resid = {}
F32, FM12 = [], []
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8)); resid[f"{name} 3/2"] = r
    terms, r, line = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8)); resid[f"{name} -1/2"] = r
terms, r, line = SY.best_section((0, 1, 0), KM12); Rser = SY.to_series(terms, SY.E8); resid["R"] = r
fbest = None
for line in SY.LINES:
    terms, r = RC.solve((0, 0, 0), K72, line)
    if fbest is None or r < fbest[1]: fbest = (terms, r, line)
fser = SY.to_series(fbest[0], SY.E8); resid["f 7/2"] = fbest[1]
hb5 = hb9 = None
for line in ("v+", "e_i", "v-"):
    terms, r = SY.solve_twisted(Fraction(5, 2), line)
    if hb5 is None or r < hb5[1]: hb5 = (terms, r, line)
    terms, r = SY.solve_twisted(Fraction(9, 2), line)
    if hb9 is None or r < hb9[1]: hb9 = (terms, r, line)
h5, h9 = SY.to_series(hb5[0], SY.E8P), SY.to_series(hb9[0], SY.E8P)
resid["h 5/2"], resid["h 9/2"] = hb5[1], hb9[1]
out["residuals"] = resid
print("forms built", round(time.time() - t0, 1), file=sys.stderr, flush=True)

CAP = SY.CAP8 // 8
sig = lambda m, p: sum(d ** p for d in range(1, m + 1) if m % d == 0)
E4 = {0: mp.mpf(1)}; E4.update({8 * m: mp.mpf(240 * sig(m, 3)) for m in range(1, CAP + 1)})
E2 = {0: mp.mpf(1)}; E2.update({8 * m: mp.mpf(-24 * sig(m, 1)) for m in range(1, CAP + 1)})


def serre(X, k):
    D = {key: (mp.mpf(key[1]) / 8) * a for key, a in X.items()}
    return SY.add((1, D), (-mp.mpf(k.numerator) / (12 * k.denominator), SY.scal_vec(E2, X)))


EI = ("e_i", 1)
E4F = [SY.scal_vec(E4, F) for F in FM12]
beta, beta_mp = [], []
for j, l in enumerate(("e_i", "v+", "v-")):
    th2 = serre(serre(FM12[j], KM12), K32)
    u2 = th2.get((l, UNIT8[l]))
    th2 = {k: v / u2 for k, v in th2.items()}
    b_mp = (th2.get(EI, 0) - E4F[j].get(EI, 0)) / fser.get(EI)
    beta_mp.append(b_mp); beta.append(complex(b_mp))
out["Q(d) beta (theta^2 = E4 F + beta f)"] = beta
q_beta = float(max(abs(b - t) / abs(t) for b, t in zip(beta_mp, (-224, -4, -112))))   # compared in mpmath


import pickle
pickle.dump({"F32": F32, "FM12": FM12, "E4F": E4F, "fser": fser, "Rser": Rser, "h5": h5, "h9": h9,
             "beta": beta, "resid": resid}, open(HERE / "forms.pkl", "wb"))
print("pickled", round(time.time() - t0, 1), file=sys.stderr, flush=True)
