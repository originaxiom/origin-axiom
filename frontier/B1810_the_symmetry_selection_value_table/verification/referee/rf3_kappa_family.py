"""rf3: at tau = i every listed direction except DR is a(kappa) = (1, 1, i kappa), kappa real; the reading S~ is
kappa -> -kappa.  Checks: (1) kappa per direction; (2) at (i,(1/2,1/2)) rank 2 for EVERY kappa (row1 + row2 || row3),
singular values even in kappa, and V(kappa, -kappa) from the closed form cos theta = |<n(kappa), n(-kappa)>| with n the
left null vector; (3) at (i,0) one left eigenbasis for every kappa (V a permutation for ANY pair kappa, kappa'), so
the permutations are one structural fact, not row-by-row evidence; (4) kappa -> 2/kappa at (i,(1/2,1/2)) (a0 ~ F_6)."""
import numpy as np
from rf_common import *
np.set_printoptions(precision=6, suppress=True, linewidth=160)
out = {}
for d in ("a0", "R", "t", "F_6", "F_10", "F_14", "F_22"):
    a = direction(d, I); a = a / a[0]
    print(d, "a/a_I =", np.round(a, 10), " kappa =", (a[2] / 1j).real, " 2^(a/4) check:", None if not d.startswith("F") else 2 ** (int(d[2:]) / 4))
def Yk(k, p, L): return Ymat(np.array([1, 1, 1j * k]), I, p, 1, -4, L)
def lnull(Y):
    u, s, vh = np.linalg.svd(Y); return u[:, np.argmin(s)]
for Ln, L in zip(("L_max", "L_2"), RADII[I]):
    print("== (i,(1/2,1/2))", Ln)
    for k in (2 ** -0.5, 2 ** 1.5, -2 ** 2.5, 2 ** 3.5, 2 ** 5.5, 0.3, 1.7, -5.0):
        Yp, Ym = Yk(k, (0.5, 0.5), L), Yk(-k, (0.5, 0.5), L)
        sp, sm = np.linalg.svd(Yp, compute_uv=False), np.linalg.svd(Ym, compute_uv=False)
        par = np.linalg.norm(np.cross((Yp[0] + Yp[1]), Yp[2])) / (np.linalg.norm(Yp[0] + Yp[1]) * np.linalg.norm(Yp[2]) + 1e-300)
        cth = abs(np.vdot(lnull(Yp), lnull(Ym)))
        Uu, su, _ = svd_sorted(Yp); Ud, sd, _ = svd_sorted(Ym); Vm = np.abs(Uu.conj().T @ Ud)
        sp2 = np.linalg.svd(Yk(2 / k, (0.5, 0.5), L), compute_uv=False)
        print(" kappa=%8.4f  s/s3=%s  even-in-kappa:%.1e  row1+row2 x row3: %.1e  cos(theta)=%.6f  |V|11=%.6f  kappa->2/kappa same spectrum: %.1e"
              % (k, np.round(np.sort(sp) / sp.max(), 6), np.max(abs(np.sort(sp) - np.sort(sm))) / sp.max(), par, cth, Vm[0, 0],
                 np.max(abs(np.sort(sp) / sp.max() - np.sort(sp2) / sp2.max()))))
    print("== (i,0)", Ln, ": one eigenbasis for every kappa?")
    Uref, _, _ = svd_sorted(Yk(0.3, (0, 0), L))
    worst = 0
    for k in np.linspace(-6, 6, 49):
        if abs(abs(k) - 2 ** 0.5) < 1e-9: continue
        U, s, _ = svd_sorted(Yk(k, (0, 0), L))
        if min(np.diff(s)) / s[-1] < 1e-6: continue
        A = np.abs(Uref.conj().T @ U); worst = max(worst, float(np.max(np.minimum(A, abs(1 - A)))))
    print("  max over 48 kappa of dist(|Uref^H U(kappa)|, permutation):", worst)
