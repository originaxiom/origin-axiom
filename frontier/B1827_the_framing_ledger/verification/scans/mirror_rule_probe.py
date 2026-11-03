"""P-555, data-free: the mirror rule (down at the mirror address) -- is the two-address mixing new, or forced trivial?
No measured value is read.  At random addresses: V_same = U_up(A)^H U_down(A) (the frame's own), V_mir = U_up(A)^H U_down(A*),
A* = (-conj(tau), line (alpha, -b)), same direction, radius and reading.  Reports |V| and J for both, and whether
U_down(A*) equals conj(U_down(A)) up to column phases."""
import itertools, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z


def sector_U(tau, line, d, L, r, sector):
    B = Z.mods()["B"]
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    a = Z.direction(d, tau)
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    Y = B.coupling(Sm, B.weighted_M(u))
    u_, s, _ = np.linalg.svd(Y); o = np.argsort(s)
    return u_[:, o], s[o]


def four(V):
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), J]


if __name__ == "__main__":
    rng = np.random.default_rng(555)
    dirs = [d for d in Z.DIRS if d != "F_-2"]
    print("%-16s %-8s %-6s %-5s | %-40s | %-40s | conj?" % ("line", "dir", "rad", "rd", "same |Vus| |Vcb| |Vub| J", "mirror |Vus| |Vcb| |Vub| J"))
    for trial in range(20):
        N = int(rng.integers(2, 13)); line = (F(int(rng.integers(0, N)), N), F(int(rng.integers(0, N)), N))
        tau = complex(float(rng.uniform(0.02, 0.48)), float(rng.uniform(1.2, 3.8)))
        d = dirs[int(rng.integers(len(dirs)))]; Lmax, L2 = Z.radii(tau); rad = int(rng.integers(2)); L = (Lmax, L2)[rad]
        ru, rdn = int(rng.integers(2)), int(rng.integers(2))
        Uu, su = sector_U(tau, line, d, L, ru, "up"); Ud, sd = sector_U(tau, line, d, L, rdn, "down")
        taum = complex(-tau.real, tau.imag); linem = (line[0], -line[1])
        Udm, sdm = sector_U(taum, linem, d, L, rdn, "down")
        same, mir = four(Uu.conj().T @ Ud), four(Uu.conj().T @ Udm)
        ph = np.diag(Ud.conj().T.conj() @ Udm.conj())                    # conj(Ud)^H ... phases if Udm = conj(Ud) D
        M = np.conj(Ud).conj().T @ Udm; isconj = np.allclose(np.abs(M), np.eye(3), atol=1e-6)
        same_s = np.allclose(sd, sdm, rtol=1e-8)
        print("%-16s %-8s %-6s %d%d    | %8.2e %8.2e %8.2e %+9.2e | %8.2e %8.2e %8.2e %+9.2e | %s sv=%s" % (
            "(%s,%s)" % line, d, ("Lmax", "L2")[rad], ru, rdn, *same, *mir, isconj, same_s))
